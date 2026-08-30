# =====================================
# CHAPTER 1
# =====================================

label chapter1:

    # =================================
    # DAY SETUP
    # =================================

    $ set_cycle("day")
    $ load_area("beach")

    # Override background khusus Chapter 1.
    # Tidak mengganggu Prologue.
    $ set_background(
        "images/backgrounds/chapter1/chapter1_beach_day.png",
        "images/backgrounds/chapter1/chapter1_beach_day.png"
    )

    scene expression get_background()

    call chapter1_opening

    call beach_hub

    jump chapter1_ending


# =====================================
# CHAPTER 1 OPENING
# =====================================

label chapter1_opening:

    scene expression get_background()

    show f1 default at mc_pos

    f1 "===== CHAPTER 1 ====="

    "An unknown brazen voice pulled me out of a trance as my gaze dropped down to be unexpectedly met with a bottomless pit right before my toes, flinching back in instinct."

    show f1 shock at mc_pos

    f1 "...!"

    f1 "You take one more step..."

    f1 "...And you'd be a goner."

    "The image of the darkness beyond is burned crisp into my mind. The current below twisted slowly as if alive, taunting those who stare long enough."

    show f1 default at mc_pos

    f1 "Not exactly the kinda place ya wanna stumble into.."

    "I slowly nodded in agreement. Before my mind could curiously wonder more to the depth of said cliff, I looked up to the source of voice."

    "What I expected was a kind mr human. I was instead met with a fish! A Corydoras perhaps? My eyes lit up with unbridled enthusiasm."

    show f1 excited at mc_pos

    "Excitement held out, I mustn't forget to express my gratitude to those who saved my life. I start to wiggle my body in an interpretative dance of gratitude."

    f1 "..."

    show f1 actual at mc_pos

    f1 "Mane just what the fugu is you doing..?!"

    show f1 pout at mc_pos

    f1 "Fishes communicate through gestures and and visual as well as colors I'm trying to express my gratitude through-"

    show f1 shock at mc_pos

    f1 "Wait.. I just spoke in water…"

    show f1 excited at mc_pos

    f1 "ARE YOU GETTING ME, MR FISH?? :D"

    show f1 default at mc_pos

    f1 "chill the carp out! Yes and yes I'm understanding all the word you saying"

    show f1 excited at mc_pos

    f1 "I'M HAVING A CONVERSATION WITH A FISH!!"

    "Struck with a thunder of explosive excitement a loud squeak pushed through me. At the same time my mouth is wide open-"

    show f1 dizzy at mc_pos

    f1 "{i}COUGHCOUCHCOUGHBLURURHRGHUGUHRH-!{/i}"

    show f1 default at mc_pos

    f1 "Holy SHRIMP you still need air huh? I think I have just what ya need"

    # cutscene: cory putting a fishbowl on mc's head

    show f1 excited at mc_pos

    f1 "Huh-? Whoaaah.. I can see better now!"

    show f1 happy at mc_pos

    f1 "You sure do!"

    show f1 actual at mc_pos

    f1 "But.. huh is that a first.. alien guppy of two legs speaks under water.. you a witch?"

    show f1 happy at mc_pos

    f1 "Am no witch! Am fish! It's my ever dream!"

    show f1 actual at mc_pos

    f1 "Ah but I couldn't do any of this before... maybe it's because of.."

    "My gaze fell down to the translucent scale I didn't realize was clutched tight in my palm the entire time. Curious, I let go of it just for one millisecond."

    "True to my hypothesis, in that frozen moment everything went silent. Save for the tranquil current whirring in my ears."

    "But as soon as I made contact with the magical scale. It all became lively. Voices, distant and nearby, fill in the atmosphere. It's like shopping at a market on a sunny sunday!"

    "Mr kind fish's voice became audible again too.."

    show f1 default at mc_pos

    f1 "--- –in't ya one step closer to a dream come true, little guppy?"

    "This is the power of only one scale. Imagine what a whole fish can do…"

    show f1 actual at mc_pos

    f1 "Mr kind fish did you see a shiny golden fish that passed by?"

    show f1 shock at mc_pos

    f1 "Golden fish? I ain't see no gold, what I saw was straight DIAMOND."

    show f1 happy at mc_pos

    f1 "Visceral beauty struck me tantalized. type shrimp."

    show f1 default at mc_pos

    f1 "Didn't bother following it though. That and ion remember where it went."

    show f1 shock at mc_pos

    f1 "Whuh? Why? :o"

    show f1 actual at mc_pos

    f1 "Ay.. how should I be telling you this.. Pretty things usually mean trouble around here."

    show f1 pout at mc_pos

    f1 "And I might just be too out of their league."

    show f1 excited at mc_pos

    f1 "Yeah! I know! Like blue dragons and and lionfish and"

    show f1 default at mc_pos

    f1 "*whistle* Well ain't you done your research.."

    show f1 pout at mc_pos

    f1 "Mhm! won't make me not touch them though!"

    "Mr kind fish sighed."

    show f1 default at mc_pos

    f1 "Point is just careful around yeah?"

    f1 "And if you don't know your way to mystery fish."

    f1 "Try exploring, ask around, riverfolks are one friendly neighborhood."

    show f1 excited at mc_pos

    f1 "Okay! :D"

    show f1 happy at mc_pos

    f1 "Alright, good. Have fun, weird guppy! Best prayers to ya adventure"

    show f1 pout at mc_pos

    f1 "Nay.. who am I kidding.. letting a 1 minute old guppy wander alone? That ain't me…"

    hide f1

    return


