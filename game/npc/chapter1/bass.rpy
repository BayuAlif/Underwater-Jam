label bass_interaction:

    hide mc
    scene ch1_day
    $ focus()
    show mc default:
        full
        right
    show bass default:
        full 
        center
    "{i}A bass drifted lazily with the current.{/i}"
    "{i}It looked like it had completely forgotten what it was doing.{/i}"

    show mc happy:
        full
        right
    mc "Hi, Mr. Bass!"

    show bass thinking:
        full 
        center
    bass "...Hm..?"

    show bass oh:
        full 
        center
        surprise
    bass "Oh."

    show bass default:
        full 
        center
    bass "...Hi."

    show bass thinking:
        full 
        center
    bass "and it's.. Ms. bass"

    show mc shock:
        full
        right
        surprise
    mc "Oh! Right, my apologies, ms bass!"
    $ focus()

    menu:

        "I'm looking for a golden shiny diamond fish. Half the size of you!":
            $ focus()
            show bass default:
                full 
                center
            show mc o:
                full
                right
            mc "Have you seen one?"
            "The bass stared blankly."

            show bass thinking:
                full 
                center
            bass "...Golden..."
            bass "...Gold..."
            bass "..."
            bass "..."

            show bass oh:
                full 
                center
                surprise
            bass "...Oh!"
            bass "The shiny one!"

            show mc happy:
                full
                right
                surprise
            mc "Mhm!"

            show bass default:
                full 
                center
            bass "...Yeah."
            bass "I think it swam north."
            bass "...Maybe"

            show bass thinking:
                full 
                center
            bass "...Pretty sure."
            bass "...Unless I'm remembering yesterday."

            show mc happy:
                full
                right
                surprise
            mc "...Thank you Ms Bass!"

            show bass default:
                full 
                center
            bass "No problem..."

            $ focus()

            $ add_clue("The Golden fish was seen swimming north.")


        "Ms Bass can you sing us a song? :o":
            $ focus()
            show mc o:
                full
                right
            show bass default:
                full 
                center
            bass "sing..?"

            show mc default:
                full
                right
            mc "yeah! Anything is fine.. maybe something about the river?"

            show bass thinking:
                full 
                center
            bass "....."
            bass "river..."
            bass "to.. the river.."
            bass "river.. River..."

            show bass oh:
                full 
                center
                surprise
            bass "take me to the river!"
            bass "twas my grandfather billy's prime time"
            bass "gotta put big mouth's name back in business huh...?"

            show bass default:
                full 
                center
            bass "thanks guppy"

            "{i}Ms Bass unlocked a core memory. Her nostalgic singing wafts through the river.{/i}"

            $ focus()

            $ add_clue("The Golden fish was seen swimming north.")

    return
