from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

from pirates.quest.QuestBase import QuestBase
from pirates.quest.Quest import Quest
from pirates.quest import QuestDB
from pirates.quest.QuestTaskState import QuestTaskState


class DistributedQuestAI(DistributedObjectAI, QuestBase, Quest):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedQuestAI')

    def __init__(self, air, questId='', giverId='', initialTaskStates=[QuestTaskState()], rewards=[]):
        DistributedObjectAI.__init__(self, air)
        Quest.__init__(self, questId, giverId, initialTaskStates, rewards)

        self.ownerId = 0
        self.combineOp = 0

        self.finalizeStateIndex = 0

    def generate(self):
        DistributedObjectAI.generate(self)

        self.d_announceNewQuest()

    def setOwnerId(self, ownerId):
        self.ownerId = ownerId

    def getOwnerId(self):
        return self.ownerId

    def d_setQuestId(self, questId):
        self.sendUpdate('setQuestId', [questId])

    def b_setQuestId(self, questId):
        self.setQuestId(questId)
        self.d_setQuestId(questId)

    def getQuestId(self):
        return self.questId

    def d_setGiverId(self, giverId):
        self.sendUpdate('setGiverId', [giverId])

    def b_setGiverId(self, giverId):
        self.setGiverId(giverId)
        self.d_setGiverId(giverId)

    def getGiverId(self):
        return self.giverId

    def d_announceNewQuest(self):
        self.sendUpdateToAvatarId(self.ownerId, 'announceNewQuest', [])

    def d_setCombineOp(self, combineOp):
        self.sendUpdate('setCombineOp', [combineOp])

    def b_setCombineOp(self, combineOp):
        self.setCombineOp(combineOp)
        self.d_setCombineOp(combineOp)

    def getCombineOp(self):
        return self.combineOp

    def d_setTaskStates(self, taskStates):
        self.sendUpdate('setTaskStates', [taskStates])

    def b_setTaskStates(self, taskStates):
        self.setTaskStates(taskStates)
        self.d_setTaskStates(taskStates)

    def getTaskStates(self):
        return self.taskStates

    def d_setRewardStructs(self, rewardStructs):
        self.sendUpdate('setRewardStructs', [rewardStructs])

    def b_setRewardStructs(self, rewardStructs):
        self.setRewardStructs(rewardStructs)
        self.d_setRewardStructs(rewardStructs)

    def setFinalizeStateIndex(self, finalizeStateIndex):
        self.finalizeStateIndex = finalizeStateIndex

    def getFinalizeStateIndex(self):
        return self.finalizeStateIndex

    def sendFinalizeEvent(self, idx=None):
        try:
            finalizeStateInfo = self.questDNA.getFinalizeInfo()[idx or self.finalizeStateIndex]
        except IndexError:
            return

        finalizeEvent = finalizeStateInfo.get('sendEvent', '')
        if not finalizeEvent:
            return

        messenger.send('%s-%d' % (finalizeEvent, self.doId))

    def d_startFinalizeScene(self, idx, giverId):
        if self.questId not in QuestDB.QuestDict:
            self.notify.warning('Cannot start finalize scene for quest %s, '
                'quest was not found in the QuestDB dictionary!' % self.questId)

            return

        try:
            finalizeInfo = self.questDNA.getFinalizeInfo()[idx]
        except IndexError:
            self.notify.warning('Failed to start finalize scene for avatar: %d, '
                'invalid sceneId: %d!' % (self.ownerId, idx))

            return

        endEvent = finalizeInfo.get('sendEvent', '')
        self.sendUpdate('startFinalizeScene', [idx, giverId, endEvent])

    def doneFinalizeScene(self):
        messenger.send('quest-finalize-%d' % self.doId)

    def d_amFinalized(self):
        Quest.setFinalized(self)
        self.sendUpdateToAvatarId(self.ownerId, 'amFinalized', [])

    def delete(self):
        QuestBase.delete(self)
        DistributedObjectAI.delete(self)
