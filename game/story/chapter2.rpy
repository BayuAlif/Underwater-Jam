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
        full
        right
        surprise
    mc "A tiny krill!"

    show krill:
        xpos 0.45
        ypos 0.62
        anchor (0.5, 0.5)
        zoom 2.0
        float_idle
    tinykrill "Eah!"

    show cory disrespect:
        full
        leftish
    cory "Heh.. you could say it's.. One in a krillion"

    show krill:
        xpos 0.45
        ypos 0.62
        anchor (0.5, 0.5)
        zoom 2.0
        vibrate(3)
    tinykrill "{size=20}Your joke sucks ass!{/size}"

    show cory unimpressed:
        full
        leftish
    cory "...."
    cory "... I say we feed that thing to a fish, guppy"

    show mc shock:
        full
        right
        sink
    mc "Aw shucks, do we really have to krill it mr cory? :("

    show krill:
        xpos 0.45
        ypos 0.62
        anchor (0.5, 0.5)
        zoom 2.0
        vibrate(4)
    tinykrill "Suffer in eternal torment both of you!"

    $ add_item("tiny_krill")
    hide krill with dissolve
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
    show mc o:
        full
        duo_right
    show cory talk_hu:
        full
        duo_left
    mc "Mr. Cory, do you know what this black lump is?"

    cory "Mmmn.. no clue."

    show cory unimpressed2:
        full
        duo_left
    cory "Almost looks like poo to me, you better drop that thing guppy."

    show mc shock:
        full
        duo_right
        sink
    mc "Yuck! it smells… weird."

    ghost "You shouldn't be carrying things you don't understand."

    show cory smile_hu:
        full
        duo_left
    cory "Yeah.. that's right guppy.."
    cory "Finally, Some self preservation in ya!"

    show mc o:
        full
        duo_right
        surprise
    mc "That.. wasn’t me…"

    "The water around us suddenly grows eerily still."
    "Faint glow pair of eyes emerges from the darkness."

    show ghost deadpan:
        full
        duo_left
        float_idle
    with dissolve

    show cory surprise:
        full
        duo_left
        surprise
        vibrate
    cory "GYAAAAAAA—"

    "Mr Cory jumped and immediately cowers behind my back with a loud screech"

    show cory side_close:
        full
        farright
        toleft
        sink
    with move

    show mc o:
        full
        duo_right
        surprise
    mc ":o"

    show mc excited:
        full
        duo_right
        jumpmc
    mc "Woah! What are you?"

    show ghost default:
        full
        duo_left
        float_idle
    ghost "A fish."

    show mc pout:
        full
        duo_right
    mc "I can see that."

    ghost "Then you needn’t know more."

    show mc o:
        full
        duo_right
    mc "Why are you here… fish?"

    show ghost side:
        full
        duo_left
        float_idle
    ghost "You were meant to find me."

    show ghost close:
        full
        duo_left
        float_idle
    ghost "But this second is not the time"
    ghost "We shall meet again.. very soon."

    show ghost side:
        full
        duo_left
        float_idle
    ghost "Or perhaps.. we have met before."

    hide ghost with dissolve

    show mc happy:
        full
        duo_right
    mc "Okay! Looking forward to meeting you again, fish!"
    mc "Mr Cory you can come out, it's fine now."

    show cory upset:
        full
        duo_left
    with move
    cory "What the eel even was that?!"
    cory "Straight out of deep sea I swear!"

    $ focus()
    $ add_item("coal_tar")
    "I obtained: a mysterious stinky black lump"
    return

