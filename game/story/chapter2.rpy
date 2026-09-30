label chapter2_start:

    $ current_chapter = 2
    $ current_cycle = "day"
    $ current_area = "northern_current"

    hide mc
    scene ch2_day with Dissolve(0.5)
    play music chap_2_day volume 0.5
    "The river flowed faster, slowly giving way to larger stones."
    "The sunlight above grew softer, hiding themself behind layers of drifting water plants as we continue to swim."
    $ focus()
    show mc o:
        full
        unpose
    show mc o:
        unpose
        right
        toleft
        walkloop
    with moveinright
    show cory netral:
        full
        unpose
    show cory netral:
        unpose
        center
        toleft
        walkloop
    with moveinright
    mc "Have you been to the sea mr. Cory?"

    show cory talk:
        unpose
        full
        center
        toleft
        walkloop
    cory "Sea? Nah that's waaay past my territory"
    cory "Nearest I've been at is meters before saltwater and freshwater collides"

    show cory smile:
        unpose
        full
        center
        toleft
        walkloop
    cory "Besides, I'm a freshwater fish guppy, one step into sea, and I explode"

    show mc shock:
        unpose
        full
        right
        toleft
        vibrate
    mc "EXPLODE?? NOOO MR CORY PLEASE DONT EXPLODE!! I LEFT MY GLUE AT HOME D:"

    show cory smile:
        unpose
        full
        center
        toleft
    cory "Ay easy, easy! I won't be exploding now..!"

    show cory side:
        unpose
        full
        center
        toleft
    cory "{cps=30}{size=24}Ah but.. that woulda mean we have to part ways-{/size}{/cps}"

    show mc o:
        unpose
        full
        right
        toleft
    mc "Woah look ahead! that's a lotta shoal!"

    show cory talk:
        unpose
        full
        center
        toleft
    cory "Huh..?"

    "Several tens of fishes crowd at what looks like a border built out of tall reefs, a small cave sits in the middle where a speckle of colorful creature stands firm guarding the entrance."

    show cory talk:
        unpose
        full
        center
        toleft
    cory "That's the border of salt fresh.."
    cory "Itsa always been a busy place but this amount is unnatural..."

    show mc o:
        unpose
        full
        right
        toleft
        surprise
    mc "Is that a shrimp guarding the cave hole?"

    "I squint my eyes into thin lines to take a better look on the eccentric colored guardian right before the cave's entrance."

    show mc excited:
        unpose
        full
        right
        toleft
        block:
            surprise
            pause 1
            repeat

    mc "Oh oh! That's a mantis shrimp!! He looks really tough!"

    show mc excited:
        full
        unpose
        right
        toleft

    mc "Mr cory can we give it a handshake? :D"

    show cory unimpressed2:
        unpose
        full
        center
        toleft
    cory "Nuh uh! unless you want your hand gone for good"

    show cory talk:
        unpose
        full
        center
        toleft
    cory "But eh, that mantis shrimp.. He had been around for a good while"
    cory "He's quite friendly, it's hard to believe if the fuss is his doing."

    show mc serious_hu:
        unpose
        full
        right
    mc "really?! You know him?"

    show cory talk_hu:
        unpose
        full
        center
        toleft
    cory "Yeah, But I say we ask around first to know what the crowd's about.."

    show mc happy:
        full
        unpose
        right
        toleft
        surprise
    mc "Sir yes sir mr cory!"

    show cory fond:
        unpose
        full
        center
        toleft
    cory "Heh, atta fish"
    $ focus()

    call chapter2_day_exploration
    call chapter2_night_start

    return


label chapter2_day_exploration:

    $ current_cycle = "day"
    $ current_area = "northern_current"

    hide mc
    scene ch2_day

    $ setup_exploration(
        [
            {
                "id": "salmon",
                "name": "Mrs. Salmon",
                "idle": "salmon idle",
                "hover": "salmon hover",
                "xpos": 1220,
                "ypos": 210,
                "check_xpos": 1445,
                "check_ypos": 160,
                "x": 0.83,
                "y": 0.28,
                "check_y": 0.15
            },
            {
                "id": "arowana",
                "name": "Mr. Wana",
                "idle": "arowana idle",
                "hover": "arowana hover",
                "xpos": 220,
                "ypos": 240,
                "check_xpos": 472,
                "check_ypos": 180,
                "x": 0.16,
                "y": 0.35,
                "check_y": 0.18
            }
        ],
        {
            "id": "tiny_krill",
            "name": "Tiny Krill",
            "idle": "item_tiny_krill",
            "hover": "item_tiny_krill_hover",
            "xpos": 815,
            "ypos": 740,
            "x": 0.48,
            "y": 0.75
        }
    )

    label .loop:

        hide mc
        scene ch2_day

        call screen exploration_screen

        $ result = _return

        if result == "salmon":
            call salmon_interaction
            $ mark_npc_explored("salmon")
            jump .loop

        elif result == "arowana":
            call arowana_interaction
            $ mark_npc_explored("arowana")
            jump .loop

        elif result == "item":
            $ collect_exploration_item()
            call chapter2_tiny_krill
            jump .loop

        elif result == "continue":
            $ chapter2_day_done = True
            return


