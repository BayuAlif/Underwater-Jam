# =========================================================
# CHAPTER 2 - NPC: AROWANA / MR. WANA
# =========================================================

label arowana:
    jump wana

label wana:

    $ cory_at_right = False

    show wana default at wana_pos
    show mc default at mc_pos

    "A silver arowana kicks big rocks with a loud grumble."

    "I wonder what it's mad about.."

    mc "Good morning si-"

    show wana mad at wana_pos

    wana "SHHHRGGHHHJHNGHHRRAHH!!"
    wana "MY BOSS IS GOING TO KILL ME I'M GOING TO GET PUBLICLY EXECUTED"

    "Mr Cory takes a step forward, shielding me behind his taller frame."

    $ cory_at_right = True
    hide mc
    show cory side at cory_right_pos

    cory "Woah, chill the eel out, my guy!"
    cory "Those rocks can hurt a ton."

    show wana default at wana_pos

    wana "Oh."
    wana "A fish."
    wana "My apologies, sir."
    wana "I failed to notice you."

    cory "Huh.. what a turn.."
    cory "Wait!"
    cory "You a silver arowana right?"
    cory "From Amazon?"

    show wana smile at wana_pos

    wana "...!"
    wana "Eel yeah I am!"
    wana "From which side are you on, brother?"

    cory "Nay, I ain't exactly from there."
    cory "It's Maranhão for me."

    wana "Ouuu shii that's where vovó at!"
    wana "I mean!"
    wana "How fortunate."
    wana "My grandma also lives in that state."

    show cory smile at cory_right_pos

    cory "Pfft.. language barriers ay?"

    call screen who_should_ask(title="Choose who should ask Mr. Wana!", subtitle="The answers he gives may vary based on his relationship with the character")

    if _return == "mc":
        jump wana_as_mc
    else:
        jump wana_as_cory


# =========================================================
# MR. WANA - AS MC
# =========================================================

label wana_as_mc:

    $ cory_at_right = False
    hide cory
    show wana default at wana_pos
    show mc default at mc_pos

    mc "What's wrong, Mr. Arowana?"

    wana "Everything."
    wana "And it's Mr. Wana."

    wana "I have a crucial meeting in less than an hour…"
    wana "My boss EXPECTS me to be there."
    wana "My colleagues EXPECTS me to be there."
    wana "My entire career EXPECTS me to be there."
    wana "The office's slug expects me to be there…"

    show mc o at mc_pos

    mc "But you're still here…"

    show wana mad at wana_pos

    wana "NO SHRIMP!"
    wana "I AM HERE."
    wana "Because of that stupid- egregious mantis shrimp!"

    show wana default at wana_pos

    wana "My apologies."
    wana "That was unprofessional of me."

    show mc happy at mc_pos

    mc "It's okay :D"

    $ cory_at_right = True
    hide mc
    show cory side at cory_right_pos

    cory "So he's been blocking all day now?"

    wana "Precisely."
    wana "That's what the crowd's about."

    $ cory_at_right = False
    hide cory
    show mc default at mc_pos

    menu:

        "Do you know why the shrimp's blocking?":

            wana "Unfortunately I do not."

            show mc o at mc_pos

            mc "Not a thing?"

            show wana squint at wana_pos

            wana "I'm sorry but I don't think I want to entertain a child right now.."


        "Tell him to just swim there.":

            mc "Mr Wana, if work is so important..."
            mc "Why don't you just leap up through the cave?"

            show wana squint at wana_pos

            wana "..."

            show mc excited at mc_pos

            mc "Just like how a flying fish would!"

            wana "..."

            show wana smile at wana_pos

            wana "HAH!"
            wana "Yes!"
            wana "How wonderful!"
            wana "I should've just tried that!."

            show mc happy at mc_pos

            mc "Right?!"
            mc "So you can just go!"

            show wana squint at wana_pos

            wana "..."
            wana "...Young fish."

            show mc o at mc_pos

            mc "Yes?"
            mc "Do you need a push?"
            mc "Me and Mr Cory can help!"

            show wana default at wana_pos

            wana "I have a meeting."
            wana "I have a boss."
            wana "I have a career."
            wana "And now I have a headache."

            show mc shock at mc_pos

            mc "Huh?"
            mc "But why…"

            show wana squint at wana_pos

            wana "Please don't give me career advice again."

            "Mr. Cory quietly steps in beside me, bending down to murmur something."

            $ cory_at_right = True
            hide mc
            show cory side at cory_right_pos

            cory "Guppy."
            cory "Maybe let's leave the poor guy alone."

            $ cory_at_right = False
            hide cory
            show mc pout at mc_pos

            mc "But I wanna help!!"

            "Mr Cory sighs and proceeds to escort me away."

            show wana default at wana_pos

            wana "I admire your patience in tending to the young one, Corydoras."

            $ cory_at_right = True
            hide mc
            show cory talk at cory_right_pos

            cory "Heh."
            cory "I'm starting to get the hang of it."

            $ cory_at_right = False
            hide cory
            show mc pout at mc_pos

            mc "hnnrhhgh!!"

    $ cory_at_right = False
    hide mc
    hide cory
    hide wana

    return


