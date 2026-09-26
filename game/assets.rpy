init -2 python:
    if "mc_front" not in config.layers:
        config.layers.insert(config.layers.index("screens") + 1, "mc_front")
    config.tag_layer["mc"] = "mc_front"

image mc default = "images/characters/mc/McDefault_.png"
image mc o = "images/characters/mc/McO.png"
image mc shock = "images/characters/mc/McShock_.png"
image mc shock_hu = "images/characters/mc/McShockHU_.png"
image mc excited = "images/characters/mc/McExcited_.png"
image mc happy = "images/characters/mc/McHappy_.png"
image mc pout = "images/characters/mc/McPout_.png"
image mc dizzy = "images/characters/mc/McDizzy.png"
image mc actually = "images/characters/mc/McActually_.png"
image mc cry = "images/characters/mc/McCry.png"
image mc holdcry = "images/characters/mc/McHoldCry_.png"
image mc sad = "images/characters/mc/McSad.png"
image mc sad_hu = "images/characters/mc/McSadHU.png"
image mc serious = "images/characters/mc/McSerious.png"
image mc serious_hu = "images/characters/mc/McSeriousHU.png"
image mc dance = "images/characters/mc/McDance.png"

image cory talk = "images/characters/cory/CoryTalkNetral_.png"
image cory smile = "images/characters/cory/CoryTalkSmile.png"
image cory surprise = "images/characters/cory/CorySurprise.png"
image cory surprise_hu = "images/characters/cory/CorySurpriseHU.png"
image cory proud = "images/characters/cory/CoryProud_.png"
image cory proud_hu = "images/characters/cory/CoryProudHU.png"
image cory side = "images/characters/cory/CorySide_.png"
image cory side_close = "images/characters/cory/CorySideClose_.png"
image cory upset = "images/characters/cory/CoryUpset_.png"
image cory upset_hu = "images/characters/cory/CoryUpsetHU.png"
image cory disrespect = "images/characters/cory/CoryDisrespectful_.png"
image cory unimpressed = "images/characters/cory/CoryOhiounimpressed1_.png"
image cory unimpressed2 = "images/characters/cory/CoryOhiounimpressed2.png"
image cory fond = "images/characters/cory/CoryFondSmile_.png"
image cory talk_hu = "images/characters/cory/CoryTalkNetralHU.png"
image cory smile_hu = "images/characters/cory/CoryTalkSmileHU.png"
image cory dizzy = "images/characters/cory/CoryUpset_.png"
image cory anon = "images/characters/cory/CoryAnon.png"

image bass idle = "images/npc/chapter1/bass/largemouth_idle.png"
image bass hover = "images/npc/chapter1/bass/largemouth_hover.png"
image bass default = "images/npc/chapter1/bass/BassDefault.png"
image bass thinking = "images/npc/chapter1/bass/BassBerpikir.png"
image bass oh = "images/npc/chapter1/bass/BassOh!.png"

image uceng idle = "images/npc/chapter1/uceng/uceng_idle.png"
image uceng hover = "images/npc/chapter1/uceng/uceng_hover.png"
image uceng default = "images/npc/chapter1/uceng/UcengDefault_.png"
image uceng annoyed = "images/npc/chapter1/uceng/UcengAnnoyed_.png"
image uceng upset = "images/npc/chapter1/uceng/UcengUpset_.png"

image lele idle = "images/npc/chapter1/catfish/catfish_idle.png"
image lele hover = "images/npc/chapter1/catfish/catfish_hover.png"
image lele default = "images/npc/chapter1/catfish/LeleDefault_.png"
image lele curiga = "images/npc/chapter1/catfish/LeleCuriga_.png"
image lele depan = "images/npc/chapter1/catfish/LeleDepan.png"
image lele tidur = "images/npc/chapter1/catfish/LelePuraPuraTidur_.png"

