# =====================================
# NPC 3 - LELE
# =====================================

label fish03:

    # =====================================
    # PEMBUKA
    # LELE + MC
    # =====================================

    $ cory_at_right = False

    # Pastikan Cory tidak terbawa dari scene sebelumnya
    hide cory

    show lele default at lele_pos
    show mc default at mc_pos

    "A catfish quietly watches from behind some seaweed."

    mc "I see you Mr catfish!"

    show lele curiga at lele_pos

    lele "..."

    show mc o at mc_pos

    "The catfish eyes me for a long second before going back into hiding. It appears to be somewhat shy?"

    "But as soon as Mr Cory swam forward its head peek in interest, like seeing an old friend"


    # =====================================
    # CORY MASUK
    # MC HILANG
    # LELE + CORY
    # =====================================

    $ cory_at_right = True

    hide mc
    hide cory

    show lele default at lele_pos
    show cory smile at cory_right_pos

    cory "ay.. Good pal, catfish."

    show lele default at lele_pos
    show cory smile at cory_right_pos

    lele "Here comes admin huh?"

    "mm maybe i should let mr cory ask instead?"


    # =====================================
    # PILIH SIAPA YANG BERTANYA
    # =====================================

    call screen who_should_ask(
        title="Choose who should ask mr catfish!",
        subtitle="The answers it gave may vary based on its relationship with the character"
    )

    if _return == "mc":
        jump fish03_ask_as_mc
    else:
        jump fish03_ask_as_cory


# =====================================
# FISH 03 - ASK AS MC
# =====================================

label fish03_ask_as_mc:

    # =====================================
    # MC + LELE ONLY
    # CORY HILANG
    # =====================================

    $ cory_at_right = False

    hide cory

    show lele default at lele_pos
    show mc o at mc_pos

    mc "Do you know where the golden fish went?"

    show lele curiga at lele_pos
    show mc o at mc_pos

    lele "..."

    show lele curiga at lele_pos
    show mc o at mc_pos

    "It watches me with a very serious judging look."

    show lele curiga at lele_pos
    show mc o at mc_pos

    lele "😹"


    # =====================================
    # MENU
    # =====================================

    menu:

        # =====================================
        # GIVE AMBALABU
        # =====================================

        "Give Ambalabu" if has_item("ambalabu"):

            show lele default at lele_pos
            show mc o at mc_pos

            "The catfish saw an opportunity and took the ambalabu from my hand."

            $ remove_item("ambalabu")

            show lele default at lele_pos
            show mc shock at mc_pos

            mc "Ah! I was going to give it nicely.."

            show lele default at lele_pos
            show mc shock at mc_pos

            lele "gokil"

            show lele default at lele_pos
            show mc o at mc_pos

            mc "gokil…?"

            show lele puratidur at lele_pos
            show mc o at mc_pos

            lele "super mega gokil"

            show lele puratidur at lele_pos
            show mc o at mc_pos

            mc "super mega gokil... :o"

            show lele puratidur at lele_pos
            show mc happy at mc_pos

            mc "gokil pro max!! :D"

            show lele curiga at lele_pos
            show mc happy at mc_pos

            lele "The sacred golden fish wields power enough to dry out all the water on this planet."

            show lele curiga at lele_pos
            show mc happy at mc_pos

            lele "Yet not many would dare to pursue until the finish line"

            show lele curiga at lele_pos
            show mc happy at mc_pos

            lele "I believe only those who remain by then are the people worthy of its blessing"

            show lele curiga at lele_pos
            show mc happy at mc_pos

            lele "Whether they shall bring the world prosper or agony."

            show lele curiga at lele_pos
            show mc happy at mc_pos

            lele "Repeating Fate only awaits by the hand of our God"

            show lele depan at lele_pos
            show mc happy at mc_pos

            lele "You should understand that better than anyone"

            show lele depan at lele_pos
            show mc shock at mc_pos

            mc "woah.. That's a lot to take in.."

            show lele depan at lele_pos
            show mc default at mc_pos

            mc "thank you mr catfish!"

            show lele default at lele_pos
            show mc default at mc_pos

            lele "mreow.. :3"


        # =====================================
        # WHAT DOES THAT MEAN
        # =====================================

        "What does that mean?":

            show lele default at lele_pos
            show mc default at mc_pos

            lele "That's why you should read more information"

            show lele default at lele_pos
            show mc o at mc_pos

            mc "...Ooh, okay..."

            show lele default at lele_pos
            show mc default at mc_pos

            mc "We were looking for the golden fish!"

            show lele puratidur at lele_pos
            show mc default at mc_pos

            lele "Yes, yes, yes. I can see that."

            show lele puratidur at lele_pos
            show mc default at mc_pos

            lele "The fish headed north."

            show lele puratidur at lele_pos
            show mc default at mc_pos

            mc "North!"

            show lele curiga at lele_pos
            show mc default at mc_pos

            lele "But stay vigilant!"

            show lele curiga at lele_pos
            show mc default at mc_pos

            lele "You might need to light your ways."


        # =====================================
        # HOW DO I EVEN SAY THAT
        # =====================================

        "How do I even say that...":

            show lele curiga at lele_pos
            show mc shock at mc_pos

            lele "..."

            show lele curiga at lele_pos
            show mc shock at mc_pos

            lele "Suki..."

            show lele curiga at lele_pos
            show mc o at mc_pos

            mc "...?"

            show lele curiga at lele_pos
            show mc o at mc_pos

            lele "Suki's Member... Member of Suki!!!"

            show lele curiga at lele_pos
            show mc o at mc_pos

            lele "Gotta be alert..."

            show lele curiga at lele_pos
            show mc o at mc_pos

            lele "Go away."

            show lele curiga at lele_pos
            show mc o at mc_pos

            "The catfish scares us away."


    # =====================================
    # CLEANUP
    # =====================================

    $ cory_at_right = False

    hide mc
    hide lele
    hide cory

    return