<<<<<<< HEAD
=======
label chapter2_ghostfish_questions:

    hide mc
    hide cory
    call screen character_question_select("Ghostfish")
    $ selected_questioner = _return

    if selected_questioner == "mc":

        show mc o at mc_left
        mc "Are you a ghost fish or a fish ghost?"

        show ghost default at npc_right
        ghost "Brave little one…"

        show ghost deadpan at npc_right
        ghost "I believe you have far better questions to ask…"

        show ghost side at npc_right
        ghost "Perhaps of.. the golden fish.."
        ghost "You haven't asked that for a while.."

        show mc shock at mc_left
        mc "ahh! You're right. but.. how did you know that?!"

        show ghost close at npc_right
        ghost "I am a fish who listens.."

        menu:
            "Do you know why mr shrimp is blocking the path?":

                show mc o at mc_left
                show ghost default at npc_right
                ghost "The mantis shrimp is but a lost cause…"

                show mc shock at mc_left
                mc "Huh?? What do you mean..?"

                show ghost close at npc_right
                ghost "Everyone mistakes anger for strength."
                ghost "Do not mistake an obstacle for an enemy."

                show mc excited at mc_left
                mc "So he's a friend?! A potential friend!"
                mc "We don't have to fight it then!"

                show ghost side at npc_right
                ghost "...I think you should know what you're fighting first."

                show ghost default at npc_right
                ghost "Perhaps a coal tar would help seek your answer"

                show mc o at mc_left
                mc "Whuh? But what's a coal tar… I don't think I've heard of it"

                show ghost close at npc_right
                ghost "A strong smelling black lump"
                ghost "Mix it with something of hardened shell and it will weaken the shrimp"

                show mc o at mc_left
                mc "But.. you just told us not to fight the shrimp..? Why do we need to weaken it?"

                show ghost deadpan at npc_right
                ghost "I never said so.. It is you who claimed that conclusion"

                show mc default at mc_left
                mc "Oh.. right! So we still need to fight it then?"

                show ghost side at npc_right
                ghost "Perhaps so…"

                $ add_clue("The Mantis Shrimp may not need to be defeated. Find out what he wants.")
                $ add_clue("Coal Tar may be useful against the Mantis Shrimp.")

            "Ms fish ghost, have you seen a super sparkly golden fish?":

                show ghost side at npc_right
                ghost "Yes I have…. It went in the direction of the sea…"

                show ghost default at npc_right
                ghost "Tell me, why do you choose to pursue the sacred cursed fish?"

                show mc default at mc_left
                mc "Because it's shiny! and not in the way.. most goldfishes shine"
                mc "The shape is weird too like it's from another universe"

                show ghost deadpan at npc_right
                ghost "....and?"

                show mc happy at mc_left
                mc "Ah I also have one of its scales, it gave me the power to speak to fishes! And to breathe underwater for a little longer!"

                show ghost default at npc_right
                ghost "Hm. And your presence… it's the same as ours, despite being human."
                ghost "Remarkable… that you can withstand its power at all."

                show mc excited at mc_left
                mc "So it really is a magic fish that gives you superpowers?!"

                show ghost side at npc_right
                ghost "…The fish you pursue is no ordinary creature."
                ghost "It only surfaces when the sea is dying, when the waters are closest to ruin."

                show ghost close at npc_right
                ghost "A final gift from the Goddess of sea, left behind after her retirement… so the sea could still right itself, even without her."

                show ghost default at npc_right
                ghost "But that gift was meant for one of us. A creature of the sea. Not a visitor to it."

                show mc shock at mc_left
                mc "Ah… but what if it fall into the wrong hands?"

                show ghost close at npc_right
                ghost "That is something only fate can answer."
                ghost "If it must be that way, then we can only watch as it happens."

                show ghost deadpan at npc_right
                ghost "The sea knows what it deserves."

                menu:
                    "If it's so powerful why not every fish in the sea chase it?":

                        show mc o at mc_left
                        show ghost close at npc_right
                        ghost "Few even know this fish exists… fewer still know what it can do."
                        ghost "It doesn't announce itself. It doesn't wait to be found."

                        show ghost side at npc_right
                        ghost "The sea decides who's worthy long before they ever see it."

                        show mc happy at mc_left
                        mc "You know so much of it! You must be suuuper worthy of having it no?"

                        show ghost close at npc_right
                        ghost "I'm but a messenger, brave one…"

                    "Do you think I'm worthy of its power?":

                        show ghost side at npc_right
                        ghost "...."

                        show ghost deadpan at npc_right
                        ghost "I believe only your heart can answer that question."

                        mc "I.. don't know…"
                        mc "All i want is to be a fish…"

                        ghost "... Then maybe that's all the sea needs.."

    else:

        show cory surprise at cory_left
        cory "M-me?! Why does it have to be me?!"

        show ghost side at npc_right
        ghost "you have a thousand questions running around in your head.."

        show ghost deadpan at npc_right
        ghost "yet your fear.. stops you from asking."
        ghost "Like shadows fleeing a light that follows without moving."

        show cory unimpressed2 at cory_left
        cory "w-what that mean yo…"

        show ghost mweheh at npc_right
        ghost "ask away, I promise I don't bite. much"

        show cory upset at cory_left
        cory "WHADDYA MEAN MUCH?!"

        menu:
            "do ya know why.. the shrimp is… stopping everyone from passing?":

                show cory talk_hu at cory_left
                show ghost close at npc_right
                ghost "perhaps I do."

                show ghost side at npc_right
                ghost "but why should I tell you"

                show cory side at cory_left
                cory "because! We-we needa know!"

                show ghost deadpan at npc_right
                ghost "not an enough reason…"

                show cory side_close at cory_left
                cory "because- we.. because the guppy needs to get to the- the golden fish!"

                show ghost side at npc_right
                ghost "hmm.."

                show ghost close at npc_right
                ghost "rejected."

                show cory upset at cory_left
                cory "what more do ya want from me mane?!"

                show ghost deadpan at npc_right
                ghost "look behind you"

                show cory side_close at cory_left
                cory "NUH UH I'M NOT FALLING FOR THAT!"

                show ghost deadpan at npc_right
                ghost "..."

                show ghost mweheh at npc_right
                ghost "boo…"

                show cory surprise at cory_left
                cory "GYAAAAH!!"

                "Mr Cory bolts away with a high pitch loud scream."

                show mc shock at mc_left
                mc "ah! Mr Cory waaaaait!!"

                show ghost mweheh at npc_right
                ghost "heh heh…"
                ghost "is that all you want to know..?"
                ghost "You're not as chatty with other fishes…"

                cory "YOU BEEN LISTENIN??"
                cory "AND WHY DO YA SOUND JEALOUS?!"

    show ghost default at npc_right
    ghost "I wish you the best of luck in your pursue, little brave one.."

    show mc o at mc_left
    mc "Will we meet again?"

    show ghost side at npc_right
    ghost "Perhaps, if fate allows…"

    show ghost close at npc_right
    ghost "May the sea be with you…"

    show mc happy at mc_left
    mc "Thank you Ms fish ghost!! I won't let you down!"

    return

