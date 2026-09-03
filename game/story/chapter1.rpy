# =====================================
# CHAPTER 1
# =====================================

label chapter1:

    # =================================
    # DAY SETUP
    # =================================

    $ set_cycle("day")
    $ load_area("beach")

    # Background default (Full / Non-bordered) untuk gameplay & eksplorasi (Siang & Malam)
    $ set_background(
        "images/backgrounds/chapter1/chapter1_beach_day.png",
        "images/backgrounds/chapter1/bg night1.jpg"
    )
    $ set_dialogue_background(
        "images/backgrounds/chapter1/bg day1_bordered.jpg",
        "images/backgrounds/chapter1/bg night1_bordered.jpg"
    )

    scene expression get_background()

    call chapter1_opening

    call beach_hub

    jump chapter1_ending


# =====================================
# CHAPTER 1 OPENING
# =====================================

label chapter1_opening:

    # Saat teks sistem / narator awal, gunakan background full (non-bordered)
    scene expression "images/backgrounds/chapter1/chapter1_beach_day.png"

    "An unknown brazen voice pulled me out of a trance as my gaze dropped down to be unexpectedly met with a bottomless pit right before my toes, flinching back in instinct."

    # Saat dialog karakter dimulai, beralih ke background bordered
    scene expression get_dialogue_background()

    show mc shock at mc_pos
    mc "...!"

    show cory netral at cory_pos
    cory "You take one more step..."

    cory "...And you'd be a goner."

    "The image of the darkness beyond is burned crisp into my mind. The current below twisted slowly as if alive, taunting those who stare long enough."

    cory "Not exactly the kinda place ya wanna stumble into.."

    show mc o at mc_pos
    "I slowly nodded in agreement. Before my mind could curiously wonder more to the depth of said cliff, I looked up to the source of voice."

    show cory netral at cory_pos
    show mc shock at mc_pos
    "What I expected was a kind mr human. I was instead met with a fish!"

    show mc excited at mc_pos
    "A Corydoras perhaps? My eyes lit up with unbridled enthusiasm"

    "Excitement held out, I mustn't forget to express my gratitude to those who saved my life."

    "I start to wiggle my body in an interpretative dance of gratitude."

    show cory unimpressed2 at cory_pos
    cory "..."

    cory "Mane just what the fugu is you doing..?!"

    show mc actual at mc_pos
    mc "Fishes communicate through gestures and and visual as well as colors I'm trying to express my gratitude through-"

    show mc o at mc_pos
    mc "Wait.. I just spoke in water..."

    show mc excited at mc_pos
    mc "ARE YOU GETTING ME, MR FISH?? :D"

    show cory surprise at cory_pos
    cory "chill the carp out! Yes and yes I'm understanding all the word you saying"

    show mc excited at mc_pos
    mc "I'M HAVING A CONVERSATION WITH A FISH!!"

    "Struck with a thunder of explosive excitement a loud squeak pushed through me. At the same time my mouth is wide open-"

    show mc dizzy at mc_pos
    mc "{i}COUGHCOUCHCOUGHBLURURHRGHUGUHRH-!{/i}"

    show cory surprise at cory_pos
    cory "Holy SHRIMP you still need air huh? I think I have just what ya need"

    # cutscene: cory putting a fishbowl on mc's head

    mc "Huh-? Whoaaah.. I can see better now!"

    show cory proud at cory_pos
    cory "You sure do!"

    show cory smile at cory_pos
    cory "But.. huh is that a first.. alien guppy of two legs speaks under water.. you a witch?"

    show mc pout at mc_pos
    mc "Am no witch! Am fish! It's my ever dream!"

    show mc o at mc_pos
    mc "Ah but I couldn't do any of this before... maybe it's because of.."

    "My gaze fell down to the translucent scale I didn't realize was clutched tight in my palm the entire time. Curious, I let go of it just for one millisecond."

    "True to my hypothesis, in that frozen moment everything went silent. Save for the tranquil current whirring in my ears."

    "But as soon as I made contact with the magical scale. It all became lively. Voices, distant and nearby, fill in the atmosphere. It's like shopping at a market on a sunny sunday!"

    "Mr kind fish's voice became audible again too.."

    show cory fond at cory_pos
    cory "----in't ya one step closer to a dream come true, little guppy?"

    show mc excited at mc_pos
    "This is the power of only one scale. Imagine what a whole fish can do..."

    show mc o at mc_pos
    mc "Mr kind fish did you see a shiny golden fish that passed by?"

    show cory smile at cory_pos
    cory "Golden fish? I ain't see no gold, what I saw was straight DIAMOND."

    cory "Visceral beauty struck me tantalized. type shrimp."

    show cory netral at cory_pos
    cory "Didn't bother following it though. That and ion remember where it went."

    show mc o at mc_pos
    mc "Whuh? Why? :o"

    show cory netral_hu at cory_pos
    cory "Ay.. how should I be telling you this.. Pretty things usually mean trouble around here."

    cory "And I might just be too out of their league."

    show mc excited at mc_pos
    mc "Yeah! I know! Like blue dragons and and lionfish and"

    show cory smile_hu at cory_pos
    cory "*whistle* Well ain't you done your research.."

    show mc happy at mc_pos
    mc "Mhm! won't make me not touch them though!"

    show cory unimpressed at cory_pos
    "Mr kind fish sighed."

    show cory netral at cory_pos
    cory "Point is just careful around yeah?"

    cory "And if you don't know your way to mystery fish."

    show cory netral_hu at cory_pos
    cory "Try exploring, ask around, riverfolks are one friendly neighborhood."

    show mc default at mc_pos
    mc "Okay! :D"

    show cory smile at cory_pos
    cory "Alright, good. Have fun, weird guppy! Best prayers to ya adventure"

    cory "..."

    show cory side at cory_pos
    cory "...."

    show cory sideclose at cory_pos
    cory "......."

    show cory unimpressed at cory_pos
    cory "Nay.. who am I kidding.. letting a 1 minute old guppy wander alone? That ain't me..."

    hide mc
    hide cory

    scene expression get_background()

    return


