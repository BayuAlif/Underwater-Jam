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

        "Ask about the golden fish":

            show mc excited at mc_pos

            mc "Hey, have you seen anything unusual around here? Like... a golden fish?"

            show bass berpikir at bass_pos

            bass "..."

            show bass oh at bass_pos

            bass "Maybe."

            show mc shock at mc_pos

            mc "You know something?"

            show bass default at bass_pos

            bass "Maybe I do."

            bass "Currents don't lie, guppy. Something bright passed through here not too long ago."

            show bass berpikir at bass_pos

            bass "Didn't stick around long enough for me to get a good look, though."

            show mc actual at mc_pos

            mc "So it's really out there..."

            show bass default at bass_pos

            bass "Maybe you should keep looking."


        "Ask Bass to sing a song":

            show mc happy at mc_pos

            mc "Hey, sing me a song!"

            show bass oh at bass_pos

            bass "...What."

            show mc excited at mc_pos

            mc "C'mon, just one little tune!"

            show bass berpikir at bass_pos

            bass "Absolutely not."

            show mc pout at mc_pos

            mc "Aw, come on."

            show bass default at bass_pos

            bass "I said no, guppy."

            bass "Do I look like I hum for a living?"

            show mc shock at mc_pos

            mc "I mean, a little, yeah."

            show bass oh at bass_pos

            bass "...Fair."

            show bass berpikir at bass_pos

            bass "Still no."

            show mc happy at mc_pos

            mc "Worth a shot."

    hide mc
    hide bass

    return