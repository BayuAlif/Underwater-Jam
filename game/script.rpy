# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC", color="#ffffff")
define unknown = Character("???", color="#ffffff")
define system = Character("System", color="#888888")

# Variabel Karakter Aktif
default current_character = "MC"

# Background dialog malam (Aset utuh 1920x1080 tanpa lubang)
image bg_dialog_night = "images/background/FIXbgnight1.png"

# =========================================================
# TRANSFORM POSISI KARAKTER (1080p)
# =========================================================
transform mc_left:
    xalign 0.12
    yalign 0.95

transform npc_right:
    xalign 0.85
    yalign 0.95

transform npc_left:
    xalign 0.12
    yalign 0.95

transform npc_center:
    xalign 0.5
    yalign 0.95

transform mc_right:
    xalign 0.85
    yalign 0.95

transform shake:
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

# =========================================================
# DEKLARASI SPRITE MC
# =========================================================
image mc default = "images/Mc/McDefault.png"
image mc normal = "mc default"
image mc netral = "mc default"

image mc happy = "images/Mc/McHappy.png"
image mc senang = "mc happy"
image mc senyum = "mc happy"

image mc actually = "images/Mc/McActually.png"
image mc normal2 = "mc actually"
image mc smug = "mc actually"

image mc excited = "images/Mc/McExcited.png"
image mc exited = "mc excited"
image mc semangat = "mc excited"

image mc dizzy = "images/Mc/McDizzy.png"
image mc bingung = "mc dizzy"
image mc bingung1 = "mc dizzy"
image mc pusing = "mc dizzy"

image mc dizzy actually = "images/Mc/McDizzyActually.png"
image mc bingungbanget = "mc dizzy actually"
image mc bingungbanget2 = "mc dizzy actually"

image mc o = "images/Mc/Mc_o.png"
image mc _o = "mc o"
image mc bingung2 = "mc o"
image mc wow = "mc o"

image mc shock = "images/Mc/McShock.png"
image mc kaget = "mc shock"
image mc dongok = "mc shock"
image mc surprised = "mc shock"

image mc shock hu = "images/Mc/McShockHU.png"
image mc shockhu = "mc shock hu"
image mc kaget hu = "mc shock hu"
image mc dongok hu = "mc shock hu"

image mc pout = "images/Mc/McPout.png"
image mc gakpuas = "mc pout"
image mc cemberut = "mc pout"
image mc kecewa = "mc pout"

image unknown = "images/CoryBlack.png"
image cory shadow = "unknown"

image jumping:
    "mc semangat"
    zoom 0.6875
    xalign 0.85
    yalign 1.0
    easeout 0.4 yoffset -50
    easein 0.4 yoffset 0
    repeat