image gator idle = "images/npc/chapter1/aligator/aligator_idle.png"
image gator hover = "images/npc/chapter1/aligator/aligator_hover.png"
image gator default = "images/npc/chapter1/aligator/GatorDefault.png"
image gator annoyed = "images/npc/chapter1/aligator/GatorAnnoyed.png"
image gator smile = "images/npc/chapter1/aligator/GatorSmile.png"
image gator surprised = "images/npc/chapter1/aligator/GatorSuprise.png"
image gator upset = "images/npc/chapter1/aligator/GatorUpset_.png"

image salmon idle = "images/npc/chapter2/Salmon/salmon_idle.png"
image salmon hover = "images/npc/chapter2/Salmon/salmon_hover.png"
image salmon default = "images/npc/chapter2/Salmon/SalDefault.png"
image salmon happy = "images/npc/chapter2/Salmon/SalHappy.png"
image salmon pien = "images/npc/chapter2/Salmon/SalPien.png"
image salmon pout = "images/npc/chapter2/Salmon/SalPout.png"
image salmon hug = "images/npc/chapter2/Salmon/SalHug.png"

image arowana idle = "images/npc/chapter2/Arowana/arowana_idle.png"
image arowana hover = "images/npc/chapter2/Arowana/arowana_hover.png"
image arowana default = "images/npc/chapter2/Arowana/AroDefault.png"
image arowana mad = "images/npc/chapter2/Arowana/AroMad.png"
image arowana smile = "images/npc/chapter2/Arowana/AroSmile.png"
image arowana squint = "images/npc/chapter2/Arowana/AroSquint.png"

image ghost idle = "images/npc/chapter2/Ghost/ghost_idle.png"
image ghost hover = "images/npc/chapter2/Ghost/ghost_hover.png"
image ghost default = "images/npc/chapter2/Ghost/GhostDefault_.png"
image ghost close = "images/npc/chapter2/Ghost/GhostClose_.png"
image ghost deadpan = "images/npc/chapter2/Ghost/GhostDeadpan_.png"
image ghost side = "images/npc/chapter2/Ghost/GhostSide_.png"
image ghost mweheh = "images/npc/chapter2/Ghost/GhostMweheh_.png"

image shrimp idle = "images/npc/chapter2/Mantis/mantis_idle.png"
image shrimp hover = "images/npc/chapter2/Mantis/mantis_hover.png"
image shrimp default = "images/npc/chapter2/Mantis/ScyDefault_.png"
image shrimp default_om = "images/npc/chapter2/Mantis/ScyDefaultOM_.png"
image shrimp laugh = "images/npc/chapter2/Mantis/ScyLaugh.png"
image shrimp proud = "images/npc/chapter2/Mantis/ScyProud.png"
image shrimp sepet = "images/npc/chapter2/Mantis/ScySepet.png"
image shrimp shy = "images/npc/chapter2/Mantis/ScyShy.png"
image shrimp smile = "images/npc/chapter2/Mantis/ScySmile.png"
image shrimp surprise = "images/npc/chapter2/Mantis/ScySurprise_.png"
image scy default = "images/npc/chapter2/Mantis/ScyDefault_.png"
image scy default_om = "images/npc/chapter2/Mantis/ScyDefaultOM_.png"
image scy laugh = "images/npc/chapter2/Mantis/ScyLaugh.png"
image scy proud = "images/npc/chapter2/Mantis/ScyProud.png"
image scy sepet = "images/npc/chapter2/Mantis/ScySepet.png"
image scy shy = "images/npc/chapter2/Mantis/ScyShy.png"
image scy smile = "images/npc/chapter2/Mantis/ScySmile.png"
image scy surprise = "images/npc/chapter2/Mantis/ScySurprise_.png"

image dunge idle = "images/npc/chapter3/dunge/crab_idle.png"
image dunge hover = "images/npc/chapter3/dunge/crab_hover.png"
image dunge default = "images/npc/chapter3/dunge/DunDefault.png"
image dunge mad = "images/npc/chapter3/dunge/DunMad.png"
image dunge smile = "images/npc/chapter3/dunge/DunSmile.png"
image dunge yeesh = "images/npc/chapter3/dunge/DunYeesh.png"

