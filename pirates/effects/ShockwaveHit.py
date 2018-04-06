# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.ShockwaveHit
import random

from direct.interval.IntervalGlobal import *
from .EffectController import EffectController
from pandac.PandaModules import *
from .PooledEffect import PooledEffect


class ShockwaveHit(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.speed = 0.2
        self.size = 8
        self.explosionSequence = 0
        self.currentType = 'Hit'
        self.card = None
        self.explosion = loader.loadModelCopy('models/effects/shockwaveRed')
        self.explosion.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        self.explosion.setDepthWrite(0)
        self.explosion.setFogOff()
        self.explosion.setLightOff()
        self.explosion.setBillboardPointEye(0.5)
        self.explosion.setScale(1)
        self.explosion.setColorScale(1, 1, 1, 1)
        self.explosion.reparentTo(self)
        self.explosion.hide()
        self.card = loader.loadModelCopy('models/effects/shockwaves')
        return

    def loadExplosion(self, hpr, type='Hit'):
        if self.currentType != type:
            self.currentType = type
            if type == 'Hit':
                tex = self.card.find('**/effectRedShockwave').findTexture('*')
                self.explosion.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
            else:
                if type == 'Dark':
                    tex = self.card.find('**/effectDarkShockwave').findTexture('*')
                    self.explosion.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MNone))
                else:
                    if type == 'Pulse':
                        tex = self.card.find('**/effectPulseShockwave').findTexture('*')
                        self.explosion.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MNone))
                    else:
                        if type == 'HitRay':
                            tex = self.card.find('**/effectFlashRays').findTexture('*')
                            self.explosion.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
            self.explosion.setTexture(tex, 1)
        self.explosion.setHpr(hpr)

    def createTrack(self):
        self.explosion.setScale(1)
        self.explosion.setColorScale(1, 1, 1, 1)
        fadeBlast = self.explosion.colorScaleInterval(self.speed * 0.66, Vec4(0, 0, 0, 0), startColorScale=Vec4(1, 1, 1, 1))
        waitFade = Sequence(Wait(self.speed * 0.33), fadeBlast)
        scaleBlast = self.explosion.scaleInterval(self.speed, self.size, blendType='easeIn')
        self.track = Sequence(Func(self.explosion.show), Parallel(scaleBlast, waitFade), Func(self.explosion.hide), Func(self.cleanUpEffect))

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        if self.card:
            self.card.removeNode()
            self.card = None
        EffectController.destroy(self)
        PooledEffect.destroy(self)
        return
# okay decompiling .\pirates\effects\ShockwaveHit.pyc
