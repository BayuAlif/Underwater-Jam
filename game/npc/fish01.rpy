# =====================================
# BASS
# =====================================

label fish01:

    show mc default at mc_pos
    show bass default at bass_pos

    bass "Hey there, guppy."

    show mc actual at mc_pos

    mc "Oh... hello."

    bass "You look like you've got a lot on your mind."

    mc "I guess I do."

    show bass berpikir at bass_pos

    bass "Hah. Don't we all."

    show mc default at mc_pos

    mc "I'm just a little guppy, by the way."

    show bass default at bass_pos

    bass "Bass."

    show bass oh at bass_pos

    bass "And before you ask, no, I don't play an instrument."

    show mc shock at mc_pos

    mc "I wasn't going to ask that."

    show bass default at bass_pos

    bass "Sure."

    menu:

        "Who are you?":

            show mc default at mc_pos

            mc "So... what exactly do you do around here?"

            show bass oh at bass_pos

            bass "Me?"

            show bass default at bass_pos

            bass "I watch the current."

            bass "Sometimes it brings interesting things."

            bass "Sometimes it brings trouble."

            show mc actual at mc_pos

            mc "That's... surprisingly philosophical."

            show bass berpikir at bass_pos

            bass "I'm a fish, guppy."

            bass "We have a lot of time to think."

            show bass default at bass_pos


        "Have you seen anything unusual?":

            show mc actual at mc_pos

            mc "Have you seen anything strange around here?"

            show bass default at bass_pos

            bass "Depends."

            bass "What do you consider strange?"

            show mc excited at mc_pos

            mc "A golden fish, maybe?"

            show bass berpikir at bass_pos

            bass "..."

            show bass oh at bass_pos

            bass "Maybe."

            show mc shock at mc_pos

            mc "You know something?"

            show bass default at bass_pos

            bass "Maybe I do."

            bass "Maybe you should keep looking."

            show bass default at bass_pos


        "Leave":

            show mc default at mc_pos

            mc "I should get going."

            show bass default at bass_pos

            bass "Try not to get swept away, guppy."

            show mc happy at mc_pos

            mc "I'll try."

    hide mc
    hide bass

    return