# =====================================
# BEACH HUB
# =====================================

label beach_hub:

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
    # KLIK BONGKAHAN EMAS
    # =================================

    elif _return == "gold_nugget":

        if not gold_nugget_taken:

            $ add_item("gold_nugget")
            $ gold_nugget_taken = True

            "Kamu mengambil bongkahan emas."

        jump beach_hub


    # =================================
    # LANJUT DAY → NIGHT
    # =================================

    elif _return == "continue_day":

        if day_objectives_complete():

            $ change_cycle()

            # Saat cycle berubah, pakai BG Night.
            $ set_background(
                "images/backgrounds/chapter1/chapter1_beach_day.png",
                "images/backgrounds/chapter1/chapter1_beach_day.png"
            )

            scene expression get_background()

            show f1 actual at mc_pos

            f1 "..."

            f1 "Mr. Cory?"

            show f1 default at mc_pos

            f1 "Its getting dark.. is it night already?"

            f1 "Time flies when yer busy picking up rocks."

            f1 "Cool rocks!"

            f1 "they sure are."

            "The last traces of sunlight slowly disappeared behind the surface. For a moment, the riverbed was bathed in a pretty faint blue glow. Then… the world went dark."

            show f1 actual at mc_pos

            f1 "..."

            "I looked around. The river looked completely different. The familiar rocks were now little more than silhouettes."

            show f1 shock at mc_pos

            f1 "Whoa…"

            show f1 default at mc_pos

            f1 "Don't wander too far."

            f1 "Night's a little different around here."

            # insert cutscene: glowing scale in dark

            "Then suddenly the golden scale in my palm starts to emit a soft blue glow, giving a small light to those around me."

            show f1 happy at mc_pos

            f1 "well that's.. convenient!"

            show f1 default at mc_pos

            f1 "Though still,"

            f1 "Keep your eyes open.. We dont know what might lurk in here"

            $ add_item("ambalabu")

            "Item get: Ambalabu"

            show f1 shock at mc_pos

            f1 "...!"

            show f1 excited at mc_pos

            f1 "is that what i think it is??"

            show f1 actual at mc_pos

            f1 "what is it mr cory?"

            show f1 default at mc_pos

            f1 "eh, just a toy.. A very popular one"

            show f1 happy at mc_pos

            f1 "I might know who might like this… hah!"

            hide f1

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

    scene expression get_background()

    "A tiny peek of sunlight cuts through the riverwater, tainting the murkish dark water in small dots of light that slowly stretches its reach. Soon enough the river is glowing in a calming blue."

    show f1 shock at mc_pos

    f1 "woah.. dawn in the river.."

    show f1 default at mc_pos

    f1 "so this is what a fish sees.."

    f1 "Mhm, not so scary anymore is it?"

    f1 "And? What've we got?"

    show f1 excited at mc_pos

    f1 "North!"

    f1 "They all said north!"

    show f1 actual at mc_pos

    f1 "north eh? The direction where the river ends.."

    show f1 default at mc_pos

    f1 "...Guess we've got our answer."

    "I looked toward the distant current. The water there flowed faster. The sunlight barely reached it."

    show f1 actual at mc_pos

    f1 "but uhh guppy.. ain't your parents worried..?"

    f1 "it's been a full day since we got here.. ya don't wanna go back for a bit?"

    show f1 happy at mc_pos

    f1 "mm? No it's fine! My parents allow me to come back home whenever I want!"

    show f1 default at mc_pos

    f1 "I don't think I'm coming back before I see that fish again.."

    show f1 happy at mc_pos

    f1 "aren't they just the kindest? To give freewill at my age!"

    show f1 actual at mc_pos

    f1 "free will ay..? Sounds worrying to me."

    show f1 default at mc_pos

    f1 "but you're right about one thing, guppy"

    show f1 excited at mc_pos

    f1 "we ain't going back until we catch that damn fish together!"

    f1 "Let's go!"

    show f1 happy at mc_pos

    f1 "Just don't make me save ya twice."

    "We begin swimming toward the northern stream. As we disappeared into the rushing water… fade out."

    hide f1

    jump chapter2