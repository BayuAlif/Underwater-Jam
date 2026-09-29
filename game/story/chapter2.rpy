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
        right
        walkto(right)
        toleft
        walkloop
    with moveinright
    show cory netral:
        full
        unpose
    show cory netral:
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

    show cory smile:
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

    show cory talk:
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
            surprise
            pause 1
            repeat
    mc "Oh oh! That's a mantis shrimp!! He looks really tough!"
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

    show mc serious_hu:
        full
        right
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
    with moveinright
    mc "A tiny krill!"

    show krill:
        full
        centerleft
        medium
    with moveinbottom
    tinykrill "Eah!"

    show cory disrespect:
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
        full
        center
    cory "...."
    cory "... I say we feed that thing to a fish, guppy"

    show mc sad_hu:
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

    "{b}I obtained a tiny krill.{/b}"
    $ focus()
    return

label chapter2_salmon:

    hide mc
    scene ch2_day
    with dissolve

    show salmon pien at npc_right
    sal "Hic hic…"
    sal "Sniff….."
    sal "....oouuugh…."

    show mc shock at mc_left
    mc "... Ma'am? Why are you crying :("

    show salmon default at npc_right
    sal "....? huh??"

    show salmon pien at npc_right
    sal "........."
    sal "I want to go get down to the sea…"
    sal "but i bloody well can't..."

    show salmon pout at npc_right
    sal "It's all… because… of that God awful….."

    show salmon pien at npc_right
    sal "UEEEEHHH………."

    show mc shock_hu at mc_left
    mc "!! waouh-? Don't cry, Mrs Salmon!"
    mc "(hugs the salmon)"

    show salmon pien at npc_right
    sal "......!!!"

    show mc happy at mc_left
    mc "There, there."
    mc "If the mama is sad, the baby gets sad, too."

    show salmon default at npc_right
    sal "...... how on ocean does a tiny you know that, love?"

    show mc actually at mc_left
    mc "I watched salmon migration on YouTube!!"
    mc "Mama salmon swims really far to lay their eggs, right?"

    show salmon happy at npc_right
    sal "Oh my…. Hahaha."
    sal "You're a very lovely little thing, aren't you?"

    show salmon default at npc_right
    sal "Though i haven't a clue what this “YouTube” is…."
    sal "Must be a helpful source of information.."

    show salmon happy at npc_right
    sal "Tell me love, are there any sort of.. Pregnancy tips in there?"
    sal "Or what a salmon parent must prepare to leave their young…"

    show mc happy at mc_left
    mc "I think so! YouTube's got everything you'd want to see!"
    sal "Oh that sounds about perfect!"

    show salmon default at npc_right
    "Mrs. Salmon looks at Cory."

    sal "Go back to your father now. He must be worried for you"

    show mc shock at mc_left
    mc "Ah, he's not my father!"

    show mc happy at mc_left
    mc "I only met him yesterday!"

    show salmon pout at npc_right
    sal "..........??"

    "Salmon glares at Cory suspiciously."

    show cory side at cory_left
    cory "Ay.. no need to look at me like that ma'am.."
    cory "I'm a trusted adult!"

    "Salmon squints her eyes at him in suspicion, not believing a thing."

    sal "...."

    show cory side_close at cory_left
    cory "glup…."

    call chapter2_salmon_questions

    show salmon pien at npc_right
    sal "I think i will have to take a detour-"
    sal "-even it'll take me aeons."

    show cory talk_hu at cory_left
    cory "A detour…. whaddya think, guppy?"

    show mc pout at mc_left
    mc "NOOO i dont wanna take a detour…!!"
    mc "The golden fish will be gone farther by then :("

    show salmon default at npc_right
    sal "Haven't a clue about any other way, unfortunately."

    show salmon happy at npc_right
    sal "I can only wish you the best of luck."
    sal "I bid you farewell guppy"

    $ add_clue("The only way to go to the sea is blocked by a mantis shrimp.")

    return

