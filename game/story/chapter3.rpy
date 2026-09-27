init python:
    cory = Character("Cory", color="#ffffff", image="cory")
    scyllarus = Character("Scyllarus", color="#ffffff", image="scy")
    seabunny = Character("Sea Bunny", color="#ffffff", image="bunny")
    hawk = Character("Gran Hawk", color="#ffffff", image="hawk")
    dun = Character("Dunge", color="#ffffff", image="dunge")
    emp = Character("Crustacean Empress VIII", color="#ffffff", image="teto")
    gob = Character("Goby", color="#ffffff")
    gator = Character("Gator", color="#ffffff", image="gator")

    crustaceans = Character("Crustaceans", color="#ffffff")
    crowd = Character("Crowd", color="#ffffff")
    emp_mc = Character("Empress & [player_name]", color="#ffffff")
    unknown_speaker = Character("???", color="#ffffff")

transform npc_left:
    xanchor 0.30
    xpos 0.28
    yanchor 1.0
    ypos 1.0
    zoom 0.70

default F1 = cory
default F2 = scyllarus
default F3 = seabunny

default has_rainbow_algae = False
default gave_algae_to_seabunny = False
default has_red_seaweed = False
default clue_golden_scale = False
default clue_empress_weakness = False
default ch3_seabunny_helped = False
default ch3_visited_seabunny = False
default ch3_visited_turtle = False
default ch3_dunge_defeated = False
default ch3_empress_defeated = False
default ch3_chapter_complete = False

init python:
    renpy.image(("cory", "talk_smile_hu"), "images/characters/cory/CoryTalkSmileHU.png")
    renpy.image(("cory", "fond_smile"), "images/characters/cory/CoryFondSmile_.png")
    renpy.image(("cory", "side_close"), "images/characters/cory/CorySideClose_.png")
    renpy.image(("cory", "unimpressed1"), "images/characters/cory/CoryOhiounimpressed1_.png")
    renpy.image(("cory", "talk_netral"), "images/characters/cory/CoryTalkNetral_.png")
    renpy.image(("cory", "talk_netral_hu"), "images/characters/cory/CoryTalkNetralHU.png")
    renpy.image(("cory", "hurt"), "images/characters/cory/CoryUpsetHU.png")

    renpy.image(("scy", "default_om"), "images/npc/chapter2/Mantis/ScyDefaultOM_.png")
    renpy.image(("scy", "pout"), "images/npc/chapter2/Mantis/ScySepet.png")
    renpy.image(("scy", "excited"), "images/npc/chapter2/Mantis/ScyLaugh.png")

    renpy.image(("dun", "default"), "images/npc/chapter3/dunge/DunDefault.png")
    renpy.image(("dun", "mad"), "images/npc/chapter3/dunge/DunMad.png")
    renpy.image(("dun", "smile"), "images/npc/chapter3/dunge/DunSmile.png")
    renpy.image(("dun", "yeesh"), "images/npc/chapter3/dunge/DunYeesh.png")

    renpy.image(("gob", "default"), "images/npc/chapter3/GOBY/TetoGunSmirk.png")
    renpy.image(("item_algae",), "images/items/chapter3/algae_idle.png")
    renpy.image(("item_algae_hover",), "images/items/chapter3/algae_hover.png")
    renpy.image(("item_seaweed",), "images/items/chapter3/seaweed_idle.png")
    renpy.image(("item_seaweed_hover",), "images/items/chapter3/seaweed_hover.png")

screen ch3_boss_negotiation_timer(timeout=8.0):
    timer timeout action Jump("ch3_boss_negotiate_mc_timeout")

label chapter3_start:
    jump ch3_start

