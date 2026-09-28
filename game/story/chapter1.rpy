label chapter1_start:

    $ current_chapter = 1
    $ current_cycle = "day"
    $ current_area = "riverbed"

    hide mc
    scene ch1_day with Dissolve(0.5)
    show mc shock:
        full
        right
    "An unknown brazen voice pulled me out of a trance."
    $ focus()
    play sound unsettling_moment fadein 1.0
    "my gaze dropped down to be unexpectedly met with a bottomless pit right before my toes, flinching back in instinct."
    mc "...!"

    show ch1_day as wave_overlay:
        alpha 0.25
        function WaveShader(amp = 0, melt="both", melt_params=(10.0,1.0,0.1))
    with Dissolve(0.5)

    show mc shock:
        full
        right

    show cory anon:
        full
        centerright
    anon "You take one more step..."
    anon "...And you'd be a goner."
    "{i}The image of the darkness beyond is burned crisp into my mind.{/i}"
    "{i}The current below twisted slowly as if alive, taunting those who stare long enough.{/i}"

    stop sound fadeout 0.5
    $ focus()
    anon "Not exactly the kinda place ya wanna stumble into.."

    show mc o:
        full
        right
    "{i}I slowly nodded in agreement.{/i}" 

    hide wave_overlay
    hide cory
    hide mc
    with Dissolve(0.5)
    "{i}Before my mind could curiously wonder more to the depth of said cliff, I looked up to the source of voice.{/i}"

    $ focus()
    play music chap_1_day volume 0.5
    show cory talk_hu:
        full
        center
    show mc shock:
        full 
        right
        surprise
    "{i}What I expected was a kind mr human. I was instead met with a fish!{/i}"

    show mc excited:
        full 
        right
        vibrate
    "{i}A Corydoras perhaps? My eyes lit up with unbridled enthusiasm{/i}"
    "{i}I mustn't forget to express my gratitude to those who saved my life.{/i}"
    show mc dance:
        full
        right
        toleft
        dancing
    "{i}I start to wiggle my body in an interpretative dance of gratitude.{/i}"

    show cory unimpressed:
        full 
        center
    cory "{cps=10}...{/cps}"
    show cory unimpressed2:
        full 
        center
    cory "Mane just what the {b}fugu{/b} is you doing..?!"

    show mc actually:
        unpose
        full 
        right
    with moveinright
    mc "{cps=45}Fishes communicate through gestures and and visual as well as colors I'm trying to express my gratitude through-{/cps}"

    show mc shock:
        full
        right
    mc "{cps=20}Wait..{/cps} I just spoke in water..."

    show mc excited:
        full 
        right
        vibrate
    mc "{size=45}ARE YOU GETTING ME, MR FISH?? :D{/size}"

    show cory surprise:
        full
        center
        surprise
    cory "chill the carp out! Yes and yes I'm understanding all the word you saying"

    show mc excited:
        full 
        right
        vibrate
    mc "{bt=10}{cps=45}{size=40}I'M HAVING A CONVERSATION WITH A FIIIISH!!{/size}{/cps}{/bt}"

    "Struck with a thunder of explosive excitement a loud squeak pushed through me. At the same time my mouth is wide open-"
    show mc dizzy:
        full 
        right
        vibrate
    mc "{i}COUGHCOUCHCOUGHBLURURHRGHUGUHRH-!{/i}"

    show cory surprise:
        full
        center
        surprise
    cory "Holy {b}SHRIMP{/b} you still need air huh? I think I have just what ya need"

    show cutchap1 with Dissolve(0.5)
    mc "Huh-? Whoaaah.. I can see better now!"
    cory "You sure do! Good thing river's full of unexpected junks like these"

    show cory smile:
        full
        center
    cory "But.. huh is that a first.. alien guppy of two legs speaks under water.. you a witch?"

    show mc pout:
        full
        right
    mc "am no witch! am fish! it's my dream ever!!"
    show mc o:
        full
        right
    mc "Ah but I couldn't do any of this before... maybe it's because of.."
    show cutchap2 with Dissolve(0.5)
    "{i}My gaze fell down to the translucent scale I didn't realize was clutched tight in my palm the entire time.{/i}" 
    show cutchap3 with Dissolve(0.5)
    stop music fadeout 0.5
    play sound underwater_current
    "{i}Curious, I let go of it just for one millisecond.{/i}"
    "{i}True to my hypothesis, in that frozen moment everything went silent. Save for the tranquil current whirring in my ears.{/i}"
    play music chap_1_day volume 0.5
    show cutchap2 with Dissolve(0.5)
    "{i}But as soon as I made contact with the magical scale. It all became lively. Voices, distant and nearby, fill in the atmosphere.{/i}" 
    "{i}It’s like shopping at a market on a sunny sunday!{/i}"
    "{i}Mr kind fish’s voice became audible again too..{/i}"

    hide cutchap3
    hide cutchap2
    hide cutchap1 
    show cory smile:
        full
        center
    cory "---, –in't ya one step closer to a dream come true, little guppy?"

    show mc shock:
        full
        right
    "{i}This is the power of only one scale. Imagine what a whole fish can do…{/i}"
    show mc default:
        full
        right
        surprise
    mc "Mr kind fish did you see a shiny golden fish that passed by?"
    show cory smile_hu:
        full
        center
    cory "Golden fish? I ain't see no gold, what I saw was straight DIAMOND."
    cory "Visceral beauty struck me tantalized. type shrimp."
    show cory side:
        full
        center
    cory "Didn’t bother following it though. That and ion remember where it went."
    show mc o:
        full
        right
        surprise
    mc "Whuh? Why? :o"
    show cory side_close:
        full
        center
    cory "Ay.. how should I be telling you this.. Pretty things usually mean trouble around here."
    show mc excited:
        full
        right
        surprise
    mc "Yeah! I know! Like blue dragons and and lionfish and-"
    show cory smile:
        full
        center
    cory "{bt}*whistle*{/bt} Well ain't you done your research.."
    show mc happy:
        full
        right
    mc "Mhm! won't make me not touch them though!"
    show cory unimpressed:
        full
        center
    "{i}Mr kind fish sighed.{/i}"
    show cory talk:
        full
        center
    cory "Point is just careful around yeah?"
    cory "And if you don't know your way to mystery fish."
    show cory smile:
        full
        center
    cory "Try exploring, ask around, riverfolks are one friendly neighborhood."
    show mc default:
        full
        right
    mc "Okay! :D"

    hide mc default
    show cory smile_hu:
        full
        center
        surprise
    cory "Alright, good. Have fun, weird guppy! Best prayers to ya adventure"
    cory "..."
    show cory side:
        full
        center
    cory "....."
    show cory side_close:
        full
        center
    cory "........"
    show cory unimpressed:
        full
        center
        sink
    cory "Nay.. who am I kidding.. letting a 1 minute old guppy wander alone? That ain't me…"

    $ focus()

    call chapter1_day_exploration

    call chapter1_night

    call chapter1_dawn

    return

