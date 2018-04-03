# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.makeapirate.PirateMale
Instruction context:
   
2097    1883  LOAD_FAST             0  'self'
           1886  LOAD_ATTR             5  'pirate'
           1889  LOAD_ATTR            63  'generateClothesColor'
           1892  CALL_FUNCTION_0       0  None
           1895  POP_TOP          
->         1896  LOAD_CONST            0  None
from pandac.PandaModules import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from pirates.pirate import HumanDNA
from pirates.makeapirate import ClothingGlobals
from pirates.piratesbase import Freebooter
import random, TattooGlobals
from otp.otpbase import OTPRender
TX = 0
TY = 1
TZ = 2
RX = 3
RY = 4
RZ = 5
SX = 6
SY = 7
SZ = 8
HAT = 0
SHIRT = 1
VEST = 2
COAT = 3
PANT = 4
BELT = 5
SOCK = 6
SHOE = 7
ZOMB_BODY_TEXTURE = 1
ZOMB_HAIR_COLOR = 7
ZOMB_HAT = 8
ZOMB_SHIRT = 0
ZOMB_SHIRT_TEXTURE = 0
ZOMB_VEST = 0
ZOMB_VEST_TEXTURE = 0
ZOMB_COAT = 0
ZOMB_COAT_TEXTURE = 0
ZOMB_PANT = 1
ZOMB_PANT_TEXTURE = 11
ZOMB_BELT = 0
ZOMB_SHOE = 0
ZOMB_SHOE_TEXTURE = 0
body_textures = [
 [
  'PM_sf_body_cauc', 'zomb_a_body'], ['PM_mi_body_cauc', 'zomb_a_body'], ['PM_mi_body_cauc', 'zomb_a_body'], ['PM_tp_body_cauc', 'zomb_a_body'], ['PM_tm_body_cauc', 'zomb_a_body']]
face_textures = [
 'male_face_cauc_a', 'male_face_cauc_b', 'male_face_asian_a', 'male_face_dark_a', 'male_face_cauc_c', 'male_face_asian_b', 'male_face_dark_b']
PC_FACE_CHOICES = [
 0, 1, 2, 3]
PC_HAIR_CHOICES = [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13]
PC_HAT_CHOICES = {0: [0], 2: [0], 6: [0], 7: [0], 8: [0]}
PC_SHIRT_CHOICES = {1: [0, 1, 2, 3, 4], 2: [0, 1, 3], 3: [0, 1, 2], 4: [1], 6: [0, 1, 2, 3], 7: [1, 2], 8: [2]}
PC_VEST_CHOICES = {0: [0], 1: [0, 1, 2, 4], 2: [0, 2, 4]}
PC_COAT_CHOICES = {0: [0], 1: [0], 2: [0]}
PC_PANT_CHOICES = {0: [0, 1, 2, 3], 1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
PC_BELT_CHOICES = {0: [0], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0]}
PC_SOCK_CHOICES = {0: [0]}
PC_SHOE_CHOICES = {0: [0], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3]}
NPC_FACE_CHOICES = [
 0, 1, 2, 3, 4, 5, 6]
NPC_HAIR_CHOICES = [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13]
NPC_HAT_CHOICES = {0: [0], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0], 6: [0], 7: [0], 8: [0], 9: [0]}
NPC_SHIRT_CHOICES = {0: [0], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3], 4: [0, 1, 2], 5: [0, 1, 2], 6: [0, 1, 2, 3], 7: [0, 1, 2], 8: [0, 1, 2], 9: [0, 1, 2], 10: [0]}
NPC_VEST_CHOICES = {0: [0], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0]}
NPC_COAT_CHOICES = {0: [0], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0], 4: [0]}
NPC_PANT_CHOICES = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3], 4: [0], 5: [0], 6: [0, 1, 2]}
NPC_BELT_CHOICES = {0: [0], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0]}
NPC_SOCK_CHOICES = {0: [0]}
NPC_SHOE_CHOICES = {0: [0], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [0], 4: [0]}
eye_iris_textures = [
 'pupilAqua', 'pupilBlue', 'pupilDarkBrown', 'pupilGreen', 'pupilHazel', 'pupilLightBrown']
male_hairs = [
 'style 0: bald', 'style 1: base w/A_top', 'style 2: base w/A1_top', 'style 3: base w/A_top + A2_sides', 'style 4: base w/A1_top + A2_sides', 'style 5: base w/A_top + B_ponytail', 'style 6: base w/A1_top + B_ponytail', 'style 8: base w/A_top + E_spike', 'style 9: base w/A1_top + E_spike', 'style 10: balding f0', 'style 11: balding g0', 'style 12: base w/A_top + H_mullet', 'style 13: base w/A1_top + H_mullet', 'style 14: mohawk i0']
shirt_styles = [
 'S_none', 'S_tanktop', 'S_no_sleeve', 'S_short_sleeve_round_neck', 'S_short_sleeve_vneck_closed', 'S_short_sleeve_vneck_open', 'S_long_sleeve_lowcut_puffy', 'S_long_sleeve_lowcut_puffy_tuck', 'S_long_sleeve_vneck_closed', 'S_long_sleeve_vneck_open']
vector_tattoos = [
 [
  0, 0.127, 0.194, 0.191, 0, 0], [0, 0.203, 0.579, 0.079, 271.1, 0], [0, 0.203, 0.831, 0.079, 271.1, 0], [0, 0.5, 0.5, 1.0, 0, 0], [0, 0.13, 0.35, 0.1, 0, 0], [0, 0.5, 0.5, 0.1, 0, 0], [0, 0.5, 0.5, 0.1, 0, 0], [0, 0.5, 0.5, 0.1, 0, 0]]
jewelry_geos_face = [
 'acc_none', 'acc_face_brow_spike_right', 'acc_face_brow_ring_right', 'acc_face_brow_spike_left', 'acc_face_brow_ring_left', 'acc_face_ear_stud_left', 'acc_face_ear_open_left', 'acc_face_ear_spike_top_left', 'acc_face_ear_hoop_b_left', 'acc_face_ear_hoop_a_left', 'acc_face_ear_spike_bot_left', 'acc_face_ear_bighoop_left', 'acc_face_ear_cuff_c_left', 'acc_face_ear_cuff_b_left', 'acc_face_ear_cuff_a_left', 'acc_face_ear_cuff_a_right', 'acc_face_ear_open_right', 'acc_face_ear_stud_right', 'acc_face_ear_spike_top_right', 'acc_face_ear_hoop_b_right', 'acc_face_ear_hoop_a_right', 'acc_face_ear_spike_bot_right', 'acc_face_ear_bighoop_right', 'acc_face_ear_cuff_c_right', 'acc_face_ear_cuff_b_right', 'acc_face_lip_ring_top_left', 'acc_face_lip_ring_bot_left', 'acc_face_lip_ring_center', 'acc_face_lip_ring_bot_right', 'acc_face_lip_ring_top_right', 'acc_face_lip_jawry', 'acc_face_nose_ring_right', 'acc_face_nose_post_top', 'acc_face_nose_post_bot', 'acc_face_nose_ring_left', 'acc_face_nose_ring_center']
jewelry_geos_body = [
 'acc_none', 'acc_body_ring_left_index_base', 'acc_body_ring_left_index_stone', 'acc_body_ring_left_mid_base', 'acc_body_ring_left_mid_stone', 'acc_body_ring_left_ring_base', 'acc_body_ring_left_ring_stone', 'acc_body_ring_left_pinky_base', 'acc_body_ring_left_pinky_stone', 'acc_body_ring_right_index_base', 'acc_body_ring_right_index_stone', 'acc_body_ring_right_mid_base', 'acc_body_ring_right_mid_stone', 'acc_body_ring_right_ring_base', 'acc_body_ring_right_ring_stone', 'acc_body_ring_right_pinky_base', 'acc_body_ring_right_pinky_stone']
jewelry_options = {'RBrow': [[0], [1], [2]], 'LBrow': [[0], [3], [4]], 'LEar': [[0], [5], [6], [7], [8, 9], [10], [11], [12], [13], [14], [11, 12, 13], [12, 13], [6, 7], [5, 12, 13]], 'REar': [[0], [15], [16], [17], [18], [19, 20], [21], [22], [23], [24], [22, 23, 24], [23, 24], [16, 18], [17, 23, 24]], 'Nose': [[0], [31], [32], [33], [34], [35], [32, 33], [32, 34]], 'Mouth': [[0], [25], [26], [27], [28], [29], [30], [25, 28], [27, 28]], 'LHand': [[0], [1], [1, 2], [3], [3, 4], [5], [5, 6], [7], [7, 8], [1, 3], [1, 5], [3, 7]], 'RHand': [[0], [9], [9, 10], [11], [11, 12], [13], [13, 14], [15], [15, 16], [9, 11], [9, 13], [11, 15]]}
clothes_textures = ClothingGlobals.textures['MALE']
SliderNames = [
 'headWidth', 'headHeight', 'headRoundness', 'jawWidth', 'jawChinAngle', 'jawChinSize', 'jawLength', 'mouthWidth', 'mouthLipThickness', 'cheekFat', 'browProtruding', 'eyeCorner', 'eyeOpeningSize', 'eyeSpacing', 'noseBridgeWidth', 'noseNostrilWidth', 'noseLength', 'noseBump', 'noseNostrilHeight', 'noseNostrilAngle', 'noseBridgeBroke', 'noseNostrilBroke', 'earScale', 'earFlap', 'earPosition']
ControlShapes = {'headWidth': [[['def_trs_left_forehead', TX, 0.224, 0, 0, 0], ['def_trs_right_forehead', TX, -0.224, 0, 0, 0]], [['def_trs_left_forehead', TX, 0.224, 0, 0, 0], ['def_trs_right_forehead', TX, -0.224, 0, 0, 0]]], 'headHeight': [[['def_trs_forehead', TZ, 0.663, 0, 0, 0], ['def_trs_left_forehead', TZ, 0.569, 0, 0, 0], ['def_trs_right_forehead', TZ, 0.569, 0, 0, 0]], [['def_trs_forehead', TZ, 0.663, 0, 0, 0], ['def_trs_left_forehead', TZ, 0.569, 0, 0, 0], ['def_trs_right_forehead', TZ, 0.569, 0, 0, 0]]], 'headRoundness': [[['def_trs_forehead', TZ, 0.608, 0, 0, 0], ['def_trs_left_forehead', TZ, 0.574, 0, 0, 0], ['def_trs_right_forehead', TZ, 0.574, 0, 0, 0], ['def_trs_mid_jaw', TZ, -0.176, 0, 0, 0], ['def_trs_mid_jaw', TY, -0.288, 0, 0, 0]]], 'jawWidth': [[['def_trs_left_jaw2', TX, 0.218, 0, 0, 0], ['def_trs_right_jaw2', TX, -0.218, 0, 0, 0]], [['def_trs_left_jaw2', TX, 0.218, 0, 0, 0], ['def_trs_right_jaw2', TX, -0.218, 0, 0, 0]]], 'jawLength': [[['trs_face_bottom', TZ, -0.02, 0, 0, 0]], [['trs_face_bottom', TZ, -0.02, 0, 0, 0]]], 'jawChinAngle': [[['def_trs_left_jaw1', TY, -0.234, 0, 0, 0], ['def_trs_right_jaw1', TY, -0.234, 0, 0, 0], ['def_trs_mid_jaw', TY, -0.313, 0, 0, 0]], [['def_trs_left_jaw1', TY, -0.234, 0, 0, 0], ['def_trs_right_jaw1', TY, -0.234, 0, 0, 0], ['def_trs_mid_jaw', TY, -0.313, 0, 0, 0]]], 'jawChinSize': [[['def_trs_left_jaw1', TX, 0.114, 0, 0, 0], ['def_trs_left_jaw1', TY, -0.209, 0, 0, 0], ['def_trs_left_jaw1', TZ, -0.118, 0, 0, 0], ['def_trs_right_jaw1', TX, -0.114, 0, 0, 0], ['def_trs_right_jaw1', TY, -0.209, 0, 0, 0], ['def_trs_right_jaw1', TZ, -0.118, 0, 0, 0], ['def_trs_mid_jaw', TZ, -0.201, 0, 0, 0]], [['def_trs_left_jaw1', TX, 0.114, 0, 0, 0], ['def_trs_left_jaw1', TY, -0.209, 0, 0, 0], ['def_trs_left_jaw1', TZ, -0.118, 0, 0, 0], ['def_trs_right_jaw1', TX, -0.114, 0, 0, 0], ['def_trs_right_jaw1', TY, -0.209, 0, 0, 0], ['def_trs_right_jaw1', TZ, -0.118, 0, 0, 0], ['def_trs_mid_jaw', TZ, -0.201, 0, 0, 0]]], 'mouthWidth': [[['trs_lips_top', SX, 1.2, 0, 0, 0], ['trs_lips_bot', SX, 1.2, 0, 0, 0]]], 'mouthLipThickness': [[['trs_lip_top', SZ, 1.2, 0, 0, 0], ['trs_lip_bot', SZ, 1.2, 0, 0, 0], ['trs_lip_left1', SZ, 1.2, 0, 0, 0], ['trs_lip_right1', SZ, 1.2, 0, 0, 0], ['trs_lip_left2', SZ, 1.2, 0, 0, 0], ['trs_lip_right2', SZ, 1.2, 0, 0, 0], ['trs_lip_left3', SZ, 1.2, 0, 0, 0], ['trs_lip_right3', SZ, 1.2, 0, 0, 0]], [['trs_lip_top', SZ, 1.2, 0, 0, 0], ['trs_lip_bot', SZ, 1.2, 0, 0, 0], ['trs_lip_left1', SZ, 1.2, 0, 0, 0], ['trs_lip_right1', SZ, 1.2, 0, 0, 0], ['trs_lip_left2', SZ, 1.2, 0, 0, 0], ['trs_lip_right2', SZ, 1.2, 0, 0, 0], ['trs_lip_left3', SZ, 1.2, 0, 0, 0], ['trs_lip_right3', SZ, 1.2, 0, 0, 0]]], 'cheekFat': [[['def_trs_left_cheek', TX, 0.216, 0, 0, 0], ['def_trs_right_cheek', TX, -0.216, 0, 0, 0]], [['def_trs_left_cheek', TX, 0.216, 0, 0, 0], ['def_trs_right_cheek', TX, -0.216, 0, 0, 0]]], 'browProtruding': [[['trs_left_eyebrow', TY, -0.05, 0, 0, 0], ['trs_right_eyebrow', TY, 0.05, 0, 0, 0]]], 'eyeCorner': [[['trs_left_eyesocket', RZ, 45 - 10, 0, 0, 0], ['trs_right_eyesocket', RZ, -(45 - 10), 0, 0, 0]], [['trs_left_eyesocket', RZ, 45 - 10, 0, 0, 0], ['trs_right_eyesocket', RZ, -(45 - 10), 0, 0, 0]]], 'eyeOpeningSize': [[['trs_left_eyesocket', SX, 1.1, 0, 0, 0], ['trs_left_eyesocket', SZ, 1.1, 0, 0, 0], ['trs_right_eyesocket', SX, 1.1, 0, 0, 0], ['trs_right_eyesocket', SZ, 1.1, 0, 0, 0]], [['trs_left_eyesocket', SX, 1.1, 0, 0, 0], ['trs_left_eyesocket', SZ, 1.1, 0, 0, 0], ['trs_right_eyesocket', SX, 1.1, 0, 0, 0], ['trs_right_eyesocket', SZ, 1.1, 0, 0, 0]]], 'eyeSpacing': [[['trs_left_eyesocket', TX, 0.008, 0, 0, 0], ['trs_right_eyesocket', TX, -0.008, 0, 0, 0]], [['trs_left_eyesocket', TX, 0.008, 0, 0, 0], ['trs_right_eyesocket', TX, -0.008, 0, 0, 0]]], 'noseBridgeWidth': [[['def_trs_mid_nose_top', SX, 1.25, 0, 0, 0]], [['def_trs_mid_nose_top', SX, 1.25, 0, 0, 0]]], 'noseNostrilWidth': [[['def_trs_mid_nose_bot', SX, 1.2, 0, 0, 0]], [['def_trs_mid_nose_bot', SX, 1.2, 0, 0, 0]]], 'noseLength': [[['def_trs_mid_nose_bot', TZ, 0.112, 0, 0, 0]], [['def_trs_mid_nose_bot', TZ, 0.112, 0, 0, 0]]], 'noseBump': [[['def_trs_mid_nose_top', TY, -0.442, 0, 0, 0], ['def_trs_mid_nose_top', TZ, 0.265, 0, 0, 0]], [['def_trs_mid_nose_top', TY, -0.442, 0, 0, 0], ['def_trs_mid_nose_top', TZ, 0.265, 0, 0, 0]]], 'noseBridgeBroke': [[['def_trs_mid_nose_top', TX, 0.015, 0, 0, 0]], [['def_trs_mid_nose_top', TX, 0.015, 0, 0, 0]]], 'noseNostrilHeight': [[['def_trs_mid_nose_bot', SY, 1.25, 0, 0, 0]], [['def_trs_mid_nose_bot', SY, 1.25, 0, 0, 0]]], 'noseNostrilAngle': [[['def_trs_mid_nose_bot', RY, 15, 0, 0, 0]], [['def_trs_mid_nose_bot', RY, 15, 0, 0, 0]]], 'noseNostrilBroke': [[['def_trs_mid_nose_bot', TX, 0.015, 0, 0, 0]], [['def_trs_mid_nose_bot', TX, 0.015, 0, 0, 0]]], 'earScale': [[['def_trs_left_ear', SZ, 1.1, 0, 0, 0], ['def_trs_right_ear', SZ, 1.1, 0, 0, 0], ['def_trs_left_ear', SX, 1.1, 0, 0, 0], ['def_trs_right_ear', SX, 1.1, 0, 0, 0]], [['def_trs_left_ear', SZ, 1.1, 0, 0, 0], ['def_trs_right_ear', SZ, 1.1, 0, 0, 0], ['def_trs_left_ear', SX, 1.1, 0, 0, 0], ['def_trs_right_ear', SX, 1.1, 0, 0, 0]]], 'earFlap': [[['def_trs_left_ear', RX, -20, 0, 0, 0], ['def_trs_right_ear', RX, -160, 0, 0, 0]], [['def_trs_left_ear', RX, -20, 0, 0, 0], ['def_trs_right_ear', RX, -160, 0, 0, 0]]], 'earPosition': [[['def_trs_left_ear', TZ, 0.216, 0, 0, 0], ['def_trs_right_ear', TZ, 0.216, 0, 0, 0]], [['def_trs_left_ear', TZ, 0.216, 0, 0, 0], ['def_trs_right_ear', TZ, 0.216, 0, 0, 0]]]}

