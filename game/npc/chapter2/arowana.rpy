label arowana_interaction:
    hide mc
    scene ch2_day
    $ focus()

    "A silver arowana kicks big rocks with a loud grumble. I wonder what it's mad about.."

    show mc happy:
        full
        right
    mc "Good morning si-"

    show arowana mad:
        full
        center
        vibrate
    arowana "SHHHRGGHHHJHNGHHRRAHH!!"
    arowana "MYBOSSISGOINTOKILLMEIMGOINGTOGETPUBLICLYEXECUTED"

    "Mr Cory takes a step forward, shielding me behind his taller frame"

    show arowana mad:
        full
        rightish
        vibrate
    with move
    show cory talk_hu:
        full
        centerleft
    with moveinleft
    cory "Woah chill the eel out my guy!"
    cory "Those rocks can hurt a ton"

    show arowana squint:
        full
        rightish
    arowana "Oh. A fish."

    show arowana default:
        full
        rightish
    arowana "My apologies, sir. I failed to notice you"

    show cory surprise:
        full
        centerleft
        surprise
    cory "Huh.. what a turn.."
    cory "Wait! You a silver arowana right?"
    cory "From Amazon?"

    show arowana smile:
        full
        rightish
        surprise
    arowana "...!"
    arowana "Eel yeah I am! From which side are you on brother?"

    show cory smile:
        full
        centerleft
    cory "Nay, I ain’t exactly from there, it’s maranhao for me"

    arowana "Ouuu shii that’s where vovo at!"

    show arowana default:
        full
        rightish
    arowana "I mean! How fortunate. My grandma.. also lives in that. State."

    show cory smile_hu:
        full
        centerleft
        surprise
    cory "Pfft.. language barriers ay?"
    $ focus()

    hide mc
    hide cory
    call screen choose_interactor(
        "Choose who should ask Mr. Wana!",
        "The answers it gives may varied based on its relationship with the character"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        call arowana_as_mc
    else:
        call arowana_as_cory

    return

label arowana_as_mc:
    $ focus()
    show mc o:
        full
        right
        surprise
    "I peek behind of Mr. Cory"
    mc "What’s wrong, Mr. Arowana?"

    show arowana default:
        full
        center
    arowana "Everything. And it's. Mr. Wana"
    arowana "I have a crucial meeting in less than an hour…"

    show arowana squint:
        full
        center
    arowana "My boss EXPECTS me to be there. My colleagues EXPECTS me to be there. My entire career EXPECTS me to be there."
    arowana "The office’s slug expects me to be there…"

    show mc o:
        full
        right
    mc "But you’re still here…"

    show arowana mad:
        full
        center
        vibrate
    arowana "NO SHRIMP!"
    arowana "I AM HERE."
    arowana "Because of that stupid- egregious mantis shrimp!"

    show arowana default:
        full
        center
    arowana "My apologies that was unprofessional of me."

    show mc happy:
        full
        right
        surprise
    mc "It’s okay :D"

    show cory talk_hu:
        full
        centerleft
    with moveinleft
    cory "So he's been blocking all day now?"

    show arowana squint:
        full
        rightish
    with move
    arowana "Precisely. That's what the crowd's about."
    $ focus()

    menu:

        "Do you know why the shrimp’s blocking?":
            $ focus()
            show mc o:
                full
                right
            show arowana default:
                full
                center
            arowana "Unfortunately I do not."

            show mc o:
                full
                right
            mc "Not a thing?"

            show arowana squint:
                full
                center
                walkto(leftish)
            arowana "I’m sorry but I don’t think I want to entertain a child right now.."

            show mc pout:
                full
                right
            mc "Awww…"
            $ focus()
            return

        "Tell him to just swim there.":
            $ focus()
            show mc o:
                full
                right
            mc "Mr Wana, if work is so important"
            mc "Why don't you just leap up through the cave?"

            show arowana default:
                full
                center
            arowana "..."

            show mc excited:
                full
                right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "Just like how a flying fish would!"

            show arowana squint:
                full
                center
            arowana "..."

            show arowana mad:
                full
                center
                vibrate
            arowana "HAH! Yes! How wonderful I should've just tried that!."

            show mc happy:
                full
                right
                surprise
            mc "Right?! So you can just go!”"

            show arowana default:
                full
                center
            arowana "..."

            show arowana squint:
                full
                center
            arowana "... Young fish."

            show mc default:
                full
                right
                surprise
            mc "Yes? Do you need a push? Me and Mr Cory can help!"

            show arowana default:
                full
                center
            arowana "I have a meeting. I have a boss. I have a career."

            show arowana squint:
                full
                center
            arowana "And now I have a headache."

            show mc shock:
                full
                right
            mc "Huh? But why…"

            arowana "Please don't give me career advice again."

            "Mr. Cory quietly steps in beside me, bending down to murmur something."

            show cory side:
                full
                centerleft
            with moveinleft
            cory "Guppy."
            cory "Maybe let's leave the poor guy alone."

            show mc pout:
                full
                right
                surprise
            mc "But I wanna help!!"

            show cory side_close:
                full
                centerleft
            "Mr Cory sighed and proceeds to escort me away"

            show arowana smile:
                full
                rightish
            arowana "I admire your patience in tending to the young one, Corydoras."

            show cory fond:
                full
                centerleft
            cory "Heh, I'm starting to get the hang of it"

            show mc pout:
                full
                right
            mc "hnnrhhgh!!"
            $ focus()
            return

    return

label arowana_as_cory:
    $ focus()
    show cory smile_hu:
        full
        centerleft
    cory "Ay mano, care to tell us what's up?"
    cory "We needa cross the border too."

    show arowana smile:
        full
        rightish
    arowana "Ay cara, of course I'll tell you everything "
    arowana "I need him sober asap."

    show arowana squint:
        full
        rightish
    arowana "Can't risk getting fired now"
    $ focus()

    menu:

        "Got an idea why shrimp’s gatekeepin?":
            $ focus()
            show cory talk_hu:
                full
                centerleft
            show arowana default:
                full
                rightish
            arowana "Not a clue, unfortunately"
            arowana "All i know is, you have to win in some kind of duel against him."

            show arowana squint:
                full
                rightish
            arowana "And another thing that I know is that I’m not a fighter."

            show cory smile:
                full
                centerleft
            cory "Heh, you look tough though, why not give it a try?"

            arowana "Can’t risk having my ass beat."
            arowana "When it’s going to be absolutely clapped by the end of the day"

            show arowana default:
                full
                rightish
            arowana "As in, from the amount of work my boss gave me."

            show cory disrespect:
                full
                centerleft
            cory "Pfft, ya boss sure love yer hardworking ass huh"

            show arowana squint:
                full
                rightish
            arowana "I’m going to pretend I didn’t hear that."

            $ focus()
            $ add_clue("You have to win in a duel to pass the shrimp.")
            return

        "You know what's up with his bizarre act?":
            $ focus()
            show cory talk:
                full
                centerleft
            show arowana default:
                full
                rightish
            arowana "No, He’s usually not this strict. I pass him on the daily."
            arowana "And I’ve got my pristine saltwater licenses and all"
            arowana "Though he’s been muttering weird stuff…"
            arowana "\"I mustn’t repeat what i did\" is what i caught most clear.."

            show cory talk_hu:
                full
                centerleft
            cory "Huh.. something must’ve happened to him then"

            show arowana mad:
                full
                rightish
                vibrate
            arowana "How unprofessional of him! He shouldn’t be letting personal matters fiddle his work!"

            show arowana squint:
                full
                rightish
            arowana "Ugh, this path is the only way I commute to work in the sea.. What should i do now"

            show cory surprise:
                full
                centerleft
            cory "Wait, you work at the sea? How are ya doing that?!"

            show arowana default:
                full
                rightish
            arowana "Doing what exactly?"

            show cory talk_hu:
                full
                centerleft
            cory "Ya know! We're the freshwater kind.. how do ya brave the sea?"

            "The silver arowana opens his briefcase."
            "The inside is filled with an absurd amount of expensive-looking equipments."

            show cory smile:
                full
                centerleft
            cory "*whistle* sweet stuffs ya got!"

            show arowana default:
                full
                rightish
            arowana "This device allows me to survive in saltwater."

            show arowana squint:
                full
                rightish
            arowana "It cost me more money than I’m comfortable admitting."

            cory "How much are we talking?"

            arowana "I would rather not expose the numbers."
            arowana "But let’s say it cost me my nine lives."

            show mc o:
                full
                right
            with moveinleft
            mc "But you’re not a cat, you’re a fish!"

            show arowana default:
                full
                rightish
            arowana "Precisely. This device was handed down eight generations before me."

            show mc pout:
                full
                right
            mc "Aww.. If only we could buy it from you…"

            show cory upset:
                full
                centerleft
            cory "Buy?! With whose clams are we talking buy?!"

            show mc happy:
                full
                right
            mc "Hehe"

            show cory unimpressed:
                full
                centerleft
            cory "ay guppy clam’s tight on me too.."

            show arowana default:
                full
                rightish
            arowana "Tell you what."
            arowana "If you're really planning to confront that shrimp…"
            show arowana smile:
                full
                rightish
            arowana "You might as well take it."
            arowana "Here, have a spare."

            show cory surprise:
                full
                centerleft
            cory "For reals yo?!"

            arowana "Of course. But it's broken. Only 50% effective..."
            arowana "Take it or leave"

            show cory smile_hu:
                full
                centerleft
            cory "I'll gladly take it! Appreciate it mano!"

            show arowana smile:
                full
                rightish
            arowana "You put some sense into the guy for me in exchange alright?"

            $ focus()
            $ add_item("saltwater_survival_device")
            $ add_clue("The Mantis Shrimp is blocking the only path to the ocean.")
            return

    return