label chapter2_salmon_questions:

    hide mc
    hide cory
    call screen character_question_select("Mrs. Salmon")
    $ selected_questioner = _return

    if selected_questioner == "mc":

        show mc o at mc_left
        show salmon default at npc_right

        menu:
            "What's stopping you from going down there, ma'am?":

                sal "There's only one path down to the sea from here, innit,"
                show salmon pout at npc_right
                sal "But a bloody mantis shrimp's blocking the way,"
                sal "So I can't get past, love."
                mc "But… why does the mantis shrimp block the way???"
                show salmon default at npc_right
                sal "I haven't the foggiest idea, love."

            "Can't you just push past the river, ma'am?":

                show mc o at mc_left
                show salmon default at npc_right
                sal "Push past it??"
                sal "Oh, perish that thought, love.."
                sal "... that path is guarded… by a mantis shrimp."
                sal "Whacking great claws and all."
                show salmon pout at npc_right
                sal "I reckon he's a bloody MMA (Marine Martial Arts) fighter."
                sal "Tried to ask nicely, but he shooed me right off…"

                show mc shock_hu at mc_left
                mc "Oh no that's terrible.."
                mc "but why would mr mantis do that?"

                show salmon default at npc_right
                sal "I haven't a clue dear, he looks like he lost his mind"
                sal "Only way to walk pass him is to win in a duel"

            "I found a tiny krill!":

                show mc happy at mc_left
                show salmon happy at npc_right
                sal "Oh how lovely! For me, sweet guppy?"
                mc "Mhm! It can be your tiny companion to keep you safe or-"

                "Mrs. Salmon starts eating the krill with a delighted face."

                show mc shock at mc_left
                sal "Mm! Scrumptious krill"
                mc "Ah.. Salmon does eat krills huh.."

                $ remove_item("tiny_krill")

                "Mrs. Salmon pulls me into a sudden hug. I can faintly hear the tiny eggs shuffling under her scales."

                sal "Thank you, thank you.. I can't remember the last time I had a meal.."

                "Her voice trembles in sincere gratitude, so soft it's enough to lull me to sleep. It was akin to mama's voice when she sings. But it's not the same.."

                "It's not her…"

                show mc pout at mc_left
                mc "mn..*sniff*"
                mc "Mama..."

                show salmon default at npc_right
                sal "...!"

                show salmon happy at npc_right
                "I feel a faint tap on my glass head. Even when I couldn't directly feel it, I could picture how it would land on my head, a gentle caress that would wipe all my worries and sadness away."

                sal "mhm, I'm here for you.."
                sal "It's alright my sweet little guppy… you're okay.."

    else:

        show salmon pout at npc_right
        sal "What on ocean are you doing with that guppy?"

        show cory talk_hu at cory_left
        cory "Ay, easy, ma'am…"
        cory "I'm just protecting the little guppy, alright?"

        menu:
            "D'you mind us asking why you can't get down to the sea?":

                show cory talk_hu at cory_left
                show salmon pout at npc_right
                sal "......."
                sal "I won't be answering your queries young man!"
                sal "not until you tell the truth about the little one."

                show cory side at cory_left
                "Mr. Cory approached Mrs. Salmon with a sigh, lowering his voice to a whisper. Though I can still make out the words quite clear."

                cory "I haven't got a full picture of the guppy's story but..."
                cory "To me, it looks like their parents somewhat abandoned 'em."

                show salmon default at npc_right
                sal "......!"

                show salmon pout at npc_right
                sal "Then just turn around and go back."
                sal "You'd know how bloody dangerous the sea can be for a fry…"

                show cory talk at cory_left
                cory "I'm well aware ma'am.."
                cory "they almost fell a deep river hole where I first found em.."

                show cory side_close at cory_left
                cory "But withholding a guppy's dream from coming true?"
                cory "I'd be too evil for that"

            "Maam, why can't you go down to the sea?":

                show salmon pout at npc_right
                show cory side_close at cory_left

                "Mrs.Salmon ignores Cory completely."

                sal "... are you sure he's not up to anything dodgy, dear?"

                show mc default at mc_left
                mc "Mm-hmm! Mr Cory is super nice!"

                show mc happy at mc_left
                mc "He's been helping me lots!"

                show salmon default at npc_right
                sal "Hm, if you say so then…"

                show salmon pout at npc_right
                sal "But! you watch your back around him anyway, love."

                show cory upset at cory_left
                cory "I'm trustworthy, swear on my gills!"

            "May I offer you some food, ma'am?":

                show cory smile_hu at cory_left
                show salmon default at npc_right

                "Cory offers a krill to Mrs. Salmon."

                if has_item("tiny_krill"):
                    sal "...!"
                    show salmon pout at npc_right
                    sal "... Hmph"

                    show cory side_close at cory_left
                    cory "I'll just... leave it here for you ma'am."

                    show salmon default at npc_right
                    sal "Wait!"

                    show cory talk_hu at cory_left
                    cory "... hm? What is it ma'am?"

                    show salmon default at npc_right
                    sal "I should be thanking you bloke properly.."
                    sal "That was rude of me, My deepest apologies.."

                    show cory smile_hu at cory_left
                    cory "Nay ma'am it's chill I'm used to it.."
                    cory "Besides, a carrying mother needs to have their guard up yeah?"

                    sal "Fair enough.. I can't help it"
                    sal "You better take a dainty great care of the little fry, okay?"
                    sal "I'm bloody worried for them.."

                    cory "Don't worry ma'am i had a little sibling just their age"
                    cory "I know what I'm doing alright!"

                    $ remove_item("tiny_krill")
                    $ salmon_trust = True

                else:
                    cory "Oh…"
                    cory "Looks like we don't have anything to offer."

    return

