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

    renpy.image(("bunny", "cry"), "images/placeholder/seabunny_cry.png")
    renpy.image(("bunny", "scared"), "images/placeholder/seabunny_scared.png")
    renpy.image(("bunny", "sad"), "images/placeholder/seabunny_sad.png")
    renpy.image(("bunny", "default"), "images/placeholder/seabunny_default.png")
    renpy.image(("bunny", "happy"), "images/placeholder/seabunny_happy.png")

    renpy.image(("hawk", "default"), "images/placeholder/hawk_default.png")
    renpy.image(("hawk", "sigh"), "images/placeholder/hawk_sigh.png")
    renpy.image(("hawk", "smile"), "images/placeholder/hawk_smile.png")
    renpy.image(("hawk", "laugh"), "images/placeholder/hawk_laugh.png")

screen ch3_boss_negotiation_timer(timeout=8.0):
    timer timeout action Jump("ch3_boss_negotiate_mc_timeout")

label chapter3_start:
    jump ch3_start

label ch3_start:
    $ current_chapter = 3
    $ current_cycle = "day"

    hide mc
    scene ch3_day
    with fade
    play music chap_3_day volume 0.5

    "The sea fills my line of sight with overwhelmingly bright pretty colors. My gaze erratically jumps from one color to another as we continue to swim further. From parrot fishes, sparkly elvis worms to rainbow open brain corals. There's way too many stuff to focus on!"

    show cory smile_hu at cory_left
    cory "heh.. Yer eyes been flying everywhere since we got here"
    cory "Don't ya get dizzy?"

    show mc excited at mc_left
    mc "ohmigosh!! Is that coral dancing?! Did you see that, Mr Cory?! I think that's the Spanish dancer!"

    show cory fond at cory_left
    cory "So excited, can't even hear me huh.."

    show cory smile_hu at cory_left
    cory "Though I must admit that this is some otherworldly beaut going on"

    show scy proud at npc_right
    scyllarus "Right?! Feast your eyes upon the neverending beauty that is sea!"

    show cory side at cory_left
    cory "To think your empress' been gatekeepin all this.. kinda messed up to think about"

    show scy sepet at npc_right
    scyllarus "But she's not entirely wrong either! Most fish criminals are freshwater types!"

    show cory side_close at cory_left
    cory "Ay.. Sure, being careful is one thing.."
    cory "But pushing that stereotype into every freshwater is a whole different thing"

    show scy default_om at npc_right
    scyllarus "Mm.. well! It's the daughter that just got promoted into empress!"
    scyllarus "The former queen that saved my life had dethroned herself not long ago"
    scyllarus "So she's still trying out new rules that feel fitting!"

    show cory unimpressed at cory_left
    cory "New ruler's a kid? That checks out.."

    show cory talk at cory_left
    cory "About time somefish teaches em a lesson then"

    show scy surprise at npc_right
    scyllarus "....!"
    scyllarus "Wait! Why are you crying comrade?!"

    show cory surprise at cory_left
    cory "Huh? I ain't crying! Are you guppy?"

    show mc shock at mc_left
    mc "Me? Why would I be?"

    show scy surprise at npc_right
    scyllarus "But I feel the vibration of someone crying!"

    unknown_speaker "nngueeeh.."

    show cory surprise at cory_left
    cory "Wait, I hear it too..!"

    show scy default_om at npc_right
    scyllarus "What if it's another one of golden fish's unfortunate victims?!"

    show mc o at mc_left
    mc "oh no! We have to find them!"

    show cory side at cory_left
    cory "Everybody's been gloomy lately huh"

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
            call ch3_seabunny_encounter
            jump .loop

        elif result in ("hawk", "turtle"):
            $ mark_npc_explored("hawk")
            call ch3_turtle_encounter
            jump .loop

        elif result == "item":
            $ collect_exploration_item()
            call ch3_item_rainbow_algae
            jump .loop

        elif result == "continue":
            jump ch3_night_explore

        jump .loop

label ch3_item_rainbow_algae:
    show mc excited at mc_left
    mc "woah! Rainbow algaes"

    show cory talk_hu at cory_left
    cory "Wait guppy, are those safe? Colors suggest me not.."

    show scy laugh at npc_right
    scyllarus "Don't fret my friend! These are harmless!"

    show mc happy at mc_left
    mc "yipee I'll take some with us then!"

    show scy default_om at npc_right
    scyllarus "Do take a considerable amount!"
    scyllarus "I will not tolerate algae hoarding!"

    show mc default at mc_left
    mc "yes yes I know!"

    show mc o at mc_left
    mc "Can i taaaake.. Mm 30?"

    show scy surprise at npc_right
    scyllarus "Absolutely not! That's more than the crown allows!"

    show scy default_om at npc_right
    scyllarus "You can only take no more than 5lbs!"

    show mc pout at mc_left
    mc "But I seen fishermen take a huuuuuge big bucket of algaes and not get yelled at!"
    mc "30 is far from filling a huge big bucket!"

    show scy default_om at npc_right
    scyllarus "No! Here in sea, we have strict rules over what we take"
    scyllarus "Especially now! The waters have been thinning for moons now…"

    show scy sepet at npc_right
    scyllarus "algae, fish, even the coral's gone quiet!"

    show mc shock at mc_left
    mc "Wait, so… it's actually bad right now?"

    show scy default_om at npc_right
    scyllarus "Bad enough that the crown had to cut the limit twice this season alone!"
    scyllarus "So no. Not 30. Not even close, guppy!"

    show mc pout at mc_left
    mc "mmn okay I understand…"

    show mc o at mc_left
    mc "mr cory whats 5 lbs in kilograms..?"

    show cory side at cory_left
    cory "I uhh.."

    show cory side_close at cory_left
    cory "ay let's just take 2 and go guppy"

    $ has_rainbow_algae = True
    $ add_item("rainbow_algae")
    return

label ch3_day_explore_continue:
    if ch3_visited_seabunny:
        $ mark_npc_explored("bunny")
    if ch3_visited_turtle:
        $ mark_npc_explored("hawk")
    jump ch3_day_explore.loop

