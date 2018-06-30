from pirates.battle import EnemyGlobals
from pirates.ship.ShipGlobals import *

CANCEL_QUEST = -1
MAXIMUM_MERC_WORK = 12


class QuestActions:

    Decline = 0
    Accept = 1
    Bribe = 2


class QuestItemNotification:

    AlreadyFound = 1
    ProgressMadeGoalMet = 2
    ProgressMadeGoalUnmet = 3
    ValidAttempt = 4
    InvalidAttempt = 5


class QuestItems:

    Key = 0
    SeaChart = 1
    Earring = 2
    RumBarrel = 3
    CrabClaw = 4
    CoinBag = 5
    TattooPattern = 6
    CopperRod = 7
    Blood = 8
    Flag = 9
    List = 10
    ArrestWarrant = 11
    Handkerchief = 12
    BatGuano = 13
    Remedy = 14
    PersonalEffects = 15
    EngravedPearl = 16
    SeveredArm = 17
    GatorSaliva = 18
    Venom = 19
    CursedWood = 20
    Map = 21
    Necklace = 22
    TinShipment = 23
    SandShipment = 24
    GlassRing = 25
    WoodenPlates = 26
    Chicken = 27
    Pig = 28
    Egg = 29
    Tooth = 30
    WaspWings = 31
    GatorScales = 32
    Poison = 33
    Mud = 34
    Grog = 35
    Doll = 36
    Dinghy = 37
    ReleaseOrders = 38
    HoneyBarrel = 39
    Dress = 40
    Dice = 41
    WaspEggs = 42
    Bile = 43
    RumBottle = 44
    Bracelet = 45
    Needle = 46
    KrakenEye = 47
    Powder = 48
    CrocWater = 49
    Entrails = 50
    Splinter = 51
    Dust = 52
    Earth = 53
    Lichen = 54
    Water = 55
    ScorpionEgg = 56
    BloodyTreasure = 57
    Nightshade = 58
    Whisker = 59
    Jar = 60
    Paper = 61
    Bone = 62
    BoneShavings = 63
    Chest = 64
    HookArm = 65
    Diamond = 66
    CigarBox = 67
    GoldChain = 68
    Cargo = 69
    Ladle = 70
    Sugar = 71
    Bottle = 72
    Molasses = 73
    Vanilla = 74
    BoneDust = 75
    SwampGas = 76
    Stinger = 77
    Bladder = 78
    Pint = 79
    Cinnamon = 80
    Coconut = 81
    Feather = 82
    Honey = 83
    Barnacles = 84
    Hairball = 85
    Flea = 86
    Drink = 87
    Schedule = 88
    Hair = 89
    Honeysuckle = 90
    Sap = 91
    Tear = 92
    Perfume = 93
    Oil = 94
    Rum = 95
    Orders = 96
    Salve = 97
    Wax = 98
    Meat = 99
    Plank = 100
    Nail = 101
    Pitch = 102
    Saw = 103
    Ship = 104
    Beam = 105
    Bolt = 106
    Sailcloth = 107
    Rope = 108
    Cannon = 109
    Figure = 110
    Parrot = 111
    Document = 112
    Eye = 113
    Painting = 114
    Treasure = 115
    Straw = 116
    Silk = 117
    Wire = 118
    Bag = 119
    Dirt = 120
    Ring = 121
    Medal = 122
    Reagent = 123
    ChessPiece = 124
    Figurine = 125
    Steel = 126
    Silver = 127
    Tongs = 128
    Coal = 129
    Message = 130
    Knife = 131
    Grenade = 132
    Branch = 133
    ShrunkenHead = 134
    Saltpeter = 135
    Charcoal = 136
    Sulfur = 137
    Fuse = 138
    Flint = 139
    Casing = 140
    Tar = 141
    TeleportTotem = 142
    BatWings = 143
    AlligatorTooth = 144
    EssenceOfWasp = 145
    TortuganArtifact = 146
    CottonYard = 147
    IronBar = 148
    AlligatorTail = 149
    CrabShell = 150
    BatHair = 151
    ScorpionBlood = 152
    ScorpionVenom = 153
    WhiskeyBarrel = 154
    SetOfBarGlasses = 155
    CoalBag = 156
    SmithingTools = 157
    PeterAttackerName = 158
    FlyTrapLeaf = 159
    FlyTrapRoot = 160
    NavyCoat = 161
    FirstMedal = 162
    EyeOfNabai = 163
    DollComponentHead = 164
    DollComponentTorso = 165
    DollComponentArmL = 166
    DollComponentArmR = 167
    DollComponentLegL = 168
    DollComponentLegR = 169
    NavyMuskets = 170
    NavyPants = 171
    SargeantsBadge = 172
    PrisonKey = 173
    FortTreasureDocument = 174
    SewingNeedle = 175
    GuardSchedule = 176
    NavySchedule = 177
    LatrineWater = 178
    MoonlitWater = 179
    BattleSaltWater = 180
    DicePair = 181
    WaterCanteen = 182
    Rubies = 183
    Amethyst = 184
    Sapphire = 185
    FineInk = 186
    Deed = 187
    EITCCoat = 188
    EITCPants = 189
    ShopApplication = 190
    Hide = 191
    Contract = 192
    BloodSample = 193
    Bandages = 194
    MedicalTools = 195
    Diary = 196
    ShipLog = 197
    FamilyHeirlooms = 198
    Gun = 199
    GunOrder = 200
    AntiquePistol = 201
    ShipPlans = 202
    BackgroundCheck = 203
    FineSteelBar = 204
    LeatherStraps = 205
    BladeSharpener = 206
    PirateLorePage = 207
    PirateLoreChest = 208
    PirateLoreBook = 209
    EITCManual = 210
    UnfinishedPirateLoreBook = 211
    GatorEye = 212
    Wasp = 213
    ScorpionEye = 214
    BatEye = 215
    CloudyBlueOrb = 216
    SkeletonRib = 217
    Badge = 218
    WritOfAuthority = 219
    GatorTooth = 220
    BatClaw = 221
    SkeletonBone = 222
    SunkenShipMast = 223
    BattleEarth = 224
    RelicPiece = 225
    CaptTeague = 226
    FlyTrapThread = 227
    RareFeather = 228
    EITCManifest = 229
    BinghamsDiary = 230
    BoltOfCloth = 231
    FineScissors = 232
    SilkThread = 233
    ScarletsPearl = 234
    LetterFromScarlet = 235
    BeltBuckle = 236
    FineShoeDesign = 237
    ScorpionShell = 238
    KrakenCloth = 239
    CursedButtons = 240
    CursedBark = 241
    CursedCloth = 242
    CursedThread = 243
    CursedNeedle = 244
    VoodooArtifact = 245
    RottenMeat = 246
    Compass = 247
    LockgrimsLetter = 248
    Tentacle = 249
    UrchinfistEye = 250
    CursedChest = 251
    FineRum = 252
    LuckyDeck = 253
    NavyShoeString = 254
    NavyAnchor = 255
    EITCParchment = 256
    EmptyFlask = 257
    Sail = 258
    ShipWheel = 259
    NavyFabric = 260
    CursedSailCloth = 261
    SpanishArmor = 262
    SpanishPistolComponent = 263
    GunStock = 264
    BoneHandle = 265
    LockOfHair = 266
    WoodenStatuette = 267
    GunPowder = 268
    Spar = 269
    StolenDaggers = 270
    Gems = 271
    NavySteel = 272
    GoldHandleRapier = 273


QuestHistoryLen = 300