label chapter2_tiny_krill:

    $ focus()
    show mc happy:
        unpose
        full
        right
        surprise
    with moveinright
    mc "A tiny krill!"

    show krill:
        full
        centerleft
        medium
    with moveinbottom
    tinykrill "Eah!"

    show cory disrespect:
        unpose
        full
        center
    with moveinleft
    cory "Heh.. you could say it's.. one in a krillion"

    show krill:
        full
        centerleft
        medium
        surprise
    tinykrill "Your joke sucks ass!"

    show cory unimpressed:
        unpose
        full
        center
    cory "...."
    cory "... I say we feed that thing to a fish, guppy"

    show mc sad_hu:
        unpose
        full
        right
        sink
    mc "Aw shucks, do we really have to krill it mr cory? :("

    show krill:
        full
        left
        medium
        vibrate
    tinykrill "Suffer in eternal torment both of you!"

    $ add_item("tiny_krill")
    hide krill with dissolve
    "{b}I obtained a tiny krill.{/b}"
    $ focus()
    return


label chapter2_night_start:

    $ current_cycle = "night"
    $ current_area = "northern_current"

    hide mc
    scene ch2_night
    with fade
    play music chap_2_night volume 0.5

    $ setup_exploration(
        [
            {
                "id": "ghostfish",
                "name": "Ghostfish",
                "idle": "ghost idle",
                "hover": "ghost hover",
                "x": 0.321,
                "y": 0.127
            },
            {
                "id": "mantis",
                "name": "Mantis Shrimp",
                "idle": "shrimp idle",
                "hover": "shrimp hover",
                "x": 0.803,
                "y": 0.242
            }
        ],
        {
            "id": "coal_tar",
            "name": "Coal Tar",
            "idle": "item_coal",
            "hover": "item_coal_hover",
            "x": 0.631,
            "y": 0.577
        }
    )

    label .loop:

        hide mc
        scene ch2_night

        call screen exploration_screen

        $ result = _return

        if result == "ghostfish":
            call ghostfish_interaction
            if _return != "unexplored":
                $ mark_npc_explored("ghostfish")
            jump .loop

        elif result == "item":
            $ collect_exploration_item()
            call chapter2_coal_tar
            jump .loop

        elif result == "mantis":
            call mantis_interaction

            if chapter2_mantis_done:
                $ mark_npc_explored("mantis")
                if exploration_complete():
                    jump chapter2_ending

            jump .loop

        elif result == "continue":
            $ chapter2_night_done = True

            if exploration_complete():
                jump chapter2_ending

            jump .loop

    return


label chapter2_coal_tar:

    $ focus()
    show mc o:
        unpose
        full
        duo_right
    mc "Mr. Cory, do you know what this black lump is?"

    show cory talk_hu:
        unpose
        full
        duo_left
    cory "Mmmn.. no clue."

    show cory unimpressed2:
        unpose
        full
        duo_left
    cory "Almost looks like poo to me, you better drop that thing guppy."

    show mc shock:
        unpose
        full
        duo_right
    mc "Yuck! it smells… weird."

    call ghost_coal_tar_encounter

    show cory upset:
        unpose
        full
        duo_left
    cory "What the eel even was that?!"
    cory "Straight out of deep sea I swear!"

    $ focus()
    $ add_item("coal_tar")

    "I obtained: a mysterious stinky black lump."

    return