label chapter1_day_exploration:

    hide mc
    scene ch1_day

    $ setup_exploration(
        [
            {
                "id": "bass",
                "name": "Ms. Bass",
                "idle": "bass idle",
                "hover": "bass hover",
                "x": 0.24,
                "y": 0.46,
                "check_y": 0.20
            },
            {
                "id": "uceng",
                "name": "Uceng",
                "idle": "uceng idle",
                "hover": "uceng hover",
                "x": 0.76,
                "y": 0.52,
                "check_y": 0.40
            }
        ],
        {
            "id": "gold_nugget",
            "name": "Golden Rock",
            "idle": "item_gold",
            "hover": "item_gold_hover",
            "x": 0.50,
            "y": 0.82
        }
    )

    label .loop:

        hide mc
        scene ch1_day

        call screen exploration_screen

        $ result = _return

        if result == "bass":

            call bass_interaction
            $ mark_npc_explored("bass")

            jump .loop

        elif result == "uceng":

            call uceng_interaction
            $ mark_npc_explored("uceng")

            jump .loop

        elif result == "item":

            $ collect_exploration_item()

            hide mc
            scene ch1_day
            show goldenrock_hover:
                center
            with moveintop
            "{b}I got a golden rock!{/b}"
            hide goldenrock_hover

            $ focus()
            show mc default:
                full
                right
            "{i}After spending some time exploring the area, I stuffed the last item into my little bag.{/i}"
            mc "..."
            mc "I think that's everything!"

            show cory smile:
                full
                center
            with moveinleft
            cory "find anything okay?"

            show mc happy:
                full
                right
                surprise
            mc "Oh! Hi Mr kind fish.. :D"

            show mc o:
                full
                right
            "I peek through my bag."
            mc "Hmm..."
            mc "Not really."
            mc "...But I found lots of cool stuff!"

            show cory talk:
                full
                center
            "Mr kind fish also takes a peek at my inventory."
            cory "..."
            mc "...?"

            show cory unimpressed:
                full
                center
            cory "Those are literally rocks."

            show mc happy:
                full
                right
                surprise
            mc "Cool rocks!"
            cory "...Half of that's traaa..."

            show mc o:
                full
                right
            mc "traaa?...treasure?"

            show cory side:
                full
                center

            cory "...Sure..."
            show mc happy:
                full
                right
                surprise
            mc "ya! One of a kind treasure indeed mr kind fish :D"

            show cory proud:
                full
                center
                surprise
            cory "also save the adjective would ya? call me cory the great now, guppy!"

            show mc happy:
                full
                right
                surprise
            mc "okay! Mr cory the great now guppy!"

            show cory side:
                full
                center
            cory "ya know what? Cory's fine.."
            $ focus()

            jump .loop

        elif result == "continue":

            $ chapter1_day_done = True
            return

