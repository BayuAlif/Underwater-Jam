label prologue:

    hide mc
    scene prologue_day
    with fade
    play ambience "audio/ambience/ambianceprologue.mp3" loop volume 1.0
    play sound "audio/sfx/wind_soft.mp3" volume 0.3
    
    "{i}Ah, the rivershore.. A serene calming scene adorned by the rustling wind of leaves.{/i}" 
    "{i}Gentle applauses are carried by the trees of forest in celebration for yet another day of the sun's blessing.{/i}" 
    hide mc
    scene cutpro1 with Dissolve(0.5)
    play sound "audio/sfx/bush_rustling.mp3" volume 0.25
    stop ambience fadeout 1.0
    "An absolute perfect scene for{cps=0.5}...{/cps}"

    hide mc
    scene cutpro2 with Dissolve(0.5)
    play music "audio/bgm/prologue_funny_underwater.ogg" fadein 1.0 volume 0.5
    mc "Weee~! For practicing my flying fish jump of course! Haha!"

    "{i}I soared through the sky, my arms and legs held up by the encouraging carry of gravity.{/i}"
    "{i}It felt like I had finally achieved the true nature of those magical fishes.{/i}"
    hide mc
    scene prologue_day
    play sound "audio/sfx/thump.mp3"
    show mc dizzy:
        unpose
        full
        right
        vibrate
    with vpunch

    mc "{bt}Woahwoah WOAH-!{/bt}"
    $ focus()
    show mc excited:
        unpose
        full
        right
        block:
            jumpmc
            pause 1
            repeat

    mc "This jump was definitely higher than yesterday's 26 tries!"
    mc "Maybe my flying fish genes have finally awoken!"

    show mc shock:
        unpose
        full
        right   
        sink
    mc "Mmm... but a true flying fish should be able to jump at least 6m high... That was only 10 cm higher and my best was 1 meter before..."
    show mc default:
        unpose
        full
        right 
        jumpmc 
    mc "Eh, oh well, I'll get there sooner or later..."

    show mc happy:
        unpose
        full
        right
        jumpmc 
    mc "Anyway! {bt}Goooood morning{/bt} citizen of riversnips kingdom!"
    $ focus()

    hide mc
    scene cutpro3 with Dissolve(0.5)
    "{i}Levelling down with my friends on the ground, I have my best grin on display ready to greet them. They stay longer when I do that.{/i}" 
    "{i}My finger gently twirls creating a small friendly swirl against the riverwater. One by one, they all turned toward the middle of the river.{/i}"
    mc "Good precious morning mr carpado! Morning ms betta! Hello to silly eely billy! and..."

    hide mc
    scene cutpro4 with Dissolve(0.5)
    stop music fadeout 5.0
    "{i}A majestic mysterious fish made its great entrance.{/i}"
    mc "Huh...?"

    hide mc
    scene cutpro5 with Dissolve(0.5)
    # play music "audio/bgm/prologue_mysterious.ogg" fadein 1.0 volume 0.5
    play ambience "audio/ambience/mysterious_golden_looking.mp3" loop fadein 1.0 volume 0.5
    mc "I don't think I've seen you before..."
    "{i}Its beauty was like nothing I've ever seen. Not even in my wildest dreams... or in the thickest fish encyclopedia with my favorite illustrator in charge.{/i}"

    hide mc
    scene cutpro6 with Dissolve(0.5)
    "{i}Stuck in trance I now realize, that I can only picture its tail now.{/i}"
    mc "Ah! Wait up!!"

    hide mc
    scene lari1 with Dissolve(0.5)
    with vpunch
    play sound "audio/sfx/wind_hard_2.mp3" volume 0.35
    "{i}Before I knew it my feet brought me up in a speed bolt. I ran along the river. Eyes locked onto the mysterious golden fish.{/i}"
    scene lari2 with Dissolve(0.5)
    "{i}Every time I thought I was close enough to reach it… It drifted just a little farther away.{/i}"
    scene lari3 with Dissolve(0.5)
    "{i}My feet stopped me at the edge of the river, where the grassy path came to an abrupt end.{/i}"
    scene prologue_day with Dissolve(0.5)
    show mc shock:
        unpose
        full
        right
        jumpmc 
    "{i}The water looked dauntingly deeper than I remember.{/i}"
    "{i}But I couldn't look away.. Not even if i tried. It felt as though it was calling me not with words, but with something I couldn't explain.{/i}"
    show mc serious_hu:
        unpose
        full
        right
    "{i}I couldn't let it escape.{/i}"
    "{i}One step became two, and before I knew it..{/i}"

    hide mc
    scene black
    stop ambience
    play sound "audio/sfx/splash.mp3"
    mc "...!"
    show cutpro8 as wave_overlay:
        alpha 0.5
        function WaveShader(amp = 0, melt="both", melt_params=(10.0,1.0,0.1))
    with Dissolve(0.5)
    "{i}A cold paralyzing splash embraces me tight.{/i}"
    play ambience "audio/ambience/unsettling_moment.mp3" loop fadein 0.5
    "{i}For a brief moment my vision is surrounded by pitch black. The only guidance a blur flicker of shimmery gold.{/i}"

    show cutpro9 as wave_overlay:
        alpha 0.5
        function WaveShader(amp = 0, melt="both", melt_params=(10.0,1.0,0.1))
    with Dissolve(0.5) 
    "{i}Yet, for some reason... I'm not at all scared.{/i}"
    show cutpro10 as wave_overlay:
        alpha 0.5
        function WaveShader(amp = 0, melt="both", melt_params=(10.0,1.0,0.1))
    with Dissolve(0.5) 
    "{i}The overwhelming need to see more of it cancels out all emotions{/i}"
    show cutpro11 as wave_overlay:
        alpha 0.5
        function WaveShader(amp = 0, melt="both", melt_params=(10.0,1.0,0.1))
    with Dissolve(0.5) 
    "{i}Then— just for a heartbeat— something broke away from it.{/i}"
    show cutpro12 as wave_overlay:
        alpha 0.5
        function WaveShader(amp = 0, melt="both", melt_params=(10.0,1.0,0.1))
    with Dissolve(0.5) 
    "{i}It landed square in my palm. Warm. Impossibly warm for something that just came off a fish underwater.{/i}"

    stop ambience
    hide mc
    scene black
    play ambience "audio/ambience/underwater_current.mp3" loop fadein 0.5
    "{i}I barely had time to look at it before the current dragged me under again.{/i}"
    show cory anon:
        unpose
        full
        centerright
    anon "ay ay ay! Where do ya think you're going guppy?! That's the end of the line!"

    stop ambience fadeout 1.0
    show mc shock:
        unpose
        full
        right
    mc "huh..?"

    jump chapter1_start