# =====================================
# BEACH HUB
# =====================================

label beach_hub:

    scene expression get_background()

    call screen beach_interaction

    # =================================
    # KLIK IKAN KIRI
    # =================================

    if _return == "fish_left":

        if is_day():
            call interact_with_npc("fish01")
            $ fish01_talked = True
        else:
            call interact_with_npc("fish03")
            $ fish03_talked = True

        jump beach_hub


    # =================================
    # KLIK IKAN KANAN
    # =================================

    elif _return == "fish_right":

        if is_day():
            call interact_with_npc("fish02")
            $ fish02_talked = True
        else:
            call interact_with_npc("fish04")
            $ fish04_talked = True

        jump beach_hub


    # =================================
    # KLIK BONGKAHAN EMAS (DAY)
    # =================================

    elif _return == "gold_nugget":

        if not gold_nugget_taken:
            $ add_item("gold_nugget")
            $ gold_nugget_taken = True

            scene expression get_dialogue_background()

            show mc default at mc_pos
            "After spending some time exploring the area, I stuffed the last item into my little bag."

            mc "..."

            mc "I think that's everything."

            show cory smile at cory_pos
            cory "find anything okay?"

            show mc happy at mc_pos
            mc "Oh! Hi Mr kind fish.. :D"

            show mc o at mc_pos
            "I peek through my bag"

            mc "Hmm..."

            mc "Not really."

            mc "...But I found lots of cool stuff!"

            "Mr kind fish also takes a peek at my inventory."

            cory "..."

            mc "...?"

            show cory unimpressed at cory_pos
            cory "Those are literally rocks."

            show mc excited at mc_pos
            mc "Cool rocks!"

            cory "... Half of that's traaa..."

            show mc o at mc_pos
            mc "traaa?...treasure?"

            cory "...Sure..."

            mc "ya! One of a kind treasure indeed mr kind fish :D"

            show cory proud_hu at cory_pos
            cory "also save the adjective would ya? call me cory the great now, guppy!"

            show mc happy at mc_pos
            mc "okay! Mr cory the great now guppy!"

            show cory unimpressed at cory_pos
            cory "ya know what? Cory's fine.."

            hide mc
            hide cory

            scene expression get_background()

        jump beach_hub


    # =================================
    # KLIK AMBALABU (NIGHT)
    # =================================

    elif _return == "ambalabu":

        if not ambalabu_taken:

            $ add_item("ambalabu")
            $ ambalabu_taken = True

            scene expression get_dialogue_background()

            "Item get: Ambalabu"

            show cory surprise at cory_pos
            show mc o at mc_pos

            cory "...!"

            cory "is that what i think it is??"

            mc "what is it mr cory?"

            show cory disrespectful at cory_pos

            cory "eh, just a toy.. A very popular one"

            show cory smile at cory_pos

            cory "I might know who might like this... hah!"

            hide mc
            hide cory

            scene expression get_background()

        jump beach_hub


    # =================================
    # LANJUT DAY → NIGHT
    # =================================

    elif _return == "continue_day":

        if day_objectives_complete():

            $ change_cycle()

            scene expression get_dialogue_background()

            "After spending some time exploring the riverbed, the warm light above us slowly began to fade."

            "The golden rays that once danced across the water became dimmer and dimmer."

            show mc o at mc_pos
            show cory side at cory_pos

            mc "..."

            mc "Mr. Cory?"

            mc "Its getting dark.. is it night already?"

            show cory side at cory_pos

            cory "Time flies when yer busy picking up rocks."

            show mc happy at mc_pos

            mc "Cool rocks!"

            show cory fond at cory_pos

            cory "they sure are."

            "The last traces of sunlight slowly disappeared behind the surface."

            "For a moment, the riverbed was bathed in a pretty faint blue glow."

            "Then... The world went dark."

            show mc o at mc_pos

            mc "..."

            "I looked around."

            "The river looked completely different."

            "The familiar rocks were now little more than silhouettes."

            "The plants swayed slowly in darkness, their shadows stretching across the riverbed."

            show mc shock at mc_pos

            mc "Whoa..."

            show cory netral at cory_pos

            cory "Don't wander too far."

            show cory netral_hu at cory_pos

            cory "Night's a little different around here."

            # insert cutscene glowing scale in dark

            "Then suddenly the golden scale in my palm starts to emit a soft blue glow. Giving a small light to those around me"

            show mc o at mc_pos
            show cory smile at cory_pos

            cory "well that's.. convenient!"

            cory "Though still,"

            cory "Keep your eyes open.. We dont know what might lurk in here"

            hide mc
            hide cory

            scene expression get_background()

            jump beach_hub

        else:

            jump beach_hub


    # =================================
    # LANJUT NIGHT → ENDING
    # =================================

    elif _return == "continue_night":

        if night_objectives_complete():

            return

        else:

            jump beach_hub


    # =================================
    # FALLBACK
    # =================================

    jump beach_hub


