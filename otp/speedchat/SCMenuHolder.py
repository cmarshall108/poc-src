# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.speedchat.SCMenuHolder
import types

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from .SCElement import SCElement
from .SCMenu import SCMenu
from .SCObject import SCObject


class SCMenuHolder(SCElement):
    __module__ = __name__
    N = 0.9
    DefaultFrameColor = (0, 0, 0, 1.0 - N)
    del N
    MenuColorScaleDown = 0.95

    def __init__(self, title, menu=None):
        SCElement.__init__(self)
        self.title = title
        scGui = loader.loadModelOnce(SCMenu.GuiModelName)
        self.scArrow = scGui.find('**/chatArrow')
        self.menu = None
        self.setMenu(menu)
        return

    def destroy(self):
        if self.menu is not None:
            self.menu.destroy()
            self.menu = None
        SCElement.destroy(self)
        return

    def setTitle(self, title):
        self.title = title
        self.invalidate()

    def getTitle(self):
        return self.title

    def setMenu(self, menu):
        if self.menu is not None:
            self.menu.destroy()
        self.menu = menu
        if self.menu is not None:
            self.privAdoptSCObject(self.menu)
            self.menu.setHolder(self)
            self.menu.reparentTo(self, 1)
            self.menu.hide()
        self.updateViewability()
        return

    def getMenu(self):
        return self.menu

    def showMenu(self):
        if self.menu is not None:
            cS = SCMenuHolder.MenuColorScaleDown
            self.menu.setColorScale(cS, cS, cS, 1)
            self.menu.enterVisible()
            self.menu.show()
        return

    def hideMenu(self):
        if self.menu is not None:
            self.menu.hide()
            self.menu.exitVisible()
        return

    def getMenuOverlap(self):
        if self.parentMenu.isTopLevel():
            return self.getTopLevelOverlap()
        else:
            return self.getSubmenuOverlap()

    def getMenuOffset(self):
        xOffset = self.width * (1.0 - self.getMenuOverlap())
        return Point3(xOffset, 0, 0)

    def onMouseClick(self, event):
        SCElement.enterActive(self)
        self.parentMenu.memberSelected(self)

    def enterActive(self):
        SCElement.enterActive(self)
        self.showMenu()
        r, g, b = self.getColorScheme().getMenuHolderActiveColor()
        a = self.getColorScheme().getAlpha()
        self.button.frameStyle[DGG.BUTTON_READY_STATE].setColor(r, g, b, a)
        self.button.updateFrameStyle()

    def exitActive(self):
        SCElement.exitActive(self)
        self.hideMenu()
        self.button.frameStyle[DGG.BUTTON_READY_STATE].setColor(*SCMenuHolder.DefaultFrameColor)
        self.button.updateFrameStyle()

    def getDisplayText(self):
        return self.title

    def updateViewability(self):
        if self.menu is None:
            self.setViewable(0)
            return
        isViewable = False
        for child in self.menu:
            if child.isViewable():
                isViewable = True
                break

        self.setViewable(isViewable)
        return

    def getMinSubmenuWidth(self):
        parentMenu = self.getParentMenu()
        if parentMenu is None:
            myWidth, myWeight = self.getMinDimensions()
        else:
            myWidth = parentMenu.getWidth()
        return 0.15 + myWidth * self.getMenuOverlap()

    def getMinDimensions(self):
        width, height = SCElement.getMinDimensions(self)
        width += 1.0
        return (
         width, height)

    def invalidate(self):
        SCElement.invalidate(self)
        if self.menu is not None:
            self.menu.invalidate()
        return

    def finalize(self, dbArgs={}):
        if not self.isDirty():
            return
        r, g, b = self.getColorScheme().getArrowColor()
        a = self.getColorScheme().getAlpha()
        self.scArrow.setColorScale(r, g, b, a)
        if self.menu is not None:
            self.menu.setPos(self.getMenuOffset())
        if self.isActive():
            r, g, b = self.getColorScheme().getMenuHolderActiveColor()
            a = self.getColorScheme().getAlpha()
            frameColor = (r, g, b, a)
        else:
            frameColor = SCMenuHolder.DefaultFrameColor
        args = {'image': self.scArrow, 'image_pos': (self.width - 0.5, 0, -self.height * 0.5), 'frameColor': frameColor}
        args.update(dbArgs)
        SCElement.finalize(self, dbArgs=args)
        return

    def hasStickyFocus(self):
        return 1

    def privSetSettingsRef(self, settingsRef):
        SCObject.privSetSettingsRef(self, settingsRef)
        if self.menu is not None:
            self.menu.privSetSettingsRef(settingsRef)
        return

    def invalidateAll(self):
        SCObject.invalidateAll(self)
        if self.menu is not None:
            self.menu.invalidateAll()
        return

    def finalizeAll(self):
        SCObject.finalizeAll(self)
        if self.menu is not None:
            self.menu.finalizeAll()
        return
# okay decompiling .\otp\speedchat\SCMenuHolder.pyc
