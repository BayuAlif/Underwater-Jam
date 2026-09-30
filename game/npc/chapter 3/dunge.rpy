label ch3_crab_encounter:
    $ mark_npc_explored("dunge")
    show mc o:
        unpose
        full
        right
        walkloop
    with moveinright
    show dun smile:
        unpose
        full
        center
        walkloop
    with moveinright
    "We spotted another crustacean."
    "It's a grown-sized dungeness crab. He seems like a laid back crustacean."

    show dun smile:
        full
        leftish
    with move
    show scy smile:
        unpose
        full
        centerright
        walkloop
    with moveinright
    "Mr shrimp advanced towards him like seeing an old friend."
    scyllarus "My comrade in arms Dunge!"
    dun "Well butter my tail and call me a biscuit!"
    dun "Larus! Hows it hangin', you ol' bottom-feeder?"

    show cory talk:
        unpose
        full
        right
        walkloop
    with moveinright
    show scy smile:
        full
        center
    with move
    show dun smile:
        full
        left
    with move
    show mc o:
        full
        right
    mc "Larus..? Is that Mr Shrimp's real name?"

    show dun default:
        full
        left
    "The crab's expression subtly changed at my unfamiliar voice, it was close to that of disdain."
    "When he noticed me and Mr. Cory's presence."

    show dun mad:
        full
        left
    dun "... Hold your seahorses. What the hell are you doin' here?"
    dun "Your tail is supposed to be guardin' the salt-fresh border!"

    show cory talk_hu:
        full
        right
    cory "Chill out mane…"

    show dun default:
        full
        left
        surprise
    dun "!!! And what's this junk you bought with ya?"

    show dun yeesh:
        full
        left
        vibrate
    dun "Dont tell me you're rollin' with these filthy freshies??"
    dun "A guppy… and and!"
    hide mc
    hide cory
    hide scy
    hide dun
    "Choose who should ask Mr. Crab! The answers it gives may varied based on its relationship with the character"
    
    
    call screen choose_interactor(
        "Choose who should ask Mr. Crab!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_crab_as_mc
    elif selected_questioner == "cory":
        jump ch3_crab_as_cory
    else:
        jump ch3_crab_as_scyllarus

label ch3_crab_as_mc:
    menu:
        "Mr. Crab can you help us talk to the Empress?":
            show mc o:
                unpose
                full
                right
                walkloop
            with moveinright
            show dun default:
                unpose
                full
                center
                walkloop
            with moveinright
            "Mr crab gives me a humbling look…"

            show mc o:
                full
                right
            show dun default:
                full
                center
            dun "Help you? what are you even supposed to be?"
            dun "Some kinda a half-breed?"
            dun "Do your parents even have the green corals?"
            mc "Green corals? :0"

            show dun yeesh:
                full
                center
            dun "Yeah green corals. The damn corals you need to legally live around here."
            dun "You must've had some relative from the saltwater side hand 'em over to ya."

            show mc shock:
                full
                right
                surprise
            mc "I uhhhhhhh...."

            show dun default:
                full
                center
            dun ".... You dont got 'em?"

            show mc shock_hu:
                full
                unpose
                right
            mc "Um we dont have one….. is it alright, mr shrimp?"

            show scy default:
                unpose
                full
                centerright
                walkloop
            with moveinright
            show dun default:
                full
                leftish
            with move
            scyllarus "They're my company, Dunge! From the freshwater."
            scyllarus "They're just passing through the reefs, not taking up residence!"

            show scy default_om:
                full
                centerright
            scyllarus "Also the green coral policy is still up for debate!"

            show dun mad:
                full
                leftish
            dun "The empress firmly stated to not let any threats in."
            show dun mad:
                full
                leftish
                surprise
            dun "This is a clear violation of rules, Larus!"

            "No clue added."
            show mc pout:
                full
                right
            mc "Aw... Mr. Crab really won't let us through..."
            show cory side:
                unpose
                full
                right
            with moveinright
            show scy default_om:
                full
                center
            with move
            show dun mad:
                full
                left
            with move
            cory "Told ya, guppy. Let's see if one of us can talk some sense into him."
            hide mc
            hide cory
            hide scy 
            hide dun
            jump ch3_crab_interactor_retry

        "Do you hate freshwater creatures? :0":
            show mc o:
                unpose
                full
                right
                walkloop
            with moveinright
            show dun default:
                unpose
                full
                center
                walkloop
            with moveinright
            dun "Freshwater tadpoles are makin' our ocean colder just by breathin' up all the warm currents!"

            show mc default:
                full
                right
            mc "Uhm actually, mr.crab, according to marine biology…"

            show mc actually:
                full
                right
            mc "... water temperature is regulated by thermohaline currents and depth, not fish respiration."
            mc "So the freshwater species don't actually alter the ocean's temperature like that :D"

            show dun yeesh:
                full
                center
                surprise
            dun "... What a load of carp!"

            show dun default:
                full
                center
            dun "Haven't heard of such nonsense in all my years clawin' this reef!"
            dun "That's prolly just a fake propaganda, lil' guppy."
            dun "Theories created by… by.."

            "Mr crab pauses, searching for words."

            show dun yeesh:
                full
                center
            dun "... by those fancy university intellectuals…"
            show dun yeesh:
                full
                center
                surprise
            dun "... who doesn't know a damn thing about the real ocean livin'!"

            "No clue added."
            show mc o:
                full
                right
            mc "He doesn't seem very interested in marine biology..."
            show cory talk:
                full
                right
            with moveinright
            cory "Heh, clearly. Let someone else handle this ol' crab."
            hide dun
            hide cory
            hide mc
            jump ch3_crab_interactor_retry
    

label ch3_crab_interactor_retry:
    menu:
        "Let Cory speak to Mr. Crab":
            jump ch3_crab_as_cory
        "Let Scyllarus speak to Mr. Crab":
            jump ch3_crab_as_scyllarus
        "Step back to the reef":
            jump ch3_night_explore.loop

label ch3_crab_as_cory:
    menu:
        "Can you help us talk to the empress?":
            show dun default:
                unpose
                full
                leftish
                walkloop
            with moveinright
            show cory talk_hu:
                unpose
                full
                rightish
                walkloop
            with moveinright
            "The crab squints his eyes, slamming one claw into the sand with an irritated click."
            show dun default:
                full
                leftish
            dun "Who the fugu are you supposed to be?"

            show cory surprise:
                full
                rightish
                surprise
            cory "Ay no hate, amigo! Lower the claws a bit, yeah?"

            show cory talk:
                full
                unpose
                rightish
            cory "Look, we ain't enemies."
            cory "I actually got a lot of respect for saltwater culture."

            show cory talk_hu:
                full
                rightish
            cory "My primos back home are huge fan of Frank Ocean."

            show dun yeesh :
                full
                leftish
            dun "The eel does a singer's name got to do with it!"
            dun "You freshies are completely useless to this ocean, anyway."
            
            show cory talk_hu:
                full
                rightish
                surprise
            cory "Ay, that's not true!"
            cory "We wash down all the good minerals from upstream to keep your corals bloomin'"

            show dun mad:
                full
                leftish
                surprise
            dun "Frankly, my dear, I don't give a damn!"
            dun "My job is to block anyone tryin' to set claws or fins in here."
            hide cory
            hide dun
            call dunge_duel

            if _return != "win" and duel_result != "win":
                show dun mad:
                    unpose
                    full
                    leftish
                with moveinright
                dun "Hah! Ya got a lot of nerve, but my claws are harder than your head, freshie!"

                show cory hurt:
                    unpose
                    full
                    centerright
                with moveinright
                cory "Guh... that crab's tough..."

                show scy default:
                    unpose
                    full
                    right
                with moveinright
                show cory hurt:
                    full
                    center
                with move
                show dun mad:
                    full
                    left
                with moveinright
                scyllarus "Do not fret, comrades! We can regroup and try again!"
                jump ch3_night_explore.loop

            jump ch3_crab_cory_duel_won

        "Hold on, did you kidnap the sea bunny's family?":
            show cory unimpressed:
                unpose
                full
                rightish
                walkloop
            with moveinright
            show dun yeesh:
                unpose
                full
                leftish
                walkloop
            with moveinright
            cory "A brute Crustacean.. Big claws…"

            show cory unimpressed:
                full
                rightish
            cory "Did you lock up the sea bunny's whole family in there?"

            show dun yeesh:
                full
                leftish
            dun "Sea bunny family? Beats me!"
            dun "So many pest trynna start a rebellion around here, I lost count."

            show cory talk_hu:
                full
                rightish
            cory "The sea bunny family, cara."
            cory "The ones who were having a picnic under the acropora coral."

            show dun smile:
                full
                leftish
            dun "... oh, them. I ain' t kidnappin' nobody."
            dun "I'm holding those lethal biohazards in quarantine."

            show cory surprise:
                full
                rightish
                surprise
            cory "Biolethal hazard… what are you even talkin about-"

            show cory upset:
                full
                unpose
                rightish
            cory "Ya literally ate their baby and got a massive stomach ache.."
            cory "..because of their natural toxins."
            cory "No wonder they namin you Dunce."

            show dun mad:
                full
                leftish
            dun "Shut your darn mouth, you freshie."

            show dun yeesh:
                full
                leftish
                surprise
            dun "It's DUNGE! D-U-N-G-I!"

            show cory disrespect:
                full
                rightish
            cory "My mane can't even spell his own name"

            show dun default:
                full
                leftish
                vibrate
            dun "NGHHRR SHUT IT!!"

            show dun mad:
                full
                leftish
            dun "That counted as assassination attempt of the officer of the reef!"

            show cory side:
                full
                rightish
            cory "....! mane you're outta your mind."

            show dun default:
                full
                leftish
            dun "..... dont tell me youre plottin' to overthrow the empress too?"

            show dun mad:
                full
                leftish
                vibrate
            dun "Bless your heart, Larus, but I gotta fight anyone who threatens to take down the regime!"
            hide cory
            hide dun
            call dunge_duel

            if _return != "win" and duel_result != "win":
                show dun mad:
                    unpose
                    full
                    leftish
                with moveinright
                dun "Hah! Ya got a lot of nerve, but my claws are harder than your head, freshie!"

                show cory hurt:
                    unpose
                    full
                    centerright
                with moveinright
                cory "Guh... that crab's tough..."

                show scy default:
                    unpose
                    full
                    right
                with moveinright
                show cory hurt:
                    full
                    center
                with move
                show dun mad:
                    full
                    left
                with moveinright
                scyllarus "Do not fret, comrades! We can regroup and try again!"
                jump ch3_night_explore.loop

            jump ch3_crab_cory_duel_won



label ch3_crab_cory_duel_won:
    show dun yeesh:
        unpose
        full
        leftish
        walkloop
    with moveinright
    dun "Oof... holy barnacles, you got some heavy fins on ya, freshie..."

    show dun default:
        full
        leftish
    dun "Aight, aight! I yield! You beat me fair and square."

    show cory smile_hu:
        unpose
        full
        centerright
        walkloop
    with moveinright
    cory "Heh. Told ya, amigo. Never underestimate freshwater folks."

    show scy smile:
        unpose
        full
        right
        walkloop
    with moveinright
    show cory smile_hu:
        full
        center
    with move
    show dun default:
        full
        left
    with move
    scyllarus "Splendidly fought, Cory! Now, comrade Dunge, will you let us through?"

    show dun default:
        full
        left
    dun "Hmph. Fine. The path to the royal cavern's clear..."
    dun "If y'all are really plottin' to challenge the Empress, watch yer backs."
    dun "She holds a powerful golden scale... and she ain't gonna entertain sweet talk."

    "...! the golden scale?"

    scyllarus "We are deeply grateful for your cooperation, Dunge!"

    $ clue_golden_scale = True
    $ ch3_dunge_defeated = True
    $ mark_npc_explored("dunge")
    $ mark_npc_explored("teto")
    "Clue added: empress had the golden scale too."
    

    jump ch3_crab_post_resolution

label ch3_crab_as_scyllarus:
    menu:
        "Did you kidnap the seabunny's family?":
            show dun default:
                unpose
                full
                leftish
                walkloop
            with moveinright
            show scy default_om:
                unpose
                full
                rightish
                walkloop
            with moveinright
            scyllarus "I'm going to have to ask you to release them, Dunge!"

            show dun default:
                full
                leftish
            dun "Nuh uh! I ain't got a reason to!"
            dun "You're acting super weird Larus"

            show scy default:
                full
                rightish
            scyllarus "Imagine it's your family.. who's getting beheaded!"

            show scy default_om:
                full
                rightish
                surprise
            scyllarus "Remember your Billy!"

            "Dunge's claws slam against the sea floor, kicking up a cloud of sand."

            show dun mad:
                full
                leftish
                vibrate
            dun "DON'T YOU DARE TALK ABOUT HIM!"
            dun "..... do not talk about my son…"

            show dun default:
                full
                leftish
                vibrate
            dun "That's.. thats exactly why… i aint letting any immigrant pass.."
            dun "Larus, you forgot what happened at the Old Canal Junction!?"
            dun "When those freshwater folks broke the damn barriers!!"
            dun "Then a sudden toxic flood destroyed our home.."
            dun "And the debris!! crushed Billy's claw before he could swim away!"

            show scy default_om:
                full
                rightish
                vibrate
            scyllarus "That was a tragedy, Dunge!"
            scyllarus "But blaming an entire kind for the negligence of a rogue group is unfair!"
            scyllarus "Villainy is defined by actions, not by which side the border one is born!"
            scyllarus "We've been wrong, Dunce!"

            show dun default:
                full
                leftish
            dun "......."
            scyllarus "this is our chance to atone!"
            scyllarus "I assure you, my friends here can make a change!"
            dun ".......... fine."
            dun "Imma… release the seabunny family…"

            show scy smile:
                full
                rightish
            scyllarus "Thank you, my dear comrade in claws!"

            show scy default_om:
                full
                rightish
            scyllarus "Tell us.. Is there anything you know regarding the Empress' weakness?"
            dun "She holds a powerful golden scale."

            show scy surprise:
                full
                rightish
            "...! the golden scale??"
            dun "Aint really sure if she'll even listen if you want to negotiate. But you can try it."
            dun "But the worst case-and it's most likely to happen- you gonna fight her."
            dun "That aint gonna be easy."

            show scy laugh:
                full
                rightish
            scyllarus "I am forever grateful for your aid, Dunge!"
            dun ".... "
            "Dunge just nods."
            hide dun
            hide scy
            $ clue_golden_scale = True
            $ ch3_dunge_defeated = True
            $ mark_npc_explored("dunge")
            $ mark_npc_explored("teto")
            "Clue added: empress had the golden scale too."
            jump ch3_crab_post_resolution

        "We need to stop the empress!":
            show dun default:
                unpose
                full
                leftish
                walkloop
            with moveinright
            show scy default:
                unpose
                full
                rightish
                walkloop
            with moveinright
            dun "Whaddya mean 'stop the empress'??"

            show dun default:
                full
                leftish
                surprise
            dun "She's makin' the sea GREAT AGAIN!!"

            show scy default:
                full
                rightish
            scyllarus "I know but..!"
            scyllarus "I start to think that we've been wrong all this time!"
            scyllarus "My new friends here opened my eyes."
            
            show scy laugh:
                full
                rightish
            scyllarus "Right, guppy, Cory? kakakaka!"

            show dun mad:
                full
                leftish
            dun "...you shell brained shrimp!"
            dun "What kind of radical leftist freshwater ideology did they feed into your brain?"

            show scy default_om:
                full
                rightish
            scyllarus "This isnt about politics, Dunge!"

            show dun yeesh:
                full
                leftish
            dun "it IS about politics!"
            dun "Freshies be stealin our krills and tresspassin' our private reef property."
            dun "A few dead freshies is just the price of peace."
            scyllarus "I helped you cut em down, Dunge!"
            scyllarus "The.. Dead bodies…!"

            show scy default:
                full
                rightish
            scyllarus "It haunts you, too, right?"

            show dun default:
                full
                leftish
            dun "......."
            dun "........................"
            dun "Don't you go playing saint with me now."
            dun "… I aint gonna join your little party,"
            dun "........"
            dun "But if y'all wanna challenge her,"
            dun "You shoulda know that she holds a powerful golden scale."

            show scy surprise:
                full
                rightish
            "...! the golden scale?"
            dun "Aint got a clue if she'll even entertain your sweet talk if you try negotiatin."
            dun "But yall can try."

            show dun mad:
                full
                leftish
            dun "Now get off before I change my mind!"

            show scy smile:
                full
                rightish
            scyllarus "We deeply appreciate it, Dunge!"
            hide dun
            hide scy

            $ clue_golden_scale = True
            $ ch3_dunge_defeated = True
            $ mark_npc_explored("dunge")
            $ mark_npc_explored("teto")
            "Clue added: empress had the golden scale too."
            jump ch3_crab_post_resolution

label ch3_crab_post_resolution:
    if not item_collected:
        show mc o:
            unpose
            full
            right
            walkloop
        with moveinright
        show cory fond:
            unpose
            full
            center
            walkloop
        with moveinright
        mc "Look, Mr. Cory! There's some bright red seaweed over by the reef!"
        mc "We should take a look around the reef before going inside!"
        "The path to the Empress's lair is open, but we should explore the reef and collect the red seaweed first."
        jump ch3_night_explore.loop
    else:
        "The path to the Empress's lair is open."
        menu:
            "Enter the Crustacean Empress's Lair":
                jump ch3_boss_intro
            "Look around the reef first":
                jump ch3_night_explore.loop


    
