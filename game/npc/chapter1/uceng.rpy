label uceng_interaction:

    hide mc
    scene ch1_day
    $ focus()
    show mc default:
        full
        right
    show uceng default:
        full 
        center
    "Another fish was carefully arranging small stones into a neat circle."

    show mc happy:
        full
        right
    mc "Hello! Excuse me? Have you seen shiny shimmery golden fish around here?"

    show uceng annoyed:
        full 
        center
    uceng "...Can't talk."
    uceng "I'm busy."

    $ focus()

    menu:

        "I found a really cool rock earlier! Might be useful for your artwork!" if has_item("gold_nugget"):

            $ focus()
            show mc default:
                full
                right
            show uceng default:
                full 
                center
            mc "i found a really cool rock earlier! Might be useful for your artwork!"

            show uceng upset:
                full 
                center
            uceng "GASP i-is.. Is that..?"
            uceng "THE ONE AND ONLY 24 KARAT ROCK RIVER?!"

            "The Uceng fish snatched the rock from my grip."

            $ remove_item("gold_nugget")

            show cory unimpressed:
                full 
                leftish
            with moveinleft

            show uceng upset:
                full
                centerright
            with move
            cory "the what now.."

            show uceng default:
                full
                centerright
            uceng "i'll tell you what, the golden fish you spot? It aint no ordinary fish.."
            uceng "rumor has it.. that fish can cure the incurable and make the impossible possible!"
            show uceng default:
                full
                centerright
                surprise
            uceng "and this 24 karat rock river was believed to be one of its descendants!"

            show cory disrespect:
                full 
                leftish
            cory "looks like painted rock to me..."

            show mc shock:
                full
                right
            mc "cure the incurable...?"
            $ focus()
            $ add_clue("The golden fish can cure the incurable and make the impossible possible.")


        "The circle looks a little asymmetrical :o":
            $ focus()
            show mc o:
                full
                right
            show uceng upset:
                full
                center
                vibrate
            uceng "WHAT. DID. YOU. SAY?"
            show uceng upset:
                full
                center
                jump
                vibrate
            uceng "you dare come here to mock, and disgrace art?!"
            uceng "how would a guppy like you know make a symmetrical circle with plain rocks?!"

            show mc happy:
                full
                right
            mc "here, let me help!"

            "I carefully arranged the rocks into a neat symmetrical circle."

            show uceng upset:
                full
                center
                jump
            uceng "..."
            uceng "i..!"

            show uceng annoyed:
                full
                center
            uceng "hmph."
            $ focus()


        "It actually looks pretty nice! :D":
            $ focus()
            show mc default:
                full
                right
            show uceng default:
                full
                center
                jump

            uceng "Heh."
            uceng "Knew someone would appreciate true art."
            uceng "So... you were looking for this golden fish?"
            uceng "...It passed by earlier."
            show uceng annoyed:
                full
                center
            uceng "...Looked like it was heading toward the old current."

            show mc happy:
                full
                right
            mc "thank you Mr uceng fish!"

            show uceng default:
                full
                center
                surprise
            uceng "No problem!"

            show uceng annoyed:
                full
                center
            uceng "...watch the rocks."
            $ focus()
            $ add_clue("The old current lies to the north.")

    return
