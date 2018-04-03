# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.uberdog.AccountDetailRecord
from otp.otpbase import OTPGlobals

class SubDetailRecord:
    __module__ = __name__

    def __init__(self):
        self.subId = 0
        self.subOwnerId = 0
        self.subName = ''
        self.subActive = ''
        self.subAccess = ''
        self.subLevel = 0
        self.subNumAvatars = 0
        self.subNumConcur = 0
        self.subFounder = 0

    def __str__(self):
        s = ''
        s += '========== Sub %d ==========\n' % self.subId
        s += 'Sub Id: %d\n' % self.subId
        s += 'Sub Owner Id: %d\n' % self.subOwnerId
        s += 'Sub Name: %s\n' % self.subName
        s += 'Sub Active: %s\n' % self.subActive
        s += 'Sub Access: %s\n' % self.subAccess
        s += 'Sub Level: %d\n' % self.subLevel
        s += 'Sub MaxAvatars: %d\n' % self.subNumAvatars
        s += 'Sub Concurrent: %d\n' % self.subNumConcur
        s += 'Sub Founder: %d\n' % self.subFounder
        return s


class AccountDetailRecord:
    __module__ = __name__

    def __init__(self):
        self.openChatEnabled = False
        self.createFriendsWithChat = False
        self.chatCodeCreation = False
        self.piratesAccess = OTPGlobals.AccessUnknown
        self.familyAccountId = 0
        self.playerAccountId = 0
        self.playerName = ''
        self.playerNameApproved = False
        self.maxAvatars = 0
        self.numFamilyMembers = 0
        self.familyMembers = []
        self.numSubs = 0
        self.subDetails = {}
        self.maxAvatarSlots = 0
        self.WLChatEnabled = False

    def getMaxNumAvatars(self, subId):
        subDetails = self.subDetails.get(subId)
        if subDetails:
            return subDetails.subNumAvatars
        else:
            return 0

    def canOpenChatAndNotGetBooted(self):
        return self.openChatEnabled or self.createFriendsWithChat

    def __str__(self):
        s = '========== Account %s ==========\n' % self.playerAccountId
        s += 'OpenChatEnabled: %s\n' % self.openChatEnabled
        s += 'WLChatEnabled: %s\n' % self.WLChatEnabled
        s += 'CreateFriendsWithChat: %s\n' % self.createFriendsWithChat
        s += 'ChatCodeCreation: %s\n' % self.chatCodeCreation
        s += 'PiratesAccess: %s\n' % self.piratesAccess
        s += 'FamilyAccountId: %d\n' % self.familyAccountId
        s += 'PlayerAccountId: %d\n' % self.playerAccountId
        s += 'PlayerName: %s\n' % self.playerName
        s += 'AccountNameApproved: %d\n' % self.playerNameApproved
        s += 'MaxAvatars: %d\n' % self.maxAvatars
        s += 'MaxAvatarSlots: %d\n' % self.maxAvatarSlots
        s += 'NumFamilyMembers: %d\n' % self.numFamilyMembers
        s += 'FamilyMembers: %s\n' % self.familyMembers
        s += 'NumSubs: %s\n' % self.numSubs
        for subDetails in self.subDetails.values():
            s += str(subDetails)

        s += '================================\n'
        return s
# okay decompiling .\otp\uberdog\AccountDetailRecord.pyc
