label ghostfish_interaction:
    hide mc
    hide cory
    scene ch2_night with dissolve
    $ focus()

    show ghost default:
        full
        center
        float_idle
    with moveinright

    show mc o:
        full
        right
    with moveinright

    "A mysterious knife fish floats in tranquility. The dark atmosphere blending in, making its eyes and white stripes the only thing visible of her."
    "The way its fin flows is mesmerizing to watch. Yet Mr Cory already cowers behind me."

    show mc happy:
        full
        right
        surprise
    mc "fish!! We meet again!"

    show ghost default:
        full
        centerright
        float_idle
    with move
    ghost "Greetings. Adventurers."
    ghost "Alas fate has brought us together once more."

    show cory side:
        full
        unpose
        offscreenleft
    show cory side:
        leftish
    with moveinleft
    cory "....."

    show ghost deadpan:
        full
        centerright
        float_idle
    ghost "Is your friend not very fond of ghosts?"

    $ focus()

    show cory proud:
        full
        leftish
        jump
    cory "W-WHO ME?! HAH! GHOSTS ARENT REAL! WHY SHOULD I BE AFRAID??"

    show mc pout:
        full
        right
    mc "That's not very nice Mr Cory! Ms Ghost fish is very much real!"

    show cory side_close:
        full
        leftish
        sink
    cory "W-Well! I'm going to pretend she's not!”"

    show ghost mweheh:
        full
        centerright
        float_idle
    ghost "Heh.. how adorable…."

    hide mc
    hide cory
    hide ghost
    with dissolve

    call screen choose_interactor(
        "Choose who should ask Ghostfish!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ghost_as_mc

    jump ghost_as_cory

label ghost_as_mc:
    $ focus()
    show cory talk:
        full
        trio_left
    show ghost default:
        full
        trio_center
        float_idle
    show mc o:
        full
        trio_right
    with dissolve

    mc "Are you a ghost fish or a fish ghost?"

    show ghost default:
        full
        trio_center
        float_idle
    ghost "Brave little one…"

    show ghost deadpan:
        full
        trio_center
        float_idle
    ghost "I believe you have far better questions to ask…"

    show ghost side:
        full
        trio_center
        float_idle
    ghost "Perhaps of.. the golden fish.."
    ghost "You haven’t asked that for a while.."

    show mc shock:
        full
        trio_right
        surprise
    mc "ahh! You’re right. but.. how did you know that?!"

    show ghost close:
        full
        trio_center
        float_idle
    ghost "I am a fish who listens.."

    menu:

        "Do you know why mr shrimp is blocking the path?":
            $ focus()
            show mc o:
                full
                trio_right
            show ghost default:
                full
                trio_center
                float_idle
            ghost "The mantis shrimp is but a lost cause…"

            show mc shock:
                full
                trio_right
                surprise
            mc "Huh?? What do you mean..?"

            show ghost close:
                full
                trio_center
                float_idle
            ghost "Everyone mistakes anger for strength."
            ghost "Do not mistake an obstacle for an enemy."

            show mc excited:
                full
                trio_right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "So he's a friend?! A potential friend!"
            mc "We don't have to fight it then!"

            show ghost side:
                full
                trio_center
                float_idle
            ghost "...I think you should know what you're fighting first."

            show ghost default:
                full
                trio_center
                float_idle
            ghost "Perhaps a coal tar would help seek your answer"

            show mc o:
                full
                trio_right
            mc "Whuh? But what's a coal tar… I don't think I've heard of it"

            show ghost close:
                full
                trio_center
                float_idle
            ghost "A strong smelling black lump"
            ghost "Mix it with something of hardened shell and it will weaken the shrimp"

            show mc o:
                full
                trio_right
                surprise
            mc "But.. you just told us not to fight the shrimp..? Why do we need to weaken it?"

            show ghost deadpan:
                full
                trio_center
                float_idle
            ghost "I never said so.. It is you who claimed that conclusion"

            show mc default:
                full
                trio_right
            mc "Oh.. right! So we still need to fight it then?"

            show ghost side:
                full
                trio_center
                float_idle
            ghost "Perhaps so…"

            $ add_clue("The Mantis Shrimp may not need to be defeated. Find out what he wants.")
            $ add_clue("Coal Tar may be useful against the Mantis Shrimp.")

        "Ms fish ghost, have you seen a super sparkly golden fish?":
            $ focus()
            show mc o:
                full
                trio_right
            show ghost side:
                full
                trio_center
                float_idle
            ghost "Yes I have…. It went in the direction of the sea…"

            show ghost default:
                full
                trio_center
                float_idle
            ghost "Tell me, why do you choose to pursue the sacred cursed fish?"

            show mc default:
                full
                trio_right
            mc "Because it's shiny! and not in the way.. most goldfishes shine"
            mc "The shape is weird too like it's from another universe"

            show ghost deadpan:
                full
                trio_center
                float_idle
            ghost "....and?"

            show mc happy:
                full
                trio_right
                surprise
            mc "Ah I also have one of its scales, it gave me the power to speak to fishes! And to breathe underwater for a little longer!"

            show ghost default:
                full
                trio_center
                float_idle
            ghost "Hm. And your presence… it's the same as ours, despite being human."
            ghost "Remarkable… that you can withstand its power at all."

            show mc excited:
                full
                trio_right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "So it really is a magic fish that gives you superpowers?!"

            show ghost side:
                full
                trio_center
                float_idle
            ghost "…The fish you pursue is no ordinary creature."
            ghost "It only surfaces when the sea is dying, when the waters are closest to ruin."

            show ghost close:
                full
                trio_center
                float_idle
            ghost "A final gift from the Goddess of sea, left behind after her retirement… so the sea could still right itself, even without her."

            show ghost default:
                full
                trio_center
                float_idle
            ghost "But that gift was meant for one of us. A creature of the sea. Not a visitor to it."

            show mc shock:
                full
                trio_right
                surprise
            mc "Ah… but what if it fall into the wrong hands?"

            show ghost close:
                full
                trio_center
                float_idle
            ghost "That is something only fate can answer."
            ghost "If it must be that way, then we can only watch as it happens."

            show ghost deadpan:
                full
                trio_center
                float_idle
            ghost "The sea knows what it deserves."

            menu:

                "If it’s so powerful why not every fish in the sea chase it?":
                    $ focus()
                    show mc o:
                        full
                        trio_right
                    show ghost close:
                        full
                        trio_center
                        float_idle
                    ghost "Few even know this fish exists… fewer still know what it can do."
                    ghost "It doesn't announce itself. It doesn't wait to be found."

                    show ghost side:
                        full
                        trio_center
                        float_idle
                    ghost "The sea decides who's worthy long before they ever see it."

                    show mc happy:
                        full
                        trio_right
                        surprise
                    mc "You know so much of it! You must be suuuper worthy of having it no?"

                    show ghost close:
                        full
                        trio_center
                        float_idle
                    ghost "I’m but a messenger, brave one…"

                "Do you think I’m worthy of its power?":
                    $ focus()
                    show ghost side:
                        full
                        trio_center
                        float_idle
                    ghost "...."

                    show ghost deadpan:
                        full
                        trio_center
                        float_idle
                    ghost "I believe only your heart can answer that question."

    show ghost default:
        full
        trio_center
        float_idle
    ghost "I wish you the best of luck in your pursue, little brave one.."

    show mc o:
        full
        trio_right
    mc "Will we meet again?"

    show ghost side:
        full
        trio_center
        float_idle
    ghost "Perhaps, if fate allows…"

    show ghost close:
        full
        trio_center
        float_idle
    ghost "May the sea be with you…"

    show mc happy:
        full
        trio_right
        surprise
    mc "Thank you Ms fish ghost!! I won't let you down!"

    $ focus()
    hide mc
    hide cory
    hide ghost
    with dissolve

    return

label ghost_as_cory:
    $ focus()
    show cory surprise:
        full
        trio_left
        jump
    show ghost side:
        full
        trio_center
        float_idle
    show mc default:
        full
        trio_right
    with dissolve

    cory "M-me?! Why does it have to be me?!"

    show ghost side:
        full
        trio_center
        float_idle
    ghost "you have a thousand questions running around in your head.."

    show ghost deadpan:
        full
        trio_center
        float_idle
    ghost "yet your fear.. stops you from asking."
    ghost "Like shadows fleeing a light that follows without moving."

    show cory unimpressed2:
        full
        trio_left
    cory "w-what that mean yo…"

    show ghost mweheh:
        full
        trio_center
        float_idle
    ghost "ask away, I promise I don't bite. much"

    show cory upset:
        full
        trio_left
        vibrate
    cory "WHADDYA MEAN MUCH?!"

    menu:

        "do ya know why.. the shrimp is… stopping everyone from passing?":
            $ focus()
            show cory talk_hu:
                full
                trio_left
            show ghost close:
                full
                trio_center
                float_idle
            ghost "perhaps I do."

            show ghost side:
                full
                trio_center
                float_idle
            ghost "but why should I tell you"

            show cory side:
                full
                trio_left
            cory "because! We-we needa know!"

            show ghost deadpan:
                full
                trio_center
                float_idle
            ghost "not an enough reason…"

            show cory side_close:
                full
                trio_left
            cory "because- we.. because the guppy needs to get to the- the golden fish!"

            show ghost side:
                full
                trio_center
                float_idle
            ghost "hmm.."

            show ghost close:
                full
                trio_center
                float_idle
            ghost "rejected."

            show cory upset:
                full
                trio_left
                vibrate
            cory "what more do ya want from me mane?!"

            show ghost deadpan:
                full
                trio_center
                float_idle
            ghost "look behind you"

            show cory side_close:
                full
                trio_left
                vibrate
            cory "NUH UH I'M NOT FALLING FOR THAT!"

            show ghost deadpan:
                full
                trio_center
            ghost "..."

            show ghost mweheh:
                medclose
                trio_center
                surprise
            with vpunch
            ghost "{size=+8}boo…{/size}"

            show cory surprise:
                full
                trio_left
                jump
                vibrate
            cory "{size=+10}GYAAAAH!!{/size}"

            hide cory with moveoutleft
            "Mr Cory bolts away with a high pitch loud scream"

            show mc shock:
                full
                trio_right
                surprise
                jumpmc
            mc "ah! Mr Cory waaaaait!!"

            show ghost mweheh:
                full
                trio_center
                float_idle
            with move
            ghost "heh heh…"

    $ focus()
    hide mc
    hide ghost
    with dissolve

    return
