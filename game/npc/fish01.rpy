# =====================================
# BASS
# =====================================

label fish01:

    show f1 default at mc_pos
    show bass default at npc_pos

    bass "Hey there, guppy."

    f1 "Oh... hello."

    bass "You look like you've got a lot on your mind."

    f1 "I guess I do."

    bass "Hah. Don't we all."

    f1 "I'm Cory, by the way."

    bass "Bass."

    bass "And before you ask, no, I don't play an instrument."

    f1 "I wasn't going to ask that."

    bass "Sure."

    menu:

        "Who are you?":

            f1 "So... what exactly do you do around here?"

            bass "Me?"

            bass "I watch the current."

            bass "Sometimes it brings interesting things."

            bass "Sometimes it brings trouble."

            f1 "That's... surprisingly philosophical."

            show bass berpikir at npc_pos

            bass "I'm a fish, guppy."

            bass "We have a lot of time to think."

            show bass default at npc_pos


        "Have you seen anything unusual?":

            f1 "Have you seen anything strange around here?"

            bass "Depends."

            bass "What do you consider strange?"

            f1 "A golden fish, maybe?"

            show bass berpikir at npc_pos

            bass "..."

            bass "Maybe."

            f1 "You know something?"

            bass "Maybe I do."

            bass "Maybe you should keep looking."

            show bass default at npc_pos


        "Leave":

            f1 "I should get going."

            bass "Try not to get swept away, guppy."

            f1 "I'll try."

    hide f1
    hide bass

    return