label chapter2_mantis:

    hide mc
    scene ch2_night
    with fade

    "The night settles in heavy, and so does the overbearing crowd dying to just quiet murmurs of protests."

    "Two pairs of eyes peek from behind a flock of corals. Analyzing the situation at hand carefully."

    show cory talk at cory_left
    cory "This is our best chance, guppy.."

    show mc default at mc_left
    mc "mm! We strike now!"

    "With a deep inhale I jumped out the coral while Mr.Cory trails behind slowly."

    "We walked over to where the shrimp still stood its ground as straight as he was in the morning."

    show mc happy at mc_left
    mc "Good evening.. Mr shrimp!"

    show shrimp surprise at npc_right
    shrimp "Huh?! A little kid?!"

    show shrimp default at npc_right
    shrimp "Go back to your parents!"
    shrimp "Using a young guppy won't make me go soft on you!"

    show shrimp default at npc_right
    shrimp "I will still punch you if you lose!"

    show cory talk at cory_left
    cory "oooh.. That's not very nice… you can't be saying young fish…"

    show shrimp surprise at npc_right
    shrimp "and who are you!!"

    show cory smile at cory_left
    cory "I'm the young guppy's guardian…"

    show shrimp sepet at npc_right
    shrimp "I'm still not letting an elderly and a young guppy pass!"
    shrimp "Especially the elder…. Squints"

    show shrimp default at npc_right
    shrimp "You have to prove yourself worthy through a duel!"
    shrimp "Only then I shall let you pass!"

    call chapter2_mantis_mc_route

    return

