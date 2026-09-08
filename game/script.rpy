# =====================================
# Characters
# =====================================

# MC (Protagonist)
define mc = Character("MC", callback=speaker_callback("mc"))

# Cory (Companion Fish)
define cory = Character("Mr. Cory", callback=speaker_callback("cory"))
define f1 = cory

# Chapter 2 - Mantis Shrimp
define shrimp = Character("Mantis Shrimp", callback=speaker_callback("shrimp"))
define scy = shrimp
define f2 = shrimp

# Chapter 3 Characters
define bunny = Character("Sea Bunny", callback=speaker_callback("bunny"))
define parva = bunny
define joruna = bunny
define f3 = bunny

define hawk = Character("Gran Hawk", callback=speaker_callback("hawk"))
define teto = Character("Empress Teto", callback=speaker_callback("teto"))
define goby = Character("Goby", callback=speaker_callback("goby"))

# NPCs
define bass = Character("Bass", callback=speaker_callback("bass"))
define uceng = Character("Uceng", callback=speaker_callback("uceng"))
define lele = Character("Lele", callback=speaker_callback("lele"))
define gator = Character("Gator", callback=speaker_callback("gator"))
define salmon = Character("Mrs. Salmon", callback=speaker_callback("salmon"))
define wana = Character("Mr. Wana", callback=speaker_callback("wana"))
define ghost = Character("Ghost", callback=speaker_callback("ghost"))


# =====================================
# Character Sprites (Global Scaling)
# =====================================

define MC_SCALE = 0.72
define CORY_SCALE = 0.74


# =====================================
# MC Sprites
# =====================================

image mc default = Transform(
    "images/mc/McDefault.png",
    zoom=MC_SCALE
)

image mc actual = Transform(
    "images/mc/McActually.png",
    zoom=MC_SCALE
)

image mc shock = Transform(
    "images/mc/McShock.png",
    zoom=MC_SCALE
)

image mc shockhu = Transform(
    "images/mc/McShockHU.png",
    zoom=MC_SCALE
)

image mc excited = Transform(
    "images/mc/McExcited.png",
    zoom=MC_SCALE
)

image mc happy = Transform(
    "images/mc/McHappy.png",
    zoom=MC_SCALE
)

image mc pout = Transform(
    "images/mc/McPout.png",
    zoom=MC_SCALE
)

image mc dizzy = Transform(
    "images/mc/McDizzy.png",
    zoom=MC_SCALE
)

image mc dizzyactually = Transform(
    "images/mc/McDizzyActually.png",
    zoom=MC_SCALE
)

image mc o = Transform(
    "images/mc/Mc_o.png",
    zoom=MC_SCALE
)


# =====================================
# Cory Sprites
# =====================================

image cory default = Transform(
    "images/cory/CoryTalkNetral.png",
    zoom=CORY_SCALE
)

image cory talk = Transform(
    "images/cory/CoryTalkNetral.png",
    zoom=CORY_SCALE
)

image cory netral = Transform(
    "images/cory/CoryTalkNetral.png",
    zoom=CORY_SCALE
)

image cory smile = Transform(
    "images/cory/CoryTalkSmile.png",
    zoom=CORY_SCALE
)

image cory fond = Transform(
    "images/cory/CoryFondSmile.png",
    zoom=CORY_SCALE
)

image cory proud = Transform(
    "images/cory/CoryProud.png",
    zoom=CORY_SCALE
)

image cory surprise = Transform(
    "images/cory/CorySurprise.png",
    zoom=CORY_SCALE
)

image cory shock = Transform(
    "images/cory/CorySurprise.png",
    zoom=CORY_SCALE
)

image cory upset = Transform(
    "images/cory/CoryUpset.png",
    zoom=CORY_SCALE
)

image cory disrespectful = Transform(
    "images/cory/CoryDisrespectful_.png",
    zoom=CORY_SCALE
)

