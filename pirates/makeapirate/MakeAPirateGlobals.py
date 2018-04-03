# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.makeapirate.MakeAPirateGlobals
BODYSHOP = 0
HEADSHOP = 1
MOUTHSHOP = 2
EYESSHOP = 3
NOSESHOP = 4
EARSHOP = 5
HAIRSHOP = 6
CLOTHESSHOP = 7
NAMESHOP = 8
TATTOOSHOP = 9
JEWELRYSHOP = 10
AVATAR_PIRATE = 0
AVATAR_SKELETON = 1
AVATAR_NAVY = 2
AVATAR_CAST = 3
ShopNames = [
 'BodyShop', 'HeadShop', 'MouthShop', 'EyesShop', 'NoseShop', 'EarShop', 'HairShop', 'ClothesShop', 'NameShop', 'TattooShop', 'JewelryShop']
LODList = [
 2000, 1000, 500]
AnimListA_B = [
 'idle', 'attention', 'axe_chop_idle', 'axe_chop_look_idle', 'bar_talk01_idle', 'bar_talk01_into_look', 'bar_talk01_look_idle', 'bar_talk01_outof_look', 'bar_talk02_idle', 'bar_talk02_into_look', 'bar_talk02_look_idle', 'bar_talk02_outof_look', 'bar_wipe', 'bar_wipe_into_look', 'bar_wipe_look_idle', 'bar_wipe_outof_look', 'bar_write_idle', 'bar_write_into_look', 'bar_write_look_idle', 'bar_write_outof_look', 'barrel_hide_idle', 'barrel_hide_into_look', 'barrel_hide_look_idle', 'barrel_hide_outof_look', 'bayonet_attack_idle', 'bayonet_attack_walk', 'bayonet_attackA', 'bayonet_attackB', 'bayonet_attackC', 'bayonet_drill', 'bayonet_idle', 'bayonet_idle_to_fight_idle', 'bayonet_run', 'bayonet_walk', 'bigbomb_charge', 'bigbomb_charge_loop', 'bigbomb_charge_throw', 'bigbomb_draw', 'bigbomb_idle', 'bigbomb_throw', 'bigbomb_walk', 'bigbomb_walk_left', 'bigbomb_walk_left_diagonal', 'bigbomb_walk_right', 'bigbomb_walk_right_diagonal', 'blacksmith_work_idle', 'blacksmith_work_into_look', 'blacksmith_work_look_idle', 'blacksmith_work_outof_look', 'board', 'bomb_charge', 'bomb_charge_loop', 'bomb_charge_throw', 'bomb_draw', 'bomb_hurt', 'bomb_idle', 'bomb_throw', 'bomb_receive', 'boxing_fromidle', 'boxing_haymaker', 'boxing_hit_head_right', 'boxing_idle', 'boxing_idle_alt', 'boxing_kick', 'boxing_punch']
AnimListC_G = [
 'cards_bad_tell', 'cards_bet', 'cards_blackjack_hit', 'cards_blackjack_stay', 'cards_cheat', 'cards_check', 'cards_good_tell', 'cards_hide', 'cards_hide_hit', 'cards_hide_idle', 'cards_pick_up', 'cards_pick_up_idle', 'cards_set_down', 'cards_set_down_lose', 'cards_set_down_win', 'cards_set_down_win_show', 'chest_idle', 'chest_kneel_to_steal', 'chest_putdown', 'chest_steal', 'chest_strafe_left', 'chest_strafe_right', 'chest_walk', 'chant_a_idle', 'chant_b_idle', 'coin_flip_idle', 'coin_flip_look_idle', 'coin_flip_old_idle', 'crazy_idle', 'crazy_look_idle', 'cutlass_attention', 'cutlass_bladestorm', 'cutlass_combo', 'cutlass_headbutt', 'cutlass_hurt', 'cutlass_kick', 'cutlass_sweep', 'cutlass_taunt', 'cutlass_walk_navy', 'dagger_asp', 'dagger_combo', 'dagger_hurt', 'dagger_receive', 'dagger_throw_sand', 'dagger_vipers_nest', 'deal', 'deal_idle', 'deal_left', 'deal_right', 'death', 'death2', 'death3', 'death4', 'doctor_work_idle', 'doctor_work_into_look', 'doctor_work_look_idle', 'doctor_work_outof_look', 'drink_potion', 'dualcutlass_combo', 'dualcutlass_draw', 'dualcutlass_idle', 'emote_anger', 'emote_celebrate', 'emote_clap', 'emote_coin_toss', 'emote_dance_jig', 'emote_fear', 'emote_flex', 'emote_laugh', 'emote_no', 'emote_sad', 'emote_smile', 'emote_thriller', 'emote_wave', 'emote_wink', 'emote_yawn', 'emote_yes', 'fall_ground', 'flute_idle', 'flute_look_idle', 'foil_coup', 'foil_hack', 'foil_idle', 'foil_slash', 'foil_thrust', 'foil_kick', 'gun_aim_idle', 'gun_draw', 'gun_fire', 'gun_hurt', 'gun_pointedup_idle', 'gun_putaway', 'gun_reload', 'gun_strafe_left']
