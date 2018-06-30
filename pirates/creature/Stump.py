# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.creature.Stump
from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *
from pirates.creature.Creature import Creature


class Stump(Creature):

    ModelInfo = ('models/char/mossman_hi', 'models/char/mossman_')
    SfxNames = dict(Creature.SfxNames)
    SfxNames.update({
        'death': 'sfx_mossman_death.mp3',
        'pain': 'sfx_mossman_agitated.mp3',
        'spawn': 'sfx_mossman_intro.mp3'
    })
    sfx = {}
    AnimList = (('idle', 'idle'), ('walk', 'walk'), ('run', 'run'),
                ('death', 'death'), ('intro', 'intro'), ('jump', 'jump'),
                ('kick', 'kick'), ('kick_right', 'kick_right'), ('slap_left',
                                                                 'slap_left'),
                ('slap_right', 'slap_right'), ('strafe_left', 'strafe_left'),
                ('strafe_right', 'strafe_right'), ('swat_left', 'swat_left'),
                ('swat_right', 'swat_right'), ('jump_attack',
                                               'jump_attack'), ('pain', 'pain'))

    class AnimationMixer(Creature.AnimationMixer):

        notify = DirectNotifyGlobal.directNotify.newCategory(
            'StumpAnimationMixer')
        LOOP = Creature.AnimationMixer.LOOP
        ACTION = Creature.AnimationMixer.ACTION
        AnimRankings = {
            'idle': (LOOP['LOOP'],),
            'walk': (LOOP['LOOP'],),
            'run': (LOOP['LOOP'],),
            'strafe_left': (LOOP['LOOP'],),
            'strafe_right': (LOOP['LOOP'],),
            'death': (ACTION['MOVIE'],),
            'intro': (ACTION['ACTION'],),
            'jump': (ACTION['ACTION'],),
            'kick': (ACTION['ACTION'],),
            'kick_right': (ACTION['ACTION'],),
            'slap_left': (ACTION['ACTION'],),
            'slap_right': (ACTION['ACTION'],),
            'swat_left': (ACTION['ACTION'],),
            'swat_right': (ACTION['ACTION'],),
            'jump_attack': (ACTION['ACTION'],),
            'pain': (ACTION['ACTION'],)
        }

    @classmethod
    def setupAnimInfo(cls):
        cls.setupAnimInfoState('LandRoam',
                               (('idle', 1.0), ('walk', 1.0), ('walk', 1.0),
                                ('walk', -1.0), ('walk', 1.0), ('walk', 1.0),
                                ('walk', 1.0), ('walk', 1.0), ('walk', 1.0),
                                ('walk', 1.0), ('idle', 1.0), ('idle', 1.0)))
        cls.setupAnimInfoState('WaterRoam',
                               (('idle', 1.0), ('walk', 1.0), ('walk', 1.0),
                                ('walk', -1.0), ('walk', 1.0), ('walk', 1.0),
                                ('walk', 1.0), ('walk', 1.0), ('walk', 1.0),
                                ('walk', 1.0), ('idle', 1.0), ('idle', 1.0)))

    def __init__(self):
        Creature.__init__(self)
        self.rightHandNode = None
        self.leftHandNode = None
        if not Stump.sfx:
            for name in Stump.SfxNames:
                Stump.sfx[name] = loader.loadSfx('audio/' +
                                                 Stump.SfxNames[name])

        self.nametagOffset = 10
        self.generateCreature()
        self.headNode = self.find('**/def_neck')
        return

    def delete(self):
        self.rightHandNode = None
        self.leftHandNode = None
        Creature.delete(self)
        return

    def generateCreature(self):
        Creature.generateCreature(self)
        self.getWeaponJoints()

    def deleteWeaponJoints(self):
        try:
            if self.rightHandNode:
                self.rightHandNode.delete()
        except:
            return
        else:
            try:
                if self.leftHandNode:
                    self.leftHandNode.delete()
            except:
                return

    def getWeaponJoints(self):
        self.deleteWeaponJoints()
        self.rightHandNode = NodePath('rightHand')
        self.leftHandNode = NodePath('leftHand')
        for lodName in self.getLODNames():
            handLocator = self.find('**/*weapon_right')
            if not handLocator.isEmpty():
                self.rightHandNode.reparentTo(handLocator)
            handLocator = self.find('**/*weapon_left')
            if not handLocator.isEmpty():
                self.leftHandNode.reparentTo(handLocator)

    def adjustNametag3d(self, parentScale=1.0):
        self.nametag3d.setZ(self.scale * parentScale * self.nametagOffset)


# okay decompiling .\pirates\creature\Stump.pyc