label chapter2_mantis_mc_route:

    menu:
        "Ask why he’s guarding the gate":

            show mc o at mc_left
            show shrimp default at npc_right
            mc "mm.. say mr shrimp.. why do you guard the gate so strictly…?"

            shrimp "Because I was told to!"

            show mc o at mc_left
            mc "told to..? By who?"

            show shrimp proud at npc_right
            shrimp "The great empress I owe my life to!"
            shrimp "She saved me in my lowest moment in life.."

            show shrimp laugh at npc_right
            shrimp "And in exchange I devote my life to her compelling regime!"

            show mc dizzy at mc_left
            mc "regime..? What's a regime :o"

            show shrimp default at npc_right
            shrimp "a regime is some sort of propaganda! Maybe!"

            show shrimp shy at npc_right
            shrimp "I'm not too good with politics either so I wouldn't know!"

            show mc pout at mc_left
            mc "blehh you're right politics suck.. All the grown ups are so invested in it"
            mc "Is it so hard for everyone to just be friends, hold hands and help each other? :("

            show shrimp sepet at npc_right
            shrimp "hmm! Maybe you're right!"

            show shrimp default at npc_right
            shrimp "but it's hard to hold hands when you've got big claws this strong!"
            shrimp "It'd always hurt someone that's a different species!"
            show shrimp shy at npc_right
            shrimp "No matter how hard you try to be gentle."

            show mc o at mc_left
            mc "..."

            menu:
                "Ask to touch his arm":

                    show mc o at mc_left
                    mc "mr shrimp.."

                    show mc excited at mc_left
                    mc "what if i were to hypothetically ask to…"
                    mc "touch your claws..?"

                    show shrimp surprise at npc_right
                    shrimp "No!"

                    show mc pout at mc_left
                    mc "huh? Why not..?"

                    show shrimp default at npc_right
                    shrimp "Because it will hurt your tiny hands!"

                    show mc pout at mc_left
                    mc "but you said you won't hesitate to punch me in a duel.."
                    mc "why are you worried now Mr.shrimp?"

                    show shrimp default at npc_right
                    shrimp "... that’s different! This is a no duel context!"
                    shrimp "I would minimize as much damage as possible!"

                    show mc happy at mc_left
                    mc "But it's okay Mr.shrimp, I don't mind pain!"

                    show shrimp surprise at npc_right
                    shrimp "huh…?"

                    show mc default at mc_left
                    mc "Some pain is worth it for the sake of knowledge."
                    mc "And also for the sake of easing other people's pain.."

                    shrimp "You're saying you'd hurt yourself just to feel my claws?!"

                    show mc excited at mc_left
                    mc "I've never met a mantis shrimp before!"
                    mc "So it made me suuuper curious on how your claws work!"

                    show shrimp sepet at npc_right
                    shrimp "... hmph. Fine then touch you shall!"

                    show shrimp default at npc_right
                    shrimp "But don't come crying if you scrape yourself!"

                    show mc pout at mc_left
                    mc "im a good guppy! Good guppies don't cry!"

                    "Quenching curiosity, I started with poking its left claw with a finger repeatedly, assessing."

                    show mc excited at mc_left
                    mc "ooo..! So THIS is what a 150-kilo punch feels like..!"

                    show shrimp proud at npc_right
                    shrimp "How's it?! Fastest moving claws in all of animal kingdom!"

                    show shrimp laugh at npc_right
                    shrimp "Grace upon the excellent anatomy of a mantis shrimp! kakaka!"

                    "Mr. shrimp puffs up like a peacock the more I shower it with giddy attention."

                    "Soon enough he would break into all kinds of different poses to showboat his cool anatomy more."

                    "His flexed sturdy shells sparkle under the dim scale's light."

                    "I can only squeak in delight as this happens."

                "Ask for a duel":

                    pass

        "oh no, I'm not here for a duel!":

            show mc happy at mc_left
            mc "I'm here to offer you snacks.. You seem veeery tired.."

            show shrimp surprise at npc_right
            shrimp "Huh…!"
            shrimp "Wait me? TIRED? Tiredness can't affect a warrior!"

            show shrimp proud at npc_right
            shrimp "But I won't say no to delicious looking delicacies"

            "Without second guessing, Mr.shrimp took about three clams, breaking the shell with his punch before stuffing it into his mouth enthusiastically."

            "I watched the interesting process with rapt attention.. I've never seen a mantis shrimp eat before…"

            show shrimp default at npc_right
            shrimp "mm? What is it! Why are you staring!"

            show shrimp default at npc_right
            shrimp "Staring won't make me share a thing with you!"

            show mc default at mc_left
            mc "ah nonono am not hungry… *stomach growls*"

            show shrimp surprise at npc_right
            shrimp "...."

            show shrimp sepet at npc_right
            shrimp "Let's hypothetically say, I shared one clam!"

            show shrimp shy at npc_right
            shrimp "Would you eat it?!"

            show mc o at mc_left
            mc "...!"

            show mc happy at mc_left
            mc "hehe don't worry you can have all of it, mr shrimp"
            mc "you look like you need it more"

            show shrimp surprise at npc_right
            shrimp "I never said that I WOULD share it with you!"
            show shrimp default at npc_right
            shrimp "That was a merely hypothetical!"

            show shrimp shy at npc_right
            shrimp "Don't get too into yourself now!"

            if has_item("coal_tar"):
                "Mr. Shrimp ate enough coal tar for it to take effect."
            else:
                "There is no coal tar to give the shrimp."

    jump chapter2_mantis_cory_route

