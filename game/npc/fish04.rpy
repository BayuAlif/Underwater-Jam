# =====================================
# GATOR
# =====================================

label fish04:

    show f1 default at mc_pos
    show gator default at npc_pos

    gator "..."

    f1 "You're a big one."

    show gator annoyed at npc_pos

    gator "And you're loud."

    f1 "I only said one sentence."

    gator "One sentence too many."

    f1 "Okay."

    f1 "I'm Cory."

    gator "Didn't ask."

    f1 "Yeah, I'm starting to notice a pattern here."

    show gator default at npc_pos

    menu:

        "Who are you?":

            f1 "So, what's your name?"

            gator "Gator."

            f1 "Gator?"

            gator "Yes."

            f1 "That's it?"

            gator "Yes."

            f1 "Right."

            gator "Are we done?"

            f1 "Probably."


        "Ask about the golden fish":

            f1 "Have you seen a golden fish?"

            gator "..."

            f1 "That's not a no."

            gator "You ask dangerous questions."

            f1 "Why?"

            gator "Because some answers are dangerous."

            f1 "That sounds like you know something."

            gator "Maybe I do."

            f1 "Are you going to tell me?"

            gator "No."


        "Leave":

            f1 "I'll be going now."

            gator "Good."

            f1 "Goodbye to you too."

            gator "..."

    hide f1
    hide gator

    return