label chapter1_night:

    $ current_cycle = "night"

    hide mc
    scene ch1_dark
    stop music 
    play music chap_1_night

    "{i}The last traces of sunlight slowly disappeared behind the surface.{/i}"

    "{i}For a moment, the riverbed was bathed in a pretty faint blue glow.{/i}"

    "{i}Then... The world went dark.{/i}"

    $ focus()
    show mc o:
        full
        right
    mc "..."
    mc "Mr. Cory?"
    mc "Its getting dark.. is it night already?"

    show cory smile:
        full
        center
    cory "Time flies when yer busy picking up rocks."
    show cory talk:
        full
        center
    cory "Don't wander too far."
    cory "Night's a little different around here."

    show mc dizzy:
        full
        right
    mc "But it's so dark! Is there no light around here..?"
    $ focus()

    hide mc
    scene cutchap4 with Dissolve(0.5)
    "{i}Then suddenly the golden scale in my palm starts to emit a soft blue glow. Giving a small light to those around me{/i}"
    mc "Woah! It wasn't this bright before!"
    cory "well that's.. convenient!"
    cory "Though still, keep your eyes open.. We dont know what might lurk in here"

    call chapter1_night_exploration

    return

label chapter1_night_exploration:

    hide mc
    scene ch1_night

    $ setup_exploration(
        [
            {
                "id": "lele",
                "name": "Lele",
                "idle": "lele idle",
                "hover": "lele hover",
                "xpos": 175,
                "ypos": 315,
                "check_xpos": 480,
                "check_ypos": 265,
                "x": 0.14,
                "y": 0.50,
                "check_y": 0.24
            },
            {
                "id": "gator",
                "name": "Gator",
                "idle": "gator idle",
                "hover": "gator hover",
                "xpos": 855,
                "ypos": 275,
                "check_xpos": 1100,
                "check_ypos": 210,
                "x": 1.08,
                "y": 0.46,
                "check_y": 0.22
            }
        ],
        {
            "id": "ambalabu",
            "name": "Ambalabu",
            "idle": "item_ambalabu",
            "hover": "item_ambalabu_hover",
            "xpos": 630,
            "ypos": 715,
            "x": 0.42,
            "y": 0.94
        }
    )

    label .loop:

        hide mc
        scene ch1_night

        call screen exploration_screen

        $ result = _return

        if result == "lele":

            call lele_interaction
            $ mark_npc_explored("lele")

            jump .loop

        elif result == "gator":

            call gator_interaction
            $ mark_npc_explored("gator")

            jump .loop

        elif result == "item":

            $ collect_exploration_item()

            hide mc
            scene ch1_night

            $ focus()
            show cory surprise:
                full
                center

            show mc o:
                full
                right

            cory "...!"
            cory "is that what i think it is??"

            mc "what is it mr cory?"

            show cory disrespect:
                full
                center
            cory "eh, just a toy.. A very popular one"

            show cory smile_hu:
                full
                center
            cory "I might know who might like this... hah!"
            $ focus()

            jump .loop

        elif result == "continue":

            $ chapter1_night_done = True
            return

label chapter1_dawn:

    hide mc
    scene ch1_night

    $ focus()
    show cory talk:
        full
        center
    cory "So, what've we got from allat?"

    show mc default:
        full
        right
    mc "North!"

    show mc happy:
        full
        right
    mc "They all said north!"

    show cory smile:
        full
        center
    cory "north eh? The direction where the river ends.."
    cory "...Guess we've got our answer."
    "{i}I looked toward the distant current. The water there flowed faster. The sunlight barely reached it.{/i}"

    show cory talk:
        full
        center
    cory "but uhh guppy.. ain't your parents worried..?"
    cory "it's been a full day since we got here.. ya don't wanna go back for a bit?"

    show mc serious_hu:
        full
        right
    mc "mm? No it's fine! My parents allow me to come back home whenever I want!"
    mc "I don't think I'm coming back before I see that fish again.."

    show mc happy:
        full
        right
    mc "aren't they just the kindest? To give freewill at my age!"

    show cory side:
        full
        center
    cory "free will ay..? Sounds worrying to me."
    show cory talk:
        full
        center
    cory "but you're right about one thing, guppy"
    show cory smile_hu:
        full
        center
    cory "we ain't going back until we catch that damn fish together!"

    show mc excited:
        full
        right
    mc "Let's go!"

    show cory fond:
        full
        center
    cory "Just don't make me save ya twice."
    $ focus()

    hide mc
    scene black with dissolve

    "END OF CHAPTER 1"

    jump chapter2_start
