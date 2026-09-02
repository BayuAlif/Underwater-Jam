# =========================================================
# CHAPTER 2
# =========================================================

label chapter2:

    # =================================
    # DAY SETUP
    # =================================

    $ set_cycle("day")
    $ load_area("border")

    $ set_background(
        "images/backgrounds/chapter 2/bg day2.jpg",
        "images/backgrounds/chapter 2/bg day2.jpg"
    )
    $ set_dialogue_background(
        "images/backgrounds/chapter 2/bg day2_bordered.jpg",
        "images/backgrounds/chapter 2/bg day2_bordered.jpg"
    )

    scene expression get_background()

    call chapter2_opening

    call chapter2_hub

    return


# =========================================================
# CHAPTER 2 OPENING
# =========================================================

label chapter2_opening:

    scene expression get_dialogue_background()

    "===== CHAPTER 2 ====="

    "The river flowed faster, slowly giving way to larger stones."

    "The sunlight above grew softer, hiding themself behind layers of drifting water plants."

    show cory talk at cory_pos
    show mc default at mc_pos

    mc "Have you been to the sea, Mr. Cory?"

    show cory side at cory_pos

    cory "Sea? Nah, that's waaay past my territory."
    cory "Nearest I've been at is meters before saltwater and freshwater collides."
    cory "Besides, I'm a freshwater fish, guppy."
    cory "One step into sea, and I explode."

    show mc shock at mc_pos

    mc "EXPLODE??"
    mc "NOOO MR CORY PLEASE DON'T EXPLODE!!"
    mc "I LEFT MY GLUE AT HOME D:"

    show cory smile at cory_pos

    cory "Ay easy, easy!"
    cory "I won't be exploding now..!"

    show cory side at cory_pos

    cory "Ah but.. that woulda mean we have to part ways-"

    show mc excited at mc_pos

    mc "Woah look ahead!"
    mc "That's a lotta shoal!"

    show cory surprise at cory_pos

    cory "Huh..?"

    "Several tens of fishes crowd at what looks like a border built out of tall reefs."

    "A small cave sits in the middle where a speckle of colorful creature stands firm guarding the entrance."

    show cory talk at cory_pos

    cory "That's the border of salt fresh.."
    cory "Itsa always been a busy place but this amount is unnatural..."

    show mc o at mc_pos

    mc "Is that a shrimp guarding the cave hole?"

    "I squint my eyes into thin lines to take a better look on the eccentric colored guardian right before the cave's entrance."

    show mc excited at mc_pos

    mc "Oh oh!"
    mc "That's a mantis shrimp!! He looks really tough!"

    show mc happy at mc_pos

    mc "Mr Cory can we give it a handshake? :D"

    show cory side at cory_pos

    cory "Nuh uh!"
    cory "Unless you want your hand gone for good."

    show cory talk at cory_pos

    cory "But eh, that mantis shrimp.. He had been around for a good while."
    cory "He's quite friendly, it's hard to believe if the fuss is his doing."

    show mc o at mc_pos

    mc "Really?!"
    mc "You know him?"

    show cory smile at cory_pos

    cory "Yeah."
    cory "But I say we ask around first."
    cory "Figure out what the crowd's about."

    hide mc
    hide cory

    scene expression get_background()

    return


# =========================================================
# CHAPTER 2 HUB
# =========================================================

label chapter2_hub:

    scene expression get_background()

    call screen chapter2_interaction

    if _return == "salmon":

        call interact_with_npc("salmon")
        $ salmon_talked = True
        jump chapter2_hub

    elif _return == "arowana":

        call interact_with_npc("arowana")
        $ wana_talked = True
        jump chapter2_hub

    elif _return == "tiny_krill":

        if not tiny_krill_taken:

            $ add_item("tiny_krill")
            $ tiny_krill_taken = True

            scene expression get_dialogue_background()

            "Item get: Tiny Krill"

            show mc happy at mc_pos

            mc "A tiny krill! It looks so small and cute."

            hide mc

            scene expression get_background()

        jump chapter2_hub

    elif _return == "continue_chapter2_day":

        "Day cycle exploration complete."

        return

    jump chapter2_hub