# =========================================================
# MR. WANA - AS CORY
# =========================================================

label wana_as_cory:

    $ cory_at_right = True
    hide mc
    show wana default at wana_pos
    show cory talk at cory_right_pos

    cory "Ay mano, care to tell us what's up?"
    cory "We needa cross the border too."

    show wana smile at wana_pos

    wana "Ay cara, of course I'll tell you everything."
    wana "I need him sober ASAP."
    wana "Can't risk getting fired now."

    menu:

        "Got an idea why shrimp's gatekeepin?":

            show wana default at wana_pos

            wana "Not a clue, unfortunately."
            wana "All I know is, you have to win in some kind of duel against him."
            wana "And another thing that I know is that I'm not a fighter."

            show cory talk at cory_right_pos

            cory "Heh, you look tough though."
            cory "Why not give it a try?"

            show wana squint at wana_pos

            wana "Can't risk having my ass beat."
            wana "When it's going to be absolutely clapped by the end of the day."
            wana "As in, from the amount of work my boss gave me."

            show cory smile at cory_right_pos

            cory "Pfft."
            cory "Ya boss sure love yer hardworking ass huh."

            show wana squint at wana_pos

            wana "I'm going to pretend I didn't hear that."


        "You know what's up with his bizarre act?":

            show wana default at wana_pos

            wana "No."
            wana "He's usually not this strict."
            wana "I pass him on the daily."
            wana "He knew of my face by now, I'm sure."

            wana "Though he's been muttering weird stuff…"
            wana "'I mustn't repeat what I did.'"
            wana "That's what I caught most clearly.."

            show cory side at cory_right_pos

            cory "Huh."
            cory "Something must've happened to him then."

            show wana mad at wana_pos

            wana "How unprofessional of him!"
            wana "He shouldn't be letting personal matters fiddle his work!"

            show wana default at wana_pos

            wana "Ugh."
            wana "This path is the only way I commute to work in the sea.."
            wana "What should I do now?"

            show cory talk at cory_right_pos

            cory "Wait!"
            cory "You work at the sea?"
            cory "How are ya doing that?!"

            show wana squint at wana_pos

            wana "Doing what exactly?"

            show cory talk at cory_right_pos

            cory "Ya know!"
            cory "We're the freshwater kind."
            cory "How do ya brave the sea?"

            "The silver arowana opens his briefcase."

            "The inside is filled with an absurd amount of expensive-looking equipment."

            show cory surprise at cory_right_pos

            cory "*whistle*"
            cory "Sweet stuffs ya got!"

            show wana smile at wana_pos

            wana "This device allows me to survive in saltwater."
            wana "It cost me more money than I'm comfortable admitting."

            show cory talk at cory_right_pos

            cory "How much are we talking?"

            show wana squint at wana_pos

            wana "I would rather not expose the numbers."
            wana "But let's say it cost me my nine lives."

            $ cory_at_right = False
            hide cory
            show mc o at mc_pos

            mc "But you're not a cat!"
            mc "You're a fish!"

            show wana default at wana_pos

            wana "Precisely."
            wana "This device was handed down eight generations before me."

            show mc shock at mc_pos

            mc "Aww.."
            mc "If only we could buy it from you…"

            $ cory_at_right = True
            hide mc
            show cory talk at cory_right_pos

            cory "Buy?!"
            cory "With whose clams are we talking buy?!"

            $ cory_at_right = False
            hide cory
            show mc happy at mc_pos

            mc "Hehe."

            $ cory_at_right = True
            hide mc
            show cory side at cory_right_pos

            cory "Ay guppy, clam's tight on me too.."

            show wana smile at wana_pos

            wana "Tell you what."
            wana "If you're really planning to confront that shrimp…"
            wana "You might as well take it."
            wana "Here, have a spare."

            show cory surprise at cory_right_pos

            cory "For reals yo?!"

            show wana default at wana_pos

            wana "Of course."
            wana "But it's broken."
            wana "Only 50%% effective..."
            wana "Take it or leave."

            show cory smile at cory_right_pos

            cory "I'll gladly take it!"
            cory "Appreciate it, mano!"

            show wana smile at wana_pos

            wana "You put some sense into the guy for me in exchange, alright?"

    $ cory_at_right = False
    hide mc
    hide cory
    hide wana

    return
