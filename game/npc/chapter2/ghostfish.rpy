default ghost_first_met = False

label ghost_coal_tar_encounter:
    ghost "You shouldn't be carrying things you don't understand."

    show cory smile_hu:
        unpose
        full
        duo_left
    cory "Yeah.. that's right guppy.."
    cory "Finally, Some self preservation in ya!"

    show mc o:
        unpose
        full
        duo_right
        surprise
    mc "That.. wasn’t me…"

    "The water around us suddenly grows eerily still."
    "Faint glow pair of eyes emerges from the darkness."

    show ghost deadpan:
        unpose
        full
        duo_left
        float_idle
    with dissolve

    show cory surprise:
        unpose
        full
        duo_left
        surprise
        vibrate
    cory "GYAAAAAAA—"

    "Mr Cory jumped and immediately cowers behind my back with a loud screech"

    show cory side_close:
        unpose
        full
        farright
        toleft
        sink
    with move

    show mc o:
        unpose
        full
        duo_right
        surprise
    mc ":o"

    show mc excited:
        unpose
        full
        duo_right
        jumpmc
    if ghost_first_met:
        mc "Woah! It's you again, Ms. Fish!"
    else:
        mc "Woah! What are you?"

    show ghost default:
        unpose
        full
        duo_left
        float_idle
    ghost "A fish."

    show mc pout:
        unpose
        full
        duo_right
    mc "I can see that."

    ghost "Then you needn’t know more."

    show mc o:
        unpose
        full
        duo_right
    mc "Why are you here… fish?"

    show ghost side:
        unpose
        full
        duo_left
        float_idle
    ghost "You were meant to find me."

    show ghost close:
        unpose
        full
        duo_left
        float_idle
    ghost "But this second is not the time"
    ghost "We shall meet again.. very soon."

    show ghost side:
        unpose
        full
        duo_left
        float_idle
    ghost "Or perhaps.. we have met before."

    hide ghost with dissolve

    show mc happy:
        unpose
        full
        duo_right
    mc "Okay! Looking forward to meeting you again, fish!"
    mc "Mr Cory you can come out, it's fine now."

    $ ghost_first_met = True
    return