# =====================================
# NPC DIALOGUE LABELS
# =====================================

# -------------------------------------
# NPC 1: BIG MOUTH BASS (DAY - fish01)
# -------------------------------------

label dialogue_fish01:

    scene expression get_dialogue_background()

    show bass default at bass_pos
    "A bass drifted lazily with the current."

    "It looked like it had completely forgotten what it was doing."

    show mc default at mc_pos
    mc "Hi, Mr. Bass!"

    "The bass turns slightly toward me with a hum."

    bass "...Hm..?"

    show bass oh at bass_pos
    bass "Oh."

    show bass default at bass_pos
    bass "...Hi."

    bass "and it's.. Ms. bass"

    show mc o at mc_pos
    mc "Oh! Right, my apologies, ms bass!"

    menu:
        "I'm looking for a golden shiny diamond fish.":
            show mc o at mc_pos
            mc "I'm looking for a golden shiny diamond fish. Half the size of you!"

            mc "Have you seen one?"

            "bass stared blankly."

            show bass berpikir at bass_pos
            bass "...Golden..."

            bass "...Gold..."

            bass "..."

            bass "..."

            show bass oh at bass_pos
            bass "...Oh!"

            bass "The shiny one!"

            mc "Mhm!"

            bass "...Yeah."

            show bass default at bass_pos
            bass "I think it swam north."

            bass "...Maybe"

            bass "...Pretty sure."

            show bass berpikir at bass_pos
            bass "...Unless I'm remembering yesterday."

            hide bass
            show cory netral at cory_pos
            cory "yeah reaaaal useful information there pal"

            show mc happy at mc_pos
            mc "...Thank you Ms Bass!"

            hide cory
            show bass default at bass_pos
            bass "No problem..."

            "Ms bass immediately went back to staring into space."

            $ set_clue("The Golden fish was seen swimming north.")

        "Ms Bass can you sing us a song?":
            mc "Ms Bass can you sing us a song? :o"

            bass "sing..?"

            show mc default at mc_pos
            mc "yeah! Anything is fine.. maybe something about the river?"

            bass "....."

            bass "river..."

            show bass berpikir at bass_pos
            bass "to.. the river.."

            bass " river.. River..."

            show bass oh at bass_pos
            bass "take me to the river!"

            bass "twas my grandfather billy's prime time"

            bass "gotta put big mouth's name back in business huh...?"

            show bass default at bass_pos
            bass "thanks guppy"

            play sound "sfx/take_me_to_the_river.ogg"

            "Ms bass unlocked a core memory. Her nostalgic singing wafts through the river."

            hide bass
            show cory smile at cory_pos
            cory "now THAT'S cool retro."

            $ set_clue("The Golden fish was seen swimming north.")

    hide bass
    hide mc
    hide cory

    scene expression get_background()

    return


