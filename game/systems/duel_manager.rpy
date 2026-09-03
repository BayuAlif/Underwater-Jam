# =========================================================
# DUEL MANAGER
# Rock Paper Scissors combat system
# Chapter 2 - Mantis Shrimp
# =========================================================


# =========================================================
# RPS LOGIC
# =========================================================

init python:

    import random

    RPS_CHOICES = [
        "rock",
        "paper",
        "scissors"
    ]

    RPS_BEATS = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def rps_shrimp_pick():
        return random.choice(RPS_CHOICES)

    def rps_resolve(player_choice, shrimp_choice):

        if player_choice == shrimp_choice:
            return "draw"

        if RPS_BEATS[player_choice] == shrimp_choice:
            return "win"

        return "lose"


# =========================================================
# DUEL VARIABLES
# =========================================================

default duel_fighter = "mc"
default duel_weakened = False
default duel_result = None
default duel_player_choice = None
default duel_shrimp_choice = None
default duel_outcome = None
default duel_round_num = 1
default duel_player_wins = 0
default duel_shrimp_wins = 0


# =========================================================
# BATTLE BACKGROUND HELPER
# =========================================================

init python:

    def mantis_battle_background():

        if renpy.loadable("images/battle/BackgroundBattle.png"):
            return "images/battle/BackgroundBattle.png"

        return None


# =========================================================
# MAIN BATTLE PAGE
# =========================================================

screen rps_round_screen(round_num, player_wins, shrimp_wins):

    modal True

    if renpy.loadable("images/battle/BackgroundBattle.png"):

        add "images/battle/BackgroundBattle.png"

    else:

        add Solid("#160b1b")


    # -----------------------------------------------------
    # MANTIS IDLE
    # -----------------------------------------------------

    if renpy.loadable("images/battle/Idle.png"):

        add "images/battle/Idle.png":
            xalign 0.5
            yalign 0.43


    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------

    text "SACRED DUEL":

        xalign 0.5
        ypos 0.035

        size 42
        color "#ffffff"

        outlines [
            (3, "#000000", 0, 0)
        ]


    text "ROUND [round_num]":

        xalign 0.5
        ypos 0.10

        size 28
        color "#ffffff"

        outlines [
            (2, "#000000", 0, 0)
        ]


    # -----------------------------------------------------
    # HP / SCORE
    # -----------------------------------------------------

    text "PLAYER     [player_wins]":

        xpos 0.06
        ypos 0.05

        size 26
        color "#ffffff"

        outlines [
            (2, "#000000", 0, 0)
        ]


    text "SHRIMP     [shrimp_wins]":

        xpos 0.77
        ypos 0.05

        size 26
        color "#ffffff"

        outlines [
            (2, "#000000", 0, 0)
        ]


    # -----------------------------------------------------
    # PLAYER HP ICONS
    # -----------------------------------------------------

    if renpy.loadable("images/battle/hp_full.png"):

        add "images/battle/hp_full.png":
            xpos 0.055
            ypos 0.13

    if renpy.loadable("images/battle/hp_full.png") and player_wins >= 1:

        add "images/battle/hp_full.png":
            xpos 0.105
            ypos 0.13


    # -----------------------------------------------------
    # SHRIMP HP ICONS
    # -----------------------------------------------------

    if renpy.loadable("images/battle/hp_full.png"):

        add "images/battle/hp_full.png":
            xpos 0.86
            ypos 0.13

    if renpy.loadable("images/battle/hp_full.png") and shrimp_wins >= 1:

        add "images/battle/hp_full.png":
            xpos 0.91
            ypos 0.13


    # -----------------------------------------------------
    # ROCK
    # -----------------------------------------------------

    if renpy.loadable("images/battle/Rock.png"):

        imagebutton:

            idle "images/battle/Rock.png"
            hover "images/battle/Rock.png"

            xalign 0.18
            yalign 0.87

            action Return("rock")

    else:

        textbutton "ROCK":

            xalign 0.18
            yalign 0.87

            text_size 34

            action Return("rock")


    # -----------------------------------------------------
    # PAPER
    # -----------------------------------------------------

    if renpy.loadable("images/battle/Paper.png"):

        imagebutton:

            idle "images/battle/Paper.png"
            hover "images/battle/Paper.png"

            xalign 0.50
            yalign 0.87

            action Return("paper")

    else:

        textbutton "PAPER":

            xalign 0.50
            yalign 0.87

            text_size 34

            action Return("paper")


    # -----------------------------------------------------
    # SCISSOR
    # -----------------------------------------------------

    if renpy.loadable("images/battle/Scissor.png"):

        imagebutton:

            idle "images/battle/Scissor.png"
            hover "images/battle/Scissor.png"

            xalign 0.82
            yalign 0.87

            action Return("scissors")

    else:

        textbutton "SCISSORS":

            xalign 0.82
            yalign 0.87

            text_size 34

            action Return("scissors")


# =========================================================
# BATTLE RESULT PAGE
# =========================================================