label ch3_start:
    $ current_chapter = 3
    $ current_cycle = "day"

    hide mc
    scene ch3_day with Dissolve (0.5)
    play music chap_3_day volume 0.5

    "The sea fills my line of sight with overwhelmingly bright pretty colors."
    "My gaze erratically jumps from one color to another as we continue to swim further."
    "From parrot fishes, sparkly elvis worms to rainbow open brain corals. There's way too many stuff to focus on!"
    $ focus ()

    show mc excited:
        full
        unpose
        offscreenright
    show mc excited:
        right
        walkto(right)
        toleft
        block:
            jumpmc
            pause 1
            repeat
    with moveinright
    show cory smile_hu:
        full
        unpose
        offscreenright
    show cory smile_hu:
        center
        walkto(center)
        toleft
        walkloop
    with moveinright
    cory "Heh.. Yer eyes been flying everywhere since we got here"
    cory "Don't ya get dizzy?"
    mc "Ohmigosh!! Is that coral dancing?! Did you see that, Mr Cory?! I think that's the Spanish dancer!"

    show cory fond:
        full
        center
        toleft
    cory "So excited, can't even hear me huh.."

    show cory smile_hu:
        full
        center
        toleft
    cory "Though I must admit that this is some otherworldly beauty going on"

    show cory smile_hu:
        full
        leftish
    with move
    show shrimp proud:
        full
        unpose
        offscreenleft
    show shrimp proud:
        centerright
        walkloop
    with moveinleft
    scy "Right?! Feast your eyes upon the neverending beauty that is sea!"

    show cory side:
        full
        leftish
    cory "To think your empress' been gatekeepin all this.. kinda messed up to think about"

    show shrimp sepet:
        full 
        centerright
    scy "But she's not entirely wrong either! Most fish criminals are freshwater types!"

    show cory side_close:
        full
        leftish
    cory "Ay.. Sure, being careful is one thing.."
    cory "But pushing that stereotype into every freshwater is a whole different thing"

    show shrimp default_om:
        full
        centerright
    scy "Mm.. well! It's the daughter that just got promoted into empress!"  
    scy "The former queen that saved my life had dethroned herself not long ago"
    scy "So she's still trying out new rules that feel fitting!"

    show cory unimpressed:
        full
        leftish
    cory "New ruler's a kid? That checks out.."

    show cory talk:
        full
        leftish
    cory "About time somefish teaches em a lesson then"

    show shrimp surprise:
        full
        centerright
        surprise
    scy "....!"
    scy "Wait! Why are you crying comrade?!"

    show cory surprise:
        full
        leftish
        surprise
    cory "Huh? I ain't crying! Are you guppy?"

    show mc shock:
        full
        unpose
        right
        toleft
    mc "Me? Why would I be?"
    scy "But I feel the vibration of someone crying!"
    unknown_speaker "nngueeeh.."

    show mc shock:
        full
        right
    show cory surprise :
        full
        unpose
        leftish
    cory "Wait, I hear it too..!"

    show shrimp default_om:
        full
        centerright
    scy "What if it's another one of golden fish's unfortunate victims?!"

    show mc o:
        full
        right
        toleft
    mc "Oh no! We have to find them!"

    show cory side:
        full
        leftish
    cory "Everybody's been gloomy lately huh"
    $ focus()

    jump ch3_day_explore

label ch3_day_explore:
    $ current_chapter = 3
    $ current_cycle = "day"

    $ setup_exploration(
        [
            {
                "id": "hawk",
                "name": "Gran Hawk",
                "idle": "turtle idle",
                "hover": "turtle hover",
                "xpos": 307,
                "ypos": 162,
                "check_xpos": 518,
                "check_ypos": 120,
                "x": 0.20,
                "y": 0.20,
                "check_y": 0.12
            },
            {
                "id": "bunny",
                "name": "Sea Bunny",
                "idle": "seabunny idle",
                "hover": "seabunny hover",
                "xpos": 1370,
                "ypos": 592,
                "check_xpos": 1411,
                "check_ypos": 550,
                "x": 0.72,
                "y": 0.58,
                "check_y": 0.52
            }
        ],
        {
            "id": "rainbow_algae",
            "name": "Rainbow Algae",
            "idle": "item_algae_idle",
            "hover": "item_algae_hover",
            "xpos": 809,
            "ypos": 807,
            "x": 0.44,
            "y": 0.77
        }
    )

    label .loop:
        hide mc
        hide cory
        hide scy
        hide bunny
        hide hawk
        scene ch3_day

        python:
            for _n in exploration_npcs:
                if _n["id"] in ("hawk", "turtle"):
                    _n["idle"] = "turtle idle"
                    _n["hover"] = "turtle hover"
                    _n["xpos"] = 307
                    _n["ypos"] = 162
                    _n["check_xpos"] = 518
                    _n["check_ypos"] = 120
                elif _n["id"] in ("bunny", "seabunny"):
                    _n["idle"] = "seabunny idle"
                    _n["hover"] = "seabunny hover"
                    _n["xpos"] = 1370
                    _n["ypos"] = 592
                    _n["check_xpos"] = 1411
                    _n["check_ypos"] = 550
            if exploration_item:
                exploration_item["xpos"] = 809
                exploration_item["ypos"] = 807

        call screen exploration_screen

        $ result = _return

        if result in ("bunny", "seabunny"):
            $ mark_npc_explored("bunny")
            call seabunny_encounter
            jump .loop

        elif result in ("hawk", "turtle"):
            $ mark_npc_explored("hawk")
            call hawk_encounter
            jump .loop

        elif result == "item":
            $ collect_exploration_item()
            call ch3_item_rainbow_algae
            jump .loop

        elif result == "continue":
            jump ch3_night_explore

        jump .loop

