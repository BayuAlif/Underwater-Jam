label ch4_talk_leo:

    scene ch4_festival_day
    with dissolve

    if not ch4_leo_talked:
        $ focus()
        play sound "audio/sfx/bush_rustling.mp3"

        #posisi kalau leo dan mc sendiri di screen 
        show mc default:
            unpose
            full
            mc_left
        show leo default:
            unpose
            medium
            center
        with moveinbottom
        leo "Greetings~!"

        show mc shock:
            unpose
            full
            mc_left
            jump(windup=0.15, power=0.45, airtime=0.35)
        show leo default:
            ease 0.1 full
            center
        mc "waouh-!"

        "I stumbled backwards for Mr Larus to catch me, a super tall figure cast shadows over us."

        #posisi kalau leo bersama 1 karkater lg  di screen 
        show mc shock at mc_left
        show leo default:
            unpose
            full
            centerleft
        with move
        show shrimp surprise:
            unpose
            full
            rightish
        with moveinright

        show shrimp surprise:
            unpose
            full
            rightish
            jump(windup=0.15, power=0.45, airtime=0.35)
        with move
        scy "Careful now!"

        leo "Mmhehe my apologies for the spook, friend.."
        leo "You're searching for the golden fish, yes?"
        leo "Sparkling rainbow, lush tail.."

        show mc excited:
            unpose
            full
            mc_left
            jumpmc
            vibrate
        mc "Yes yes you're right!! Super spot on!"

        leo "I can be of your aid I assure you~!"
        leo "You just have to follow me!"

        show mc excited:
            unpose
            full
            mc_left
            jump(windup=0.15, power=0.45, airtime=0.35)
            walkto(rightish, steps=3, walktime=1.0)
        pause 1.0

        show leo niko:
            full
            unpose
            leftish
        with move

        show shrimp default:
            full
            unpose
            center
        with move

        show cory upset_hu:
            full
            unpose
            right
        with moveinright

        pause 0.5

        cory "Hold your seahorses!"

        #posisi kalau trio dengan leo
        show shrimp default behind cory:
            full
            unpose
            center
        with move
        show leo niko:
            full
            unpose
            leftish
        with move
        show mc shock:
            full
            mc_left
        $ focus()

        menu:
            "How did ya know we're lookin for it?":
                $ focus()
                cory "How did ya know we're lookin for it?"
                leo "Mmm.. it's no science, I've seen you go around asking about it.."
                leo "Like a little ballerina in a broken music box~"
                leo "Round and round you go, same question, same steps, same tune.."
                leo "Doesn't it make you dizzy?"
                show mc default:
                    unpose
                    full
                    mc_left
                mc "mmn.. No! Because if I get dizzy.."
                mc "Mr. Cory and Mr. Larus will help make it go away!"
                mc "So I have nothing to worry about!"
                leo "I like your answer~!! Always so refreshing!"

            "How do we know ya really know of the fish's whereabouts?":
                $ focus()
                cory "How do we know ya really know of the fish's whereabouts?"
                leo "Mm but until now.. you've been blindly following clues from strangers too right?"
                leo "What makes it different from what I said?"
                show shrimp smile behind cory:
                    full
                    unpose
                    center
                    jump(windup=0.15, power=0.45, airtime=0.35)
                with move

                scy "He's right my friend, Cory! We have each other, it'll all be fine!"
                show mc happy:
                    unpose
                    full
                    mc_left
                    surprise
                mc "Mhm yaa mr Cory you worry too much"
                mc "More than both of my parents combined.."
                show cory upset:
                    full
                    unpose
                    right
                    sink
                cory "Ugh.. maybe you're right my bad…"
                cory "Dunno what got to me"
                "Mr Cory looks like he's got a lot in mind"

        leo "Besides, the ocean's my playground~!"
        leo "I know it like the back of my hand..."
        leo "Which means i get to join your fun little party yes?"

        show mc happy:
            unpose
            full
            mc_left
            jumpmc
        mc "Yaa! Welcome aboard miss…?"

        leo "Leo is fine~! Leo Drurga"

        show mc o:
            unpose
            full
            mc_left
            surprise
        mc "Drurga.. :o"
        "The surname tickles something familiar in the back of my brain. Yet I can't really pinpoint what"

        show shrimp proud behind cory:
            full
            unpose
            center
            jump(windup=0.15, power=0.45, airtime=0.35)
        with move
        scy "We welcome you to our thrilling little search party, comrade!"

        leo "My oh my this would be spiiine tingling~!"
        leo "Ah but I doubt we can go into searching right away.."
        leo "Not when the chief's having trouble.."
        leo "He'll go whiny about how much help they require for the festival…"
        $ focus()

        $ ch4_leo_talked = True
    else:
        leo "My, my, aren't you an eager little guppy~ Don't keep the chief waiting too long, hm?"
        $ focus()

    hide cory
    hide shrimp
    hide mc
    hide leo
    with dissolve

    jump ch4_npc_explore_hub
