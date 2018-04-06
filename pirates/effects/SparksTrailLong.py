# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.SparksTrailLong
from direct.interval.IntervalGlobal import *
from direct.particles import ForceGroup, ParticleEffect, Particles
from .EffectController import EffectController
from pandac.PandaModules import *
from .PooledEffect import PooledEffect


class SparksTrailLong(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/particleCards')
        self.card = model.find('**/particleStars')
        self.cardScale = 64.0
        self.effectColor = Vec4(1, 1, 1, 1)
        self.effectScale = 1.0
        self.lifespan = 2.0
        if not SparksTrailLong.particleDummy:
            SparksTrailLong.particleDummy = render.attachNewNode(ModelNode('SparksTrailLongParticleDummy'))
            SparksTrailLong.particleDummy.setDepthWrite(0)
        self.f = ParticleEffect.ParticleEffect()
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('PointEmitter')
        self.f.addParticles(self.p0)
        f0 = ForceGroup.ForceGroup('Gravity')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, -5.0), 1.0, 0)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.f.addForceGroup(f0)
        self.p0.setPoolSize(128)
        self.p0.setBirthRate(0.02)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(0)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(self.lifespan)
        self.p0.factory.setLifespanSpread(0.1)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(90.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(25.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, -2.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.setEffectScale(self.effectScale)

    def createTrack(self):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.015), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(self.lifespan + 0.1), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(1.0), self.endEffect)

    def setLifespan(self, duration):
        self.lifespan = duration
        self.p0.factory.setLifespanBase(duration)

    def setEffectColor(self, color):
        self.effectColor = color
        self.p0.renderer.setColor(self.effectColor)

    def setEffectScale(self, scale):
        self.effectScale = scale
        self.p0.renderer.setInitialXScale(0.05 * self.cardScale * scale)
        self.p0.renderer.setFinalXScale(0.5 * self.cardScale * scale)
        self.p0.renderer.setInitialYScale(0.05 * self.cardScale * scale)
        self.p0.renderer.setFinalYScale(0.5 * self.cardScale * scale)
        self.p0.emitter.setAmplitude(30.0 * scale)

    def cleanUpEffect(self):
        self.f.disable()
        self.detachNode()
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompiling .\pirates\effects\SparksTrailLong.pyc