AnimListI_Si = [
 'idle_B_shiftWeight', 'idle_sit', 'idle_sit_alt', 'idle_flex', 'idle_handhip', 'idle_handhip_from_idle', 'idle_yawn', 'into_deal', 'jail_dropinto', 'jail_idle', 'jail_standup', 'jump', 'jump_idle', 'kick_door', 'kick_door_loop', 'kneel', 'kneel_fromidle', 'knife_throw', 'kraken_struggle_idle', 'kraken_fight_idle', 'left_face', 'loom_idle', 'loom_into_look', 'loom_look_idle', 'loom_outof_look', 'lute_idle', 'lute_into_look', 'lute_look_idle', 'lute_outof_look', 'map_head_into_look_left', 'map_head_look_left_idle', 'map_head_outof_look_left', 'map_look_arm_left', 'map_look_arm_right', 'map_look_boot_left', 'map_look_boot_right', 'map_look_pant_right', 'march', 'patient_work_idle', 'primp_idle', 'primp_into_look', 'primp_look_idle', 'primp_outof_look', 'repairfloor_idle', 'repairfloor_into', 'repairfloor_outof', 'rigging_climb', 'rope_board', 'rope_dismount', 'rope_grab', 'rope_grab_from_idle', 'run', 'run_diagonal_left', 'run_diagonal_right', 'run_with_weapon', 'sand_in_eyes', 'sand_in_eyes_holdweapon_noswing', 'screenshot_pose', 'friend_pose', 'search_low', 'search_med', 'semi_conscious_loop', 'semi_conscious_standup', 'shovel', 'shovel_idle', 'shovel_idle_into_dig', 'sit', 'sit_idle', 'sit_hanginglegs_outof_look', 'sit_hanginglegs_look_idle', 'sit_hanginglegs_into_look', 'sit_hanginglegs_idle', 'sit_sleep_outof_look', 'sit_sleep_look_idle', 'sit_sleep_into_look', 'sit_sleep_idle']
AnimListSl_Sz = [
 'sleep_idle', 'sleep_into_look', 'sleep_outof_look', 'sleep_sick_idle', 'sleep_sick_into_look', 'sleep_sick_look_idle', 'sleep_sick_outof_look', 'sow_idle', 'sow_into_look', 'sow_look_idle', 'sow_outof_look', 'spin_left', 'spin_right', 'stir_idle', 'stir_into_look', 'stir_look_idle', 'stir_outof_look', 'stock_idle', 'stock_sleep', 'stock_sleep_to_idle', 'strafe_left', 'strafe_right', 'summon_idle', 'sweep', 'sweep_idle', 'sweep_look_idle', 'sweep_into_look', 'sweep_outof_look', 'swim', 'swim_back', 'swim_back_diagonal_left', 'swim_back_diagonal_right', 'swim_into_tread_water', 'swim_left', 'swim_left_diagonal', 'swim_right', 'swim_right_diagonal', 'swing_aboard', 'sword_comboA', 'sword_draw', 'sword_hit', 'sword_idle', 'sword_putaway', 'sword_roll_thrust', 'sword_slash', 'sword_cleave', 'sword_lunge', 'sword_thrust']
AnimListT_Z = [
 'tatoo_idle', 'tatoo_into_look', 'tatoo_look_idle', 'tatoo_outof_look', 'tatoo_receive_idle', 'tatoo_receive_into_look', 'tatoo_receive_look_idle', 'tatoo_receive_outof_look', 'teleport', 'tentacle_idle', 'tentacle_squeeze', 'tread_water', 'tread_water_into_teleport', 'turn_left', 'turn_right', 'voodoo_doll_poke', 'voodoo_doll_hurt', 'voodoo_draw', 'voodoo_idle', 'voodoo_swarm', 'voodoo_tune', 'voodoo_walk', 'walk', 'walk_back_diagonal_left', 'walk_back_diagonal_right', 'wand_cast_fire', 'wand_cast_idle', 'wand_cast_start', 'wand_hurt', 'wand_idle', 'wheel_idle']
AnimList = []
SkeletonBodyTypes = [
 '1', '2', '4', '8', 'djcr', 'djjm', 'djko', 'djpa', 'djtw', 'sp1', 'sp2', 'sp3', 'sp4', 'fr1', 'fr2', 'fr3', 'fr4']
CastBodyTypes = [
 'js', 'wt', 'es', 'cb', 'td', 'dj', 'jg', 'jr', 'fl', 'sl']
# okay decompiling .\pirates\makeapirate\MakeAPirateGlobals.pyc
