# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.treasuremap.DistributedTreasureMapInstance
from direct.fsm import FSM
from direct.showbase.PythonUtil import report
from pirates.instance import DistributedInstanceWorld
from pirates.piratesbase import PiratesGlobals
from pirates.quest import DistributedQuest, QuestHolder
from pirates.quest.MiniQuestItemGui import MiniQuestItemGui


class DistributedTreasureMapInstance(DistributedInstanceWorld.DistributedInstanceWorld, QuestHolder.QuestHolder, FSM.FSM):
    __module__ = __name__
    notify = directNotify.newCategory('DistributedTreasureMapInstance')

    def __init__(self, cr):
        DistributedInstanceWorld.DistributedInstanceWorld.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedTreasureMapInstance')
        self.pendingObjectiveRequest = None
        self.pendingShipRequest = None
        self.objectives = []
        return

    def announceGenerate(self):
        DistributedInstanceWorld.DistributedInstanceWorld.announceGenerate(self)
        base.cr.treasureMap = self
        localAvatar.guiMgr.showTMUI(self)
        if localAvatar.guiMgr.questPage:
            localAvatar.guiMgr.questPage.trackedQuestLabel.hide()
        localAvatar.b_setTeleportFlag(PiratesGlobals.TFTreasureMap)

    def disable(self):
        base.cr.treasureMap = None
        FSM.FSM.cleanup(self)
        localAvatar.guiMgr.hideTMUI()
        if localAvatar.guiMgr.questPage:
            localAvatar.guiMgr.questPage.trackedQuestLabel.show()
        localAvatar.b_clearTeleportFlag(PiratesGlobals.TFTreasureMap)
        if self.pendingObjectiveRequest:
            base.cr.relatedObjectMgr.abortRequest(self.pendingObjectiveRequest)
            self.pendingObjectiveRequest = None
        if self.pendingShipRequest:
            base.cr.relatedObjectMgr.abortRequest(self.pendingShipRequest)
            self.pendingShipRequest = None
        DistributedInstanceWorld.DistributedInstanceWorld.disable(self)
        return

    def enterWaitClientsReady(self):
        pass

    @report(types=['frameCount', 'deltaStamp', 'args'], dConfigParam='want-blackpearl-report')
    def setBarrierData(self, data):
        DistributedInstanceWorld.DistributedInstanceWorld.setBarrierData(self, data)
        self.doneBarrier(self.uniqueName('allAvatarsReady'))

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterReward(self):
        pass

    def exitReward(self):
        pass

    def filterReward(self, request, args=[]):
        if request in ['Completed']:
            return self.defaultFilter(request, args)

    def enterNotCompleted(self):
        pass

    def exitNotCompleted(self):
        pass

    def filterNotCompleted(self, request, args=[]):
        if request in ['Completed']:
            return self.defaultFilter(request, args)

    def enterCompleted(self):
        pass

    def exitCompleted(self):
        pass

    def getItemList(self):
        return self.getObjectives()

    def getObjectives(self):
        return self.objectives

    def setObjectives(self, objectives):
        self.objectives = []
        for currObjective in objectives:
            self.objectives.append({'Type': 'ObjectId', 'Value': currObjective})
            self.pendingObjectiveRequest = base.cr.relatedObjectMgr.requestObjects([currObjective], eachCallback=self.tagAsObjective)

        print('got new objectives list %s' % objectives)
        messenger.send(self.getItemChangeMsg())

    def getItemChangeMsg(self):
        return self.taskName('objectiveChanged')

    def tagAsObjective(self, quest):
        quest.type = DistributedQuest.QUEST_TYPE_TM

    def setTMComplete(self, instanceResults, playerResults):
        guiMgr = base.localAvatar.guiMgr
        guiMgr.hideTrays()
        guiMgr.hideTMUI()
        guiMgr.showTMCompleteUI(self, playerResults)

    def createNewItem(self, item, parent, itemType=None, columnWidths=[], color=None):
        return MiniQuestItemGui(item, parent)

    def requestTreasureMapLeave(self):
        localAvatar.guiMgr.hideTMCompleteUI()
        localAvatar.guiMgr.showTrays()
        self.sendUpdate('requestLeave', [0])

    def requestLeaveApproved(self, parentId, zoneId, shipId):
        localAvatar.setInterest(parentId, zoneId, ['tmExit'])
        self.pendingShipRequest = base.cr.relatedObjectMgr.requestObjects([shipId], eachCallback=self.goToShip)

    def goToShip(self, pendingObj):
        pendingObj.localAvatarBoardShip()
        self.cr.teleportMgr.initiateTeleport(PiratesGlobals.INSTANCE_TM, 'mainWorld')
# okay decompiling .\pirates\treasuremap\DistributedTreasureMapInstance.pyc
