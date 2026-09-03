# =========================================================
# CHAPTER 2 - NPC: GHOST FISH
# =========================================================


label ghostfish:

    $ cory_at_right = False

    scene expression get_dialogue_background()

    # =====================================================
    # OPENING
    # =====================================================

    show ghost default at ghost_pos
    show mc happy at mc_pos
    hide cory

    "A mysterious knife fish floats in tranquility. The dark atmosphere blending in, making its eyes and white stripes the only thing visible of her."

    "The way its fin flows is mesmerizing to watch. Yet Mr Cory already cowers behind me."


    # =====================================================
    # MC
    # =====================================================

    show mc happy at mc_pos
    hide cory

    mc "fish!! We meet again!"


    # =====================================================
    # GHOST
    # MC tetap ada
    # =====================================================

    show ghost default at ghost_pos

    ghost "Greetings. Adventurers."
    ghost "Alas fate has brought us together once more."


    # =====================================================
    # CORY
    # Cory menggantikan MC
    # =====================================================

    hide mc
    show cory sideclose at cory_right_pos

    cory "....."


    # =====================================================
    # GHOST
    # Cory tetap ada
    # =====================================================

    show ghost deadpan at ghost_pos

    ghost "Is your friend not very fond of ghosts?"


    # =====================================================
    # CORY
    # =====================================================

    hide mc
    show cory proud at cory_right_pos

    cory "W-WHO ME?! HAH! GHOSTS ARENT REAL! WHY SHOULD I BE AFRAID??"


    # =====================================================
    # MC
    # Cory diganti MC
    # =====================================================

    hide cory
    show mc pout at mc_pos

    mc "That's not very nice Mr Cory! Ms Ghost fish is very much real!"


    # =====================================================
    # CORY
    # MC diganti Cory
    # =====================================================

    hide mc
    show cory sideclose at cory_right_pos

    cory "W-Well! I'm going to pretend she's not!"


    # =====================================================
    # GHOST
    # Cory tetap
    # =====================================================

    show ghost mweheh at ghost_pos

    ghost "Heh.. how adorable…."


    # =====================================================
    # SELECT INTERACTOR
    # =====================================================

    hide cory
    show mc default at mc_pos

    call select_interactor

    if _return == "mc":
        jump ghostfish_as_mc
    else:
        jump ghostfish_as_cory



# =========================================================
# GHOST FISH - AS MC
# =========================================================

