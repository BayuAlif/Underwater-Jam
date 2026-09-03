# =========================================================
# NPC AROWANA INTERACTION
# =========================================================

label arowana:
    jump wana

label wana:

    scene expression get_dialogue_background()

    show wana default at wana_pos

    "A silver arowana kicks big rocks with a loud grumble. I wonder what it's mad about.."

    show mc o at mc_pos

    mc "Good morning si-"

    show wana mad at wana_pos

    wana "SHHHRGGHHHJHNGHHRRAHH!!"
    wana "MYBOSSISGOINTOKILLMEIMGOINGTOGETPUBLICLYEXECUTED"

    "Mr Cory takes a step forward, shielding me behind his taller frame"

    hide mc
    show cory netral_hu at cory_right_pos

    cory "Woah chill the eel out my guy!"
    cory "Those rocks can hurt a ton"

    show wana squint at wana_pos

    wana "Oh. A fish."
    wana "My apologies, sir. I failed to notice you"

    show cory surprise_hu at cory_right_pos

    cory "Huh.. what a turn.."
    cory "Wait! You a silver arowana right?"
    cory "From Amazon?"

    show wana smile at wana_pos

    wana "...!"
    wana "Eel yeah I am! From which side are you on brother?"

    show cory smile at cory_right_pos

    cory "Nay, I ain't exactly from there, it's maranhao for me"

    show wana smile at wana_pos

    wana "Ouuu shii that's where vovo at!"
    wana "I mean! How fortunate. My grandma.. also lives in that. State."

    show cory smile_hu at cory_right_pos

    cory "Pfft.. language barriers ay?"

    # =====================================================
    # Cory selesai bicara sebelum pilihan.
    # Hide Cory supaya tidak muncul saat select character.
    # =====================================================

    hide cory
    show mc default at mc_pos

    call select_interactor

    if _return == "mc":
        jump arowana_ask_as_mc
    else:
        jump arowana_ask_as_cory


# =========================================================
# AS MC
# =========================================================

label arowana_ask_as_mc:

    $ cory_at_right = False

    # MC berada di kanan.
    # Cory tidak tampil karena MC yang dipilih.
    hide cory
    show mc o at mc_pos

    "I peek behind of Mr. Cory"

    mc "What's wrong, Mr. Arowana?"

    show wana default at wana_pos

    wana "Everything. And it's. Mr. Wana"
    wana "I have a crucial meeting in less than an hour..."
    wana "My boss EXPECTS me to be there. My colleagues EXPECTS me to be there. My entire career EXPECTS me to be there."
    wana "The office's slug expects me to be there..."

    mc "But you're still here..."

    show wana mad at wana_pos

    wana "NO SHRIMP!"
    wana "I AM HERE."
    wana "Because of that stupid- egregious mantis shrimp!"

    show wana default at wana_pos

    wana "My apologies that was unprofessional of me."

    show mc happy at mc_pos

    mc "It's okay :D"

    # =====================================================
    # CORY SPEAKS
    # Cory harus berada di posisi kanan / posisi MC.
    # =====================================================

    hide mc
    show cory netral_hu at cory_right_pos

    cory "So he's been blocking all day now?"

    show wana default at wana_pos

    wana "Precisely. That's what the crowd's about."

    # Cory selesai bicara.
    # Kembalikan MC ke kanan.
    hide cory
    show mc default at mc_pos

    menu:

        "Do you know why the shrimp's blocking?":

            show mc o at mc_pos

            show wana default at wana_pos

            wana "Unfortunately I do not."

            mc "Not a thing?"

            show wana squint at wana_pos

            wana "I'm sorry but don't think I want to entertain a child right now.."

            show mc pout at mc_pos

            mc "Awww..."

        "Tell him to just swim there.":

            show mc o at mc_pos

            mc "Mr Wana, if work is so important"
            mc "Why don't you just leap up through the cave?"

            show wana default at wana_pos

            wana "..."

            show mc excited at mc_pos

            mc "Just like how a flying fish would!"

            show wana squint at wana_pos

            wana "..."

            show wana mad at wana_pos

            wana "HAH! Yes! How wonderful I should've just tried that!."

            show mc happy at mc_pos

            mc "Right?! So you can just go!"

            show wana default at wana_pos

            wana "..."
            wana "... Young fish."

            show mc default at mc_pos

            mc "Yes? Do you need a push? Me and Mr Cory can help!"

            wana "I have a meeting. I have a boss. I have a career."
            wana "And now I have a headache."

            show mc shock at mc_pos

            mc "Huh? But why..."

            wana "Please don't give me career advice again."

            # =================================================
            # CORY SPEAKS
            # Cory berada di kanan / posisi MC.
            # =================================================

            hide mc
            show cory side at cory_right_pos

            "Mr. Cory quietly steps in beside me, bending down to murmur something."

            cory "Guppy."
            cory "Maybe let's leave the poor guy alone."

            # Cory selesai.
            # MC kembali ke kanan.
            hide cory
            show mc pout at mc_pos

            mc "But I wanna help!!"

            # =================================================
            # CORY SPEAKS LAGI
            # Tetap di kanan.
            # =================================================

            hide mc
            show cory sideclose at cory_right_pos

            "Mr Cory sighed and proceeds to escort me away"

            show wana smile at wana_pos

            wana "I admire your patience in tending to the young one, Corydoras."

            show cory fond at cory_right_pos

            cory "Heh, I'm starting to get the hang of it"

            # Cory selesai.
            hide cory
            show mc pout at mc_pos

            mc "hnnrhhgh!!"


    # =====================================================
    # END MC ROUTE
    # =====================================================

    hide mc
    hide cory
    hide wana

    scene expression get_background()

    return


