from direct.fsm.FSM import FSM
from direct.directnotify.DirectNotifyGlobal import directNotify


class BattleAvatarGameFSMAI(FSM):
    notify = directNotify.newCategory('BattleAvatarGameFSMAI')

    def __init__(self, air, avatar):
        FSM.__init__(self, self.__class__.__name__)

        self.air = air
        self.avatar = avatar

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterLandRoam(self):
        pass

    def exitLandRoam(self):
        pass

    def enterDeath(self):
        pass

    def exitDeath(self):
        pass

    def enterThrownInJail(self):
        pass

    def exitThrownInJail(self):
        pass