class PirateMale(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('PirateMale')

    def __init__(self, pirate, dna):
        self.pirate = pirate
        self.dna = dna
        self.dnaZomb = HumanDNA.HumanDNA()
        self.makeZombie()
        self.loaded = 0
        self.texDict = {}
        self.bodySets = [{}, {}, {}]
        self.tattooZones = [
         [
          1, 2, 3, 4, 5], [9, 11, 13], [8, 10, 12], [-1], [0], [2], [16, 17], [18, 19]]
        self.tattooStage = TextureStage('tattoo')
        self.tattooStage.setTexcoordName('tattoomap')
        self.tattoos = [
         1, 2, 3, 4, 5, 6, 7, 8]
        self.currentClothing = {'HAT': [0, 0, 0], 'SHIRT': [0, 0, 0], 'VEST': [0, 0, 0], 'COAT': [0, 0, 0], 'BELT': [0, 0, 0], 'PANT': [0, 0, 0], 'SHOE': [0, 0, 0]}
        self.currentClothingModels = {'HAT': NodePathCollection(), 'HAIR': NodePathCollection(), 'BEARD': NodePathCollection(), 'MUSTACHE': NodePathCollection(), 'SHIRT': NodePathCollection(), 'VEST': NodePathCollection(), 'COAT': NodePathCollection(), 'BELT': [NodePathCollection(), NodePathCollection()], 'PANT': NodePathCollection(), 'SHOE': NodePathCollection()}
        self.currentBody = NodePathCollection()
        self.currentBody.addPath(NodePath('temp'))
        self.currentBody.addPath(NodePath('temp'))
        self.currentBody.addPath(NodePath('temp'))
        self.currentTatttooZones = [
         NodePathCollection(), NodePathCollection(), NodePathCollection()]
        self.newAvatars = base.config.GetBool('want-new-avatars', 0)

    def delete(self):
        del self.pirate
        del self.dna
        del self.dnaZomb

    def setHairBaseColor(self):
        dna = self.pirate.style
        if self.pirate.zombie:
            dna = self.dnaZomb
        baseColor = dna.getHairBaseColor()
        self.currentClothingModels['HAIR'].setColorScale(baseColor)
        self.currentClothingModels['BEARD'].setColorScale(baseColor)
        self.currentClothingModels['MUSTACHE'].setColorScale(baseColor)
        self.eyeBrows.setColorScale(baseColor)

    def setupTattoos(self):
        if not hasattr(base, 'cr'):
            self.tattoos[0] = self.pirate.style.getTattooChest()
            self.tattoos[1] = self.pirate.style.getTattooZone2()
            self.tattoos[2] = self.pirate.style.getTattooZone3()
            self.tattoos[3] = self.pirate.style.getTattooZone4()
            self.tattoos[4] = self.pirate.style.getTattooZone5()
            self.tattoos[5] = self.pirate.style.getTattooZone6()
            self.tattoos[6] = self.pirate.style.getTattooZone7()
            self.tattoos[7] = self.pirate.style.getTattooZone8()
        else:
            if self.pirate.isPaid == True:
                self.tattoos[0] = self.pirate.style.getTattooChest()
                self.tattoos[1] = self.pirate.style.getTattooZone2()
                self.tattoos[2] = self.pirate.style.getTattooZone3()
                self.tattoos[3] = self.pirate.style.getTattooZone4()
                self.tattoos[4] = self.pirate.style.getTattooZone5()
                self.tattoos[5] = self.pirate.style.getTattooZone6()
                self.tattoos[6] = self.pirate.style.getTattooZone7()
                self.tattoos[7] = self.pirate.style.getTattooZone8()
            else:
                self.tattoos[0] = [
                 0, 0, 0, 1, 0, 0]
                self.tattoos[1] = [0, 0, 0, 1, 0, 0]
                self.tattoos[2] = [0, 0, 0, 1, 0, 0]
                self.tattoos[3] = [0, 0, 0, 1, 0, 0]
                self.tattoos[4] = [0, 0, 0, 1, 0, 0]
                self.tattoos[5] = [0, 0, 0, 1, 0, 0]
                self.tattoos[6] = [0, 0, 0, 1, 0, 0]
                self.tattoos[7] = [0, 0, 0, 1, 0, 0]
        for i in range(4):
            tattooArea = self.currentTattooZones[i]
            tattoo = self.tattoos[i]
            zones = self.tattooZones[i]
            tex = TattooGlobals.getTattooImage(tattoo[0])
            scale = float(tex.getXSize()) / float(tex.getYSize())
            scaleX = tattoo[3] * scale
            scaleY = tattoo[3]
            t = TransformState.makePosRotateScale2d(Vec2(tattoo[1], tattoo[2]), tattoo[4], Vec2(scaleX, scaleY))
            tex.setWrapU(Texture.WMBorderColor)
            tex.setWrapV(Texture.WMBorderColor)
            tex.setBorderColor(VBase4(1.0, 1.0, 1.0, 0.0))
            for j in range(tattooArea.getNumPaths()):
                part = tattooArea[j]
                part.setTexTransform(self.tattooStage, t)

            tattooArea.setTexture(self.tattooStage, tex)

    def updateTattoo(self, index):
        if index > 3:
            return
        tattoo = self.tattoos[index]
        tattooArea = self.currentTattooZones[index]
        tex = TattooGlobals.getTattooImage(tattoo[0])
        scale = float(tex.getXSize()) / float(tex.getYSize())
        scaleX = tattoo[3] * scale
        scaleY = tattoo[3]
        t = TransformState.makePosRotateScale2d(Vec2(tattoo[1], tattoo[2]), tattoo[4], Vec2(scaleX, scaleY))
        tex.setWrapU(Texture.WMBorderColor)
        tex.setWrapV(Texture.WMBorderColor)
        tex.setBorderColor(VBase4(1.0, 1.0, 1.0, 0.0))
        tattooArea.setTexture(self.tattooStage, tex)
        for j in range(tattooArea.getNumPaths()):
            tattooArea[j].setTexTransform(self.tattooStage, t)

    def setupHairMultiTexture(self):

        def setupMultiTexture(parts):
            for i in range(0, len(parts)):
                if not parts[i].isEmpty():
                    for j in range(0, parts[i].getNumPaths()):
                        hair = parts[i][j]
                        tc = hair.findAllTextureStages()
                        for k in range(0, tc.getNumTextureStages()):
                            if tc[k].getName().find('dummy') != -1:
                                tc.removeTextureStage(tc[k])
                                break

                        for k in range(0, tc.getNumTextureStages()):
                            if tc[k].getTexcoordName().getName().find('light') != -1:
                                tc[k].setMode(TextureStage.MBlend)
                                tc[k].setSort(10)
                            elif tc[k].getTexcoordName().getName().find('dark') != -1:
                                tc[k].setSort(0)

        setupMultiTexture(self.hairPieces)
        setupMultiTexture(self.beards)
        setupMultiTexture(self.mustaches)
        setupMultiTexture(self.eyeBrows)

    def showHair(self):
        for i in range(0, len(self.hairs[self.hairIdx])):
            pi = self.hairs[self.hairIdx][i]
            if not self.hairPieces[pi].isEmpty():
                self.hairPieces[pi].unstash()

    def hideHair(self):
        for i in range(0, len(self.hairs[self.hairIdx])):
            if not self.hairPieces[self.hairs[self.hairIdx][i]].isEmpty():
                self.hairPieces[self.hairs[self.hairIdx][i]].stash()
            if not self.hairCuts[self.hairs[self.hairIdx][i]].isEmpty():
                self.hairCuts[self.hairs[self.hairIdx][i]].stash()

    def handleHeadHiding(self):
        hairIdx = [self.pirate.style.getHairHair(), self.pirate.style.getHairBaseColor()]
        hatIdx = self.pirate.style.getClothesHat() + [self.pirate.style.getHatColor()]
        if self.pirate.zombie:
            hatIdx = [
             ZOMB_HAT, 0, 0]
            hatColor = self.dnaZomb.lookupHatColor()
        else:
            hatColor = HumanDNA.hatColors[0][hatIdx[2]]
        currentHat = self.hatSets[hatIdx[0]]
        currentHair = self.hairSets[hairIdx[0]][hatIdx[0]]
        self.currentClothingModels['HAIR'].stash()
        currentHair.unstash()
        self.currentClothingModels['BEARD'].stash()
        self.currentClothingModels['MUSTACHE'].stash()
        currentBeardIdx = self.pirate.style.getHairBeard()
        currentBeard = self.beards[currentBeardIdx]
        currentStache = self.mustaches[self.pirate.style.getHairMustache()]
        baseColor = self.pirate.style.getHairBaseColor()
        currentBeard.setColorScale(baseColor)
        currentStache.setColorScale(baseColor)
        currentBeard.unstash()
        if not (currentBeardIdx > 0 and currentBeardIdx < 4):
            currentStache.unstash()
        self.currentClothingModels['BEARD'] = currentBeard
        self.currentClothingModels['MUSTACHE'] = currentStache
        self.currentClothingModels['HAIR'] = currentHair
        self.currentClothingModels['HAT'].stash()
        texInfo = clothes_textures['HAT'][hatIdx[0]][hatIdx[1]]
        texName = texInfo[0].split('+')
        if self.texDict[texName[0]]:
            if len(texName) > 1:
                for base in (0, 2, 4):
                    currentHat[base].setTexture(self.texDict[texName[0]], 3)
                    currentHat[base + 1].setTexture(self.texDict[texName[1]], 4)

            else:
                currentHat.setTexture(self.texDict[texName[0]])
            currentHat.setColorScale(hatColor)
            if self.pirate.optimizeLOD:
                for i in xrange(currentHat.getNumPaths() * 2 / 3, currentHat.getNumPaths()):
                    currentHat[i].setColorScale(VBase4(texInfo[1][0] * hatColor[0], texInfo[1][1] * hatColor[1], texInfo[1][2] * hatColor[2], 1))

        self.currentClothingModels['HAT'] = currentHat
        if hatIdx[0] > 0:
            currentHat.setColorScale(hatColor)
            currentHat.unstash()
            if hatIdx[0] == 7:
                if hairIdx[0] in [0, 9, 10, 13]:
                    for i in range(0, currentHat.getNumPaths()):
                        if currentHat[i].getName().find('bald') == -1:
                            currentHat[i].stash()

                else:
                    for i in range(0, currentHat.getNumPaths()):
                        if currentHat[i].getName().find('bald') != -1:
                            currentHat[i].stash()

            if self.pirate.optimizeLOD:
                lowLODColor = self.getTextureName('HAT', hatIdx[0], 0)[1]
                if currentHat.getNumPaths() > 1:
                    currentHat[2].setColorScale(VBase4(lowLODColor[0] * hatColor[0], lowLODColor[1] * hatColor[1], lowLODColor[2] * hatColor[2], 1))
        self.setHairBaseColor()

    def showFacialHair(self):
        self.currentClothingModels['BEARD'].stash()
        self.currentClothingModels['MUSTACHE'].stash()
        currentBeard = self.beards[self.beardIdx]
        currentStache = self.mustaches[self.mustacheIdx]
        baseColor = self.pirate.style.getHairBaseColor()
        currentBeard.setColorScale(baseColor)
        currentStache.setColorScale(baseColor)
        currentBeard.unstash()
        if not (self.beardIdx > 0 and self.beardIdx < 4):
            currentStache.unstash()
        self.currentClothingModels['BEARD'] = currentBeard
        self.currentClothingModels['MUSTACHE'] = currentStache

    def setupHead(self, lodName='2000'):
        geom = self.pirate.getGeomNode()
        self.faceZomb = geom.findAllMatches('**/gh_master_face')
        self.faces = []
        faceData = NodePathCollection()
        irisData = NodePathCollection()
        eyeData = NodePathCollection()
        for lod in ['2000', '1000', '500']:
            flattenMe = NodePath('flattenMe')
            lodNP = self.pirate.getLOD(lod)
            faceSet = lodNP.findAllMatches('**/body_master_face')
            faceSet.addPathsFrom(lodNP.findAllMatches('**/eyelid*'))
            for i in xrange(faceSet.getNumPaths()):
                faceSet[i].copyTo(flattenMe)

            flattenMe.flattenStrong()
            faceParts = flattenMe.findAllMatches('**/+GeomNode')
            lodNP.findAllMatches('**/body_master_face').detach()
            lodNP.findAllMatches('**/eyelid*').detach()
            faceParts.reparentTo(lodNP.getChild(0))
            faceData.addPathsFrom(faceParts)
            flattenMe = NodePath('flattenMe')
            eyeballs = lodNP.findAllMatches('**/eye_ball*')
            for i in xrange(eyeballs.getNumPaths()):
                eyeballs[i].copyTo(flattenMe)

            flattenMe.flattenStrong()
            eyeBallParts = flattenMe.findAllMatches('**/+GeomNode')
            lodNP.findAllMatches('**/eye_ball*').detach()
            eyeBallParts.reparentTo(lodNP.getChild(0))
            eyeData.addPathsFrom(eyeBallParts)
            irisSet = lodNP.findAllMatches('**/eye_iris*')
            flattenMe = NodePath('flattenMe')
            for i in xrange(irisSet.getNumPaths()):
                irisSet[i].copyTo(flattenMe)

            flattenMe.flattenStrong()
            lodNP.findAllMatches('**/eye_iris*').detach()
            irisParts = flattenMe.findAllMatches('**/+GeomNode')
            irisParts.reparentTo(lodNP.getChild(0))
            irisData.addPathsFrom(irisParts)

        self.faces.append(faceData)
        self.irises = irisData
        self.eyeBalls = eyeData
        self.teeth = geom.findAllMatches('**/teeth*')
        self.tooths = []
        self.toothIdx = 0
        self.tooths.append(geom.findAllMatches('**/teeth_none*'))
        self.tooths.append(geom.findAllMatches('**/teeth_all*'))
        self.eyeBrow = geom.findAllMatches('**/hair_eyebrow_*')
        self.eyeBrows = []
        self.eyeBrowIdx = 0
        self.eyeBrows = NodePathCollection()
        for lod in ['2000', '1000', '500']:
            eyebrows = self.pirate.getLOD(lod).findAllMatches('**/hair_eyebrow_*')
            flattenMe = NodePath('flattenMe')
            for i in xrange(eyebrows.getNumPaths()):
                eyebrows[i].copyTo(flattenMe)

            flattenMe.flattenStrong()
            geoms = flattenMe.findAllMatches('**/+GeomNode')
            self.pirate.getLOD(lod).findAllMatches('**/hair_eyebrow_*').detach()
            geoms.reparentTo(self.pirate.getLOD(lod).getChild(0))
            self.eyeBrows.addPathsFrom(geoms)

        self.eyeBrows.stash()
        if base.config.GetBool('want-gen-pics-buttons'):
            self.eyes = self.pirate.findAllMatches('**/eye_*')
        self.hair = geom.findAllMatches('**/hair*')
        hairList = [
         '**/hair_none*', '**/hair_base', '**/hair_a0', '**/hair_a1', '**/hair_a2', '**/hair_b1', '**/hair_d0', '**/hair_e1', '**/hair_f0', '**/hair_g0', '**/hair_h0', '**/hair_i0']
        self.hairPieces = []
        self.hairPieces.append(geom.findAllMatches('**/hair_none*'))
        self.hairPieces.append(geom.findAllMatches('**/hair_base'))
        self.hairPieces.append(geom.findAllMatches('**/hair_a0'))
        self.hairPieces.append(geom.findAllMatches('**/hair_a1'))
        self.hairPieces.append(geom.findAllMatches('**/hair_a2'))
        self.hairPieces.append(geom.findAllMatches('**/hair_b1'))
        self.hairPieces.append(geom.findAllMatches('**/hair_d0'))
        self.hairPieces.append(geom.findAllMatches('**/hair_e1'))
        self.hairPieces.append(geom.findAllMatches('**/hair_f0'))
        self.hairPieces.append(geom.findAllMatches('**/hair_g0'))
        self.hairPieces.append(geom.findAllMatches('**/hair_h0'))
        self.hairPieces.append(geom.findAllMatches('**/hair_i0'))
        self.hairs = []
        self.hairIdx = self.pirate.style.getHairHair()
        self.hairs.append([0])
        self.hairs.append([1, 2])
        self.hairs.append([1, 3])
        self.hairs.append([1, 2, 4])
        self.hairs.append([1, 3, 4])
        self.hairs.append([1, 2, 5])
        self.hairs.append([1, 3, 5])
        self.hairs.append([1, 2, 7])
        self.hairs.append([1, 3, 7])
        self.hairs.append([8])
        self.hairs.append([9])
        self.hairs.append([1, 2, 10])
        self.hairs.append([1, 3, 10])
        self.hairs.append([11])
        hairCutList = [
         '**/hair_none*', '**/hair_base_cut*', '**/hair_a0_cut*', '**/hair_a1_cut*', '**/hair_a2_cut*', '**/hair_b1_cut*', '**/hair_d0_cut*', '**/hair_e1_cut*', '**/hair_f0_cut*', '**/hair_g0_cut*', '**/hair_h0_cut*', '**/hair_i0_cut*']
        self.hairCuts = []
        self.hairCuts.append(geom.findAllMatches('**/hair_none*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_base_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_a0_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_a1_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_a2_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_b1_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_d0_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_e1_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_f0_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_g0_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_h0_cut*'))
        self.hairCuts.append(geom.findAllMatches('**/hair_i0_cut*'))
        self.beard = geom.findAllMatches('**/beard_*')
        self.beards = []
        self.beardIdx = self.pirate.style.getHairBeard()
        self.beards.append(geom.findAllMatches('**/beard_none*'))
        self.beards.append(geom.findAllMatches('**/beard_a0*'))
        self.beards.append(geom.findAllMatches('**/beard_a1*'))
        self.beards.append(geom.findAllMatches('**/beard_h0*'))
        self.beards.append(geom.findAllMatches('**/beard_c1*'))
        self.beards.append(geom.findAllMatches('**/beard_c2*'))
        self.beards.append(geom.findAllMatches('**/beard_c3*'))
        self.beards.append(geom.findAllMatches('**/beard_f0*'))
        self.beards.append(geom.findAllMatches('**/beard_f1*'))
        self.beards.append(geom.findAllMatches('**/beard_g0*'))
        self.beards.append(geom.findAllMatches('**/beard_i0*'))
        self.beard.stash()
        self.mustache = geom.findAllMatches('**/mustache_*')
        self.mustaches = []
        self.mustacheIdx = self.pirate.style.getHairMustache()
        self.mustaches.append(geom.findAllMatches('**/mustache_none*'))
        self.mustaches.append(geom.findAllMatches('**/mustache_d0*'))
        self.mustaches.append(geom.findAllMatches('**/mustache_d1*'))
        self.mustaches.append(geom.findAllMatches('**/mustache_d2*'))
        self.mustaches.append(geom.findAllMatches('**/mustache_d3*'))
        self.mustaches.append(geom.findAllMatches('**/mustache_e0*'))
        self.mustaches.append(geom.findAllMatches('**/mustache_e1*'))
        self.mustache.stash()
        self.eyeBrows.unstash()
        self.hat = geom.findAllMatches('**/clothing_layer1_hat_*')
        self.hats = []
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_none'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_captain'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_tricorn'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_navy'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_india_navy'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_admiral'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_bandanna_full'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_bandanna_reg*'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_band_beanie'))
        self.hats.append(geom.findAllMatches('**/clothing_layer1_hat_barbossa'))
        self.hat.stash()
        self.eyepatch = geom.findAllMatches('**/eye_patch*')
        self.eyepatch.stash()
        self.wig = geom.findAllMatches('**/wig*')
        self.wig.stash()
        self.jewelryFaceParts = []
        for name in jewelry_geos_face:
            self.jewelryFaceParts.append(self.pirate.findAllMatches('**/%s' % name))

        self.jewelryBodyParts = []
        for name in jewelry_geos_body:
            self.jewelryBodyParts.append(self.pirate.findAllMatches('**/%s' % name))

        for npc in self.jewelryFaceParts:
            length = npc.getNumPaths()
            for i in range(length):
                node = npc[i]
                node.showThrough(OTPRender.GlowCameraBitmask)

        for npc in self.jewelryBodyParts:
            length = npc.getNumPaths()
            for i in range(length):
                node = npc[i]
                node.showThrough(OTPRender.GlowCameraBitmask)

        self.accBody = geom.findAllMatches('**/acc_body*')
        self.numBodyJewelry = self.accBody.getNumPaths()
        self.accFace = geom.findAllMatches('**/acc_face*')
        self.numFaceJewelry = self.accFace.getNumPaths()
        self.accBody.stash()
        self.accFace.stash()
        self.jewelrySets = {}
        for key in jewelry_options.keys():
            self.jewelrySets[key] = []
            options = jewelry_options[key]
            if key == 'LHand' or key == 'RHand':
                parts = self.jewelryBodyParts
            else:
                parts = self.jewelryFaceParts
            for piece in options:
                primary = NodePathCollection()
                secondary = NodePathCollection()
                length = len(piece)
                if length == 1:
                    primary.addPathsFrom(parts[piece[0]])
                else:
                    if length > 1:
                        primary.addPathsFrom(parts[piece[0]])
                        for idx in range(1, length):
                            secondary.addPathsFrom(parts[piece[idx]])

                data = [
                 primary, secondary]
                self.jewelrySets[key].append(data)

        self.currentJewelry = {'LEar': [0, 0, 0], 'REar': [0, 0, 0], 'LBrow': [0, 0, 0], 'RBrow': [0, 0, 0], 'Nose': [0, 0, 0], 'Mouth': [0, 0, 0], 'LHand': [0, 0, 0], 'RHand': [0, 0, 0]}
        self.hairLODs = []
        self.hairCutLODs = []
        for item in hairList:
            itemInfo = {}
            for lod in ['500', '1000', '2000']:
                itemInfo[lod] = self.pirate.getLOD(lod).findAllMatches(item)

            self.hairLODs.append(itemInfo)

        for item in hairCutList:
            itemInfo = {}
            for lod in ['500', '1000', '2000']:
                itemInfo[lod] = self.pirate.getLOD(lod).findAllMatches(item)

            self.hairCutLODs.append(itemInfo)

        self.generateHairSets()
        self.hair.stash()

    def setBlendValue(self, val, attr):
        self.pirate.setBlendValue(0.0, self.blendShapes[attr][0])
        if len(self.blendShapes[attr]) > 1:
            self.pirate.setBlendValue(0.0, self.blendShapes[attr][1])
        if val >= 0.0:
            if len(self.blendShapes[attr]) > 1:
                blendName = self.blendShapes[attr][1]
            else:
                blendName = self.blendShapes[attr][0]
        else:
            blendName = self.blendShapes[attr][0]
            val = -val
        self.pirate.setBlendValue(val, blendName)

    def setupBody(self, lodName=2000):
        geom = self.pirate.getGeomNode()
        self.body = self.pirate.findAllMatches('**/body_*')
        faceParts = []
        for i in xrange(self.body.getNumPaths()):
            if self.body[i].getName().find('master_face') >= 0:
                faceParts.append(self.body[i])

        for part in faceParts:
            self.body.removePath(part)

        if self.newAvatars:
            self.stripTexture(self.body)
        self.bodyPiecesToGroup = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 2, 9: 1, 10: 2, 11: 1, 12: 2, 13: 1, 14: 2, 15: 1, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0}
        self.groupsToBodyPieces = [
         [
          0, 1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20, 21], [9, 11, 13, 15], [8, 10, 12, 14]]
        layerBList = [
         '**/body_neck*', '**/body_torso_base', '**/body_torso_back', '**/body_torso_front', '**/body_collar_sharp', '**/body_collar_round', '**/body_belt', '**/body_waist', '**/body_armpit_right', '**/body_armpit_left', '**/body_shoulder_right', '**/body_shoulder_left', '**/body_forearm_right', '**/body_forearm_left', '**/body_hand_right', '**/body_hand_left', '**/body_knee_right', '**/body_knee_left', '**/body_shin_right', '**/body_shin_left', '**/body_foot_right', '**/body_foot_left']
        self.layerBodyLODs = []
        for part in layerBList:
            bodyParts = {}
            for lod in ['2000', '1000', '500']:
                bodyParts[lod] = self.pirate.getLOD(lod).find(part)

            self.layerBodyLODs.append(bodyParts)

        chest = NodePathCollection()
        leftArm = NodePathCollection()
        rightArm = NodePathCollection()
        self.currentTattooZones = [
         chest, leftArm, rightArm, self.faces[0]]
        for i in self.bodyPiecesToGroup.items():
            self.currentTattooZones[i[1]].addPath(self.layerBodyLODs[i[0]]['2000'])
            self.currentTattooZones[i[1]].addPath(self.layerBodyLODs[i[0]]['1000'])
            self.currentTattooZones[i[1]].addPath(self.layerBodyLODs[i[0]]['500'])

        self.bodys = []
        self.bodyIdx = 0
        self.bodys.append(geom.findAllMatches('**/body_neck*'))
        self.bodys.append(geom.findAllMatches('**/body_torso_base'))
        self.bodys.append(geom.findAllMatches('**/body_torso_back'))
        self.bodys.append(geom.findAllMatches('**/body_torso_front'))
        self.bodys.append(geom.findAllMatches('**/body_collar_sharp'))
        self.bodys.append(geom.findAllMatches('**/body_collar_round'))
        self.bodys.append(geom.findAllMatches('**/body_belt'))
        self.bodys.append(geom.findAllMatches('**/body_waist'))
        self.bodys.append(geom.findAllMatches('**/body_armpit_right'))
        self.bodys.append(geom.findAllMatches('**/body_armpit_left'))
        self.bodys.append(geom.findAllMatches('**/body_shoulder_right'))
        self.bodys.append(geom.findAllMatches('**/body_shoulder_left'))
        self.bodys.append(geom.findAllMatches('**/body_forearm_right'))
        self.bodys.append(geom.findAllMatches('**/body_forearm_left'))
        self.bodys.append(geom.findAllMatches('**/body_hand_right'))
        self.bodys.append(geom.findAllMatches('**/body_hand_left'))
        self.bodys.append(geom.findAllMatches('**/body_knee_right'))
        self.bodys.append(geom.findAllMatches('**/body_knee_left'))
        self.bodys.append(geom.findAllMatches('**/body_shin_right'))
        self.bodys.append(geom.findAllMatches('**/body_shin_left'))
        self.bodys.append(geom.findAllMatches('**/body_foot_right'))
        self.bodys.append(geom.findAllMatches('**/body_foot_left'))
        for part in self.bodys:
            part.stash()

        self.currentBody = NodePathCollection()
        self.bodyTextures = loader.loadModelCopy('models/misc/male_body.bam')
        self.numBodys = len(body_textures[0])
        self.bodyTextureIdx = self.pirate.style.getBodySkin()
        self.lowLODSkinColor = VBase4(0.81, 0.69, 0.62, 1.0)
        self.faceTextures = loader.loadModelCopy('models/misc/male_face.bam')
        self.numFaces = len(face_textures)
        self.faceTextureIdx = self.pirate.style.getHeadTexture()
        self.numEyeColors = len(eye_iris_textures)
        self.eyesColorIdx = self.pirate.style.getEyesColor()
        self.skinColorIdx = self.pirate.style.getBodyColor()
        self.hairColorIdx = self.pirate.style.getHairColor()
        for shape in body_textures:
            for texName in shape:
                tex = self.bodyTextures.findTexture(texName)
                if tex:
                    self.texDict[texName] = tex
                else:
                    self.texDict[texName] = None

        return

    def setupClothing(self, lodName='2000'):
        geom = self.pirate.getGeomNode()
        self.clothing = self.pirate.findAllMatches('**/clothing_*')
        self.clothingsAcc = []
        self.clothingAccIdx = 0
        self.clothingsLayer1 = []
        self.clothingsLayer2 = []
        self.clothingsLayer3 = []
        self.clothingsShirt = []
        self.clothingShirtIdx = 0
        self.clothingShirtTexture = 0
        self.clothingsVest = []
        self.clothingVestIdx = 0
        self.clothingVestTexture = 0
        self.clothingsCoat = []
        self.clothingCoatIdx = 0
        self.clothingCoatTexture = 0
        self.clothingsPant = []
        self.clothingPantIdx = 0
        self.clothingPantTexture = 0
        self.clothingsBelt = []
        self.clothingBeltIdx = 0
        self.clothingBeltTexture = 0
        self.clothingsSock = []
        self.clothingSockIdx = 0
        self.clothingSockTexture = 0
        self.clothingsShoe = []
        self.clothingShoeIdx = 0
        self.clothingShoeTexture = 0
        self.clothingsHat = []
        self.clothingHatIdx = 0
        self.clothingHatTexture = 0
        self.partLayer = {}
        layer1List = [
         '**/clothing_layer1_shirt_common_open_base', '**/clothing_layer1_shirt_common_bottom_open_base', '**/clothing_layer1_shirt_common_closed_base', '**/clothing_layer1_shirt_common_closed_front', '**/clothing_layer1_shirt_common_bottom_out_closed_base', '**/clothing_layer1_shirt_common_bottom_out_closed_front', '**/clothing_layer1_shirt_common_bottom_in_closed_base', '**/clothing_layer1_shirt_common_bottom_in_closed_front', '**/clothing_layer1_shirt_common_collar_square', '**/clothing_layer1_shirt_common_collar_v_high1', '**/clothing_layer1_shirt_common_collar_v_high2', '**/clothing_layer1_shirt_common_collar_v_low', '**/clothing_layer1_shirt_common_veryshort_sleeve', '**/clothing_layer1_shirt_common_short_sleeve', '**/clothing_layer1_shirt_common_long_straight_sleeve', '**/clothing_layer1_shirt_common_long_puffy_sleeve', '**/clothing_layer1_pant_tucked_*', '**/clothing_layer1_pant_untucked_*', '**/clothing_layer1_pant_shorts_*', '**/clothing_layer1_pant_short_*', '**/clothing_layer1_pant_navy*', '**/clothing_layer1_pant_india_navy*', '**/clothing_layer1_shoe_none_*', '**/clothing_layer1_shoe_boot_tall_*', '**/clothing_layer1_shoe_boot_short_*', '**/clothing_layer1_shoe_boot_cuff_*', '**/clothing_layer1_shoe_navy*', '**/clothing_layer1_shoe_india_navy*', '**/clothing_layer1_shirt_apron', '**/clothing_layer1_pant_apron', '**/clothing_layer1_pant_apron_skirt', '**/clothing_layer1_hat_captain;+s', '**/clothing_layer1_hat_tricorn;+s', '**/clothing_layer1_hat_navy;+s', '**/clothing_layer1_hat_india_navy;+s', '**/clothing_layer1_hat_admiral;+s', '**/clothing_layer1_hat_bandanna_full;+s', '**/clothing_layer1_hat_bandanna_reg*;+s', '**/clothing_layer1_hat_band_beanie;+s', '**/clothing_layer1_hat_barbossa;+s', '**/clothing_layer1_hat_barbossa_feather;+s']
        self.layer1LODs = []
        for item in layer1List:
            itemInfo = {}
            for lod in ['500', '1000', '2000']:
                itemInfo[lod] = self.pirate.getLOD(lod).findAllMatches(item)

            self.layer1LODs.append(itemInfo)

        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_open_base'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_bottom_open_base'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_closed_base'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_closed_front'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_bottom_out_closed_base'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_bottom_out_closed_front'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_bottom_in_closed_base'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_bottom_in_closed_front'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_collar_square'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_collar_v_high1'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_collar_v_high2'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_collar_v_low'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_veryshort_sleeve'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_short_sleeve'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_long_straight_sleeve'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_common_long_puffy_sleeve'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_tucked_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_untucked_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_shorts_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_short_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_navy*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_india_navy*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shoe_none_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shoe_boot_tall_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shoe_boot_short_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shoe_boot_cuff_*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shoe_navy*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shoe_india_navy*'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_shirt_apron'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_apron'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_pant_apron_skirt'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_captain;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_tricorn;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_navy;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_india_navy;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_admiral;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_bandanna_full;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_bandanna_reg;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_band_beanie;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_barbossa;+s'))
        self.clothingsLayer1.append(geom.findAllMatches('**/clothing_layer1_hat_barbossa_feather;+s'))
        self.partLayer['SHIRT'] = self.clothingsLayer1
        self.partLayer['PANT'] = self.clothingsLayer1
        self.partLayer['SHOE'] = self.clothingsLayer1
        self.partLayer['HAT'] = self.clothingsLayer1
        self.clothesTextures = loader.loadModelCopy('models/misc/male_clothes.bam')
        self.clothingsShirt.append([[]])
        self.clothingsShirt.append([[2, 3, 4, 5, 9], -1, -2, -3, -4, -5])
        self.clothingsShirt.append([[2, 3, 4, 5, 9], -1, -2, -3, -4, -5])
        self.clothingsShirt.append([[2, 3, 4, 5, 10, 13], -1, -2, -3, -4, -5, -8, -9, -10, -11])
        self.clothingsShirt.append([[2, 3, 4, 5, 9, 13], -1, -2, -3, -4, -5, -8, -9, -10, -11])
        self.clothingsShirt.append([[0, 1, 13], -1, -2, -8, -9, -10, -11])
        self.clothingsShirt.append([[2, 3, 4, 5, 11, 15], -1, -2, -3, -8, -9, -10, -11, -12, -13])
        self.clothingsShirt.append([[2, 3, 4, 5, 9, 14], -1, -2, -3, -4, -5, -8, -9, -10, -11, -12, -13])
        self.clothingsShirt.append([[0, 1, 14], -1, -2, -8, -9, -10, -11, -12, -13])
        self.clothingsShirt.append([[28], -1, -2, -3, -4, -8, -9, -10, -11])
        self.clothingsShirt.append([[2, 3, 4, 5, 9, 14], -1, -2, -3, -4, -5, -8, -9, -10, -11, -12, -13])
        self.clothingsHat.append([[]])
        self.clothingsHat.append([[31]])
        self.clothingsHat.append([[32]])
        self.clothingsHat.append([[33]])
        self.clothingsHat.append([[34]])
        self.clothingsHat.append([[35]])
        self.clothingsHat.append([[36]])
        self.clothingsHat.append([[37]])
        self.clothingsHat.append([[38]])
        self.clothingsHat.append([[39, 40]])
        self.clothingsPant.append([[16], -6, -7, -16, -17])
        self.clothingsPant.append([[17], -6, -7, -16, -17])
        self.clothingsPant.append([[18], -6, -7])
        self.clothingsPant.append([[19], -6, -7])
        self.clothingsPant.append([[20], -6, -7, -16, -17, -18, -19])
        self.clothingsPant.append([[21], -6, -7, -16, -17, -18, -19])
        self.clothingsPant.append([[30, 29], -6, -7, -16, -17, -18, -19])
        self.clothingsShoe.append([[22]])
        self.clothingsShoe.append([[23], -18, -19, -20, -21])
        self.clothingsShoe.append([[24], -20, -21])
        self.clothingsShoe.append([[26], -20, -21])
        self.clothingsShoe.append([[27], -20, -21])
        self.clothingsShoe.append([[25], -20, -21])
        layer2List = [
         '**/clothing_layer2_vest_none*', '**/clothing_layer2_vest_open*', '**/clothing_layer2_vest_closed*', '**/clothing_layer2_vest_long_closed*', '**/clothing_layer2_belt_none*', '**/clothing_layer2_belt_sash_reg_base', '**/clothing_layer2_belt_sash_reg_front', '**/clothing_layer2_belt_oval', '**/clothing_layer2_belt_buckle_oval', '**/clothing_layer2_belt_square', '**/clothing_layer2_belt_buckle_square']
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_vest_none*'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_vest_open*'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_vest_closed*'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_vest_long_closed*'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_none*'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_sash_reg_base'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_sash_reg_front'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_oval'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_buckle_oval'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_square'))
        self.clothingsLayer2.append(geom.findAllMatches('**/clothing_layer2_belt_buckle_square'))
        self.partLayer['VEST'] = self.clothingsLayer2
        self.partLayer['BELT'] = self.clothingsLayer2
        self.clothingsVest.append([[0]])
        self.clothingsVest.append([[1], -1, -2])
        self.clothingsVest.append([[2], -1, -2, -3])
        self.clothingsVest.append([[3], -1, -2, -3])
        self.clothingsBelt.append([[4]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[9, 10]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[7, 8]])
        self.clothingsBelt.append([[9, 10]])
        self.clothingsBelt.append([[9, 10]])
        self.clothingsBelt.append([[5, 6]])
        self.clothingsBelt.append([[9, 10]])
        self.clothingsBelt.append([[9, 10]])
        self.clothingsLayer3.append(geom.findAllMatches('**/clothing_layer3_coat_none*'))
        self.clothingsLayer3.append(geom.findAllMatches('**/clothing_layer3_coat_long*'))
        self.clothingsLayer3.append(geom.findAllMatches('**/clothing_layer3_coat_short*'))
        self.clothingsLayer3.append(geom.findAllMatches('**/clothing_layer3_coat_navy*'))
        self.clothingsLayer3.append(geom.findAllMatches('**/clothing_layer3_coat_india_navy*'))
        layer3List = [
         '**/clothing_layer3_coat_none*', '**/clothing_layer3_coat_long*', '**/clothing_layer3_coat_short*', '**/clothing_layer3_coat_navy*', '**/clothing_layer3_coat_india_navy*']
        if base.config.GetBool('want-gen-pics-buttons'):
            self.clothesByType = {'SHIRT': self.clothingsLayer1[:16] + self.clothingsLayer1[28:29], 'VEST': self.clothingsLayer2[:4], 'PANT': self.clothingsLayer1[16:22] + self.clothingsLayer1[29:30], 'COAT': self.clothingsLayer3, 'BELT': self.clothingsLayer2[4:], 'SHOE': self.clothingsLayer1[22:28], 'HAT': self.clothingsLayer1[31:]}
        self.partLayer['COAT'] = self.clothingsLayer3
        self.clothingsCoat.append([[0]])
        self.clothingsCoat.append([[1], -1, -2, -8, -9, -10, -11, -12, -13])
        self.clothingsCoat.append([[2], -1, -2, -8, -9, -10, -11, -12, -13])
        self.clothingsCoat.append([[3], -1, -2, -3, -4, -5, -8, -9, -10, -11, -12, -13])
        self.clothingsCoat.append([[4], -1, -2, -3, -4, -5, -8, -9, -10, -11, -12, -13])
        for type in clothes_textures.values():
            for model in type:
                for texInfo in model:
                    textures = texInfo[0].split('+')
                    for texName in textures:
                        tex = self.clothesTextures.findTexture(texName)
                        if tex:
                            self.texDict[texName] = tex
                        else:
                            self.texDict[texName] = None

        self.texDict['PM_none'] = None
        if self.newAvatars:
            self.generateShirtSets()
            self.generatePantSets()
            self.generateShoeSets()
            self.layer2LODs = []
            for item in layer2List:
                itemInfo = {}
                for lod in ['500', '1000', '2000']:
                    itemInfo[lod] = self.pirate.getLOD(lod).findAllMatches(item)

                self.layer2LODs.append(itemInfo)

            self.generateVestSets()
            self.generateBeltSets()
            self.layer3LODs = []
            for item in layer3List:
                itemInfo = {}
                for lod in ['500', '1000', '2000']:
                    itemInfo[lod] = self.pirate.getLOD(lod).findAllMatches(item)

                self.layer3LODs.append(itemInfo)

            self.generateCoatSets()
        self.generateHatSets()
        self.clothing.stash()
        return

    def setupSelectionChoices(self, type):
        data = ClothingGlobals.SELECTION_CHOICES.get(type, None)
        if not data:
            return
        choices = data['MALE']
        self.choices = {}
        self.choices['FACE'] = choices.get('FACE', [])
        self.choices['HAIR'] = choices.get('HAIR', [])
        self.choices['HAT'] = choices.get('HAT', [])
        self.choices['SHIRT'] = choices.get('SHIRT', [])
        self.choices['VEST'] = choices.get('VEST', [])
        self.choices['COAT'] = choices.get('COAT', [])
        self.choices['PANT'] = choices.get('PANT', [])
        self.choices['BELT'] = choices.get('BELT', [])
        self.choices['SHOE'] = choices.get('SHOE', [])
        return

    def setClothesTexture(self, tex, listParts, layer, color=None):
        for i in range(0, len(listParts)):
            parts = layer[listParts[i]]
            if not parts.isEmpty():
                numPaths = parts.getNumPaths()
                for j in range(0, numPaths):
                    if tex:
                        parts[j].setTexture(tex, 1)
                    if color is None or self.pirate.optimizeLOD == 0:
                        continue
                    medIdx = numPaths / 3
                    lowIdx = numPaths / 3 * 2
                    if j >= medIdx and j < lowIdx:
                        if 'layer2_belt_' in parts[j].getName():
                            parts[j].setColorScale(color)
                        elif 'layer1_shoe_' in parts[j].getName():
                            parts[j].setColorScale(color)
                    elif j >= lowIdx:
                        parts[j].setColorScale(color)

        return

    def setPartTexture(self, part, geomIdx, texIdx, pieces):
        numParts = len(clothes_textures[part])
        if numParts == 0:
            return
        if geomIdx >= numParts:
            self.notify.warning('part (%s) geom index (%s), capping it (%s)' % (part, geomIdx, numParts - 1))
            geomIdx = numParts - 1
        numTextures = len(clothes_textures[part][geomIdx])
        if numTextures == 0:
            return
        if texIdx >= numTextures:
            self.notify.warning('part (%s) texture index (%s) out of range (%s), capping it (%s)' % (part, geomIdx, texIdx, numTextures - 1))
            texIdx = numTextures - 1
        texture = clothes_textures[part][geomIdx][texIdx]
        texName = texture[0].split('+')
        lowLODColor = texture[1]
        if len(texName) > 1:
            tex = self.texDict[texName[0]]
            self.setClothesTexture(tex, [pieces[0]], self.partLayer[part], lowLODColor)
            tex = self.texDict[texName[1]]
            self.setClothesTexture(tex, [pieces[1]], self.partLayer[part], lowLODColor)
        else:
            tex = self.clothesTextures.findTexture(texName[0])
            self.setClothesTexture(tex, pieces, self.partLayer[part], lowLODColor)

    def getTextureName(self, partIdx, idx, texIdx):
        try:
            return clothes_textures[partIdx][idx][texIdx]
        except:
            return

        return

    def handleJewelryHiding(self):
        jewelryDNA = {'LEar': self.pirate.style.getJewelryZone1(), 'REar': self.pirate.style.getJewelryZone2(), 'LBrow': self.pirate.style.getJewelryZone3(), 'RBrow': self.pirate.style.getJewelryZone4(), 'Nose': self.pirate.style.getJewelryZone5(), 'Mouth': self.pirate.style.getJewelryZone6(), 'LHand': self.pirate.style.getJewelryZone7(), 'RHand': self.pirate.style.getJewelryZone8()}
        for key in self.currentJewelry.keys():
            primaryColor = HumanDNA.jewelryColors[jewelryDNA[key][1]]
            secondaryColor = HumanDNA.jewelryColors[jewelryDNA[key][2]]
            oldIdx = self.currentJewelry[key][0]
            newIdx = jewelryDNA[key][0]
            for np in self.jewelrySets[key][oldIdx]:
                np.stash()

            for npIdx in range(len(self.jewelrySets[key][newIdx])):
                np = self.jewelrySets[key][newIdx][npIdx]
                np.unstash()
                if npIdx == 0 and primaryColor:
                    np.setColor(primaryColor)
                elif secondaryColor:
                    np.setColor(secondaryColor)

            self.currentJewelry[key] = jewelryDNA[key]

    def handleClothesHiding(self):
        if not self.newAvatars:
            self.handleClothesHidingOld()
            self.setupTattoos()
            return
        if self.pirate.zombie:
            dna = self.dnaZomb
        else:
            dna = self.pirate.style
        shirtIdx = dna.getClothesShirt()
        vestIdx = dna.getClothesVest()
        coatIdx = dna.getClothesCoat()
        pantIdx = dna.getClothesPant()
        beltIdx = dna.getClothesBelt()
        shoeIdx = dna.getClothesShoe()
        hatIdx = dna.getClothesHat()
        hairIdx = [
         dna.getHairHair(), dna.getHairColor()]
        if beltIdx[0] != 0:
            style1 = 'belt'
        else:
            style1 = 'nobelt'
        if vestIdx[0] != 3:
            stylePant = style1
        else:
            stylePant = 'belt'
        layerPant = self.clothingsPant[pantIdx[0]]
        layerShoe = self.clothingsShoe[shoeIdx[0]]
        layerShirt = self.clothingsShirt[shirtIdx[0]]
        layerShirtModified = [[]] + layerShirt[1:]
        for elem in layerShirt[0]:
            if beltIdx[0] != 0:
                if elem == 4:
                    elem = 6
                else:
                    if elem == 5:
                        elem = 7
                layerShirtModified[0].append(elem)

        layerVest = self.clothingsVest[vestIdx[0]]
        layerBelt = self.clothingsBelt[beltIdx[0]]
        layerCoat = self.clothingsCoat[coatIdx[0]]
        currentVest = self.vestSets[vestIdx[0]][style1]['full']
        currentShirt = self.shirtSets[shirtIdx[0]][style1]['full']
        currentCoat = self.coatSets[coatIdx[0]]
        currentBelt = self.beltSets[beltIdx[0]]['full']
        currentPant = self.pantSets[pantIdx[0]][stylePant]
        currentShoe = self.shoeSets[shoeIdx[0]]
        if coatIdx[0] > 0:
            if coatIdx[0] == 2 and vestIdx[0] == 3:
                currentVest = self.vestSets[vestIdx[0]][style1]['coatSpecial']
            else:
                if vestIdx[0] > 0:
                    currentVest = self.vestSets[vestIdx[0]][style1]['coat']
            if vestIdx[0] > 1:
                currentShirt = self.shirtSets[shirtIdx[0]][style1]['coat+closedVest']
            else:
                currentShirt = self.shirtSets[shirtIdx[0]][style1]['coat']
            currentBelt = self.beltSets[beltIdx[0]]['coat']
        else:
            if vestIdx[0] > 1:
                currentShirt = self.shirtSets[shirtIdx[0]][style1]['closedVest']
            else:
                if vestIdx[0] > 0:
                    currentShirt = self.shirtSets[shirtIdx[0]][style1]['openVest']
        self.currentClothingModels['SHIRT'].stash()
        currentShirt.unstash()
        texInfo = clothes_textures['SHIRT'][shirtIdx[0]][shirtIdx[1]]
        if self.texDict[texInfo[0]]:
            currentShirt.setTexture(self.texDict[texInfo[0]])
            shirtColor = dna.lookupClothesTopColor()[0]
            currentShirt.setColorScale(shirtColor)
            if self.pirate.optimizeLOD:
                for i in xrange(currentShirt.getNumPaths() * 2 / 3, currentShirt.getNumPaths()):
                    currentShirt[i].setColorScale(VBase4(texInfo[1][0] * shirtColor[0], texInfo[1][1] * shirtColor[1], texInfo[1][2] * shirtColor[2], 1))

        self.currentClothingModels['SHIRT'] = currentShirt
        self.currentClothingModels['VEST'].stash()
        texInfo = clothes_textures['VEST'][vestIdx[0]][vestIdx[1]]
        currentVest.unstash()
        self.currentClothingModels['VEST'] = currentVest
        if self.texDict[texInfo[0]]:
            vestColor = dna.lookupClothesTopColor()[1]
            currentVest.setTexture(self.texDict[texInfo[0]])
            currentVest.setColorScale(vestColor)
            if self.pirate.optimizeLOD:
                for i in xrange(currentVest.getNumPaths() * 2 / 3, currentVest.getNumPaths()):
                    currentVest[i].setColorScale(VBase4(texInfo[1][0] * vestColor[0], texInfo[1][1] * vestColor[1], texInfo[1][2] * vestColor[2], 1))

        self.currentClothingModels['COAT'].stash()
        texInfo = clothes_textures['COAT'][coatIdx[0]][coatIdx[1]]
        currentCoat.unstash()
        self.currentClothingModels['COAT'] = currentCoat
        if self.texDict[texInfo[0]]:
            coatColor = dna.lookupClothesTopColor()[2]
            if coatIdx[0] not in ClothingGlobals.navy_coat_geoms:
                currentCoat.setTexture(self.texDict[texInfo[0]])
            currentCoat.setColorScale(coatColor)
            if self.pirate.optimizeLOD:
                for i in xrange(currentCoat.getNumPaths() * 2 / 3, currentCoat.getNumPaths()):
                    currentCoat[i].setColorScale(VBase4(texInfo[1][0] * coatColor[0], texInfo[1][1] * coatColor[1], texInfo[1][2] * coatColor[2], 1))

        self.handleHeadHiding()
        self.currentClothingModels['BELT'][0].stash()
        self.currentClothingModels['BELT'][1].stash()
        texInfo = clothes_textures['BELT'][beltIdx[0]][beltIdx[1]]
        currentBelt[0].unstash()
        currentBelt[1].unstash()
        texNames = texInfo[0].split('+')
        self.currentClothingModels['BELT'] = currentBelt
        if len(texNames) > 1:
            tex1 = self.texDict[texNames[0]]
            tex2 = self.texDict[texNames[1]]
            if tex1:
                currentBelt[0].setTexture(tex1)
            if tex2:
                currentBelt[1].setTexture(tex2)
        else:
            tex1 = self.texDict[texNames[0]]
            if tex1:
                currentBelt[0].setTexture(tex1)
                currentBelt[1].setTexture(tex1)
        beltColor = dna.lookupClothesBotColor()[1]
        for i in [0, 1]:
            currentBelt[i].setColorScale(beltColor)
            if self.pirate.optimizeLOD:
                for j in xrange(currentBelt[i].getNumPaths() * 2 / 3, currentBelt[i].getNumPaths()):
                    currentBelt[i][j].setColorScale(VBase4(texInfo[1][0] * beltColor[0], texInfo[1][1] * beltColor[1], texInfo[1][2] * beltColor[2], 1))

        self.currentClothingModels['PANT'].stash()
        texInfo = clothes_textures['PANT'][pantIdx[0]][pantIdx[1]]
        currentPant.unstash()
        self.currentClothingModels['PANT'] = currentPant
        if self.texDict[texInfo[0]]:
            pantColor = dna.lookupClothesBotColor()[0]
            currentPant.setTexture(self.texDict[texInfo[0]])
            currentPant.setColorScale(pantColor)
            if self.pirate.optimizeLOD:
                for i in xrange(currentPant.getNumPaths() * 2 / 3, currentPant.getNumPaths()):
                    currentPant[i].setColorScale(VBase4(texInfo[1][0] * pantColor[0], texInfo[1][1] * pantColor[1], texInfo[1][2] * pantColor[2], 1))

        self.currentClothingModels['SHOE'].stash()
        currentShoe.unstash()
        texInfo = clothes_textures['SHOE'][shoeIdx[0]][shoeIdx[1]]
        if self.texDict[texInfo[0]]:
            shoeColor = dna.lookupClothesBotColor()[2]
            currentShoe.setTexture(self.texDict[texInfo[0]])
            if self.pirate.optimizeLOD:
                for i in xrange(currentShoe.getNumPaths() * 2 / 3, currentShoe.getNumPaths()):
                    currentShoe[i].setColorScale(VBase4(texInfo[1][0] * shoeColor[0], texInfo[1][1] * shoeColor[1], texInfo[1][2] * shoeColor[2], 1))

        self.currentClothingModels['SHOE'] = currentShoe
        bodySet = [
         set(), set(), set()]
        for partSet in [layerShirtModified, layerVest, layerCoat, layerPant, layerShoe, layerBelt]:
            for i in partSet[1:]:
                bodySet[self.bodyPiecesToGroup[-i]].add(-i)

        bodyList = [ list(x) for x in bodySet ]
        for pieces in bodyList:
            pieces.sort()

        bodyTuple = [ tuple(x) for x in bodyList ]
        for i in xrange(3):
            if bodyTuple[i] not in self.bodySets[i]:
                flattenedSet = NodePathCollection()
                for lod in ['2000', '1000', '500']:
                    flattenMe = NodePath('flattenMe')
                    for j in self.groupsToBodyPieces[i]:
                        if j not in bodySet[i]:
                            self.layerBodyLODs[j][lod].copyTo(flattenMe)

                    flattenMe.flattenStrong()
                    lodParts = flattenMe.findAllMatches('**/+GeomNode')
                    self.stripTexture(lodParts)
                    lodParts.reparentTo(self.pirate.getLOD(lod).getChild(0))
                    flattenedSet.addPathsFrom(lodParts)

                self.bodySets[i][bodyTuple[i]] = flattenedSet

        if self.pirate.zombie:
            bodyTexIdx = ZOMB_BODY_TEXTURE
        else:
            bodyTexIdx = 0
        tex = self.texDict[body_textures[self.pirate.style.getBodyShape()][bodyTexIdx]]
        currentBody = NodePathCollection()
        currentChest = self.bodySets[0][bodyTuple[0]]
        currentLeftArm = self.bodySets[1][bodyTuple[1]]
        currentRightArm = self.bodySets[2][bodyTuple[2]]
        currentBody.addPathsFrom(currentChest)
        currentBody.addPathsFrom(currentLeftArm)
        currentBody.addPathsFrom(currentRightArm)
        if tex:
            currentBody.setTexture(tex)
        if self.pirate.zombie:
            skinColor = VBase4(1, 1, 1, 1)
            lowColor = VBase4(1, 1, 1, 1)
        else:
            skinColor = self.pirate.style.getSkinColor()
            lowColor = self.lowLODSkinColor
        self.faces[0].setColorScale(skinColor)
        currentBody.setColorScale(skinColor)
        if self.pirate.optimizeLOD:
            color = VBase4(lowColor[0] * skinColor[0], lowColor[1] * skinColor[1], lowColor[2] * skinColor[2], 1.0)
            currentChest[2].setColorScale(color)
            currentLeftArm[2].setColorScale(color)
            currentRightArm[2].setColorScale(color)
            self.faces[0][2].setColorScale(color)
        self.currentBody.stash()
        currentBody.unstash()
        self.currentBody = currentBody
        self.currentTattooZones = [currentChest, currentLeftArm, currentRightArm, self.faces[0]]
        self.setupTattoos()

    def handleClothesHidingOld--- This code section failed: ---

