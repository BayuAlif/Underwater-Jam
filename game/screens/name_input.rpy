## Name Input System for Underwater Jam

define NAME_INPUT_DEFAULT = "Mc"
define NAME_INPUT_PROMPT = "What is your name?"
define NAME_INPUT_MAX_LENGTH = 14

label name_input_start:
    # Reset audio or fade smoothly
    stop music fadeout 1.0

    # Ensure clean screen state
    window hide
    hide mc

    # Show background and MC sprite on master layer (behind textbox on screens layer)
    scene bg name_input with dissolve
    show mc_name_input at mc_name_pos onlayer master with dissolve

    # Prompt the player to input their name
    $ entered_name = renpy.input(NAME_INPUT_PROMPT, default=NAME_INPUT_DEFAULT, length=NAME_INPUT_MAX_LENGTH).strip()
    $ entered_name = entered_name.replace("[", "").replace("]", "").replace("{", "").replace("}", "")

    # Fallback to default if empty
    if not entered_name:
        $ entered_name = NAME_INPUT_DEFAULT

    $ player_name = entered_name

    # Confirmation so player can correct any typos
    menu:
        "Is \"[player_name]\" your name?"
        "Yes, that's me!":
            pass
        "No, let me change it":
            jump name_input_start

    # Character speaks their own name to confirm the namebox works
    mc "Hehe, that's right! My name is [player_name]!"

    # Clean transition into prologue
    hide mc_name_input onlayer master with dissolve
    jump prologue
