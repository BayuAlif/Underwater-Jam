label chapter2_start:

    $ current_chapter = 2
    $ current_cycle = "day"
    $ current_area = "northern_current"

    hide mc
    scene ch2_day with Dissolve(0.5)
    play music chap_2_day volume 0.5
    "The river flowed faster, slowly giving way to larger stones."
    "The sunlight above grew softer, hiding themself behind layers of drifting water plants."
    $ focus()
    show mc o:
        offscreenright
        full
        right
        walkto(right)
        toleft
        walkloop
    with moveinright
    show cory side:
        offscreenright
        full
        center
        walkto(center)
        toleft
        walkloop
    with moveinright
    mc "Have you been to the sea mr. Cory?"

    show cory talk:
        full
        center
        toleft
        walkloop
    cory "Sea? Nah that's waaay past my territory"
    cory "Nearest I've been at is meters before saltwater and freshwater collides"

    show cory smile_hu:
        full
        center
        walkloop
    cory "Besides, I'm a freshwater fish guppy, one step into sea, and I explode"

    show mc shock:
        full
        right
        toleft
        walkloop
        vibrate
    mc "EXPLODE?? NOOO MR CORY PLEASE DONT EXPLODE!! I LEFT MY GLUE AT HOME D:"

    show cory smile:
        full
        center
        toleft
        walkloop
    cory "Ay easy, easy! I won't be exploding now..!"

    show cory side:
        full
        center
        toleft
        walkloop
    cory "{cps=30}{size=24}Ah but.. that woulda mean we have to part ways-{/size}{/cps}"

    show mc o:
        full
        right
    mc "Woah look ahead! that's a lotta shoal!"

    show cory talk:
        full
        center
        toleft
        walkloop
    cory "Huh..?"

    "Several tens of fishes crowd at what looks like a border built out of tall reefs, a small cave sits in the middle where a speckle of colorful creature stands firm guarding the entrance."

    show cory talk_hu:
        full
        center
    cory "That's the border of salt fresh.."
    cory "Itsa always been a busy place but this amount is unnatural..."

    show mc o:
        full
        right
        surprise
    mc "Is that a shrimp guarding the cave hole?"

    "I squint my eyes into thin lines to take a better look on the eccentric colored guardian right before the cave's entrance."

    show mc excited:
        full
        right
        block:
            jumpmc
            pause 1
            repeat
    mc "Oh oh! That's a mantis shrimp!! He looks really though!"

    show mc excited:
        full
        right
    mc "Mr cory can we give it a handshake? :D"

    show cory unimpressed2:
        full
        center
    cory "Nuh uh! unless you want your hand gone for good"

    show cory talk:
        full
        center
    cory "But eh, that mantis shrimp.. He had been around for a good while"
    cory "He's quite friendly, it's hard to believe if the fuss is his doing."

    mc "really?! You know him?"

    show cory talk_hu:
        full
        center
    cory "Yeah, But I say we ask around first to know what the crowd's about.."

    show mc happy:
        full
        right
        surprise
    mc "Sir yes sir mr cory!"

    show cory fond:
        full
        center
    cory "Heh, atta fish"
    $ focus()

    call chapter2_day_exploration
    jump chapter2_night_start

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
        full
        right
        surprise
    mc "A tiny krill!"

    show krill:
        full
        left
        medium
    tinykrill "Eah!"

    show cory disrespect:
        full
        center
    cory "Heh.. you could say it's.. One in a krillion"

    show krill:
        full
        left
        medium
        surprise
    tinykrill "{size=20}Your joke sucks ass!{/size}"

    show cory unimpressed:
        full
        center
    cory "...."
    cory "... I say we feed that thing to a fish, guppy"

    show mc shock:
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
    "I obtained a tiny krill"
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
            $ mark_npc_explored("ghostfish")
            jump .loop

        elif result == "item":
            $ collect_exploration_item()
            call chapter2_coal_tar
            jump .loop

        elif result == "mantis":
            call mantis_interaction
            $ mark_npc_explored("mantis")
            if chapter2_mantis_done:
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
    show mc o at mc_center_left
    mc "Mr. Cory, do you know what this black lump is?"

    show cory talk_hu at cory_center_right
    cory "Mmmn.. no clue."

    show cory unimpressed2 at cory_center_right
    cory "Almost looks like poo to me, you better drop that thing guppy."

    show mc shock at mc_center_left
    mc "Yuck! it smells… weird."

    show ghost deadpan at npc_right
    ghost "You shouldn't be carrying things you don't understand."

    show cory smile_hu at cory_left
    cory "Yeah.. that's right guppy.."
    cory "Finally, Some self preservation in ya!"

    show mc o at mc_left
    mc "That.. wasn’t me…"

    "The water around us suddenly grows eerily still."
    "Faint glow pair of eyes emerges from the darkness."

    show cory surprise at cory_left
    cory "GYAAAAAAA—"

    "Mr Cory jumped and immediate cower behind my back with a loud screech"

    show mc o at mc_left
    mc ":o"

    show mc excited at mc_left
    mc "Woah! What are you?"

    show ghost default at npc_right
    ghost "A fish."

    show mc pout at mc_left
    mc "I can see that."

    ghost "Then you needn’t know more."

    show mc o at mc_left
    mc "Why are you here… fish?"

    show ghost side at npc_right
    ghost "You were meant to find me."

    show ghost close at npc_right
    ghost "But this second is not the time"
    ghost "We shall meet again.. very soon."

    show ghost side at npc_right
    ghost "Or perhaps.. we have met before."

    show mc happy at mc_left
    mc "Okay! Looking forward to meeting you again, fish!"
    mc "Mr Cory you can come out, it's fine now."

    show cory upset at cory_left
    cory "What the eel even was that?!"
    cory "Straight out of deep sea I swear!"

    $ focus()
    $ add_item("coal_tar")
    "I obtained: a mysterious stinky black lump"
    return

