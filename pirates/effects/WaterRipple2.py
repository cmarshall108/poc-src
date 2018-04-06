# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.WaterRipple2
import random

from direct.interval.IntervalGlobal import *
from direct.particles import ForceGroup, ParticleEffect, Particles
from .EffectController import EffectController
from pandac.PandaModules import *
from .PooledEffect import PooledEffect


class WaterRipple2(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.particleDummy = render.attachNewNode(ModelNode('RippleParticleDummy'))
        self.particleDummy.setDepthWrite(0)
        self.particleDummy.setDepthTest(0)
        self.particleDummy.setFogOff()
        self.particleDummy.setBin('water', 15)
        mask = 268435455
        stencil = StencilAttrib.make(1, StencilAttrib.SCFEqual, StencilAttrib.SOKeep, StencilAttrib.SOKeep, StencilAttrib.SOKeep, 1, mask, mask)
        self.particleDummy.setAttrib(stencil)
        self.effectScale = 1.0
        self.f = ParticleEffect.ParticleEffect()
        self.f.reparentTo(self)
        self.effectGeom = loader.loadModel('models/effects/ripple2')
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('GeomParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.p0.emitter.setRadius(0.25)
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(32)
        self.p0.setBirthRate(0.3)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(2.5)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, -0.01))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.renderer.setGeomNode(self.effectGeom.node())
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setZScaleFlag(0)
        self.setEffectScale(self.effectScale)

    def createTrack(self):
        self.disturb = Sequence(Func(self.p0.setEmitter, 'DiscEmitter'), Func(self.p0.setBirthRate, 0.3), Func(self.p0.factory.setLifespanBase, 2.0), Wait(1.0), Func(self.p0.setEmitter, 'PointEmitter'), Func(self.p0.setBirthRate, 0.5), Func(self.p0.factory.setLifespanBase, 3.5))
        self.startEffect = Sequence(Func(self.p0.clearToInitial), Func(self.p0.setBirthRate, 0.4), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(3.0), Func(self.p0.setBirthRate, 0.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(2.0), self.endEffect)

    def setEffectScale(self, scale):
        self.effectScale = scale
        self.p0.renderer.setInitialXScale(3.0 * scale)
        self.p0.renderer.setFinalXScale(25.0 * scale)
        self.p0.renderer.setInitialYScale(3.0 * scale)
        self.p0.renderer.setFinalYScale(25.0 * scale)

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompiling .\pirates\effects\WaterRipple2.pyc