# =========================================================
# AS CORY
# =========================================================

label arowana_ask_as_cory:

    # Karena Cory dipilih sebagai interactor,
    # Cory berada di posisi kanan / posisi MC.
    $ cory_at_right = True

    hide mc
    show cory smile_hu at cory_right_pos

    cory "Ay mano, care to tell us what's up?"
    cory "We needa cross the border too."

    show wana default at wana_pos

    wana "Ay cara, of course I'll tell you everything"
    wana "I need him sober asap."
    wana "Can't risk getting fired now"

    menu:

        "Got an idea why shrimp's gatekeepin?":

            show cory netral_hu at cory_right_pos

            wana "Not a clue, unfortunately"
            wana "All I know is, you have to win in some kind of duel against him."
            wana "And another thing that I know is that I'm not a fighter."

            show cory smile at cory_right_pos

            cory "Heh, you look tough though, why not give it a try?"

            wana "Can't risk having my ass beat."
            wana "When it's going to be absolutely clapped by the end of the day"
            wana "As in, from the amount of work my boss gave me."

            show cory disrespectful at cory_right_pos

            cory "Pfft, ya boss sure love yer hardworking ass huh"

            show wana squint at wana_pos

            wana "I'm going to pretend I didn't hear that."

            $ add_clue("You have to win in a duel to pass the shrimp.")


        "You know what's up with his bizarre act?":

            show cory netral at cory_right_pos

            wana "No, He's usually not this strict"
            wana "I pass him on the daily. He knew of my face by now I'm sure"
            wana "Though he's been muttering weird stuff..."
            wana "\"I mustn't repeat what I did\" is what I caught most clear.."

            show cory netral_hu at cory_right_pos

            cory "Huh.. something must've happened to him then"

            show wana squint at wana_pos

            wana "How unprofessional of him! He shouldn't be letting personal matters fiddle his work!"
            wana "Ugh, this path is the only way I commute to work in the sea.. What should I do now"

            show cory surprise at cory_right_pos

            cory "Wait, you work at the sea? How are ya doing that?!"

            show wana default at wana_pos

            wana "Doing what exactly?"

            show cory netral_hu at cory_right_pos

            cory "Ya know! We're the freshwater kind.. how do ya brave the sea?"

            "The silver arowana opens his briefcase."
            "The inside is filled with an absurd amount of expensive-looking equipments."

            show cory smile at cory_right_pos

            cory "*whistle* sweet stuffs ya got!"

            show wana default at wana_pos

            wana "This device allows me to survive in saltwater."
            wana "It cost me more money than I'm comfortable admitting."

            cory "How much are we talking?"

            show wana squint at wana_pos

            wana "I would rather not expose the numbers."
            wana "But let's say it cost me my nine lives."

            # MC speaks.
            hide cory
            show mc o at mc_pos

            mc "But you're not a cat, you're a fish!"

            show wana default at wana_pos

            wana "Precisely. This device was handed down eight generations before me."

            show mc pout at mc_pos

            mc "Aww.. If only we could buy it from you..."

            # Cory speaks.
            hide mc
            show cory upset at cory_right_pos

            cory "Buy?! With whose clams are we talking buy?!"

            # MC speaks again.
            hide cory
            show mc happy at mc_pos

            mc "Hehe"

            # Cory speaks again.
            hide mc
            show cory unimpressed at cory_right_pos

            cory "ay guppy clam's tight on me too.."

            show wana default at wana_pos

            wana "Tell you what."
            wana "If you're really planning to confront that shrimp..."
            wana "You might as well take it."
            wana "Here, have a spare."

            show cory surprise at cory_right_pos

            cory "For reals yo?!"

            show wana default at wana_pos

            wana "Of course. But it's broken. Only 50%% effective..."
            wana "Take it or leave"

            show cory smile_hu at cory_right_pos

            cory "I'll gladly take it! Appreciate it mano!"

            show wana smile at wana_pos

            wana "You put some sense into the guy for me in exchange alright?"

            $ add_item("saltwater_device")
            $ add_clue("The Mantis Shrimp is blocking the only path to the ocean.")


    # =====================================================
    # END CORY ROUTE
    # =====================================================

    $ cory_at_right = False

    hide mc
    hide cory
    hide wana

    scene expression get_background()

    return