class LocationIds:
    RAMBLESHACK_DOCK = '1190757402.45joswilso'
    PORT_ROYAL_ISLAND = '1150922126.8dzlu'
    PORT_ROYAL_PORT = '1155695180.13sdnaik'
    PORT_ROYAL_FORT_CHARLES = '1175621632.0dxschafe0'
    PORT_ROYAL_CAVE_A = '1164952144.06sdnaik'
    PORT_ROYAL_CAVE_B = '1165001772.05sdnaik'
    PORT_ROYAL_JUNGLE_A = '1169592956.59sdnaik'
    PORT_ROYAL_JUNGLE_B = '1161798288.34sdnaik'
    PORT_ROYAL_JUNGLE_C = '1164141722.61sdnaik'
    ANY_PORT_ROYAL_JUNGLE = 'AnyPortRoyalJungle'
    ANY_PORT_ROYAL_CAVE = 'AnyPortRoyalCave'
    GOVERNORS_MANSION = '1188163728.78joswilso'
    PORT_ROYAL_DINGHY = '1187144960.0dxschafe'
    PORT_ROYAL_GRAVEYARD = '1188511028.75joswilso'
    PORT_ROYAL_ALL = 'AllOfPortRoyal'
    TORTUGA_ISLAND = '1156207188.95dzlu'
    TORTUGA_PORT = '1158295517.91sdnaik'
    TORTUGA_JUNGLE_A_GRAVEYARD = '1165004570.58sdnaik'
    TORTUGA_JUNGLE_B_SWAMPY = '1165009856.72sdnaik'
    TORTUGA_JUNGLE_C = '1165009873.53sdnaik'
    TORTUGA_CAVE = '1158121765.09sdnaik'
    TORTUGA_SWAMP = '1169179552.88sdnaik'
    TORTUGA_ALL = 'AllOfTortuga'
    DEL_FUEGO_ISLAND = '1142018473.22dxschafe'
    DEL_FUEGO_FORT_DUNDEE = '1175825280.0dxschafe'
    DEL_FUEGO_PORT = '1158285017.39sdnaik'
    DEL_FUEGO_PORT_PULGAS = '1175622157.78sdnaik'
    DEL_FUEGO_CAVE_C = '1164929110.98sdnaik'
    DEL_FUEGO_CAVE_D = '1167862588.52sdnaik'
    DEL_FUEGO_CAVE_E = '1168057131.73sdnaik'
    DEL_FUEGO_JUNGLE_B = '1167857698.16sdnaik'
    DEL_FUEGO_ALL = 'AllOfPadresDelFuego'
    ANVIL_ISLAND = '1164135492.81dzlu'
    ANVIL_PORT = '1168745928.39WDIG'
    ANVIL_CAVE_BARBOSA = '1172209006.11sdnaik'
    ANVIL_ALL = 'AllOfDevilsAnvil'
    DRIFTWOOD_ISLAND = '1164763706.66sdnaik'
    DRIFTWOOD_PORT = '1176252928.0mike1'
    DRIFTWOOD_ALL = 'AllOfDriftwood'
    RUMRUNNER_ISLE = '1161282725.84kmuller'
    RUMRUNNER_PORT = '1176253312.0mike'
    RUMRUNNER_CELLAR = '1185994805.82kmuller0'
    RUMRUNNER_ALL = 'AllOfRumrunners'
    ISLA_PERDIDA = '1164157132.99dzlu'
    PERDIDA_PORT = '1168745561.13WDIG'
    PERDIDA_JUNGLE_B = '1172209955.25sdnaik'
    PERDIDA_ALL = 'AllOfPerdida'
    CUBA_ISLAND = '1160614528.73sdnaik'
    CUBA_PORT = '1162600301.39sdnaik'
    CUBA_SWAMP = '1161732578.06sdnaik'
    CUBA_ALL = 'AllOfCuba'
    KINGSHEAD_ISLAND = '1159933206.48sdnaik'
    KINGSHEAD_PORT = '1168743023.63sdnaik'
    KINGSHEAD_PORT_REAR = '1168743125.73sdnaik'
    KINGSHEAD_DOOR = '1189479168.0sdnaik0'
    KINGSHEAD_ALL = 'AllOfKingshead'
    ISLA_CANGREJOS = '1156359855.24bbathen'
    CANGREJOS_PORT = '1158295957.41sdnaik'
    CANGREJOS_ALL = 'AllOfCangrejos'
    CUTTHROAT_ISLAND = '1173382404.64sdnaik'
    CUTTHROAT_PORT = '1173382757.63sdnaik'
    CUTTHROAT_ALL = 'AllOfCutthroat'
    OUTCAST_ISLE = '1173381952.2sdnaik'
    OUTCAST_PORT = '1173382841.06sdnaik'
    OUTCAST_ALL = 'AllOfOutcast'
    ISLA_TORMENTA = '1164150392.42dzlu'
    TORMENTA_PORT = '1168741735.28sdnaik'
    TORMENTA_CAVE_B = '1172208344.92sdnaik'
    TORMENTA_ALL = 'AllOfTormenta'
    PARLOR_BUILDING = '1161805620.28Shochet'
    ANY_LARGE_ISLAND = 'AnyLargeIsland'
    ANY_LARGE_PORT = 'AnyLargePort'
    ANY_WILD_ISLAND = 'AnyWildIsland'
    ANY_WILD_PORT = 'AnyWildPort'
    ANY_LOCATION = 'AnyLocation'
    LocationDefs = {
        PORT_ROYAL_ISLAND: (PORT_ROYAL_ISLAND,),
        PORT_ROYAL_PORT: (PORT_ROYAL_PORT,),
        PORT_ROYAL_FORT_CHARLES: (PORT_ROYAL_FORT_CHARLES,),
        PORT_ROYAL_CAVE_A: (PORT_ROYAL_CAVE_A,),
        PORT_ROYAL_CAVE_B: (PORT_ROYAL_CAVE_B,),
        ANY_PORT_ROYAL_CAVE: (PORT_ROYAL_CAVE_A, PORT_ROYAL_CAVE_B),
        PORT_ROYAL_JUNGLE_A: (PORT_ROYAL_JUNGLE_A,),
        PORT_ROYAL_JUNGLE_B: (PORT_ROYAL_JUNGLE_B,),
        PORT_ROYAL_JUNGLE_C: (PORT_ROYAL_JUNGLE_C,),
        ANY_PORT_ROYAL_JUNGLE: (PORT_ROYAL_JUNGLE_A, PORT_ROYAL_JUNGLE_B,
                                PORT_ROYAL_JUNGLE_C),
        GOVERNORS_MANSION: (GOVERNORS_MANSION,),
        PORT_ROYAL_GRAVEYARD: (PORT_ROYAL_GRAVEYARD,),
        PORT_ROYAL_DINGHY: (PORT_ROYAL_DINGHY,),
        PORT_ROYAL_ALL:
        (PORT_ROYAL_ISLAND, PORT_ROYAL_PORT, PORT_ROYAL_FORT_CHARLES,
         PORT_ROYAL_CAVE_A, PORT_ROYAL_CAVE_B, PORT_ROYAL_JUNGLE_A,
         PORT_ROYAL_JUNGLE_B, PORT_ROYAL_JUNGLE_C, GOVERNORS_MANSION,
         PORT_ROYAL_GRAVEYARD, PORT_ROYAL_DINGHY),
        TORTUGA_ISLAND: (TORTUGA_ISLAND,),
        TORTUGA_PORT: (TORTUGA_PORT,),
        TORTUGA_JUNGLE_A_GRAVEYARD: (TORTUGA_JUNGLE_A_GRAVEYARD,),
        TORTUGA_JUNGLE_B_SWAMPY: (TORTUGA_JUNGLE_B_SWAMPY,),
        TORTUGA_JUNGLE_C: (TORTUGA_JUNGLE_C,),
        TORTUGA_CAVE: (TORTUGA_CAVE,),
        TORTUGA_SWAMP: (TORTUGA_SWAMP,),
        TORTUGA_ALL: (TORTUGA_ISLAND, TORTUGA_PORT, TORTUGA_JUNGLE_A_GRAVEYARD,
                      TORTUGA_JUNGLE_B_SWAMPY, TORTUGA_JUNGLE_C, TORTUGA_CAVE,
                      TORTUGA_SWAMP),
        DEL_FUEGO_ISLAND: (DEL_FUEGO_ISLAND,),
        DEL_FUEGO_FORT_DUNDEE: (DEL_FUEGO_FORT_DUNDEE,),
        DEL_FUEGO_PORT: (DEL_FUEGO_PORT,),
        DEL_FUEGO_PORT_PULGAS: (DEL_FUEGO_PORT_PULGAS,),
        DEL_FUEGO_CAVE_C: (DEL_FUEGO_CAVE_C,),
        DEL_FUEGO_CAVE_D: (DEL_FUEGO_CAVE_D,),
        DEL_FUEGO_CAVE_E: (DEL_FUEGO_CAVE_E,),
        DEL_FUEGO_JUNGLE_B: (DEL_FUEGO_JUNGLE_B,),
        DEL_FUEGO_ALL: (DEL_FUEGO_ISLAND, DEL_FUEGO_FORT_DUNDEE, DEL_FUEGO_PORT,
                        DEL_FUEGO_PORT_PULGAS, DEL_FUEGO_CAVE_C,
                        DEL_FUEGO_CAVE_D, DEL_FUEGO_CAVE_E, DEL_FUEGO_JUNGLE_B),
        CUBA_ISLAND: (CUBA_ISLAND,),
        CUBA_PORT: (CUBA_PORT,),
        CUBA_SWAMP: (CUBA_SWAMP,),
        CUBA_ALL: (CUBA_ISLAND, CUBA_PORT, CUBA_SWAMP),
        KINGSHEAD_ISLAND: (KINGSHEAD_ISLAND,),
        KINGSHEAD_PORT: (KINGSHEAD_PORT,),
        KINGSHEAD_PORT_REAR: (KINGSHEAD_PORT_REAR,),
        KINGSHEAD_DOOR: (KINGSHEAD_DOOR,),
        KINGSHEAD_ALL: (KINGSHEAD_ISLAND, KINGSHEAD_PORT, KINGSHEAD_PORT_REAR,
                        KINGSHEAD_DOOR),
        ANVIL_ISLAND: (ANVIL_ISLAND,),
        ANVIL_PORT: (ANVIL_PORT,),
        ANVIL_CAVE_BARBOSA: (ANVIL_CAVE_BARBOSA,),
        ANVIL_ALL: (ANVIL_ISLAND, ANVIL_PORT, ANVIL_CAVE_BARBOSA),
        DRIFTWOOD_ISLAND: (DRIFTWOOD_ISLAND,),
        DRIFTWOOD_PORT: (DRIFTWOOD_PORT,),
        DRIFTWOOD_ALL: (DRIFTWOOD_ISLAND, DRIFTWOOD_PORT),
        RUMRUNNER_ISLE: (RUMRUNNER_ISLE,),
        RUMRUNNER_PORT: (RUMRUNNER_PORT,),
        RUMRUNNER_CELLAR: (RUMRUNNER_CELLAR,),
        RUMRUNNER_ALL: (RUMRUNNER_ISLE, RUMRUNNER_PORT, RUMRUNNER_CELLAR),
        ISLA_PERDIDA: (ISLA_PERDIDA,),
        PERDIDA_PORT: (PERDIDA_PORT,),
        PERDIDA_JUNGLE_B: (PERDIDA_JUNGLE_B,),
        PERDIDA_ALL: (ISLA_PERDIDA, PERDIDA_PORT, PERDIDA_JUNGLE_B),
        OUTCAST_ISLE: (OUTCAST_ISLE,),
        OUTCAST_PORT: (OUTCAST_PORT,),
        OUTCAST_ALL: (OUTCAST_ISLE, OUTCAST_PORT),
        ISLA_TORMENTA: (ISLA_TORMENTA,),
        TORMENTA_PORT: (TORMENTA_PORT,),
        TORMENTA_CAVE_B: (TORMENTA_CAVE_B,),
        TORMENTA_ALL: (ISLA_TORMENTA, TORMENTA_PORT, TORMENTA_CAVE_B),
        CUTTHROAT_ISLAND: (CUTTHROAT_ISLAND,),
        CUTTHROAT_PORT: (CUTTHROAT_PORT,),
        CUTTHROAT_ALL: (CUTTHROAT_ISLAND, CUTTHROAT_PORT),
        ISLA_CANGREJOS: (ISLA_CANGREJOS,),
        CANGREJOS_PORT: (CANGREJOS_PORT,),
        CANGREJOS_ALL: (ISLA_CANGREJOS, CANGREJOS_PORT),
        ANY_LARGE_ISLAND: (PORT_ROYAL_ISLAND, TORTUGA_ISLAND, DEL_FUEGO_ISLAND,
                           CUBA_ISLAND, KINGSHEAD_ISLAND),
        ANY_LARGE_PORT: (PORT_ROYAL_PORT, TORTUGA_PORT, DEL_FUEGO_PORT,
                         DEL_FUEGO_PORT_PULGAS, CUBA_PORT, KINGSHEAD_PORT),
        ANY_WILD_ISLAND: (ANVIL_ISLAND, DRIFTWOOD_ISLAND, RUMRUNNER_ISLE,
                          ISLA_PERDIDA, OUTCAST_ISLE, ISLA_CANGREJOS,
                          CUTTHROAT_ISLAND, ISLA_TORMENTA),
        ANY_WILD_PORT: (ANVIL_PORT, DRIFTWOOD_PORT, RUMRUNNER_PORT,
                        PERDIDA_PORT, OUTCAST_PORT, CANGREJOS_PORT,
                        CUTTHROAT_PORT, TORMENTA_PORT),
        ANY_LOCATION:
        None
    }