label ghostfish_interaction:
    hide mc
    hide cory
    scene ch2_night with dissolve
    $ focus()

    if not has_item("coal_tar"):
        show ghost default:
            unpose
            full
            center
            float_idle
        with moveinright

        show mc o:
            unpose
            full
            right
        with moveinright

        "A mysterious knife fish floats in tranquility. The dark atmosphere blending in, making its eyes and white stripes the only thing visible of her."
        "The way its fin flows is mesmerizing to watch. Yet Mr Cory already cowers behind me."

        show mc o:
            unpose
            full
            right
            surprise
        mc "Uhm... hello? Miss Fish?"

        show ghost default:
            unpose
            full
            centerright
            float_idle
        with move
        ghost "Greetings, little wanderer."
        ghost "You seek answers in the dark, yet your eyes haven't caught the strange remnant resting on the riverbed."

        show mc o:
            unpose
            full
            right
        mc "The riverbed? Is there something down there?"

        show ghost close:
            unpose
            full
            centerright
            float_idle
        ghost "Look closer before you speak with the unseen. Search the seabed first."

        hide ghost
        hide mc
        hide cory
        with dissolve

        $ ghost_first_met = True
        return "unexplored"

    show ghost default:
        unpose
        full
        center
        float_idle
    with moveinright
    show mc o:
        unpose
        full
        right
    with moveinright

    "A mysterious knife fish floats in tranquility. The dark atmosphere blending in, making its eyes and white stripes the only thing visible of her."
    "The way its fin flows is mesmerizing to watch. Yet Mr Cory already cowers behind me."

    show mc happy:
        unpose
        full
        right
        surprise
    mc "fish!! We meet again!"

    show ghost default:
        unpose
        full
        center
        float_idle
    with move
    ghost "Greetings. Adventurers."
    ghost "Alas fate has brought us together once more."

    show cory side:
        full
        unpose
        leftish
    with moveinleft
    show ghost deadpan:
        unpose
        full
        centerright
        float_idle
    with move
    cory "....."
    ghost "Is your friend not very fond of ghosts?"

    show cory proud:
        unpose
        full
        leftish
        surprise
    cory "W-WHO ME?! HAH! GHOSTS ARENT REAL! WHY SHOULD I BE AFRAID??"

    show mc pout:
        unpose
        full
        right
    mc "That's not very nice Mr Cory! Ms Ghost fish is very much real!"

    show cory side_close:
        unpose
        full
        leftish
        sink
    cory "W-Well! I'm going to pretend she's not!”"

    show ghost mweheh:
        unpose
        full
        centerright
        float_idle
    ghost "Heh.. how adorable…."
    $ focus()

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
        unpose
        full
        leftish
    show ghost default:
        unpose
        full
        centerright
        float_idle
    show mc o:
        unpose
        full
        right
    with dissolve

    mc "Are you a ghost fish or a fish ghost?"

    show ghost default:
        unpose
        full
        centerright
        float_idle
    ghost "Brave little one…"

    show ghost deadpan:
        unpose
        full
        centerright
        float_idle
    ghost "I believe you have far better questions to ask…"

    show ghost side:
        unpose
        full
        centerright
        float_idle
    ghost "Perhaps of.. the golden fish.."
    ghost "You haven’t asked that for a while.."
    

    show mc shock:
        unpose
        full
        right
        surprise
    mc "ahh! You’re right. but.. how did you know that?!"

    show ghost close:
        unpose
        full
        centerright
        float_idle
    ghost "I am a fish who listens.."

    $ focus()


    menu:

        "Do you know why mr shrimp is blocking the path?":
            $ focus()
            show mc o:
                unpose
                full
                right
            show ghost default:
                unpose
                full
                centerright
                float_idle
            ghost "The mantis shrimp is but a lost cause…"

            show mc shock:
                unpose
                full
                right
                surprise
            mc "Huh?? What do you mean..?"

            show ghost close:
                unpose
                full
                centerright
                float_idle
            ghost "Everyone mistakes anger for strength."
            ghost "Do not mistake an obstacle for an enemy."

            show mc excited:
                unpose
                full
                right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "So he's a friend?! A potential friend!"
            mc "We don't have to fight it then!"

            show ghost side:
                unpose
                full
                centerright
                float_idle
            ghost "...I think you should know what you're fighting first."

            show ghost default:
                unpose
                full
                centerright
                float_idle
            ghost "Perhaps a coal tar would help seek your answer"

            show mc o:
                unpose
                full
                right
            mc "Whuh? But what's a coal tar… I don't think I've heard of it"

            show ghost close:
                unpose
                full
                centerright
                float_idle
            ghost "A strong smelling black lump"
            ghost "Mix it with something of hardened shell and it will weaken the shrimp"

            show mc o:
                unpose
                full
                right
                surprise
            mc "But.. you just told us not to fight the shrimp..? Why do we need to weaken it?"

            show ghost deadpan:
                unpose
                full
                centerright
                float_idle
            ghost "I never said so.. It is you who claimed that conclusion"

            show mc default:
                unpose
                full
                right
            mc "Oh.. right! So we still need to fight it then?"

            show ghost side:
                unpose
                full
                centerright
                float_idle
            ghost "Perhaps so…"

            $ add_clue("The Mantis Shrimp may not need to be defeated. Find out what he wants.")
            $ add_clue("Coal Tar may be useful against the Mantis Shrimp.")
            $ focus()


        "Ms fish ghost, have you seen a super sparkly golden fish?":
            $ focus()
            show mc o:
                unpose
                full
                right
            show ghost side:
                unpose
                full
                centerright
                float_idle
            ghost "Yes I have…. It went in the direction of the sea…"

            show ghost default:
                unpose
                full
                centerright
                float_idle
            ghost "Tell me, why do you choose to pursue the sacred cursed fish?"

            show mc default:
                unpose
                full
                right
            mc "Because it's shiny! and not in the way.. most goldfishes shine"
            mc "The shape is weird too like it's from another universe"

            show ghost deadpan:
                unpose
                full
                centerright
                float_idle
            ghost "....and?"

            show mc happy:
                unpose
                full
                right
                surprise
            mc "Ah I also have one of its scales, it gave me the power to speak to fishes! And to breathe underwater for a little longer!"

            show ghost default:
                unpose
                full
                centerright
                float_idle
            ghost "Hm. And your presence… it's the same as ours, despite being human."
            ghost "Remarkable… that you can withstand its power at all."

            show mc excited:
                unpose
                full
                right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "So it really is a magic fish that gives you superpowers?!"

            show ghost side:
                unpose
                full
                centerright
                float_idle
            ghost "…The fish you pursue is no ordinary creature."
            ghost "It only surfaces when the sea is dying, when the waters are closest to ruin."

            show ghost close:
                unpose
                full
                centerright
                float_idle
            ghost "A final gift from the Goddess of sea, left behind after her retirement… so the sea could still right itself, even without her."

            show ghost default:
                unpose
                full
                centerright
                float_idle
            ghost "But that gift was meant for one of us. A creature of the sea. Not a visitor to it."

            show mc shock:
                unpose
                full
                right
                surprise
            mc "Ah… but what if it fall into the wrong hands?"

            show ghost close:
                unpose
                full
                centerright
                float_idle
            ghost "That is something only fate can answer."
            ghost "If it must be that way, then we can only watch as it happens."

            show ghost deadpan:
                unpose
                full
                centerright
                float_idle
            ghost "The sea knows what it deserves."


            menu:

                "If it’s so powerful why not every fish in the sea chase it?":
                    $ focus()
                    show mc o:
                        unpose
                        full
                        right
                    show ghost close:
                        unpose
                        full
                        centerright
                        float_idle
                    ghost "Few even know this fish exists… fewer still know what it can do."
                    ghost "It doesn't announce itself. It doesn't wait to be found."

                    show ghost side:
                        unpose
                        full
                        centerright
                        float_idle
                    ghost "The sea decides who's worthy long before they ever see it."

                    show mc happy:
                        unpose
                        full
                        right
                        surprise
                    mc "You know so much of it! You must be suuuper worthy of having it no?"

                    show ghost close:
                        unpose
                        full
                        centerright
                        float_idle
                    ghost "I’m but a messenger, brave one…"
                    $ focus()


                "Do you think I’m worthy of its power?":
                    $ focus()
                    show ghost side:
                        unpose
                        full
                        centerright
                        float_idle
                    ghost "...."

                    show ghost deadpan:
                        unpose
                        full
                        centerright
                        float_idle
                    ghost "I believe only your heart can answer that question."
 


    show ghost default:
        unpose
        full
        centerright
        float_idle
    ghost "I wish you the best of luck in your pursue, little brave one.."

    show mc o:
        unpose
        full
        right
    mc "Will we meet again?"

    show ghost side:
        unpose
        full
        centerright
        float_idle
    ghost "Perhaps, if fate allows…"

    show ghost close:
        unpose
        full
        centerright
        float_idle
    ghost "May the sea be with you…"

    show mc happy:
        unpose
        full
        right
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
        unpose
        full
        leftish
        jump
    show ghost side:
        unpose
        full
        centerright
        float_idle
    show mc default:
        unpose
        full
        right
    with dissolve

    cory "M-me?! Why does it have to be me?!"

    show ghost side:
        unpose
        full
        centerright
        float_idle
    ghost "you have a thousand questions running around in your head.."

    show ghost deadpan:
        unpose
        full
        centerright
        float_idle
    ghost "yet your fear.. stops you from asking."
    ghost "Like shadows fleeing a light that follows without moving."

    show cory unimpressed2:
        unpose
        full
        leftish
    cory "w-what that mean yo…"

    show ghost mweheh:
        unpose
        full
        centerright
        float_idle
    ghost "ask away, I promise I don't bite. much"

    show cory upset:
        unpose
        full
        leftish
        vibrate
    cory "WHADDYA MEAN MUCH?!"
    $ focus()

    menu:

        "do ya know why.. the shrimp is… stopping everyone from passing?":
            $ focus()
            show cory talk_hu:
                unpose
                full
                leftish
            show ghost close:
                unpose
                full
                centerright
                float_idle
            ghost "perhaps I do."

            show ghost side:
                unpose
                full
                centerright
                float_idle
            ghost "but why should I tell you"

            show cory side:
                unpose
                full
                leftish
            cory "because! We-we needa know!"

            show ghost deadpan:
                unpose
                full
                centerright
                float_idle
            ghost "not an enough reason…"

            show cory side_close:
                unpose
                full
                leftish
            cory "because- we.. because the guppy needs to get to the- the golden fish!"

            show ghost side:
                unpose
                full
                centerright
                float_idle
            ghost "hmm.."

            show ghost close:
                unpose
                full
                centerright
                float_idle
            ghost "rejected."

            show cory upset:
                unpose
                full
                leftish
                vibrate
            cory "what more do ya want from me mane?!"

            show ghost deadpan:
                unpose
                full
                centerright
                float_idle
            ghost "look behind you"

            show cory side_close:
                unpose
                full
                leftish
                vibrate
            cory "NUH UH I'M NOT FALLING FOR THAT!"

            show ghost deadpan:
                unpose
                full
                centerright
            ghost "..."

            show ghost mweheh:
                unpose
                center
                ease 0.1 medclose
                surprise
            with vpunch
            show cutjumpscare with vpunch
            ghost "{size=+8}boo…{/size}"

            show ghost mweheh:
                unpose
                ease 0.3 full
                center
                float_idle
            show cory surprise:
                unpose
                full
                leftish
                jump
                vibrate
            cory "{size=+10}GYAAAAH!!{/size}"

            hide cutjumpscare
            hide cory with moveoutleft
            "Mr Cory bolts away with a high pitch loud scream"

            show mc shock:
                unpose
                full
                right
                surprise
            mc "ah! Mr Cory waaaaait!!"

            hide mc with moveoutleft
            show ghost mweheh:
                unpose
                full
                center
                float_idle
            with move
            ghost "heh heh… putting the spook.. in spooktober"

    $ focus()
    hide mc
    hide ghost
    with dissolve

    return