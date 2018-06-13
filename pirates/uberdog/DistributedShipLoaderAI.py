from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.FSM import FSM
from pirates.ship import ShipGlobals
from pirates.uberdog import UberDogGlobals


class ShipFSM(FSM):

    def __init__(self, manager, avatar, callback=None):
        FSM.__init__(self, 'ShipFSM')

        self.manager = manager
        self.avatar = avatar
        self.callback = callback

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterStart(self):
        pass

    def exitStart(self):
        pass

    def enterStop(self):
        del self.manager.avatar2fsm[self.avatar.doId]
        self.demand('Off')

    def exitStop(self):
        pass


class CreateShipFSM(ShipFSM):

    def enterStart(self, shipType):

        def shipCreatedCallback(shipId):
            inventory = self.avatar.getInventory()

            if not inventory:
                self.notify.warning('Failed to create ship %d, avatar %d has no inventory!' % (
                    shipId, self.avatar.doId))

                return

            inventory.b_setCategoryAndDoId(UberDogGlobals.\
                InventoryCategory.SHIPS, shipId)

            self.request('Stop')

        shipConfig = ShipGlobals.getShipConfig(shipType)

        fields = {
            'setBaseTeam': (0,),
            'setShipClass': (shipConfig['setShipClass'][0],),
            'setName': ('Unnamed Ship',),
            'setInventoryId': (0,),
            'setIsFlagship': (0,),
            'setMaxHp': (shipConfig['setMaxHp'][0],),
            'setHp': (shipConfig['setHp'][0],),
            'setMaxSp': (0,),
            'setSp': (0,),
            'setHullCondition': (0,),
            'setMaxCargo': (0,),
            'setCargo': ([],),
            'setMaxCrew': (shipConfig['setMaxCrew'][0],),
            'setWishName': ('',),
            'setWishNameState': ('',),
        }

        self.manager.air.dbInterface.createObject(self.manager.air.dbId,
            self.manager.air.dclassesByName['PlayerShipAI'],
            fields=fields,
            callback=shipCreatedCallback)

    def exitStart(self):
        pass


class LoadShipsFSM(ShipFSM):

    def __init__(self, *args, **kwargs):
        ShipFSM.__init__(self, *args, **kwargs)

        self.pendingShips = []

    def enterStart(self):
        inventory = self.avatar.getInventory()

        if not inventory:
            self.notify.warning('Cannot load ships for avatar %d, unknown inventory!' % (
                self.avatar.doId))

            self.demand('Stop')
            return

        self.pendingShips = inventory.getShipList()

        for shipId in self.pendingShips:
            self.__loadShip(shipId)

    def __loadShip(self, shipId):

        def shipLoadedCallback(dclass, fields):
            self.pendingShips.remove(shipId)
            self.manager.air.sendActivate(shipId,
                0,
                0,
                dclass=dclass)

            target = self.avatar.getDISLid() << 32 | self.avatar.doId
            self.manager.air.setOwner(shipId, target)

            if not self.pendingShips:
                self.request('Stop')

        self.manager.air.dbInterface.queryObject(self.manager.air.dbId,
            shipId,
            shipLoadedCallback,
            dclass=self.manager.air.dclassesByName['PlayerShipAI'])

    def exitStart(self):
        pass


class DistributedShipLoaderAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedShipLoaderAI')

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)

        self.avatar2fsm = {}

    def runShipFSM(self, fsmType, avatar, *args):
        if avatar.doId in self.avatar2fsm:
            self.notify.warning('Cannot start shipFSM, an FSM is already running for avatar %d!' % (
                avatar.doId))

            return

        self.avatar2fsm[avatar.doId] = fsmType(self, avatar)
        self.avatar2fsm[avatar.doId].request('Start', *args)

    def createShip(self, avatar, shipType):
        self.runShipFSM(CreateShipFSM, avatar, shipType)

    def loadShips(self, avatar):
        self.runShipFSM(LoadShipsFSM, avatar)
