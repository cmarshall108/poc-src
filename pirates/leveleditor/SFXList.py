# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.leveleditor.SFXList
SOUND_FX_LIST = {
    'Cannon Fire': [
        'audio/cball_fire_1.mp3', 'audio/cball_fire_2.mp3',
        'audio/cball_fire_3.mp3', 'audio/cball_fire_4.mp3',
        'audio/cball_fire_5.mp3'
    ],
    'Distant Cannon': [
        'audio/dist_cannon_01.mp3', 'audio/dist_cannon_02.mp3',
        'audio/dist_cannon_03.mp3', 'audio/dist_cannon_04.mp3',
        'audio/dist_cannon_05.mp3', 'audio/dist_cannon_06.mp3',
        'audio/dist_cannon_07.mp3', 'audio/dist_cannon_08.mp3',
        'audio/dist_cannon_09.mp3', 'audio/dist_cannon_10.mp3'
    ],
    'Sword': [
        'audio/sword-clashNclang.mp3', 'audio/sword-swipeNclang1.mp3',
        'audio/sword-swipeNclang2.mp3', 'audio/sword-swipeNclang3.mp3'
    ],
    'Explosion': [
        'audio/explo_wood_1.mp3', 'audio/explo_wood_2.mp3',
        'audio/explode-w-glass.mp3'
    ]
}


def getSFXList():
    resultDic = {}
    totalList = []
    for sfxGroup in SOUND_FX_LIST.keys():
        sfxList = [[sfxGroup], SOUND_FX_LIST[sfxGroup]]
        totalList.append(sfxList)

    resultDic['["SFX Group"]'] = totalList
    return resultDic


# okay decompiling .\pirates\leveleditor\SFXList.pyc
