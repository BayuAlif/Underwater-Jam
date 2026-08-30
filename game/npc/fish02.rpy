# =====================================
# UCENG
# =====================================

label fish02:

    show mc default at mc_pos
    show uceng default at uceng_pos

    uceng "HEY!"

    show mc shock at mc_pos

    mc "Whoa!"

    uceng "You're new here, aren't you?"

    show mc actual at mc_pos

    mc "Is it that obvious?"

    uceng "Very!"

    show mc pout at mc_pos

    mc "Great."

    show uceng default at uceng_pos

    uceng "Don't worry, I mean it in a good way!"

    mc "I'm not sure that makes it better."

    uceng "I'm Uceng!"

    show mc default at mc_pos

    mc "Cory."

    show mc happy at mc_pos

    uceng "Nice to meet you, Cory!"

    menu:

        "What are you doing here?":

            show mc default at mc_pos

            mc "What are you doing all the way out here?"

            show uceng default at uceng_pos

            uceng "Exploring!"

            show mc actual at mc_pos

            mc "By yourself?"

            uceng "Of course!"

            show uceng annoyed at uceng_pos

            uceng "Well..."

            uceng "Most of the time."

            show mc pout at mc_pos

            mc "You don't sound very sure."

            show uceng annoyed at uceng_pos

            uceng "I'm very brave."

            uceng "Usually."


        "Did you see anything?":

            show mc actual at mc_pos

            mc "Did you see anything strange around here?"

            show uceng default at uceng_pos

            uceng "Hmm..."

            uceng "I saw something moving earlier."

            show mc shock at mc_pos

            mc "What was it?"

            show uceng annoyed at uceng_pos

            uceng "I don't know!"

            uceng "It was really fast."

            uceng "And kind of shiny."

            show mc excited at mc_pos

            mc "Shiny?"

            show uceng default at uceng_pos

            uceng "Yeah!"

            uceng "You should probably ask someone else about it."

            show uceng upset at uceng_pos

            uceng "I'm not going near that thing again."

            show uceng default at uceng_pos


        "Leave":

            show mc default at mc_pos

            mc "I should get going."

            show uceng default at uceng_pos

            uceng "Okay!"

            uceng "Be careful, Cory!"

            show mc happy at mc_pos

            mc "You too, Uceng."

    hide mc
    hide uceng

    return