def getLocationList(locationId):
    return LocationIds.LocationDefs.get(locationId)


class PropIds:

    PR_CRATE_1 = '1175737088.0dxschafe'
    PR_CRATE_2 = '1175737088.0dxschafe0'
    PR_CRATE_3 = '1175737216.0dxschafe'
    PR_CRATE_4 = '1175737216.0dxschafe0'
    PR_CRATE_5 = '1175737216.0dxschafe1'
    PR_CRATE_6 = '1175737216.0dxschafe2'
    PR_CRATE_7 = '1175737216.0dxschafe3'
    PR_CRATE_8 = '1175737216.0dxschafe4'
    PR_CRATE_9 = '1175737216.0dxschafe5'
    PR_CRATE_10 = '1175737344.0dxschafe'
    PR_CRATE_11 = '1175737344.0dxschafe0'
    PR_CRATE_12 = '1175737344.0dxschafe1'
    PR_CRATE_13 = '1175737344.0dxschafe2'
    PR_CRATE_14 = '1175737344.0dxschafe3'
    PR_CRATE_15 = '1175737472.0dxschafe'
    PR_CRATES = 'PortRoyalCrates'
    FC_DESK = '1170742144.0mike'
    FC_SHELF = '1175826048.0dxschafe0'
    FC_CLOCK = '1175826048.0dxschafe1'
    FC_BARREL_EASY_1 = '1177104768.0dxschafe'
    FC_BARREL_EASY_2 = '1177104896.0dxschafe0'
    FC_BARREL_EASY_3 = '1176414336.0dxschafe'
    FC_BARREL_EASY_4 = '1177104768.0dxschafe0'
    FC_EASY_BARRELS = 'FortCharlesEasyBarrels'
    FC_BARREL_MED_1 = '1177108352.0dxschafe'
    FC_BARREL_MED_2 = '1176414976.0dxschafe'
    FC_BARREL_MED_3 = '1177104896.0dxschafe'
    FC_BARREL_MED_4 = '1175826048.0dxschafe'
    FC_MED_BARRELS = 'FortCharlesMedBarrels'
    FC_BARRELS = 'FortCharlesBarrels'
    FC_CRATE_EASY_1 = '1177108096.0dxschafe'
    FC_CRATE_EASY_2 = '1177366400.0dxschafe'
    FC_EASY_CRATES = 'FortCharlesEasyCrates'
    FC_CRATE_MED_1 = '1176414464.0dxschafe'
    FC_CRATE_MED_2 = '1176414336.0dxschafe0'
    FC_CRATE_MED_3 = '1176414976.0dxschafe0'
    FC_CRATE_MED_4 = '1177352320.0dxschafe'
    FC_CRATE_MED_5 = '1177108224.0dxschafe'
    FC_MED_CRATES = 'FortCharlesMedCrates'
    FC_CRATES = 'FortCharlesCrates'
    BOWDASH_CABINET = '1173148032.0mike'
    T_CRATE_1 = '1173148288.0mike'
    T_CRATE_2 = '1173148416.0mike'
    T_CRATE_3 = '1173148416.0mike0'
    T_ANY_CRATE = 'TAnyCrate'
    T_EITC_DESK = '1186512896.0dxschafe'
    T_OUTPOST_DESK = '1187057664.0dxschafe'
    T_BOATSWAIN_DESK = '1175037824.0dxschafe'
    FD_SHELF = '1175823104.0dxschafe'
    FD_CABINET = '1175823104.0dxschafe0'
    FD_DESK = '1175822976.0dxschafe'
    FD_FURNITURE = 'FortDundeeFurniture'
    FD_BARREL_EASY_1 = '1177541760.0dxschafe'
    FD_BARREL_EASY_2 = '1177539968.0dxschafe'
    FD_BARREL_EASY_3 = '1177540992.0dxschafe'
    FD_BARREL_EASY_4 = '1177541888.0dxschafe'
    FD_BARREL_EASY_5 = '1177541120.0dxschafe'
    FD_BARREL_EASY_6 = '1177540096.0dxschafe0'
    FD_EASY_BARRELS = 'FortDundeeEasyBarrels'
    FD_BARREL_MED_1 = '1177541248.0dxschafe1'
    FD_BARREL_MED_2 = '1177541632.0dxschafe0'
    FD_BARREL_MED_3 = '1175824768.0dxschafe1'
    FD_BARREL_MED_4 = '1177540864.0dxschafe1'
    FD_MED_BARRELS = 'FortDundeeMedBarrels'
    FD_BARRELS = 'FortDundeeBarrels'
    FD_CRATE_EASY_1 = '1177540096.0dxschafe'
    FD_EASY_CRATES = 'FortDundeeEasyCrates'
    FD_CRATE_MED_1 = '1177541248.0dxschafe2'
    FD_CRATE_MED_2 = '1177541248.0dxschafe0'
    FD_CRATE_MED_3 = '1175824768.0dxschafe0'
    FD_CRATE_MED_4 = '1177541632.0dxschafe'
    FD_CRATE_MED_5 = '1177540224.0dxschafe'
    FD_MED_CRATES = 'FortDundeeMedCrates'
    FD_CRATES = 'FortDundeeCrates'
    FD_ALL = 'AllFortDundeeCratesBarrels'
    KH_CRATE_1 = '1177716480.0dxschafe6'
    KH_CRATE_2 = '1177717248.0dxschafe2'
    KH_CRATE_3 = '1177716480.0dxschafe10'
    KH_CRATE_4 = '1177715584.0dxschafe5'
    KH_CRATE_5 = '1177716480.0dxschafe5'
    KH_CRATE_6 = '1177717504.0dxschafe1'
    KH_CRATE_7 = '1177716480.0dxschafe8'
    KH_CRATE_8 = '1177717248.0dxschafe4'
    KH_CRATE_9 = '1177970176.0dxschafe'
    KH_CRATE_10 = '1177716480.0dxschafe11'
    KH_CRATE_11 = '1177716480.0dxschafe2'
    KH_CRATE_12 = '1177716864.0dxschafe'
    KH_CRATE_13 = '1177716480.0dxschafe'
    KH_CRATE_14 = '1177716480.0dxschafe3'
    KH_CRATE_15 = '1177716480.0dxschafe9'
    KH_CRATE_16 = '1177715584.0dxschafe3'
    KH_CRATE_17 = '1177716864.0dxschafe2'
    KH_CRATE_18 = '1177717248.0dxschafe1'
    KH_CRATE_19 = '1177717248.0dxschafe3'
    KH_CRATE_20 = '1177716480.0dxschafe1'
    KH_CRATE_21 = '1177717120.0dxschafe0'
    KH_CRATE_22 = '1177716480.0dxschafe4'
    KH_CRATE_23 = '1177715584.0dxschafe9'
    KH_CRATE_24 = '1177716480.0dxschafe0'
    KH_CRATE_25 = '1177716864.0dxschafe0'
    KH_CRATE_26 = '1176849536.0dxschafe'
    KH_CRATE_27 = '1177717248.0dxschafe'
    KH_CRATE_28 = '1177717248.0dxschafe0'
    KH_CRATE_29 = '1177716992.0dxschafe1'
    KH_CRATE_30 = '1177717120.0dxschafe'
    KH_CRATE_31 = '1177717504.0dxschafe0'
    KH_CRATE_32 = '1177715584.0dxschafe7'
    KH_CRATE_33 = '1177716480.0dxschafe7'
    KH_CRATE_34 = '1177716864.0dxschafe1'
    KH_CRATE_35 = '1177715584.0dxschafe8'
    KH_CRATE_36 = '1177715584.0dxschafe2'
    KH_CRATE_37 = '1177716992.0dxschafe0'
    KH_CRATE_38 = '1177716992.0dxschafe'
    KH_CRATES = 'KingsheadCrates'
    KH_BARREL_1 = '1177717248.0dxschafe6'
    KH_BARREL_2 = '1177715584.0dxschafe'
    KH_BARREL_3 = '1177715328.0dxschafe9'
    KH_BARREL_4 = '1177715584.0dxschafe11'
    KH_BARREL_5 = '1177715712.0dxschafe4'
    KH_BARREL_6 = '1177715712.0dxschafe1'
    KH_BARREL_7 = '1177715584.0dxschafe1'
    KH_BARREL_8 = '1177715712.0dxschafe3'
    KH_BARREL_9 = '1177715584.0dxschafe6'
    KH_BARREL_10 = '1177717248.0dxschafe8'
    KH_BARREL_11 = '1177715584.0dxschafe10'
    KH_BARREL_12 = '1177714048.0dxschafe'
    KH_BARREL_13 = '1177715328.0dxschafe6'
    KH_BARREL_14 = '1177717248.0dxschafe12'
    KH_BARREL_15 = '1177715200.0dxschafe'
    KH_BARREL_16 = '1177717248.0dxschafe5'
    KH_BARREL_17 = '1177717248.0dxschafe10'
    KH_BARREL_18 = '1177713792.0dxschafe0'
    KH_BARREL_19 = '1177717248.0dxschafe14'
    KH_BARREL_20 = '1177717504.0dxschafe'
    KH_BARREL_21 = '1177715584.0dxschafe4'
    KH_BARREL_22 = '1177715328.0dxschafe5'
    KH_BARREL_23 = '1177715328.0dxschafe2'
    KH_BARREL_24 = '1177717248.0dxschafe9'
    KH_BARREL_25 = '1177715328.0dxschafe8'
    KH_BARREL_26 = '1177715328.0dxschafe0'
    KH_BARREL_27 = '1177717248.0dxschafe11'
    KH_BARREL_28 = '1177713792.0dxschafe'
    KH_BARREL_29 = '1177715712.0dxschafe0'
    KH_BARREL_30 = '1177717248.0dxschafe7'
    KH_BARREL_31 = '1177715328.0dxschafe7'
    KH_BARREL_32 = '1177715712.0dxschafe'
    KH_BARREL_33 = '1177715584.0dxschafe0'
    KH_BARREL_34 = '1177715328.0dxschafe1'
    KH_BARREL_35 = '1177715328.0dxschafe3'
    KH_BARREL_36 = '1177713664.0dxschafe0'
    KH_BARREL_37 = '1177713664.0dxschafe2'
    KH_BARREL_38 = '1177717248.0dxschafe13'
    KH_BARREL_39 = '1177715712.0dxschafe2'
    KH_BARREL_40 = '1177715328.0dxschafe4'
    KH_BARREL_41 = '1177713664.0dxschafe'
    KH_BARREL_42 = '1177713664.0dxschafe1'
    KH_BARRELS = 'KingsheadBarrels'
    KH_HAYSTACK_1 = '1176845824.0dxschafe3'
    KH_HAYSTACK_2 = '1176845696.0dxschafe'
    KH_HAYSTACK_3 = '1176845568.0dxschafe'
    KH_HAYSTACKS = 'KingsheadHaystacks'
    KH_WELL_1 = '1176846464.0dxschafe'
    KH_WELL_2 = '1176849152.0dxschafe'
    KH_WELLS = 'KingsheadWells'
    NAVY_BARRELS = 'NavyBarrels'
    NAVY_CRATES = 'NavyCrates'
    VEGAS_GOV_DESK = '1169451658.54Shochet'
    ANY_PROP = 'AnyProp'
    PropDefs = {
        VEGAS_GOV_DESK: (VEGAS_GOV_DESK,),
        PR_CRATES:
        (PR_CRATE_1, PR_CRATE_2, PR_CRATE_3, PR_CRATE_4, PR_CRATE_5, PR_CRATE_6,
         PR_CRATE_7, PR_CRATE_8, PR_CRATE_9, PR_CRATE_10, PR_CRATE_11,
         PR_CRATE_12, PR_CRATE_13, PR_CRATE_14, PR_CRATE_15),
        FC_DESK: (FC_DESK,),
        FC_SHELF: (FC_SHELF,),
        FC_CLOCK: (FC_CLOCK,),
        FC_EASY_BARRELS: (FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3,
                          FC_BARREL_EASY_4),
        FC_MED_BARRELS: (FC_BARREL_MED_1, FC_BARREL_MED_2, FC_BARREL_MED_3,
                         FC_BARREL_MED_4),
        FC_BARRELS: (FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3,
                     FC_BARREL_EASY_4, FC_BARREL_MED_1, FC_BARREL_MED_2,
                     FC_BARREL_MED_3, FC_BARREL_MED_4),
        FC_EASY_CRATES: (FC_CRATE_EASY_1, FC_CRATE_EASY_2),
        FC_MED_CRATES: (FC_CRATE_MED_1, FC_CRATE_MED_2, FC_CRATE_MED_3,
                        FC_CRATE_MED_4, FC_CRATE_MED_5),
        FC_CRATES: (FC_CRATE_EASY_1, FC_CRATE_EASY_2, FC_CRATE_MED_1,
                    FC_CRATE_MED_2, FC_CRATE_MED_3, FC_CRATE_MED_4,
                    FC_CRATE_MED_5),
        BOWDASH_CABINET: (BOWDASH_CABINET,),
        T_ANY_CRATE: (T_CRATE_1, T_CRATE_2, T_CRATE_3),
        T_EITC_DESK: (T_EITC_DESK,),
        T_OUTPOST_DESK: (T_OUTPOST_DESK,),
        FD_SHELF: (FD_SHELF,),
        FD_CABINET: (FD_CABINET,),
        FD_DESK: (FD_DESK,),
        FD_FURNITURE: (FD_SHELF, FD_CABINET, FD_DESK),
        FD_EASY_BARRELS: (FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3,
                          FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6),
        FD_MED_BARRELS: (FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3,
                         FD_BARREL_MED_4),
        FD_BARRELS:
        (FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4,
         FD_BARREL_EASY_5, FD_BARREL_EASY_6, FD_BARREL_MED_1, FD_BARREL_MED_2,
         FD_BARREL_MED_3, FD_BARREL_MED_4),
        FD_EASY_CRATES: (FD_CRATE_EASY_1,),
        FD_MED_CRATES: (FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3,
                        FD_CRATE_MED_4, FD_CRATE_MED_5),
        FD_CRATES: (FD_CRATE_EASY_1, FD_CRATE_MED_1, FD_CRATE_MED_2,
                    FD_CRATE_MED_3, FD_CRATE_MED_4, FD_CRATE_MED_5),
        FD_ALL:
        (FD_CRATE_EASY_1, FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3,
         FD_CRATE_MED_4, FD_CRATE_MED_5, FD_BARREL_EASY_1, FD_BARREL_EASY_2,
         FD_BARREL_EASY_3, FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6,
         FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3, FD_BARREL_MED_4),
        KH_CRATES:
        (KH_CRATE_1, KH_CRATE_2, KH_CRATE_3, KH_CRATE_4, KH_CRATE_5, KH_CRATE_6,
         KH_CRATE_7, KH_CRATE_8, KH_CRATE_9, KH_CRATE_10, KH_CRATE_11,
         KH_CRATE_12, KH_CRATE_13, KH_CRATE_14, KH_CRATE_15, KH_CRATE_16,
         KH_CRATE_17, KH_CRATE_18, KH_CRATE_19, KH_CRATE_20, KH_CRATE_21,
         KH_CRATE_22, KH_CRATE_23, KH_CRATE_24, KH_CRATE_25, KH_CRATE_26,
         KH_CRATE_27, KH_CRATE_28, KH_CRATE_29, KH_CRATE_30, KH_CRATE_31,
         KH_CRATE_32, KH_CRATE_33, KH_CRATE_34, KH_CRATE_35, KH_CRATE_36,
         KH_CRATE_37, KH_CRATE_38),
        KH_BARRELS:
        (KH_BARREL_1, KH_BARREL_2, KH_BARREL_3, KH_BARREL_4, KH_BARREL_5,
         KH_BARREL_6, KH_BARREL_7, KH_BARREL_8, KH_BARREL_9, KH_BARREL_10,
         KH_BARREL_11, KH_BARREL_12, KH_BARREL_13, KH_BARREL_14, KH_BARREL_15,
         KH_BARREL_16, KH_BARREL_17, KH_BARREL_18, KH_BARREL_19, KH_BARREL_20,
         KH_BARREL_21, KH_BARREL_22, KH_BARREL_23, KH_BARREL_24, KH_BARREL_25,
         KH_BARREL_26, KH_BARREL_27, KH_BARREL_28, KH_BARREL_29, KH_BARREL_30,
         KH_BARREL_31, KH_BARREL_32, KH_BARREL_33, KH_BARREL_34, KH_BARREL_35,
         KH_BARREL_36, KH_BARREL_37, KH_BARREL_38, KH_BARREL_39, KH_BARREL_40,
         KH_BARREL_41, KH_BARREL_42),
        KH_HAYSTACKS: (KH_HAYSTACK_1, KH_HAYSTACK_2, KH_HAYSTACK_3),
        KH_WELLS: (KH_WELL_1, KH_WELL_2),
        NAVY_BARRELS:
        (FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3, FC_BARREL_EASY_4,
         FC_BARREL_MED_1, FC_BARREL_MED_2, FC_BARREL_MED_3, FC_BARREL_MED_4,
         FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4,
         FD_BARREL_EASY_5, FD_BARREL_EASY_6, FD_BARREL_MED_1, FD_BARREL_MED_2,
         FD_BARREL_MED_3, FD_BARREL_MED_4, KH_BARREL_1, KH_BARREL_2,
         KH_BARREL_3, KH_BARREL_4, KH_BARREL_5, KH_BARREL_6, KH_BARREL_7,
         KH_BARREL_8, KH_BARREL_9, KH_BARREL_10, KH_BARREL_11, KH_BARREL_12,
         KH_BARREL_13, KH_BARREL_14, KH_BARREL_15, KH_BARREL_16, KH_BARREL_17,
         KH_BARREL_18, KH_BARREL_19, KH_BARREL_20, KH_BARREL_21, KH_BARREL_22,
         KH_BARREL_23, KH_BARREL_24, KH_BARREL_25, KH_BARREL_26, KH_BARREL_27,
         KH_BARREL_28, KH_BARREL_29, KH_BARREL_30, KH_BARREL_31, KH_BARREL_32,
         KH_BARREL_33, KH_BARREL_34, KH_BARREL_35, KH_BARREL_36, KH_BARREL_37,
         KH_BARREL_38, KH_BARREL_39, KH_BARREL_40, KH_BARREL_41, KH_BARREL_42),
        NAVY_CRATES:
        (FC_CRATE_EASY_1, FC_CRATE_EASY_2, FC_CRATE_MED_1, FC_CRATE_MED_2,
         FC_CRATE_MED_3, FC_CRATE_MED_4, FC_CRATE_MED_5, FD_CRATE_EASY_1,
         FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3, FD_CRATE_MED_4,
         FD_CRATE_MED_5, KH_CRATE_1, KH_CRATE_2, KH_CRATE_3, KH_CRATE_4,
         KH_CRATE_5, KH_CRATE_6, KH_CRATE_7, KH_CRATE_8, KH_CRATE_9,
         KH_CRATE_10, KH_CRATE_11, KH_CRATE_12, KH_CRATE_13, KH_CRATE_14,
         KH_CRATE_15, KH_CRATE_16, KH_CRATE_17, KH_CRATE_18, KH_CRATE_19,
         KH_CRATE_20, KH_CRATE_21, KH_CRATE_22, KH_CRATE_23, KH_CRATE_24,
         KH_CRATE_25, KH_CRATE_26, KH_CRATE_27, KH_CRATE_28, KH_CRATE_29,
         KH_CRATE_30, KH_CRATE_31, KH_CRATE_32, KH_CRATE_33, KH_CRATE_34,
         KH_CRATE_35, KH_CRATE_36, KH_CRATE_37, KH_CRATE_38),
        ANY_PROP:
        None
    }


