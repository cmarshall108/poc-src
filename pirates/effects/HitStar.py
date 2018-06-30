import random

from direct.interval.IntervalGlobal import *
from direct.particles import ForceGroup, ParticleEffect, Particles
from pirates.effects.EffectController import EffectController
from pandac.PandaModules import *
from pirates.effects.PooledEffect import PooledEffect


class HitStar(PooledEffect, EffectController):

    cardScale = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/effectCandle')
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()
        self.setColorScaleOff()
        self.setBillboardPointEye(1.0)
        self.f = ParticleEffect.ParticleEffect()
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1', 32)
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereSurfaceEmitter')
        self.f.addParticles(self.p0)

    def createTrack(self):
        self.p0.setBirthRate(0.02)
        self.p0.setLitterSize(32)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(0.2)
        self.p0.factory.setLifespanSpread(0.05)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(360.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(0.5)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.0001 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.01 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.0005 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.06 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(
            ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor,
            ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(0.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.0001)
        self.startEffect = Sequence(
            Func(self.p0.setBirthRate, 0.02), Func(self.p0.clearToInitial),
            Func(self.f.start, self, self), Func(self.f.reparentTo, self))
        self.endEffect = Sequence(
            Func(self.p0.setBirthRate, 2.0), Wait(1.5),
            Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(0.2), self.endEffect)

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
