# MC is intentionally on its own layer above the dialogue screen.
# Cory and all NPCs remain on the normal master layer, so they stay behind the textbox.
init -2 python:
    if "mc_front" not in config.layers:
        config.layers.insert(config.layers.index("screens") + 1, "mc_front")
    config.tag_layer["mc"] = "mc_front"

# ============================================================
# ASSETS.RPY
# Friendly-name aliases used by the dialogue scripts (prologue.rpy,
# story/chapter1.rpy, story/chapter2.rpy, npc/chapter1/*.rpy, npc/chapter2/*.rpy).
#
# The REAL sprite declarations (one per original PNG file, cropped to their
# drawn content, positioned back with Composite) now live in
# game/sprites_declare.rpy. This file just points every old "show mc shock" /
# "show bass default" style tag at the matching new tag, so none of the
# existing story scripts need to be rewritten.
#
# This also fixes a few paths that were pointing at the wrong folder / wrong
# filename in the original file (bass, salmon, arowana, ghost & shrimp
# idle/hover, and the ghost/shrimp expression files that were missing their
# trailing underscore) — those were dead references before.
# ============================================================

# ============================================================
# assets.rpy — direct sprite declarations (plain file paths)
# ============================================================

# ---- Mc ----
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

# ---- Cory ----
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

# ---- Bass (chapter 1) ----
image bass idle = "images/npc/chapter1/bass/largemouth_idle.png"
image bass hover = "images/npc/chapter1/bass/largemouth_hover.png"
image bass default = "images/npc/chapter1/bass/BassDefault.png"
image bass thinking = "images/npc/chapter1/bass/BassBerpikir.png"
image bass oh = "images/npc/chapter1/bass/BassOh!.png"

# ---- Uceng (chapter 1) ----
image uceng idle = "images/npc/chapter1/uceng/uceng_idle.png"
image uceng hover = "images/npc/chapter1/uceng/uceng_hover.png"
image uceng default = "images/npc/chapter1/uceng/UcengDefault_.png"
image uceng annoyed = "images/npc/chapter1/uceng/UcengAnnoyed_.png"
image uceng upset = "images/npc/chapter1/uceng/UcengUpset_.png"

# ---- Lele / catfish (chapter 1) ----
image lele idle = "images/npc/chapter1/catfish/catfish_idle.png"
image lele hover = "images/npc/chapter1/catfish/catfish_hover.png"
image lele default = "images/npc/chapter1/catfish/LeleDefault_.png"
image lele curiga = "images/npc/chapter1/catfish/LeleCuriga_.png"
image lele depan = "images/npc/chapter1/catfish/LeleDepan.png"
image lele tidur = "images/npc/chapter1/catfish/LelePuraPuraTidur_.png"

# ---- Gator (chapter 1) ----
image gator idle = "images/npc/chapter1/aligator/aligator_idle.png"
image gator hover = "images/npc/chapter1/aligator/aligator_hover.png"
image gator default = "images/npc/chapter1/aligator/GatorDefault.png"
image gator annoyed = "images/npc/chapter1/aligator/GatorAnnoyed.png"
image gator smile = "images/npc/chapter1/aligator/GatorSmile.png"
image gator surprised = "images/npc/chapter1/aligator/GatorSuprise.png"
image gator upset = "images/npc/chapter1/aligator/GatorUpset_.png"

# ---- Salmon (chapter 2) ----
image salmon idle = "images/npc/chapter2/Salmon/salmon_idle.png"
image salmon hover = "images/npc/chapter2/Salmon/salmon_hover.png"
image salmon default = "images/npc/chapter2/Salmon/SalDefault.png"
image salmon happy = "images/npc/chapter2/Salmon/SalHappy.png"
image salmon pien = "images/npc/chapter2/Salmon/SalPien.png"
image salmon pout = "images/npc/chapter2/Salmon/SalPout.png"
image salmon hug = "images/npc/chapter2/Salmon/SalHug.png"

# ---- Arowana (chapter 2) ----
image arowana idle = "images/npc/chapter2/Arowana/arowana_idle.png"
image arowana hover = "images/npc/chapter2/Arowana/arowana_hover.png"
image arowana default = "images/npc/chapter2/Arowana/AroDefault.png"
image arowana mad = "images/npc/chapter2/Arowana/AroMad.png"
image arowana smile = "images/npc/chapter2/Arowana/AroSmile.png"
image arowana squint = "images/npc/chapter2/Arowana/AroSquint.png"