# -------------------------------------
# NPC 2: UCENG (DAY - fish02)
# -------------------------------------

label dialogue_fish02:

    scene expression get_dialogue_background()

    show uceng default at uceng_pos
    show mc o at mc_pos
    "Another fish was carefully arranging small stones into a neat circle."

    show mc default at mc_pos
    mc "Hello! Excuse me? Have you seen shiny shimmery golden fish around here?"

    show uceng annoyed at uceng_pos
    uceng "...Can't talk."

    uceng "I'm busy."

    menu:
        "Give rock item" if gold_nugget_taken:
            show mc happy at mc_pos
            mc "i found a really cool rock earlier! Might be useful for your artwork!"

            show uceng upset at uceng_pos
            uceng "GASP i-is.. Is that..?"

            uceng "THE ONE AND ONLY 24 KARAT ROCK RIVER?!"

            "The Uceng fish snatched the rock from my grip"

            hide uceng
            show cory unimpressed at cory_pos
            cory "the what now.."

            hide cory
            show uceng default at uceng_pos
            uceng "i'll tell you what, the golden fish you spot? It aint no ordinary fish.."

            uceng "rumor has it.. that fish can cure the incurable and make the impossible possible!"

            uceng "and this 24 karat rock river was believed to be one of its descendants!"

            hide uceng
            show cory unimpressed at cory_pos
            cory "looks like painted rock to me..."

            show mc o at mc_pos
            mc "cure the incurable...?"

            "mc will remember that"

            $ set_clue("The old current lies to the north")

        "The circle looks a little asymmetrical :o":
            show mc o at mc_pos
            hide cory
            show uceng upset at uceng_pos
            uceng "WHAT. DID. YOU. SAY?"

            uceng "you dare come here to mock, and disgrace art?!"

            uceng "how would a guppy like you know make a symmetrical circle with plain rocks?!"

            show mc default at mc_pos
            mc "here, let me help!"

            "I carefully arranged the rocks into a neat symmetrical circle"

            uceng "..."

            uceng "i..!"

            show uceng annoyed at uceng_pos
            uceng "hmph."

            $ set_clue("The old current lies to the north")

        "It actually looks pretty nice.":
            show mc default at mc_pos
            show uceng default at uceng_pos
            "Uceng grinned proudly."

            uceng "Heh."

            uceng "Knew someone would appreciate true art."

            uceng "So... you were looking for this golden fish?"

            uceng "...It passed by earlier."

            uceng "...Looked like it was heading toward the old current."

            mc "thank you Mr uceng fish!"

            uceng "No problem!"

            show uceng annoyed at uceng_pos
            uceng "...watch the rocks."

            $ set_clue("The old current lies to the north")

    hide uceng
    hide mc
    hide cory

    scene expression get_background()

    return


# -------------------------------------
# NPC 3: LELE (NIGHT - fish03)
# -------------------------------------

