label bass_interaction:

    hide mc
    scene ch1_day
    $ focus()
    show mc default:
        unpose
        full
        right
    show bass default:
        unpose
        full 
        center
    "{i}A bass drifted lazily with the current.{/i}"
    "{i}It looked like it had completely forgotten what it was doing.{/i}"

    show mc happy:
        unpose
        full
        right
    mc "Hi, Mr. Bass!"

    show bass thinking:
        unpose
        full 
        center
    bass "...Hm..?"

    show bass oh:
        unpose
        full 
        center
        surprise
    bass "Oh."

    show bass default:
        unpose
        full 
        center
    bass "...Hi."

    show bass thinking:
        unpose
        full 
        center
    bass "and it's.. Ms. bass"

    show mc shock:
        unpose
        full
        right
        surprise
    mc "Oh! Right, my apologies, ms bass!"
    $ focus()

    menu:

        "I'm looking for a golden shiny diamond fish. Half the size of you!":
            $ focus()
            show bass default:
                unpose
                full 
                center
            show mc o:
                unpose
                full
                right
            mc "Have you seen one?"
            "The bass stared blankly."

            show bass thinking:
                unpose
                full 
                center
            bass "...Golden..."
            bass "...Gold..."
            bass "..."
            bass "..."

            show bass oh:
                unpose
                full 
                center
                surprise
            bass "...Oh!"
            bass "The shiny one!"

            show mc happy:
                unpose
                full
                right
                surprise
            mc "Mhm!"

            show bass default:
                unpose
                full 
                center
            bass "...Yeah."
            bass "I think it swam north."
            bass "...Maybe"

            show bass thinking:
                unpose
                full 
                center
            bass "...Pretty sure."
            bass "...Unless I'm remembering yesterday."

            show mc happy:
                unpose
                full
                right
                surprise
            mc "...Thank you Ms Bass!"

            show bass default:
                unpose
                full 
                center
            bass "No problem..."

            $ focus()

            $ add_clue("The Golden fish was seen swimming north.")

        "Ms Bass can you sing us a song? :o":
            $ focus()
            show mc o:
                unpose
                full
                right
            show bass default:
                unpose
                full 
                center
            bass "sing..?"

            show mc default:
                unpose
                full
                right
            mc "yeah! Anything is fine.. maybe something about the river?"

            show bass thinking:
                unpose
                full 
                center
            bass "....."
            bass "river..."
            bass "to.. the river.."
            bass "river.. River..."

            show bass oh:
                unpose
                full 
                center
                surprise
            bass "take me to the river!"
            bass "twas my grandfather billy's prime time"
            bass "gotta put big mouth's name back in business huh...?"

            show bass default:
                unpose
                full 
                center
            bass "thanks guppy"

            "{i}Ms Bass unlocked a core memory. Her nostalgic singing wafts through the river.{/i}"

            $ focus()

            $ add_clue("The Golden fish was seen swimming north.")

    return