label ghostfish_as_mc:

    $ cory_at_right = False

    # MC aktif
    hide cory
    show mc o at mc_pos
    show ghost default at ghost_pos

    mc "Are you a ghost fish or a fish ghost?"


    # =====================================================
    # GHOST
    # MC tetap
    # =====================================================

    show ghost default at ghost_pos

    ghost "Brave little one…"


    show ghost deadpan at ghost_pos

    ghost "I believe you have far better questions to ask…"


    show ghost side at ghost_pos

    ghost "Perhaps of.. the golden fish.."
    ghost "You haven’t asked that for a while.."


    # =====================================================
    # MC
    # =====================================================

    show mc shock at mc_pos

    mc "ahh! You’re right. but.. how did you know that?!"


    # =====================================================
    # GHOST
    # =====================================================

    show ghost close at ghost_pos

    ghost "I am a fish who listens.."


    # =====================================================
    # OPTION 1 / OPTION 2
    # =====================================================

    menu:

        # =================================================
        # OPTION 1
        # =================================================

        "Do you know why mr shrimp is blocking the path?":

            # Ghost
            show ghost default at ghost_pos

            ghost "The mantis shrimp is but a lost cause…"


            # MC
            show mc shock at mc_pos

            mc "Huh?? What do you mean..?"


            # Ghost
            show ghost close at ghost_pos

            ghost "Everyone mistakes anger for strength."
            ghost "Do not mistake an obstacle for an enemy."


            # MC
            show mc excited at mc_pos

            mc "So he's a friend?! A potential friend!"
            mc "We don't have to fight it then!"


            # Ghost
            show ghost side at ghost_pos

            ghost "...I think you should know what you're fighting first."


            show ghost default at ghost_pos

            ghost "Perhaps a coal tar would help seek your answer"


            # MC
            show mc o at mc_pos

            mc "Whuh? But what's a coal tar… I don't think I've heard of it"


            # Ghost
            show ghost close at ghost_pos

            ghost "A strong smelling black lump"
            ghost "Mix it with something of hardened shell and it will weaken the shrimp"


            # MC
            show mc o at mc_pos

            mc "But.. you just told us not to fight the shrimp..? Why do we need to weaken it?"


            # Ghost
            show ghost deadpan at ghost_pos

            ghost "I never said so.. It is you who claimed that conclusion"


            # MC
            show mc default at mc_pos

            mc "Oh.. right! So we still need to fight it then?"


            # Ghost
            show ghost side at ghost_pos

            ghost "Perhaps so…"


            $ add_clue("The Mantis Shrimp may not need to be defeated. Find out what he wants.")
            $ add_clue("Coal Tar may be useful against the Mantis Shrimp.")



        # =================================================
        # OPTION 2
        # =================================================

        "Ms fish ghost, have you seen a super sparkly golden fish?":

            # MC
            show mc o at mc_pos


            # Ghost
            show ghost side at ghost_pos

            ghost "Yes I have…. It went in the direction of the sea…"


            show ghost default at ghost_pos

            ghost "Tell me, why do you choose to pursue the sacred cursed fish?"


            # MC
            show mc default at mc_pos

            mc "Because it's shiny! and not in the way.. most goldfishes shine"
            mc "The shape is weird too like it's from another universe"


            # Ghost
            show ghost deadpan at ghost_pos

            ghost "....and?"


            # MC
            show mc happy at mc_pos

            mc "Ah I also have one of its scales, it gave me the power to speak to fishes! And to breathe underwater for a little longer!"


            # Ghost
            show ghost default at ghost_pos

            ghost "Hm. And your presence… it's the same as ours, despite being human."
            ghost "Remarkable… that you can withstand its power at all."


            # MC
            show mc excited at mc_pos

            mc "So it really is a magic fish that gives you superpowers?!"


            # Ghost
            show ghost side at ghost_pos

            ghost "…The fish you pursue is no ordinary creature."
            ghost "It only surfaces when the sea is dying, when the waters are closest to ruin."


            show ghost close at ghost_pos

            ghost "A final gift from the Goddess of sea, left behind after her retirement… so the sea could still right itself, even without her."


            show ghost default at ghost_pos

            ghost "But that gift was meant for one of us. A creature of the sea. Not a visitor to it."


            # MC
            show mc shock at mc_pos

            mc "Ah… but what if it fall into the wrong hands?"


            # Ghost
            show ghost close at ghost_pos

            ghost "That is something only fate can answer."
            ghost "If it must be that way, then we can only watch as it happens."


            show ghost deadpan at ghost_pos

            ghost "The sea knows what it deserves."


            # =================================================
            # OPTION A / OPTION B
            # =================================================

            menu:

                # =============================================
                # OPTION A
                # =============================================

                "If it’s so powerful why not every fish in the sea chase it?":

                    # MC
                    show mc o at mc_pos


                    # Ghost
                    show ghost close at ghost_pos

                    ghost "Few even know this fish exists… fewer still know what it can do."
                    ghost "It doesn't announce itself. It doesn't wait to be found."


                    show ghost side at ghost_pos

                    ghost "The sea decides who's worthy long before they ever see it."


                    # MC
                    show mc happy at mc_pos

                    mc "You know so much of it! You must be suuuper worthy of having it no?"


                    # Ghost
                    show ghost close at ghost_pos

                    ghost "I’m but a messenger, brave one…"



                # =============================================
                # OPTION B
                # =============================================

                "Do you think I’m worthy of its power?":

                    # Ghost
                    show ghost side at ghost_pos

                    ghost "...."


                    show ghost deadpan at ghost_pos

                    ghost "I believe only your heart can answer that question."


                    # MC
                    show mc default at mc_pos

                    mc "I.. don’t know…"
                    mc "All i want is to be a fish…"


                    # Ghost
                    show ghost side at ghost_pos

                    ghost "... Then maybe that's all the sea needs.."



    # =====================================================
    # AFTER ALL OPTIONS
    # =====================================================

    # Ghost
    show ghost default at ghost_pos

    ghost "I wish you the best of luck in your pursue, little brave one.."


    # MC
    show mc o at mc_pos

    mc "Will we meet again?"


    # Ghost
    show ghost side at ghost_pos

    ghost "Perhaps, if fate allows…"


    show ghost close at ghost_pos

    ghost "May the sea be with you…"


    # MC
    show mc happy at mc_pos

    mc "Thank you Ms fish ghost!! I won't let you down!"


    # =====================================================
    # CLEAN UP BEFORE CORY ROUTE / RETURN
    # =====================================================

    hide mc
    hide cory
    hide ghost

    $ cory_at_right = False

    return



