label ch4_talk_rin:

    scene ch4_festival_day
    with dissolve

    if not ch4_rin_talked:
        "An enormous whale shark towers the three of us."

        show mc happy at mc_left, jumpmc
        mc "Helloooo!! Good morning sir :D wao you're so biiiiig!!"

        rin "Ah-! Goodness Gracious!"
        rin "Oh just a guppy aren't you.. Scared the teeth out of old me.."

        show mc o at mc_left
        mc "oops hehe my bad..!"

        rin "No matter, Youth need not apologize for simply... being young"

        menu:
            "Have you seen a golden fish around?":
                show mc o at mc_left
                mc "We saw it but we lost it amongst these.. Golds you have piled up!"
                rin "A Golden fish, you say..?"
                "Mr Whale Shark's great eye drifts slowly toward the mountain of gold ornaments piled around him, as though sifting through decades of memory rather than metal."
                rin "Mm. I believe... I may have seen such a thing"
                show mc excited at mc_left, walkto(centerleft, steps=2, walktime=0.6, bounce=0.5, sway=0.3)
                pause 0.6
                mc "Really?! Can you tell us?"
                rin "Now, now. Need not to hurry young one."
                show mc pout at mc_left, sink
                mc "Mnn but I need to know now.. Before it goes further :("
                rin "Patience will reward you grand.."
                rin "We're currently having trouble with a festival that's going to occur tonight.."

            "Why's there so many gold here? Are you a gold thief :o":
                show mc o at mc_left
                mc "Why's there so many gold here? Are you a gold thief :o"
                rin "Thief? Oh no, no you have it wrong.."
                rin "I'm too old to be fretting about wealth.."
                rin "These golds will be used for an upcoming festival."
                rin "Golds are believed to stray away evil and bad omens, young one"

        show mc o at mc_left
        mc "A festival..?"

        show mc excited at mc_left, vibrate
        mc "Will there be lots of food? I haven't eaten in a while"

        rin "Oh why of course a big feast will occur!"
        rin "It's only fitting for a festival this important."

        show cory talk at cory_left
        cory "What's the festival about if we may know, sir?"

        rin "Yes, a dire one."
        rin "It's a festival that we held up once a year to ward off evil and bad luck"
        rin "It's the least we can do to repay the ocean.."
        rin "However, the sea has been quite turbulent lately, so we were forced to change plans and decided to host it twice a year instead."
        rin "But we completely underestimated how long gathering materials would take…"
        rin "... now we're worried we won't finish in time if the festival is held tonight."
        rin "That's why, as much as I'd love to help with you search, I can't assist you."

        show mc happy at mc_left, jumpmc
        mc "Alright then we'll help you!"

        rin "Oh how wonderful! The people thank you for your benevolence."
        rin "Rest assured travelers, we will be preparing the best of meals for your help."

        show cory smile at cory_left, surprise
        cory "About time we fill our stomachs.."

        show scy proud at npc_right, jump
        scy "Don't fret my friend we shall be of assistance! As much as we can!"

        $ ch4_rin_talked = True
    else:
        rin "Take your time, young travelers. Lending a hand with the festival materials will ensure our celebration succeeds tonight."

    hide cory
    hide scy
    hide mc
    with dissolve

    jump ch4_npc_explore_hub