label dialogue_fish03:

    scene expression get_dialogue_background()

    show lele default at lele_pos
    "A catfish quietly watches from behind some seaweed."

    show mc default at mc_pos
    mc "I see you Mr catfish!"

    show lele curiga at lele_pos
    lele "..."

    show mc o at mc_pos
    "The catfish eyes me for a long second before going back into hiding. It appears to be somewhat shy?"

    show mc default at mc_pos
    "But as soon as Mr Cory swam forward its head peek in interest, like seeing an old friend"

    hide lele
    show cory smile at cory_pos
    cory "ay.. Good pal, catfish."

    hide cory
    show lele default at lele_pos
    lele "Here comes admin huh?"

    "mm maybe i should let mr cory ask instead?"

    call select_interactor

    if _return == "mc":

        show mc o at mc_pos
        mc "Do you know where the golden fish went?"

        show lele curiga at lele_pos
        lele "..."

        "It watches me with a very serious judging look."

        menu:
            "Give Ambalabu" if ambalabu_taken:
                show lele default at lele_pos
                "The catfish saw an opportunity and took the ambalabu from my hand."

                show mc shock at mc_pos
                mc "Ah! I was going to give it nicely.."

                lele "gokil"

                mc "gokil...?"

                show lele puratidur at lele_pos
                lele "super mega gokil"

                show mc o at mc_pos
                mc "super mega gokil... :o"

                show mc happy at mc_pos
                mc "gokil pro max!! :D"

                show lele curiga at lele_pos
                lele "The sacred golden fish wields power enough to dry out all the water on this planet."

                lele "Yet not many would dare to pursue until the finish line"

                lele "I believe only those who remain by then are the people worthy of its blessing"

                lele "Whether they shall bring the world prosper or agony."

                lele "Repeating Fate only awaits by the hand of our God"

                show lele depan at lele_pos
                lele "You should understand that better than anyone"

                show mc shock at mc_pos
                mc "woah.. That's a lot to take in.."

                show mc default at mc_pos
                mc "thank you mr catfish!"

                show lele default at lele_pos
                lele "mreow.. :3"

            "What does that mean?":
                show mc o at mc_pos
                show lele default at lele_pos
                lele "That's why you should read more information"

                mc "...Ooh, okay..."

                show mc default at mc_pos
                mc "We were looking for the golden fish!"

                show lele puratidur at lele_pos
                lele "Yes, yes, yes. I can see that."

                lele "The fish headed north."

                mc "North!"

                show lele curiga at lele_pos
                lele "But stay vigilant!"

                lele "You might need to light your ways."

            "How do I even say that...":
                show mc shock at mc_pos
                show lele curiga at lele_pos
                lele "..."

                lele "Suki..."

                mc "...?"

                lele "Suki's Member... Member of Suki!!!"

                lele "Gotta be alert..."

                lele "Go away."

                "The catfish scares us away."


    else:

        $ cory_at_right = True

        menu:
            "Which way is it pal?, i needa find out":
                hide mc
                hide lele
                show cory netral at cory_right_pos
                hide cory
                show lele default at lele_pos
                lele "North Kalimantan"

                hide lele
                show cory upset at cory_right_pos
                cory "is what a public liar woulda say!"

                show cory netral_hu at cory_right_pos
                cory "ay, spare me some real information would ya"

                hide cory
                show lele puratidur at lele_pos
                lele "i'll tell ya tomorrow"

                hide lele
                show cory netral_hu at cory_right_pos
                cory "Even with tempe goreng on the line?"

                hide cory
                show lele default at lele_pos
                lele "tempting."

                show lele puratidur at lele_pos
                lele "but nah."

                hide lele
                show cory upset at cory_right_pos
                cory "oh you watch your back"

                show cory smile_hu at cory_right_pos
                cory "what about iced tea?"

                hide cory
                show lele default at lele_pos
                lele "Appetizing.."

                hide lele
                show cory smile_hu at cory_right_pos
                cory "also with rice"

                cory "and spice"

                hide cory
                show lele puratidur at lele_pos
                lele "that's what i'm talking about!"

                hide lele
                show cory smile_hu at cory_right_pos
                cory "smart choice"

                hide cory
                show lele default at lele_pos
                lele "but i want 10 of each of them"

                hide lele
                show cory surprise at cory_right_pos
                cory "oh shrimp"

                cory "where's the logic behind that?!"

                show cory unimpressed at cory_right_pos
                cory "oh well what can i do,, we have a deal"

                hide cory
                show lele default at lele_pos
                lele "awesome"

                show lele puratidur at lele_pos
                lele "The fish headed north"

                hide lele
                show cory smile at cory_right_pos
                cory "Alhamdulillah"

            "Give Ambalabu" if ambalabu_taken:
                hide mc
                show cory smile at cory_right_pos
                hide cory
                show lele default at lele_pos
                lele "gokil"

                hide lele
                show cory disrespectful at cory_right_pos
                cory "super gokil"

                hide cory
                show lele puratidur at lele_pos
                lele "super mega gokil"

                hide lele
                show cory smile at cory_right_pos
                cory "super mega gokil pro max"

                hide cory
                show lele default at lele_pos
                lele "The sacred golden fish wields power enough to dry out all the water on this planet."

                lele "Yet not many would dare to pursue until the finish line"

                lele "I believe only those who remain by then are the people worthy of its blessing"

                lele "Whether they shall bring the world prosper or agony."

                lele "Repeating Fate only awaits by the hand of our God"

                show lele depan at lele_pos
                lele "You should understand that better than anyone"

                hide lele
                show cory netral at cory_right_pos
                cory "what does that even mean..."

    $ cory_at_right = False
    $ set_clue("All clues point toward the northern current.")

    hide lele
    hide mc
    hide cory

    scene expression get_background()

    return


