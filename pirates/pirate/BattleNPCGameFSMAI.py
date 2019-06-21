import random

from panda3d.core import *

from direct.distributed.ClockDelta import *
from direct.showbase import PythonUtil
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.GridParent import GridParent

from pirates.battle import EnemyGlobals
from pirates.pirate.BattleAvatarGameFSMAI import BattleAvatarGameFSMAI
from pirates.movement import MotionFSM
from pirates.battle import WeaponGlobals
from pirates.battle.EnemySkills import EnemySkills
from pirates.pirate import AvatarTypes


class BattleNPCGameFSMAI(BattleAvatarGameFSMAI):
    notify = directNotify.newCategory('BattleNPCGameFSMAI')

    def __init__(self, air, avatar):
        BattleAvatarGameFSMAI.__init__(self, air, avatar)

        self.__movementInterval = None
        self.__pausedTask = None
        self.__updateBattleStateTask = None
        self.__nextAttackTask = None
        self.__chaseTargetTask = None

        # update our game state as we change it
        self.setBroadcastStateChanges(True)
        self.accept(self.getStateChangeEvent(), self.__updateGameState)

    def __updateGameState(self):
        self.avatar.d_setGameState(self.getCurrentOrNextState())

    def getPatrolRadius(self):
        return float(self.avatar.spawnNode.objectData.get('Patrol Radius', 0.0))

    def getPauseChance(self):
        return float(self.avatar.spawnNode.objectData.get('Pause Chance', 50.0))

    def getPauseDuration(self):
        return float(self.avatar.spawnNode.objectData.get('Pause Duration', 15.0))

    def shouldFollowTarget(self, attackTarget):
        if not attackTarget:
            return False

        distance = self.avatar.getDistance(attackTarget)
        return distance > EnemyGlobals.INSTANT_AGGRO_RADIUS_DEFAULT / 2

    def getPatrolPoint(self):
        parentObj = self.avatar.getParentObj()
        if not parentObj:
            return None

        patrolRadius = self.getPatrolRadius()
        if patrolRadius == 0.0:
            return None

        sx, sy, sz = self.avatar.getSpawnPos()
        x = random.uniform(sx - patrolRadius, sx + patrolRadius)
        y = random.uniform(sy - patrolRadius, sy + patrolRadius)
        return Point3(x, y, sz)

    def getWalkToPointDoneName(self):
        return self.avatar.uniqueName('walkToPoint-done')

    def getWalkToPointPausedName(self):
        return self.avatar.uniqueName('walkToPoint-paused')

    def getUpdateBattleStateTaskName(self):
        return self.avatar.taskName('update-battle-state')

    def getNextAttackTaskName(self):
        return self.avatar.taskName('next-attack')

    def getChaseTargetTaskName(self):
        return self.avatar.taskName('chase-target')

    def getAttackDelayModdifier(self):
        delayInfo = [
            WeaponGlobals.NO_DELAY,
            WeaponGlobals.SHORT_DELAY,
            WeaponGlobals.MED_DELAY,
            WeaponGlobals.LONG_DELAY]

        return random.choice(delayInfo)

    def getNewAttackTarget(self):
        attackTargetDoId = self.air.targetMgr.findTargetableObject(self.avatar.doId)
        if not attackTargetDoId:
            return None

        return self.air.doId2do.get(attackTargetDoId)

    def getDistFromSpawnNode(self):
        spawnNodeNP = NodePath('spawnNode-%d' % self.avatar.doId)
        spawnNodeNP.setPos(*self.avatar.getSpawnPos())
        return self.avatar.getDistance(spawnNodeNP)

    def _drawWeapon(self):
        if not self.avatar.isWeaponDrawn:
            self.avatar.b_setCurrentWeapon(self.avatar.currentWeaponId, 1)

    def _putAwayWeapon(self):
        self.avatar.b_setCurrentWeapon(self.avatar.currentWeaponId, 0)

    def _chooseNextAttack(self, task):
        # choose a random skill to attack the player with
        baseSkills = EnemyGlobals.getBaseSkills(self.avatar.avatarType)
        skillList = baseSkills[1]
        skillId = random.choice(skillList)

        areaIdList = self.air.targetMgr.getAttackers(self.avatar.doId)
        timestamp = globalClockDelta.getRealNetworkTime(bits=16)
        self.avatar.useTargetedSkill(self.avatar, self.avatar.currentTarget, skillId, 0, areaIdList, timestamp, self.avatar.getPos(), 0)

        # get the total delay on how long it will take the enemy to
        # use this attack, once the enemy has completed it's attack,
        # select another attack until this loop is broken...
        delay = WeaponGlobals.getAttackDelay(skillId)
        delay += WeaponGlobals.getAttackDuration(skillId)
        delay += self.getAttackDelayModdifier()

        # update our task delay
        task.setDelay(delay)
        return task.again

    def beginAttackingTarget(self):
        self.__nextAttackTask = taskMgr.doMethodLater(WeaponGlobals.SHORT_DELAY, self._chooseNextAttack, self.getNextAttackTaskName())

    def _chaseTarget(self, task):
        self.findNextWalkToPoint()
        return task.done

    def beginChasingTarget(self):
        # we setup a task for this because we do not want to block
        # the state call with an infinite recursive loop...
        self.__chaseTargetTask = taskMgr.add(self._chaseTarget, self.getChaseTargetTaskName())

    def findNextWalkToPoint(self):
        state = self.getCurrentOrNextState()
        if state == 'Patrol' or state == 'Walk':
            patrolPoint = self.getPatrolPoint()
            if not patrolPoint:
                self.notify.warning('Could not find patrol point for NPC with doId: %d' % self.avatar.doId)

                # since we couldn't find an attack target, we cannot just do nothing;
                # instead let's just set our current state to our starting state.
                self.demand(self.avatar.getStartState())
                return

            pauseDuration = random.uniform(1.0, self.getPauseDuration())
            self.__pausedTask = taskMgr.doMethodLater(pauseDuration, self.walkToPoint, self.getWalkToPointPausedName(),
                extraArgs=[patrolPoint], appendTask=False)
        elif state == 'AttackChase':
            currentTarget = self.avatar.currentTarget
            if not currentTarget:
                self.demand('BreakCombat')
                return

            spawnNodeDistance = self.getDistFromSpawnNode()
            if spawnNodeDistance > EnemyGlobals.AGGRO_RADIUS_TOLERANCE:
                # we've went too far away from our spawn node, walk us back to our spawn node,
                # then set our default state and wait for a new battle...
                self.request('BreakCombat')
                return

            shouldFollowTarget = self.shouldFollowTarget(currentTarget)
            if not shouldFollowTarget:
                # we've arrived at the walk point and the attacker hasn't gone
                # outside our aggro radius, let's begin attacking the avatar...
                self.request('Battle')
                return

            self.walkToPoint(currentTarget.getPos(), currentTarget.getParent())
        elif state == 'BreakCombat':
            self.request(self.avatar.getStartState())

    def walkToPoint(self, walkPoint, parent=None):
        if not parent or parent.isEmpty():
            parent = self.avatar.getParentObj()

        # setup a node applying the walkPoint relative to the parent
        # parameter provided by this function, this allows us to properly
        # face towards the correct location even across the cartesian grid...
        walkPointNode = NodePath('walkPoint-%d' % self.avatar.doId)
        walkPointNode.setPos(parent, walkPoint)

        self.avatar.lookAt(walkPointNode)

        self.acceptOnce(self.getWalkToPointDoneName(), self.findNextWalkToPoint)
        walkSpeed = MotionFSM.WALK_CUTOFF * 2

        self.__movementInterval = self.avatar.posInterval(walkSpeed, walkPoint, other=parent)
        self.__movementInterval.setDoneEvent(self.getWalkToPointDoneName())
        self.__movementInterval.start()

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterPatrol(self, *args, **kwargs):
        self.findNextWalkToPoint()

    def exitPatrol(self):
        if self.__movementInterval:
            self.__movementInterval.finish()
            self.__movementInterval = None

        if self.__pausedTask:
            taskMgr.remove(self.__pausedTask)
            self.__pausedTask = None

    def enterWalk(self):
        self.findNextWalkToPoint()

    def exitWalk(self):
        if self.__movementInterval:
            self.__movementInterval.finish()
            self.__movementInterval = None

        if self.__pausedTask:
            taskMgr.remove(self.__pausedTask)
            self.__pausedTask = None

    def __updateBattleState(self, task):
        currentTarget = self.avatar.currentTarget
        if not currentTarget:
            self.demand('BreakCombat')
            return task.done

        shouldFollowTarget = self.shouldFollowTarget(currentTarget)
        if shouldFollowTarget and (self.avatar.avatarType not in [AvatarTypes.FlyTrap, AvatarTypes.Monkey]):
            state = self.getCurrentOrNextState()
            if state == 'Battle':
                self.request('AttackChase')
                return task.done

            self.findNextWalkToPoint()

        # check to see if the target goes out of range of us,
        # this is mostly useful for fly traps (which don't move).
        distanceFromTarget = self.avatar.getDistance(currentTarget)
        if distanceFromTarget > EnemyGlobals.AGGRO_RADIUS_TOLERANCE:
            # the player has went too far away, walk us back to our spawn node,
            # then set our default state and wait for a new battle...
            self.request('BreakCombat')
            return task.done

        return task.cont

    def enterAmbush(self):
        pass

    def exitAmbush(self):
        pass

    def enterBattle(self):
        if not self.avatar.currentTarget:
            attackTarget = self.getNewAttackTarget()
            assert(attackTarget is not None)
            self.avatar.b_setCurrentTarget(attackTarget.doId)

        self.avatar.startLookAt()

        # update our anim state
        self.avatar.b_setAnimSet('default')

        # draw our weapon
        self._drawWeapon()

        # start attacking our target
        self.beginAttackingTarget()
        self.__updateBattleStateTask = taskMgr.add(self.__updateBattleState, self.getUpdateBattleStateTaskName())

    def filterBreakCombat(self, request, args=[]):
        # the monkey cannot attack anyone, as it does not have a weapon or skills...
        if request == 'Battle' and self.avatar.avatarType == AvatarTypes.Monkey:
            return

        return self.defaultFilter(request, args)

    def exitBattle(self):
        if self.__updateBattleStateTask:
            taskMgr.remove(self.__updateBattleStateTask)
            self.__updateBattleStateTask = None

        if self.__nextAttackTask:
            taskMgr.remove(self.__nextAttackTask)
            self.__nextAttackTask = None

        self.avatar.stopLookAt()

    def enterAttackChase(self, *args, **kwargs):
        assert(self.avatar.currentTarget is not None)
        self.avatar.startLookAt()

        # start attacking our target
        self.beginAttackingTarget()
        print ('enterAttackChase', 'beginAttackingTarget')

        # begin following our target
        self.beginChasingTarget()
        self.__updateBattleStateTask = taskMgr.add(self.__updateBattleState, self.getUpdateBattleStateTaskName())

    def exitAttackChase(self):
        if self.__chaseTargetTask:
            taskMgr.remove(self.__chaseTargetTask)
            self.__chaseTargetTask = None

        if self.__movementInterval:
            self.__movementInterval.finish()
            self.__movementInterval = None

        if self.__updateBattleStateTask:
            taskMgr.remove(self.__updateBattleStateTask)
            self.__updateBattleStateTask = None

        if self.__nextAttackTask:
            taskMgr.remove(self.__nextAttackTask)
            self.__nextAttackTask = None

        self.avatar.stopLookAt()

    def enterBreakCombat(self):
        self.avatar.b_setCurrentTarget(0)

        # put away our weapon
        self._putAwayWeapon()

        # walk us back to our spawn point then set our default state.
        self.walkToPoint(Point3(*self.avatar.getSpawnPos()))

    def filterBreakCombat(self, request, args=[]):
        if request == 'advance':
            return 'LandRoam'

        if request == 'Battle':
            return

        return self.defaultFilter(request, args)

    def exitBreakCombat(self):
        # update our anim state
        spawnNode = self.avatar.getSpawnNode()
        self.avatar.b_setAnimSet(spawnNode.objectData.get('AnimSet', 'default'))

    def enterDeath(self, *args, **kwargs):
        self.air.battleMgr.rewardAttackers(self.avatar)
        self.avatar.spawnNode.processDeath()

    def exitDeath(self):
        pass
