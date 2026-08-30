# =====================================
# NPC 3 - LELE
# =====================================

label fish03:

    $ cory_at_right = False

    show lele default at lele_pos
    show mc default at mc_pos

    "A catfish quietly watches from behind some seaweed."

    show mc default at mc_pos

    mc "I see you Mr catfish!"

    show lele curiga at lele_pos

    lele "..."

    show mc o at mc_pos

    "The catfish eyes me for a long second before going back into hiding. It appears to be somewhat shy?"

    show mc default at mc_pos

    "But as soon as Mr Cory swam forward its head peek in interest, like seeing an old friend"

    # Cory maju menyapa Lele (Cory di kanan, Lele di kiri)
    $ cory_at_right = True
    hide mc
    show cory smile at cory_right_pos

    cory "ay.. Good pal, catfish."

    show lele default at lele_pos

    lele "Here comes admin huh?"

    "mm maybe i should let mr cory ask instead?"

    call screen who_should_ask(title="Choose who should ask mr catfish!", subtitle="The answers it gave may vary based on its relationship with the character")

    if _return == "mc":
        jump fish03_ask_as_mc
    else:
        jump fish03_ask_as_cory


# =====================================
# AS MC
# =====================================

label fish03_ask_as_mc:

    $ cory_at_right = False
    hide cory
    show lele curiga at lele_pos
    show mc o at mc_pos

    mc "Do you know where the golden fish went?"

    lele "..."

    "It watches me with a very serious judging look."

    lele "😹"

    menu:

        "😹 (Give Ambalabu)" if has_item("ambalabu"):

            show lele default at lele_pos

            "The catfish saw an opportunity and took the ambalabu from my hand."

            $ remove_item("ambalabu")

            show mc shock at mc_pos

            mc "Ah! I was going to give it nicely.."

            lele "gokil"

            mc "gokil…?"

            show lele puratidur at lele_pos

            lele "super mega gokil"

            show mc o at mc_pos

            mc "super mega gokil… :o"

            show mc happy at mc_pos

            mc "gokil pro max!! :D"

            show lele curiga at lele_pos

            lele "The sacred golden fish wields power enough to dry out all the water on this planet."

            lele "Yet not many would dare to pursue until the finish line"

            lele "I believe only those who remain by then are the people worthy of its blessing"

            lele "Whether they shall bring the world prosper or agony."

            lele "Repeating Fate only awaits by the hand of our God"

            show lele depan at lele_pos

            lele "You should understand that better than anyone"

            show mc shock at mc_pos

            mc "woah.. That’s a lot to take in.."

            show mc default at mc_pos

            mc "thank you mr catfish!"

            show lele default at lele_pos

            lele "mreow.. :3"


        "What does that mean?":

            show mc o at mc_pos
            show lele default at lele_pos

            lele "That’s why you should read more information 😂"

            mc "...Ooh, okay…"

            show mc default at mc_pos

            mc "We were looking for the golden fish!"

            show lele puratidur at lele_pos

            lele "Yes, yes, yes. I can see that. 😹"

            lele "The fish headed north."

            mc "North!"

            show lele curiga at lele_pos

            lele "But stay vigilant!"

            lele "You might need to light your ways."


        "How do I even say that…":

            show mc shock at mc_pos
            show lele curiga at lele_pos

            lele "..."

            lele "Suki…"

            mc "...?"

            lele "Suki’s Member… Member of Suki!!!"

            lele "Gotta be alert…"

            lele "Go away."

            "The catfish scares us away."

    $ cory_at_right = False
    hide mc
    hide lele
    hide cory

    return


# =====================================
# AS CORY
# =====================================

label fish03_ask_as_cory:

    $ cory_at_right = True
    hide mc
    show lele default at lele_pos
    show cory talk at cory_right_pos

    menu:

        "which way is it pal?, i needa find out":

            show cory talk at cory_right_pos
            show lele default at lele_pos

            cory "which way is it pal?, i needa find out"

            lele "North Kalimantan"

            show cory upset at cory_right_pos

            cory "is what a public liar woulda say!"

            show cory netral_hu at cory_right_pos

            cory "ay, spare me some real information would ya"

            show lele puratidur at lele_pos

            lele "i’ll tell ya tomorrow"

            cory "Even with tempe goreng on the line?"

            show lele default at lele_pos

            lele "tempting."

            show lele puratidur at lele_pos

            lele "but nah."

            show cory upset at cory_right_pos

            cory "oh you watch your back"

            show cory smile_hu at cory_right_pos

            cory "what about iced tea?"

            show lele default at lele_pos

            lele "Appetizing.."

            cory "also with rice"

            cory "and spice"

            show lele puratidur at lele_pos

            lele "that’s what i’m talking about!"

            cory "smart choice"

            show lele default at lele_pos

            lele "but i want 10 of each of them"

            show cory surprise at cory_right_pos

            cory "oh shrimp"

            cory "where’s the logic behind that?!"

            show cory unimpressed at cory_right_pos

            cory "oh well what can i do,, we have a deal"

            lele "awesome"

            show lele puratidur at lele_pos

            lele "The fish headed north"

            show cory smile at cory_right_pos

            cory "Alhamdulillah"


        "Give Ambalabu" if has_item("ambalabu"):

            show cory smile at cory_right_pos
            show lele default at lele_pos

            $ remove_item("ambalabu")

            lele "gokil"

            show cory disrespectful at cory_right_pos

            cory "super gokil"

            show lele puratidur at lele_pos

            lele "super mega gokil"

            show cory smile at cory_right_pos

            cory "super mega gokil pro max"

            show lele default at lele_pos

            lele "The sacred golden fish wields power enough to dry out all the water on this planet."

            lele "Yet not many would dare to pursue until the finish line"

            lele "I believe only those who remain by then are the people worthy of its blessing"

            lele "Whether they shall bring the world prosper or agony."

            lele "Repeating Fate only awaits by the hand of our God"

            show lele depan at lele_pos

            lele "You should understand that better than anyone"

            show cory talk at cory_right_pos

            cory "what does that even mean…"


        "Ask directly":

            show cory talk at cory_right_pos
            show lele default at lele_pos

            cory "Hey Lele, we're tracking the golden fish."

            show lele curiga at lele_pos

            lele "North. Just follow the stream up north."

            show cory smile at cory_right_pos

            cory "Appreciate it, pal."

    $ cory_at_right = False
    hide mc
    hide lele
    hide cory

    return