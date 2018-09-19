import random

from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from pirates.creature.DistributedAnimalAI import DistributedAnimalAI
from pirates.npc.DistributedNPCTownfolkAI import DistributedNPCTownfolkAI
from pirates.npc.DistributedNPCSkeletonAI import DistributedNPCSkeletonAI
from pirates.npc.DistributedNPCNavySailorAI import DistributedNPCNavySailorAI
from pirates.npc.DistributedBossSkeletonAI import DistributedBossSkeletonAI
from pirates.npc.DistributedBossNavySailorAI import DistributedBossNavySailorAI
from pirates.npc import BossNPCList
from pirates.creature.DistributedCreatureAI import DistributedCreatureAI
from pirates.creature.DistributedBossCreatureAI import DistributedBossCreatureAI
from pirates.creature.DistributedSeagullAI import DistributedSeagullAI
from pirates.piratesbase import PiratesGlobals
from pirates.pirate.AvatarType import AvatarType
from pirates.pirate import AvatarTypes
from pirates.leveleditor import NPCList
from pirates.piratesbase import PLocalizer
from pirates.battle import EnemyGlobals
from pirates.ai import HolidayGlobals
from pirates.quest.QuestConstants import NPCIds


class SpawnNodeBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SpawnNodeBase')

    def __init__(self, air, objType, objectData, parent, objKey):
        self.air = air

        self._objType = objType
        self._objectData = objectData
        self._parent = parent
        self._objKey = objKey
        self._npc = None

        # allow our logger to send notify messages...
        self.notify.setInfo(True)

    @property
    def objType(self):
        return self._objType

    @property
    def objectData(self):
        return self._objectData

    @property
    def parent(self):
        return self._parent

    @property
    def objKey(self):
        return self._objKey

    @property
    def npc(self):
        return self._npc

    def getAvatarType(self):
        raise NotImplementedError('%s does not extend getAvatarType!' % \
            self.__class__.__name__)

    def setNPCAttributes(self, npc):
        pass

    def getNPCClass(self, avatarType):
        raise NotImplementedError('%s does not extend getNPCClass!' % \
            self.__class__.__name__)

    def setup(self):
        # spawn the initial avatar...
        self.__attemptSpawn()

    def processDeath(self):
        if not self._npc:
            self.notify.debug('Attempted to perform death on a %s without a npc!' % \
                self.__class__.__name__)

            return

        taskMgr.doMethodLater(5, self.__respawn, 'perform-respawn-%s' % self.objKey)

    def canRespawn(self):
        holidayName = self.objectData.get('Holiday', None)
        if holidayName:
            holidayId = HolidayGlobals.getHolidayIdFromName(holidayName)
            if holidayId:
                return self.air.newsManager.isHolidayActive(holidayId)

        return True

    def processHolidayStart(self, holidayId):
        if self._npc:
            return

        if self.canRespawn():
            self.__attemptSpawn()

    def processHolidayEnd(self, holidayId):
        if not self._npc:
            return

        if not self.canRespawn():
            self.__died(self._npc)

    def __respawn(self, task):
        if not self._npc:
            self.notify.warning('Attempted to perform respawn on a %s without a npc!' % \
                self.__class__.__name__)

            return

        self._npc.requestDelete()
        self._npc = None

        respawns = self.objectData.get('Respawns', True)
        if not respawns:
            #TODO: is this the proper way of handling this?
            removeSpawnNode(self.objType, self)
            return

        #TODO: Is this a constant?
        spawnTimer = 20
        taskMgr.doMethodLater(spawnTimer, self.__spawn, 'perform-spawn-%s' % self.objKey)

        return task.done

    def getNPCTeam(self, avatarType):
        if avatarType.isA(AvatarTypes.Navy):
            return PiratesGlobals.NAVY_TEAM
        elif avatarType.isA(AvatarTypes.TradingCo):
            return PiratesGlobals.TRADING_CO_TEAM
        elif avatarType.isA(AvatarTypes.Undead):
            if avatarType.isA(AvatarTypes.French):
                return PiratesGlobals.FRENCH_UNDEAD_TEAM
            elif avatarType.isA(AvatarTypes.Spanish):
                return PiratesGlobals.SPANISH_UNDEAD_TEAM
            else:
                return PiratesGlobals.UNDEAD_TEAM
        elif avatarType.isA(AvatarTypes.Creature):
            return PiratesGlobals.UNDEAD_TEAM
        elif avatarType.isA(AvatarTypes.Townfolk):
            return PiratesGlobals.VILLAGER_TEAM
        else:
            return PiratesGlobals.PLAYER_TEAM

    def __attemptSpawn(self, task=None):
        if not self.canRespawn():
            return

        self.__spawn()
        return Task.done

    def __spawn(self, task=None):
        # Create the npc class
        avatarType = self.getAvatarType()
        npcCls = self.getNPCClass(avatarType)
        if npcCls is None:
            self.notify.warning('No NPC class defined for AvatarType: %s' % avatarType)
            return

        npc = npcCls(self.air)

        # Set NPC Node data
        npc.setScale(self.objectData.get('Scale'))
        npc.setUniqueId('' if avatarType.getBoss() else self.objKey)
        npc.setPos(self.objectData.get('Pos', (0, 0, 0)))
        npc.setHpr(self.objectData.get('Hpr', (0, 0, 0)))
        npc.setSpawnPosHpr(npc.getPos(), npc.getHpr())
        npc.setInitZ(npc.getZ())
        npc.setTeam(self.getNPCTeam(avatarType))

        npc.setAvatarType(avatarType)
        npc.setAggroRadius(float(self.objectData.get('Aggro Radius', 0.0)))

        # Load boss data if applicable
        if avatarType.getBoss() and hasattr(npc, 'loadBossData'):
            bossId = self.objKey if self.objType != 'Spawn Node' else npc.getUniqueId()
            npc.loadBossData(bossId, avatarType)

        # Set NPC health
        if hasattr(npc, 'bossData'):
            npc.setLevel(npc.bossData.get('Level', 0) or EnemyGlobals.getRandomEnemyLevel(
                avatarType))
        else:
            npc.setLevel(EnemyGlobals.getRandomEnemyLevel(avatarType))

        npcHp, npcMp = EnemyGlobals.getEnemyStats(avatarType, npc.getLevel())
        if avatarType.getBoss() and hasattr(npc, 'bossData'):
            npcHp = npcHp * npc.bossData['HpScale']
            npcMp = npcMp * npc.bossData['MpScale']

        npc.setMaxHp(npcHp)
        npc.setHp(npc.getMaxHp(), True)

        npc.setMaxMojo(npcMp)
        npc.setMojo(npc.getMaxMojo())

        # Set custom spawner based attributes
        self.setNPCAttributes(npc)

        # Set NPC DNA if applicable
        dnaId = self.objKey
        if hasattr(npc, 'setDNAId'):
            if self.objectData.get('CustomModel', 'None') != 'None':
                npc.setDNAId(self.objectData.get('CustomModel', ''))
            elif dnaId:
                npc.setDNAId(dnaId)

        # Name the NPC
        name = avatarType.getName()
        if dnaId and dnaId in NPCList.NPC_LIST:
            name = NPCList.NPC_LIST[dnaId][NPCList.setName]
        if dnaId == NPCIds.ELIZABETH:
            name = 'Elizabeth Swann'
        elif dnaId == NPCIds.BARBOSSA:
            name = 'Captain Barbossa'

        if hasattr(npc, 'bossData'):
            name = npc.bossData.get('Name', PLocalizer.Unknown)
        elif avatarType.getBoss():
            name = PLocalizer.BossNames[avatarType.faction][avatarType.track][avatarType.id][avatarType.boss]

        npc.setName(name)

        # Set starting state info
        npc.setAnimSet(npc.getAnimSet()) # TODO: This isn't proper but it'll force them into an idle state instead of them t-posing
        npc.setStartState(self.objectData.get('Start State', 'Idle'))

        # Generate npc
        zoneId = self.parent.getZoneFromXYZ(npc.getPos())
        self.parent.generateChildWithRequired(npc, zoneId)
        self.parent.builder.parentObjectToCell(npc, zoneId)
        self.parent.builder.addObject(npc)

        npc.d_setInitZ(npc.getZ())
        npc.d_setSpawnIn()

        # Save a copy of the npc and tell it about myself. This will come in handy
        self._npc = npc
        npc.setSpawner(self)

        # Print out useful debugging information
        locationName = self.parent.getLocalizerName()
        self.notify.debug('Generating %s (%s) under zone %d on %s at %s with doId %d' % (npc.getName(), self.objKey,
            npc.zoneId, locationName, npc.getPos(), npc.doId))

        if avatarType.getBoss():
            self.notify.info('Spawning boss %s (%s) on %s!' % (npc.getName(), self.objKey, locationName))

        return Task.done