image cory unimpressed = Transform(
    "images/cory/CoryOhiounimpressed1_.png",
    zoom=CORY_SCALE
)

# FIX:
# fish03.rpy memanggil "cory ohiounimpressed1"
# jadi image tersebut harus didefinisikan.
image cory ohiounimpressed1 = Transform(
    "images/cory/CoryOhiounimpressed1_.png",
    zoom=CORY_SCALE
)

image cory unimpressed2 = Transform(
    "images/cory/CoryOhiounimpressed2.png",
    zoom=CORY_SCALE
)

image cory side = Transform(
    "images/cory/CorySide.png",
    zoom=CORY_SCALE
)

image cory sideclose = Transform(
    "images/cory/CorySideClose.png",
    zoom=CORY_SCALE
)

image cory netral_hu = Transform(
    "images/cory/CoryTalkNetralHU_.png",
    zoom=CORY_SCALE
)

image cory smile_hu = Transform(
    "images/cory/CoryTalkSmileHU.png",
    zoom=CORY_SCALE
)

image cory surprise_hu = Transform(
    "images/cory/CorySurpriseHU.png",
    zoom=CORY_SCALE
)

image cory proud_hu = Transform(
    "images/cory/CoryProudHU.png",
    zoom=CORY_SCALE
)

image cory upset_hu = Transform(
    "images/cory/CoryUpsetHU.png",
    zoom=CORY_SCALE
)


# =====================================
# Chapter 1 NPCs
# =====================================

define BASS_SCALE = 0.76

image bass default = Transform(
    "images/npc/chapter1/bass/BassDefault.png",
    zoom=BASS_SCALE
)

image bass berpikir = Transform(
    "images/npc/chapter1/bass/BassBerpikir.png",
    zoom=BASS_SCALE
)

image bass oh = Transform(
    "images/npc/chapter1/bass/BassOh!.png",
    zoom=BASS_SCALE
)


define UCENG_SCALE = 0.70

image uceng default = Transform(
    "images/npc/chapter1/uceng/UcengDefault.png",
    zoom=UCENG_SCALE
)

image uceng annoyed = Transform(
    "images/npc/chapter1/uceng/UcengAnnoyed.png",
    zoom=UCENG_SCALE
)

image uceng upset = Transform(
    "images/npc/chapter1/uceng/UcengUpset.png",
    zoom=UCENG_SCALE
)


define LELE_SCALE = 0.77

image lele default = Transform(
    "images/npc/chapter1/lele/LeleDefault.png",
    zoom=LELE_SCALE
)

image lele curiga = Transform(
    "images/npc/chapter1/lele/LeleCuriga.png",
    zoom=LELE_SCALE
)

image lele depan = Transform(
    "images/npc/chapter1/lele/LeleDepan.png",
    zoom=LELE_SCALE
)

image lele puratidur = Transform(
    "images/npc/chapter1/lele/LelePuraPuraTidur_.png",
    zoom=LELE_SCALE
)


define GATOR_SCALE = 0.74

image gator default = Transform(
    "images/npc/chapter1/gator/GatorDefault.png",
    zoom=GATOR_SCALE
)

image gator annoyed = Transform(
    "images/npc/chapter1/gator/GatorAnnoyed.png",
    zoom=GATOR_SCALE
)

image gator smile = Transform(
    "images/npc/chapter1/gator/GatorSmile.png",
    zoom=GATOR_SCALE
)

image gator surprised = Transform(
    "images/npc/chapter1/gator/GatorSurprised.png",
    zoom=GATOR_SCALE
)

image gator upset = Transform(
    "images/npc/chapter1/gator/GatorUpset.png",
    zoom=GATOR_SCALE
)


# =====================================
# Chapter 2 NPCs
# =====================================

define WANA_SCALE = 0.95

image wana default = Transform(
    "images/npc/chapter2/arowana/AroDefault.png",
    zoom=WANA_SCALE,
    xanchor=0.685
)

