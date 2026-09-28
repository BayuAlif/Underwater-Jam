define NAME_INPUT_DEFAULT = "Koral"
define NAME_INPUT_PROMPT = "What is your name?"
define NAME_INPUT_MAX_LENGTH = 14

label name_input_start:
    stop music fadeout 1.0

    hide mc

    scene bg name_input with dissolve
    show mc_name_input at mc_name_pos onlayer master with dissolve

    "Oh my, a player? Hi there~! You're going to live for the next few hours in this cute adventurous little vessel... "
    "Pick a name that suits them~! Or do you want to go as their original name? Mmn not a very creative name I tell you.."

label name_input_prompt:
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
            jump name_input_prompt

    mc "Hehe, that's right! My name is [player_name]!"

    hide mc_name_input onlayer master with dissolve
    jump prologue
