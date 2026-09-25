label lele_interaction:

    hide mc
    scene ch1_night
    $ focus()
    show mc default:
        full
        right
    show lele curiga:
        full
        offscreenright
    "A catfish quietly watches from behind some seaweed."

    show mc happy:
        full
        right
    mc "I see you Mr catfish!"

    show lele curiga:
        full
        offscreenright
        vibrate
    lele "..."

    show mc o:
        full
        right
    "The catfish eyes me for a long second before going back into hiding. It appears to be somewhat shy?"
    "But as soon as Mr Cory swam forward its head peek in interest, like seeing an old friend."

    show cory smile:
        full 
        leftish
    with moveinleft
    cory "ay.. Good pal, catfish."

    show lele default:
        full
        centerright
    with move
    lele "Here comes admin huh?"

    $ focus()

    hide mc
    hide cory
    call screen choose_interactor(
        "Choose who should ask Mr. Catfish!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump lele_as_mc

    jump lele_as_cory

label lele_as_mc:
    show mc o:
        full
        right
    show lele curiga:
        full
        center

    mc "Do you know where the golden fish went?"

    show lele default:
        full
        center
    lele "..."

    "It watches me with a very serious judging look."

    show lele tidur:
        full
        center
    lele "😹"

    menu:

        "😹 Give Ambalabu" if has_item("ambalabu"):
            show mc default:
                full
                right
            show lele default:
                full
                center
            "The catfish saw an opportunity and took the ambalabu from my hand."

            $ remove_item("ambalabu")

            show mc pout:
                full
                right
                surprise
            mc "Ah! I was going to give it nicely.."

            show lele default:
                full
                center
                surprise
            lele "gokil"

            show mc o:
                full
                right
                surprise
            mc "gokil...?"

            show lele tidur:
                full
                center
            lele "super mega gokil"

            show mc o:
                full
                right
                surprise
            mc "super mega gokil... :o"
            show mc happy:
                full
                right
                surprise
            mc "gokil pro max!! :D"

            show lele depan:
                full
                center
            lele "The sacred golden fish wields power enough to dry out all the water on this planet."
            lele "Yet not many would dare to pursue until the finish line"
            lele "Its entrance a grand warning to inevitable calamity of a threat caused none other by greed."
            lele "I believe only those who remain by then are the people worthy of its blessing"
            lele "Whether they shall bring the world prosper or agony."
            lele "Repeating Fate only awaits by the hand of our God"

            show lele depan:
                full
                center
            lele "You should understand that better than anyone"

            show mc shock:
                full
                right
                surprise
            mc "woah.. That's a lot to take in.."

            show lele default:
                full
                center
            lele "mreow.. :3"

            $ focus()

        "What does that mean?":
            show mc o:
                full
                right
                surprise

            show lele default:
                full
                center
            lele "That's why you should read more information"

            show mc shock:
                full
                right
                surprise
            mc "i uh, okay...?"

            show mc default:
                full
                right
                surprise
            mc "We were looking for the golden fish!"

            show lele tidur:
                full
                center
            lele "The fish headed y-axis (or \(+y\))"

            show mc shock:
                full
                right
                surprise
            mc "Whauh?? what's that supposed to mean?"
            mc "My mama never taught me math..."

            $ focus()
            $ add_clue("The fish headed north.")

        "How do I even say that...":
            $ focus()
            show mc shock:
                full
                right
                surprise

            show lele curiga:
                full
                center
            lele "..."
            lele "Suki..."

            show mc o:
                full
                right
                surprise
            mc "...?"

            show lele curiga:
                full
                center
                vibrate
                surprise
            lele "Suki's Member... Member of Suki!!!"
            lele "Gotta be alert..."
            lele "Go away."

            show lele curiga:
                full
                center
            with moveoutleft
            "The catfish scares us away."
            $ focus()

    return

label lele_as_cory:
    show cory smile:
        full 
        leftish
    show lele default:
        full
        centerright
    menu:   

        "Which way is it pal?, i needa find out":

            $ focus()
            show cory talk:
                full 
                leftish
            cory "which way is it pal?, i needa find out"

            show lele curiga:
                full
                centerright 
            lele "North Antartica"

            show cory upset:
                full 
                leftish
            cory "is what a public liar woulda say!"

            show cory talk_hu:
                full 
                leftish
            cory "ay, spare me some real information would ya"

            show lele tidur:
                full
                centerright 
            lele "i'll tell ya tomorrow"

            show cory smile:
                full 
                leftish
            cory "Even with tempe goreng on the line?"

            show lele default:
                full
                centerright 
                surprise
            lele "tempting."

            show lele tidur:
                full
                centerright
            lele "but nah."

            show cory smile_hu:
                full 
                leftish
            cory "Even with tempe goreng on the line?"

            show lele default:
                full
                centerright 
                surprise
            lele "Appetizing.."

            show cory smile_hu:
                full 
                leftish
                surprise
            cory "also with rice"
            cory "and spice"

            show lele tidur:
                full
                centerright
            lele "that's what i'm talking about!"

            show cory proud_hu:
                full 
                leftish
            cory "smart choice"

            show lele default:
                full
                centerright 
                surprise
            lele "but i want 10 of each of them"

            show cory unimpressed:
                full 
                leftish
                sink
            cory "oh well what can i do,, we have a deal"

            show lele default:
                full
                centerright 
                surprise
            lele "awesome"

            show lele tidur:
                full
                centerright
            lele "The fish headed north"

            show cory unimpressed2:
                full 
                leftish
            cory "Mane, all that trouble for a single worded answer?"

            $ focus()
            $ add_clue("The fish headed north.")

        "Give Ambalabu" if has_item("ambalabu"):

            $ remove_item("ambalabu")
            $ focus()
            show cory smile_hu:
                full 
                leftish
            show lele default:
                full
                centerright
                surprise
            lele "gokil"

            show cory disrespect:
                full 
                leftish
            cory "super gokil"

            show lele tidur:
                full
                centerright
            lele "super mega gokil"

            show cory smile_hu:
                full 
                leftish
                surprise
            cory "super mega gokil pro max"

            show lele depan:
                full
                centerright
            lele "The sacred golden fish wields power enough to dry out all the water on this planet."
            lele "Yet not many would dare to pursue until the finish line"
            lele "Its entrance a grand warning to inevitable calamity of a threat caused none other by greed."
            lele "I believe only those who remain by then are the people worthy of its blessing"
            lele "Whether they shall bring the world prosper or agony."
            lele "Repeating Fate only awaits by the hand of our God"

            show cory surprise:
                full 
                leftish
                surprise
            cory "... i uhh.. I'm not.. sure whatta say to that."

            show cory smile:
                full 
                leftish
            cory "but thanks pal..."

            $ focus()

            $ add_clue("All clues point toward the northern current.")

    $ add_clue("All clues point toward the northern current.")

    return
