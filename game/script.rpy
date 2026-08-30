# =====================================
# Characters
# =====================================

# MC
define f1 = Character("Cory", callback=speaker_callback("f1"))

# NPCs
define bass = Character("Bass", callback=speaker_callback("bass"))
define uceng = Character("Uceng", callback=speaker_callback("uceng"))
define lele = Character("Lele", callback=speaker_callback("lele"))
define gator = Character("Gator", callback=speaker_callback("gator"))


# =====================================
# Character Sprites
# =====================================

# Cory (MC)
image f1 default = "images/mc/McDefault.png"
image f1 actual = "images/mc/McActually.png"
image f1 shock = "images/mc/McShock.png"
image f1 shockhu = "images/mc/McShockHU.png"
image f1 excited = "images/mc/McExcited.png"
image f1 happy = "images/mc/McHappy.png"
image f1 pout = "images/mc/McPout.png"
image f1 dizzy = "images/mc/McDizzy.png"
image f1 dizzyactually = "images/mc/McDizzyActually.png"

# NPCs
image bass default = "images/npc/chapter1/bass/BassDefault.png"
image bass berpikir = "images/npc/chapter1/bass/BassBerpikir.png"
image bass oh = "images/npc/chapter1/bass/BassOh!.png"

image uceng default = "images/npc/chapter1/uceng/UcengDefault.png"
image uceng annoyed = "images/npc/chapter1/uceng/UcengAnnoyed.png"
image uceng upset = "images/npc/chapter1/uceng/UcengUpset.png"

image lele default = "images/npc/chapter1/lele/LeleDefault.png"
image lele curiga = "images/npc/chapter1/lele/LeleCuriga.png"
image lele depan = "images/npc/chapter1/lele/LeleDepan.png"
image lele puratidur = "images/npc/chapter1/lele/LelePuraPuraTidur_.png"

image gator default = "images/npc/chapter1/gator/GatorDefault.png"
image gator annoyed = "images/npc/chapter1/gator/GatorAnnoyed.png"
image gator smile = "images/npc/chapter1/gator/GatorSmile.png"
image gator surprised = "images/npc/chapter1/gator/GatorSurprised.png"
image gator upset = "images/npc/chapter1/gator/GatorUpset.png"


# =====================================
# Game Start
# =====================================

label start:

    jump chapter1