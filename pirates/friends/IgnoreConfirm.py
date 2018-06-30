from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.gui.DirectGui import *
from direct.task.Task import Task
from otp.otpbase import OTPGlobals, OTPLocalizer
from otp.uberdog.RejectCode import RejectCode
from panda3d.core import *
from pirates.battle.DistributedBattleNPC import DistributedBattleNPC
from pirates.piratesbase import PiratesGlobals, PLocalizer
from pirates.piratesgui import GuiPanel, PiratesGuiGlobals
from pirates.piratesgui.RequestButton import RequestButton


class IgnoreConfirmButton(RequestButton):

    def __init__(self, text, command, width=1.0):
        RequestButton.__init__(self, text, command, width)
        self.initialiseoptions(IgnoreConfirmButton)


class IgnoreConfirm(GuiPanel.GuiPanel):
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
            State.State('alreadyIgnored', self.enterAlreadyIgnored,
                        self.exitAlreadyIgnored),
            State.State('self', self.enterSelf, self.exitSelf),
            State.State('startIgnore', self.enterStartIgnore,
                        self.exitStartIgnore),
            State.State('endIgnore', self.enterEndIgnore, self.exitEndIgnore),
            State.State('cancel', self.enterCancel, self.exitCancel)
        ], 'off', 'off')
        self.message = DirectLabel(
            parent=self,
            relief=None,
            text='',
            text_scale=PiratesGuiGlobals.TextScaleLarge,
            text_align=TextNode.ACenter,
            text_fg=PiratesGuiGlobals.TextFG2,
            text_shadow=PiratesGuiGlobals.TextShadow,
            text_wordwrap=11,
            pos=(0.25, 0, 0.35),
            textMayChange=1)
        self.context = None
        self.bOk = IgnoreConfirmButton(
            text=OTPLocalizer.FriendInviterOK, command=self.__handleOk)
        self.bOk.reparentTo(self)
        self.bOk.setPos(0.2, 0, 0.05)
        self.bOk.hide()
        self.bCancel = IgnoreConfirmButton(
            text=OTPLocalizer.FriendInviterCancel,
            command=self.__handleCancel,
            width=1.5)
        self.bCancel.reparentTo(self)
        self.bCancel.setPos(0.2, 0, 0.05)
        self.bCancel.hide()
        self.bStop = IgnoreConfirmButton(
            text=OTPLocalizer.AvatarPanelStopIgnore,
            command=self.__handleStop,
            width=1.5)
        self.bStop.reparentTo(self)
        self.bStop.setPos(0.2, 0, 0.15)
        self.bStop.hide()
        self.bYes = IgnoreConfirmButton(
            text=OTPLocalizer.FriendInviterYes, command=self.__handleYes)
        self.bYes.reparentTo(self)
        self.bYes.setPos(0.1, 0, 0.05)
        self.bYes.hide()
        self.bNo = IgnoreConfirmButton(
            text=OTPLocalizer.FriendInviterNo, command=self.__handleNo)
        self.bNo.reparentTo(self)
        self.bNo.setPos(0.3, 0, 0.05)
        self.bNo.hide()
        self.fsm.enterInitialState()
        if self.avId == None:
            self.fsm.request('getNewFriend')
        else:
            self.fsm.request('begin')

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
        elif base.cr.avatarFriendsManager.checkIgnored(self.avId):
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
        self.message[
            'text'] = OTPLocalizer.IgnoreConfirmRemoveIgnore % self.avName
        self['text_pos'] = (0.0, 0.2)
        self.context = None
        self.bStop.show()
        self.bCancel.show()

    def exitAlreadyIgnored(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bStop.hide()
        self.bCancel.hide()

    def enterSelf(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmSelf
        self.context = None
        self.bOk.show()

    def exitSelf(self):
        self.bOk.hide()

    def enterStartIgnore(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmNewIgnore % self.avName
        self.context = None
        self.bOk.show()

    def exitStartIgnore(self):
        self.bOk.hide()

    def enterEndIgnore(self):
        self.message['text'] = OTPLocalizer.IgnoreConfirmEndIgnore % self.avName
        self.context = None
        self.bOk.show()

    def exitEndIgnore(self):
        self.bOk.hide()

    def enterCancel(self):
        if self.context != None:
            self.context = None
        self.fsm.request('off')

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