label ch3_seabunny_encounter:
    hide mc
    hide cory
    hide scy
    scene ch3_day
    with dissolve

    "A seabunny is found crying behind luscious corals. I wonder what made it cry that loud?"

    show bunny cry at npc_right
    seabunny "nghuuuu.. ueeeh… ueeh!!!!"

    show mc shock at mc_left
    mc "huh..? What's wrong?"

    show bunny cry at npc_right
    seabunny "uuu.. shiku shiku.. My family.. They took them!!"

    show scy default_om at npc_left
    scyllarus "And who exactly is this \"they\"?!"

    show bunny scared at npc_right
    seabunny "GYAAA IT'S THEM IT'S THEM!!"

    "The bunny shaped slug lets out a high pitched scream. Mr. Shrimp's presence sending her scurrying away to curl and hide behind a coral as it cowers in fear."

    show scy surprise at npc_left
    scyllarus "Huh…?!"

    show mc o at mc_left
    mc "Can you specify who or what took your family?"

    show bunny scared at npc_right
    "The sea bunny seems to refuse to answer anything with Mr Shrimp nearby"

    hide mc
    hide cory
    hide scy
    hide bunny
    call screen choose_interactor(
        "Choose who should ask Sea Bunny!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_seabunny_as_mc
    elif selected_questioner == "cory":
        jump ch3_seabunny_as_cory
    else:
        jump ch3_seabunny_as_scyllarus

label ch3_seabunny_as_mc:
    show mc happy at mc_left
    mc "Don't be scared, sea bunny!"
    mc "Mr shrimp is far away now!"

    show bunny scared at npc_right
    seabunny "He's.. still around though.."

    mc "It's okay I won't let him get near you!"

    show bunny sad at npc_right
    seabunny "nguu.. okay I trust you…"

    menu:
        "What happened to your family?":
            jump ch3_bunny_mc_opt1

        "Why are you scared of Mr Shrimp?":
            jump ch3_bunny_mc_opt2

        "Do you need a hug? (Give rainbow algae)" if has_rainbow_algae:
            jump ch3_bunny_mc_opt3

label ch3_bunny_mc_opt1:
    show bunny sad at npc_right
    seabunny "They were taken away.. by a big brute crab.."
    seabunny "He claimed to be.. doing that under the crustacean empress 'command.."
    seabunny "Said that my.. kind is a threat to the sea…"

    show mc pout at mc_left
    mc "What!! That's awful!"
    mc "Everyone gets a chance to live at the sea no matter how dangerous!"
    mc "Without what they claim as threats.. The sea would be in a bigger danger!"

    show bunny default at npc_right
    seabunny "Eh..? Is that so..?"

    show mc default at mc_left
    mc "mhm!"
    mc "Mhm! Even the scary stuff has a job!"

    show mc actually at mc_left
    mc "If you take it away, whatever it used to hunt just grows and grows until that's the problem instead!"
    mc "It's like a big circle predator, prey, little guys, big guys"
    mc "snap one part off and the whole thing tips over!"
    mc "So whoever's calling your kind a 'threat'? They just don't get it!"

    show bunny happy at npc_right
    seabunny "Ahh I see! Mmn! That makes perfect sense!"

    show bunny sad at npc_right
    seabunny "If only they would understand…"

    show mc happy at mc_left
    mc "Don't worry we'll make them understand!!"
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_bunny_mc_opt2:
    show mc o at mc_left
    show bunny scared at npc_right
    seabunny "He's a crustacean!!"
    seabunny "They're the kind who took my family away!"

    show bunny sad at npc_right
    seabunny "And crustaceans they.. they all work under the crustacean empress right?"

    show mc pout at mc_left
    mc "Mm he does but.. He's different!"
    mc "He realized that what the empress' pushing is wrong!"
    mc "And now we're here to talk to the empress about it!"

    show bunny default at npc_right
    seabunny "But will the empress hear you out…?"
    seabunny "She's very ruthless and stubborn…"

    show bunny sad at npc_right
    seabunny "She's not afraid to kill those who defy her…"

    show mc happy at mc_left
    mc "mmm.. Then we'll just fight her!"

    show bunny scared at npc_right
    seabunny "dowawa?! Fight her..?!"

    show mc excited at mc_left
    mc "Yeah! Mr Cory will tank all her attacks!"

    show bunny happy at npc_right
    seabunny "That's so very cool!! You need your own shounen series!"

    show mc shock at mc_left
    mc "shounen? Ah!! Like Chainsaw Man?"

    show bunny happy at npc_right
    seabunny "Yes!! Ah finally someone that gets it!!"
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_bunny_mc_opt3:
    show bunny scared at npc_right
    seabunny "i..!"

    show bunny sad at npc_right
    seabunny "As much as I'd very much like one…right now"

    show bunny cry at npc_right
    seabunny "nnghh shiku shiku *sniffle* you can't hug me..!!"

    show mc happy at mc_left
    mc "It's fine! I know sea bunnies contain this weird toxin in their bodies but.."

    show mc actually at mc_left
    mc "Try eating this.. I read that what makes seabunny toxic is what they eat!"

    show bunny default at npc_right
    seabunny "mn.. huh? Rainbow algae.."
    seabunny "Even when it's true.. The sponges that we eat are still crucial for our survival.."

    show mc happy at mc_left
    mc "mm then I'll still hug you!"

    show bunny scared at npc_right
    seabunny "huh?"

    show mc excited at mc_left
    mc "I don't mind a little itch! You look very fluffy to touch!"

    show bunny scared at npc_right
    seabunny "B-but..!"

    "Without letting those words finish, I pulled it into a tight hug. Burying my face into its fluffy looking appendages."

    show bunny cry at npc_right
    seabunny "uu.. UEHHHH"

    show mc happy at mc_left
    mc "it's okay.. Let it all out"

    show bunny cry at npc_right
    seabunny "UHNNG I MISS MY FAAAMILY.. I MISS THEM!!"
    seabunny "ITS ALL MY FAAAULT UEEEEH…!!!!"

    show mc pout at mc_left
    mc "no no it's not!!"

    show mc default at mc_left
    mc "it's a good thing that you're still here with us…"

    show mc happy at mc_left
    mc "don't worry sea bunny we'll get your family back!!"

    show bunny sad at npc_right
    seabunny "promise…?"

    mc "mhm! Pinky promise!!"
    $ gave_algae_to_seabunny = True
    $ has_rainbow_algae = False
    $ ch3_seabunny_helped = True
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_seabunny_as_cory:
    show cory smile_hu at cory_left
    cory "Ay, easy now slug.."
    cory "I've driven the shrimp away for a bit, you're safe"

    show bunny default at npc_right
    seabunny "Thank you.. You have my gratitude…"

    "Sea bunny bows down in expression of gratitude"

    show bunny sad at npc_right
    seabunny "Also.. please don't refer to me with that.. S word.."

    cory "S word…?"

    seabunny "And ends with a g.."

    show cory side at cory_left
    cory "Oh right! My bad.."

    show cory smile at cory_left
    cory "What would you like to be called then?"

    show bunny default at npc_right
    seabunny "Sea bunny or nudibranch is fine.."

    menu:
        "Mind telling us what happened?":
            jump ch3_bunny_cory_opt1

        "I'm sorry to hear about your family.. must be tough on ya.. (Give rainbow algae)" if has_rainbow_algae:
            jump ch3_bunny_cory_opt2

label ch3_bunny_cory_opt1:
    show cory talk_hu at cory_left
    show bunny default at npc_right
    seabunny "Me and my family were just having a nice sunny picnic.. under the pink acropora coral…"

    show bunny happy at npc_right
    seabunny "Laughter all around.. As we feed each other sponges.."
    seabunny "I was going out a little to pick more sponges for us.."

    show bunny scared at npc_right
    seabunny "Until.. A big brute crab suddenly came through"

    show bunny sad at npc_right
    seabunny "So I hid behind a coral.."
    seabunny "He said he was hungry.. So my mom tried to offer him a sponge but..!"
    seabunny "He tried it.. He spat it out.. Then he moves over to.. My- and he-!"

    show bunny scared at npc_right
    seabunny "He..! He ate.. My baby sibling..?!"

    show cory surprise at cory_left
    cory "Oh shrimp.. That's real messed up…"

    show cory side at cory_left
    cory "I'm so very sorry…"

    show bunny default at npc_right
    seabunny "But we sea bunnies.. have toxins in our bodies.."
    seabunny "When the crab took a bite.. The toxins start eating him out from inside"
    seabunny "Angered.. He then took the rest of my family away claiming us as a danger to the sea.."

    show bunny sad at npc_right
    seabunny "At least.. my sibling fought until the very end.."
    seabunny "I still couldn't forgive myself for letting that crab get away…"
    seabunny "And for letting it all.. happen… It's my fault.."

    show bunny cry at npc_right
    seabunny "UEEEEHH SHIKU SHIKU"

    show cory upset at cory_left
    cory "Hey, hey don't blame yourself now!"

    show cory talk at cory_left
    cory "What could ya possibly do anyway? If you jump out you'll get kidnapped too!"

    show cory talk_hu at cory_left
    cory "What you did was the best choice, so now you can save your family"

    show bunny cry at npc_right
    seabunny "uuu…"

    show cory talk_hu at cory_left
    cory "Don't worry we'll get him"
    cory "We're planning to overthrow this whole crustacean dictator bullshrimp"
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_bunny_cory_opt2:
    show cory side at cory_left
    show bunny sad at npc_right
    seabunny "Mm.."

    show cory talk at cory_left
    cory "I had a little sister too.."

    show cory smile_hu at cory_left
    cory "Real ball of sunshine.."

    show cory talk_hu at cory_left
    cory "But she got some kind of weird sickness going on.. that eventually separates us…"

    show cory side_close at cory_left
    cory "guh sorry for the sudden vent.. I'll stop now"

    show bunny default at npc_right
    seabunny "No! It's fine.. She must've been really dear to you.. I'm sorry.."

    show cory side at cory_left
    cory "She's still alive though.. Somewhere in this vast sea.."

    show cory smile_hu at cory_left
    cory "Ah, Have you eaten anything? I've got some algae for ya.."
    cory "And it's rainbow algae!"

    show bunny happy at npc_right
    seabunny "Rainbow algae..? so pretty! kirakira"
    seabunny "Thank you!"

    show bunny sad at npc_right
    seabunny "But I.. I don't think I can.. eat after what I had to witness…"

    show cory talk_hu at cory_left
    cory "You can't be like that… your family wouldn't want ya to skip meals would they?"

    seabunny "..."

    show cory smile_hu at cory_left
    cory "Eat up sea bunny.."

    show cory fond at cory_left
    cory "So you've got the strength to look at them in the eyes when ya meet them again"

    show bunny default at npc_right
    seabunny "You're right.. Thank you.."
    $ gave_algae_to_seabunny = True
    $ has_rainbow_algae = False
    $ ch3_seabunny_helped = True
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_seabunny_as_scyllarus:
    "The sea bunny stands at a reasonably far distance"

    show bunny scared at npc_right
    seabunny "Your red shelled kind! the one who does all of this evil baka stuff!"

    show bunny sad at npc_right
    seabunny "My family.. Is detained for simply living…"

    show scy default_om at npc_left
    scyllarus "Oh! It's probably one of the crustaceans doing!"

    menu:
        "Apologize in advance":
            jump ch3_bunny_scy_opt1

        "Please accept this algae as a token of apology!" if has_rainbow_algae:
            jump ch3_bunny_scy_opt2

label ch3_bunny_scy_opt1:
    "Mr Shrimp took a few steps forward to properly bow down in an apologetical manner"

    show scy default_om at npc_left
    scyllarus "I apologize for the inconvenience that my kind has inflicted upon your family!"

    show bunny scared at npc_right
    seabunny "EEEK-!"

    "The sea bunny curls up in fear"

    seabunny "I.. kindly.. ask you to stay away.. Please…!"

    show scy default at npc_left
    scyllarus "...! Understood!"
    scyllarus "Then I shall stand at a safe, reasonable distance!"

    "Mr Shrimp took exactly one step away from the sea bunny"

    show bunny scared at npc_right
    seabunny "T-that's not enough distance!"
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_bunny_scy_opt2:
    show scy shy at npc_left
    scyllarus "I was informed that algae counts as one of your diet!"

    show bunny scared at npc_right
    seabunny "...?!"
    seabunny "I.. I read this in mangas before!"
    seabunny "It's probably poisoned right?! Or.."
    seabunny "Or you make it super delicious.."
    seabunny "And when I'm busy eating your gift.. piri piri..."
    seabunny "BAAN!! You kidnap me!"

    show scy surprise at npc_left
    scyllarus "WHAT! Preposterous! I wouldn't do such dirty tactics!"

    show bunny sad at npc_right
    seabunny "Guuu..!You'll never know! Must keep guard up! kuyo kuyo…"

    show scy sepet at npc_left
    scyllarus "And manga.. Is that some kind of.. new type of algaes?!"

    show scy default_om at npc_left
    scyllarus "I'll search for one if it makes you forgive us!"

    "The sea bunny refuses to take the sea algae"
    $ ch3_visited_seabunny = True
    jump ch3_day_explore_continue

label ch3_turtle_encounter:
    hide mc
    hide cory
    hide scy
    hide bunny
    scene ch3_day
    with dissolve

    "A seaturtle sways haphazardly above us. It suddenly throws a rock at mr.shrimp"

    show scy surprise at npc_left
    scyllarus "whuh?! What's that about!"

    show hawk default at npc_right
    hawk "get lost ya red shell!"
    hawk "we've got enough of ya bullshrimp"

    hide scy
    show cory smile_hu at npc_left
    cory "everyone's got a problem with your kind huh?"

    show mc o at mc_left
    mc "mmm it seems like the problem delve deeper than a simple hate…"
    mc "let's try asking her out!"

    hide mc
    hide cory
    call screen choose_interactor(
        "Choose who should ask Gran Hawk!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_turtle_as_mc
    elif selected_questioner == "cory":
        jump ch3_turtle_as_cory
    else:
        jump ch3_turtle_as_scyllarus

label ch3_turtle_as_mc:
label ch3_hawk_as_mc:
    show hawk default at npc_right
    hawk "Get away from that red freak guppy.."
    hawk "they can't be trusted with"

    menu:
        "Why do you hate mr. shrimp so much?":
            jump ch3_hawk_mc_opt1

        "What have the crustaceans done?":
            jump ch3_hawk_mc_opt2

label ch3_hawk_mc_opt1:
    show hawk default at npc_right
    hawk "I remember faces, that shrimp's gate guarding one!"
    hawk "He didn't get my grandturts a passing!"

    show mc pout at mc_left
    mc "But he's not like that anymore!"

    show mc default at mc_left
    mc "He's let everyone pass now you should be able to meet your grand turtles!"

    show hawk sigh at npc_right
    hawk "I know, don't worry I met them, they're safe now"
    hawk "But eh, my blood gets boiling at the sight of them now"

    show mc pout at mc_left
    mc "well! Fair point but targeting your anger at every crustaceans is bad too.."
    mc "Maybe some of them didn't want to do it.."

    show mc o at mc_left
    mc "won't it make you just like them..?"

    show hawk laugh at npc_right
    hawk "Hah, s'pose you got a point there."

    show hawk smile at npc_right
    hawk "My neighbor's a shrimp. Marchin protests with us too."

    show hawk default at npc_right
    hawk "Not all are bad, but some that stay silent is as bad, which means they agree with whatever going on"

    show mc happy at mc_left
    mc "Mr shrimp is good I know! We're trying to talk it out with the empress!"

    show hawk sigh at npc_right
    hawk "Crikey, good luck with that"
    $ ch3_visited_turtle = True
    jump ch3_day_explore_continue

label ch3_hawk_mc_opt2:
    show mc o at mc_left
    show hawk default at npc_right
    hawk "Whole sea's changed, guppy. Not for the better."

    mc "mm? how so?"

    hawk "The crustaceans they used to mind their own business.."

    show hawk sigh at npc_right
    hawk "Until the former empress pass the crown to her young"
    hawk "It all became a mess from there on"
    hawk "Now there's checkpoints. Papers. 'Loyalty tests'."

    show hawk default at npc_right
    hawk "Ain't about danger. It's about control."

    show mc default at mc_left
    mc "Mmn.. So the real problem lies on the empress!"

    show hawk sigh at npc_right
    hawk "Yeah, most red shells are natural born bullies"
    hawk "And her regime greenlit all their bad habits to all of sea"

    show mc o at mc_left
    mc "hmmm.. Why don't we all go and complain to the empress?"

    show hawk smile at npc_right
    hawk "hah! We've tried"
    hawk "Most got killed for it. It's like a war going on"
    hawk "But I've eaten heaps of em for brekkie!"

    show mc happy at mc_left
    mc "oh! Right crustaceans are a part of a sea turtle's diet"

    show hawk laugh at npc_right
    hawk "Hah right! They don't call me gran hawk for none!"
    hawk "Can't bring an empress down alone though"
    $ ch3_visited_turtle = True
    jump ch3_day_explore_continue

label ch3_turtle_as_cory:
label ch3_hawk_as_cory:
    show hawk default at npc_right
    hawk "You! You're a freshwater aren't ya?"
    hawk "What on ocean are you doing with that red shell?"

    show cory side at cory_left
    cory "Ay, calm down ma'am.."
    cory "I ain't exactly a fan of the crustacean's idealism"

    show cory talk_hu at cory_left
    cory "But my man, tis shrimp is ain't like others"

    menu:
        "What ya got going with the shrimp?":
            jump ch3_hawk_cory_opt1

        "Is it because of the crustacean empress?":
            jump ch3_hawk_cory_opt2

label ch3_hawk_cory_opt1:
    hawk "I remember faces, that shrimp's gate guarding one!"

    show cory talk_hu at cory_left
    show hawk default at npc_right
    hawk "He didn't get my grandturts a passing!"

    show cory talk_hu at cory_left
    cory "I understand your feeling but.."
    cory "He's already lettin all the fishes pass now, your grandturts should be safe"

    show cory smile at cory_left
    cory "I know he's got a good heart. Just a little lost cause"

    show hawk sigh at npc_right
    hawk "and how could you be so sure of that?"

    show cory smile_hu at cory_left
    cory "He's abandoned his post just to shout a protest to the empress"

    show hawk default at npc_right
    hawk "and have you actually met the empress?"

    show cory talk at cory_left
    cory "Not yet, but we're on our way ma'am"

    show hawk smile at npc_right
    hawk "Have you thought long enough to think that…"
    hawk "All of this might be a trap?"

    show cory talk at cory_left
    cory "huh?"

    show cory talk_hu at cory_left
    cory "What do ya mean by that, ma'am?"

    show hawk default at npc_right
    hawk "That mantis shrimp's leading yall to her lair.."
    hawk "what if it's just a facade?"

    show hawk sigh at npc_right
    hawk "You're diving into the anglerfish's light, mate"

    show cory side_close at cory_left
    cory "guh, I didn't think that far…."

    show cory side at cory_left
    cory "A huge part of my heart believes in him though"

    show hawk laugh at npc_right
    hawk "hah you a better fish than I am then"
    hawk "Just stay vigilant alright?"
    $ ch3_visited_turtle = True
    jump ch3_day_explore_continue

label ch3_hawk_cory_opt2:
    show cory talk_hu at cory_left
    show hawk default at npc_right
    hawk "Be real careful of that empress alright"
    hawk "It's two peas in a pod situation"

    show cory talk_hu at cory_left
    cory "Two peas in a pod? She got backup?"

    hawk "nay she's got a fatal weakness"

    show hawk default at npc_right
    hawk "a goby fish while she a pistol shrimp"
    hawk "Ever heard of that tale?"

    show cory side at cory_left
    cory "I'm a freshwater folk don't think I'm familiar with that"

    show hawk default at npc_right
    hawk "Pistol shrimp's near blind, see. Digs the burrow, keeps it tidy."
    hawk "So the goby does the watching. Sits right by the entrance, eyes peeled."
    hawk "Shrimp keeps a feeler on 'em at all times."

    show hawk sigh at npc_right
    hawk "Big threat? Goby'll block the whole entrance with its own body."
    hawk "They move as one. Can't have one without the other, really."

    show hawk default at npc_right
    hawk "You gotta aim for the goby first"
    hawk "or, take them both down at the same time"

    show cory surprise at cory_left
    cory "*whistle* Interesting mechanism they got going on"

    show cory talk_hu at cory_left
    cory "We plan on taking this the diplomatic route though ma'am."
    cory "But if it does get to that point.."

    show cory smile_hu at cory_left
    cory "I owe you for that one, ma'am thank you!"

    show hawk laugh at npc_right
    hawk "Anything to bring her down"
    $ clue_empress_weakness = True
    $ ch3_visited_turtle = True
    jump ch3_day_explore_continue

label ch3_turtle_as_scyllarus:
label ch3_hawk_as_scyllarus:
    show hawk default at npc_right
    hawk "Get ya stank dirty claws outta here red shell!"

    show scy default at npc_left
    scyllarus "I wipe my claws hourly! I can assure you that I'm not dirty!"

    menu:
        "I apologize in advance":
            jump ch3_hawk_scy_opt1

label ch3_hawk_scy_opt1:
    show scy default at npc_left
    show hawk default at npc_right
    hawk "hawk tuah! fugu off with that apology of yours!"
    hawk "I'm not the only one that needs your pointless apologies!"

    show hawk sigh at npc_right
    hawk "ya have wronged the whole sea, red shell"

    show scy default at npc_left
    scyllarus "...!"

    show scy default_om at npc_left
    scyllarus "Then please allow me…"

    "Mr Shrimp takes a firm step back and swivel around facing the vast sea, before he took a long deep breath."

    show scy laugh at npc_left
    scyllarus "I APOLOGIIIIIZEE FOR THEE INCONVEEENIIEEEEENNNCEEAAAHHH!!!!"

    show hawk smile at npc_right
    hawk "pfft-!"

    show hawk laugh at npc_right
    hawk "hahahah!"
    hawk "Hate to admit it! But you pass the vibe check"
    hawk "Still ain't forgiving you though"
    $ ch3_visited_turtle = True
    jump ch3_day_explore_continue

label ch3_night_explore:
    $ current_cycle = "night"

    hide mc
    hide cory
    hide scy
    hide hawk
    scene ch3_night
    with fade
    play music chap_3_night volume 0.5

    show scy smile at npc_right
    scyllarus "This way everyone! We'll arrive at the lair soon!"

    show cory talk at cory_left
    cory "Guh.. and how soon exactly is soon?"

    show cory upset at cory_left
    cory "We've been swimmin for more than half a day now!"

    show mc shock at mc_left
    mc "nnguuh.. I can't feel my legs anymore…"

    show cory smile_hu at cory_left
    cory "Here, let me hold onto ya guppy"

    "Mr Cory gently wraps his fins around my tummy in a loose hold horizontally, the rest is carried by the water's current and light buoyancy. I held my arms wide like an airplane"
    "I feel like a remora fish latching onto a shark's under."

    show mc happy at mc_left
    mc "Thank you.. Mr Cory.."

    show mc o at mc_left
    mc "mnn do fishes ever get tired of swimming..?"

    show cory talk at cory_left
    cory "Nah we don't"

    show scy default at npc_right
    scyllarus "Yes we do!"

    show cory smile_hu at cory_left
    cory "Can't speak for a crustacean but.. how these fins moving? They're automatic!"
    cory "You don't ever get tired of breathing do ya?"

    show mc default at mc_left
    mc "ahh so it's like breathing.. :o"

    show scy smile at npc_right
    scyllarus "Look ahead, my comrades! We have reached the perimeter of the royal reef!"

    show cory talk at cory_left
    cory "The water feels different here... heavy, red, and quiet."

    show mc o at mc_left
    mc "Look, there are figures stationed near the coral formations! Let's explore before we step inside!"

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
                show dun default at npc_right
                dun "The path is clear. Go on ahead into the lair before I change my mind."
                menu:
                    "Enter the Empress's Lair":
                        jump ch3_boss_intro
                    "Stay in the reef":
                        jump .loop
            else:
                jump ch3_crab_encounter

        elif result in ("teto", "goby"):
            if not ch3_dunge_defeated:
                show dun mad at npc_right
                dun "Hold your seahorses! No one steps a claw into Her Majesty's lair without goin' through me first!"
                show cory side at cory_left
                cory "Looks like Big Dunge down there is blockin' the cavern entrance. We gotta deal with him first."
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
    show mc excited at mc_left
    mc "wao!! This seaweed is so red!"
    mc "Is it where the color red came from?"

    show scy default_om at npc_right
    scyllarus "Mm! It is a firmly believed theory that it's where crustaceans get their color from!"
    scyllarus "Crustacean mothers often told their young to feed on red seaweed to get a brighter red pigment!"

    show scy default at npc_right
    scyllarus "The redder you are the fiercer you look!"

    show mc o at mc_left
    mc "ooo i see.."

    show cory side at cory_left
    cory "Sounds like a plot to get your young to eat their veggies.."

    show cory upset at cory_left
    cory "Ay, you're only allowed to take 2 guppy!"
    cory "Don't think I ain't noticing you counting how much you can take in your little arms!"

    show mc pout at mc_left
    mc "aw.. okay :("
    mc "one more for mama because she likes red…"

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

label ch3_crab_encounter:
    $ mark_npc_explored("dunge")
    show mc o at mc_left
    show dun smile at npc_right

    "We spotted another crustacean."
    "It's a grown-sized dungeness crab. He seems like a laid back crustacean."

    hide dun smile at npc_right
    show scy smile
    "Mr shrimp advanced towards him like seeing an old friend."

    scyllarus "My comrade in arms Dunge!"

    hide scy smile
    show scy smile at npc_left
    show dun smile at npc_right
    dun "Well butter my tail and call me a biscuit!"
    dun "Larus! Hows it hangin', you ol' bottom-feeder?"

    show mc o at mc_left
    mc "Larus..? Is that Mr Shrimp's real name?"

    show dun default at npc_right
    "The crab's expression subtly changed at my unfamiliar voice, it was close to that of disdain."
    "When he noticed me and Mr. Cory's presence."

    show dun mad at npc_right
    dun "... Hold your seahorses. What the hell are you doin' here?"
    dun "Your tail is supposed to be guardin' the salt-fresh border!"

    hide scy
    show cory talk_hu at cory_left
    cory "Chill out mane…"

    show dun default at npc_right
    dun "!!! And what's this junk you bought with ya?"

    show dun yeesh at npc_right
    dun "Dont tell me you're rollin' with these filthy freshies??"
    dun "A guppy… and and!"

    "Choose who should ask Mr. Crab! The answers it gives may varied based on its relationship with the character"

    hide mc
    hide cory
    hide scy
    hide dun
    call screen choose_interactor(
        "Choose who should ask Mr. Crab!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_crab_as_mc
    elif selected_questioner == "cory":
        jump ch3_crab_as_cory
    else:
        jump ch3_crab_as_scyllarus

label ch3_crab_as_mc:
    menu:
        "Mr. Crab can you help us talk to the Empress?":
            jump ch3_crab_mc_opt1

        "Do you hate freshwater creatures? :0":
            jump ch3_crab_mc_opt2

label ch3_crab_mc_opt1:
    show mc o at mc_left
    show dun default at npc_right
    "Mr crab gives me a humbling look…"

    dun "Help you? what are you even supposed to be?"
    dun "Some kinda a half-breed?"
    dun "Do your parents even have the green corals?"

    show mc o at mc_left
    mc "Green corals? :0"

    show dun yeesh at npc_right
    dun "Yeah green corals. The damn corals you need to legally live around here."
    dun "You must've had some relative from the saltwater side hand 'em over to ya."

    show mc shock at mc_left
    mc "I uhhhhhhh...."

    show dun default at npc_right
    dun ".... You dont got 'em?"

    show mc shock_hu at mc_left
    mc "Um we dont have one….. is it alright, mr shrimp?"

    show scy default at npc_left
    scyllarus "They're my company, Dunge! From the freshwater."
    scyllarus "They're just passing through the reefs, not taking up residence!"

    show scy default_om at npc_left
    scyllarus "Also the green coral policy is still up for debate!"

    show dun mad at npc_right
    dun "The empress firmly stated to not let any threats in."
    dun "This is a clear violation of rules, Larus!"

    "No clue added."
    show mc pout at mc_left
    mc "Aw... Mr. Crab really won't let us through..."
    show cory side at cory_left
    cory "Told ya, guppy. Let's see if one of us can talk some sense into him."
    jump ch3_crab_interactor_retry

label ch3_crab_mc_opt2:
    show mc o at mc_left
    show dun default at npc_right
    dun "Freshwater tadpoles are makin' our ocean colder just by breathin' up all the warm currents!"

    show mc default at mc_left
    mc "Uhm actually, mr.crab, according to marine biology…"

    show mc actually at mc_left
    mc "... water temperature is regulated by thermohaline currents and depth, not fish respiration."
    mc "So the freshwater species don't actually alter the ocean's temperature like that :D"

    show dun yeesh at npc_right
    dun "... What a load of carp!"

    show dun default at npc_right
    dun "Haven't heard of such nonsense in all my years clawin' this reef!"
    dun "That's prolly just a fake propaganda, lil' guppy."
    dun "Theories created by… by.."

    "Mr crab pauses, searching for words."

    show dun yeesh at npc_right
    dun "... by those fancy university intellectuals…"
    dun "... who doesn't know a damn thing about the real ocean livin'!"

    "No clue added."
    show mc o at mc_left
    mc "He doesn't seem very interested in marine biology..."
    show cory talk at cory_left
    cory "Heh, clearly. Let someone else handle this ol' crab."
    jump ch3_crab_interactor_retry

label ch3_crab_interactor_retry:
    menu:
        "Let Cory speak to Mr. Crab":
            jump ch3_crab_as_cory
        "Let Scyllarus speak to Mr. Crab":
            jump ch3_crab_as_scyllarus
        "Step back to the reef":
            jump ch3_night_explore.loop

label ch3_crab_as_cory:
    menu:
        "Can you help us talk to the empress?":
            jump ch3_crab_cory_opt1

        "Hold on, did you kidnap the sea bunny's family?":
            jump ch3_crab_cory_opt2

label ch3_crab_cory_opt1:
    show dun default at npc_right
    show cory talk_hu at cory_left
    "The crab squints his eyes, slamming one claw into the sand with an irritated click."

    dun "Who the fugu are you supposed to be?"

    show cory surprise at cory_left
    cory "Ay no hate, amigo! Lower the claws a bit, yeah?"

    show cory talk at cory_left
    cory "Look, we ain't enemies."
    cory "I actually got a lot of respect for saltwater culture."

    show cory talk_hu at cory_left
    cory "My primos back home are huge fan of Frank Ocean."

    show dun yeesh at npc_right
    dun "The eel does a singer's name got to do with it!"
    dun "You freshies are completely useless to this ocean, anyway."

    show cory talk_hu at cory_left
    cory "Ay, that's not true!"
    cory "We wash down all the good minerals from upstream to keep your corals bloomin'"

    show dun mad at npc_right
    dun "Frankly, my dear, I don't give a damn!"
    dun "My job is to block anyone tryin' to set claws or fins in here."

    call dunge_duel

    if _return != "win" and duel_result != "win":
        show dun mad at npc_right
        dun "Hah! Ya got a lot of nerve, but my claws are harder than your head, freshie!"
        show cory hurt at cory_left
        cory "Guh... that crab's tough..."
        show scy default at npc_right
        scyllarus "Do not fret, comrades! We can regroup and try again!"
        jump ch3_night_explore.loop

    jump ch3_crab_cory_duel_won

label ch3_crab_cory_opt2:
    show cory unimpressed at cory_left
    cory "A brute Crustacean.. Big claws…"
    cory "Did you lock up the sea bunny's whole family in there?"

    show dun yeesh at npc_right
    dun "Sea bunny family? Beats me!"
    dun "So many pest trynna start a rebellion around here, I lost count."

    show cory talk_hu at cory_left
    cory "The sea bunny family, cara."
    cory "The ones who were having a picnic under the acropora coral."

    show dun smile at npc_right
    dun "... oh, them. I ain' t kidnappin' nobody."
    dun "I'm holding those lethal biohazards in quarantine."

    show cory surprise at cory_left
    cory "Biolethal hazard… what are you even talkin about-"

    show cory upset at cory_left
    cory "Ya literally ate their baby and got a massive stomach ache.."
    cory "..because of their natural toxins."
    cory "No wonder they namin you Dunce."

    show dun mad at npc_right
    dun "Shut your darn mouth, you freshie."

    show dun yeesh at npc_right
    dun "It's DUNGE! D-U-N-G-I!"

    show cory disrespect at cory_left
    cory "My mane can't even spell his own name"

    show dun default at npc_right
    dun "NGHHRR SHUT IT!!"

    show dun mad at npc_right
    dun "That counted as assassination attempt of the officer of the reef!"

    show cory side at cory_left
    cory "....! mane you're outta your mind."

    show dun default at npc_right
    dun "..... dont tell me youre plottin' to overthrow the empress too?"

    show dun mad at npc_right
    dun "Bless your heart, Larus, but I gotta fight anyone who threatens to take down the regime!"

    call dunge_duel

    if _return != "win" and duel_result != "win":
        show dun mad at npc_right
        dun "Hah! Ya got a lot of nerve, but my claws are harder than your head, freshie!"
        show cory hurt at cory_left
        cory "Guh... that crab's tough..."
        show scy default at npc_right
        scyllarus "Do not fret, comrades! We can regroup and try again!"
        jump ch3_night_explore.loop

    jump ch3_crab_cory_duel_won

label ch3_crab_cory_duel_won:
    show dun yeesh at npc_right
    dun "Oof... holy barnacles, you got some heavy fins on ya, freshie..."

    show dun default at npc_right
    dun "Aight, aight! I yield! You beat me fair and square."

    show cory smile_hu at cory_left
    cory "Heh. Told ya, amigo. Never underestimate freshwater folks."

    show scy smile at npc_right
    scyllarus "Splendidly fought, Cory! Now, comrade Dunge, will you let us through?"

    show dun default at npc_right
    dun "Hmph. Fine. The path to the royal cavern's clear..."
    dun "If y'all are really plottin' to challenge the Empress, watch yer backs."
    dun "She holds a powerful golden scale... and she ain't gonna entertain sweet talk."

    "...! the golden scale?"

    scyllarus "We are deeply grateful for your cooperation, Dunge!"

    $ clue_golden_scale = True
    $ ch3_dunge_defeated = True
    $ mark_npc_explored("dunge")
    $ mark_npc_explored("teto")
    "Clue added: empress had the golden scale too."

    jump ch3_crab_post_resolution

label ch3_crab_as_scyllarus:
    menu:
        "Did you kidnap the seabunny's family?":
            jump ch3_crab_scy_opt1

        "We need to stop the empress!":
            jump ch3_crab_scy_opt2

label ch3_crab_scy_opt1:
    show scy default_om at npc_left
    scyllarus "I'm going to have to ask you to release them, Dunge!"

    show dun default at npc_right
    dun "Nuh uh! I ain't got a reason to!"
    dun "You're acting super weird Larus"

    show scy default at npc_left
    scyllarus "Imagine it's your family.. who's getting beheaded!"

    show scy default_om at npc_left
    scyllarus "Remember your Billy!"

    "Dunge's claws slam against the sea floor, kicking up a cloud of sand."

    show dun mad at npc_right
    dun "DON'T YOU DARE TALK ABOUT HIM!"
    dun "..... do not talk about my son…"

    show dun default at npc_right
    dun "That's.. thats exactly why… i aint letting any immigrant pass.."

    dun "Larus, you forgot what happened at the Old Canal Junction!?"
    dun "When those freshwater folks broke the damn barriers!!"
    dun "Then a sudden toxic flood destroyed our home.."
    dun "And the debris!! crushed Billy's claw before he could swim away!"

    scyllarus "That was a tragedy, Dunge!"
    scyllarus "But blaming an entire kind for the negligence of a rogue group is unfair!"
    scyllarus "Villainy is defined by actions, not by which side the border one is born!"
    scyllarus "We've been wrong, Dunce!"

    dun "......."

    scyllarus "this is our chance to atone!"
    scyllarus "I assure you, my friends here can make a change!"

    dun ".......... fine."
    dun "Imma… release the seabunny family…"

    scyllarus "Thank you, my dear comrade in claws!"
    scyllarus "Tell us.. Is there anything you know regarding the Empress' weakness?"

    dun "She holds a powerful golden scale."

    "...! the golden scale??"

    dun "Aint really sure if she'll even listen if you want to negotiate. But you can try it."
    dun "But the worst case-and it's most likely to happen- you gonna fight her."
    dun "That aint gonna be easy."

    scyllarus "I am forever grateful for your aid, Dunge!"

    dun ".... "
    "Dunge just nods."

    $ clue_golden_scale = True
    $ ch3_dunge_defeated = True
    $ mark_npc_explored("dunge")
    $ mark_npc_explored("teto")
    "Clue added: empress had the golden scale too."
    jump ch3_crab_post_resolution

label ch3_crab_scy_opt2:
    show dun default at npc_left
    dun "Whaddya mean 'stop the empress'??"
    dun "She's makin' the sea GREAT AGAIN!!"

    show scy default at npc_right
    scyllarus "I know but..!"
    scyllarus "I start to think that we've been wrong all this time!"
    scyllarus "My new friends here opened my eyes."
    scyllarus "Right, guppy, Cory? kakakaka!"

    dun "...you shell brained shrimp!"
    dun "What kind of radical leftist freshwater ideology did they feed into your brain?"

    scyllarus "This isnt about politics, Dunge!"

    dun "it IS about politics!"
    dun "Freshies be stealin our krills and tresspassin' our private reef property."
    dun "A few dead freshies is just the price of peace."

    scyllarus "I helped you cut em down, Dunge!"
    scyllarus "The.. Dead bodies…!"
    scyllarus "It haunts you, too, right?"

    dun "......."
    dun "........................"
    dun "Don't you go playing saint with me now."
    dun "… I aint gonna join your little party,"
    dun "........"
    dun "But if y'all wanna challenge her,"
    dun "You shoulda know that she holds a powerful golden scale."

    "...! the golden scale?"

    dun "Aint got a clue if she'll even entertain your sweet talk if you try negotiatin."
    dun "But yall can try."
    dun "Now get off before I change my mind!"

    scyllarus "We deeply appreciate it, Dunge!"

    $ clue_golden_scale = True
    $ ch3_dunge_defeated = True
    $ mark_npc_explored("dunge")
    $ mark_npc_explored("teto")
    "Clue added: empress had the golden scale too."
    jump ch3_crab_post_resolution

label ch3_crab_post_resolution:
    if not item_collected:
        show mc o at mc_left
        mc "Look, Mr. Cory! There's some bright red seaweed over by the reef!"
        mc "We should take a look around the reef before going inside!"
        "The path to the Empress's lair is open, but we should explore the reef and collect the red seaweed first."
        jump ch3_night_explore.loop
    else:
        "The path to the Empress's lair is open."
        menu:
            "Enter the Crustacean Empress's Lair":
                jump ch3_boss_intro
            "Look around the reef first":
                jump ch3_night_explore.loop

label ch3_boss_intro:
    hide mc
    hide cory
    hide scy
    hide dun
    scene ch3_night
    with dissolve

    show scy laugh at npc_right
    scyllarus "Welcome my friends to the humble abode of crustacean empress the VIII!"

    show mc excited at mc_left
    mc "Woah!! It's so.. Red!"

    show scy smile at npc_right
    scyllarus "Yes! Red is her favored color after all!"

    hide mc
    show mc serious at mc_left
    mc "But how can she know colors..? Aren't pistol shrimps blind?"

    scyllarus "They're almost blind, actually! And she's just told that her color is red, and it immediately become her favorite!"

    show cory smile_hu at cory_left
    cory "And the eighth you say..? She gon rule for 36 years?"

    "Abruptly—"

    hide mc
    hide cory
    hide scy
    show teto default
    gob "Fall to your knees and tremble before Her Majestic Majesty, the one and only!"
    gob "Her Majesty Empress Crustacean the VIII!"

    emp "Ah, a visitor?"
    emp "Kekeke! That's me, that's me! I'm Crustacean Empress VIII!"

    hide teto
    show goby struck at npc_left
    show teto default at npc_right
    gob "Mhm, the best empress on the crustacean line~!"

    emp "Oh you humble me so, my right hand!"

    gob "Ah but your greatness must be known across the seven seas~!"

    emp "Across seven seas you say?!"

    gob "I am merely speaking truth, your Majesty!"

    hide goby
    show cory unimpressed at cory_left
    cory "Are all crustaceans like this…?"

    hide cory
    show goby surprise at npc_left
    emp "WHAT?! You dare question the might of an empress?!"

    gob "They seem to have a death wish, your majesty.."

    hide goby
    show teto gun_smirk
    emp "Then fulfill your wish I shall! Wouldn't the majestic I be the fairest?!"

    play sound "audio/attack_2.mp3"
    $ renpy.pause(0.2)
    play sound "audio/attack_1.mp3"

    hide teto
    show cory surprise at cory_left
    cory "WOAH WOAH-! CHILL OUT YOUR CRUSTACEAN MAJESTY! PUT THE GUN DOWN"

    show scy default_om at npc_right
    scyllarus "Wait, don't!! I beg for mercy on every one of my ten legs, your majesty!"

    hide cory
    show teto gun_smirk at npc_left
    emp "Ah, If it's not my strongest soldier Scyllarus…"
    emp "What petty excuse do you have in defense?"

    hide scy
    show goby disgust at npc_right
    gob "I don't think there was ever an excuse to bring in dirtwater.."

    hide goby
    show scy default_om at npc_right
    scyllarus "I beg of Your Majesty and your highly regarded right hand!"

    emp "Oh oh! Are you here to spread marvelous news?! Have you found and fetched me the great golden fish?!"

    scyllarus "I-! No.. not yet your majesty.. I still have yet to acquire the golden fish.. but!"
    scyllarus "My dear comrades here have a proposition that'll make it worthwhile!"

    hide teto
    show teto upset at npc_left
    emp "Proposition..? Bleehh my ears are made to hear only the best of things not the boring ones.."

    hide scy
    show goby annoy at npc_right
    gob "Their filthy words are not for your ears your majesty"
    gob "Let me decide if it is worthwhile.. As you say it"

    hide goby
    show scy default_om at npc_right
    hide teto
    show teto laugh at npc_left
    emp "Hah! You be my filter, my highly regarded right hand."
    emp "I shall busy myself with my new golden toy!"

    jump ch3_boss_negotiation

label ch3_boss_negotiation:
    hide mc
    hide cory
    hide scy
    hide teto
    call screen choose_interactor(
        "Choose who should negotiate with the Empress!",
        "Each character will present their own proposal"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_boss_negotiate_as_mc
    elif selected_questioner == "cory":
        jump ch3_boss_negotiate_as_cory
    else:
        jump ch3_boss_negotiate_as_scyllarus

label ch3_boss_negotiate_as_mc:
    show mc happy at mc_left
    mc "Hi!! Your highness goby fish!"

    show goby default at npc_left
    gob "You have 10 seconds to speak your lies"
    gob "Before my spear goes through you."

    show mc shock_hu at mc_left
    mc "ah only t-ten seconds?! oh no! oh no!"

    show goby annoy at npc_left
    gob "There goes your two seconds."

    show screen ch3_boss_negotiation_timer(8.0)

    menu:
        "\"I propose crustaceans and every creature in the sea hold hands until the end of time!\"":
            hide screen ch3_boss_negotiation_timer
            jump ch3_boss_negotiate_mc_opt1

        "\"I propose that the crustaceans apologize to everyone in sea!\"":
            hide screen ch3_boss_negotiation_timer
            jump ch3_boss_negotiate_mc_opt2

        "\"I think this might be a great addition to your red collection!\" (Give red seaweed)" if has_red_seaweed:
            hide screen ch3_boss_negotiation_timer
            jump ch3_boss_negotiate_mc_opt3

label ch3_boss_negotiate_mc_timeout:
    hide screen ch3_boss_negotiation_timer
    show goby surprise at npc_left
    gob "Time's up! You hesitated, dirtwater!"
    mc "W-wait! I have an answer! Don't poke me with the spear!"
    jump ch3_boss_negotiate_mc_opt1

label ch3_boss_negotiate_mc_opt1:
    show mc default at mc_left
    show goby default at npc_left
    gob "..."
    gob "Unlike a defect breed like you.."
    gob "We have no hands you speak of"
    gob "All we have are chelipeds"

    show mc o at mc_left
    mc "But you're not even a crustacean! What you have are fins!"

    gob "...!"

    show mc o at mc_left
    mc "If you can command an army of crustaceans"
    mc "If you can hold the empress' great chelipeds.."

    show mc pout at mc_left
    mc "What makes you stop at holding other fishes' fins..?"

    show mc default at mc_left
    mc "Besides.. Goby fishes have relatives in freshwater!"

    gob "I'm not a part of that filthy kind."
    gob "You think you're so smart because you've read a few books?"
    gob "Save those futile fun facts for afterlife"
    hide goby
    jump ch3_boss_negotiate_mc_after

label ch3_boss_negotiate_mc_opt2:
    show mc o at mc_left
    mc "Everyone we met seemed really sad because of what the crustaceans did.."
    mc "Some lost their families. Some are scared to even leave their homes."

    show mc happy at mc_left
    mc "Therefore, saying sorry would be a good start?"
    mc "Maybe then they all would be kind and respect you too"

    show goby surprise at npc_left
    gob "The audacity!"
    gob "You demand an apology from the rulers of the sea?"

    show mc pout at mc_left
    mc "But order isn't supposed to make everyone scared!"

    gob "What the sea thinks is never worth our concern!"
    hide goby
    jump ch3_boss_negotiate_mc_after

label ch3_boss_negotiate_mc_opt3:
    show mc happy at mc_left
    show goby surprise at npc_left
    gob "...!"
    gob "That's.. The great empress' favorite!"

    show teto laugh at npc_right
    emp "DID SOMEONE SAY RED SEAWEED?!"

    show mc default at mc_left
    mc "Mhm! I picked it up on the way here! As a peace offering!"

    emp "How thoughtful! Gimme it!"

    play sound "audio/attack_1.mp3"
    "At the blink of an eye with a discreet bang! The seaweed vanished.. Now already a crushed victim under the shrimp's eager munch teeth"

    show goby annoy at npc_left
    gob "Your Majesty, please remember that they are here to negotiate."

    emp "I know! I can eat and listen at the same time."
    emp "munch munch munch…"

    show mc shock at mc_left
    "Did she use her pistol to steal the seaweed from my hand without injuring me?"

    show mc o at mc_left
    "Whatever it was, I need to see it again! Maybe I should provoke her more?"

    gob "Ah your majesty- there's a seaweed on your cheek"

    emp "Really?! Help me get rid of it my Gobby!"

    gob "Affirmative.."

    show mc happy at mc_left
    mc "Yaaay true love wins!"

    show mc excited at mc_left
    mc "Which means Freshwater and Saltwater can live together in peace now!!"

    gob "T-true love-?!"
    hide goby
    hide teto
    jump ch3_boss_negotiate_mc_after

label ch3_boss_negotiate_mc_after:
    show goby surprise at npc_left
    gob "We have to obliterate these scums at once, Your Majesty"

    show teto gun_smirk at npc_right
    emp "Hah! Count me in on the fun! I've got to test my new found!"

    show goby default at npc_left
    gob "My empress, I'm afraid these filth isn't worth your power…"

    hide teto
    show teto pout at npc_right
    emp "Hmph! But I wanna use my brand new golden toy!"

    "Ms Empress Shrimp pulls out what it seems a golden scale from under her robe. Its shimmer glistens in rainbows under the light."

    show mc shock at mc_left
    mc "The golden scale.. she really has it"

    gob "Then unleash nightmares that follows them to hell, Your Majestic Majesty"

    show teto gun_smirk at npc_right
    hide goby
    show cory side_close at cory_left
    cory "Looks like we have no choice but to fight fins and gills, ay?"

    jump ch3_boss_battle

label ch3_boss_negotiate_as_cory:
    hide teto
    show goby default at npc_right
    gob "You got exactly 1.8 seconds."

    show cory surprise at cory_left
    cory "...!"
    cory "Might as well say fugu off with your bullcarp shrimp regime-!"

    show goby surprise at npc_right
    gob "Enough! That was more than 3 seconds!"

    play sound "audio/attack_3.mp3"
    "My eyes widen into saucers as it registers a flash of red. The goby's spear grazes past Mr.Cory, tearing through flesh but missing anything vital. A warning, and nothing more."

    show cory hurt at cory_left
    cory "Guh-!"

    show mc shock_hu at mc_left
    mc "Mr. Cory…!!"
    mc "WHY WOULD YOU SAY THAAAT MR CORYYY!!"

    hide goby
    show teto default at npc_right
    emp "Oooh a rebel I sense?!"
    emp "Kekeke! That bravery of yours, I quite like it!"
    emp "It'll make your screams echo all the sweeter."

    hide teto
    show goby surprise at npc_right
    gob "Now face agonizing torture, worth three lifetimes over, dirtwater."

    hide goby
    show scy sepet at npc_right
    scyllarus "Frankly! I don't think I can defend you on this one, my questionable friend!"

    jump ch3_boss_battle

label ch3_boss_negotiate_as_scyllarus:
    show goby surprise at npc_right
    gob "Make it count, Scyllarus."
    gob "I'm only hearing you out because you're our precious strongest personnel"
    show goby default at npc_right
    gob "Having you against us will be disadvantageous for both of us."

    show scy default_om at npc_left
    scyllarus "I'll make it justifiable!"

    menu:
        "\"We propose a future where freshwater creatures are no longer detained simply for existing in the sea\"":
            jump ch3_boss_scy_opt1

        "\"We propose that the crustaceans rule with honor again, not fear!\"":
            jump ch3_boss_scy_opt2

        "\"Calm yourself down first your highness!\" (Give red seaweed)" if has_red_seaweed:
            jump ch3_boss_scy_opt3

label ch3_boss_scy_opt1:
    show goby default at npc_right
    gob "Oh? You'd bring numbers to a fight, Scyllarus?"

    show scy default_om at npc_left
    scyllarus "By statistics! Seafolks' crime rates are still higher than the freshwater immigrants!"
    scyllarus "With that data in mind.. we shouldn't have detained freshwaters for simply setting fins into sea!"
    scyllarus "And to keep punishing an entire species for the sins of a few is neither just, nor even strategic!"

    show goby annoy at npc_right
    gob "Even when those are facts.."
    gob "You can't dismiss that incident.."
    gob "In which disaster were caused by those filthy freshwaters?"
    gob "Fishes, mollusks, our own kind — all of them paid for what happened at the Old Canal Junction."
    gob "What we're doing are simply precautions"
    gob "So tragedy doesn't repeat itself…"

    show scy default at npc_left
    scyllarus "But that was 10 years ago, general!"
    scyllarus "Longer than both you and the empress' ages combined!"
    scyllarus "I was there when it happened…"
    scyllarus "And it was also a freshwater that helped me through that time…"
    scyllarus "So don't tell me they're all the villains in this story!"
    scyllarus "I refuse to believe that anymore!"
    jump ch3_boss_negotiate_scy_after

label ch3_boss_scy_opt2:
    show scy shy at npc_left
    scyllarus "It truly pains me to say this but…!"
    scyllarus "We were once honored, loved. Well mannered."
    scyllarus "Crustaceans are of the supportive, enthusiastically kind!"
    scyllarus "Our way of showing it might come off as rough but..!"
    scyllarus "It is necessary to fight for the things we care for!"
    show scy default at npc_left
    scyllarus "Now all I've seen from seafolks are that of disdain and fear of us.."
    scyllarus "Is that really what our kind wants to be known as..?"
    scyllarus "A ruthless, impudent dictatorship that easily tramples the life of others..!"

    show goby default at npc_right
    gob "You talk all high and mighty.."
    gob "Yet how many died pleading at your own claws, Scyllarus?"

    scyllarus "....!"
    scyllarus "That's why I…!!"

    show goby annoy at npc_right
    gob "Your fierce claws.. are not made for compassion is it?"
    gob "You're a killing machine."
    gob "One that would swipe through anything in its path, crustacean or not, if ordered to.."
    gob "You're not one to propose for harmony."

    scyllarus "..."

    show mc pout at mc_left
    mc "YOU'RE WRONG!!"

    show goby default at npc_right
    gob "oh..?"

    show mc holdcry at mc_left
    mc "Mr. shrimp- Mr.. Mr Sc... Cy.. Clarus has never once hurt me!"

    hide scy
    show cory talk at cory_left
    cory "It's Scyllarus guppy…"

    hide cory
    show scy default at npc_left
    show mc sad_hu at mc_left
    mc "He always touches me super carefully! I've never got any scratches see!"

    "I extended both arms outwards, showing off every unscratched, unbruised inch of them."

    show mc sad at mc_left
    mc "He's.. he's … always trying his best to not hurt anyone…"

    scyllarus "....guppy"

    hide scy
    show cory talk at cory_left
    cory "What they said!"
    cory "Our big ol friend here is not what you claim a killin machine!"
    cory "He's just stuck under a regime he can't escape from.."
    cory "He's not killin for fun, it was yous who put the weapon in his claws in the first place!"

    hide cory
    show scy shy at npc_left
    scyllarus "Cory…!"

    gob "Foolish dirtwaters! You just haven't witnessed his true side yet!"

    show mc happy at mc_left
    mc "Maybe so! But.. I trust the side of him I have seen!"
    jump ch3_boss_negotiate_scy_after

label ch3_boss_scy_opt3:
    show scy smile at npc_left
    scyllarus "My friend here picked out the brightest, freshest red seaweed for you to feast!"

    hide goby
    show teto laugh at npc_right
    emp "Oh ho ho don't mind if I do~!!"
    emp "Mmmn.. this is why you're the best Scyllarus..!"

    hide teto
    show goby surprise at npc_right
    gob "He's the best…? But your highness you told me that I'm-"
    show goby disgust at npc_right
    gob "sigh.. please don't play favorites in front of the enemy, your majesty."

    hide goby
    show teto default at npc_right
    emp "shh what does he have to say! Speak my esteemed soldier Scyllarus!"

    show scy default at npc_left
    scyllarus "Right now.. we are at a compromised position, your majesty.."
    scyllarus "The seafolks hates and fear us, the freshwaters no longer trust us either.."
    scyllarus "This isn't a war we can win by claws and fear alone!"
    scyllarus "So with that in mind.. I propose that.."
    scyllarus "We go back to Her Majesty the VII's system.."
    scyllarus "We earn the sea's trust instead of demanding its fear!"

    show teto upset at npc_right
    emp "My.. mother?!"
    emp "YOU FOOLISH SAND-FILLED BRAIN LUDICROUS IMBECILE!!"
    show teto gun_upset at npc_right
    emp "I'm sick of it! My mother's softness cost us everything, and you want me to make that same mistake?!"
    emp "CRUSTACEANS!! Detain them at once!"
    jump ch3_boss_negotiate_scy_after

label ch3_boss_negotiate_scy_after:
    hide teto
    show goby default at npc_right
    gob "This is exactly why you were never fit to be a general."
    gob "Sand for brains, One sob story from a guppy and you fold like a cheap net."
    gob "That's not honor, Scyllarus. That's just being easy to manipulate."

    show scy default_om at npc_left
    scyllarus "I'd rather be wrong for believing in people than right for fearing them!"

    hide goby
    show teto default at npc_right
    emp "Heh! Time to answer the most asked question then!"
    emp "The ultimate showdown…!!"

    show mc excited at mc_left
    mc "Oh my oh my!"

    emp_mc "PISTOL SHRIMP VS MANTIS SHRIMP!! YOU WON'T BELIEVE WHO WINS?? (GONE WRONG)"

    show teto gun_smirk at npc_right
    emp "KEKEKEKE!! Oh how I adore you! Too bad I gotta kill you now!"

    hide scy
    show cory upset at cory_left
    cory "Aye! This is no play guppy! Get your ass ready for a fight!"

label ch3_boss_battle:
    show cory talk at cory_left
    cory "Hah that means nothing, we got one ourself too! Show em guppy!"

    emp "Oh-ho! Well that makes it the more interesting…!"
    emp "May the best gold bearer wins! Spoiler: it is I, most obviously!"

    call empress_duel

    $ ch3_empress_defeated = True
    jump ch3_ending

label ch3_ending:
    hide mc
    hide cory
    hide scy
    scene ch3_night
    with dissolve

    show goby surprise at npc_left
    gob "Your majesty!!"

    show teto upset at npc_right
    emp "gooobyyy…"

    show goby default at npc_left
    gob "Hark! We must flee at once!"

    emp "FLEE?? that's bullshriiimp!! that's what a coward does we're no cowards gobyyy! Waaah!"

    gob "My apologies your majesty, but your survival is my priority."
    gob "You have won, Scyllarus.. fair and square."
    gob "I might be a right hand of a tyrant.. but I still have dignity left in me."

    show teto gun_upset at npc_right
    emp "OI!! ARE YA CALLING ME UNDIGNIFIED??! A TYRANT TOO?!"
    emp "I'LL GET YOUR PETTY ASS SCYLLARUUUUS!!! I STILL HAVE THE GOLD SCALE WITH ME-!"

    hide goby
    show cory smile at cory_left
    cory "Heh, you mean this thing?"

    show teto upset at npc_right
    emp "WHA-! WHEN DID YOU-! GHRRRR STUPID FRESHWATER THIEF!! ROT IN THE DEEPEST PIT OF DEEP FUGGING SEA- MMPH-?!"

    "A fin gently pressed the former empress' mouth shut"

    hide cory
    show goby default at npc_left
    gob "Please excuse us.. If fate allows, we'll cross path once more"
    show goby disgust at npc_left
    gob "And when that time comes.. We'll have our fitting revenge"
    hide goby
    hide teto

    "Miss General Goby flashes a rueful smile at us, before hauling her still-sputtering empress off into the deep, a trail of bubbles marking their retreat."

    show cory talk at cory_left
    cory "Heh.. didn't thought gob's still have some sense like that"

    show scy proud at npc_right
    scyllarus "Hm! I always knew General had a sense of justice in her!"

    show scy sepet at npc_right
    scyllarus "But her devotion for the empress weighs heavier…"

    show scy smile at npc_right
    scyllarus "Hah! Now that's over all there is to make a statement of apology to the seafolks and…"

    show mc excited at mc_left
    mc "Mr Shrimp look!! Woah, so many people gathered at the front!"

    show scy surprise at npc_right
    scyllarus "Hm..?!"

    crowd "Thank you weird looking guppy!"
    crowd "We love you!!"
    crowd "Yeah! You're our hero!"

    show mc happy at mc_left
    mc "We.. couldn't at all do this without Mr. Shrim- Mr. Cyllarus' help!"
    mc "So I'd like.. for all of you to thank him too!"

    show cory talk at cory_left
    cory "What they said! Turnin' around over for betrayal was never an easy task!"
    cory "He's the one that showed us the path, protected us, and defy the empress' ruthless ruling!"

    show scy surprise at npc_right
    scyllarus "B-Betrayal?! Outrageous! What I did was what was right!"

    crowd "Thank you Scyllarus!!"
    crowd "WE LOVE YOU LARUUUS!!"
    crowd "I'M GOING TO NAME MY GUPPY AFTER YOU SCYLLARUUUS!!"
    crowd "PLEASE PLEASE PLEASE PLEASE HAVE MY FIRST NEWBORN SCYLLARUS!!"
    crowd "Thank you mr big shiiiimp!"

    show scy proud at npc_right
    scyllarus "W-WOAH! I've never received this much love from a crowd!"
    scyllarus "Thank you everyone! It is my greatest honor to be aid of the sea!!"
    scyllarus "Seeing smiles that bloom from the actions of my own claws.."
    scyllarus "I've never felt so powerful! KAKAKA!"

    hide cory
    show dunge default at npc_left
    dun "Larus!"

    scyllarus "Ah, my comrade Dunge, crustaceans! I-!"

    "Mr Clarus' words were abruptly cut upon spotting the crab's lowered head, claws tucked close in a way Mr Shrimp had never seen before."
    "An entire army of crustaceans follow through crabs, mantis shrimps, lobsters, hermits still dragging borrowed shells kneel in perfect unison before him, chelipeds pressed flat against the sand"

    dun "We're sorry for all the troubles we caused..!"
    dun "And now that Her Majesty's fallen.. it's only right the crown goes to the strongest soldier left standin'."

    crustaceans "Your Majesty Scyllarus!!"
    crustaceans "All hail the new empire!"

    show scy default_om at npc_right
    scyllarus "...."
    scyllarus "Everyone, please, stand up, and listen clear!"
    scyllarus "I'm no emperor, and I have no interest in being crowned one!"

    dun "But Larus.. you beat her fair and square. That's how it's always worked 'round here."
    dun "Strongest claw makes the rules."

    show scy sepet at npc_right
    scyllarus "Then let today be the day that rule dies with her."

    "The crowd murmurs, uncertain, still bowed."

    show mc o at mc_left
    mc "Ohh! Does that mean Mr. Shrimp is king now?!"

    show scy pout at npc_right
    scyllarus "It's Scyllarus, and no, guppy!"
    scyllarus "Crustacean Empress the VII.."
    scyllarus "She told me once, that the sea belongs to no one and everyone at once.."
    scyllarus "That we, as merely one of its many inhabitants, were never given the right to rule it.."
    scyllarus "Only the responsibility to help it thrive."
    scyllarus "and her dethrone was.. that of her own choice.."
    scyllarus "But her daughter took the chance for a ruling instead!"

    show mc default at mc_left
    mc "You'd make a great king though mr Clarus.."

    scyllarus "It's Scyllarus!! And even if I would.. I have no interest in a throne built on someone else's exile."
    scyllarus "Now, I shall honor her wishes! And let the sea be an free safe space!"

    "Slowly, claw by claw, the army rises. Uncertain, murmuring amongst themselves, but no longer kneeling."

    dun "...No Man's Land, huh."
    dun "Guess that means I got no orders left to follow."
    dun "I'm steppin' down too, then. No more green corals. No more borders. Not on my claws, not anymore."

    show scy smile at npc_right
    scyllarus "That's exactly what it means! From today onward, Seafolks, whether it's fins, chelipeds, claws, flippers, spikes..! Whatever your appendages are!"
    scyllarus "We must all help each other! Make the sea a comfortable, safe living space for all!"
    scyllarus "And to my beloved comrades… who's helped me realize.."

    "Mr Shrimp turns to face us, his usual boastful grin softened into something quieter."

    scyllarus "Cory.. you called me your mate before you ever called me an ally."
    scyllarus "You saw a friend where everyone else only saw a weapon."
    scyllarus "I don't think I've properly thanked you for that."

    show scy default_om at npc_right
    scyllarus "And guppy.."
    scyllarus "The two of you gave me back a version of myself I thought I'd lost the day I put on this armor."

    show scy excited at npc_right
    scyllarus "So! From now on, I.. vow to be under your command!"

    show mc excited at mc_left
    mc "REALLY?! mm theeen…"
    mc "Can I take 30 rainbow algaes and 40 red seaweeds?!"
    mc "oh oh maybe.. 35 clams too…"

    hide dunge
    show cory upset at cory_left
    cory "WHAT-?! Don't listen to them larus!"
    cory "You're not ours to command! you're our mate!"
    cory "And mates don't tell each other what to do!"

    show scy surprise at npc_right
    scyllarus "MATE?! Mate! You say….!"
    scyllarus "Hmm.. and you say \"our\" which includes the guppy.."
    scyllarus "I'm sorry but I must decline! I'm not one to be interested in young guppies!"
    scyllarus "But my dear comrade Cory however, If you are committed enough…!"
    scyllarus "I.. might as well give us a try!"

    show cory surprise at cory_left
    cory "....??!"
    cory "NAY AY AY AY YOU'VE GOT THE WRONG IDEA CARA!"
    cory "I MEANT COMRADES!! AIN'T NO INTIMACY PARTNER!!"

    show scy laugh at npc_right
    scyllarus "OH..!!"
    scyllarus "KAKAKA! Very well a comrade I should be!"
    scyllarus "And as for the guppy…!"
    scyllarus "My apologies but I'm still not letting you exploit the sea in whatever shape or form!"

    show mc pout at mc_left
    mc "ueeeeh.. :("

    show cory talk at cory_left
    cory "But now we got two of these huh.."

    show mc happy at mc_left
    mc "I wanna keep it!"

    show cory talk at cory_left
    cory "feel anythin different?"

    show mc excited at mc_left
    mc "woah..! I.. I can hear your voices clearer and and!"
    mc "and.. my skin feels.. Less pruny now!"
    mc "It's as if I'm becoming more and more of a fish! :D"

    show scy laugh at npc_right
    scyllarus "KAKAKA! Good for you!"

    show mc o at mc_left
    mc "mnn.. I wanna try something"

    "I took off the weighing glass on my head"

    show cory talk at cory_left
    cory "Don't push yourself too hard alright?"

    show mc shock at mc_left
    mc "... nguhk..!"
    mc "it's.. the waterbreathing time! It was only for a few minutes before"
    mc "now I can breathe just fine!"

    hide scy
    show gator smile at npc_right
    gator "ouuu shiiii.."
    gator "you all look nasty… need help?"

    show mc excited at mc_left
    mc "Ms. Gator!! We meet again!"

    gator "mm yep what I say about catching that golden fish before you do"
    show gator annoyed at npc_right
    gator "but frankly? I just.. lost motivation midway.."
    gator "waaaay too much of a hassle.."

    show cory side at cory_left
    cory "Gatha.."

    show gator default at npc_right
    gator "But I did get this.."
    gator "As a proof that I did get to it hmph!"
    gator "you can't be saying shrimp like I was too slow or anythin now"

    show mc o at mc_left
    mc "wait! Where did you get this and when?"
    mc "We haven't seen the fish lately.."

    gator "it's just riiiight there"

    show gator surprised at npc_right
    gator "I don't get why you're so adamant on getting it guppy.."
    gator "But best of luck to ya alright"

    $ ch3_chapter_complete = True

    hide mc
    hide gator
    hide cory
    with dissolve

    scene black with fade
    "END OF CHAPTER 3"

    jump chapter4_start
