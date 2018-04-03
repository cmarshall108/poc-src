# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.PooledEffect
from pandac.PandaModules import *
from direct.showbase import Pool
from direct.showbase.DirectObject import DirectObject

class PooledEffect(DirectObject, NodePath):
    __module__ = __name__
    pool = None
    poolLimit = 124

    @classmethod
    def getEffect(self):
        if self.pool is None:
            self.pool = Pool.Pool()
        if self.pool.hasFree():
            return self.pool.checkout()
        else:
            free, used = self.pool.getNumItems()
            if free + used < self.poolLimit:
                self.pool.add(self())
                return self.pool.checkout()
            else:
                return
        return

    @classmethod
    def cleanup(self):
        if self.pool:
            self.pool.cleanup(self.destroy)
            self.pool = None
        return

    def __init__(self):
        NodePath.__init__(self, self.__class__.__name__)
        self.accept('clientLogout', self.__class__.cleanup)

    def destroy(self, item=None):
        if item:
            self.pool.remove(item)
        self.ignore('clientLogout')
        self.removeNode()
# okay decompiling .\pirates\effects\PooledEffect.pyc