label chapter2_mantis_cory_route:

    show shrimp default at npc_right
    shrimp "You've bothered me enough!"
    shrimp "It is time for us to duel if you're so insistent on passing through!"

    show cory side at cory_left
    cory "Guess we got no other choice huh.."

    show cory talk at cory_left
    cory "prepare yerself to fight guppy…"

    show shrimp default at npc_right
    shrimp "We shall now start a sacred duel of… ROCK PAPER SCISSORS!"

    show cory surprise at cory_left
    cory "whuh?"

    show mc shock at mc_left
    mc "eh?"

    show cory upset at cory_left
    cory "mane all that trouble just for some guppy games?!"
    cory "Why don't everyfish just play and pass then?!"

    show shrimp default at npc_right
    shrimp "The moment i mention a duel they all cower in fear and retreat!"
    shrimp "You're the second bravest soul to duel with me today!"

    show mc o at mc_left
    mc "Did the first fish pass?"

    show shrimp default at npc_right
    shrimp "No! They died under the weight of my mighty punch!"

    show cory unimpressed at cory_left
    cory "glup…"

    show mc excited at mc_left
    mc "oh…!"

    show shrimp default at npc_right
    shrimp "The rules are easy!"
    shrimp "Each of you, have three rounds to go against me!"
    shrimp "And each round, whoever wins gets to attack the loser!"
    shrimp "Winning condition! Best two out of three wins!"

    show shrimp sepet at npc_right
    shrimp "Or if one of us is dead!"

    show shrimp proud at npc_right
    shrimp "Since you came in a pair, and I'm a generous mantis shrimp!"
    shrimp "One of you wins, and you both get through the gate!"

    show mc o at mc_left
    mc "question! Are we allowed to dodge the attack?"

    show shrimp default at npc_right
    shrimp "yes, dodge you shall!"

    show shrimp proud at npc_right
    shrimp "hmph! But can you really dodge my fast punches?!"

    show mc happy at mc_left
    mc "hehe we'll see about that"

    show cory talk_hu at cory_left
    cory "you ready to start, guppy?"

    menu:
        "Sir yes sir mr. cory!":
            pass

    call mantis_duel

    if duel_result == "win":

        show mc yay:
            full 
            right
            surprise
        mc "We did it!! We won mr.Cory!!"

        show cory proud_hu:
            full
            center
            moveinleft
        cory "EEEL YEAHH THAT'S WHAT I'M TALKING ABOUT GUPPY!!"

        show shrimp default:
            full
            centerleft
            moveinleft
        show cory proud_hu:
            full
            rightish
        with move
        shrimp "Hmph! Very well!"
        show shrimp default_om:
            full
            centerleft
            moveinleft
        shrimp "You have proven yourself worthy of the sea's grace!"

        show shrimp default:
            full
            left
        with move
        show mc o:
            full 
            right
        "Mr shrimp moves aside to reveal the cave's entrance and its long tunnel."
        "But we couldn't just go yet.."
        show mc serious:
            full 
            right
            surprise
        mc "mr shrimp.. Why don't you come along with us?"

        show shrimp surprise:
            full
            centerleft
            surprise
        with move
        shrimp "{size=50}WHAT?!{/size}"

        show cory surprise:
            full
            rightish
            surprise
        cory "{size=45}HUH?!{/size}"
        cory "Guppy did you not see how deadly those punches are?!"

        show mc serious_hu:
            full 
            right
        mc "I know! But it was part of the duel.."
        mc "He didn't even once hurt us before it started…"

        show cory side_close:
            full
            rightish
        cory "... can't argue with that."

        show shrimp surprise:
            full
            centerleft
            surprise
        shrimp "... But why the sudden preposterous preposition?!"
        shrimp "I'm the guardian of the sacred sea-salt gate!"
        show shrimp default_om:
            full
            centerleft
        shrimp "I mustn't leave my post! I mustn't let the unworthy pass!"

        mc "but you can't keep doing this mr shrimp.."
        mc "there are fishes that reeaaally need to pass the gate.."

        show cory talk:
            full
            rightish
        cory "They're right.."
        cory "There's a pregnant fish.. And some fish gone mad because of this carp"
        show cory talk_hu:
            full
            rightish
        cory "Before this, You were actively helpin out fishes in need"
        cory "Those who couldn't pay the prices of this gate, you'd help them pass.."
        show cory netral:
            full
            rightish
        cory "You've changed, what's up with that? Really."

        show shrimp shy:
            full
            centerleft
            sink
        shrimp "...."
        shrimp "I was..!"

        show shrimp sepet:
            unpose
            full
            centerleft
        shrimp "What I did was a moment of weakness! One that I wouldn't repeat!"
        show shrimp shy:
            full
            centerleft
        shrimp "And the cost of it was.. something irreversible…"
        shrimp "The one moment I let my guard down.."

        show shrimp surprise:
            full
            centerleft
            surprise
        shrimp "a sudden golden burst of incredible power dashed past me!"

        show mc o at mc_left
        mc "the golden fish…!"

        show shrimp default_om:
            unpose
            full
            centerleft
        shrimp "It's thousand suns way stronger than what my claws, my whole body can endure!"
        show shrimp shy:
            full
            centerleft
        shrimp "I have never felt more powerless in my life than that moment!"
        shrimp "and it was I that let such a dangerous powerful entity into the sea…"
        show shrimp default:
            full
            centerleft
        shrimp "One that doesn't bend down to rules… not even negotiation"
        show shrimp default_om:
            full
            centerleft
            surprise
        shrimp "Since that moment, the empress has tightened security at every gate that leads to the sea."

        show shrimp shy:
            full
            centerleft
        shrimp "And even when the empress had known of my crimes of letting fishes that didn't qualify pass through…"

        show shrimp smile:
            full
            centerleft
        shrimp "She still forgave me!"

        show shrimp default_om:
            full
            centerleft
        shrimp "I swore to her that I won't repeat the same mistake!"

        mc "But mr shrimp.. It wasn't your fault that the golden fish pass through!"
        mc "it wasn't something you can stop.. Nor something you can expect"
        mc "and me and mr cory are heading to sea in search of the golden fish!"
        mc "We can search for it together! To prevent it from doing more harm"

        show shrimp surprise:
            full
            centerleft
            surprise
        shrimp "YOU ARE?!"

        show shrimp shy:
            full
            centerleft
            sink
        shrimp "But.. who will guard the gates.. If not me?"

        cory "Naaah i don't think it needs guarding."
        cory "That shrimp empress's regime.. Is total bullshrimp"

        mc "the sea is big enough for everyone! And the sea can defend itself.."

        cory "There are fishes who just want to survive and meet their family.."
        cory "They don't mean no harm to the sea i guarantee.."

        show shrimp sepet:
            unpose
            full
            centerleft
        shrimp ".... Fine! I'll go! But only if we talk it out first with the shrimp empress!"

        show shrimp default:
            full
            centerleft
        shrimp "I can't just abandon my post without notice"
        show shrimp default_om:
            full
            centerleft
            surprise
        shrimp "That would be betrayal of the highest order!"

        jump chapter2_ending