# =========================================================
# GHOST FISH - AS CORY
# =========================================================

label ghostfish_as_cory:

    $ cory_at_right = True

    # =====================================================
    # CORY
    # MC diganti Cory
    # =====================================================

    hide mc
    show ghost default at ghost_pos
    show cory surprise at cory_right_pos

    cory "M-me?! Why does it have to be me?!"


    # =====================================================
    # GHOST
    # Cory tetap
    # =====================================================

    show ghost side at ghost_pos

    ghost "you have a thousand questions running around in your head.."


    show ghost deadpan at ghost_pos

    ghost "yet your fear.. stops you from asking."
    ghost "Like shadows fleeing a light that follows without moving."


    # =====================================================
    # CORY
    # =====================================================

    hide mc
    show cory unimpressed2 at cory_right_pos

    cory "w-what that mean yo…"


    # =====================================================
    # GHOST
    # =====================================================

    show ghost mweheh at ghost_pos

    ghost "ask away, I promise I don't bite. much"


    # =====================================================
    # CORY
    # =====================================================

    hide mc
    show cory upset at cory_right_pos

    cory "WHADDYA MEAN MUCH?!"


    # =====================================================
    # CORY QUESTION
    # =====================================================

    menu:

        "do ya know why.. the shrimp is… stopping everyone from passing?":

            # Cory
            show cory netral_hu at cory_right_pos


            # Ghost
            show ghost close at ghost_pos

            ghost "perhaps I do."


            show ghost side at ghost_pos

            ghost "but why should I tell you"


            # Cory
            show cory side at cory_right_pos

            cory "because! We-we needa know!"


            # Ghost
            show ghost deadpan at ghost_pos

            ghost "not an enough reason…"


            # Cory
            show cory sideclose at cory_right_pos

            cory "because- we.. because the guppy needs to get to the- the golden fish!"


            # Ghost
            show ghost side at ghost_pos

            ghost "hmm.."


            show ghost close at ghost_pos

            ghost "rejected."


            # Cory
            show cory upset at cory_right_pos

            cory "what more do ya want from me mane?!"


            # Ghost
            show ghost deadpan at ghost_pos

            ghost "look behind you"


            # Cory
            show cory sideclose at cory_right_pos

            cory "NUH UH I'M NOT FALLING FOR THAT!"


            # Ghost
            show ghost deadpan at ghost_pos

            ghost "..."


            # Horror cutscene
            show ghost mweheh at ghost_pos

            ghost "boo…"


            # Cory
            show cory surprise at cory_right_pos

            cory "GYAAAAH!!"


            "Mr Cory bolts away with a high pitch loud scream"


            # MC
            # Cory sudah pergi, MC muncul
            hide cory
            show mc shock at mc_pos

            mc "ah! Mr Cory waaaaait!!"


            # Ghost
            # MC tetap
            show ghost mweheh at ghost_pos

            ghost "heh heh…"
            ghost "is that all you want to know..?"
            ghost "You’re not as chatty with other fishes…"


            # Cory kembali dan menggantikan MC
            hide mc
            show cory sideclose at cory_right_pos

            cory "YOU BEEN LISTENIN??"
            cory "AND WHY DO YA SOUND JEALOUS?!"


    # =====================================================
    # END
    # =====================================================

    $ cory_at_right = False

    hide mc
    hide cory
    hide ghost

    return