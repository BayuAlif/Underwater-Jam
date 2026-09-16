label arowana_interaction:
    scene ch2_day
    $ focus()
    show mc o:
        full
        right
    show arowana mad:
        full
        center
        vibrate
    "A silver arowana kicks big rocks with a loud grumble."

    arowana "{sc}{size=45}SHHHRGGHHHJHNGHHRRAHH!!{/size}{/sc}"
    arowana "{sc}{size=45}MYBOSSISGOINTOKILLMEIMGOINGTOGETPUBLICLYEXECUTED{/size}{/sc}"
    show arowana mad:
        full
        rightish
        vibrate
    with move
    show cory talk_hu:
        full
        centerleft
    with moveinleft
    cory "Chill the eel out my guy!"
    cory "Those rocks can hurt a ton!"

    show arowana squint:
        ease 0.5
        full
        rightish
    arowana "Oh. A fish."
    show arowana default:
        full
        rightish
    arowana "My apologies, sir. I failed to notice you."

    show cory smile:
        full
        centerleft
    cory "Huh.. what a turn.."

    show cory surprise:
        full
        centerleft
        surprise
    cory "Wait! You a silver arowana right?! From Amazon?"

    show arowana smile:
        full
        rightish
        surprise
    arowana "...!"
    arowana "Eel yeah I am! From which side are you on brother?"

    show cory smile_hu:
        full
        centerleft
    cory "Nay, I ain't exactly from there, it's maranhao for me"

    show arowana smile:
        full
        rightish
        surprise
    arowana "Ouuu shii that's where vovo at!"

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

    call screen choose_interactor(
        "Choose who should ask Mr. Wana!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump arowana_as_mc

    jump arowana_as_cory


label arowana_as_mc:
    $ focus()
    show mc o:
        full
        right
        surprise
    show arowana default:
        full
        center
    mc "What's wrong, Mr. Arowana?"

    show arowana squint:
        full
        center
    arowana "Everything. And it's. Mr. Wana"
    arowana "I have a crucial meeting in less than an hour..."
    show arowana mad:
        full
        center
        vibrate
    arowana "My boss EXPECTS me to be there. My colleagues EXPECTS me to be there. My entire career EXPECTS me to be there."
    arowana "The office's slug expects me to be there..."

    show mc shock:
        full
        right
        surprise
    mc "But you're still here..."

    show arowana mad:
        full
        center
        vibrate 
    arowana "{sc}{size=45}NO SHRIMP!{/sc}{/size}"
    arowana "{sc}{size=45}I AM HERE.{/sc}{/size}"
    arowana "{sc}{size=45}Because of that stupid- egregious mantis shrimp!{/sc}{/size}"

    show arowana default:
        ease 0.5
        full
        center
    arowana "My apologies that was unprofessional of me."

    show mc happy:
        full
        right
        surprise
    mc "It's okay :D"

    show cory talk_hu:
        full
        centerleft
    with moveinleft
    cory "So he's been blocking all day now?"

    show arowana default:
        ease 0.5
        full
        rightish
    with move
    arowana "Precisely. That's what the crowd's about."
    $ focus()

    menu:

        "Do you know why the shrimp's blocking?":
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
                surprise
            mc "Not a single itty tiny thing?"

            show arowana squint:
                full
                center
                walkto(leftish)
            arowana "I'm sorry but don't think I want to entertain a child right now.."

            show mc pout:
                full
                right
            mc "Awww... hmph!"
            $ focus()


        "Tell him to just swim there.":
            $ focus()
            show arowana default:
                full
                center
            show mc o:
                full
                right
            mc "Mr Wana, if work is so important.."
            show mc default:
                full
                right
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
            arowana "{sc}{size=40}HAH! Yes! How wonderful I should've just tried that!.{/sc}{/size}"

            show mc happy:
                full
                right 
                surprise
            mc "Right?! So you can just go!"

            show arowana squint:
                full
                center
            arowana "..."
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
            mc "Huh? But why..."

            show arowana default:
                full
                center
            arowana "Please don't give me career advice again."

            show mc pout:
                full
                right 
                surprise         
            mc "But I'm just trying to heeelp..!!"

            show arowana default:
                full
                rightish
            with move
            
            show cory side:
                full
                centerleft
            with moveinleft
            cory "Guppy."
            cory "Let's leave the poor guy alone."

            show mc pout:
                full
                right 
                surprise  
            mc "But I wanna help!!"

            show cory side_close:
                full
                centerleft
            "Mr Cory sighed and proceeds to escort me away."

            show arowana smile:
                full
                rightish
            arowana "I admire your patience in tending to the young one, Corydoras."

            show cory proud:
                full
                centerleft
            cory "Heh, I'm starting to get the hang of it"
            $ focus()


label arowana_as_cory:
    $ focus()
    show cory smile_hu:
            full
            centerleft
    show arowana smile:
            full
            rightish
    cory "Ay mano, care to tell us what's up?"
    cory "We needa cross the border too."

    show arowana smile:
            full
            rightish
    arowana "Ay cara, of course I'll tell you everything"
    arowana "I need him sober asap."
    show arowana squint:
            full
            rightish
    arowana "Can't risk getting fired now"
    $ focus()

    menu:

        "Got any idea why shrimp's gatekeepin?":
            $ focus()
            show cory talk:
                full
                centerleft
            show arowana default:
                full
                rightish
            arowana "Not a clue, unfortunately"
            arowana "All I know is, you have to win in some kind of duel against him."

            show arowana squint:
                full
                rightish
            arowana "And another thing that I know is that I'm not a fighter."

            show cory smile_hu:
                full
                centerleft
            cory "Heh, you look tough though, why not give it a try?"

            show arowana default:
                full
                rightish
            arowana "Can't risk having my ass beat."
            show arowana squint:
                full
                rightish
            arowana "When it's going to be absolutely clapped by the end of the day"

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
            arowana "I'm going to pretend I didn't hear that."

            $ focus()
            $ add_clue("You have to win in a duel to pass the shrimp.")


        "You know what's up with his bizarre act?":
            $ focus()
            show cory talk:
                full
                centerleft
            show arowana default:
                full
                rightish
            arowana "No, He's usually not this strict"
            arowana "I pass him on the daily. He knew of my face by now i'm sure"
            arowana "Though he's been muttering weird stuff..."
            show arowana squint:
                full
                rightish
            arowana "\"I mustn't repeat what i did\" is what i caught most clear.."

            show cory talk_hu:
                full
                centerleft
            cory "Huh.. something must've happened to him then"

            show arowana mad:
                full
                rightish
                vibrate
            arowana "How unprofessional of him! He shouldn't be letting personal matters fiddle his work!"

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
            arowana "It cost me more money than I'm comfortable admitting."

            cory "How much are we talking?"

            show arowana squint:
                full
                rightish
            arowana "I would rather not expose the numbers."
            arowana "But let's say it cost me my nine lives."

            show mc o:
                full
                right
            with moveinleft
            mc "But you're not a cat, you're a fish!"

            show arowana default:
                full
                rightish
            arowana "Precisely. This device was handed down eight generations before me."

            show mc sad_hu:
                full
                right
            mc "Aww.. If only we could buy it from you..."

            show cory unimpressed:
                full
                centerleft
            cory "Buy?! With whose clams are we talking buy?"

            show mc happy:
                full
                right
            mc "Hehe"

            show cory side_close:
                full
                centerleft
            cory "ay guppy clam's tight on me too.."

            show arowana default:
                full
                rightish
            arowana "I'm sorry I can't be of much help."
            arowana "Wishing you the best on your journey.."

            $ focus()
            $ add_clue("The Mantis Shrimp is blocking the only path to the ocean.")

    return