label ch3_item_rainbow_algae:
    $ focus ()
    show mc excited:
        full
        unpose
        offscreenright
    show mc excited:
        right
        walkto(right)
        toleft
        surprise
    with moveinright
    mc "Woah! Rainbow algaes"

    show cory talk_hu:
        full
        unpose
        offscreenright
    show cory talk_hu:
        center
        walkto(center)
        toleft
        walkloop
    with moveinright
    cory "Wait guppy, are those safe? Colors suggest me not.."

    show cory talk_hu:
        full
        leftish
    with move
    show shrimp laugh:
        full
        unpose
        offscreenleft
    show shrimp laugh:
        centerright
        walkloop
    with moveinleft
    scy "Don't fret my friend! These are harmless!"

    show mc happy:
        full
        right
        surprise
    mc "Yipee! I'll take some with us then!"

    show shrimp default_om:
        full
        centerright
        vibrate
    scy "Do take a considerable amount!"
    scy "I will not tolerate algae hoarding!"

    show mc default:
        full
        unpose
        right
    mc "Yes, yes, I know!"

    show mc o:
        full
        right
    mc "Can i taaaake.. Mm 30?"

    show shrimp surprise:
        full
        centerright
        surprise
    scy "Absolutely not! That's more than the crown allows!"

    show shrimp default_om:
        full 
        unpose
        centerright
    scy "You can only take no more than 5lbs!"

    show mc pout:
        full
        right
    mc "But I seen fishermen take a huuuuuge big bucket of algaes and not get yelled at!"
    mc "30 is far from filling a huge big bucket!"

    show shrimp default_om:
        full
        centerright
    scy "No! Here in sea, we have strict rules over what we take"
    scy "Especially now! The waters have been thinning for moons now…"

    show shrimp sepet:
        full
        centerright
    scy "Algae, fish, even the coral's gone quiet!"

    show mc shock:
        full
        right
    mc "Wait, so… it's actually bad right now?"

    show shrimp default_om:
        full
        centerright
    scy "Bad enough that the crown had to cut the limit twice this season alone!"

    show shrimp default_om:
        full
        centerright
    scy "So no. Not 30. Not even close, guppy!"

    show mc pout:
        full
        right
    mc "Mmn okay, I understand…"

    show mc o:
        full
        right
    mc "Mr cory, whats 5 lbs in kilograms..?"

    show cory side:
        full
        leftish
    cory "I uhh.."

    show cory side_close:
        full
        leftish
    cory "Ay, let's just take 2 and go guppy"
    $ focus ()
    $ has_rainbow_algae = True
    $ add_item("rainbow_algae")
    return

label ch3_day_explore_continue:
    if ch3_visited_seabunny:
        $ mark_npc_explored("bunny")
    if ch3_visited_turtle:
        $ mark_npc_explored("hawk")
    jump ch3_day_explore.loop
    
