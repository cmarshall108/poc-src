# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.GrapeshotEffect
from pandac.PandaModules import *
from direct.showbase.DirectObject import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from pirates.piratesbase import PiratesGlobals
from pirates.effects import PolyTrail
from PooledEffect import PooledEffect
from EffectController import EffectController
from pirates.effects.RoundshotProjectile import RoundshotProjectile
import random

class GrapeshotEffect(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.placeHolder = self.attachNewNode('grapeShotDummy')
        self.roundshots = []

    def spawnShot(self, time, targetPos, motion_color=None, startOffset=Vec3(0, 0, 0)):
        effect = RoundshotProjectile()
        if effect:
            self.roundshots.append(effect)
            effect.reparentTo(self)
            effect.setPos(self, startOffset)
            effect.play(time, targetPos, motion_color)

    def createTrack(self, rate=1):
        time = 2.0
        if base.options.getSpecialEffectsSetting() >= base.options.SpecialEffectsHigh:
            num_grapeshot_tracers = 10
        if base.options.getSpecialEffectsSetting() >= base.options.SpecialEffectsMedium:
            num_grapeshot_tracers = 7
        if base.options.getSpecialEffectsSetting() >= base.options.SpecialEffectsLow:
            num_grapeshot_tracers = 4
        self.track = Sequence()
        for i in range(num_grapeshot_tracers):
            self.placeHolder.setPos(self, random.uniform(-30, 30), random.uniform(400, 500), random.uniform(-20, 20))
            targetPos = self.placeHolder.getPos(self)
            self.track.append(Func(self.spawnShot, time + random.uniform(-0.5, 1.0), targetPos))

        self.track.append(Wait(4.0))
        self.track.append(Func(self.cleanUpEffect))

    def play(self, rate=1):
        self.createTrack()
        self.track.start()

    def cleanUpEffect(self):
        self.detachNode()
        for roundshot in self.roundshots:
            roundshot.destroy()

        self.roundshots = []
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        self.stop()
        for roundshot in self.roundshots:
            roundshot.destroy()

        self.roundshots = []
        self.placeHolder.removeNode()
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompiling .\pirates\effects\GrapeshotEffect.pyc