image crab idle = "images/backgrounds/chapter3/NIGHT/crab_idle.png"
image crab hover = "images/backgrounds/chapter3/NIGHT/crab_hover.png"
image seaweed idle = "images/backgrounds/chapter3/NIGHT/seaweed_idle.png"
image seaweed hover = "images/backgrounds/chapter3/NIGHT/seaweed_hover.png"
image bg night3 = "images/backgrounds/chapter3/NIGHT/bg night3.jpg"
image bg night3_bordered = "images/backgrounds/chapter3/NIGHT/bg night3_bordered.jpg"

image hawk idle = "images/npc/chapter3/hawk/turtle_idle.png"
image hawk hover = "images/npc/chapter3/hawk/turtle_hover.png"
image hawk default = "images/npc/chapter3/hawk/HawkDefault.png"
image hawk laugh = "images/npc/chapter3/hawk/HawkLaugh.png"
image hawk sigh = "images/npc/chapter3/hawk/HawkSigh.png"
image hawk smile = "images/npc/chapter3/hawk/HawkSmile.png"

image teto idle = "images/npc/chapter3/teto/teto_idle.png"
image teto hover = "images/npc/chapter3/teto/teto_hover.png"
image teto default = "images/npc/chapter3/teto/TetoDefault.png"
image teto gun_smirk = "images/npc/chapter3/teto/TetoGunSmirk.png"
image teto gun_upset = "images/npc/chapter3/teto/TetoGunUpset.png"
image teto laugh = "images/npc/chapter3/teto/TetoLaugh.png"
image teto pout = "images/npc/chapter3/teto/TetoPout.png"
image teto upset = "images/npc/chapter3/teto/TetoUpset.png"

image goby default = "images/npc/chapter3/GOBY/GobyDefault.png"
image goby annoy = "images/npc/chapter3/GOBY/GobyAnnoyed.png"
image goby disgust = "images/npc/chapter3/GOBY/GobyDisgusted.png"
image goby surprise ="images/npc/chapter3/GOBY/GobySurprise.png"
image goby struck = "images/npc/chapter3/GOBY/GobyStrucked.png"

image bunny idle = "images/npc/chapter3/seabunny/seabunny_idle.png"
image bunny hover = "images/npc/chapter3/seabunny/seabunny_hover.png"
image bunny default = "images/npc/chapter3/seabunny/BunnyDefault.png"
image bunny cry = "images/npc/chapter3/seabunny/BunnyCry.png"
image bunny happy = "images/npc/chapter3/seabunny/BunnyHappy.png"
image bunny sad = "images/npc/chapter3/seabunny/BunnySad.png"
image bunny scared = "images/npc/chapter3/seabunny/BunnyScared.png"

image empress placeholder = Solid("#8b2635")

image leo default = "images/characters/rotasi/LeoIdle.png"
image leo smile = "images/characters/rotasi/LeoHover.png"
image leo proud = "images/characters/rotasi/LeoHover.png"
image leo surprise = "images/characters/rotasi/LeoHover.png"
image leo talk = "images/characters/rotasi/LeoIdle.png"

# Chapter 5 Anomaly & Mirage Sprites
image scy_anomaly_cry:
    "images/chapter5/anomalies/scy_anomaly_cry.png"
    zoom 0.52

image scy_anomaly_burst:
    "images/chapter5/anomalies/scy_anomaly_burst.png"
    zoom 0.52

image cory_anomaly_distort:
    "images/chapter5/anomalies/cory_anomaly_distort.png"
    zoom 0.50

image cory_anomaly_scream:
    "images/chapter5/anomalies/cory_anomaly_scream.png"
    zoom 0.50

image leo_anomaly:
    "images/chapter5/anomalies/leo_anomaly.png"
    zoom 0.50

