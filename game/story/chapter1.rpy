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

    "===== CHAPTER 1 ====="

    "An unknown brazen voice pulled me out of a trance as my gaze dropped down to be unexpectedly met with a bottomless pit right before my toes, flinching back in instinct."

    # Saat dialog karakter dimulai, beralih ke background bordered
    scene expression get_dialogue_background()

    show cory talk at cory_pos
    show mc shock at mc_pos

    mc "...!"

    show cory talk at cory_pos

    cory "You take one more step..."

    cory "...And you'd be a goner."

    "The image of the darkness beyond is burned crisp into my mind. The current below twisted slowly as if alive, taunting those who stare long enough."

    show cory side at cory_pos

    cory "Not exactly the kinda place ya wanna stumble into.."

    "I slowly nodded in agreement. Before my mind could curiously wonder more to the depth of said cliff, I looked up to the source of voice."

    "What I expected was a kind mr human. I was instead met with a fish! A Corydoras perhaps? My eyes lit up with unbridled enthusiasm."

    show mc excited at mc_pos

    "Excitement held out, I mustn't forget to express my gratitude to those who saved my life. I start to wiggle my body in an interpretative dance of gratitude."

    show cory unimpressed at cory_pos

    cory "..."

    show cory disrespectful at cory_pos

    cory "Mane just what the fugu is you doing..?!"

    show mc pout at mc_pos

    mc "Fishes communicate through gestures and and visual as well as colors I'm trying to express my gratitude through-"

    show mc shock at mc_pos

    mc "Wait.. I just spoke in water…"

    show mc excited at mc_pos

    mc "ARE YOU GETTING ME, MR FISH?? :D"

    show cory sideclose at cory_pos

    cory "chill the carp out! Yes and yes I'm understanding all the word you saying"

    show mc excited at mc_pos

    mc "I'M HAVING A CONVERSATION WITH A FISH!!"

    "Struck with a thunder of explosive excitement a loud squeak pushed through me. At the same time my mouth is wide open-"

    show mc dizzy at mc_pos

    mc "{i}COUGHCOUCHCOUGHBLURURHRGHUGUHRH-!{/i}"

    show cory surprise at cory_pos

    cory "Holy SHRIMP you still need air huh? I think I have just what ya need"

    # cutscene: cory putting a fishbowl on mc's head

    show mc excited at mc_pos
    show cory smile at cory_pos

    mc "Huh-? Whoaaah.. I can see better now!"

    show cory proud at cory_pos

    cory "You sure do!"

    show cory talk at cory_pos

    cory "But.. huh is that a first.. alien guppy of two legs speaks under water.. you a witch?"

    show mc happy at mc_pos

    mc "Am no witch! Am fish! It's my ever dream!"

    show mc actual at mc_pos

    mc "Ah but I couldn't do any of this before... maybe it's because of.."

    "My gaze fell down to the translucent scale I didn't realize was clutched tight in my palm the entire time. Curious, I let go of it just for one millisecond."

    "True to my hypothesis, in that frozen moment everything went silent. Save for the tranquil current whirring in my ears."

    "But as soon as I made contact with the magical scale. It all became lively. Voices, distant and nearby, fill in the atmosphere. It's like shopping at a market on a sunny sunday!"

    "Mr kind fish's voice became audible again too.."

    show cory talk at cory_pos

    cory "--- –in't ya one step closer to a dream come true, little guppy?"

    "This is the power of only one scale. Imagine what a whole fish can do…"

    show mc actual at mc_pos

    mc "Mr kind fish did you see a shiny golden fish that passed by?"

    show cory fond at cory_pos

    cory "Golden fish? I ain't see no gold, what I saw was straight DIAMOND."

    cory "Visceral beauty struck me tantalized. type shrimp."

    show cory side at cory_pos

    cory "Didn't bother following it though. That and ion remember where it went."

    show mc shock at mc_pos

    mc "Whuh? Why? :o"

    show cory talk at cory_pos

    cory "Ay.. how should I be telling you this.. Pretty things usually mean trouble around here."

    show mc pout at mc_pos

    cory "And I might just be too out of their league."

    show mc excited at mc_pos

    mc "Yeah! I know! Like blue dragons and and lionfish and"

    show cory smile at cory_pos

    cory "*whistle* Well ain't you done your research.."

    show mc pout at mc_pos

    mc "Mhm! won't make me not touch them though!"

    "Mr kind fish sighed."

    show cory talk at cory_pos

    cory "Point is just careful around yeah?"

    cory "And if you don't know your way to mystery fish."

    cory "Try exploring, ask around, riverfolks are one friendly neighborhood."

    show mc excited at mc_pos

    mc "Okay! :D"

    show cory smile at cory_pos

    cory "Alright, good. Have fun, weird guppy! Best prayers to ya adventure"

    hide mc
    hide cory

    scene expression get_background()

    return


# =====================================
# BEACH HUB
# =====================================

label beach_hub:

    # Selalu pastikan saat eksplorasi / klik ikan / item, background adalah Full sesuai cycle (Siang/Malam)
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

            "She kept a small gold lump."

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

            cory "I might know who might like this… hah!"

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

            show cory talk at cory_pos

            cory "Time flies when yer busy picking up rocks."

            show mc happy at mc_pos

            mc "Cool rocks!"

            show cory fond at cory_pos

            cory "they sure are."

            "The last traces of sunlight slowly disappeared behind the surface."

            "For a moment, the riverbed was bathed in a pretty faint blue glow."

            "Then… The world went dark."

            show mc o at mc_pos

            mc "..."

            "I looked around."

            "The river looked completely different."

            "The familiar rocks were now little more than silhouettes."

            "The plants swayed slowly in darkness, their shadows stretching across the riverbed."

            show mc shock at mc_pos

            mc "Whoa…"

            show cory talk at cory_pos

            cory "Don’t wander too far."

            show cory netral_hu at cory_pos

            cory "Night’s a little different around here."

            # insert cutscene glowing scale in dark

            "Then suddenly the golden scale in my palm starts to emit a soft blue glow. Giving a small light to those around me"

            show mc o at mc_pos
            show cory smile at cory_pos

            mc "well that's.. convenient!"

            cory "Though still,"

            mc "Keep your eyes open.. We dont know what might lurk in here"

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
# CHAPTER 1 ENDING
# =====================================

label chapter1_ending:

    scene expression get_dialogue_background()

    "A tiny peek of sunlight cuts through the riverwater. Tainting the murkish dark water in small dots of light that slowly stretches its reach. Soon enough the river is glowing in a calming blue"

    show mc o at mc_pos
    show cory netral at cory_pos

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

    cory "...Guess we've got our answer."

    "I looked toward the distant current. The water there flowed faster. The sunlight barely reached it."

    show cory talk at cory_pos

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

    "We begin swimming toward the northern stream. As we disappeared into the rushing water…"

    "Fade Out."

    hide mc
    hide cory

    jump chapter2