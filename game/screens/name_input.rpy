define NAME_INPUT_DEFAULT = "Koral"
define NAME_INPUT_PROMPT = "Pick a name that suits them"
define NAME_INPUT_MAX_LENGTH = 14

label name_input_start:
    stop music fadeout 1.0
    scene black

    hide mc

    scene bg name_input with dissolve
    show mc_name_input at mc_name_pos onlayer master with dissolve

    "Oh my, a player? Hi there~! You're going to live for the next few hours in this cute adventurous little vessel..."

label name_input_prompt:
    $ default_name = player_name if player_name else NAME_INPUT_DEFAULT
    $ entered_name = renpy.input(NAME_INPUT_PROMPT, default=default_name, length=NAME_INPUT_MAX_LENGTH)
    $ entered_name = entered_name.replace("[", "").replace("]", "").replace("{", "").replace("}", "").strip()

    if not entered_name:
        $ entered_name = NAME_INPUT_DEFAULT

    $ player_name = entered_name

    "Is \"[player_name]\" your name?"

    menu:
        "Yes, that's me!":
            pass
        "No, let me change it":
            jump name_input_prompt

    mc "Hehe, that's right! My name is [player_name]!"

    hide mc_name_input onlayer master with dissolve
    jump prologue
