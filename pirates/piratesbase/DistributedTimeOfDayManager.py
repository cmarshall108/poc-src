from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
from direct.distributed.ClockDelta import globalClockDelta
from otp.ai.MagicWordGlobal import *
from TimeOfDayManager import TimeOfDayManager
from pirates.piratesbase import TODGlobals
from pirates.effects.FireworkGlobals import *


class DistributedTimeOfDayManager(DistributedObject, TimeOfDayManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTimeOfDayManager')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        TimeOfDayManager.__init__(self)

    def generate(self):
        self.cr.timeOfDayManager = self
        DistributedObject.generate(self)

    def disable(self):
        TimeOfDayManager.disable(self)
        DistributedObject.disable(self)
        if self.cr.timeOfDayManager == self:
            self.cr.timeOfDayManager = None

    def delete(self):
        TimeOfDayManager.delete(self)
        DistributedObject.delete(self)

    def sync(self, cycleType, startingState, startingTime, cycleDuration):
        self.cycleType = cycleType
        self.startingState = startingState
        self.startingTime = startingTime
        self.cycleDuration = cycleDuration
        self.enterInitState()


@magicWord(category=CATEGORY_SYSTEM_ADMIN, types=[int])
def setClouds(level):
    """
    Locally sets the timeOfDayManager cloud state
    """

    base.cr.timeOfDayManager.skyGroup.setCloudLevel(level)
    return 'Transitioning clouds to %d.' % level


@magicWord(category=CATEGORY_SYSTEM_ADMIN, types=[int])
def fireworks(showType=FireworkShowType.FourthOfJuly):
    """
    Locally enables or disables Fourth of July fireworks
    """

    timestamp = globalClockDelta.localElapsedTime(base.cr.timeOfDayManager.startingTime, bits=32)
    if base.cr.activeWorld:
        if not base.cr.activeWorld.fireworkShowMgr:
            base.cr.activeWorld.enableFireworkShow(timestamp, showType)
        else:
            base.cr.activeWorld.disableFireworkShow()

    return "Toggled fireworks show with type: %d" % showType