label chapter2_arowana:

    show arowana mad at npc_right
    "A silver arowana kicks big rocks with a loud grumble. I wonder what it's mad about.."

    show mc happy at mc_left
    mc "Good morning si-"

    show arowana mad at npc_right
    aro "SHHHRGGHHHJHNGHHRRAHH!!"
    aro "MYBOSSISGOINTOKILLMEIMGOINGTOGETPUBLICLYEXECUTED"

    "Mr Cory takes a step forward, shielding me behind his taller frame."

    show cory talk_hu at cory_left
    cory "Woah chill the eel out my guy!"

    cory "Those rocks can hurt a ton"

    show arowana squint at npc_right
    aro "Oh. A fish."

    show arowana default at npc_right
    show arowana default at npc_right
    aro "My apologies, sir. I failed to notice you"

    show cory surprise_hu at cory_left
    cory "Huh.. what a turn.."
    cory "Wait! You a silver arowana right?"
    cory "From Amazon?"

    show arowana smile at npc_right
    aro "...!"
    aro "Eel yeah I am! From which side are you on brother?"

    show cory smile at cory_left
    cory "Nay, I ain't exactly from there, it's maranhao for me"

    aro "Ouuu shii that's where vovo at!"

    show arowana default at npc_right
    aro "I mean! How fortunate. My grandma.. also lives in that. State."

    show cory smile_hu at cory_left
    cory "Pfft.. language barriers ay?"

    call chapter2_arowana_questions

    return