1935       0  LOAD_FAST             0  'self'
           3  LOAD_ATTR             1  'clothing'
           6  LOAD_ATTR             2  'stash'
           9  CALL_FUNCTION_0       0  None
          12  POP_TOP          

1937      13  LOAD_FAST             0  'self'
          16  LOAD_ATTR             3  'body'
          19  LOAD_ATTR             4  'unstash'
          22  CALL_FUNCTION_0       0  None
          25  POP_TOP          

1950      26  LOAD_FAST             0  'self'
          29  LOAD_ATTR             5  'pirate'
          32  LOAD_ATTR             6  'zombie'
          35  JUMP_IF_FALSE        13  'to 51'
          38  POP_TOP          

1951      39  LOAD_FAST             0  'self'
          42  LOAD_ATTR             7  'dnaZomb'
          45  STORE_FAST            9  'dna'
          48  JUMP_FORWARD         13  'to 64'
        51_0  COME_FROM            35  '35'
          51  POP_TOP          

1953      52  LOAD_FAST             0  'self'
          55  LOAD_ATTR             5  'pirate'
          58  LOAD_ATTR             9  'style'
          61  STORE_FAST            9  'dna'
        64_0  COME_FROM            48  '48'

1955      64  LOAD_FAST             9  'dna'
          67  LOAD_ATTR            10  'getClothesShirt'
          70  CALL_FUNCTION_0       0  None
          73  STORE_FAST           10  'shirtIdx'