def getPropList(propId):
    return PropIds.PropDefs.get(propId)


class TreasureIds:

    PR_CHEST_1 = '1165018378.63Shochet'
    PR_CHEST_2 = '1165018628.69Shochet'
    PR_CHEST_3 = '1165018665.78Shochet'
    PR_CHEST_4 = '1165018696.72Shochet'
    PR_CHEST_5 = '1165018724.53Shochet'
    PR_CHEST_6 = '1165018774.94Shochet'
    PR_CHEST_7 = '1165018816.39Shochet'
    PR_CHESTS = 'PortRoyalChests'
    PR_ROYAL_CAVERNS_CHEST_1 = '1165019105.05Shochet'
    PR_ROYAL_CAVERNS_CHEST_2 = '1165019132.53Shochet'
    PR_ROYAL_CAVERNS_CHEST_3 = '1165019166.08Shochet'
    PR_ROYAL_CAVERNS_CHEST_4 = '1175898752.0dxschafe0'
    PR_ROYAL_CAVERNS_CHEST_5 = '1190851456.0dxschafe'
    PR_ROYAL_CAVERNS_CHESTS = 'PortRoyalRoyalCavernsChests'
    PR_GOVERNOR_G_CHEST_1 = '1176150912.0dxschafe'
    PR_GOVERNOR_G_CHEST_2 = '1176151040.0dxschafe'
    PR_GOVERNOR_G_CHEST_3 = '1176151040.0dxschafe0'
    PR_GOVERNOR_G_CHEST_4 = '1176151040.0dxschafe1'
    PR_GOVERNOR_G_CHEST_5 = '1176151168.0dxschafe0'
    PR_GOVERNOR_G_CHEST_6 = '1176151296.0dxschafe'
    PR_GOVERNOR_G_CHEST_7 = '1176151424.0dxschafe'
    PR_GOVERNOR_G_CHESTS = 'PortRoyalGovernorGardenChests'
    CUTTS_TREASURE = '1178300160.0dxschafe'
    SCORPION_TREASURE = '1177007104.0dxschafe'
    FLYTRAP_TREASURE = '1177021184.0dxschafe'
    T_CHEST_5 = '1165199625.3Shochet'
    T_CHEST_6 = '1165199876.28Shochet'
    T_CHEST_7 = '1165199908.11Shochet'
    T_CHEST_8 = '1189564672.0dxschafe'
    T_CHEST_9 = '1165200029.95Shochet'
    T_CHEST_10 = '1175102976.0dxschafe'
    T_CHESTS = 'TortugaChests'
    T_W_CHEST_1 = '1165201347.11Shochet'
    T_W_CHEST_2 = '1165201844.27Shochet'
    T_W_CHEST_3 = '1165205254.09Shochet'
    T_W_CHEST_4 = '1177007104.0dxschafe'
    T_W_CHESTS = 'TortugaWildwoodChests'
    DW_CHEST_1 = '1175533440.0dxschafe'
    DW_CHEST_2 = '1175533440.0dxschafe0'
    DW_CHEST_3 = '1213740055.14WDIG'
    DW_CHEST_4 = '1213740088.81WDIG'
    DW_CHEST_5 = '1213740104.3WDIG'
    DW_CHEST_6 = '1213740118.8WDIG'
    DW_CHEST_7 = '1213740163.47WDIG'
    DW_CHEST_8 = '1213740183.83WDIG'
    DW_CHEST_9 = '1213740223.27WDIG'
    DW_CHEST_10 = '1213740249.55WDIG'
    DW_CHESTS = 'DriftwoodIslandChests'
    DF_CHEST_1 = '1176229632.0dxschafe'
    DF_CHEST_2 = '1176235904.0dxschafe'
    DF_CHEST_3 = '1176229120.0dxschafe1'
    DF_CHEST_4 = '1176229120.0dxschafe2'
    DF_CHESTS = 'DelFuegoChests'
    DF_CHEST_CAVE_D_1 = '1175816960.0dxschafe'
    DF_CHEST_CAVE_D_2 = '1176249984.0dxschafe'
    DF_CHEST_CAVE_D_3 = '1176249984.0dxschafe0'
    DF_CHEST_CAVE_D_4 = '1176249984.0dxschafe1'
    DF_CHEST_CAVE_D_5 = '1176249984.0dxschafe2'
    DF_CHEST_CAVE_D_6 = '1176322048.0dxschafe'
    DF_CHEST_CAVE_D_7 = '1176322048.0dxschafe0'
    DF_CHEST_CAVE_D = 'DelFuegoCaveDChests'
    KH_CHEST_1 = '1176845952.0dxschafe0'
    KH_CHEST_2 = '1176856832.0dxschafe'
    KH_CHEST_3 = '1176846080.0dxschafe'
    KH_CHESTS = 'KingsheadChests'
    RR_CHEST_1 = '1182807552.0dxschafe0'
    RR_CHEST_2 = '1182807424.0dxschafe'
    RR_CHEST_3 = '1182807552.0dxschafe2'
    RR_CHEST_4 = '1182807552.0dxschafe'
    RR_CHESTS = 'Rumrunner Isle Chests'
    IC_CHEST_1 = '1175105408.0dxschafe'
    IC_CHEST_2 = '1175041664.0dxschafe'
    IC_CHEST_3 = '1175041664.0dxschafe0'
    IC_CHEST_4 = '1175041664.0dxschafe1'
    IC_CHEST_5 = '1175041664.0dxschafe2'
    IC_CHEST_6 = '1175041664.0dxschafe3'
    IC_CHEST_7 = '1175041664.0dxschafe4'
    IC_CHEST_8 = '1175041664.0dxschafe5'
    IC_CHEST_9 = '1175041664.0dxschafe6'
    IC_CHEST_10 = '1175041664.0dxschafe7'
    IC_CHEST_11 = '1210112896.0WDIG'
    IC_CHESTS = 'IslaCangrejosChests'
    IP_CHEST_1 = '1175021696.0dxschafe0'
    IP_WASP_TREASURE = '1186713984.0dxschafe'
    TO_DJ_TREASURE = '1186714240.0dxschafe0'
    CT_CHEST_1 = '1210109440.0WDIG'
    OI_DJ_TREASURE = '1186714240.0dxschafe0'
    ANY_TREASURE = 'AnyTreasure'
    TreasureDefs = {
        PR_CHEST_1: (PR_CHEST_1,),
        PR_CHEST_2: (PR_CHEST_2,),
        PR_CHEST_3: (PR_CHEST_3,),
        PR_CHEST_4: (PR_CHEST_4,),
        PR_CHEST_5: (PR_CHEST_5,),
        PR_CHEST_6: (PR_CHEST_6,),
        PR_CHEST_7: (PR_CHEST_7,),
        PR_CHESTS: (PR_CHEST_1, PR_CHEST_2, PR_CHEST_3, PR_CHEST_4, PR_CHEST_5,
                    PR_CHEST_6, PR_CHEST_7),
        PR_ROYAL_CAVERNS_CHEST_1: (PR_ROYAL_CAVERNS_CHEST_1,),
        PR_ROYAL_CAVERNS_CHEST_2: (PR_ROYAL_CAVERNS_CHEST_2,),
        PR_ROYAL_CAVERNS_CHEST_3: (PR_ROYAL_CAVERNS_CHEST_3,),
        PR_ROYAL_CAVERNS_CHEST_4: (PR_ROYAL_CAVERNS_CHEST_4,),
        PR_ROYAL_CAVERNS_CHEST_5: (PR_ROYAL_CAVERNS_CHEST_5,),
        PR_ROYAL_CAVERNS_CHESTS:
        (PR_ROYAL_CAVERNS_CHEST_1, PR_ROYAL_CAVERNS_CHEST_2,
         PR_ROYAL_CAVERNS_CHEST_3, PR_ROYAL_CAVERNS_CHEST_4,
         PR_ROYAL_CAVERNS_CHEST_5),
        PR_GOVERNOR_G_CHEST_1: (PR_GOVERNOR_G_CHEST_1,),
        PR_GOVERNOR_G_CHEST_2: (PR_GOVERNOR_G_CHEST_2,),
        PR_GOVERNOR_G_CHEST_3: (PR_GOVERNOR_G_CHEST_3,),
        PR_GOVERNOR_G_CHEST_4: (PR_GOVERNOR_G_CHEST_4,),
        PR_GOVERNOR_G_CHEST_5: (PR_GOVERNOR_G_CHEST_5,),
        PR_GOVERNOR_G_CHEST_6: (PR_GOVERNOR_G_CHEST_6,),
        PR_GOVERNOR_G_CHEST_7: (PR_GOVERNOR_G_CHEST_7,),
        PR_GOVERNOR_G_CHESTS:
        (PR_GOVERNOR_G_CHEST_1, PR_GOVERNOR_G_CHEST_2, PR_GOVERNOR_G_CHEST_3,
         PR_GOVERNOR_G_CHEST_4, PR_GOVERNOR_G_CHEST_5, PR_GOVERNOR_G_CHEST_6,
         PR_GOVERNOR_G_CHEST_7),
        CUTTS_TREASURE: (CUTTS_TREASURE,),
        SCORPION_TREASURE: (SCORPION_TREASURE,),
        FLYTRAP_TREASURE: (FLYTRAP_TREASURE,),
        T_CHEST_5: (T_CHEST_5,),
        T_CHEST_6: (T_CHEST_6,),
        T_CHEST_7: (T_CHEST_7,),
        T_CHEST_8: (T_CHEST_8,),
        T_CHEST_9: (T_CHEST_9,),
        T_CHEST_10: (T_CHEST_10,),
        T_CHESTS: (T_CHEST_5, T_CHEST_6, T_CHEST_7, T_CHEST_8, T_CHEST_9,
                   T_CHEST_10),
        T_W_CHESTS: (T_W_CHEST_1, T_W_CHEST_2, T_W_CHEST_3, T_W_CHEST_4),
        DF_CHEST_1: (DF_CHEST_1,),
        DF_CHEST_2: (DF_CHEST_2,),
        DF_CHEST_3: (DF_CHEST_3,),
        DF_CHEST_4: (DF_CHEST_4,),
        DF_CHESTS: (DF_CHEST_1, DF_CHEST_2, DF_CHEST_3, DF_CHEST_4),
        DF_CHEST_CAVE_D_1: (DF_CHEST_CAVE_D_1,),
        DF_CHEST_CAVE_D_2: (DF_CHEST_CAVE_D_2,),
        DF_CHEST_CAVE_D_3: (DF_CHEST_CAVE_D_3,),
        DF_CHEST_CAVE_D_4: (DF_CHEST_CAVE_D_4,),
        DF_CHEST_CAVE_D_5: (DF_CHEST_CAVE_D_5,),
        DF_CHEST_CAVE_D_6: (DF_CHEST_CAVE_D_6,),
        DF_CHEST_CAVE_D_7: (DF_CHEST_CAVE_D_7,),
        DF_CHEST_CAVE_D: (DF_CHEST_CAVE_D_1, DF_CHEST_CAVE_D_2,
                          DF_CHEST_CAVE_D_3, DF_CHEST_CAVE_D_4,
                          DF_CHEST_CAVE_D_5, DF_CHEST_CAVE_D_6,
                          DF_CHEST_CAVE_D_7),
        KH_CHESTS: (KH_CHEST_1, KH_CHEST_2, KH_CHEST_3),
        KH_CHEST_1: (KH_CHEST_1,),
        KH_CHEST_2: (KH_CHEST_2,),
        KH_CHEST_3: (KH_CHEST_3,),
        RR_CHEST_1: (RR_CHEST_1,),
        RR_CHESTS: (RR_CHEST_1, RR_CHEST_2, RR_CHEST_3, RR_CHEST_4),
        CT_CHEST_1: (CT_CHEST_1,),
        DW_CHESTS: (DW_CHEST_1, DW_CHEST_2, DW_CHEST_3, DW_CHEST_4, DW_CHEST_5,
                    DW_CHEST_6, DW_CHEST_7, DW_CHEST_8, DW_CHEST_9,
                    DW_CHEST_10),
        IC_CHEST_1: (IC_CHEST_1,),
        IC_CHEST_9: (IC_CHEST_9,),
        IC_CHEST_11: (IC_CHEST_11,),
        IC_CHESTS: (IC_CHEST_1, IC_CHEST_2, IC_CHEST_3, IC_CHEST_4, IC_CHEST_5,
                    IC_CHEST_6, IC_CHEST_7, IC_CHEST_8, IC_CHEST_9,
                    IC_CHEST_10),
        IP_CHEST_1: (IP_CHEST_1,),
        IP_WASP_TREASURE: (IP_WASP_TREASURE,),
        OI_DJ_TREASURE: (OI_DJ_TREASURE,),
        ANY_TREASURE:
        None
    }