label chapter2_ending:
    $ focus()
    show mc excited at mc_left
    mc "onward! to the sea we go!"

    show shrimp laugh at npc_right
    shrimp "to the sea!"

    show cory side at cory_left
    cory "..."

    show cory side_close at cory_left
    cory "......"

    show cory fond at cory_left
    cory "imp.. I leave the guppy's safety to ya alright?"

    show cory smile_hu at cory_left
    cory "Shrimps have better resistance in freshwater don't they?"

    if has_item("saltwater_survival_device"):
        cory "And we only have one 50% effective saltwater device.."

    show mc shock at mc_left
    mc "...!!"

    show shrimp default at npc_right
    shrimp "yes of course! Protect i shall. it is my utmost duty to protect!"

    show mc pout at mc_left
    mc "no!"

    show cory side_close at cory_left
    cory "guppy.."

    show mc pout at mc_left
    mc "no no no! I’m not going anywhere without Mr. Cory!!"

    show cory talk at cory_left
    cory "guppy, I’d dry the sea to come along but-"

    show mc pout at mc_left
    mc "mr shrimp cant you protect him? With your punches!"
    mc "punch all the freshwater away from mr.cory!"

    show shrimp sepet at npc_right
    shrimp "..."

    show shrimp default at npc_right
    shrimp "I'm afraid I cannot, my dear comrade!"
    shrimp "punching water is akin to fighting a shadow…"

    show mc shock at mc_left
    mc "no.."

    show mc holdcry at mc_left
    mc "but you promised… *sniffle*"
    mc "that we'd catch that fish together...."

    show cory side_close at cory_left
    cory "....."
    cory "I’m.. God terribly. sorry guppy.."
    cory "I didn't think far enough that it'd reach the sea.."

    show cory side at cory_left
    cory "...I’m afraid that I’m a fraud..."

    show shrimp smile at npc_right
    shrimp "that makes a good rhyme!"

    "The fish scale in my bag suddenly glows into a blinding sparkly light for one second. Painting the three of us in gold, before it dims once more. But something felt different"

    show mc o at mc_left
    mc "mm?"

    show cory surprise at cory_left
    cory "I-! Huh? I feel different!"

    show mc o at mc_left
    mc "Try stepping in the saltwater, Mr.Cory!"

    show cory side at cory_left
    cory "Are ya sure..? What if it's just my imagination?"

    show mc happy at mc_left
    mc "trust me!"

    show cory side_close at cory_left
    cory "Alright…"

    "Mr Cory hesitantly takes one step into where freshwater and saltwater collide with one eye closed."

    show cory surprise at cory_left
    cory "Holy mother of sea…!"

    show mc shock at mc_left
    mc "d-does it hurt-"

    "Before I can finish my line I was swept into a spinning hug"

    show cory proud at cory_left
    cory "I CAN'T BELIEVE IT!! I'M IN SALTWATER GUPPY!!"

    show mc excited at mc_left
    mc "YAAAAAY"

    "Mr shrimp then lifts the both of us with its strong claws spinning us all into a dizzying spiral"

    show shrimp laugh at npc_right
    shrimp "KAKAKA! WAHOO!"

    show cory upset at cory_left
    cory "THAT’S WAY TOO FAAAUUUAASHHTT SHRIMP PUT US DOOOOWN"

    show mc excited at mc_left
    mc "YIPEEEEE FAAASTEEER!!"

    show shrimp surprise at npc_right
    shrimp "Ah! My apologies, comrades! And congratulations to Mr. Cory!"

    "Mr shimp then carefully puf us down"

    show shrimp laugh at npc_right
    shrimp "With this, we can now safely travel amongst the seas! KAKAKA!"

    show cory unimpressed at cory_left
    cory "ngnuuurhhhehhkk"

    show mc dizzy at mc_left
    mc "oaooaooouhh yaaaah lets meef the… crustashan empeees.."

    show shrimp smile at npc_right
    shrimp "Don’t worry, my dizzy lieges! I’ll carry the both of you until you regain your ground! Or.. your water!"

    $ focus()
    hide mc
    scene black with dissolve

    "END OF CHAPTER 2"

    jump chapter3_start