1956      76  LOAD_FAST             9  'dna'
          79  LOAD_ATTR            12  'getClothesVest'
          82  CALL_FUNCTION_0       0  None
          85  STORE_FAST            7  'vestIdx'

1957      88  LOAD_FAST             9  'dna'
          91  LOAD_ATTR            14  'getClothesCoat'
          94  CALL_FUNCTION_0       0  None
          97  STORE_FAST           17  'coatIdx'

1958     100  LOAD_FAST             9  'dna'
         103  LOAD_ATTR            16  'getClothesPant'
         106  CALL_FUNCTION_0       0  None
         109  STORE_FAST           16  'pantIdx'

1959     112  LOAD_FAST             9  'dna'
         115  LOAD_ATTR            18  'getClothesBelt'
         118  CALL_FUNCTION_0       0  None
         121  STORE_FAST           13  'beltIdx'

1960     124  LOAD_FAST             9  'dna'
         127  LOAD_ATTR            20  'getClothesShoe'
         130  CALL_FUNCTION_0       0  None
         133  STORE_FAST            8  'shoeIdx'

1961     136  LOAD_FAST             9  'dna'
         139  LOAD_ATTR            22  'getClothesHat'
         142  CALL_FUNCTION_0       0  None
         145  STORE_FAST            5  'hatIdx'