# -------------------------------------
# NPC 4: ALLIGATOR (NIGHT - fish04)
# -------------------------------------

label dialogue_fish04:

    scene expression get_dialogue_background()

    show gator default at gator_pos
    "An alligator lounging beside a large rock. It looked completely unbothered by anything that would be around it. One of its claws casually tapped against the rock."

    show mc default at mc_pos
    mc "Hello! Good evening!"

    "The alligator slowly turned its head toward me."

    gator "Huh?"

    gator "Oh."

    show gator annoyed at gator_pos
    gator "A guppy."

    show mc happy at mc_pos
    mc "anyway ms gator I'm looking for a golden fish!"

    show gator surprised at gator_pos
    gator "wait ya can tell I'm a gator?"

    gator "Even down to the fact that I'm no male. Impressive."

    show gator annoyed at gator_pos
    gator "Most thought that I'm a.. ugh, a croс."

    show mc o at mc_pos
    mc "mm it's pretty easy to tell an alligator and a crocodile apart.."

    mc "alligators have a U shaped snout while crocodiles have it V shaped!"

    mc "also alligators only have their upper teeth visible when the jaw is closed, while crocodiles have them both shown!"

    mc "as to how to tell the sex apart, it's the size and how slim you are"

    show gator smile at gator_pos
    gator "*whistle* I like this guppy."

    gator "you were saying golden fish?"

    show mc default at mc_pos
    mc "Mhm! Suuuper shiny!"

    show gator default at gator_pos
    gator "Oh, THAT pretty thing."

    show mc o at mc_pos
    mc "You know it!??"

    show gator surprised at gator_pos
    gator "Know it?"

    gator "Kid, half the river's been staring at the swimming gem."

    gator "Thing practically lights up the whole river."

    show gator default at gator_pos
    gator "I saw it zoom past me earlier."

    mc "Which direction did it go?"

    gator "mm.. pretty sure North..."

    show mc happy at mc_pos
    mc "All leads road to north!"

    hide gator
    show cory side at cory_pos
    cory "ay.. i think ya got it mixed up there guppy"

    hide cory
    show gator default at gator_pos
    gator "shut up. They can think on their own"

    show gator smile at gator_pos
    gator "Right, guppy?"

    hide gator
    show cory upset at cory_pos
    cory "what did ya get so defensive for!"

    hide cory
    show gator default at gator_pos
    gator "just teaching you on how to babysit."

    hide gator
    show cory upset at cory_pos
    cory "who's saying what about babysitting?! I'm just accompanying the little thing!"

    hide cory
    show gator annoyed at gator_pos
    gator "you just defined babysitting."

    hide gator
    show cory upset at cory_pos
    cory "since when did you care so much for a guppy anyway?"

    cory "You always eat them for lunch, especially on Tuesdays."

    show mc o at mc_pos
    mc "mm, it is Tuesday today..."

    hide cory
    show gator annoyed at gator_pos
    gator "I could say the same to ya. Last time I seen you with a guppy it was when you were-"

    hide gator
    show cory disrespectful at cory_pos
    cory "LA LA LA CANT HEAR YA OVER THESE THIIICK FINS O' MINE"

    hide cory
    show gator upset at gator_pos
    gator "OH YOU SHUT YOUR MOUTH BOY I CAN EAT YOU RIGHT ABOUT NOW."

    gator "YOUR FOUL TASTE IS THE ONLY THING STOPPING ME."

    "I stare at both of them from the sidelines. Feeling a stiff electric tension swells between them as it goes on. It was like watching mama and papa speak to each other. Maybe I should try stopping them.."

    menu:
        "Don't stop them":
            show mc shock at mc_pos
            "I continue to stare as they exhaust themselves"

            show gator upset at gator_pos
            gator "you.. Motherfucker"

            show mc o at mc_pos
            mc "...!"

            hide gator
            show cory upset at cory_pos
            cory "nasty NASTY gator..!"

            show mc o at mc_pos
            mc " what does a motherfucker mean? :o my parents said that thing a lot too.."

            show mc shock at mc_pos
            cory ".."

            hide cory
            show gator surprised at gator_pos
            gator "......."

            hide gator
            show cory side at cory_pos
            cory "it means uhh-!"

            show cory smile_hu at cory_pos
            cory "Means that you love your mother a lot!"

            show mc happy at mc_pos
            mc "ohh I love my mama! so I'm a motherfucker too! :D"

            hide cory
            show gator annoyed at gator_pos
            gator ".... No! Motherfucker means you HATE your mother, guppy."

            gator "don't listen to that fish"

            show mc shock at mc_pos
            mc "ohh.. okay I'm not a motherfucker then :("

            hide gator
            show cory netral at cory_pos
            cory "ya know what truce on that."

            hide cory
            show gator default at gator_pos
            gator "Anyway."

            gator "You better run now"

            gator "Everyone's chasing it."

            show mc o at mc_pos
            mc "Everyone?"

            gator "Mhm, all creatures on water. Perhaps on land too like you are."

            gator "Pretty thing like that doesn't stay a secret for long"

            gator "And once the whole water starts wanting the same thing..."

            show gator annoyed at gator_pos
            gator "Things get messy."

            show mc default at mc_pos
            mc "I'll be careful!"

            show gator smile at gator_pos
            gator "Good, I'd hate to hear some little guppy got swept away."

            hide gator
            show cory netral_hu at cory_pos
            cory "Don't worry gatha."

            cory "I've got an eye on him."

            hide cory
            show gator annoyed at gator_pos
            gator "I don't trust you, you're bad at babysitting"

            hide gator
            show cory upset at cory_pos
            cory "no I'm not!"

            show mc happy at mc_pos
            mc "but Mr Cory is kind to me! I trust him!"

            hide cory
            show gator smile at gator_pos
            gator "Ha!"

            gator "Go on then, little guppy."

            gator "Chase your shiny thing."

            gator "Just don't let the river chase you back."

            gator "and if you got lost in the way?"

            gator "punch Cory in the face, I'll come running"

            hide gator
            show cory surprise at cory_pos
            cory "ay!"

            show mc default at mc_pos
            mc "Okay! Thank you!"

        "Distract them":
            show mc shock at mc_pos
            mc "i uhm.. Ms.. gator why did you not follow the golden fish when it's so shiny?"

            hide mc
            hide cory
            show gator surprised at gator_pos
            show cory surprise at cory_pos
            "At the sound of my voice they both turn to me with a realizing look on their face. Distancing from one another with a firm ehem."

            hide cory
            show gator default at gator_pos
            gator "Because it was fast."

            show mc o at mc_pos
            mc "Oh! :o"

            hide gator
            show cory disrespectful at cory_pos
            cory ".... Heh"

            hide cory
            show gator default at gator_pos
            gator "..."

            show gator annoyed at gator_pos
            gator "Don't give me that look."

            show mc o at mc_pos
            mc "What look?"

            gator "The look."

            gator "The 'wow, the big scary alligator is lost to a fish' look."

            show mc shock at mc_pos
            mc "I wasn't at all thinking that!"

            hide gator
            show cory smile at cory_pos
            cory "I was sure as eel thinking that"

            hide cory
            show gator default at gator_pos
            gator "I definitely could've caught it if I wanted."

            hide gator
            show cory smile_hu at cory_pos
            cory "Ya sure could."

            hide cory
            show gator annoyed at gator_pos
            gator "I COULD."

            hide gator
            show cory disrespectful at cory_pos
            cory "mhm"

            hide cory
            show gator upset at gator_pos
            gator "oh I CAN."

            hide gator
            show cory disrespectful at cory_pos
            cory "whatever you say guppy."

            show mc shock at mc_pos
            "I heard a loud snap from miss Gator's direction"

            hide cory
            show gator annoyed at gator_pos
            gator "Oh fine you wanna go, punk?"

            gator "I'm getting to that fish first.."

            show gator upset at gator_pos
            gator "and eat im going to eat it right on your face"

            show gator smile at gator_pos
            gator "See how you'll like that"

            "With a face of determination and disdain Ms gator left in a hurry. The current swirling in her wake."

            show mc shock at mc_pos
            hide gator
            show cory side at cory_pos
            mc "...."

            mc "Mr.. Cory.. alligators can actually swim up to thirty kilometers per hour"

            mc "which is.. faster than both of us combined.."

            show cory surprise at cory_pos
            cory "they can WHAT."

            cory "sweet mother of kraken.."

            cory "WE SPRINTING GUPPY COME ON!"

            hide cory
            show gator smile at gator_pos
            gator "Besides I had better things to do."

            mc "Like what?"

            gator "..."

            "The alligator glanced at the rock next to it."

            gator "Guarding this rock."

            mc "..."

            hide gator
            show cory surprise at cory_pos
            cory "..."

            hide cory
            show gator smile at gator_pos
            gator "It's important."

            mc "What's so special about it."

            gator "It's a rock."

            mc "Oh!"

            mc "I like rocks!"

            gator "..."

            gator "You're alright, kid."

            mc "Hehe!"

    $ set_clue("All clues point toward the northern current.")

    hide gator
    hide mc
    hide cory

    scene expression get_background()

    return