image wana mad = Transform(
    "images/npc/chapter2/arowana/AroMad.png",
    zoom=WANA_SCALE,
    xanchor=0.758
)

image wana smile = Transform(
    "images/npc/chapter2/arowana/AroSmile.png",
    zoom=WANA_SCALE,
    xanchor=0.685
)

image wana squint = Transform(
    "images/npc/chapter2/arowana/AroSquint.png",
    zoom=WANA_SCALE,
    xanchor=0.719
)

image arowana default = Transform(
    "images/npc/chapter2/arowana/AroDefault.png",
    zoom=WANA_SCALE,
    xanchor=0.685
)

image arowana mad = Transform(
    "images/npc/chapter2/arowana/AroMad.png",
    zoom=WANA_SCALE,
    xanchor=0.758
)

image arowana smile = Transform(
    "images/npc/chapter2/arowana/AroSmile.png",
    zoom=WANA_SCALE,
    xanchor=0.685
)

image arowana squint = Transform(
    "images/npc/chapter2/arowana/AroSquint.png",
    zoom=WANA_SCALE,
    xanchor=0.719
)


define SALMON_SCALE = 0.95

image salmon default = Transform(
    "images/npc/chapter2/salmon/SalDefault.png",
    zoom=SALMON_SCALE
)

image salmon happy = Transform(
    "images/npc/chapter2/salmon/SalHappy.png",
    zoom=SALMON_SCALE
)

image salmon pien = Transform(
    "images/npc/chapter2/salmon/SalPien.png",
    zoom=SALMON_SCALE
)

image salmon cry = Transform(
    "images/npc/chapter2/salmon/SalPien.png",
    zoom=SALMON_SCALE
)

image salmon pout = Transform(
    "images/npc/chapter2/salmon/SalPout.png",
    zoom=SALMON_SCALE
)


# =====================================
# Ghost
# =====================================

define GHOST_SCALE = 0.95

image ghost default = Transform(
    "images/npc/chapter2/ghost/GhostDefault.png",
    zoom=GHOST_SCALE
)

image ghost close = Transform(
    "images/npc/chapter2/ghost/GhostClose.png",
    zoom=GHOST_SCALE
)

image ghost deadpan = Transform(
    "images/npc/chapter2/ghost/GhostDeadpan.png",
    zoom=GHOST_SCALE
)

image ghost mweheh = Transform(
    "images/npc/chapter2/ghost/GhostMweheh.png",
    zoom=GHOST_SCALE
)

image ghost side = Transform(
    "images/npc/chapter2/ghost/GhostSide.png",
    zoom=GHOST_SCALE
)


# =====================================
# Mantis Shrimp (Scyllarus)
# =====================================

define MANTIS_SCALE = 0.95

image shrimp default = Transform(
    "images/npc/chapter2/mantis/ScyDefault.png",
    zoom=MANTIS_SCALE
)

image shrimp laugh = Transform(
    "images/npc/chapter2/mantis/ScyLaugh.png",
    zoom=MANTIS_SCALE
)

image shrimp proud = Transform(
    "images/npc/chapter2/mantis/ScyProud.png",
    zoom=MANTIS_SCALE
)

image shrimp seppet = Transform(
    "images/npc/chapter2/mantis/ScySepet.png",
    zoom=MANTIS_SCALE
)

image shrimp sepet = Transform(
    "images/npc/chapter2/mantis/ScySepet.png",
    zoom=MANTIS_SCALE
)

image shrimp shy = Transform(
    "images/npc/chapter2/mantis/ScyShy.png",
    zoom=MANTIS_SCALE
)

image shrimp smile = Transform(
    "images/npc/chapter2/mantis/ScySmile.png",
    zoom=MANTIS_SCALE
)

image shrimp surprise = Transform(
    "images/npc/chapter2/mantis/ScySurprise.png",
    zoom=MANTIS_SCALE
)

image shrimp defaultom = Transform(
    "images/npc/chapter2/mantis/ScyDefault.png",
    zoom=MANTIS_SCALE
)

