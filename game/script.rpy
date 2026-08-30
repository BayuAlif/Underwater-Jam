# =====================================
# Characters
# =====================================

# MC (Protagonist)
define mc = Character("MC", callback=speaker_callback("mc"))

# Cory (Companion Fish)
define cory = Character("Mr. Cory", callback=speaker_callback("cory"))
define f1 = cory

# NPCs
define bass = Character("Bass", callback=speaker_callback("bass"))
define uceng = Character("Uceng", callback=speaker_callback("uceng"))
define lele = Character("Lele", callback=speaker_callback("lele"))
define gator = Character("Gator", callback=speaker_callback("gator"))
define salmon = Character("Mrs. Salmon", callback=speaker_callback("salmon"))
define wana = Character("Mr. Wana", callback=speaker_callback("wana"))


# =====================================
# Character Sprites (Global Scaling)
# =====================================

define MC_SCALE = 0.85
define CORY_SCALE = 0.74

# MC (Protagonist) Sprites - Skala Global 0.85
image mc default = Transform("images/mc/McDefault.png", zoom=MC_SCALE)
image mc actual = Transform("images/mc/McActually.png", zoom=MC_SCALE)
image mc shock = Transform("images/mc/McShock.png", zoom=MC_SCALE)
image mc shockhu = Transform("images/mc/McShockHU.png", zoom=MC_SCALE)
image mc excited = Transform("images/mc/McExcited.png", zoom=MC_SCALE)
image mc happy = Transform("images/mc/McHappy.png", zoom=MC_SCALE)
image mc pout = Transform("images/mc/McPout.png", zoom=MC_SCALE)
image mc dizzy = Transform("images/mc/McDizzy.png", zoom=MC_SCALE)
image mc dizzyactually = Transform("images/mc/McDizzyActually.png", zoom=MC_SCALE)
image mc o = Transform("images/mc/Mc_o.png", zoom=MC_SCALE)

# Cory Sprites - Skala Global 0.80 dan Di-flip agar Menghadap ke Kanan (ke arah MC)
image cory default = Transform("images/cory/CoryTalkNetral.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory talk = Transform("images/cory/CoryTalkNetral.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory netral = Transform("images/cory/CoryTalkNetral.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory smile = Transform("images/cory/CoryTalkSmile.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory fond = Transform("images/cory/CoryFondSmile.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory proud = Transform("images/cory/CoryProud.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory surprise = Transform("images/cory/CorySurprise.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory shock = Transform("images/cory/CorySurprise.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory upset = Transform("images/cory/CoryUpset.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory disrespectful = Transform("images/cory/CoryDisrespectful_.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory unimpressed = Transform("images/cory/CoryOhiounimpressed1_.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory unimpressed2 = Transform("images/cory/CoryOhiounimpressed2.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory side = Transform("images/cory/CorySide.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory sideclose = Transform("images/cory/CorySideClose.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory netral_hu = Transform("images/cory/CoryTalkNetralHU_.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory smile_hu = Transform("images/cory/CoryTalkSmileHU.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory surprise_hu = Transform("images/cory/CorySurpriseHU.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory proud_hu = Transform("images/cory/CoryProudHU.png", zoom=CORY_SCALE, xzoom=-1.0)
image cory upset_hu = Transform("images/cory/CoryUpsetHU.png", zoom=CORY_SCALE, xzoom=-1.0)

# NPCs - Skala Global (Menghadap ke kanan/MC)
image bass default = Transform("images/npc/chapter1/bass/BassDefault.png", zoom=0.85, xzoom=-1.0)
image bass berpikir = Transform("images/npc/chapter1/bass/BassBerpikir.png", zoom=0.85, xzoom=-1.0)
image bass oh = Transform("images/npc/chapter1/bass/BassOh!.png", zoom=0.85, xzoom=-1.0)

image uceng default = Transform("images/npc/chapter1/uceng/UcengDefault.png", zoom=0.85, xzoom=-1.0)
image uceng annoyed = Transform("images/npc/chapter1/uceng/UcengAnnoyed.png", zoom=0.85, xzoom=-1.0)
image uceng upset = Transform("images/npc/chapter1/uceng/UcengUpset.png", zoom=0.85, xzoom=-1.0)

image lele default = Transform("images/npc/chapter1/lele/LeleDefault.png", zoom=0.78, xzoom=-1.0)
image lele curiga = Transform("images/npc/chapter1/lele/LeleCuriga.png", zoom=0.78, xzoom=-1.0)
image lele depan = Transform("images/npc/chapter1/lele/LeleDepan.png", zoom=0.78, xzoom=-1.0)
image lele puratidur = Transform("images/npc/chapter1/lele/LelePuraPuraTidur_.png", zoom=0.78, xzoom=-1.0)

define GATOR_SCALE = 0.67

image gator default = Transform("images/npc/chapter1/gator/GatorDefault.png", zoom=GATOR_SCALE)
image gator annoyed = Transform("images/npc/chapter1/gator/GatorAnnoyed.png", zoom=GATOR_SCALE)
image gator smile = Transform("images/npc/chapter1/gator/GatorSmile.png", zoom=GATOR_SCALE)
image gator surprised = Transform("images/npc/chapter1/gator/GatorSurprised.png", zoom=GATOR_SCALE)
image gator upset = Transform("images/npc/chapter1/gator/GatorUpset.png", zoom=GATOR_SCALE)


# =====================================
# Game Start
# =====================================

label start:

    jump chapter1