1964     148  LOAD_FAST             0  'self'
         151  LOAD_ATTR            24  'clothingsPant'
         154  LOAD_FAST            16  'pantIdx'
         157  LOAD_CONST            1  0
         160  BINARY_SUBSCR    
         161  BINARY_SUBSCR    
         162  STORE_FAST           15  'layerPant'

1965     165  LOAD_GLOBAL          26  'NodePathCollection'
         168  CALL_FUNCTION_0       0  None
         171  STORE_FAST           12  'parts'

1968     174  LOAD_FAST             0  'self'
         177  LOAD_ATTR            28  'clothesTextures'
         180  LOAD_CONST            0  None
         183  COMPARE_OP            3  '!='
         186  JUMP_IF_FALSE       100  'to 289'
       189_0  THEN                     290
         189  POP_TOP          

1969     190  LOAD_FAST            16  'pantIdx'
         193  LOAD_CONST            1  0
         196  BINARY_SUBSCR    
         197  LOAD_CONST            2  6
         200  COMPARE_OP            2  '=='
         203  JUMP_IF_FALSE        45  'to 251'
       206_0  THEN                     286
         206  POP_TOP          

1970     207  LOAD_FAST             0  'self'
         210  LOAD_ATTR            30  'setPartTexture'
         213  LOAD_CONST            3  'PANT'
         216  LOAD_FAST            16  'pantIdx'
         219  LOAD_CONST            1  0
         222  BINARY_SUBSCR    
         223  LOAD_FAST            16  'pantIdx'
         226  LOAD_CONST            4  1
         229  BINARY_SUBSCR    
         230  LOAD_FAST            15  'layerPant'
         233  LOAD_CONST            1  0
         236  BINARY_SUBSCR    
         237  LOAD_CONST            4  1
         240  BINARY_SUBSCR    
         241  BUILD_LIST_1          1  None
         244  CALL_FUNCTION_4       4  None
         247  POP_TOP          
         248  JUMP_ABSOLUTE       290  'to 290'
       251_0  COME_FROM           203  '203'
         251  POP_TOP          

1972     252  LOAD_FAST             0  'self'
         255  LOAD_ATTR            30  'setPartTexture'
         258  LOAD_CONST            3  'PANT'
         261  LOAD_FAST            16  'pantIdx'
         264  LOAD_CONST            1  0
         267  BINARY_SUBSCR    
         268  LOAD_FAST            16  'pantIdx'
         271  LOAD_CONST            4  1
         274  BINARY_SUBSCR    
         275  LOAD_FAST            15  'layerPant'
         278  LOAD_CONST            1  0
         281  BINARY_SUBSCR    
         282  CALL_FUNCTION_4       4  None
         285  POP_TOP          
         286  JUMP_FORWARD          1  'to 290'
       289_0  COME_FROM           186  '186'
         289  POP_TOP          
       290_0  COME_FROM           286  '286'

1973     290  SETUP_LOOP           81  'to 374'
         293  LOAD_GLOBAL          31  'range'
         296  LOAD_CONST            1  0
         299  LOAD_GLOBAL          32  'len'
         302  LOAD_FAST            15  'layerPant'
         305  LOAD_CONST            1  0
         308  BINARY_SUBSCR    
         309  CALL_FUNCTION_1       1  None
         312  CALL_FUNCTION_2       2  None
         315  GET_ITER         
         316  FOR_ITER             54  'to 373'
         319  STORE_FAST           20  'j'

1974     322  LOAD_FAST             0  'self'
         325  LOAD_ATTR            34  'clothingsLayer1'
         328  LOAD_FAST            15  'layerPant'
         331  LOAD_CONST            1  0
         334  BINARY_SUBSCR    
         335  LOAD_FAST            20  'j'
         338  BINARY_SUBSCR    
         339  BINARY_SUBSCR    
         340  STORE_FAST           12  'parts'

1975     343  LOAD_FAST            12  'parts'
         346  LOAD_ATTR            35  'getNumPaths'
         349  CALL_FUNCTION_0       0  None
         352  JUMP_IF_FALSE        14  'to 369'
         355  POP_TOP          

1976     356  LOAD_FAST            12  'parts'
         359  LOAD_ATTR             4  'unstash'
         362  CALL_FUNCTION_0       0  None
         365  POP_TOP          
         366  JUMP_BACK           316  'to 316'
       369_0  COME_FROM           352  '352'
         369  POP_TOP          
         370  JUMP_BACK           316  'to 316'
         373  POP_BLOCK        
       374_0  COME_FROM           290  '290'

1977     374  LOAD_FAST             0  'self'
         377  LOAD_ATTR            36  'handleLayer1Hiding'
         380  LOAD_FAST            15  'layerPant'
         383  CALL_FUNCTION_1       1  None
         386  POP_TOP          

1980     387  LOAD_FAST             0  'self'
         390  LOAD_ATTR            37  'clothingsShoe'
         393  LOAD_FAST             8  'shoeIdx'
         396  LOAD_CONST            1  0
         399  BINARY_SUBSCR    
         400  BINARY_SUBSCR    
         401  STORE_FAST           11  'layerShoe'

1981     404  LOAD_GLOBAL          26  'NodePathCollection'
         407  CALL_FUNCTION_0       0  None
         410  STORE_FAST           12  'parts'

1984     413  LOAD_FAST             0  'self'
         416  LOAD_ATTR            28  'clothesTextures'
         419  LOAD_CONST            0  None
         422  COMPARE_OP            3  '!='
         425  JUMP_IF_FALSE        38  'to 466'
       428_0  THEN                     467
         428  POP_TOP          

1985     429  LOAD_FAST             0  'self'
         432  LOAD_ATTR            30  'setPartTexture'
         435  LOAD_CONST            5  'SHOE'
         438  LOAD_FAST             8  'shoeIdx'
         441  LOAD_CONST            1  0
         444  BINARY_SUBSCR    
         445  LOAD_FAST             8  'shoeIdx'
         448  LOAD_CONST            4  1
         451  BINARY_SUBSCR    
         452  LOAD_FAST            11  'layerShoe'
         455  LOAD_CONST            1  0
         458  BINARY_SUBSCR    
         459  CALL_FUNCTION_4       4  None
         462  POP_TOP          
         463  JUMP_FORWARD          1  'to 467'
       466_0  COME_FROM           425  '425'
         466  POP_TOP          
       467_0  COME_FROM           463  '463'

1986     467  SETUP_LOOP           81  'to 551'
         470  LOAD_GLOBAL          31  'range'
         473  LOAD_CONST            1  0
         476  LOAD_GLOBAL          32  'len'
         479  LOAD_FAST            11  'layerShoe'
         482  LOAD_CONST            1  0
         485  BINARY_SUBSCR    
         486  CALL_FUNCTION_1       1  None
         489  CALL_FUNCTION_2       2  None
         492  GET_ITER         
         493  FOR_ITER             54  'to 550'
         496  STORE_FAST           20  'j'

1987     499  LOAD_FAST             0  'self'
         502  LOAD_ATTR            34  'clothingsLayer1'
         505  LOAD_FAST            11  'layerShoe'
         508  LOAD_CONST            1  0
         511  BINARY_SUBSCR    
         512  LOAD_FAST            20  'j'
         515  BINARY_SUBSCR    
         516  BINARY_SUBSCR    
         517  STORE_FAST           12  'parts'

1988     520  LOAD_FAST            12  'parts'
         523  LOAD_ATTR            35  'getNumPaths'
         526  CALL_FUNCTION_0       0  None
         529  JUMP_IF_FALSE        14  'to 546'
         532  POP_TOP          

1989     533  LOAD_FAST            12  'parts'
         536  LOAD_ATTR             4  'unstash'
         539  CALL_FUNCTION_0       0  None
         542  POP_TOP          
         543  JUMP_BACK           493  'to 493'
       546_0  COME_FROM           529  '529'
         546  POP_TOP          
         547  JUMP_BACK           493  'to 493'
         550  POP_BLOCK        
       551_0  COME_FROM           467  '467'

