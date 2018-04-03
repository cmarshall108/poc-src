# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.EffectController
from pandac.PandaModules import *

class EffectController:
    __module__ = __name__
    particleDummy = None

    def __init__(self):
        self.track = None
        self.startEffect = None
        self.endEffect = None
        self.f = None
        self.p0 = None
        return

    def createTrack(self):
        pass

    def destroy(self):
        self.finish()
        if self.f:
            self.f.cleanup()
        self.f = None
        self.p0 = None
        self.removeNode()
        return

    def cleanUpEffect(self):
        self.setPosHpr(0, 0, 0, 0, 0, 0)
        if self.f:
            self.f.disable()
        self.detachNode()

    def reallyCleanUpEffect(self):
        self.cleanUpEffect()
        self.finish()

    def play(self, lod=None):
        if lod != None:
            try:
                self.createTrack(lod)
            except TypeError, e:
                raise TypeError('Error loading %s effect.' % self.__class__.__name__)

        else:
            self.createTrack()
        self.track.start()
        return

    def stop(self):
        if self.track:
            self.track.pause()
            self.track = None
        if self.startEffect:
            self.startEffect.pause()
            self.startEffect = None
        if self.endEffect:
            self.endEffect.pause()
            self.endEffect = None
        self.cleanUpEffect()
        return

    def finish(self):
        if self.track:
            self.track.pause()
            self.track = None
        if self.startEffect:
            self.startEffect.pause()
            self.startEffect = None
        if self.endEffect:
            self.endEffect.pause()
            self.endEffect = None
        return

    def startLoop(self, lod=None):
        if lod != None:
            try:
                self.createTrack(lod)
            except TypeError, e:
                raise TypeError('Error loading %s effect.' % self.__class__.__name__)

        else:
            self.createTrack()
        if self.startEffect:
            self.startEffect.start()
        return

    def stopLoop(self):
        if self.startEffect:
            self.startEffect.pause()
            self.startEffect = None
        if self.endEffect and not self.endEffect.isPlaying():
            self.endEffect.start()
        return

    def getTrack(self):
        if not self.track:
            self.createTrack()
        return self.track
# okay decompiling .\pirates\effects\EffectController.pyc