# ---- Ghostfish (chapter 2) ----
image ghost idle = "images/npc/chapter2/Ghost/ghost_idle.png"
image ghost hover = "images/npc/chapter2/Ghost/ghost_hover.png"
image ghost default = "images/npc/chapter2/Ghost/GhostDefault_.png"
image ghost close = "images/npc/chapter2/Ghost/GhostClose_.png"
image ghost deadpan = "images/npc/chapter2/Ghost/GhostDeadpan_.png"
image ghost side = "images/npc/chapter2/Ghost/GhostSide_.png"
image ghost mweheh = "images/npc/chapter2/Ghost/GhostMweheh_.png"

# ---- Mantis Shrimp (chapter 2) ----
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

# ---- Dunge / crab (chapter 3) ----
image dunge idle = "images/npc/chapter3/dunge/crab_idle.png"
image dunge hover = "images/npc/chapter3/dunge/crab_hover.png"
image dunge default = "images/npc/chapter3/dunge/DunDefault.png"
image dunge mad = "images/npc/chapter3/dunge/DunMad.png"
image dunge smile = "images/npc/chapter3/dunge/DunSmile.png"
image dunge yeesh = "images/npc/chapter3/dunge/DunYeesh.png"

# ---- Hawk / hawksbill turtle (chapter 3) ----
image hawk idle = "images/npc/chapter3/hawk/turtle_idle.png"
image hawk hover = "images/npc/chapter3/hawk/turtle_hover.png"
image hawk default = "images/npc/chapter3/hawk/HawkDefault.png"
image hawk laugh = "images/npc/chapter3/hawk/HawkLaugh.png"
image hawk sigh = "images/npc/chapter3/hawk/HawkSigh.png"
image hawk smile = "images/npc/chapter3/hawk/HawkSmile.png"

# ---- Teto / goby (chapter 3) ----
image teto idle = "images/npc/chapter3/gobypis/teto_idle.png"
image teto hover = "images/npc/chapter3/gobypis/teto_hover.png"

# ---- Sea Bunny (chapter 3) ----
image bunny idle = "images/npc/chapter3/seabunny/seabunny_idle.png"
image bunny hover = "images/npc/chapter3/seabunny/seabunny_hover.png"
image bunny default = "images/npc/chapter3/seabunny/BunnyDefault.png"
image bunny cry = "images/npc/chapter3/seabunny/BunnyCry.png"
image bunny happy = "images/npc/chapter3/seabunny/BunnyHappy.png"
image bunny sad = "images/npc/chapter3/seabunny/BunnySad.png"
image bunny scared = "images/npc/chapter3/seabunny/BunnyScared.png"

# ---- Legacy single-word aliases ----
image cory_talk_neutral = "images/characters/cory/CoryTalkNetral_.png"
image cory_side_legacy = "images/characters/cory/CorySide_.png"
image cory_surprise_legacy = "images/characters/cory/CorySurprise.png"
image cory_unimpressed2_legacy = "images/characters/cory/CoryOhiounimpressed2.png"
image mc_shock_legacy = "images/characters/mc/McShock_.png"
image mc_o_legacy = "images/characters/mc/McO.png"
image mc_excited_legacy = "images/characters/mc/McExcited_.png"
image mc_dizzy_legacy = "images/characters/mc/McDizzy.png"
image mc_actually_legacy = "images/characters/mc/McActually_.png"

# ============================================================
# Items, backgrounds & battle art (unchanged / not part of the sprite crop)
# ============================================================

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

image prologue_day = "images/backgrounds/prologue/prologue_day.jpg"
image ch1_day = "images/backgrounds/chapter1/bgday1.jpg"
image ch1_night = "images/backgrounds/chapter1/bgnight1.jpg"
image ch1_dark = "images/backgrounds/chapter1/bgdark1.png"
image ch2_day = "images/backgrounds/chapter2/bgday2.jpg"
image ch2_night = "images/backgrounds/chapter2/bgnight2.jpg"
image ch1_dialogue = "images/backgrounds/chapter1/bgday1.jpg"
image ch2_dialogue = "images/backgrounds/chapter2/bgnight2.jpg"
image ch3_day = "images/backgrounds/chapter3/DAY/bg day3_bordered.jpg"
image ch3_night = "images/backgrounds/chapter3/NIGHT/bg night3_bordered.jpg"

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