label chapter2_ending:

    $ focus()
    show mc excited:
        full
        right
        unpose
    show mc excited:
        unpose
        walkloop
    mc "onward! to the sea we go!"

    show shrimp laugh:
        full
        unpose
        offscreenleft
    show shrimp laugh:
        unpose
        centerleft
        walkloop
    with moveinleft
    shrimp "KAKAKA! to the sea!"

    show cory netral:
        full
        unpose
        offscreenleft
    show cory netral:
        unpose
        rightish
        walkloop
    cory "..."

    show cory side:
        unpose
        full
        right
    with move
    cory "......"

    show cory fond:
        unpose
        full
        right
    cory "shrimp.. I leave the guppy's safety to ya alright?"
    cory "Shrimps have better resistance in freshwater don't they?"

    if has_item("saltwater_survival_device"):
        show cory side:
            unpose
            full
            right
        cory "And we only have one 50%% effective saltwater device.."

    show mc shock:
        unpose
        full
        right
    mc "...!!"

    show shrimp default:
        unpose
        full
        centerleft
    show cory side:
        unpose
        full
        rightish
    with move
    shrimp "yes of course! Protect i shall. it is my utmost duty to protect!"

    show mc pout:
        unpose
        full
        right
    mc "no!"

    show cory side_close:
        unpose
        full
        rightish
    cory "guppy.."

    show mc pout:
        unpose
        full
        right
    mc "no no no! I'm not going anywhere without Mr. Cory!!"

    show cory talk:
        unpose
        full
        rightish
    cory "guppy, I'd dry the sea to come along but-"

    show mc pout:
        unpose
        full
        right
    mc "mr shrimp cant you protect him? With your punches!"
    mc "punch all the freshwater away from mr.cory!"

    show shrimp sepet:
        unpose
        full
        centerleft
    shrimp "..."

    show shrimp default:
        unpose
        full
        centerleft
    shrimp "I'm afraid I cannot, my dear comrade!"
    shrimp "punching water is akin to fighting a shadow…"

    show mc shock:
        unpose
        full
        right
    mc "no.."

    show mc holdcry:
        unpose
        full
        right
    mc "but you promised… *sniffle*"
    mc "that we'd catch that fish together...."

    show cory side_close:
        unpose
        full
        rightish
    cory "....."
    cory "I'm.. God terribly. sorry guppy.."
    cory "I didn't think far enough that it'd reach the sea.."

    show cory side:
        unpose
        full
        rightish
        sink
    cory "...I'm afraid that I'm a fraud..."

    show shrimp smile:
        unpose
        full
        centerleft
    shrimp "that makes a good rhyme!"

    "The fish scale in my bag suddenly glows into a blinding sparkly light for one second."
    "Painting the three of us in gold, before it dims once more."
    "But something felt different."

    show mc o:
        unpose
        full
        right
    mc "mm?"

    show cory surprise:
        unpose
        full
        rightish
        surprise
    cory "I-! Huh? I feel different!"

    show mc o:
        unpose
        full
        right
    mc "Try stepping in the saltwater, Mr.Cory!"

    show cory side:
        unpose
        full
        rightish
    cory "Are ya sure..? What if it's just my imagination?"

    show mc happy:
        unpose
        full
        right
    mc "trust me!"

    show cory side_close:
        unpose
        full
        rightish
    cory "Alright… here goes nothin.."

    "Mr Cory hesitantly takes one step into where freshwater and saltwater collide with one eye closed."

    show cory surprise:
        unpose
        full
        rightish
        surprise
    cory "Holy mother of sea…!"

    show mc shock:
        unpose
        full
        right
    mc "d-does it hurt-"

    "Before I can finish my line I was swept into a spinning hug."

    show cory proud_hu:
        unpose
        full
        rightish
        surprise
        vibrate
    cory "I CAN'T BELIEVE IT!! I'M IN SALTWATER GUPPY!!"

    show mc excited:
        unpose
        full
        right
    mc "YAAAAAY"

    "Mr shrimp then lifts the both of us with its strong claws spinning us all into a dizzying spiral."

    show shrimp laugh:
        unpose
        full
        centerleft
    shrimp "KAKAKA! WAHOO!"

    show cory upset:
        unpose
        full
        rightish
        vibrate
    cory "{sc}THAT'S WAY TOO FAAAUUUAASHHTT SHRIMP PUT US DOOOOWN{/sc}"

    show mc excited:
        unpose
        full
        right
    mc "YIPEEEEE FAAASTEEER!!"

    show shrimp surprise:
        unpose
        full
        centerleft
    shrimp "Ah! My apologies, comrades! And congratulations to Mr. Cory!"

    "Mr shrimp then carefully puts us down."

    show shrimp laugh:
        unpose
        full
        centerleft
    shrimp "With this, we can now safely travel amongst the seas! KAKAKA!"

    show cory unimpressed2:
        unpose
        full
        rightish
        vibrate
    cory "ngnuuurhhhehhkk"

    show mc dizzy:
        unpose
        full
        right
    mc "oaooaooouhh yaaaah lets meef the… crustashan empeees.."

    show shrimp smile:
        unpose
        full
        centerleft
    shrimp "Don't worry, my dizzy lieges! I'll carry the both of you until you regain your ground! Or.. your water!"

    $ focus()
    hide mc
    scene black with dissolve

    menu:
        "Continue to Chapter 3":
            jump chapter3_start
