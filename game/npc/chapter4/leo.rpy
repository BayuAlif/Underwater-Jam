label ch4_talk_leo:

    scene ch4_festival_day
    with dissolve

    if not ch4_leo_talked:
        play sound "audio/bush_rustling.mp3"
        leo "Greetings~!"

        show mc shock at mc_left, walkto(leftish, steps=2, walktime=0.5, bounce=0.2, sway=0.2)
        pause 0.5
        mc "waouh-!"

        "I stumbled backwards for Mr Larus to catch me, a super tall figure cast shadows over us."

        show mc shock at mc_left
        show scy surprise at npc_right, surprise
        scy "Careful now!"

        leo "Mmhehe my apologies for the spook, friend.."
        leo "You're searching for the golden fish, yes?"
        leo "Sparkling rainbow, lush tail.."

        show mc excited at mc_left, jumpmc, vibrate
        mc "Yes yes you're right!! Super spot on!"

        leo "I can be of your aid I assure you~!"
        leo "You just have to follow me!"

        show mc excited at mc_left, walkto(rightish, steps=3, walktime=1.0)
        pause 1.0

        show cory side at cory_left
        cory "Hold your seahorses!"
        show mc excited at mc_left

        menu:
            "How did ya know we're lookin for it?":
                cory "How did ya know we're lookin for it?"
                leo "Mmm.. it's no science, I've seen you go around asking about it.."
                leo "Like a little ballerina in a broken music box~"
                leo "Round and round you go, same question, same steps, same tune.."
                leo "Doesn't it make you dizzy?"
                show mc default at mc_left
                mc "mmn.. No! Because if I get dizzy.."
                mc "Mr. Cory and Mr. Larus will help make it go away!"
                mc "So I have nothing to worry about!"
                leo "I like your answer~!! Always so refreshing!"

            "How do we know ya really know of the fish's whereabouts?":
                cory "How do we know ya really know of the fish's whereabouts?"
                leo "Mm but until now.. you've been blindly following clues from strangers too right?"
                leo "What makes it different from what I said?"
                show scy smile at npc_right, surprise
                scy "He's right my friend, Cory! We have each other, it'll all be fine!"
                show mc happy at mc_left, surprise
                mc "Mhm yaa mr Cory you worry too much"
                mc "More than both of my parents combined.."
                show cory upset at cory_left, sink
                cory "Ugh.. maybe you're right my bad…"
                cory "Dunno what got to me"
                "Mr Cory looks like he's got a lot in mind"

        leo "Besides, the ocean's my playground~!"
        leo "I know it like the back of my hand..."
        leo "Which means i get to join your fun little party yes?"

        show mc happy at mc_left, jumpmc
        mc "Yaa! Welcome aboard miss…?"

        leo "Leo is fine~! Leo Drurga"

        show mc o at mc_left, surprise
        mc "Drurga.. :o"
        "The surname tickles something familiar in the back of my brain. Yet I can't really pinpoint what"

        show scy proud at npc_right, jump
        scy "We welcome you to our thrilling little search party, comrade!"

        leo "My oh my this would be spiiine tingling~!"
        leo "Ah but I doubt we can go into searching right away.."
        leo "Not when the chief's having trouble.."
        leo "He'll go whiny about how much help they require for the festival…"

        $ ch4_leo_talked = True
    else:
        leo "My, my, aren't you an eager little guppy~ Don't keep the chief waiting too long, hm?"

    hide cory
    hide scy
    hide mc
    with dissolve

    jump ch4_npc_explore_hub