label chapter2_arowana_questions:

    hide mc
    hide cory
    call screen character_question_select("Mr. Wana")
    $ selected_questioner = _return

    if selected_questioner == "mc":

        show mc o at mc_left

        menu:
            "Do you know why the shrimp's blocking?":

                show arowana default at npc_right
                aro "Unfortunately I do not."

                show mc o at mc_left
                mc "Not a thing?"

                show arowana squint at npc_right
                aro "I'm sorry but don't think I want to entertain a child right now.."

                show mc pout at mc_left
                mc "Awww…"

            "Tell him to just swim there.":

                show mc o at mc_left
                mc "Mr Wana, if work is so important"
                mc "Why don't you just leap up through the cave?"

                show arowana default at npc_right
                aro "..."

                show mc excited at mc_left
                mc "Just like how a flying fish would!"

                show arowana squint at npc_right
                aro "..."

                show arowana mad at npc_right
                aro "HAH! Yes! How wonderful I should've just tried that!."

                show mc happy at mc_left
                mc "Right?! So you can just go!"

                show arowana default at npc_right
                aro "..."

                show arowana squint at npc_right
                aro "... Young fish."

                show mc default at mc_left
                mc "Yes? Do you need a push? Me and Mr Cory can help!"

                show arowana default at npc_right
                aro "I have a meeting. I have a boss. I have a career."

                show arowana squint at npc_right
                aro "And now I have a headache."

                show mc shock at mc_left
                mc "Huh? But why…"

                aro "Please don't give me career advice again."

                show cory side at cory_left
                cory "Guppy."

                cory "Maybe let's leave the poor guy alone."

                show mc pout at mc_left
                mc "But I wanna help!!"

                show cory side_close at cory_left
                "Mr Cory sighed and proceeds to escort me away"

                show arowana smile at npc_right
                aro "I admire your patience in tending to the young one, Corydoras."

                show cory fond at cory_left
                cory "Heh, I'm starting to get the hang of it"

                show mc pout at mc_left
                mc "hnnrhhgh!!"

    else:

        show cory smile_hu at cory_left
        cory "Ay mano, care to tell us what's up?"
        cory "We needa cross the border too."

        show arowana smile at npc_right
        aro "Ay cara, of course I'll tell you everything"
        aro "I need him sober asap."

        show arowana squint at npc_right
        aro "Can't risk getting fired now"

        menu:
            "Got an idea why shrimp's gatekeepin?":

                show cory talk_hu at cory_left
                show arowana default at npc_right
                aro "Not a clue, unfortunately"
                aro "All i know is, you have to win in some kind of duel against him."

                show arowana squint at npc_right
                aro "And another thing that I know is that I'm not a fighter."

                show cory smile at cory_left
                cory "Heh, you look tough though, why not give it a try?"

                aro "Can't risk having my ass beat."
                aro "When it's going to be absolutely clapped by the end of the day"

                show arowana default at npc_right
                aro "As in, from the amount of work my boss gave me."

                show cory disrespect at cory_left
                cory "Pfft, ya boss sure love yer hardworking ass huh"

                show arowana squint at npc_right
                aro "I'm going to pretend I didn't hear that."

                $ add_clue("You have to win in a duel to pass the shrimp.")

            "You know what's up with his bizarre act?":

                show cory talk at cory_left
                show arowana default at npc_right
                aro "No, He's usually not this strict"
                aro "I pass him on the daily. He knew of my face by now i'm sure"
                aro "Though he's been muttering weird stuff…"
                aro "I mustn't repeat what i did is what i caught most clear.."

                show cory talk_hu at cory_left
                cory "Huh.. something must've happened to him then"

                show arowana mad at npc_right
                aro "How unprofessional of him! He shouldn't be letting personal matters fiddle his work!"

                show arowana squint at npc_right
                aro "Ugh, this path is the only way I commute to work in the sea.. What should i do now"

                show cory surprise at cory_left
                cory "Wait, you work at the sea? How are ya doing that?!"

                show arowana default at npc_right
                aro "Doing what exactly?"

                show cory talk_hu at cory_left
                cory "Ya know! We're the freshwater kind.. how do ya brave the sea?"

                "The silver arowana opens his briefcase."

                "The inside is filled with an absurd amount of expensive-looking equipments."

                show cory smile at cory_left
                cory "*whistle* sweet stuffs ya got!"

                show arowana default at npc_right
                aro "This device allows me to survive in saltwater."

                show arowana squint at npc_right
                aro "It cost me more money than I'm comfortable admitting."

                cory "How much are we talking?"

                aro "I would rather not expose the numbers."
                aro "But let's say it cost me my nine lives."

                show mc o at mc_left
                mc "But you're not a cat, you're a fish!"

                show arowana default at npc_right
                aro "Precisely. This device was handed down eight generations before me."

                show mc pout at mc_left
                mc "Aww.. If only we could buy it from you…"

                show cory upset at cory_left
                cory "Buy?! With whose clams are we talking buy?!"

                show mc happy at mc_left
                mc "Hehe"

                show cory unimpressed at cory_left
                cory "ay guppy clam's tight on me too.."

                show arowana default at npc_right
                aro "Tell you what."

                aro "If you're really planning to confront that shrimp…"

                show arowana smile at npc_right
                aro "You might as well take it."
                aro "Here, have a spare."

                show cory surprise at cory_left
                cory "For reals yo?!"

                aro "Of course. But it's broken. Only 50% effective..."
                aro "Take it or leave"

                show cory smile_hu at cory_left
                cory "I'll gladly take it! Appreciate it mano!"

                show arowana smile at npc_right
                aro "You put some sense into the guy for me in exchange alright?"

                $ add_item("saltwater_survival_device")
                $ add_clue("The Mantis Shrimp is blocking the only path to the ocean.")

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

            if chapter2_mantis_done:
                $ mark_npc_explored("mantis")

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
    mc "That.. wasn't me…"

    "The water around us suddenly grows eerily still."

    "Faint glow pair of eyes emerges from the darkness."

    show cory surprise at cory_left
    cory "GYAAAAAAA—"

    "Mr Cory jumped and immediate cower behind my back with a loud screech."

    show mc o at mc_left
    mc ":o"

    show mc excited at mc_left
    mc "Woah! What are you?"

    show ghost default at npc_right
    ghost "A fish."

    show mc pout at mc_left
    mc "I can see that."

    ghost "Then you needn't know more."

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

    "I obtained: a mysterious stinky black lump."

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
            centerleft
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

        show mc o:
            full
            right
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