image leo_anomaly_scream:
    "images/chapter5/anomalies/leo_anomaly_scream.png"
    zoom 0.50

image scy_mirage = "scy_anomaly_cry"
image scy_mirage cry = "scy_anomaly_cry"
image scy_mirage burst = "scy_anomaly_burst"

image cory_mirage = "cory_anomaly_distort"
image cory_mirage distort = "cory_anomaly_distort"
image cory_mirage scream = "cory_anomaly_scream"

image leo_mirage = "leo_anomaly"
image leo_mirage default = "leo_anomaly"
image leo_mirage scream = "leo_anomaly_scream"

image bg abyss_depths = "images/backgrounds/chapter5/bg_abyss_center.png"
image bg abyss_wide = "images/backgrounds/chapter5/bg_abyss_wide.png"
image bg abyss_zone_left = "images/backgrounds/chapter5/bg_abyss_left.png"
image bg abyss_zone_center = "images/backgrounds/chapter5/bg_abyss_center.png"
image bg abyss_zone_right = "images/backgrounds/chapter5/bg_abyss_right.png"

image ch5_arrow_left = "images/ui/chapter5/arrow_left.png"
image ch5_arrow_left_hover = "images/ui/chapter5/arrow_left_hover.png"
image ch5_arrow_right = "images/ui/chapter5/arrow_right.png"
image ch5_arrow_right_hover = "images/ui/chapter5/arrow_right_hover.png"
image bg bedroom_dream = "images/backgrounds/chapter2/bgday2.jpg"
image bg tsunami_approaching = "images/backgrounds/chapter1/bgnight1.jpg"
image white = Solid("#ffffff")

image cory_talk_neutral = "images/characters/cory/CoryTalkNetral_.png"
image cory_side_legacy = "images/characters/cory/CorySide_.png"
image cory_surprise_legacy = "images/characters/cory/CorySurprise.png"
image cory_unimpressed2_legacy = "images/characters/cory/CoryOhiounimpressed2.png"
image mc_shock_legacy = "images/characters/mc/McShock_.png"
image mc_o_legacy = "images/characters/mc/McO.png"
image mc_excited_legacy = "images/characters/mc/McExcited_.png"
image mc_dizzy_legacy = "images/characters/mc/McDizzy.png"
image mc_actually_legacy = "images/characters/mc/McActually_.png"

image item_gold_idle = "images/items/chapter1/goldenrock_idle.png"
image item_gold_hover = "images/items/chapter1/goldenrock_hover.png"
image item_gold = "images/items/chapter1/goldenrock_idle.png"
image item_gold_hover_legacy = "images/items/chapter1/goldenrock_hover.png"
image item_ambalabu_idle = "images/items/chapter1/ambalabu_idle.png"
image item_ambalabu_hover = "images/items/chapter1/ambalabu_hover.png"
image item_ambalabu = "images/items/chapter1/ambalabu_idle.png"
image item_ambalabu_hover_legacy = "images/items/chapter1/ambalabu_hover.png"
image item_tiny_krill = "images/items/chapter2/krill_idle.png"
image item_tiny_krill_hover = "images/items/chapter2/krill_hover.png"
image item_coal = "images/items/chapter2/coal_idle.png"
image item_coal_hover = "images/items/chapter2/coal_hover.png"
image krill = "images/items/chapter2/krill_idle.png"
image krillangy = "images/items/chapter2/krill_idle.png"
image item_algae_idle = "images/items/chapter3/algae_idle.png"
image item_algae_hover = "images/items/chapter3/algae_hover.png"
image item_algae = "images/items/chapter3/algae_idle.png"
image item_seaweed_idle = "images/items/chapter3/seaweed_idle.png"
image item_seaweed_hover = "images/items/chapter3/seaweed_hover.png"
image item_seaweed = "images/items/chapter3/seaweed_idle.png"
image turtle idle = "images/npc/chapter3/hawk/turtle_idle.png"
image turtle hover = "images/npc/chapter3/hawk/turtle_hover.png"
image seabunny idle = "images/npc/chapter3/seabunny/seabunny_idle.png"
image seabunny hover = "images/npc/chapter3/seabunny/seabunny_hover.png"

