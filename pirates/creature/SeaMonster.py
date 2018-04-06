# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.creature.SeaMonster
import copy
import random

from direct.actor import Actor
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *
from otp.avatar import Avatar
from otp.otpbase import OTPGlobals, OTPRender
from pandac.PandaModules import *
from pirates.battle import EnemyGlobals
from pirates.effects.JRDeathEffect import JRDeathEffect
from pirates.effects.JRSpiritEffect import JRSpiritEffect
from pirates.effects.ShockwaveRing import ShockwaveRing
from pirates.effects.UsesEffectNode import UsesEffectNode
from pirates.movement.AnimationMixer import AnimationMixer
from pirates.movement.UsesAnimationMixer import UsesAnimationMixer
from pirates.pirate import AvatarTypes
from pirates.pirate.AvatarType import AvatarType
from pirates.piratesbase import PiratesGlobals

WALK_CUTOFF = 0.5
ADVANCE_CUTOFF = 0.5
RUN_CUTOFF = PiratesGlobals.ToonForwardSpeed

class SeaMonster(UsesAnimationMixer, Avatar.Avatar, UsesEffectNode):
    __module__ = __name__
    FailsafeAnims = (('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0), ('idle', 1.0))
    SfxNames = {'death': 'bodyFall-08.mp3'}
    sfx = {}
    actor = None
    animInfo = {}

    class AnimationMixer(AnimationMixer):
        __module__ = __name__
        LOOP = AnimationMixer.LOOP
        ACTION = dict(AnimationMixer.ACTION)
        ACTION['MOVIE'] = AnimationMixer.ACTION_INDEX + 1

    def __init__(self, animationMixer=None):
        Avatar.Avatar.__init__(self)
        UsesEffectNode.__init__(self)
        self.setPickable(0)
        self.shadowFileName = 'models/misc/drop_shadow'
        self.nameText = None
        self.avatarType = None
        if not SeaMonster.sfx:
            for name in SeaMonster.SfxNames:
                SeaMonster.sfx[name] = loader.loadSfx('audio/' + SeaMonster.SfxNames[name])

        OTPRender.renderReflection(False, self, 'p_creature', None)
        animationMixer = self.AnimationMixer
        UsesAnimationMixer.__init__(self, animationMixer)
        return

    def delete(self):
        Avatar.Avatar.delete(self)

    def forceLoadAnimDict(self):
        for anim in self.animDict:
            self.getAnimControls(anim)

    def generateSeaMonster(self):
        if self.actor:
            self.copyActor(self.actor)

    def setAvatarType(self, avatarType):
        if self.avatarType:
            self.initializeNametag3d()
            return
        else:
            self.avatarType = avatarType
            self.height = EnemyGlobals.getHeight(avatarType)
            self.initializeDropShadow()
            self.initializeNametag3d()

    def initializeNametag3d(self):
        if self.avatarType.isA(AvatarType(base=AvatarTypes.Animal)):
            return
        Avatar.Avatar.initializeNametag3d(self)
        self.nametag3d.setH(self.getGeomNode().getH())
        self.nametag3d.setFogOff()
        self.nametag3d.setLightOff()
        self.nametag3d.setColorScaleOff(100)
        self.nametag.setFont(PiratesGlobals.getPirateBoldOutlineFont())
        self.iconNodePath = self.nametag.getNameIcon()
        if self.iconNodePath.isEmpty():
            self.notify.warning('empty iconNodePath in initializeNametag3d')
            return 0
        if not self.nameText:
            self.nameText = OnscreenText(fg=Vec4(1, 1, 1, 1), bg=Vec4(0, 0, 0, 0), scale=1.1, align=TextNode.ACenter, mayChange=1, font=PiratesGlobals.getPirateBoldOutlineFont())
            self.nameText.reparentTo(self.iconNodePath)
            self.nameText.setTransparency(TransparencyAttrib.MDual, 2)
            self.nameText.setColorScaleOff(100)
            self.nameText.setLightOff()
            self.nameText.setFogOff()
            scale = self.nametag3d.getScale(render)
            self.nameText.setScale(1.0 / scale[0])

    def scaleAnimRate(self, forwardSpeed):
        rate = 1.0
        myMaxSpeed = self.getMaxSpeed()
        if myMaxSpeed > 0 and forwardSpeed > 0:
            currTime = globalClockDelta.globalClock.getFrameTime()
            maxSpeed = myMaxSpeed * (currTime - self.prevSpeedClock)
            prevTime = self.prevSpeedClock
            self.prevSpeedClock = currTime
            rate = min(1.25, forwardSpeed / maxSpeed)
        return rate

    def getNametagJoints(self):
        joints = []
        for lodName in self.getLODNames():
            bundle = self.getPartBundle('modelRoot', lodName)
            joint = bundle.findChild('name_tag')
            if joint:
                joints.append(joint)

        return joints

    def getAirborneHeight(self):
        return 0.0

    def getMaxSpeed(self):
        return 0

    def getRadius(self):
        return self.battleTubeRadius

    def play(self, *args, **kwArgs):
        UsesAnimationMixer.play(self, *args, **kwArgs)

    def loop(self, *args, **kwArgs):
        UsesAnimationMixer.loop(self, *args, **kwArgs)

    def pingpong(self, *args, **kwArgs):
        UsesAnimationMixer.pingpong(self, *args, **kwArgs)

    def pose(self, *args, **kwArgs):
        UsesAnimationMixer.pose(self, *args, **kwArgs)

    def stop(self, *args, **kwArgs):
        UsesAnimationMixer.stop(self, *args, **kwArgs)

    def getDeathAnimName(self, animNum=None):
        animStrings = ['death']
        if animNum not in list(range(len(animStrings))):
            animNum = random.choice([0])
        return animStrings[animNum]

    def getEnterDeathTrack(self):
        animName = self.getDeathAnimName()
        if not animName:
            return Sequence()
        frames = self.getNumFrames(animName)
        duration = self.getDuration(animName)
        if not frames:
            return Sequence()

        def playSfx():
            sfx = self.sfx.get('death')
            if sfx:
                sfx.play()

        def startVFX():
            if base.options.getSpecialEffectsSetting() >= base.options.SpecialEffectsHigh:
                effectScale = EnemyGlobals.getEnemyScale(self)
                deathEffect = JRDeathEffect.getEffect()
                if deathEffect:
                    deathEffect.reparentTo(render)
                    deathEffect.setPos(self.getPos(render))
                    deathEffect.setScale(effectScale)
                    deathEffect.effectScale = effectScale
                    deathEffect.play()
                shockwaveRingEffect = ShockwaveRing.getEffect()
                if shockwaveRingEffect:
                    shockwaveRingEffect.reparentTo(render)
                    shockwaveRingEffect.setPos(self.getPos(render))
                    shockwaveRingEffect.size = 24.0 + effectScale
                    Sequence(Wait(0.25), Func(shockwaveRingEffect.play)).start()
                spiritEffect = JRSpiritEffect.getEffect()
                if spiritEffect:
                    spiritEffect.reparentTo(render)
                    spiritEffect.setPos(self.getPos(render))
                    spiritEffect.setZ(self.getZ(render) + 6.0)
                    Sequence(Wait(0.25), Func(spiritEffect.play)).start()

        return Sequence(Wait(0.5), Parallel(Func(playSfx), Sequence(self.actorInterval(animName, blendOutT=0.0), Func(self.disableMixing), Func(self.pose, animName, frames - 1, blendT=0.0)), Sequence(Wait(duration / 3.0), Func(self.setTransparency, 1), LerpColorScaleInterval(self, duration / 4.0, Vec4(0.55, 0.7, 0.2, 1.0), startColorScale=Vec4(1)), Wait(duration / 3.0), Func(startVFX), LerpColorScaleInterval(self, 0.5, Vec4(0.0, 0.0, 0.0, 0.0), startColorScale=Vec4(0.55, 0.7, 0.2, 1.0)), Func(self.hide), Func(self.clearTransparency), Func(self.clearColorScale)), Func(self.setAllowInteract, False)))

    def getExitDeathTrack(self):
        return Sequence(Func(self.show))

    def getAnimInfo(self, state):
        return self.animInfo.get(state, self.FailsafeAnims)

    @classmethod
    def setupAnimInfoState(cls, state, info):
        if len(info) < len(cls.FailsafeAnims):
            info += cls.FailsafeAnims[len(info) - len(cls.FailsafeAnims):]
        cls.animInfo[state] = info

    @classmethod
    def setupAnimInfo(cls):
        cls.setupAnimInfoState('LandRoam', cls.FailsafeAnims)
        cls.setupAnimInfoState('WaterRoam', cls.FailsafeAnims)

    @classmethod
    def setupAnims(cls):
        cls.animInfo = copy.copy(SeaMonster.animInfo)
        cls.setupAnimInfo()
        filePrefix = cls.ModelInfo[1]
        animList = cls.AnimList
        animDict = {}
        for anim in animList:
            animDict[anim[0]] = filePrefix + anim[1]

        cls.animDict = animDict

    def setLODs(self):
        avatarDetail = base.config.GetString('avatar-detail', 'high')
        if avatarDetail == 'high':
            dist = [
             0, 20, 80, 280]
        else:
            if avatarDetail == 'med':
                dist = [
                 0, 10, 40, 280]
            else:
                if avatarDetail == 'low':
                    dist = [
                     0, 6, 20, 280]
                else:
                    raise Exception('Invalid avatar-detail: %s' % avatarDetail)
        self.addLOD('low', dist[3], dist[2])
        self.addLOD('med', dist[2], dist[1])
        self.addLOD('hi', dist[1], dist[0])

    @classmethod
    def setupAssets(cls):
        cls.animInfo = copy.copy(SeaMonster.animInfo)
        cls.setupAnimInfo()
        filePrefix = cls.ModelInfo[1]
        animList = cls.AnimList
        animDict = {}
        for anim in animList:
            animDict[anim[0]] = filePrefix + anim[1]

        cls.animDict = animDict
        filePrefix = cls.ModelInfo[1]
        for name in cls.SfxNames:
            cls.sfx[name] = loader.loadSfx('audio/' + cls.SfxNames[name])

        cls.actor = Actor.Actor()
        if loader.loadModel(filePrefix + 'med') != None:
            avatarDetail = base.config.GetString('avatar-detail', 'high')
            if avatarDetail == 'high':
                dist = [0, 200, 800, 2800]
            else:
                if avatarDetail == 'med':
                    dist = [0, 100, 400, 2800]
                else:
                    if avatarDetail == 'low':
                        dist = [0, 60, 200, 2800]
                    else:
                        raise Exception('Invalid avatar-detail: %s' % avatarDetail)
            cls.actor.setLODNode()
            cls.actor.addLOD('low', dist[3], dist[2])
            cls.actor.addLOD('med', dist[2], dist[1])
            cls.actor.addLOD('hi', dist[1], dist[0])
            cls.actor.loadModel(filePrefix + 'hi', 'modelRoot', 'hi')
            cls.actor.loadModel(filePrefix + 'med', 'modelRoot', 'med')
            cls.actor.loadModel(filePrefix + 'low', 'modelRoot', 'low')
            cls.actor.loadAnims(cls.animDict, 'modelRoot', 'all')
        else:
            cls.actor.loadModel(cls.ModelInfo[0])
            cls.actor.loadAnims(cls.animDict)
        cls.actor.getGeomNode().setH(180)
        return


SeaMonster.setupAnimInfo()
# okay decompiling .\pirates\creature\SeaMonster.pyc