>>>>>>> restore-friend-work
label chapter2_ending:
    $ focus()
    show mc excited:
        full
        trio_right
        jumpmc
    mc "onward! to the sea we go!"

    show shrimp laugh:
<<<<<<< HEAD
        trio_center_mantis
        toleft
        surprise
    shrimp "to the sea!"

    show cory side:
        full
        trio_left
    cory "..."

    show cory side_close:
        full
        trio_left
        sink
    cory "......"

    show cory fond:
        full
        trio_left
    cory "imp.. I leave the guppy's safety to ya alright?"

    show cory smile_hu:
        full
        trio_left
    cory "Shrimps have better resistance in freshwater don't they?"

    if has_item("saltwater_survival_device"):
        cory "And we only have one 50%% effective saltwater device.."
=======
            full
            centerleft
            toleft
            walkloop
    shrimp "KAKAKA! to the sea!"

    show cory netral:
            full
            rightish
    cory "..."

    show cory side:
            full
            rightish
    cory "......"

    show cory fond:
            full
            rightish
    cory "shrimp.. I leave the guppy's safety to ya alright?"
    cory "Shrimps have better resistance in freshwater don't they?"

    if has_item("saltwater_survival_device"):
        show cory side:
            full
            rightish
        cory "And we only have one 50% effective saltwater device.."