# =====================================
# FISH 03 - ASK AS CORY
# =====================================

label fish03_ask_as_cory:

    # =====================================
    # CORY + LELE ONLY
    # MC HILANG
    # =====================================

    $ cory_at_right = True

    hide mc

    # PASTIKAN DUA-DUANYA MUNCUL
    show lele default at lele_pos
    show cory talk at cory_right_pos


    menu:

        # =====================================
        # WHICH WAY IS IT PAL
        # =====================================

        "which way is it pal?, i needa find out":

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele default at lele_pos
            show cory talk at cory_right_pos

            cory "which way is it pal?, i needa find out"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele default at lele_pos
            show cory talk at cory_right_pos

            lele "North Kalimantan"

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele default at lele_pos
            show cory upset at cory_right_pos

            cory "is what a public liar woulda say!"

            show lele default at lele_pos
            show cory netral_hu at cory_right_pos

            cory "ay, spare me some real information would ya"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele puratidur at lele_pos
            show cory netral_hu at cory_right_pos

            lele "i'll tell ya tomorrow"

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele puratidur at lele_pos
            show cory netral_hu at cory_right_pos

            cory "Even with tempe goreng on the line?"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele default at lele_pos
            show cory netral_hu at cory_right_pos

            lele "tempting."

            show lele puratidur at lele_pos
            show cory netral_hu at cory_right_pos

            lele "but nah."

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele puratidur at lele_pos
            show cory upset at cory_right_pos

            cory "oh you watch your back"

            show lele puratidur at lele_pos
            show cory smile_hu at cory_right_pos

            cory "what about iced tea?"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele default at lele_pos
            show cory smile_hu at cory_right_pos

            lele "Appetizing.."

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele default at lele_pos
            show cory smile_hu at cory_right_pos

            cory "also with rice"

            show lele default at lele_pos
            show cory smile_hu at cory_right_pos

            cory "and spice"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele puratidur at lele_pos
            show cory smile_hu at cory_right_pos

            lele "that's what i'm talking about!"

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele puratidur at lele_pos
            show cory proud_hu at cory_right_pos

            cory "smart choice"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele default at lele_pos
            show cory proud_hu at cory_right_pos

            lele "but i want 10 of each of them"

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele default at lele_pos
            show cory surprise at cory_right_pos

            cory "oh shrimp"

            show lele default at lele_pos
            show cory surprise at cory_right_pos

            cory "where's the logic behind that?!"

            show lele default at lele_pos
            show cory ohiounimpressed1 at cory_right_pos

            cory "oh well what can i do,, we have a deal"

            # ---------------------------------
            # LELE
            # ---------------------------------

            show lele default at lele_pos
            show cory ohiounimpressed1 at cory_right_pos

            lele "awesome"

            show lele puratidur at lele_pos
            show cory ohiounimpressed1 at cory_right_pos

            lele "The fish headed north"

            # ---------------------------------
            # CORY
            # ---------------------------------

            show lele puratidur at lele_pos
            show cory smile at cory_right_pos

            cory "Alhamdulillah"


        # =====================================
        # GIVE AMBALABU
        # =====================================

        "Give Ambalabu" if has_item("ambalabu"):

            show lele default at lele_pos
            show cory smile at cory_right_pos

            $ remove_item("ambalabu")

            # LELE
            show lele default at lele_pos
            show cory smile at cory_right_pos

            lele "gokil"

            # CORY
            show lele default at lele_pos
            show cory disrespectful at cory_right_pos

            cory "super gokil"

            # LELE
            show lele puratidur at lele_pos
            show cory disrespectful at cory_right_pos

            lele "super mega gokil"

            # CORY
            show lele puratidur at lele_pos
            show cory smile at cory_right_pos

            cory "super mega gokil pro max"

            # LELE
            show lele default at lele_pos
            show cory smile at cory_right_pos

            lele "The sacred golden fish wields power enough to dry out all the water on this planet."

            show lele default at lele_pos
            show cory smile at cory_right_pos

            lele "Yet not many would dare to pursue until the finish line"

            show lele default at lele_pos
            show cory smile at cory_right_pos

            lele "I believe only those who remain by then are the people worthy of its blessing"

            show lele default at lele_pos
            show cory smile at cory_right_pos

            lele "Whether they shall bring the world prosper or agony."

            show lele default at lele_pos
            show cory smile at cory_right_pos

            lele "Repeating Fate only awaits by the hand of our God"

            show lele depan at lele_pos
            show cory smile at cory_right_pos

            lele "You should understand that better than anyone"

            # CORY
            show lele depan at lele_pos
            show cory talk at cory_right_pos

            cory "what does that even mean…"


        # =====================================
        # ASK DIRECTLY
        # =====================================

        "Ask directly":

            show lele default at lele_pos
            show cory talk at cory_right_pos

            cory "Hey Lele, we're tracking the golden fish."

            show lele curiga at lele_pos
            show cory talk at cory_right_pos

            lele "North. Just follow the stream up north."

            show lele curiga at lele_pos
            show cory smile at cory_right_pos

            cory "Appreciate it, pal."


    # =====================================
    # CLEANUP
    # =====================================

    $ cory_at_right = False

    hide mc
    hide lele
    hide cory

    return