def getTreasureList(treasureId):
    return TreasureIds.TreasureDefs.get(treasureId)


class ShipIds:

    ANY_LARGE_SHIP = 'AnyLargeShip'
    ANY_WARSHIP = 'AnyWarShip'
    ANY_EITC_CORVETTE = 'AnyEITCCorvette'
    ANY_EITC_SEA_VIPER = 'AnyEITCSeaViper'
    ANY_EITC_MARAUDER = 'AnyEITCMarauder'
    ANY_EITC_BARRACUDA = 'AnyEITCBarracuda'
    ANY_FRENCH_SHADOW_CROW = 'AnyFrenchShadowCrow'
    ANY_FRENCH_HELLHOUND = 'AnyFrenchHellhound'
    ANY_FRENCH_BLOOD_SCOURGE = 'AnyFrenchBloodScourge'
    ANY_SPANISH_SHADOW_CROW = 'AnySpanishShadowCrow'
    ANY_SPANISH_HELLHOUND = 'AnySpanishHellhound'
    ANY_SPANISH_BLOOD_SCOURGE = 'AnySpanishBloodScourge'
    ShipDefs = {
        INTERCEPTORL1: (NAVY_FERRET, EITC_SEA_VIPER),
        INTERCEPTORL2: (NAVY_GREYHOUND, EITC_BLOODHOUND),
        INTERCEPTORL3: (NAVY_KINGFISHER, EITC_BARRACUDA),
        INTERCEPTORL4: (NAVY_PREDATOR, EITC_CORSAIR),
        MERCHANTL1: (NAVY_BULWARK, EITC_SENTINEL),
        MERCHANTL2: (NAVY_VANGUARD, EITC_IRONWALL),
        MERCHANTL3: (NAVY_MONARCH, EITC_OGRE),
        MERCHANTL4: (NAVY_COLOSSUS, EITC_BEHEMOTH),
        WARSHIPL1: (NAVY_PANTHER, EITC_CORVETTE),
        WARSHIPL2: (NAVY_CENTURION, EITC_MARAUDER),
        WARSHIPL3: (NAVY_MAN_O_WAR, EITC_WARLORD),
        WARSHIPL4: (NAVY_DREADNOUGHT, EITC_JUGGERNAUT),
        ANY_LARGE_SHIP:
        (NAVY_BULWARK, EITC_SENTINEL, NAVY_VANGUARD, EITC_IRONWALL,
         NAVY_MONARCH, EITC_OGRE, NAVY_COLOSSUS, EITC_BEHEMOTH, NAVY_PANTHER,
         EITC_CORVETTE, NAVY_CENTURION, EITC_MARAUDER, NAVY_MAN_O_WAR,
         EITC_WARLORD, NAVY_DREADNOUGHT, EITC_JUGGERNAUT),
        ANY_WARSHIP: (NAVY_PANTHER, EITC_CORVETTE, NAVY_CENTURION,
                      EITC_MARAUDER, NAVY_MAN_O_WAR, EITC_WARLORD,
                      NAVY_DREADNOUGHT, EITC_JUGGERNAUT),
        ANY_EITC_CORVETTE: (EITC_CORVETTE,),
        ANY_EITC_SEA_VIPER: (EITC_SEA_VIPER,),
        ANY_EITC_MARAUDER: (EITC_MARAUDER,),
        ANY_EITC_BARRACUDA: (EITC_BARRACUDA,),
        ANY_FRENCH_SHADOW_CROW: (SKEL_SHADOW_CROW_FR,),
        ANY_FRENCH_HELLHOUND: (SKEL_HELLHOUND_FR,),
        ANY_FRENCH_BLOOD_SCOURGE: (SKEL_BLOOD_SCOURGE_FR,),
        ANY_SPANISH_SHADOW_CROW: (SKEL_SHADOW_CROW_SP,),
        ANY_SPANISH_HELLHOUND: (SKEL_HELLHOUND_SP,),
        ANY_SPANISH_BLOOD_SCOURGE: (SKEL_BLOOD_SCOURGE_SP,)
    }