# Scy aliases for shrimp
image scy default = Transform("images/npc/chapter2/mantis/ScyDefault.png", zoom=MANTIS_SCALE)
image scy laugh = Transform("images/npc/chapter2/mantis/ScyLaugh.png", zoom=MANTIS_SCALE)
image scy proud = Transform("images/npc/chapter2/mantis/ScyProud.png", zoom=MANTIS_SCALE)
image scy sepet = Transform("images/npc/chapter2/mantis/ScySepet.png", zoom=MANTIS_SCALE)
image scy seppet = Transform("images/npc/chapter2/mantis/ScySepet.png", zoom=MANTIS_SCALE)
image scy shy = Transform("images/npc/chapter2/mantis/ScyShy.png", zoom=MANTIS_SCALE)
image scy smile = Transform("images/npc/chapter2/mantis/ScySmile.png", zoom=MANTIS_SCALE)
image scy surprise = Transform("images/npc/chapter2/mantis/ScySurprise.png", zoom=MANTIS_SCALE)
image scy defaultom = Transform("images/npc/chapter2/mantis/ScyDefault.png", zoom=MANTIS_SCALE)


# =====================================
# Chapter 3 NPCs: Sea Bunny & Sea Turtle
# =====================================

define BUNNY_SCALE = 0.82
define HAWK_SCALE = 0.90

init -15 python:
    def safe_ch3_sprite(path, fallback):
        if renpy.loadable(path):
            return path
        return fallback

image bunny default = Transform(
    safe_ch3_sprite("images/npc/chapter3/bunny/BunnyDefault.png", "images/mc/McDefault.png"),
    zoom=BUNNY_SCALE
)
image bunny cry = Transform(
    safe_ch3_sprite("images/npc/chapter3/bunny/BunnyCry.png", "images/mc/McShock.png"),
    zoom=BUNNY_SCALE
)
image bunny scared = Transform(
    safe_ch3_sprite("images/npc/chapter3/bunny/BunnyScared.png", "images/mc/McPout.png"),
    zoom=BUNNY_SCALE
)
image bunny sad = Transform(
    safe_ch3_sprite("images/npc/chapter3/bunny/BunnySad.png", "images/mc/McPout.png"),
    zoom=BUNNY_SCALE
)
image bunny happy = Transform(
    safe_ch3_sprite("images/npc/chapter3/bunny/BunnyHappy.png", "images/mc/McHappy.png"),
    zoom=BUNNY_SCALE
)

image hawk default = Transform(
    safe_ch3_sprite("images/npc/chapter3/hawk/HawkDefault.png", "images/cory/CoryTalkNetral.png"),
    zoom=HAWK_SCALE
)
image hawk sigh = Transform(
    safe_ch3_sprite("images/npc/chapter3/hawk/HawkSigh.png", "images/cory/CorySide.png"),
    zoom=HAWK_SCALE
)
image hawk laugh = Transform(
    safe_ch3_sprite("images/npc/chapter3/hawk/HawkLaugh.png", "images/cory/CoryTalkSmile.png"),
    zoom=HAWK_SCALE
)
image hawk smile = Transform(
    safe_ch3_sprite("images/npc/chapter3/hawk/HawkSmile.png", "images/cory/CoryTalkSmile.png"),
    zoom=HAWK_SCALE
)


# =====================================
# Script Convenience Image Aliases
# =====================================