label ch3_night_explore:
    $ current_cycle = "night"
    hide mc
    hide cory
    hide scy
    hide hawk
    scene ch3_night with Dissolve (0.5)
    play music chap_3_night volume 0.5

    $ focus ()
    show scy smile:
        full
        unpose
        offscreenright
    show scy smile:
        centerright
        walkloop
    with moveinright
    scyllarus "This way everyone! We'll arrive at the lair soon!"

    show cory talk:
        full
        unpose
        offscreenright
    show cory talk:
        leftish
        walkloop
    with moveinright
    cory "Guh.. and how soon exactly is soon?"

    show scy smile:
        full
        centerright
    show cory upset :
        full
        leftish
        surprise
    cory "We've been swimmin for more than half a day now!"

    show mc shock:
        full
        unpose
        offscreenright
    show mc shock:
        right
        vibrate
    with moveinright
    mc "nnguuh.. I can't feel my legs anymore…"

    show cory smile_hu:
        full
        leftish
    show mc shock:
        full
        right
    cory "Here, let me hold onto ya guppy"

    "Mr Cory gently wraps his fins around my tummy in a loose hold horizontally, the rest is carried by the water's current and light buoyancy."
    "I held my arms wide like an airplane."
    "I feel like a remora fish latching onto a shark's under."

    show mc happy:
        full
        right
    mc "Thank you.. Mr Cory.."

    show mc o:
        full
        right
    mc "Mnn do fishes ever get tired of swimming..?"

    show cory talk:
        full
        leftish
    cory "Nah we don't"

    show scy default:
        full
        centerright
        surprise
    scyllarus "Yes we do!"

    show cory smile_hu:
        full
        leftish
    cory "Can't speak for a crustacean but.. how these fins moving? They're automatic!"
    cory "You don't ever get tired of breathing do ya?"

    show mc default:
        full
        right
    mc "ahh so it's like breathing.. :o"

    show scy smile:
        full
        centerright
    scyllarus "Look ahead, my comrades! We have reached the perimeter of the royal reef!"

    show cory talk:
        full
        leftish
    cory "The water feels different here... heavy, red, and quiet."

    show mc o:
        full
        right
        surprise
    mc "Look, there are figures stationed near the coral formations! Let's explore before we step inside!"
    $ focus ()

    $ current_chapter = 3
    $ current_cycle = "night"

    $ setup_exploration(
        [
            {
                "id": "dunge",
                "name": "Dunge Crab",
                "idle": "crab idle",
                "hover": "crab hover",
                "xpos": 456,
                "ypos": 762,
                "check_xpos": 690,
                "check_ypos": 730,
                "x": 0.35,
                "y": 0.75,
                "check_y": 0.68
            },
            {
                "id": "teto",
                "name": "Royal Cavern",
                "idle": "teto idle",
                "hover": "teto hover",
                "xpos": 860,
                "ypos": 374,
                "check_xpos": 1089,
                "check_ypos": 350,
                "x": 0.55,
                "y": 0.40,
                "check_y": 0.33
            }
        ],
        {
            "id": "red_seaweed",
            "name": "Red Seaweed",
            "idle": "seaweed idle",
            "hover": "seaweed hover",
            "xpos": 862,
            "ypos": 598,
            "x": 0.48,
            "y": 0.58
        }
    )

    label .loop:
        hide mc
        hide cory
        hide scy
        hide dun
        hide teto
        scene ch3_night

        python:
            for _n in exploration_npcs:
                if _n["id"] in ("dunge", "crab"):
                    _n["idle"] = "crab idle"
                    _n["hover"] = "crab hover"
                    _n["xpos"] = 456
                    _n["ypos"] = 762
                    _n["check_xpos"] = 690
                    _n["check_ypos"] = 730
                elif _n["id"] in ("teto", "goby"):
                    _n["idle"] = "teto idle"
                    _n["hover"] = "teto hover"
                    _n["xpos"] = 860
                    _n["ypos"] = 374
                    _n["check_xpos"] = 1089
                    _n["check_ypos"] = 350
            if exploration_item:
                exploration_item["idle"] = "seaweed idle"
                exploration_item["hover"] = "seaweed hover"
                exploration_item["xpos"] = 862
                exploration_item["ypos"] = 598

        call screen exploration_screen

        $ result = _return

        if result in ("dunge", "crab"):
            if ch3_dunge_defeated:
                $ focus ()
                show dun default:
                    full
                    unpose
                    offscreenright
                show dun default:
                    center
                with moveinright
                dun "The path is clear. Go on ahead into the lair before I change my mind."
                $ focus ()
                menu:
                    "Enter the Empress's Lair":
                        jump ch3_boss_intro
                    "Stay in the reef":
                        jump .loop
            else:
                jump ch3_crab_encounter

        elif result in ("teto", "goby"):
            $ mark_npc_explored("teto")
            if not ch3_dunge_defeated:
                $ focus ()
                show dun mad:
                    full
                    unpose
                    offscreenright
                show dun mad:
                    leftish
                with moveinright
                dun "Hold your seahorses! No one steps a claw into Her Majesty's lair without goin' through me first!"
                show cory side:
                    full
                    unpose
                    offscreenright
                show cory side:
                    rightish
                with moveinright
                cory "Looks like Big Dunge down there is blockin' the cavern entrance. We gotta deal with him first."
                $ focus ()
                jump .loop
            else:
                "The entrance to the Crustacean Empress's lair is open before us."
                menu:
                    "Enter the Empress's Lair":
                        jump ch3_boss_intro
                    "Stay in the reef":
                        jump .loop

        elif result == "item":
            $ collect_exploration_item()
            call ch3_item_red_seaweed
            jump .loop

        elif result == "continue":
            if not ch3_dunge_defeated:
                show dun mad at npc_right
                dun "Where do you think you're goin'? No one passes through without permission!"
                show cory side at cory_left
                cory "Looks like we gotta deal with Big Dunge first."
                jump ch3_crab_encounter
            else:
                jump ch3_boss_intro

        jump .loop

label ch3_item_red_seaweed:
    $ focus ()
    show mc excited:
        full
        unpose
        offscreenright
    show mc excited:
        right
        surprise
    with moveinright
    mc "wao!! This seaweed is so red!"
    mc "Is it where the color red came from?"

    show scy default_om:
        full
        unpose
        offscreenright
    show scy default_om:
        centerright
        walkloop
    with moveinright
    scyllarus "Mm! It is a firmly believed theory that it's where crustaceans get their color from!"
    scyllarus "Crustacean mothers often told their young to feed on red seaweed to get a brighter red pigment!"

    show scy default:
        full
        centerright
    scyllarus "The redder you are the fiercer you look!"

    show mc o:
        full
        right
    mc "ooo i see.."

    show cory side:
        full
        unpose
        offscreenright
    show cory side:
        leftish
        walkloop
    with moveinright
    cory "Sounds like a plot to get your young to eat their veggies.."

    show cory upset:
        full
        leftish
        surprise
    cory "Ay, you're only allowed to take 2 guppy!"
    cory "Don't think I ain't noticing you counting how much you can take in your little arms!"

    show mc pout:
        full
        right
    mc "aw.. okay :("
    mc "one more for mama because she likes red…"
    $ focus ()
    $ has_red_seaweed = True
    return