class TownfolkSpawnNode(SpawnNodeBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownfolkSpawnNode')

    def getAvatarType(self):
        category = self.objectData.get('Category', '')
        if not hasattr(AvatarTypes, category):
            self.notify.warning('Failed to spawn Townfolk (%s); Unknown category %s' % (self.objKey, category))
            return
        return getattr(AvatarTypes, category, AvatarTypes.Commoner)

    def setNPCAttributes(self, npc):
        shopId = self.objectData.get('ShopID', 'PORT_ROYAL_DEFAULTS')
        if not hasattr(PiratesGlobals, shopId):
            self.notify.warning('Failed to spawn Townfolk (%s); Unknown shopId: %s' % (self.objKey, shopid))
        npc.setShopId(getattr(PiratesGlobals, shopId, 0))

        helpId = self.objectData.get('HelpID', 'NONE')
        if hasattr(PiratesGlobals, helpId):
            npc.setHelpId(getattr(PiratesGlobals, helpId, 0))

    def getNPCClass(self, avatarType):
        return DistributedNPCTownfolkAI

class EnemySpawnNode(SpawnNodeBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('EnemySpawnNode')

    def __init__(self, *args, **kwargs):
        self.wantRandomBosses = config.GetBool('want-random-bosses', True)
        self.randomBossChance = config.GetInt('random-boss-spawn-change', 5)

        SpawnNodeBase.__init__(self, *args, **kwargs)

    def getAvatarType(self):
        spawnable = self.objectData.get('Spawnables', '')
        species = self.objectData.get('Species', '')
        if spawnable not in AvatarTypes.NPC_SPAWNABLES:
            if species == 'Monkey':
                return AvatarTypes.Monkey

            self.notify.warning('Failed to spawn %s (%s); Not a valid spawnable.' % (spawnable, self.objKey))
            return AvatarTypes.FrenchUndeadA

        avatarType = random.choice(AvatarTypes.NPC_SPAWNABLES[spawnable])()
        bossType = avatarType.getRandomBossType()

        # Attempt to pick a RNG boss type
        if bossType and self.wantRandomBosses:
            if random.randint(1, 100) <= self.randomBossChance:
                if bossType not in self.air.enemySpawner.randomBosses:
                    self.air.enemySpawner.randomBosses.append(bossType)
                    avatarType = bossType
            elif config.GetBool('force-random-bosses', False):
                if bossType not in self.air.enemySpawner.randomBosses:
                    self.air.enemySpawner.randomBosses.append(bossType)
                    avatarType = bossType

        return avatarType

    def setNPCAttributes(self, npc):
        weapons = EnemyGlobals.getEnemyWeapons(npc.getAvatarType(), npc.getLevel()).keys()

        #TODO: Better place to add this?
        drawnAnimSets = ['attention']
        defaultDrawn = True if self.objectData.get('AnimSet', '') in drawnAnimSets else False
        npc.setCurrentWeapon(random.choice(weapons), config.GetBool('want-enemy-weapons', defaultDrawn))

    def getNPCClass(self, avatarType):
        enemyCls = None

        if avatarType.isA(AvatarTypes.Undead):
            if avatarType.getBoss():
                enemyCls = DistributedBossSkeletonAI
            else:
                enemyCls = DistributedNPCSkeletonAI
        elif avatarType.isA(AvatarTypes.TradingCo) or avatarType.isA(AvatarTypes.Navy):
            if avatarType.getBoss():
                enemyCls = DistributedBossNavySailorAI
            else:
                enemyCls = DistributedNPCNavySailorAI
        elif avatarType.isA(AvatarTypes.LandCreature) or avatarType.isA(AvatarTypes.AirCreature):
            if avatarType.getBoss():
                enemyCls = DistributedBossCreatureAI
            else:
                enemyCls = DistributedCreatureAI
        else:
            self.notify.warning('Received unknown AvatarType: %s' % avatarType)

        return enemyCls

class AnimalSpawnNode(SpawnNodeBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('AnimalSpawnNode')

    def getAvatarType(self):
        species = self.objectData.get('Species', None)
        if not species:
            self.notify.warning('Failed to generate Animal %s; Species was not defined' % self._objKey)
            return

        if not hasattr(AvatarTypes, species):
            self.notify.warning('Failed to generate Animal %s; %s is not a valid species' % (self._objKey, species))
            return
        return getattr(AvatarTypes, species, AvatarTypes.Chicken)

    def getNPCClass(self, avatarType):
        animalClass = DistributedAnimalAI
        if avatarType == AvatarTypes.Seagull:
            animalClass = DistributedSeagullAI
        return animalClass

class BossEnemySpawnNode(EnemySpawnNode):

    def getAvatarType(self):
        avId = self.objectData.get('AvId', 1)
        avTrack = self.objectData.get('AvTrack', 0)

        faction = AvatarTypes.Undead.faction
        if self.objType == 'Creature':
            faction = AvatarTypes.Creature.faction
        elif self.objType == 'NavySailor':
            faction = AvatarTypes.Navy.faction

        avatarType = AvatarType(faction=faction, track=avTrack, id=avId)
        return avatarType.getBossType()

class DistributedEnemySpawnerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEnemySpawnerAI')
    notify.setInfo(True)

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.randomBosses = []
        self.spawnNodes = {}

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        self.accept('HolidayStarted', self.__processHolidayStart)
        self.accept('HolidayEnded', self.__processHolidayEnd)

    def delete(self):
        DistributedObjectAI.delete(self)

        self.ignore('HolidayStarted')
        self.ignore('HolidayEnded')

    def __processHolidayStart(self, holidayId):
        for spawnNodeKey in self.spawnNodes:
            spawnNodes = self.spawnNodes[spawnNodeKey]
            for spawnNode in spawnNodes:
                spawnNode.processHolidayStart(holidayId)

    def __processHolidayEnd(self, holidayId):
        for spawnNodeKey in self.spawnNodes:
            spawnNodes = self.spawnNodes[spawnNodeKey]
            for spawnNode in spawnNodes:
                spawnNode.processHolidayEnd(holidayId)

    def getSpawnNodesFromType(self, type):
        if type not in self.spawnNodes:
            return []

        return self.spawnNodes[type]

    def getSpawnNodeFromTypeAndKey(self, type, key):
        spawns = self.getSpawnNodesFromType(type)
        found = None
        for spawn in spawns:
            if spawn.objkey == key:
                found = spawn
                break

        return found

    def removeSpawnNode(self, type, spawnNode):
        if not type in self.spawnNodes:
            return

        self.spawnNodes[type].remove(spawnNode)

    def __registerSpawnNode(self, type, spawnNode):
        if not self.getSpawnNodesFromType(type):
            self.spawnNodes[type] = []

        self.spawnNodes[type].append(spawnNode)

    def createObject(self, objType, objectData, parent, parentUid, objKey, dynamic):
        newObj = None

        spawnClasses = {
            'Townsperson': TownfolkSpawnNode,
            'Spawn Node': EnemySpawnNode,
            'Dormant NPC Spawn Node': EnemySpawnNode,
            'Animal': AnimalSpawnNode,
            'Skeleton': BossEnemySpawnNode,
            'NavySailor': BossEnemySpawnNode,
            'Creature': BossEnemySpawnNode
        }

        if objType not in spawnClasses:
            self.notify.warning('Received unknown generate: %s' % objType)
            return

        # check to see if we have any explicit objects that need
        # to be generated in some other way...
        if objType == 'Animal':
            if objectData['Species'] == 'Monkey':
                objType = 'Spawn Node'

        spawnClass = spawnClasses[objType]
        spawnNode = spawnClass(self.air, objType, objectData, parent, objKey)

        # check to see if we want enemies or not since alpha will
        # not introduce killable enemies yet...
        if isinstance(spawnNode, EnemySpawnNode) and config.GetBool('want-alpha-blockers', False):
            return

        spawnNode.setup()
        self.__registerSpawnNode(objType, spawnNode)
        return newObj
