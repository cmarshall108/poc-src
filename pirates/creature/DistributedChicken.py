# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.creature.DistributedChicken
from pirates.creature.DistributedAnimal import DistributedAnimal
from pirates.creature.Chicken import Chicken

class DistributedChicken(DistributedAnimal):
    __module__ = __name__

    def __init__(self, cr):
        DistributedAnimal.__init__(self, cr, Chicken())
# okay decompiling .\pirates\creature\DistributedChicken.pyc