label ch3_teto_encounter:
    show mc o at mc_left
    show teto default

    if not getattr(store, "ch3_teto_visited", False):
        $ ch3_teto_visited = True
        teto "Halt! Who dares lurk around the royal threshold of Her Majesty's lair?"
        hide teto default

        show teto default at npc_left
        show scy smile at npc_right
        scyllarus "Greetings, royal sentinels! It is I, Scyllarus! We have journeyed far to present ourselves before Her Majesty!"

        show teto gun_smirk at npc_left
        teto "Hah! Present yourselves? With freshwater strays tagging behind your tail?"
        teto "Nobody enters this cavern without going through proper protocol—and Big Dunge is guarding the outer perimeter down there!"

        hide teto gun_smirk
        show cory side at cory_left
        cory "Is that a goby riding shotgun on a pistol shrimp? And why are they looking at us like they're itching to pull a trigger?"

        hide scy smile
        show teto gun_upset at npc_right
        teto "Keep your whiskers to yourself, catfish! Talk to Dunge down there first if you want any hope of passing through!"

        show mc o at mc_left
        mc "They look very fierce... We should probably speak to Mr. Crab first!"
    else:
        show teto gun_smirk at npc_right
        teto "I told you already! Go speak to Dunge down there! The Empress doesn't entertain unannounced wanderers!"

    return

label ch3_boss_intro:
    hide mc
    hide cory
    hide scy
    hide dun
    scene ch3_night with Dissolve (0.5)

    $ focus ()
    show scy laugh:
        full
        unpose
        offscreenright
    show scy laugh:
        centerright
        walkloop
    with moveinright
    scyllarus "Welcome my friends to the humble abode of crustacean empress the VIII!"

    show mc excited:
        full
        unpose
        offscreenright
    show mc excited:
        right
        surprise
    with moveinright
    mc "Woah!! It's so.. Red!"

    show scy smile:
        full
        centerright
        surprise
    scyllarus "Yes! Red is her favored color after all!"

    show mc serious:
        full
        unpose
        right
    mc "But how can she know colors..? Aren't pistol shrimps blind?"
    show scy smile:
        full
        centerright
    scyllarus "They're almost blind, actually!"
    scyllarus "And she's just told that her color is red, and it immediately become her favorite!"

    show cory smile_hu:
        full
        unpose
        offscreenright
    show cory smile_hu:
        leftish
        walkloop
    with moveinright
    cory "And the eighth you say..? She gon rule for 36 years?"

    "Abruptly—"

    hide mc 
    hide cory  
    hide scy 
    with moveoutleft

    show goby default:
        full
        unpose
        offscreenright
    show goby default:
        centerright
    with moveinright
    gob "Fall to your knees and tremble before Her Majestic Majesty, the one and only!"
    gob "Her Majesty Empress Crustacean the VIII!"

    show teto default:
        full
        unpose
        offscreenright
    show teto default:
        centerleft
    with moveinright
    emp "Ah, a visitor?"
    emp "Kekeke! That's me, that's me! I'm Crustacean Empress VIII!"

    show goby struck:
        full
        centerright
    gob "Mhm, the best empress on the crustacean line~!"

    show teto default:
        full
        centerleft
    emp "Oh you humble me so, my right hand!"

    show goby struck:
        full
        centerright
    gob "Ah but your greatness must be known across the seven seas~!"
    emp "Across seven seas you say?!"
    gob "I am merely speaking truth, your Majesty!"

    show cory unimpressed:
        full
        unpose
        offscreenright
    show cory unimpressed:
        leftish
    with moveinleft
    show teto default:
        full
        centerright
    with move
    show goby struck:
        full
        rightish
    with move
    cory "Are all crustaceans like this…?"

    show teto upset:
        full
        centerright
        vibrate
    emp "WHAT?! You dare question the might of an empress?!"

    show goby annoy:
        full
        rightish
    gob "They seem to have a death wish, your majesty.."

    show teto gun_smirk:
        full
        centerright
        surprise
    emp "Then fulfill your wish I shall! Wouldn't the majestic I be the fairest?!"

    show teto gun_smirk:
        full
        unpose
        centerright
    play sound "audio/attack_2.mp3"
    $ renpy.pause(0.2)
    play sound "audio/attack_1.mp3"

    show cory surprise:
        full
        leftish
        surprise
    cory "WOAH WOAH-! CHILL OUT YOUR CRUSTACEAN MAJESTY! PUT THE GUN DOWN"

    hide cory with moveoutleft
    show scy default_om:
        full
        unpose
        offscreenright
    show scy default_om:
        leftish
    with moveinleft
    scyllarus "Wait, don't!! I beg for mercy on every one of my ten legs, your majesty!"
    emp "Ah, If it's not my strongest soldier Scyllarus…"
    emp "What petty excuse do you have in defense?"

    show goby disgust:
        full
        rightish
    gob "I don't think there was ever an excuse to bring in dirtwater.."
    scyllarus "I beg of Your Majesty and your highly regarded right hand!"
    emp "Oh oh! Are you here to spread marvelous news?! Have you found and fetched me the great golden fish?!"

    show scy surprise:
        full
        leftish
    scyllarus "I-! No.. not yet your majesty.. I still have yet to acquire the golden fish.. but!"
    show scy default:
        full
        leftish
    scyllarus "My dear comrades here have a proposition that'll make it worthwhile!"

    show teto upset:
        full
        centerright
    emp "Proposition..? Bleehh my ears are made to hear only the best of things not the boring ones.."

    show goby annoy:
        full
        rightish
    gob "Their filthy words are not for your ears your majesty"
    gob "Let me decide if it is worthwhile.. As you say it"

    show teto laugh:
        full
        centerright
    emp "Hah! You be my filter, my highly regarded right hand."
    emp "I shall busy myself with my new golden toy!"
    $ focus ()
    jump ch3_boss_negotiation