1990     551  LOAD_FAST             0  'self'
         554  LOAD_ATTR            36  'handleLayer1Hiding'
         557  LOAD_FAST            11  'layerShoe'
         560  CALL_FUNCTION_1       1  None
         563  POP_TOP          

1993     564  LOAD_GLOBAL          32  'len'
         567  LOAD_FAST             0  'self'
         570  LOAD_ATTR            39  'clothingsShirt'
         573  CALL_FUNCTION_1       1  None
         576  STORE_FAST            2  'numShirts'

1994     579  LOAD_FAST            10  'shirtIdx'
         582  LOAD_CONST            1  0
         585  BINARY_SUBSCR    
         586  STORE_FAST           19  'myShirtIdx'

1996     589  LOAD_FAST            19  'myShirtIdx'
         592  LOAD_FAST             2  'numShirts'
         595  COMPARE_OP            5  '>='
         598  JUMP_IF_FALSE        44  'to 645'
       601_0  THEN                     646
         601  POP_TOP          

1997     602  LOAD_FAST             0  'self'
         605  LOAD_ATTR            42  'notify'
         608  LOAD_ATTR            43  'warning'
         611  LOAD_CONST            6  'shirt (%s) out of range, capping it (%s)'
         614  LOAD_FAST            19  'myShirtIdx'
         617  LOAD_FAST             2  'numShirts'
         620  LOAD_CONST            4  1
         623  BINARY_SUBTRACT  
         624  BUILD_TUPLE_2         2  None
         627  BINARY_MODULO    
         628  CALL_FUNCTION_1       1  None
         631  POP_TOP          

1999     632  LOAD_FAST             2  'numShirts'
         635  LOAD_CONST            4  1
         638  BINARY_SUBTRACT  
         639  STORE_FAST           19  'myShirtIdx'
         642  JUMP_FORWARD          1  'to 646'
       645_0  COME_FROM           598  '598'
         645  POP_TOP          
       646_0  COME_FROM           642  '642'

2000     646  LOAD_FAST             0  'self'
         649  LOAD_ATTR            39  'clothingsShirt'
         652  LOAD_FAST            19  'myShirtIdx'
         655  BINARY_SUBSCR    
         656  STORE_FAST           14  'layerShirt'

2003     659  LOAD_GLOBAL          26  'NodePathCollection'
         662  CALL_FUNCTION_0       0  None
         665  STORE_FAST           12  'parts'

2006     668  BUILD_LIST_0          0  None
         671  STORE_FAST            3  'layerShirtModified'

2007     674  BUILD_LIST_0          0  None
         677  STORE_FAST            1  'layerShirt0Modified'

2008     680  SETUP_LOOP           98  'to 781'
         683  LOAD_FAST            14  'layerShirt'
         686  LOAD_CONST            1  0
         689  BINARY_SUBSCR    
         690  GET_ITER         
         691  FOR_ITER             86  'to 780'
         694  STORE_FAST           21  'elem'

2009     697  LOAD_FAST            13  'beltIdx'
         700  LOAD_CONST            1  0
         703  BINARY_SUBSCR    
         704  LOAD_CONST            1  0
         707  COMPARE_OP            3  '!='
         710  JUMP_IF_FALSE        50  'to 763'
       713_0  THEN                     764
         713  POP_TOP          

2010     714  LOAD_FAST            21  'elem'
         717  LOAD_CONST            7  4
         720  COMPARE_OP            2  '=='
         723  JUMP_IF_FALSE        10  'to 736'
       726_0  THEN                     760
         726  POP_TOP          

2011     727  LOAD_CONST            2  6
         730  STORE_FAST           21  'elem'
         733  JUMP_ABSOLUTE       764  'to 764'
       736_0  COME_FROM           723  '723'
         736  POP_TOP          

2012     737  LOAD_FAST            21  'elem'
         740  LOAD_CONST            8  5
         743  COMPARE_OP            2  '=='
         746  JUMP_IF_FALSE        10  'to 759'
       749_0  THEN                     760
         749  POP_TOP          

2013     750  LOAD_CONST            9  7
         753  STORE_FAST           21  'elem'
         756  JUMP_ABSOLUTE       764  'to 764'
       759_0  COME_FROM           746  '746'
         759  POP_TOP          
         760  JUMP_FORWARD          1  'to 764'
       763_0  COME_FROM           710  '710'
         763  POP_TOP          
       764_0  COME_FROM           760  '760'

2014     764  LOAD_FAST             1  'layerShirt0Modified'
         767  LOAD_ATTR            48  'append'
         770  LOAD_FAST            21  'elem'
         773  CALL_FUNCTION_1       1  None
         776  POP_TOP          
         777  JUMP_BACK           691  'to 691'
         780  POP_BLOCK        
       781_0  COME_FROM           680  '680'

2015     781  LOAD_FAST             3  'layerShirtModified'
         784  LOAD_ATTR            48  'append'
         787  LOAD_FAST             1  'layerShirt0Modified'
         790  CALL_FUNCTION_1       1  None
         793  POP_TOP          

2016     794  SETUP_LOOP           31  'to 828'
         797  LOAD_FAST            14  'layerShirt'
         800  LOAD_CONST            4  1
         803  SLICE+1          
         804  GET_ITER         
         805  FOR_ITER             19  'to 827'
         808  STORE_FAST           21  'elem'

2017     811  LOAD_FAST             3  'layerShirtModified'
         814  LOAD_ATTR            48  'append'
         817  LOAD_FAST            21  'elem'
         820  CALL_FUNCTION_1       1  None
         823  POP_TOP          
         824  JUMP_BACK           805  'to 805'
         827  POP_BLOCK        
       828_0  COME_FROM           794  '794'

2019     828  LOAD_FAST             0  'self'
         831  LOAD_ATTR            28  'clothesTextures'
         834  LOAD_CONST            0  None
         837  COMPARE_OP            3  '!='
         840  JUMP_IF_FALSE        38  'to 881'
       843_0  THEN                     882
         843  POP_TOP          

2020     844  LOAD_FAST             0  'self'
         847  LOAD_ATTR            30  'setPartTexture'
         850  LOAD_CONST           10  'SHIRT'
         853  LOAD_FAST            10  'shirtIdx'
         856  LOAD_CONST            1  0
         859  BINARY_SUBSCR    
         860  LOAD_FAST            10  'shirtIdx'
         863  LOAD_CONST            4  1
         866  BINARY_SUBSCR    
         867  LOAD_FAST             3  'layerShirtModified'
         870  LOAD_CONST            1  0
         873  BINARY_SUBSCR    
         874  CALL_FUNCTION_4       4  None
         877  POP_TOP          
         878  JUMP_FORWARD          1  'to 882'
       881_0  COME_FROM           840  '840'
         881  POP_TOP          
       882_0  COME_FROM           878  '878'

2021     882  SETUP_LOOP           81  'to 966'
         885  LOAD_GLOBAL          31  'range'
         888  LOAD_CONST            1  0
         891  LOAD_GLOBAL          32  'len'
         894  LOAD_FAST             3  'layerShirtModified'
         897  LOAD_CONST            1  0
         900  BINARY_SUBSCR    
         901  CALL_FUNCTION_1       1  None
         904  CALL_FUNCTION_2       2  None
         907  GET_ITER         
         908  FOR_ITER             54  'to 965'
         911  STORE_FAST           20  'j'

2023     914  LOAD_FAST             0  'self'
         917  LOAD_ATTR            34  'clothingsLayer1'
         920  LOAD_FAST             3  'layerShirtModified'
         923  LOAD_CONST            1  0
         926  BINARY_SUBSCR    
         927  LOAD_FAST            20  'j'
         930  BINARY_SUBSCR    
         931  BINARY_SUBSCR    
         932  STORE_FAST           12  'parts'

2024     935  LOAD_FAST            12  'parts'
         938  LOAD_ATTR            35  'getNumPaths'
         941  CALL_FUNCTION_0       0  None
         944  JUMP_IF_FALSE        14  'to 961'
         947  POP_TOP          

2025     948  LOAD_FAST            12  'parts'
         951  LOAD_ATTR             4  'unstash'
         954  CALL_FUNCTION_0       0  None
         957  POP_TOP          
         958  JUMP_BACK           908  'to 908'
       961_0  COME_FROM           944  '944'
         961  POP_TOP          
         962  JUMP_BACK           908  'to 908'
         965  POP_BLOCK        
       966_0  COME_FROM           882  '882'

2026     966  LOAD_FAST            12  'parts'
         969  LOAD_ATTR            35  'getNumPaths'
         972  CALL_FUNCTION_0       0  None
         975  JUMP_IF_FALSE        17  'to 995'
       978_0  THEN                     996
         978  POP_TOP          

2027     979  LOAD_FAST             0  'self'
         982  LOAD_ATTR            36  'handleLayer1Hiding'
         985  LOAD_FAST             3  'layerShirtModified'
         988  CALL_FUNCTION_1       1  None
         991  POP_TOP          
         992  JUMP_FORWARD          1  'to 996'
       995_0  COME_FROM           975  '975'
         995  POP_TOP          
       996_0  COME_FROM           992  '992'

2033     996  LOAD_FAST             0  'self'
         999  LOAD_ATTR            49  'clothingsVest'
        1002  LOAD_FAST             7  'vestIdx'
        1005  LOAD_CONST            1  0
        1008  BINARY_SUBSCR    
        1009  BINARY_SUBSCR    
        1010  STORE_FAST           18  'layerVest'

2034    1013  LOAD_GLOBAL          26  'NodePathCollection'
        1016  CALL_FUNCTION_0       0  None
        1019  STORE_FAST           12  'parts'

2037    1022  LOAD_FAST             0  'self'
        1025  LOAD_ATTR            28  'clothesTextures'
        1028  LOAD_CONST            0  None
        1031  COMPARE_OP            3  '!='
        1034  JUMP_IF_FALSE        38  'to 1075'
      1037_0  THEN                     1076
        1037  POP_TOP          

2038    1038  LOAD_FAST             0  'self'
        1041  LOAD_ATTR            30  'setPartTexture'
        1044  LOAD_CONST           11  'VEST'
        1047  LOAD_FAST             7  'vestIdx'
        1050  LOAD_CONST            1  0
        1053  BINARY_SUBSCR    
        1054  LOAD_FAST             7  'vestIdx'
        1057  LOAD_CONST            4  1
        1060  BINARY_SUBSCR    
        1061  LOAD_FAST            18  'layerVest'
        1064  LOAD_CONST            1  0
        1067  BINARY_SUBSCR    
        1068  CALL_FUNCTION_4       4  None
        1071  POP_TOP          
        1072  JUMP_FORWARD          1  'to 1076'
      1075_0  COME_FROM          1034  '1034'
        1075  POP_TOP          
      1076_0  COME_FROM          1072  '1072'

2039    1076  SETUP_LOOP           81  'to 1160'
        1079  LOAD_GLOBAL          31  'range'
        1082  LOAD_CONST            1  0
        1085  LOAD_GLOBAL          32  'len'
        1088  LOAD_FAST            18  'layerVest'
        1091  LOAD_CONST            1  0
        1094  BINARY_SUBSCR    
        1095  CALL_FUNCTION_1       1  None
        1098  CALL_FUNCTION_2       2  None
        1101  GET_ITER         
        1102  FOR_ITER             54  'to 1159'
        1105  STORE_FAST           20  'j'

2040    1108  LOAD_FAST             0  'self'
        1111  LOAD_ATTR            51  'clothingsLayer2'
        1114  LOAD_FAST            18  'layerVest'
        1117  LOAD_CONST            1  0
        1120  BINARY_SUBSCR    
        1121  LOAD_FAST            20  'j'
        1124  BINARY_SUBSCR    
        1125  BINARY_SUBSCR    
        1126  STORE_FAST           12  'parts'

2041    1129  LOAD_FAST            12  'parts'
        1132  LOAD_ATTR            35  'getNumPaths'
        1135  CALL_FUNCTION_0       0  None
        1138  JUMP_IF_FALSE        14  'to 1155'
        1141  POP_TOP          

2042    1142  LOAD_FAST            12  'parts'
        1145  LOAD_ATTR             4  'unstash'
        1148  CALL_FUNCTION_0       0  None
        1151  POP_TOP          
        1152  JUMP_BACK          1102  'to 1102'
      1155_0  COME_FROM          1138  '1138'
        1155  POP_TOP          
        1156  JUMP_BACK          1102  'to 1102'
        1159  POP_BLOCK        
      1160_0  COME_FROM          1076  '1076'

2043    1160  LOAD_FAST            12  'parts'
        1163  LOAD_ATTR            35  'getNumPaths'
        1166  CALL_FUNCTION_0       0  None
        1169  JUMP_IF_FALSE        85  'to 1257'
      1172_0  THEN                     1258
        1172  POP_TOP          

2045    1173  LOAD_FAST             7  'vestIdx'
        1176  LOAD_CONST            1  0
        1179  BINARY_SUBSCR    
        1180  LOAD_CONST            4  1
        1183  COMPARE_OP            4  '>'
        1186  JUMP_IF_FALSE        32  'to 1221'
        1189  POP_TOP          

2046    1190  LOAD_FAST             0  'self'
        1193  LOAD_ATTR            52  'handleLayer2Hiding'
        1196  LOAD_FAST             0  'self'
        1199  LOAD_ATTR            34  'clothingsLayer1'
        1202  LOAD_FAST             3  'layerShirtModified'
        1205  LOAD_CONST           12  'base'
        1208  LOAD_CONST           13  'front'
        1211  LOAD_CONST           14  'collar_v_low'
        1214  CALL_FUNCTION_5       5  None
        1217  POP_TOP          
        1218  JUMP_FORWARD         20  'to 1241'
      1221_0  COME_FROM          1186  '1186'
        1221  POP_TOP          

2048    1222  LOAD_FAST             0  'self'
        1225  LOAD_ATTR            52  'handleLayer2Hiding'
        1228  LOAD_FAST             0  'self'
        1231  LOAD_ATTR            34  'clothingsLayer1'
        1234  LOAD_FAST             3  'layerShirtModified'
        1237  CALL_FUNCTION_2       2  None
        1240  POP_TOP          
      1241_0  COME_FROM          1218  '1218'

2049    1241  LOAD_FAST             0  'self'
        1244  LOAD_ATTR            36  'handleLayer1Hiding'
        1247  LOAD_FAST            18  'layerVest'
        1250  CALL_FUNCTION_1       1  None
        1253  POP_TOP          
        1254  JUMP_FORWARD          1  'to 1258'
      1257_0  COME_FROM          1169  '1169'
        1257  POP_TOP          
      1258_0  COME_FROM          1254  '1254'

2052    1258  LOAD_FAST             0  'self'
        1261  LOAD_ATTR            53  'handleHeadHiding'
        1264  CALL_FUNCTION_0       0  None
        1267  POP_TOP          

2055    1268  LOAD_FAST             0  'self'
        1271  LOAD_ATTR            54  'clothingsBelt'
        1274  LOAD_FAST            13  'beltIdx'
        1277  LOAD_CONST            1  0
        1280  BINARY_SUBSCR    
        1281  BINARY_SUBSCR    
        1282  STORE_FAST            6  'layerBelt'

2056    1285  LOAD_GLOBAL          26  'NodePathCollection'
        1288  CALL_FUNCTION_0       0  None
        1291  STORE_FAST           12  'parts'

2059    1294  LOAD_FAST             0  'self'
        1297  LOAD_ATTR            28  'clothesTextures'
        1300  LOAD_CONST            0  None
        1303  COMPARE_OP            3  '!='
        1306  JUMP_IF_FALSE        38  'to 1347'
      1309_0  THEN                     1348
        1309  POP_TOP          

2060    1310  LOAD_FAST             0  'self'
        1313  LOAD_ATTR            30  'setPartTexture'
        1316  LOAD_CONST           15  'BELT'
        1319  LOAD_FAST            13  'beltIdx'
        1322  LOAD_CONST            1  0
        1325  BINARY_SUBSCR    
        1326  LOAD_FAST            13  'beltIdx'
        1329  LOAD_CONST            4  1
        1332  BINARY_SUBSCR    
        1333  LOAD_FAST             6  'layerBelt'
        1336  LOAD_CONST            1  0
        1339  BINARY_SUBSCR    
        1340  CALL_FUNCTION_4       4  None
        1343  POP_TOP          
        1344  JUMP_FORWARD          1  'to 1348'
      1347_0  COME_FROM          1306  '1306'
        1347  POP_TOP          
      1348_0  COME_FROM          1344  '1344'

2064    1348  SETUP_LOOP           81  'to 1432'
        1351  LOAD_GLOBAL          31  'range'
        1354  LOAD_CONST            1  0
        1357  LOAD_GLOBAL          32  'len'
        1360  LOAD_FAST             6  'layerBelt'
        1363  LOAD_CONST            1  0
        1366  BINARY_SUBSCR    
        1367  CALL_FUNCTION_1       1  None
        1370  CALL_FUNCTION_2       2  None
        1373  GET_ITER         
        1374  FOR_ITER             54  'to 1431'
        1377  STORE_FAST           20  'j'