image CoryTalkSmileHU = Transform("images/cory/CoryTalkSmileHU.png", zoom=CORY_SCALE)
image CoryFondSmile = Transform("images/cory/CoryFondSmile.png", zoom=CORY_SCALE)
image CorySide = Transform("images/cory/CorySide.png", zoom=CORY_SCALE)
image CorySideClose = Transform("images/cory/CorySideClose.png", zoom=CORY_SCALE)
image CoryOhiounimpressed1 = Transform("images/cory/CoryOhiounimpressed1_.png", zoom=CORY_SCALE)
image CoryTalkNetral = Transform("images/cory/CoryTalkNetral.png", zoom=CORY_SCALE)
image CoryTalkNetralHU = Transform("images/cory/CoryTalkNetralHU_.png", zoom=CORY_SCALE)
image CorySurprise = Transform("images/cory/CorySurprise.png", zoom=CORY_SCALE)
image CoryUpset = Transform("images/cory/CoryUpset.png", zoom=CORY_SCALE)
image CorySmile = Transform("images/cory/CoryTalkSmile.png", zoom=CORY_SCALE)

image McExcited = Transform("images/mc/McExcited.png", zoom=MC_SCALE)
image McShock = Transform("images/mc/McShock.png", zoom=MC_SCALE)
image Mc_o = Transform("images/mc/Mc_o.png", zoom=MC_SCALE)
image McHappy = Transform("images/mc/McHappy.png", zoom=MC_SCALE)
image McDefault = Transform("images/mc/McDefault.png", zoom=MC_SCALE)
image McPout = Transform("images/mc/McPout.png", zoom=MC_SCALE)
image McActually = Transform("images/mc/McActually.png", zoom=MC_SCALE)

image ScyProud = Transform("images/npc/chapter2/mantis/ScyProud.png", zoom=MANTIS_SCALE)
image ScySepet = Transform("images/npc/chapter2/mantis/ScySepet.png", zoom=MANTIS_SCALE)
image ScyDefaultOM = Transform("images/npc/chapter2/mantis/ScyDefault.png", zoom=MANTIS_SCALE)
image ScySurprise = Transform("images/npc/chapter2/mantis/ScySurprise.png", zoom=MANTIS_SCALE)
image ScyLaugh = Transform("images/npc/chapter2/mantis/ScyLaugh.png", zoom=MANTIS_SCALE)
image ScyShy = Transform("images/npc/chapter2/mantis/ScyShy.png", zoom=MANTIS_SCALE)
image ScyDefault = Transform("images/npc/chapter2/mantis/ScyDefault.png", zoom=MANTIS_SCALE)

image BunnyCry = Transform(safe_ch3_sprite("images/npc/chapter3/bunny/BunnyCry.png", "images/mc/McShock.png"), zoom=BUNNY_SCALE)
image BunnyScared = Transform(safe_ch3_sprite("images/npc/chapter3/bunny/BunnyScared.png", "images/mc/McPout.png"), zoom=BUNNY_SCALE)
image BunnySad = Transform(safe_ch3_sprite("images/npc/chapter3/bunny/BunnySad.png", "images/mc/McPout.png"), zoom=BUNNY_SCALE)
image BunnyDefault = Transform(safe_ch3_sprite("images/npc/chapter3/bunny/BunnyDefault.png", "images/mc/McDefault.png"), zoom=BUNNY_SCALE)
image BunnyHappy = Transform(safe_ch3_sprite("images/npc/chapter3/bunny/BunnyHappy.png", "images/mc/McHappy.png"), zoom=BUNNY_SCALE)

image HawkDefault = Transform(safe_ch3_sprite("images/npc/chapter3/hawk/HawkDefault.png", "images/cory/CoryTalkNetral.png"), zoom=HAWK_SCALE)
image HawkSigh = Transform(safe_ch3_sprite("images/npc/chapter3/hawk/HawkSigh.png", "images/cory/CorySide.png"), zoom=HAWK_SCALE)
image HawkLaugh = Transform(safe_ch3_sprite("images/npc/chapter3/hawk/HawkLaugh.png", "images/cory/CoryTalkSmile.png"), zoom=HAWK_SCALE)
image HawkSmile = Transform(safe_ch3_sprite("images/npc/chapter3/hawk/HawkSmile.png", "images/cory/CoryTalkSmile.png"), zoom=HAWK_SCALE)


# =====================================
# Game Start
# =====================================

label start:

    jump chapter1