>>>>>>> restore-friend-work

    show mc shock:
        full
        trio_right
        surprise
    mc "...!!"

<<<<<<< HEAD
    show shrimp default_om:
        trio_center_mantis
        toleft
=======
    show shrimp default:
            full
            centerleft
>>>>>>> restore-friend-work
    shrimp "yes of course! Protect i shall. it is my utmost duty to protect!"

    show mc pout:
        full
        trio_right
    mc "no!"

    show cory side_close:
<<<<<<< HEAD
        full
        trio_left
=======
            full
            rightish
>>>>>>> restore-friend-work
    cory "guppy.."

    show mc pout:
        full
        trio_right
        jumpmc
    mc "no no no! I’m not going anywhere without Mr. Cory!!"

    show cory talk:
<<<<<<< HEAD
        full
        trio_left
    cory "guppy, I’d dry the sea to come along but-"
=======
            full
            rightish
    cory "guppy, I'd dry the sea to come along but-"
>>>>>>> restore-friend-work

    show mc pout:
        full
        trio_right
        surprise
    mc "mr shrimp cant you protect him? With your punches!"
    mc "punch all the freshwater away from mr.cory!"

    show shrimp sepet:
<<<<<<< HEAD
        trio_center_mantis
        toleft
=======
            full
            centerleft
>>>>>>> restore-friend-work
    shrimp "..."

    show shrimp default_om:
        trio_center_mantis
        toleft
    shrimp "I'm afraid I cannot, my dear comrade!"
    shrimp "punching water is akin to fighting a shadow…"

    show mc shock:
        full
        trio_right
        sink
    mc "no.."

    show mc holdcry:
        full
        trio_right
        sink
        vibrate(1)
    mc "but you promised… *sniffle*"
    mc "that we'd catch that fish together...."

    show cory side_close:
<<<<<<< HEAD
        full
        trio_left
        sink
=======
            full
            rightish
>>>>>>> restore-friend-work
    cory "....."
    cory "I’m.. God terribly. sorry guppy.."
    cory "I didn't think far enough that it'd reach the sea.."

    show cory side:
<<<<<<< HEAD
        full
        trio_left
    cory "...I’m afraid that I’m a fraud..."
=======
            full
            rightish
            sink
    cory "...I'm afraid that I'm a fraud..."
>>>>>>> restore-friend-work

    show shrimp smile:
        trio_center_mantis
        toleft
    shrimp "that makes a good rhyme!"

