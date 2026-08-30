# =====================================
# UCENG
# =====================================

label fish02:

    show f1 default at mc_pos
    show uceng default at npc_pos

    uceng "HEY!"

    f1 "Whoa!"

    uceng "You're new here, aren't you?"

    f1 "Is it that obvious?"

    uceng "Very!"

    f1 "Great."

    uceng "Don't worry, I mean it in a good way!"

    f1 "I'm not sure that makes it better."

    uceng "I'm Uceng!"

    f1 "Cory."

    uceng "Nice to meet you, Cory!"

    menu:

        "What are you doing here?":

            f1 "What are you doing all the way out here?"

            uceng "Exploring!"

            f1 "By yourself?"

            uceng "Of course!"

            uceng "Well..."

            uceng "Most of the time."

            f1 "You don't sound very sure."

            uceng "I'm very brave."

            uceng "Usually."


        "Did you see anything?":

            f1 "Did you see anything strange around here?"

            uceng "Hmm..."

            uceng "I saw something moving earlier."

            f1 "What was it?"

            uceng "I don't know!"

            uceng "It was really fast."

            uceng "And kind of shiny."

            f1 "Shiny?"

            uceng "Yeah!"

            uceng "You should probably ask someone else about it."

            show uceng upset at npc_pos

            uceng "I'm not going near that thing again."

            show uceng default at npc_pos


        "Leave":

            f1 "I should get going."

            uceng "Okay!"

            uceng "Be careful, Cory!"

            f1 "You too, Uceng."

    hide f1
    hide uceng

    return