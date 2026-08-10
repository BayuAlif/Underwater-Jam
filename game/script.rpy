# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("gulugulu")
define f1u = Character("???")
define f2 = Character("Fihfriend2")
define f3 = Character("Fihfriend3")

image jumping:
    "testmchappy"
    yalign 1.0
    easeout 0.4 yoffset -50
    easein 0.4 yoffset 0
    repeat

screen riverside_click():
    add "rivershoredaybg"
    modal True

    imagebutton auto "fihfriend2_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "fihfriend2")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("fihfriendsporty")

    imagebutton auto "fihfriend3_%s":
        hovered SetVariable("screen_tooltip", "fihfriend3")
        unhovered SetVariable("screen_tooltip", "")
        focus_mask True
        action Jump("fihfriendgoth")


label start:
    play sound happy
    scene rivershorebg
    "{i}Ah, the rivershore. A serene calming scene adorned by the rustling wind of leaves.{/i}" 
    "{i}Gentle applauses are carried by the trees of forest in celebration for yet another day of the sun’s blessing..{/i}"
   
    scene rustlingbush
    "{i}An absolute perfect scene for….{/i}"

    scene flyingfish
    mc "Weee~! For practicing my flying fish jump of course! Haha!"

    "{i}I soared through the sky, my arms and legs held up by the encouraging carry of gravity.{/i}"
    "{i}It felt like I had finally achieved the true nature of those magical fishes.{/i}"

    scene rivershoredaybg
    hide testmcdefault
    show jumping
    mc "woahwoah WOAH-!"
    mc "This jump was definitely higher than yesterday's 26 tries! Maybe my flying fish genes have finally awoken!"
    hide jumping
    show testmcsad
    mc "mmm.. but a true flying fish should be able to jump at least 6m high.. That was only 10 cm higher and my best was 1 meter before.."
    show testmchappy
    mc "eh, oh well, ill get there sooner or later.."
    mc "anyway! Goooood morning citizen of riversnips kingdom!"

    scene ngubekriver1
    "{i}Levelling down with my friends on the ground, I have my best grin on display ready to greet them. They stay longer when I do that.{/i}"
    "{i}My finger gently twirls creating a small friendly swirl against the riverwater.{/i}"
    "{i}One by one, they all turned toward the middle of the river.{/i}"

    mc "good precious morning mr carpado! Morning ms betta! Hello to silly eely billy! and..."

    scene ngubekriver2
    mc "huh...?"
    "{i}A majestic mysterious fish made its great entrance.{/i}"
  
    scene ngubekriver3
    mc "I dont think I’ve seen you before..."
    "{i}Its beauty was like nothing I've ever seen. Not even in my wildest dreams.. or in the thickest fish encyclopedia with my favorite illustrator in charge.{/i}"

    scene ngubekriver4
    "{i}Stuck in  trance i now realize, that i can only picture its tail now.{/i}"
    mc "Ah! Wait up!!"

    scene rivershoredaybg
    play sound melancholy
    #insert cutscene running through the forest 
    
    #insert sfx runthroughforest
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
    #sfxsplash
    "{i}A cold paralyzing splash embraces me tight.{/i}"
    "{i}For a brief moment my vision is surrounded by pitch black. The only guidance a blur flicker of shimmery gold.{/i}"
    scene reachgold
    "{i}Yet, for some reason... I'm not at all scared.{/i}"
    "{i}call it practice!{/i}"

    #insert cutscene of a single scale drifting loose from the fish's tail
    scene goldscale1
    "{i}Then— just for a heartbeat— something broke away from it.{/i}"
    scene goldscale2
    "{i}A single scale, spinning loose from its tail, catching the light like a falling star.{/i}"
    scene goldscale3
    "{i}Without thinking, my hand shot out.{/i}"
    #sfx small chime/glimmer sound
    scene goldscale4
    "{i}It landed square in my palm. Warm. Impossibly warm for something that just came off a fish underwater.{/i}"
    "{i}I barely had time to look at it before the current dragged me under again.{/i}"

    scene black
    f1u "ay ay ay! Where do ya think you're going guppy?! That's the end of the line!"
    mc "huh?"

    
label riverside_click:
    scene rivershoredaybg
    call screen riverside_click
    return

label fihfriendsporty:
    show fihfriend2_idle
    f2 "hi there!"
    jump riverside_click

label fihfriendgoth:
    show fihfriend3_idle
    f3 "greetings..."
    jump riverside_click


    return