def getShipList(shipId):
    return ShipIds.ShipDefs.get(shipId)


class NPCIds:

    DOGGEREL_DAN = '1154731709.64jubutler'
    WILL_TURNER = '1152830677.95jubutler'
    TIA_DALMA_PR = '1154497344.0jubutlerPR'
    ELIZABETH = '1171325040.86MAsaduzz'
    DARBY_DRYDOCK = '1156986248.77jasyeung'
    GRAHAM_MARSH = '1169083104.56sdnaik'
    JEWELER_SMITTY = '1169151219.8mike'
    R_SMITH_PEWTERER = '1157094552.02jasyeung'
    HARBORMASTER = '1156986071.78jasyeung'
    DOCKWORKER_FITZ = '1168748251.22joswilso'
    PICKERT = '1174345216.0dxschafe'
    CASSANDRA = '1175554816.0dxschafe'
    LUCINDA = '1175553664.0dxschafe'
    DAISY = '1175635584.0dxschafe'
    GORDON_GREER = '1169190957.44mike'
    BINGHAM = '1169060460.13mike'
    BLAKELEY = '1169075008.52mike'
    JUNE = '1169075683.22mike'
    EWAN = '1169079172.34sdnaik'
    BARTHOLOMEW_WATKINS = '1157048353.58jasyeung'
    JOSIE_MCKEEDY = '1178234368.0dchiappe1'
    JOSIE_MCREEDY = '1178234368.0dchiappe1'
    SAM_SEABONES = '1154574164.57jubutler'
    PETER_CHIPPARR = '1178654720.0dchiappe'
    SHANE_MCGREENY = '1187219584.0dxschafe0'
    JIM_WAVEMONGER = '1185832192.0dxschafe1'
    SOLOMON_ODOUGAL = '1201028352.0dxschafe'
    WILLIAM_TURK = '1175792768.0dxschafe'
    SARAH = '1201109074.66dxschafe'
    EDWARD_SHACKLEBY = '1181263360.0dxschafe'
    EDWARD_STORMHAWK = '1156986020.6jasyeung'
    JOHN_WALLACE = '1181171584.0dxschafe0'
    JACK_ROWDY_ROOSTER = '1209749843.55dxschafe'
    NATHANIEL_TRUEHOUND = '1196896512.0dxschafe'
    CAPTAIN_JOB = '1180720000.0dchiappe1'
    ENSIGN_GRIMM = '1219895971.52mtucker'
    PHILLIP_FULLER = '1181260288.0dxschafe'
    BARBOSSA = '1172618710.78sdnaik'
    JACK = '1174954368.0jubutler'
    JOSHAMEE = '1168022298.47Shochet'
    NILL_OFFRILL = '1172630144.0mike'
    CARVER = '1168022348.66Shochet'
    HENDRY_CUTTS = '1169071109.22mike'
    GILADOGA = '1172887552.0mike0'
    DOC_GROG = '1169068641.66mike'
    LE_CERDO = '1169078025.53mike'
    ORINDA = '1169063296.16mike'
    MALLET = '1172276608.0mike'
    BENEDEK = '1169070429.72mike'
    BOWDASH = '1169075474.72mike'
    SCARLET = '1168052247.45mike'
    FABIOLA = '1165199931.31Shochet'
    TOMAS = '1169076564.88mike'
    BUTCHER_BROWN = '1169076109.16mike'
    BEN_FLATTS = '1169076368.97mike'
    BONITA = '1169067906.19mike'
    MILLIE = '1169077360.47mike'
    BLACKSMITH_FLINTY = '1169075869.81mike'
    O_MALLEY = '1165199819.22Shochet'
    SEAMSTRESS_ANNE = '1169077081.52mike'
    JOHNNY_MCVANE = '1169088062.75mike'
    RETAVICK = '1175650176.0dxschafe'
    SIMON_HORNBOW = '1187306240.0dxschafe'
    DAJIN_MING = '1196907776.0dxschafe0'
    LALA_LOVEL = '1201025280.0dxschafe'
    BUTCHER_BROWN = '1169076109.16mike'
    BOATSWAIN_BILL = '1181593472.0dxschafe'
    BIG_PHIL = '1179961216.0dchiappe'
    SLIM = '1179360256.0dchiappe'
    JACK_REDRAT = '1175800576.0dxschafe'
    ALEXANDER_THAYER = '1181606272.0dxschafe'
    ISAIAH_CALLECUTTER = '1196904064.0dxschafe'
    AMELIA_SUNFELLOW = '1212432000.0WDIG1'
    GUNNER = '1169078705.84mike'
    GARRETT = '1172887552.0mike'
    DUCHAMPS = '1173146624.0mike0'
    MORRIS = '1173147520.0mike'
    ROMANY_BEV = '1157097924.52jasyeung'
    OLIVIER = '1175721216.0dxschafe'
    FERNANDO = '1175733248.0dxschafe'
    PAUPER_PEDRO = '1175730944.0dxschafe'
    RICO = '1175733376.0dxschafe'
    BALTHASAR = '1157097728.52jasyeung'
    VALENTINA = '1177714944.0mike'
    FAKE_VALENTINA = '1111111111.1mwt'
    PERLA_ALODIA = '1201228098.28dxschafe'
    MERCEDES_CORAZON = '1201230131.11dxschafe'
    SHOCHETT_PRYMME = '1157097962.5jasyeung'
    BILLY_MCKIDD = '1190744501.14dxschafe'
    ROLAND_RAGGART = '1207073489.41mtucker'
    ERASMUS_GRIMSDITCH = '1157098075.78jasyeung'
    ADORIA_DOLORES = '1201227181.3dxschafe'
    DELILAH_DUNSMORE = '1219965016.25mtucker'
    MIGUEL_MONTOYA = '1220039541.89mtucker'
    FERRERA = '1157098037.86jasyeung'
    BILLY_MCKIDD = '1190744501.14dxschafe'
    TIA_DALMA = '1154497344.0jubutler'
    MACOMO = '1176186151.42mike'
    CARLOS_CIENFUEGOS = '1189456447.08kmuller'
    BASTIEN_CRAVEN = '1169081738.45mike'
    JOHN_SMITH = '1169094482.66mike'
    BRONZE_JOHN = '1169094669.8mike'
    WOODRUFF = '1175101824.0dxschafe'
    SCARY_MARY = '1170739712.0mike'
    DOG_LOCKGRIM = '1214345458.84WDIG'
    MAGGIE_RIGRAGE = '1214345910.48WDIG'
    CAPTAIN_STEADMAN = '1170739968.0mike'
    ALTHEA = '1174342784.0dxschafe'
    CAPTAIN_BILLINGTON = '1174353792.0dxschafe'
    WALLACE = '1174343680.0dxschafe'
    OHENRY = '1174344320.0dxschafe'
    CAPTAIN_ARCHER = '1174345984.0dxschafe'
    TRENT = '1174351616.0dxschafe'
    CAPTAIN_JONES = '1174351232.0dxschafe'
    ALBERTO = '1174350464.0dxschafe'
    JEHAN_CARROU = '1175118080.0dxschafe'
    PENROD = '1175117568.0dxschafe0'
    COLLIER = '1175119104.0dxschafe1'
    CAPTAIN_BARTS = '1175120896.0dxschafe0'
    CAPTAIN_REGINALD = '1176322304.0mike1'
    CAPTAIN_DENNISON = '1176322432.0mike'
    CAPTAIN_HEDLEY = '1176322432.0mike0'
    CAPTAIN_BIGGLETON = '1176322560.0mike'
    CAPTAIN_NORMAN = '1176322560.0mike0'
    CAPTAIN_FITZPATRICK = '1176322688.0mike'
    CAPTAIN_HAMILTON = '1176322688.0mike0'
    CAPTAIN_MONTROSE = '1176322816.0mike'
    LUTHER = '1176322944.0mike'
    OFFICER_MILLER = '1190420608.0dxschafe1'
    COMMANDER_GENTRY = '1190420736.0dxschafe'
    CAPTAIN_ACKERS = '1219104942.43mtucker'
    CAPTAIN_SWAIN = '1219105162.48mtucker'
    BLACK_MACK = '1176334208.0mike0'
    GARCIA_DE_AVARCIA = '1203449603.97akelts'
    PIERRE_LE_PORC = '1202519757.13akelts'
    SPANISH_SHIPWRIGHT = '1203451028.89akelts'
    GENERAL_BLOODLESS = '1219428571.98mtucker'
    GENERAL_HEX = '1220906480.53mtucker'
    GENERAL_SANDSPINE = '1219434293.16mtucker'
    GENERAL_DARKHART = '1219424341.05mtucker'
    NEBAN_THE_HIRED_GUN = '1219352693.09mtucker'
    REMINGTON_THE_ASSASSIN = '1219367627.94mtucker'
    SAMUEL = '1219339266.79mtucker'
    BONERATTLER = '1219426331.38mtucker'
    UNDEAD_TIMOTHY_DARTAN = '1219425030.24mtucker'
    DREADTOOTH = '1219277508.79mtucker'
    VENOM_LASH = '1218760328.71mtucker'


class Bribes:

    SMALL = 10
    MEDIUM = 50
    LARGE = 100
    HUGE = 500


class PokerPots:

    SMALL = 40
    MEDIUM = 80
    LARGE = 150
    HUGE = 400


class ExpRewards:

    TRIVIAL = 25
    SMALL = 100
    MEDIUM = 500
    LARGE = 1000
    HUGE = 2000


class Probability:

    EXTREMELY_RARE = 0.01
    VERY_RARE = 0.1
    RARE = 0.25
    INFREQUENT = 0.5
    FREQUENT = 0.75
    VERY_FREQUENT = 0.9
    ALWAYS = 1.0


class Attempts:

    VERY_RARE = 16
    RARE = 10
    INFREQUENT = 7
    FREQUENT = 4
    VERY_FREQUENT = 2
    ALWAYS = 1


class DoubleRepTime:

    HALFHOUR = 60 * 30
    HOUR = 60 * 60
    TWOHOUR = 60 * 120
    THREEHOUR = 60 * 180
