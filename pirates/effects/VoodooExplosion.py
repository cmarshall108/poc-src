# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.VoodooExplosion
import random

from direct.interval.IntervalGlobal import *
from direct.particles import ForceGroup, ParticleEffect, Particles
from pirates.effects.EffectController import EffectController
from pandac.PandaModules import *
from pirates.effects.PooledEffect import PooledEffect


class VoodooExplosion(PooledEffect, EffectController):

    cardScale = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.setDepthWrite(0)
        self.setLightOff()
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModelCopy('models/effects/particleMaps')
        self.card = model.find('**/particleWhiteSteam')
        self.card2 = model.find('**/particleDarkSmoke')
        self.f = ParticleEffect.ParticleEffect()
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.p1 = Particles.Particles('particles-2')
        self.p1.setFactory('ZSpinParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.p1.setEmitter('SphereSurfaceEmitter')
        self.f.addParticles(self.p0)
        self.f.addParticles(self.p1)
        f0 = ForceGroup.ForceGroup('gravity')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, -20.0), 1.0, 1)
        force0.setActive(1)
        f0.addForce(force0)
        f1 = ForceGroup.ForceGroup('Noise')
        force1 = LinearNoiseForce(2.0, 0)
        force1.setVectorMasks(0, 0, 1)
        force1.setActive(1)
        f1.addForce(force1)
        self.f.addForceGroup(f0)
        self.f.addForceGroup(f1)
        self.p0.setPoolSize(8)
        self.p0.setBirthRate(0.1)
        self.p0.setLitterSize(8)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(3.5)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.25)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(0.35)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.01 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.4 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.01 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.4 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.getColorInterpolationManager().addLinear(
            0.0, 1.0, Vec4(0.0, 0.0, 0.0, 1.0), Vec4(0.2, 0.1, 0.6, 0.4), 1)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 10.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 1.0))
        self.p0.emitter.setRadius(0.75)
        self.p0.emitter.setOuterAngle(90.0)
        self.p0.emitter.setInnerAngle(0.0)
        self.p0.emitter.setOuterMagnitude(8.0)
        self.p0.emitter.setInnerMagnitude(0.0)
        self.p0.emitter.setCubicLerping(0)
        self.p1.setPoolSize(128)
        self.p1.setBirthRate(0.01)
        self.p1.setLitterSize(128)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(1)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(1.5)
        self.p1.factory.setLifespanSpread(0.75)
        self.p1.factory.setMassBase(4.0)
        self.p1.factory.setMassSpread(0.0)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.factory.setInitialAngle(0.0)
        self.p1.factory.setInitialAngleSpread(90.0)
        self.p1.factory.enableAngularVelocity(1)
        self.p1.factory.setAngularVelocity(500.0)
        self.p1.factory.setAngularVelocitySpread(100.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p1.renderer.setUserAlpha(0.2)
        self.p1.renderer.setFromNode(self.card2)
        self.p1.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(1)
        self.p1.renderer.setInitialXScale(0.003 * self.cardScale)
        self.p1.renderer.setFinalXScale(0.025 * self.cardScale)
        self.p1.renderer.setInitialYScale(0.003 * self.cardScale)
        self.p1.renderer.setFinalYScale(0.04 * self.cardScale)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.renderer.setColorBlendMode(
            ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor,
            ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p1.renderer.getColorInterpolationManager().addLinear(
            0.0, 1.0, Vec4(1.0, 1.0, 1.0, 0.2), Vec4(0.75, 0.6, 1.0, 0), 1)
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p1.emitter.setAmplitude(1.0)
        self.p1.emitter.setAmplitudeSpread(0.0)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, 5))
        self.p1.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p1.emitter.setRadius(0.1)

    def createTrack(self, rate=1):
        self.startEffect = Sequence(
            Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial),
            Func(self.p1.setBirthRate, 0.01), Func(self.p1.clearToInitial),
            Func(self.f.start, self, self))
        self.endEffect = Sequence(
            Func(self.p0.setBirthRate, 100), Func(self.p1.setBirthRate, 100),
            Wait(4.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(0.5), self.endEffect)

    def setEffectColor(self, color):
        self.effectColor = Vec4(1, 1, 1, 1) - (Vec4(1, 1, 1, 1) - color) / 2.0
        self.p0.renderer.getColorInterpolationManager().clearToInitial()
        self.p0.renderer.getColorInterpolationManager().addLinear(
            0.0, 1.0, Vec4(0.0, 0.0, 0.0, 1.0), self.effectColor / 2.0, 1)
        self.p1.renderer.getColorInterpolationManager().clearToInitial()
        self.p1.renderer.getColorInterpolationManager().addLinear(
            0.0, 1.0, Vec4(1.0, 1.0, 1.0, 0.2),
            self.effectColor - Vec4(0, 0, 0, 1), 1)

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)


# okay decompiling .\pirates\effects\VoodooExplosion.pyc