# =========================================================
# DEKLARASI SPRITE MC
# =========================================================
image mc default = Transform("images/Mc/McDefault.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc normal = "mc default"
image mc netral = "mc default"

image mc happy = Transform("images/Mc/McHappy.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc senang = "mc happy"
image mc senyum = "mc happy"

image mc actually = Transform("images/Mc/McActually.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc normal2 = "mc actually"
image mc smug = "mc actually"

image mc excited = Transform("images/Mc/McExcited.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc exited = "mc excited"
image mc semangat = "mc excited"

image mc dizzy = Transform("images/Mc/McDizzy.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc bingung = "mc dizzy"
image mc bingung1 = "mc dizzy"
image mc pusing = "mc dizzy"

image mc dizzy actually = Transform("images/Mc/McDizzyActually.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc bingungbanget = "mc dizzy actually"
image mc bingungbanget2 = "mc dizzy actually"

image mc o = Transform("images/Mc/Mc_o.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc _o = "mc o"
image mc bingung2 = "mc o"
image mc wow = "mc o"

image mc shock = Transform("images/Mc/McShock.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc kaget = "mc shock"
image mc dongok = "mc shock"
image mc surprised = "mc shock"

image mc shock hu = Transform("images/Mc/McShockHU.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc shockhu = "mc shock hu"
image mc kaget hu = "mc shock hu"
image mc dongok hu = "mc shock hu"

image mc pout = Transform("images/Mc/McPout.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc gakpuas = "mc pout"
image mc cemberut = "mc pout"
image mc kecewa = "mc pout"

image jumping:
    "mc semangat"
    yalign 1.0
    easeout 0.4 yoffset -50
    easein 0.4 yoffset 0
    repeat

label start:
    play music prologue_funny_underwater
    scene rivershore
    "{i}Ah, the rivershore. A serene calming scene adorned by the rustling wind of leaves.{/i}" 
    "{i}Gentle applauses are carried by the trees of forest in celebration for yet another day of the sun’s blessing..{/i}"
   
    scene rustlingbush with dissolve
    play sound bushrustling
    "{i}An absolute perfect scene for….{/i}"

    scene flyingfish
    mc "Weee~! For practicing my flying fish jump of course! Haha!"

    "{i}I soared through the sky, my arms and legs held up by the encouraging carry of gravity.{/i}"
    "{i}It felt like I had finally achieved the true nature of those magical fishes.{/i}"

    scene rivershore at shake
    play sound thump
    show mc bingung at mc_right
    mc "woahwoah WOAH-!"
    hide mc bingung
    show jumping at mc_right
    mc "This jump was definitely higher than yesterday's 26 tries! Maybe my flying fish genes have finally awoken!"
    hide jumping
    show mc kaget at mc_right
    mc "mmm.. but a true flying fish should be able to jump at least 6m high.. That was only 10 cm higher and my best was 1 meter before.."
    show mc senyum at mc_right
    mc "eh, oh well, ill get there sooner or later.."
    hide mc senyum
    show jumping at mc_right
    mc "anyway! Goooood morning citizen of riversnips kingdom!"

    hide jumping
    scene ngubekriver1 with dissolve
    "{i}Levelling down with my friends on the ground, I have my best grin on display ready to greet them. They stay longer when I do that.{/i}"
    "{i}My finger gently twirls creating a small friendly swirl against the riverwater.{/i}"
    "{i}One by one, they all turned toward the middle of the river.{/i}"

    mc "good precious morning mr carpado! Morning ms betta! Hello to silly eely billy! and..."

    scene ngubekriver2 
    mc "huh...?"
    stop music fadeout 1.0
    play music goldenfish fadein 2.0 volume 1.0
    "{i}A majestic mysterious fish made its great entrance.{/i}"
  
    scene ngubekriver3
    mc "I dont think I’ve seen you before..."
    "{i}Its beauty was like nothing I've ever seen. Not even in my wildest dreams.. or in the thickest fish encyclopedia with my favorite illustrator in charge.{/i}"

    scene ngubekriver4
    "{i}Stuck in  trance i now realize, that i can only picture its tail now.{/i}"
    mc "Ah! Wait up!!"

    scene rivershoredaybg
    #insert cutscene running through the forest 
    
    play sound forestrun volume 0.2
    "{i}An intense need to follow that mysterious gorgeous fish overwhelms my whole body. My heart is urging me to see more of it. To get closer. To touch it.{/i}"
    scene runforest
    "{i}Before I knew it my feet brought me up in a speed bolt. I ran along the river. Eyes locked onto the mysterious golden fish. 
    The river twisting through patches of tall grass and scattered rocks, forcing me to weave around them as I chase after it. {/i}"
    "{i}Every time I thought I was close enough to reach it… It drifted just a little farther away. 
    My feet stopped me at the edge of the river, where the grassy path came to an abrupt end.{/i}"
    "{i}The water looked dauntingly deeper than I remember. Its brilliant scales shimmered beneath the sunlight, 
    scattering countless rainbow reflections across the water, taunting me to follow its trail.{/i}"
    "{i}I couldn't look away.. Not even if i tried. It felt as though it was calling me not with words, but with something I couldn't explain.{/i}"
    "{i}I couldn't let it escape.{/i}"
    "{i}One step became two, and before I knew it..{/i}"

    scene fallwater
    play sound splash
    "{i}A cold paralyzing splash embraces me tight.{/i}"
    "{i}For a brief moment my vision is surrounded by pitch black. The only guidance a blur flicker of shimmery gold.{/i}"
    scene reachgold with dissolve
    "{i}Yet, for some reason... I'm not at all scared.{/i}"
    "{i}call it practice!{/i}"

    #insert cutscene of a single scale drifting loose from the fish's tail
    scene goldscale2 with dissolve
    "{i}Then— just for a heartbeat— something broke away from it.{/i}"
    scene goldscale1 with dissolve
    "{i}A single scale, spinning loose from its tail, catching the light like a falling star.{/i}"
    scene goldscale3 with dissolve
    "{i}Without thinking, my hand shot out.{/i}"
    play sound sparkle
    scene goldscale4 with dissolve
    "{i}It landed square in my palm. Warm. Impossibly warm for something that just came off a fish underwater.{/i}"
    "{i}I barely had time to look at it before the current dragged me under again.{/i}"

    scene black with fade
    show unknown at npc_left
    unknown "ay ay ay! Where do ya think you're going guppy?! That's the end of the line!"
    stop music fadeout 1.0
    show mc kaget at mc_right
    mc "huh?"

    return