<<<<<<< HEAD
    "The fish scale in my bag suddenly glows into a blinding sparkly light for one second. Painting the three of us in gold, before it dims once more. But something felt different"

    show mc o:
        full
        right
        surprise
    with Dissolve(0.5)
    mc "mm?"

    show cory surprise:
        full
        leftish
        surprise
=======
    "The fish scale in my bag suddenly glows into a blinding sparkly light for one second."
    "Painting the three of us in gold, before it dims once more."
    "But something felt different."

    show mc o at mc_left
    mc "mm?"

    show cory surprise:
            unpose
            full
            rightish
            surprise
>>>>>>> restore-friend-work
    cory "I-! Huh? I feel different!"

    show mc o:
        full
        right
    mc "Try stepping in the saltwater, Mr.Cory!"

    show cory side:
<<<<<<< HEAD
        full
        leftish
=======
            unpose
            full
            rightish
>>>>>>> restore-friend-work
    cory "Are ya sure..? What if it's just my imagination?"

    show mc happy:
        full
        right
        surprise
    mc "trust me!"

    show cory side_close:
<<<<<<< HEAD
        full
        leftish
    cory "Alright…"
=======
            unpose
            full
            rightish
    cory "Alright… here goes nothin.."
>>>>>>> restore-friend-work

    "Mr Cory hesitantly takes one step into where freshwater and saltwater collide with one eye closed."

    show cory surprise:
<<<<<<< HEAD
        full
        centerleft
        walkto(centerleft, walktime=1.5)
    with move

=======
            full
            rightish
            surprise
>>>>>>> restore-friend-work
    cory "Holy mother of sea…!"

    show mc shock:
        full
        right
        surprise
    mc "d-does it hurt-"

    "Before I can finish my line I was swept into a spinning hug"

<<<<<<< HEAD
    show cory proud:
        full
        centerleft
        jumpmc
=======
    show cory proud_hu:
            full
            rightish
            surprise
            vibrate
>>>>>>> restore-friend-work
    cory "I CAN'T BELIEVE IT!! I'M IN SALTWATER GUPPY!!"

    show mc excited:
        full
        right
        jumpmc
    mc "YAAAAAY"

    "Mr shrimp then lifts the both of us with its strong claws spinning us all into a dizzying spiral"

    show shrimp laugh:
        full
        center
        jumpmc
    show mc excited:
        full
        right
        surprise
        vibrate(3)
    show cory upset:
        full
        leftish
        surprise
        vibrate(3)
    shrimp "KAKAKA! WAHOO!"

<<<<<<< HEAD
    cory "THAT’S WAY TOO FAAAUUUAASHHTT SHRIMP PUT US DOOOOWN"
=======
    show cory upset:
            full
            rightish
            vibrate
    cory "{sc}THAT'S WAY TOO FAAAUUUAASHHTT SHRIMP PUT US DOOOOWN {/sc}"
>>>>>>> restore-friend-work

    mc "YIPEEEEE FAAASTEEER!!"

    show shrimp surprise:
        full
        center
    shrimp "Ah! My apologies, comrades! And congratulations to Mr. Cory!"

    "Mr shrimp then carefully puts us down"

    show shrimp laugh:
        trio_right_mantis
        toleft
    with move
    shrimp "With this, we can now safely travel amongst the seas! KAKAKA!"

<<<<<<< HEAD
    show cory unimpressed:
        full
        trio_left
        sink
=======
    show cory unimpressed2:
            full
            rightish
            vibrate
>>>>>>> restore-friend-work
    cory "ngnuuurhhhehhkk"

    show mc dizzy:
        full
        trio_center
        sink
        vibrate(2)
    mc "oaooaooouhh yaaaah lets meef the… crustashan empeees.."

    show shrimp smile:
        trio_right_mantis
        toleft
    shrimp "Don’t worry, my dizzy lieges! I’ll carry the both of you until you regain your ground! Or.. your water!"

    $ focus()
    hide mc
    hide cory
    hide shrimp
    scene black with dissolve

    "END OF CHAPTER 2"

    jump chapter3_start
