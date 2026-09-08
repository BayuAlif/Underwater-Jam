# =========================================================
# CHAPTER 3 - THE OPEN SEA
# =========================================================

label chapter3:

    # =================================
    # DAY SETUP
    # =================================

    $ set_cycle("day")
    $ load_area("sea")

    $ set_background(
        "images/backgrounds/chapter 3/bg day3.jpg",
        "images/backgrounds/chapter 2/bg night2.jpg"
    )

    $ set_dialogue_background(
        "images/backgrounds/chapter 3/bg day3_bordered.jpg",
        "images/backgrounds/chapter 2/bg night2_bordered.jpg"
    )

    scene expression get_background()

    call chapter3_opening

    jump chapter3_hub


# =========================================================
# CHAPTER 3 OPENING
# =========================================================

label chapter3_opening:

    scene expression get_dialogue_background()

    "===== CHAPTER 3 ====="

    "The sea fills my line of sight with overwhelmingly bright pretty colors. My gaze erratically jumps from one color to another as we continue to swim further."

    "From parrot fishes, sparkly elvis worms to rainbow open brain corals. There’s way too many stuff to focus on!"

    show cory smile_hu at cory_pos

    cory "heh.. Yer eyes been flying everywhere since we got here."
    cory "Don’t ya get dizzy?"

    show mc excited at mc_pos

    mc "ohmigosh!! Is that coral dancing?! Did you see that, Mr Cory?! I think that’s the Spanish dancer!"

    show cory fond at cory_pos

    cory "So excited, can’t even hear me huh.."

    show cory smile_hu at cory_pos

    cory "Though I must admit that this is some otherworldly beaut going on."

    show scy proud at shrimp_right_pos

    scy "Right?! Feast your eyes upon the neverending beauty that is sea!"

    show cory side at cory_pos

    cory "To think your empress’ been gatekeepin all this.. kinda messed up to think about."

    show scy sepet at shrimp_right_pos

    scy "But she’s not entirely wrong either! Most fish criminals are freshwater types!"

    show cory sideclose at cory_pos

    cory "Ay.. Sure, being careful is one thing.."
    cory "But pushing that stereotype into every freshwater is a whole different thing."

    show scy defaultom at shrimp_right_pos

    scy "Mm.. well! It’s the daughter that just got promoted into empress!"
    scy "The former queen that saved my life had dethroned herself not long ago."
    scy "So she’s still trying out new rules that feel fitting!"

    show cory ohiounimpressed1 at cory_pos

    cory "New ruler’s a kid? That checks out.."

    show cory netral at cory_pos

    cory "About time somefish teaches em a lesson then."

    show scy surprise at shrimp_right_pos

    scy "....!"
    scy "Wait! Why are you crying comrade?!"

    show cory surprise at cory_pos

    cory "Huh? I ain’t crying! Are you guppy?"

    show mc shock at mc_pos

    mc "Me? Why would I be?"

    show scy surprise at shrimp_right_pos

    scy "But I feel the vibration of someone crying!"

    "???" "nngueeeh.."

    show cory surprise at cory_pos

    cory "Wait, I hear it too..!"

    show scy defaultom at shrimp_right_pos

    scy "What if it’s another one of golden fish’s unfortunate victims?!"

    show mc o at mc_pos

    mc "oh no! We have to find them!"

    show cory side at cory_pos

    cory "Everybody’s been gloomy lately huh."

    hide mc
    hide cory
    hide scy

    scene expression get_background()

    return


# =========================================================
# CHAPTER 3 HUB
# DAY + NIGHT
# =========================================================

label chapter3_hub:

    scene expression get_background()

    call screen chapter3_interaction

    $ hub_choice = _return

    # =====================================================
    # DAY - SEA BUNNY
    # =====================================================

    if hub_choice == "seabunny":

        call interact_with_npc("seabunny")

        jump chapter3_hub

    # =====================================================
    # DAY - SEA TURTLE (GRAN HAWK)
    # =====================================================

    elif hub_choice == "seaturtle":

        call interact_with_npc("seaturtle")

        jump chapter3_hub

    # =====================================================
    # DAY - RAINBOW ALGAE
    # =====================================================

    elif hub_choice == "rainbow_algae":

        if not rainbow_algae_taken:

            call chapter3_rainbow_algae_pickup

        jump chapter3_hub

    # =====================================================
    # DAY -> NIGHT
    # =====================================================

    elif hub_choice == "continue_chapter3_day":

        $ change_cycle()

        scene expression get_dialogue_background()

        "The bright tropical colors of the sea deepen into a shadowy indigo as night falls across the reefs."

        show mc o at mc_pos
        show cory side at cory_pos

        mc "The corals look so different in the dark..."

        show scy default at shrimp_right_pos

        scy "Stay alert, comrades! The crustacean patrols grow far more aggressive once the sun sets!"

        show cory netral at cory_pos

        cory "Keep yer fins steady, guppy. We're getting closer to that empress."

        hide mc
        hide cory
        hide scy

        scene expression get_background()

        jump chapter3_hub

    jump chapter3_hub


# =========================================================
# RAINBOW ALGAE PICKUP
# =========================================================

label chapter3_rainbow_algae_pickup:

    $ add_item("rainbow_algae")
    $ rainbow_algae_taken = True

    scene expression get_dialogue_background()

    show mc excited at mc_pos
    show cory netral_hu at cory_pos

    mc "woah! Rainbow algaes!"

    show cory netral_hu at cory_pos

    cory "Wait guppy, are those safe? Colors suggest me not.."

    show scy laugh at shrimp_right_pos

    scy "Don’t fret my friend! These are harmless!"

    show mc happy at mc_pos

    mc "yipee I’ll take some with us then!"

    show scy defaultom at shrimp_right_pos

    scy "Do take a considerable amount!"
    scy "I will not tolerate algae hoarding!"

    show mc default at mc_pos

    mc "yes yes I know!"

    show mc o at mc_pos

    mc "Can i taaaake.. Mm 30?"

    show scy surprise at shrimp_right_pos

    scy "Absolutely not! That’s more than the crown allows!"

    show scy defaultom at shrimp_right_pos

    scy "You can only take no more than 5lbs!"

    show mc pout at mc_pos

    mc "But I seen fishermen take a huuuuuge big bucket of algaes and not get yelled at!"
    mc "30 is far from filling a huge big bucket!"

    show scy defaultom at shrimp_right_pos

    scy "No! Here in sea, we have strict rules over what we take."
    scy "Especially now! The waters have been thinning for moons now…"

    show scy sepet at shrimp_right_pos

    scy "Algae, fish, even the coral's gone quiet!"

    show mc shock at mc_pos

    mc "Wait, so… it's actually bad right now?"

    show scy defaultom at shrimp_right_pos

    scy "Bad enough that the crown had to cut the limit twice this season alone!"
    scy "So no. Not 30. Not even close, guppy!"

    show mc pout at mc_pos

    mc "mmn okay I understand…"

    show mc o at mc_pos

    mc "mr cory whats 5 lbs in kilograms..?"

    show cory side at cory_pos

    cory "I uhh.."

    show cory sideclose at cory_pos

    cory "ay let’s just take 2 and go guppy."

    "I obtained: Rainbow Algae"

    hide mc
    hide cory
    hide scy

    scene expression get_background()

    return