2065    1380  LOAD_FAST             0  'self'
        1383  LOAD_ATTR            51  'clothingsLayer2'
        1386  LOAD_FAST             6  'layerBelt'
        1389  LOAD_CONST            1  0
        1392  BINARY_SUBSCR    
        1393  LOAD_FAST            20  'j'
        1396  BINARY_SUBSCR    
        1397  BINARY_SUBSCR    
        1398  STORE_FAST           12  'parts'

2066    1401  LOAD_FAST            12  'parts'
        1404  LOAD_ATTR            35  'getNumPaths'
        1407  CALL_FUNCTION_0       0  None
        1410  JUMP_IF_FALSE        14  'to 1427'
        1413  POP_TOP          

2067    1414  LOAD_FAST            12  'parts'
        1417  LOAD_ATTR             4  'unstash'
        1420  CALL_FUNCTION_0       0  None
        1423  POP_TOP          
        1424  JUMP_BACK          1374  'to 1374'
      1427_0  COME_FROM          1410  '1410'
        1427  POP_TOP          
        1428  JUMP_BACK          1374  'to 1374'
        1431  POP_BLOCK        
      1432_0  COME_FROM          1348  '1348'

2068    1432  LOAD_FAST            12  'parts'
        1435  LOAD_ATTR            35  'getNumPaths'
        1438  CALL_FUNCTION_0       0  None
        1441  JUMP_IF_TRUE         17  'to 1461'
        1444  POP_TOP          
        1445  LOAD_FAST             7  'vestIdx'
        1448  LOAD_CONST            1  0
        1451  BINARY_SUBSCR    
        1452  LOAD_CONST           16  3
        1455  COMPARE_OP            2  '=='
      1458_0  COME_FROM          1441  '1441'
        1458  JUMP_IF_FALSE        26  'to 1487'
      1461_0  THEN                     1488
        1461  POP_TOP          

2070    1462  LOAD_FAST             0  'self'
        1465  LOAD_ATTR            52  'handleLayer2Hiding'
        1468  LOAD_FAST             0  'self'
        1471  LOAD_ATTR            34  'clothingsLayer1'
        1474  LOAD_FAST            15  'layerPant'
        1477  LOAD_CONST           17  'belt'
        1480  CALL_FUNCTION_3       3  None
        1483  POP_TOP          
        1484  JUMP_FORWARD          1  'to 1488'
      1487_0  COME_FROM          1458  '1458'
        1487  POP_TOP          
      1488_0  COME_FROM          1484  '1484'

2071    1488  LOAD_FAST            12  'parts'
        1491  LOAD_ATTR            35  'getNumPaths'
        1494  CALL_FUNCTION_0       0  None
        1497  JUMP_IF_FALSE        43  'to 1543'
        1500  POP_TOP          
        1501  LOAD_FAST             7  'vestIdx'
        1504  LOAD_CONST            1  0
        1507  BINARY_SUBSCR    
        1508  LOAD_CONST           16  3
        1511  COMPARE_OP            2  '=='
        1514  JUMP_IF_FALSE        26  'to 1543'
        1517  POP_TOP          

2072    1518  LOAD_FAST             0  'self'
        1521  LOAD_ATTR            52  'handleLayer2Hiding'
        1524  LOAD_FAST             0  'self'
        1527  LOAD_ATTR            51  'clothingsLayer2'
        1530  LOAD_FAST            18  'layerVest'
        1533  LOAD_CONST           17  'belt'
        1536  CALL_FUNCTION_3       3  None
        1539  POP_TOP          
        1540  JUMP_ABSOLUTE      1548  'to 1548'
      1543_0  COME_FROM          1514  '1514'
      1543_1  COME_FROM          1497  '1497'
        1543  POP_TOP          
        1544  JUMP_FORWARD          1  'to 1548'
        1547  POP_TOP          
      1548_0  COME_FROM          1544  '1544'

2075    1548  LOAD_FAST             0  'self'
        1551  LOAD_ATTR            56  'clothingsCoat'
        1554  LOAD_FAST            17  'coatIdx'
        1557  LOAD_CONST            1  0
        1560  BINARY_SUBSCR    
        1561  BINARY_SUBSCR    
        1562  STORE_FAST            4  'layerCoat'

2076    1565  LOAD_GLOBAL          26  'NodePathCollection'
        1568  CALL_FUNCTION_0       0  None
        1571  STORE_FAST           12  'parts'

2079    1574  LOAD_FAST             0  'self'
        1577  LOAD_ATTR            28  'clothesTextures'
        1580  LOAD_CONST            0  None
        1583  COMPARE_OP            3  '!='
        1586  JUMP_IF_FALSE        62  'to 1651'
      1589_0  THEN                     1652
        1589  POP_TOP          

2081    1590  LOAD_FAST            17  'coatIdx'
        1593  LOAD_CONST            1  0
        1596  BINARY_SUBSCR    
        1597  LOAD_GLOBAL          58  'ClothingGlobals'
        1600  LOAD_ATTR            59  'navy_coat_geoms'
        1603  COMPARE_OP            7  'not-in'
        1606  JUMP_IF_FALSE        38  'to 1647'
      1609_0  THEN                     1648
        1609  POP_TOP          

2082    1610  LOAD_FAST             0  'self'
        1613  LOAD_ATTR            30  'setPartTexture'
        1616  LOAD_CONST           18  'COAT'
        1619  LOAD_FAST            17  'coatIdx'
        1622  LOAD_CONST            1  0
        1625  BINARY_SUBSCR    
        1626  LOAD_FAST            17  'coatIdx'
        1629  LOAD_CONST            4  1
        1632  BINARY_SUBSCR    
        1633  LOAD_FAST             4  'layerCoat'
        1636  LOAD_CONST            1  0
        1639  BINARY_SUBSCR    
        1640  CALL_FUNCTION_4       4  None
        1643  POP_TOP          
        1644  JUMP_ABSOLUTE      1652  'to 1652'
      1647_0  COME_FROM          1606  '1606'
        1647  POP_TOP          
        1648  JUMP_FORWARD          1  'to 1652'
      1651_0  COME_FROM          1586  '1586'
        1651  POP_TOP          
      1652_0  COME_FROM          1648  '1648'

2083    1652  SETUP_LOOP           81  'to 1736'
        1655  LOAD_GLOBAL          31  'range'
        1658  LOAD_CONST            1  0
        1661  LOAD_GLOBAL          32  'len'
        1664  LOAD_FAST             4  'layerCoat'
        1667  LOAD_CONST            1  0
        1670  BINARY_SUBSCR    
        1671  CALL_FUNCTION_1       1  None
        1674  CALL_FUNCTION_2       2  None
        1677  GET_ITER         
        1678  FOR_ITER             54  'to 1735'
        1681  STORE_FAST           20  'j'

2084    1684  LOAD_FAST             0  'self'
        1687  LOAD_ATTR            60  'clothingsLayer3'
        1690  LOAD_FAST             4  'layerCoat'
        1693  LOAD_CONST            1  0
        1696  BINARY_SUBSCR    
        1697  LOAD_FAST            20  'j'
        1700  BINARY_SUBSCR    
        1701  BINARY_SUBSCR    
        1702  STORE_FAST           12  'parts'

2085    1705  LOAD_FAST            12  'parts'
        1708  LOAD_ATTR            35  'getNumPaths'
        1711  CALL_FUNCTION_0       0  None
        1714  JUMP_IF_FALSE        14  'to 1731'
        1717  POP_TOP          

2086    1718  LOAD_FAST            12  'parts'
        1721  LOAD_ATTR             4  'unstash'
        1724  CALL_FUNCTION_0       0  None
        1727  POP_TOP          
        1728  JUMP_BACK          1678  'to 1678'
      1731_0  COME_FROM          1714  '1714'
        1731  POP_TOP          
        1732  JUMP_BACK          1678  'to 1678'
        1735  POP_BLOCK        
      1736_0  COME_FROM          1652  '1652'

2087    1736  LOAD_FAST            12  'parts'
        1739  LOAD_ATTR            35  'getNumPaths'
        1742  CALL_FUNCTION_0       0  None
        1745  JUMP_IF_FALSE       121  'to 1869'
      1748_0  THEN                     1870
        1748  POP_TOP          

2088    1749  LOAD_FAST            17  'coatIdx'
        1752  LOAD_CONST            1  0
        1755  BINARY_SUBSCR    
        1756  LOAD_CONST           19  2
        1759  COMPARE_OP            2  '=='
        1762  JUMP_IF_FALSE        46  'to 1811'
        1765  POP_TOP          
        1766  LOAD_FAST             7  'vestIdx'
        1769  LOAD_CONST            1  0
        1772  BINARY_SUBSCR    
        1773  LOAD_CONST           16  3
        1776  COMPARE_OP            2  '=='
        1779  JUMP_IF_FALSE        29  'to 1811'
        1782  POP_TOP          

2089    1783  LOAD_FAST             0  'self'
        1786  LOAD_ATTR            61  'handleLayer3Hiding'
        1789  LOAD_FAST             0  'self'
        1792  LOAD_ATTR            51  'clothingsLayer2'
        1795  LOAD_FAST            18  'layerVest'
        1798  LOAD_FAST             3  'layerShirtModified'
        1801  LOAD_CONST           20  'legs_base'
        1804  CALL_FUNCTION_4       4  None
        1807  POP_TOP          
        1808  JUMP_FORWARD         23  'to 1834'
      1811_0  COME_FROM          1779  '1779'
      1811_1  COME_FROM          1762  '1762'
        1811  POP_TOP          

2091    1812  LOAD_FAST             0  'self'
        1815  LOAD_ATTR            61  'handleLayer3Hiding'
        1818  LOAD_FAST             0  'self'
        1821  LOAD_ATTR            51  'clothingsLayer2'
        1824  LOAD_FAST            18  'layerVest'
        1827  LOAD_FAST             3  'layerShirtModified'
        1830  CALL_FUNCTION_3       3  None
        1833  POP_TOP          
      1834_0  COME_FROM          1808  '1808'

2092    1834  LOAD_FAST             0  'self'
        1837  LOAD_ATTR            52  'handleLayer2Hiding'
        1840  LOAD_FAST             0  'self'
        1843  LOAD_ATTR            51  'clothingsLayer2'
        1846  LOAD_FAST             6  'layerBelt'
        1849  CALL_FUNCTION_2       2  None
        1852  POP_TOP          

2093    1853  LOAD_FAST             0  'self'
        1856  LOAD_ATTR            36  'handleLayer1Hiding'
        1859  LOAD_FAST             4  'layerCoat'
        1862  CALL_FUNCTION_1       1  None
        1865  POP_TOP          
        1866  JUMP_FORWARD          1  'to 1870'
      1869_0  COME_FROM          1745  '1745'
        1869  POP_TOP          
      1870_0  COME_FROM          1866  '1866'

2096    1870  LOAD_FAST             0  'self'
        1873  LOAD_ATTR             5  'pirate'
        1876  LOAD_ATTR            62  'generateColor'
        1879  CALL_FUNCTION_0       0  None
        1882  POP_TOP          

2097    1883  LOAD_FAST             0  'self'
        1886  LOAD_ATTR             5  'pirate'
        1889  LOAD_ATTR            63  'generateClothesColor'
        1892  CALL_FUNCTION_0       0  None
        1895  POP_TOP          
        1896  LOAD_CONST            0  None
        1899  RETURN_VALUE     

