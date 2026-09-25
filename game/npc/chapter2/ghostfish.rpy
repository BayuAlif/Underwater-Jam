label ghostfish_interaction:
    hide mc
    scene ch2_night
    $ focus()
    show ghost default:
        full
        center
        float_idle
    show mc o:
        full
        right

    "A mysterious knife fish floats in tranquility. The dark atmosphere blending in, making its eyes and white stripes the only thing visible of her."
    "The way its fin flows is mesmerizing to watch. Yet Mr Cory already cowers behind me."

    show mc happy at mc_npc
    mc "fish!! We meet again!"

    show ghost default at ghost_right
    ghost "Greetings. Adventurers."
    ghost "Alas fate has brought us together once more."

    cory "....."

    show ghost deadpan at ghost_right
    ghost "Is your friend not very fond of ghosts?"

    $ focus()

    show cory proud at cory_npc
    cory "W-WHO ME?! HAH! GHOSTS ARENT REAL! WHY SHOULD I BE AFRAID??"

    show mc pout at mc_npc
    mc "That's not very nice Mr Cory! Ms Ghost fish is very much real!"

    show cory side_close at cory_npc
    cory "W-Well! I'm going to pretend she's not!”"

    show ghost mweheh at ghost_right
    ghost "Heh.. how adorable…."

    hide mc
    hide cory
    call screen choose_interactor(
        "Choose who should ask Ghostfish!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ghost_as_mc

    jump ghost_as_cory

label ghost_as_mc:

    show mc o at mc_npc
    show cory talk at cory_npc
    show ghost default at ghost_right

    mc "Are you a ghost fish or a fish ghost?"

    show ghost default at ghost_right
    ghost "Brave little one…"

    show ghost deadpan at ghost_right
    ghost "I believe you have far better questions to ask…"

    show ghost side at ghost_right
    ghost "Perhaps of.. the golden fish.."
    ghost "You haven’t asked that for a while.."

    show mc shock at mc_npc
    mc "ahh! You’re right. but.. how did you know that?!"

    show ghost close at ghost_right
    ghost "I am a fish who listens.."

    menu:

        "Do you know why mr shrimp is blocking the path?":

            show mc o at mc_npc
            show ghost default at ghost_right
            ghost "The mantis shrimp is but a lost cause…"

            show mc shock at mc_npc
            mc "Huh?? What do you mean..?"

            show ghost close at ghost_right
            ghost "Everyone mistakes anger for strength."
            ghost "Do not mistake an obstacle for an enemy."

            show mc excited at mc_npc
            mc "So he's a friend?! A potential friend!"
            mc "We don't have to fight it then!"

            show ghost side at ghost_right
            ghost "...I think you should know what you're fighting first."

            show ghost default at ghost_right
            ghost "Perhaps a coal tar would help seek your answer"

            show mc o at mc_npc
            mc "Whuh? But what's a coal tar… I don't think I've heard of it"

            show ghost close at ghost_right
            ghost "A strong smelling black lump"
            ghost "Mix it with something of hardened shell and it will weaken the shrimp"

            show mc o at mc_npc
            mc "But.. you just told us not to fight the shrimp..? Why do we need to weaken it?"

            show ghost deadpan at ghost_right
            ghost "I never said so.. It is you who claimed that conclusion"

            show mc default at mc_npc
            mc "Oh.. right! So we still need to fight it then?"

            show ghost side at ghost_right
            ghost "Perhaps so…"

            $ add_clue("The Mantis Shrimp may not need to be defeated. Find out what he wants.")
            $ add_clue("Coal Tar may be useful against the Mantis Shrimp.")

        "Ms fish ghost, have you seen a super sparkly golden fish?":

            show mc o at mc_npc
            show ghost side at ghost_right
            ghost "Yes I have…. It went in the direction of the sea…"

            show ghost default at ghost_right
            ghost "Tell me, why do you choose to pursue the sacred cursed fish?"

            show mc default at mc_npc
            mc "Because it's shiny! and not in the way.. most goldfishes shine"
            mc "The shape is weird too like it's from another universe"

            show ghost deadpan at ghost_right
            ghost "....and?"

            show mc happy at mc_npc
            mc "Ah I also have one of its scales, it gave me the power to speak to fishes! And to breathe underwater for a little longer!"

            show ghost default at ghost_right
            ghost "Hm. And your presence… it's the same as ours, despite being human."
            ghost "Remarkable… that you can withstand its power at all."

            show mc excited at mc_npc
            mc "So it really is a magic fish that gives you superpowers?!"

            show ghost side at ghost_right
            ghost "…The fish you pursue is no ordinary creature."
            ghost "It only surfaces when the sea is dying, when the waters are closest to ruin."

            show ghost close at ghost_right
            ghost "A final gift from the Goddess of sea, left behind after her retirement… so the sea could still right itself, even without her."

            show ghost default at ghost_right
            ghost "But that gift was meant for one of us. A creature of the sea. Not a visitor to it."

            show mc shock at mc_npc
            mc "Ah… but what if it fall into the wrong hands?"

            show ghost close at ghost_right
            ghost "That is something only fate can answer."
            ghost "If it must be that way, then we can only watch as it happens."

            show ghost deadpan at ghost_right
            ghost "The sea knows what it deserves."

            menu:

                "If it’s so powerful why not every fish in the sea chase it?":

                    show mc o at mc_npc
                    show ghost close at ghost_right
                    ghost "Few even know this fish exists… fewer still know what it can do."
                    ghost "It doesn't announce itself. It doesn't wait to be found."

                    show ghost side at ghost_right
                    ghost "The sea decides who's worthy long before they ever see it."

                    show mc happy at mc_npc
                    mc "You know so much of it! You must be suuuper worthy of having it no?"

                    show ghost close at ghost_right
                    ghost "I’m but a messenger, brave one…"

                "Do you think I’m worthy of its power?":

                    show ghost side at ghost_right
                    ghost "...."

                    show ghost deadpan at ghost_right
                    ghost "I believe only your heart can answer that question."

    show ghost default at ghost_right
    ghost "I wish you the best of luck in your pursue, little brave one.."

    show mc o at mc_npc
    mc "Will we meet again?"

    show ghost side at ghost_right
    ghost "Perhaps, if fate allows…"

    show ghost close at ghost_right
    ghost "May the sea be with you…"

    show mc happy at mc_npc
    mc "Thank you Ms fish ghost!! I won't let you down!"

    return

label ghost_as_cory:

    show mc default at mc_npc
    show cory surprise at cory_npc
    show ghost side at ghost_right

    cory "M-me?! Why does it have to be me?!"

    show ghost side at ghost_right
    ghost "you have a thousand questions running around in your head.."

    show ghost deadpan at ghost_right
    ghost "yet your fear.. stops you from asking."
    ghost "Like shadows fleeing a light that follows without moving."

    show cory unimpressed2 at cory_npc
    cory "w-what that mean yo…"

    show ghost mweheh at ghost_right
    ghost "ask away, I promise I don't bite. much"

    show cory upset at cory_npc
    cory "WHADDYA MEAN MUCH?!"

    menu:

        "do ya know why.. the shrimp is… stopping everyone from passing?":

            show cory talk_hu at cory_npc
            show ghost close at ghost_right
            ghost "perhaps I do."

            show ghost side at ghost_right
            ghost "but why should I tell you"

            show cory side at cory_npc
            cory "because! We-we needa know!"

            show ghost deadpan at ghost_right
            ghost "not an enough reason…"

            show cory side_close at cory_npc
            cory "because- we.. because the guppy needs to get to the- the golden fish!"

            show ghost side at ghost_right
            ghost "hmm.."

            show ghost close at ghost_right
            ghost "rejected."

            show cory upset at cory_npc
            cory "what more do ya want from me mane?!"

            show ghost deadpan at ghost_right
            ghost "look behind you"

            show cory side_close at cory_npc
            cory "NUH UH I'M NOT FALLING FOR THAT!"

            show ghost deadpan at ghost_right
            ghost "..."

            show ghost mweheh at ghost_right
            ghost "boo…"

            show cory surprise at cory_npc
            cory "GYAAAAH!!"

            "Mr Cory bolts away with a high pitch loud scream"

            show mc shock at mc_npc
            mc "ah! Mr Cory waaaaait!!"

            show ghost mweheh at ghost_right
            ghost "heh heh…"

    return