image prologue_day = "images/backgrounds/prologue/prologue_day.jpg"
image ch1_day = "images/backgrounds/chapter1/bgday1.jpg"
image ch1_night = "images/backgrounds/chapter1/bgnight1.jpg"
image ch1_dark = "images/backgrounds/chapter1/bgdark1.png"
image ch2_day = "images/backgrounds/chapter2/bgday2.jpg"
image ch2_night = "images/backgrounds/chapter2/bgnight2.jpg"
image ch1_dialogue = "images/backgrounds/chapter1/bgday1.jpg"
image ch2_dialogue = "images/backgrounds/chapter2/bgnight2.jpg"
image ch3_day = "images/backgrounds/chapter3/bgday3.jpg"
image ch3_night = "images/backgrounds/chapter3/bgnight3.jpg"
image ch4_day = "images/backgrounds/chapter4/bg_festival_day.png"
image ch4_night = "images/backgrounds/chapter4/bg_festival_night.jpg"
image ch4_dialogue = "images/backgrounds/chapter4/bg_festival_day.png"
image ch4_dialogue_night = "images/backgrounds/chapter4/bg_festival_night.jpg"
image ch4_festival_day = "images/backgrounds/chapter4/bg_festival_day.png"
image ch4_festival_night = "images/backgrounds/chapter4/bg_festival_night.jpg"
image ch4_festival_night_bordered = "images/backgrounds/chapter4/bg_festival_night_bordered.jpg"

# Chapter 4 Exploration Sprites
image rin_explore_idle = "images/npc/chapter4/rin_explore_idle.png"
image rin_explore_hover = "images/npc/chapter4/rin_explore_hover.png"
image leo_explore_idle = "images/npc/chapter4/leo_explore_idle.png"
image leo_explore_hover = "images/npc/chapter4/leo_explore_hover.png"

image ch4_coral_idle = "images/items/chapter4/ch4_coral_idle.png"
image ch4_coral_hover = "images/items/chapter4/ch4_coral_hover.png"
image ch4_woodbox_idle = "images/items/chapter4/ch4_woodbox_idle.png"
image ch4_woodbox_hover = "images/items/chapter4/ch4_woodbox_hover.png"

image krillstall_idle = "images/items/chapter4/krillstall_idle.png"
image krillstall_hover = "images/items/chapter4/krillstall_hover.png"
image shootstall_idle = "images/items/chapter4/shootstall_idle.png"
image shootstall_hover = "images/items/chapter4/shootstall_hover.png"

image cutpro1 = "images/cutscenes/prologue/1.png"
image cutpro2 = "images/cutscenes/prologue/2.png"
image cutpro3 = "images/cutscenes/prologue/3.png"
image cutpro4 = "images/cutscenes/prologue/4.png"
image cutpro5 = "images/cutscenes/prologue/5.png"
image cutpro6 = "images/cutscenes/prologue/6.png"
image cutpro8 = "images/cutscenes/prologue/8.png"
image cutpro9 = "images/cutscenes/prologue/9.png"
image cutpro10 = "images/cutscenes/prologue/10.png"
image cutpro11 = "images/cutscenes/prologue/11.png"
image cutpro12 = "images/cutscenes/prologue/12.png"

image cutchap1 = "images/cutscenes/chapter1/1.png"
image cutchap2 = "images/cutscenes/chapter1/2.png"
image cutchap3 = "images/cutscenes/chapter1/3.png"
image cutchap4 = "images/cutscenes/chapter1/4.png"
image cutchap5 = "images/cutscenes/chapter1/5.png"

image bg name_input = "images/BackgroundNama.png"
image mc_name_input = "images/SpriteMCgede.png"

transform mc_name_pos:
    xalign 0.5
    yalign 1.0