screen rps_result_screen(player_choice, shrimp_choice, outcome):

    modal True

    if renpy.loadable("images/battle/BackgroundBattle.png"):
        add "images/battle/BackgroundBattle.png"
    else:
        add Solid("#160b1b")


    # -----------------------------------------------------
    # CHOOSE MANTIS IMAGE
    # -----------------------------------------------------

    if outcome == "lose":

        if renpy.loadable("images/battle/IdleDMG.png"):
            add "images/battle/IdleDMG.png":
                xalign 0.5
                yalign 0.43

        elif renpy.loadable("images/battle/Idle.png"):
            add "images/battle/Idle.png":
                xalign 0.5
                yalign 0.43

    else:

        if renpy.loadable("images/battle/Idle.png"):
            add "images/battle/Idle.png":
                xalign 0.5
                yalign 0.43


    # -----------------------------------------------------
    # RESULT TEXT
    # -----------------------------------------------------

    if outcome == "draw":

        text "DRAW!":
            xalign 0.5
            ypos 0.15
            size 52
            color "#ffffff"
            outlines [(3, "#000000", 0, 0)]

    elif outcome == "win":

        text "YOU WIN!":
            xalign 0.5
            ypos 0.15
            size 52
            color "#ffffff"
            outlines [(3, "#000000", 0, 0)]

    else:

        text "MR. SHRIMP WINS!":
            xalign 0.5
            ypos 0.15
            size 52
            color "#ffffff"
            outlines [(3, "#000000", 0, 0)]


    text "YOU: [player_choice.upper()]":
        xalign 0.5
        ypos 0.25
        size 28
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    text "MR. SHRIMP: [shrimp_choice.upper()]":
        xalign 0.5
        ypos 0.30
        size 28
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]


    # -----------------------------------------------------
    # IMPACT IMAGE
    # -----------------------------------------------------

    if outcome == "win":

        if player_choice == "rock" and renpy.loadable("images/battle/RockImpact.png"):
            add "images/battle/RockImpact.png":
                xalign 0.5
                yalign 0.55

        elif player_choice == "paper" and renpy.loadable("images/battle/PaperImpact.png"):
            add "images/battle/PaperImpact.png":
                xalign 0.5
                yalign 0.55

        elif player_choice == "scissors" and renpy.loadable("images/battle/ScissorImpact.png"):
            add "images/battle/ScissorImpact.png":
                xalign 0.5
                yalign 0.55


    elif outcome == "lose":

        if shrimp_choice == "rock" and renpy.loadable("images/battle/RockImpact.png"):
            add "images/battle/RockImpact.png":
                xalign 0.5
                yalign 0.55

        elif shrimp_choice == "paper" and renpy.loadable("images/battle/PaperImpact.png"):
            add "images/battle/PaperImpact.png":
                xalign 0.5
                yalign 0.55

        elif shrimp_choice == "scissors" and renpy.loadable("images/battle/ScissorImpact.png"):
            add "images/battle/ScissorImpact.png":
                xalign 0.5
                yalign 0.55


    textbutton "CONTINUE":

        xalign 0.5
        yalign 0.90

        text_size 30

        action Return()


# =========================================================
# BEST OF THREE
# =========================================================

label rps_best_of_three(fighter="mc", weakened=False):

    $ duel_fighter = fighter
    $ duel_weakened = weakened
    $ duel_round_num = 1
    $ duel_player_wins = 0
    $ duel_shrimp_wins = 0
    $ duel_result = None

    jump rps_round_loop


# =========================================================
# RPS ROUND LOOP
# =========================================================

label rps_round_loop:

    # -----------------------------------------------------
    # FULL BATTLE PAGE
    # -----------------------------------------------------

    hide mc
    hide cory
    hide shrimp

    call screen rps_round_screen(
        duel_round_num,
        duel_player_wins,
        duel_shrimp_wins
    )

    $ duel_player_choice = _return
    $ duel_shrimp_choice = rps_shrimp_pick()

    $ duel_outcome = rps_resolve(
        duel_player_choice,
        duel_shrimp_choice
    )


    # -----------------------------------------------------
    # RESULT PAGE
    # -----------------------------------------------------

    call screen rps_result_screen(
        duel_player_choice,
        duel_shrimp_choice,
        duel_outcome
    )


    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    if duel_outcome == "draw":

        jump rps_round_loop


    # -----------------------------------------------------
    # PLAYER WINS ROUND
    # -----------------------------------------------------

    elif duel_outcome == "win":

        $ duel_player_wins += 1
        $ duel_round_num += 1

        if duel_player_wins >= 2:

            $ duel_result = "player_win"
            return

        jump rps_round_loop


    # -----------------------------------------------------
    # SHRIMP WINS ROUND
    # -----------------------------------------------------

    else:

        $ duel_shrimp_wins += 1
        $ duel_round_num += 1

        # Coal Tar means the shrimp does not immediately KO
        # the current fighter.
        if duel_weakened:

            if duel_shrimp_wins >= 2:

                $ duel_result = "ko"
                return

            jump rps_round_loop

        # Without Coal Tar, one clean hit KOs MC.
        else:

            $ duel_result = "ko"
            return
