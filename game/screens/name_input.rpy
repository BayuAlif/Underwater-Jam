define NAME_INPUT_DEFAULT = "Mc"
define NAME_INPUT_PROMPT = "What is your name?"
define NAME_INPUT_MAX_LENGTH = 14

label name_input_start:
    stop music fadeout 1.0

    window hide
    hide mc

    scene bg name_input with dissolve
    show mc_name_input at mc_name_pos onlayer master with dissolve

    $ entered_name = renpy.input(NAME_INPUT_PROMPT, default=NAME_INPUT_DEFAULT, length=NAME_INPUT_MAX_LENGTH).strip()
    $ entered_name = entered_name.replace("[", "").replace("]", "").replace("{", "").replace("}", "")

    if not entered_name:
        $ entered_name = NAME_INPUT_DEFAULT

    $ player_name = entered_name

    menu:
        "Is \"[player_name]\" your name?"
        "Yes, that's me!":
            pass
        "No, let me change it":
            jump name_input_start

    mc "Hehe, that's right! My name is [player_name]!"

    hide mc_name_input onlayer master with dissolve
    jump prologue
