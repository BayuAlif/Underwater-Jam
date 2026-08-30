# =====================================
# LELE
# =====================================

label fish03:

    show f1 default at mc_pos
    show lele puratidur at npc_pos

    lele "..."

    f1 "Uh..."

    f1 "Hello?"

    show lele depan at npc_pos

    lele "You shouldn't be here."

    f1 "That's not a very friendly greeting."

    show lele curiga at npc_pos

    lele "It's not meant to be."

    f1 "Right."

    f1 "I'm Cory."

    lele "I know."

    f1 "You know my name?"

    lele "Word travels."

    menu:

        "Who are you?":

            f1 "So who are you?"

            lele "Lele."

            f1 "That's it?"

            lele "That's my name."

            f1 "Okay."

            lele "You ask a lot of questions."

            f1 "I'm trying to figure things out."

            lele "Then ask better questions."


        "Ask about the night":

            f1 "Why does everything feel different at night?"

            lele "Because the things hiding during the day start moving."

            f1 "That's... not comforting."

            lele "It wasn't supposed to be."

            f1 "You're not very reassuring, are you?"

            lele "No."


        "Leave":

            f1 "I'll leave you alone."

            lele "Good."

            f1 "See you around, I guess."

            lele "Maybe."

    hide f1
    hide lele

    return