# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.friends.IgnoreConfirm
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.task.Task import Task
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals
from otp.uberdog.RejectCode import RejectCode
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import GuiPanel
from pirates.piratesgui import PiratesGuiGlobals
from pirates.battle.DistributedBattleNPC import DistributedBattleNPC
from pirates.piratesgui.RequestButton import RequestButton

class IgnoreConfirmButton(RequestButton):
    __module__ = __name__

    def __init__(self, text, command, width=1.0):
        RequestButton.__init__(self, text, command, width)
        self.initialiseoptions(IgnoreConfirmButton)


class IgnoreConfirm(GuiPanel.GuiPanel):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('IgnoreConfirm')

    def __init__(self, avId, avName):
        GuiPanel.GuiPanel.__init__(self, 'Ignore Confirm', 0.5, 0.5)
        self.initialiseoptions(IgnoreConfirm)
        self.setPos(0.15, 0, 0.25)
        self.avId = avId
        self.avName = avName
        self.fsm = ClassicFSM.ClassicFSM('IgnoreConfirm', [
         State.State('off', self.enterOff, self.exitOff),
         State.State('begin', self.enterBegin, self.exitBegin),
         State.State('notYet', self.enterNotYet, self.exitNotYet),
         State.State('alreadyIgnored', self.enterAlreadyIgnored, self.exitAlreadyIgnored),
         State.State('self', self.enterSelf, self.exitSelf),
         State.State('startIgnore', self.enterStartIgnore, self.exitStartIgnore),
         State.State('endIgnore', self.enterEndIgnore, self.exitEndIgnore),
         State.State('cancel', self.enterCancel, self.exitCancel)], 'off', 'off')
        self.message = DirectLabel(parent=self, relief=None, text='', text_scale=PiratesGuiGlobals.TextScaleLarge, text_align=TextNode.ACenter, text_fg=PiratesGuiGlobals.TextFG2, text_shadow=PiratesGuiGlobals.TextShadow, text_wordwrap=11, pos=(0.25,
                                                                                                                                                                                                                                                    0,
                                                                                                                                                                                                                                                    0.35), textMayChange=1)
        self.context = None
        self.bOk = IgnoreConfirmButton(text=OTPLocalizer.FriendInviterOK, command=self.__handleOk)
        self.bOk.reparentTo(self)
        self.bOk.setPos(0.2, 0, 0.05)
        self.bOk.hide()
        self.bCancel = IgnoreConfirmButton(text=OTPLocalizer.FriendInviterCancel, command=self.__handleCancel, width=1.5)
        self.bCancel.reparentTo(self)
        self.bCancel.setPos(0.2, 0, 0.05)
        self.bCancel.hide()
        self.bStop = IgnoreConfirmButton(text=OTPLocalizer.AvatarPanelStopIgnore, command=self.__handleStop, width=1.5)
        self.bStop.reparentTo(self)
        self.bStop.setPos(0.2, 0, 0.15)
        self.bStop.hide()
        self.bYes = IgnoreConfirmButton(text=OTPLocalizer.FriendInviterYes, command=self.__handleYes)
        self.bYes.reparentTo(self)
        self.bYes.setPos(0.1, 0, 0.05)
        self.bYes.hide()
        self.bNo = IgnoreConfirmButton(text=OTPLocalizer.FriendInviterNo, command=self.__handleNo)
        self.bNo.reparentTo(self)
        self.bNo.setPos(0.3, 0, 0.05)
        self.bNo.hide()
        self.fsm.enterInitialState()
        if self.avId == None:
            self.fsm.request('getNewFriend')
        else:
            self.fsm.request('begin')
        return

    def destroy(self):
        if hasattr(self, 'destroyed'):
            return
        self.destroyed = 1
        self.fsm.request('cancel')
        del self.fsm
        GuiPanel.GuiPanel.destroy(self)

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterBegin(self):
        myId = base.localAvatar.doId
        if self.avId == myId:
            self.fsm.request('self')
        else:
            if base.cr.avatarFriendsManager.checkIgnored(self.avId):
                self.fsm.request('alreadyIgnored')
            else:
                self.fsm.request('notYet')

    def exitBegin(self):
        pass

    def enterNotYet(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmNotYet % self.avName
        self.bYes.show()
        self.bNo.show()

    def exitNotYet(self):
        self.bYes.hide()
        self.bNo.hide()

    def enterAlreadyIgnored(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmRemoveIgnore % self.avName
        self['text_pos'] = (0.0, 0.2)
        self.context = None
        self.bStop.show()
        self.bCancel.show()
        return

    def exitAlreadyIgnored(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bStop.hide()
        self.bCancel.hide()

    def enterSelf(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmSelf
        self.context = None
        self.bOk.show()
        return

    def exitSelf(self):
        self.bOk.hide()

    def enterStartIgnore(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmNewIgnore % self.avName
        self.context = None
        self.bOk.show()
        return

    def exitStartIgnore(self):
        self.bOk.hide()

    def enterEndIgnore(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmEndIgnore % self.avName
        self.context = None
        self.bOk.show()
        return

    def exitEndIgnore(self):
        self.bOk.hide()

    def enterCancel(self):
        if self.context != None:
            self.context = None
        self.fsm.request('off')
        return

    def exitCancel(self):
        pass

    def __handleOk(self):
        self.destroy()

    def __handleCancel(self):
        self.destroy()

    def __handleStop(self):
        if self.fsm.getCurrentState().getName() == 'alreadyIgnored':
            base.cr.avatarFriendsManager.removeIgnore(self.avId)
            self.fsm.request('endIgnore')

    def __handleYes(self):
        if self.fsm.getCurrentState().getName() == 'notYet':
            base.cr.avatarFriendsManager.addIgnore(self.avId)
            self.fsm.request('startIgnore')

    def __handleNo(self):
        self.destroy()

    def __handleList(self):
        messenger.send('openFriendsList')
# okay decompiling .\pirates\friends\IgnoreConfirm.pyc