# =====================================
# CHAPTER 1 ENDING
# =====================================

label chapter1_ending:

    scene expression get_dialogue_background()

    "A tiny peek of sunlight cuts through the riverwater. Tainting the murkish dark water in small dots of light that slowly stretches its reach. Soon enough the river is glowing in a calming blue"

    show mc o at mc_pos
    mc "woah.. dawn in the river.."

    show mc excited at mc_pos
    mc "so this is what a fish sees.."

    show cory smile at cory_pos
    cory "Mhm, not so scary anymore is it?"

    show cory netral_hu at cory_pos
    cory "And? What've we got?"

    show mc default at mc_pos
    mc "North!"

    show mc happy at mc_pos
    mc "They all said north!"

    show cory side at cory_pos
    cory "north eh? The direction where the river ends.."

    show cory smile at cory_pos
    cory "... Guess we've got our answer."

    "I looked toward the distant current. The water there flowed faster. The sunlight barely reached it."

    show cory netral at cory_pos
    cory "but uhh guppy.. ain't your parents worried..?"

    cory "it's been a full day since we got here.. ya don't wanna go back for a bit?"

    show mc o at mc_pos
    mc "mm? No it's fine! My parents allow me to come back home whenever I want!"

    show mc default at mc_pos
    mc "I don't think I'm coming back before I see that fish again.."

    mc "aren't they just the kindest? To give freewill at my age!"

    show cory side at cory_pos
    cory "free will ay..? Sounds worrying to me."

    cory "but you're right about one thing, guppy"

    cory "we ain't going back until we catch that damn fish together!"

    show mc happy at mc_pos
    mc "Let's go!"

    show cory fond at cory_pos
    cory "Just don’t make me save ya twice."

    "We begin swimming toward the northern stream. As we disappeared into the rushing water..."

    "Fade Out."

    hide mc
    hide cory

    jump chapter2