label ch3_ending:
    hide mc
    hide cory
    hide scy
    scene ch3_night with Dissolve (0.5)

    $ focus ()
    show goby surprise:
        full
        unpose
        offscreenright
    show goby surprise:
        centerright
    with moveinright
    gob "Your majesty!!"

    show teto upset:
        full
        unpose
        offscreenright
    show teto upset:
        centerleft
    with moveinright
    emp "gooobyyy…"

    show goby default:
        full
        centerright
    gob "Hark! We must flee at once!"

    show teto upset:
        full
        centerleft
        surprise
    emp "FLEE?? that's bullshriiimp!! that's what a coward does we're no cowards gobyyy! Waaah!"

    show teto upset:
        full
        unpose
        centerleft
    gob "My apologies your majesty, but your survival is my priority."
    gob "You have won, Scyllarus.. fair and square."
    gob "I might be a right hand of a tyrant.. but I still have dignity left in me."

    show teto gun_upset: 
        full
        centerleft
        vibrate
    emp "OI!! ARE YA CALLING ME UNDIGNIFIED??! A TYRANT TOO?!"
    emp "I'LL GET YOUR PETTY ASS SCYLLARUUUUS!!! I STILL HAVE THE GOLD SCALE WITH ME-!"


    show cory smile:
        full
        unpose
        offscreenleft
    show cory smile:
        leftish
    with moveinleft
    show teto gun_upset:
        full
        center
        vibrate
    with move
    show goby default:
        full
        rightish
    with move
    cory "Heh, you mean this thing?"

    show teto upset:
        full
        center
        vibrate
    emp "WHA-! WHEN DID YOU-! GHRRRR STUPID FRESHWATER THIEF!! ROT IN THE DEEPEST PIT OF DEEP FUGGING SEA- MMPH-?!"
    "A fin gently pressed the former empress' mouth shut"

    show teto upset:
        full
        center
    gob "Please excuse us.. If fate allows, we'll cross path once more"

    show goby disgust:
        full
        rightish
    gob "And when that time comes.. We'll have our fitting revenge"

    hide goby
    hide teto
    with moveoutright
    "Miss General Goby flashes a rueful smile at us, before hauling her still-sputtering empress off into the deep, a trail of bubbles marking their retreat."

    show cory talk:
        full
        leftish
    cory "Heh.. didn't thought gob's still have some sense like that"

    show scy proud:
        full
        unpose
        offscreenleft
    show scy proud:
        centerright
    with moveinleft
    scyllarus "Hm! I always knew General had a sense of justice in her!"

    show scy sepet:
        full
        centerright
    scyllarus "But her devotion for the empress weighs heavier…"

    show scy smile:
        full
        centerright
    scyllarus "Hah! Now that's over all there is to make a statement of apology to the seafolks and…"

    show mc excited:
        full
        unpose
        offscreenleft
    show mc excited:
        right
        block:
            jumpmc
            pause 1
            repeat
    with moveinleft
    mc "Mr Shrimp look!! Woah, so many people gathered at the front!"

    show scy surprise:
        full
        centerright
    scyllarus "Hm..?!"

    crowd "Thank you weird looking guppy!"
    crowd "We love you!!"
    crowd "Yeah! You're our hero!"

    show mc happy:
        full
        unpose
        right
    mc "We.. couldn't at all do this without Mr. Shrim- Mr. Cyllarus' help!"
    mc "So I'd like.. for all of you to thank him too!"
    cory "What they said! Turnin' around over for betrayal was never an easy task!"
    cory "He's the one that showed us the path, protected us, and defy the empress' ruthless ruling!"

    show scy surprise:
        full
        centerright
        jump
    scyllarus "B-Betrayal?! Outrageous! What I did was what was right!"

    crowd "Thank you Scyllarus!!"
    crowd "WE LOVE YOU LARUUUS!!"
    crowd "I'M GOING TO NAME MY GUPPY AFTER YOU SCYLLARUUUS!!"
    crowd "PLEASE PLEASE PLEASE PLEASE HAVE MY FIRST NEWBORN SCYLLARUS!!"
    crowd "Thank you mr big shiiiimp!"

    show scy proud:
        full
        centerright
    scyllarus "W-WOAH! I've never received this much love from a crowd!"
    scyllarus "Thank you everyone! It is my greatest honor to be aid of the sea!!"
    scyllarus "Seeing smiles that bloom from the actions of my own claws.."
    show scy proud:
        full
        centerright
        jump
    scyllarus "I've never felt so powerful! KAKAKA!"
    hide cory with moveoutleft

    show dunge default:
        full
        unpose
        offscreenleft
    show dunge default:
        leftish
    with moveinleft
    dun "Larus!"

    show scy laugh:
        full
        unpose
        centerright
    scyllarus "Ah, my comrade Dunge, crustaceans! I-!"

    "Mr Clarus' words were abruptly cut upon spotting the crab's lowered head, claws tucked close in a way Mr Shrimp had never seen before."
    "An entire army of crustaceans follow through crabs, mantis shrimps, lobsters, hermits still dragging borrowed shells kneel in perfect unison before him, chelipeds pressed flat against the sand"

    
    dun "We're sorry for all the troubles we caused..!"
    dun "And now that Her Majesty's fallen.. it's only right the crown goes to the strongest soldier left standin'."

    crustaceans "Your Majesty Scyllarus!!"
    crustaceans "All hail the new empire!"

    show scy default_om:
        full
        centerright
    scyllarus "...."
    scyllarus "Everyone, please, stand up, and listen clear!"
    scyllarus "I'm no emperor, and I have no interest in being crowned one!"

    dun "But Larus.. you beat her fair and square. That's how it's always worked 'round here."
    dun "Strongest claw makes the rules."

    show scy sepet:
        full
        centerright
    scyllarus "Then let today be the day that rule dies with her."

    "The crowd murmurs, uncertain, still bowed."

    show mc o:
        full
        right
    mc "Ohh! Does that mean Mr. Shrimp is king now?!"

    show scy sepet:
        full
        centerright
        jump
    scyllarus "It's Scyllarus, and no, guppy!"

    show scy default:
        full
        centerright
    scyllarus "Crustacean Empress the VII.."

    show scy default_om:
        full
        centerright
    scyllarus "She told me once, that the sea belongs to no one and everyone at once.."
    scyllarus "That we, as merely one of its many inhabitants, were never given the right to rule it.."
    scyllarus "Only the responsibility to help it thrive."
    scyllarus "and her dethrone was.. that of her own choice.."
    scyllarus "But her daughter took the chance for a ruling instead!"

    show mc default:
        full
        right
    mc "You'd make a great king though mr Clarus.."

    show scy sepet:
        full
        centerright
        jump
    scyllarus "It's Scyllarus!! And even if I would.. I have no interest in a throne built on someone else's exile."

    show scy sepet:
        full
        unpose
        centerright
    scyllarus "Now, I shall honor her wishes! And let the sea be an free safe space!"

    "Slowly, claw by claw, the army rises. Uncertain, murmuring amongst themselves, but no longer kneeling."

    dun "...No Man's Land, huh."

    show dunge smile:
        full 
        leftish
    dun "Guess that means I got no orders left to follow."
    dun "I'm steppin' down too, then. No more green corals. No more borders. Not on my claws, not anymore."

    hide dunge with moveoutleft
    show scy smile:
        full
        unpose
        centerright
    scyllarus "That's exactly what it means! From today onward, Seafolks, whether it's fins, chelipeds, claws, flippers, spikes..! Whatever your appendages are!"
    scyllarus "We must all help each other! Make the sea a comfortable, safe living space for all!"

    show scy shy:
        full
        centerright
    scyllarus "And to my beloved comrades… who's helped me realize.."

    "Mr Shrimp turns to face us, his usual boastful grin softened into something quieter."

    scyllarus "Cory.. you called me your mate before you ever called me an ally."
    scyllarus "You saw a friend where everyone else only saw a weapon."
    scyllarus "I don't think I've properly thanked you for that."

    show scy default_om:
        full
        centerright
    scyllarus "And guppy.."

    show scy smile:
        full
        centerright
    scyllarus "The two of you gave me back a version of myself I thought I'd lost the day I put on this armor."
    scyllarus "So! From now on, I.. vow to be under your command!"

    show mc excited:
        full
        right
        block:
            jumpmc
            pause 1
            repeat
    mc "REALLY?! mm theeen…"
    mc "Can I take 30 rainbow algaes and 40 red seaweeds?!"
    mc "oh oh maybe.. 35 clams too…"

    show cory upset:
        full
        unpose
        offscreenleft
    show cory upset:
        leftish
    with moveinleft
    cory "WHAT-?! Don't listen to them larus!"
    cory "You're not ours to command! you're our mate!"
    cory "And mates don't tell each other what to do!"

    show scy surprise:
        full
        centerright
        jump
    scyllarus "MATE?! Mate! You say….!"

    show scy surprise:
        full
        unpose
        centerright
    scyllarus "Hmm.. and you say \"our\" which includes the guppy.."

    show scy shy:
        full
        centerright
    scyllarus "I'm sorry but I must decline! I'm not one to be interested in young guppies!"
    scyllarus "But my dear comrade Cory however, If you are committed enough…!"
    scyllarus "I.. might as well give us a try!"

    show cory surprise:
        full
        leftish 
        jump
    cory "....??!"

    show cory surprise:
        full
        unpose
        leftish
    cory "NAY AY AY AY YOU'VE GOT THE WRONG IDEA CARA!"
    cory "I MEANT COMRADES!! AIN'T NO INTIMACY PARTNER!!"

    show scy laugh:
        full
        centerright
        jump
    scyllarus "OH..!!"

    show scy laugh:
        full
        unpose
        centerright
    scyllarus "KAKAKA! Very well a comrade I should be!"

    show scy default:
        full
        centerright
    scyllarus "And as for the guppy…!"

    show scy default_om:
        full
        centerright
    scyllarus "My apologies but I'm still not letting you exploit the sea in whatever shape or form!"

    show mc pout:
        full
        unpose
        right
    mc "ueeeeh.. :("

    show cory talk:
        full
        leftish
    cory "But now we got two of these huh.."

    show mc happy:
        full
        right
        jump
    mc "I wanna keep it!"
    cory "feel anythin different?"

    show mc excited:
        full
        right
        block:
            jumpmc
            pause 1
            repeat
    mc "woah..! I.. I can hear your voices clearer and and!"
    mc "and.. my skin feels.. Less pruny now!"
    mc "It's as if I'm becoming more and more of a fish! :D"

    show scy laugh:
        full
        centerright
    scyllarus "KAKAKA! Good for you!"

    show mc o:
        full
        unpose
        right
    mc "mnn.. I wanna try something"

    "I took off the weighing glass on my head"

    show cory talk:
        full
        leftish
    cory "Don't push yourself too hard alright?"

    show mc shock:
        full
        right
    mc "... nguhk..!"
    mc "it's.. the waterbreathing time! It was only for a few minutes before"
    mc "now I can breathe just fine!"

    show gator smile:
        full
        unpose
        offscreenright
    show gator smile:
        rightish
    with moveinright
    show scy laugh:
        full
        center
    with move
    gator "ouuu shiiii.."
    gator "you all look nasty… need help?"

    show mc excited:
        full
        right
    mc "Ms. Gator!! We meet again!"
    gator "mm yep what I say about catching that golden fish before you do"

    show gator annoyed:
        full
        rightish
    gator "but frankly? I just.. lost motivation midway.."
    gator "waaaay too much of a hassle.."

    show cory side:
        full
        leftish
    cory "Gatha.."

    show gator default:
        full
        rightish
    gator "But I did get this.."
    gator "As a proof that I did get to it hmph!"
    gator "you can't be saying shrimp like I was too slow or anythin now"

    show mc o:
        full
        right
    mc "wait! Where did you get this and when?"
    mc "We haven't seen the fish lately.."

    gator "it's just riiiight there"

    show gator surprised:
        full
        rightish
    gator "I don't get why you're so adamant on getting it guppy.."
    gator "But best of luck to ya alright"
    $ focus ()
    $ ch3_chapter_complete = True

    hide mc
    hide scy
    hide gator
    hide cory
    with dissolve

    scene black with fade
    "END OF CHAPTER 3"

    jump chapter4_start