label chapter2_ending:
    $ focus()
    show mc excited:
            full
            right
            unpose
    show mc excited:
            walkloop
    mc "onward! to the sea we go!"

    show shrimp laugh:
        full
        unpose
        offscreenleft
    show shrimp laugh:
        centerleft
        walkloop
    with moveinleft
    shrimp "KAKAKA! to the sea!"

    show cory netral:
            full
            unpose
            offscreenleft
    show cory netral:
            rightish
            walkloop
    cory "..."

    show cory side:
            full
            right
    with move
    cory "......"

    show cory fond:
            full
            right
    cory "shrimp.. I leave the guppy's safety to ya alright?"
    cory "Shrimps have better resistance in freshwater don't they?"

    if has_item("saltwater_survival_device"):
        show cory side:
            full
            right
        cory "And we only have one 50% effective saltwater device.."

    show mc shock:
            full
            right
    mc "...!!"

    show shrimp default:
            full
            centerleft
    show cory side:
            full
            rightish
    with move
    shrimp "yes of course! Protect i shall. it is my utmost duty to protect!"

    show mc pout:
            full
            right
    mc "no!"

    show cory side_close:
            full
            rightish
    cory "guppy.."

    show mc pout:
            full
            right
    mc "no no no! I'm not going anywhere without Mr. Cory!!"

    show cory talk:
            full
            rightish
    cory "guppy, I'd dry the sea to come along but-"

    show mc pout:
            full
            right
    mc "mr shrimp cant you protect him? With your punches!"
    mc "punch all the freshwater away from mr.cory!"

    show shrimp sepet:
            full
            centerleft
    shrimp "..."

    show shrimp default:
            full
            centerleft
    shrimp "I'm afraid I cannot, my dear comrade!"
    shrimp "punching water is akin to fighting a shadow…"

    show mc shock:
            full
            right
    mc "no.."

    show mc holdcry:
            full
            right
    mc "but you promised… *sniffle*"
    mc "that we'd catch that fish together...."

    show cory side_close:
            full
            rightish
    cory "....."
    cory "I'm.. God terribly. sorry guppy.."
    cory "I didn't think far enough that it'd reach the sea.."

    show cory side:
            full
            rightish
            sink
    cory "...I'm afraid that I'm a fraud..."

    show shrimp smile:
            full
            centerleft
    shrimp "that makes a good rhyme!"

    "The fish scale in my bag suddenly glows into a blinding sparkly light for one second."
    "Painting the three of us in gold, before it dims once more."
    "But something felt different."

    show mc o:
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
            full
            right
    mc "Try stepping in the saltwater, Mr.Cory!"

    show cory side:
            unpose
            full
            rightish
    cory "Are ya sure..? What if it's just my imagination?"

    show mc happy:
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
            full
            rightish
            surprise
    cory "Holy mother of sea…!"

    show mc shock:
            full
            right
    mc "d-does it hurt-"

    "Before I can finish my line I was swept into a spinning hug."

    show cory proud_hu:
            full
            rightish
            surprise
            vibrate
    cory "I CAN'T BELIEVE IT!! I'M IN SALTWATER GUPPY!!"

    show mc excited:
            full
            right
    mc "YAAAAAY"

    "Mr shrimp then lifts the both of us with its strong claws spinning us all into a dizzying spiral."

    show shrimp laugh:
            full
            centerleft
    shrimp "KAKAKA! WAHOO!"

    show cory upset:
            full
            rightish
            vibrate
    cory "{sc}THAT'S WAY TOO FAAAUUUAASHHTT SHRIMP PUT US DOOOOWN{/sc}"

    show mc excited:
            full
            right
    mc "YIPEEEEE FAAASTEEER!!"

    show shrimp surprise:
            full
            centerleft
    shrimp "Ah! My apologies, comrades! And congratulations to Mr. Cory!"

    "Mr shrimp then carefully puts us down."

    show shrimp laugh:
            full
            centerleft
    shrimp "With this, we can now safely travel amongst the seas! KAKAKA!"

    show cory unimpressed2:
            full
            rightish
            vibrate
    cory "ngnuuurhhhehhkk"

    show mc dizzy:
            full
            right
    mc "oaooaooouhh yaaaah lets meef the… crustashan empeees.."

    show shrimp smile:
            full
            centerleft
    shrimp "Don't worry, my dizzy lieges! I'll carry the both of you until you regain your ground! Or.. your water!"

    $ focus()
    hide mc
    scene black with dissolve

    menu:
        "Continue to Chapter 3":
            jump chapter3_start

        "End":
            return