Parse error at or near `LOAD_CONST' instruction at offset 1896

    def handleClothesGui(self, type, texIdx):
        clothing = self.currentClothing[type]
        if texIdx >= len(clothes_textures[type][clothing[0]]):
            self.currentClothing[type][1] = 0
        if texIdx < 0:
            self.currentClothing[type][1] = len(clothes_textures[type][clothing[0]]) - 1
        self.pirate.setClothesByType(type, clothing[0], clothing[1])
        self.handleClothesHiding()

    def getTextureChoices(self, clothesIdx):
        return clothes_textures[clothesIdx]

    def handleLayer1Hiding(self, element):
        parts = self.bodys
        for i in range(1, len(element)):
            idx = element[i]
            parts[-idx].stash()

    def handleLayer2Hiding(self, clothingLayer, layer1Element, hide1='base', hide2=None, hide3=None):
        for i in range(0, len(layer1Element[0])):
            idx = layer1Element[0][i]
            parts = clothingLayer[idx]
            for j in range(0, parts.getNumPaths()):
                if hide1 != None and parts[j].getName().find(hide1) != -1:
                    parts[j].stash()
                elif hide2 != None and parts[j].getName().find(hide2) != -1:
                    parts[j].stash()
                elif hide3 != None and parts[j].getName().find(hide3) != -1:
                    parts[j].stash()

        return

    def handleLayer3Hiding(self, clothingLayer, layer2Element, layer1Element, show1=None):
        for i in range(0, len(layer2Element[0])):
            parts = clothingLayer[layer2Element[0][i]]
            for j in range(0, parts.getNumPaths()):
                if parts[j].getName().find('front') < 0:
                    if show1:
                        if parts[j].getName().find(show1) < 0:
                            parts[j].stash()
                    else:
                        parts[j].stash()

        if layer1Element == None:
            return
        for i in range(0, len(layer1Element[0])):
            parts = self.clothingsLayer1[layer1Element[0][i]]
            for j in range(0, parts.getNumPaths()):
                if parts[j].getName().find('front') < 0:
                    if parts[j].getName().find('collar') < 0:
                        parts[j].stash()

        return

    def getTattooBaseTexture(self):
        return 'male_tattoomap'

    def handleTattooMapping(self):
        parts = self.body.getNumPaths()
        tex = TattooGlobals.getTattooImage(0)
        tex.setWrapU(Texture.WMBorderColor)
        tex.setWrapV(Texture.WMBorderColor)
        tex.setBorderColor(VBase4(1.0, 1.0, 1.0, 0.0))
        for i in range(parts):
            self.body.getPath(i).setTexture(self.tattooStage, tex)

    def hideAllJewelry(self):
        self.jewelryLEarIdx = [0, 0, 0]
        self.jewelryREarIdx = [0, 0, 0]
        self.jewelryLBrowIdx = [0, 0, 0]
        self.jewelryRBrowIdx = [0, 0, 0]
        self.jewelryNoseIdx = [0, 0, 0]
        self.jewelryMouthIdx = [0, 0, 0]
        self.jewelryLHandIdx = [0, 0, 0]
        self.jewelryRHandIdx = [0, 0, 0]
        self.accFace.stash()
        self.accBody.stash()

    def handleJewelryOptions(self, key, increment=True):
        options = jewelry_options[key]
        idx = self.currentJewelry[key][0]
        primaryColor = HumanDNA.jewelryColors[self.currentJewelry[key][1]]
        secondaryColor = HumanDNA.jewelryColors[self.currentJewelry[key][2]]
        self.jewelrySets[key][idx][0].stash()
        self.jewelrySets[key][idx][1].stash()
        if increment:
            idx += 1
            length = len(self.jewelrySets[key])
            if idx >= length:
                idx = 0
        else:
            idx -= 1
            length = len(self.jewelrySets[key])
            if idx < length:
                idx = length - 1
        self.jewelrySets[key][idx][0].unstash()
        if primaryColor:
            self.jewelrySets[key][idx][0].setColor(primaryColor)
        self.jewelrySets[key][idx][1].unstash()
        if secondaryColor:
            self.jewelrySets[key][idx][1].setColor(secondaryColor)
        self.currentJewelry[key][0] = idx

    def initialParts(self):
        self.clothing.stash()
        self.hair.stash()
        self.beard.stash()
        self.mustache.stash()
        self.hat.stash()
        self.eyepatch.stash()
        self.wig.stash()
        self.accBody.stash()
        self.accFace.stash()

    def setFromDNA(self):
        zombie = self.pirate.zombie
        if self.pirate.style == None:
            self.clothingsPant[0][0].unstash()
            self.bodys[5].stash()
            self.bodys[10].stash()
            self.bodys[11].stash()
        else:
            self.tattoos[0] = self.pirate.style.getTattooChest()
            self.handleClothesHiding()
            self.handleHeadHiding()
            self.hairIdx = self.pirate.style.getHairHair()
            self.beardIdx = self.pirate.style.getHairBeard()
            self.mustacheIdx = self.pirate.style.getHairMustache()
            self.handleJewelryHiding()
        return

    def makeZombie(self):
        self.dnaZomb.setHairColor(ZOMB_HAIR_COLOR)
        self.dnaZomb.setClothesShirt(ZOMB_SHIRT, ZOMB_SHIRT_TEXTURE)
        self.dnaZomb.setClothesVest(ZOMB_VEST, ZOMB_VEST_TEXTURE)
        self.dnaZomb.setClothesCoat(ZOMB_COAT, ZOMB_COAT_TEXTURE)
        self.dnaZomb.setClothesPant(ZOMB_PANT, ZOMB_PANT_TEXTURE)
        self.dnaZomb.setClothesBelt(ZOMB_BELT)
        self.dnaZomb.setClothesShoe(ZOMB_SHOE, ZOMB_SHOE_TEXTURE)
        self.dnaZomb.setClothesTopColor(0, 0, 0)
        self.dnaZomb.setClothesBotColor(0, 0, 0)

    def generatePantSets(self):
        self.pantSets = []
        for pantIdx in xrange(len(self.clothingsPant)):
            pant = self.clothingsPant[pantIdx]
            texName = clothes_textures['PANT'][pantIdx][0]
            if pantIdx in ClothingGlobals.shopkeep_pant_geoms:
                tex = None
            else:
                tex = self.texDict.get(texName[0])
            flattenedSet = {'belt': NodePathCollection(), 'nobelt': NodePathCollection()}
            for lod in ['2000', '1000', '500']:
                pantData = {'belt': NodePathCollection(), 'nobelt': NodePathCollection()}
                for idx in pant[0]:
                    pieceSet = self.layer1LODs[idx][lod]
                    for i in xrange(pieceSet.getNumPaths()):
                        piece = pieceSet[i]
                        if piece.getName().find('belt') < 0:
                            pantData['nobelt'].addPath(piece)
                            pantData['belt'].addPath(piece)
                        else:
                            pantData['nobelt'].addPath(piece)

                for style1 in ['belt', 'nobelt']:
                    data = pantData[style1]
                    geomSet = self.flattenData(data, lod, tex)
                    flattenedSet[style1].addPathsFrom(geomSet)

            self.pantSets.append(flattenedSet)

        return

    def generateHatSets(self):
        self.hatSets = []
        for hatIdx in xrange(len(self.clothingsHat)):
            hat = self.clothingsHat[hatIdx]
            texName = clothes_textures['HAT'][hatIdx][0]
            sTex = texName[0].split('+')
            if len(sTex) > 1:
                tex = self.texDict.get(sTex[0])
            else:
                tex = self.texDict.get(texName[0])
            flattenedSet = NodePathCollection()
            for lod in ['2000', '1000', '500']:
                for idx in hat[0]:
                    hatData = NodePathCollection()
                    pieceSet = self.layer1LODs[idx][lod]
                    for i in xrange(pieceSet.getNumPaths()):
                        piece = pieceSet[i]
                        hatData.addPath(piece)

                    geomSet = self.flattenHatData(hatData, lod)
                    flattenedSet.addPathsFrom(geomSet)

            self.hatSets.append(flattenedSet)

    def generateShoeSets(self):
        self.shoeSets = []
        for shoeIdx in xrange(len(self.clothingsShoe)):
            shoe = self.clothingsShoe[shoeIdx]
            texName = clothes_textures['SHOE'][shoeIdx][0]
            tex = self.texDict.get(texName[0])
            flattenedSet = NodePathCollection()
            for lod in ['2000', '1000', '500']:
                shoeData = NodePathCollection()
                for idx in shoe[0]:
                    pieceSet = self.layer1LODs[idx][lod]
                    for i in xrange(pieceSet.getNumPaths()):
                        piece = pieceSet[i]
                        shoeData.addPath(piece)

                geomSet = self.flattenData(shoeData, lod, tex)
                flattenedSet.addPathsFrom(geomSet)

            self.shoeSets.append(flattenedSet)

    def generateShirtSets(self):
        self.shirtSets = []
        for shirtIdx in xrange(len(self.clothingsShirt)):
            shirt = self.clothingsShirt[shirtIdx]
            texName = clothes_textures['SHIRT'][shirtIdx][0]
            tex = self.texDict.get(texName[0])
            flattenedSet = {'nobelt': {'full': NodePathCollection(), 'openVest': NodePathCollection(), 'closedVest': NodePathCollection(), 'coat': NodePathCollection(), 'coat+closedVest': NodePathCollection()}, 'belt': {'full': NodePathCollection(), 'openVest': NodePathCollection(), 'closedVest': NodePathCollection(), 'coat': NodePathCollection(), 'coat+closedVest': NodePathCollection()}}
            for lod in ['2000', '1000', '500']:
                shirtData = {'nobelt': {'full': NodePathCollection(), 'openVest': NodePathCollection(), 'closedVest': NodePathCollection(), 'coat': NodePathCollection(), 'coat+closedVest': NodePathCollection()}, 'belt': {'full': NodePathCollection(), 'openVest': NodePathCollection(), 'closedVest': NodePathCollection(), 'coat': NodePathCollection(), 'coat+closedVest': NodePathCollection()}}
                for idx in shirt[0]:
                    if idx == 4 or idx == 5:
                        if idx == 4:
                            pieceSet = self.layer1LODs[6][lod]
                        else:
                            pieceSet = self.layer1LODs[7][lod]
                        for i in xrange(pieceSet.getNumPaths()):
                            piece = pieceSet[i]
                            shirtData['belt']['full'].addPath(piece)
                            if piece.getName().find('base') < 0:
                                shirtData['belt']['openVest'].addPath(piece)
                                if piece.getName().find('front') < 0 and piece.getName().find('collar_v_low') < 0:
                                    shirtData['belt']['closedVest'].addPath(piece)
                                if piece.getName().find('front') >= 0 or piece.getName().find('collar') >= 0:
                                    shirtData['belt']['coat'].addPath(piece)
                                if piece.getName().find('collar') >= 0 and piece.getName().find('collar_v_low') < 0:
                                    shirtData['belt']['coat+closedVest'].addPath(piece)

                        pieceSet = self.layer1LODs[idx][lod]
                        for i in xrange(pieceSet.getNumPaths()):
                            piece = pieceSet[i]
                            shirtData['nobelt']['full'].addPath(piece)
                            if piece.getName().find('base') < 0:
                                shirtData['nobelt']['openVest'].addPath(piece)
                                if piece.getName().find('front') < 0 and piece.getName().find('collar_v_low') < 0:
                                    shirtData['nobelt']['closedVest'].addPath(piece)
                                if piece.getName().find('front') >= 0 or piece.getName().find('collar') >= 0:
                                    shirtData['nobelt']['coat'].addPath(piece)
                                if piece.getName().find('collar') >= 0 and piece.getName().find('collar_v_low') < 0:
                                    shirtData['nobelt']['coat+closedVest'].addPath(piece)

                    else:
                        pieceSet = self.layer1LODs[idx][lod]
                        for i in xrange(pieceSet.getNumPaths()):
                            piece = pieceSet[i]
                            shirtData['belt']['full'].addPath(piece)
                            shirtData['nobelt']['full'].addPath(piece)
                            if piece.getName().find('base') < 0:
                                shirtData['belt']['openVest'].addPath(piece)
                                shirtData['nobelt']['openVest'].addPath(piece)
                                if piece.getName().find('front') < 0 and piece.getName().find('collar_v_low') < 0:
                                    shirtData['belt']['closedVest'].addPath(piece)
                                    shirtData['nobelt']['closedVest'].addPath(piece)
                                if piece.getName().find('front') >= 0 or piece.getName().find('collar') >= 0:
                                    shirtData['belt']['coat'].addPath(piece)
                                    shirtData['nobelt']['coat'].addPath(piece)
                                if piece.getName().find('collar') >= 0 and piece.getName().find('collar_v_low') < 0:
                                    shirtData['belt']['coat+closedVest'].addPath(piece)
                                    shirtData['nobelt']['coat+closedVest'].addPath(piece)

                for style1 in ['belt', 'nobelt']:
                    for style2 in ['full', 'openVest', 'closedVest', 'coat', 'coat+closedVest']:
                        data = shirtData[style1][style2]
                        geomSet = self.flattenData(data, lod, tex)
                        flattenedSet[style1][style2].addPathsFrom(geomSet)

            self.shirtSets.append(flattenedSet)

    def generateVestSets(self):
        self.vestSets = []
        for vestIdx in xrange(len(self.clothingsVest)):
            vest = self.clothingsVest[vestIdx]
            texName = clothes_textures['VEST'][vestIdx][0]
            tex = self.texDict.get(texName[0])
            flattenedSet = {'belt': {'full': NodePathCollection(), 'coat': NodePathCollection(), 'coatSpecial': NodePathCollection()}, 'nobelt': {'full': NodePathCollection(), 'coat': NodePathCollection(), 'coatSpecial': NodePathCollection()}}
            for lod in ['2000', '1000', '500']:
                vestData = {'belt': {'full': NodePathCollection(), 'coat': NodePathCollection(), 'coatSpecial': NodePathCollection()}, 'nobelt': {'full': NodePathCollection(), 'coat': NodePathCollection(), 'coatSpecial': NodePathCollection()}}
                for idx in vest[0]:
                    pieceSet = self.layer2LODs[idx][lod]
                    for i in xrange(pieceSet.getNumPaths()):
                        piece = pieceSet[i]
                        legs_base = piece.getName().find('legs_base') >= 0
                        front = piece.getName().find('front') >= 0
                        coat = front
                        coatSpecial = front or legs_base
                        belt = not piece.getName().find('belt') >= 0
                        if belt:
                            vestData['belt']['full'].addPath(piece)
                            if coatSpecial:
                                vestData['belt']['coatSpecial'].addPath(piece)
                            if coat:
                                vestData['belt']['coat'].addPath(piece)
                        vestData['nobelt']['full'].addPath(piece)
                        if coatSpecial:
                            vestData['nobelt']['coatSpecial'].addPath(piece)
                        if coat:
                            vestData['nobelt']['coat'].addPath(piece)

                for style1 in ['belt', 'nobelt']:
                    for style2 in ['full', 'coat', 'coatSpecial']:
                        data = vestData[style1][style2]
                        geomSet = self.flattenData(data, lod, tex)
                        flattenedSet[style1][style2].addPathsFrom(geomSet)

            self.vestSets.append(flattenedSet)

    def generateCoatSets(self):
        self.coatSets = []
        for coatIdx in xrange(len(self.clothingsCoat)):
            coat = self.clothingsCoat[coatIdx]
            texName = clothes_textures['COAT'][coatIdx][0]
            if coatIdx in ClothingGlobals.navy_coat_geoms:
                tex = None
            else:
                tex = self.texDict.get(texName[0])
            flattenedSet = NodePathCollection()
            for lod in ['2000', '1000', '500']:
                geomSet = self.flattenSet(coat[0], self.layer3LODs, lod, tex)
                flattenedSet.addPathsFrom(geomSet)

            self.coatSets.append(flattenedSet)

        return

    def generateBeltSets(self):
        self.beltSets = []
        for beltIdx in xrange(len(self.clothingsBelt)):
            belt = self.clothingsBelt[beltIdx]
            texName = clothes_textures['BELT'][beltIdx][0][0].split('+')
            tex = self.texDict.get(texName[0])
            flattenedSet = {'full': [NodePathCollection(), NodePathCollection()], 'coat': [NodePathCollection(), NodePathCollection()]}
            for lod in ['2000', '1000', '500']:
                beltData = {'full': [NodePathCollection(), NodePathCollection()], 'coat': [NodePathCollection(), NodePathCollection()]}
                idx1 = belt[0][0]
                pieceSet1 = self.layer2LODs[idx1][lod]
                for i in xrange(pieceSet1.getNumPaths()):
                    piece = pieceSet1[i]
                    beltData['full'][0].addPath(piece)
                    if piece.getName().find('base') < 0:
                        beltData['coat'][0].addPath(piece)

                if len(belt[0]) > 1:
                    idx2 = belt[0][1]
                    pieceSet2 = self.layer2LODs[idx2][lod]
                    for i in xrange(pieceSet2.getNumPaths()):
                        piece = pieceSet2[i]
                        beltData['full'][1].addPath(piece)
                        if piece.getName().find('base') < 0:
                            beltData['coat'][1].addPath(piece)

                for style in ['full', 'coat']:
                    for i in [0, 1]:
                        data = beltData[style]
                        geomSet = self.flattenData(data[i], lod, tex)
                        flattenedSet[style][i].addPathsFrom(geomSet)

            self.beltSets.append(flattenedSet)

    def generateHairSets(self):
        cuts = [
         'cut_none', 'cut_captain', 'cut_tricorn', 'cut_navy', 'cut_admiral', 'cut_admiral', 'cut_bandanna_full', 'cut_bandanna', 'cut_beanie', 'cut_admiral']

        def getBasicData():
            data = []
            for i in xrange(len(self.hats)):
                data.append(NodePathCollection())

            return data

        nonCutOpts = {}
        self.hairSets = []
        dataCache = {'2000': {}, '1000': {}, '500': {}}
        for hairIdx in xrange(len(self.hairs)):
            hairParts = self.hairs[hairIdx]
            flattenedSet = getBasicData()
            for hatIdx in xrange(len(self.hats)):
                for lod in ['2000', '1000', '500']:
                    hairIndices = set()
                    hairCutIndices = set()
                    hairData = NodePathCollection()
                    for partIdx in hairParts:
                        hair = self.hairLODs[partIdx][lod]
                        if partIdx == 1 or hatIdx == 0:
                            hairData.addPathsFrom(hair)
                            hairIndices.add(partIdx)
                        elif partIdx > 0:
                            hairCut = self.hairCutLODs[partIdx][lod]
                            cutFound = 0
                            for j in xrange(hairCut.getNumPaths()):
                                if hairCut[j].getName().find(cuts[hatIdx]) >= 0:
                                    hairCutIndices.add(partIdx)
                                    hairData.addPath(hairCut[j])
                                    cutFound = 1

                            if not cutFound:
                                if hatIdx == 7 and partIdx == 2 or partIdx == 5 or partIdx == 8 or partIdx == 10:
                                    hairIndices.add(partIdx)
                                    hairData.addPathsFrom(hair)

                    hl = list(hairIndices)
                    hl.sort()
                    t1 = tuple(hl)
                    hcl = list(hairCutIndices)
                    hcl.sort()
                    t2 = tuple(hcl)
                    cachedCopy = dataCache[lod].get((hatIdx, t1, t2))
                    if cachedCopy:
                        flattenedSet[hatIdx].addPathsFrom(cachedCopy)
                    else:
                        geomSet = self.flattenData(hairData, lod, False)
                        flattenedSet[hatIdx].addPathsFrom(geomSet)
                        dataCache[lod][(hatIdx, t1, t2)] = geomSet

            self.hairSets.append(flattenedSet)

        self.dataCache = dataCache

    def flattenSet(self, parts, layerSet, lod, stripTex=True):
        flattenMe = NodePath('flattenMe')
        for i in parts:
            geomData = layerSet[i][lod]
            for j in xrange(geomData.getNumPaths()):
                geomData[j].copyTo(flattenMe)

        flattenMe.flattenStrong()
        geomSet = flattenMe.findAllMatches('**/+GeomNode')
        if stripTex:
            self.stripTexture(geomSet)
        geomSet.reparentTo(self.pirate.getLOD(lod).getChild(0))
        geomSet.stash()
        return geomSet

    def flattenData(self, geomData, lod, stripTex=True, flattenStrong=True):
        flattenMe = NodePath('flattenMe')
        for i in xrange(geomData.getNumPaths()):
            geomData[i].copyTo(flattenMe)

        if flattenStrong:
            flattenMe.flattenStrong()
        geomSet = flattenMe.findAllMatches('**/+GeomNode')
        if stripTex:
            self.stripTexture(geomSet)
        geomSet.reparentTo(self.pirate.getLOD(lod).getChild(0))
        geomSet.stash()
        return geomSet

    def flattenHatData(self, geomData, lod):
        flattenMe = NodePath('flattenMe')
        for i in xrange(geomData.getNumPaths()):
            geomPart = geomData[i].copyTo(flattenMe)
            geomPart.setState(geomPart.getState().removeAttrib(TextureAttrib.getClassType()))
            geomNode = geomPart.node()
            for j in xrange(geomNode.getNumGeoms()):
                geomState = geomNode.getGeomState(j)
                if geomState.getAttrib(TextureAttrib.getClassType()).getTexture().getName().find('eather') < 0:
                    geomNode.setGeomState(j, geomState.removeAttrib(TextureAttrib.getClassType()))

        geomSet = flattenMe.findAllMatches('**/+GeomNode')
        for i in xrange(geomSet.getNumPaths()):
            geomSet.reparentTo(self.pirate.getLOD(lod).getChild(0))
            geomSet.stash()

        return geomSet

    def stripTexture(self, geomSet):
        for i in xrange(geomSet.getNumPaths()):
            geomSet[i].setState(geomSet[i].getState().removeAttrib(TextureAttrib.getClassType()))
            geomNode = geomSet[i].node()
            for j in xrange(geomNode.getNumGeoms()):
                geomState = geomNode.getGeomState(j)
                geomNode.setGeomState(j, geomState.removeAttrib(TextureAttrib.getClassType()))
