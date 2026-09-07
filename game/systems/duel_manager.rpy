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

    def rps_shrimp_pick(player_history=None, round_num=1):
        """
        Mantis still uses the normal RPS rules, but becomes more
        observant as the duel goes on.

        The current choice is NOT used to choose the Mantis' move.
        Only previous player choices are considered, so the player
        cannot be directly countered after locking in a choice.
        """

        if not player_history or round_num <= 1:
            return random.choice(RPS_CHOICES)

        counts = {
            "rock": player_history.count("rock"),
            "paper": player_history.count("paper"),
            "scissors": player_history.count("scissors")
        }

        most_used = max(counts, key=counts.get)

        # Round 2: Mantis starts adapting.
        # Round 3+: Mantis reads the player's pattern more often.
        if round_num == 2:
            counter_chance = 0.55
        else:
            counter_chance = 0.70

        if random.random() < counter_chance:
            return {
                "rock": "paper",
                "paper": "scissors",
                "scissors": "rock"
            }[most_used]

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
default duel_player_history = []

default duel_player_hp = 3
default duel_shrimp_hp = 3
default duel_mantis_damaged = False



# =========================================================
# BATTLE ASSET HELPERS
# =========================================================

init python:

    def battle_asset(path):

        full_path = "images/battle/" + path

        if renpy.loadable(full_path):
            return full_path

        return None


    def duel_player_status_asset(fighter, hp):

        if fighter == "cory":

            if hp <= 0:
                return battle_asset("status/CoryDead.png")

            elif hp <= 2:
                return battle_asset("status/CoryHalf.png")

            else:
                return battle_asset("status/CoryFull.png")

        if hp <= 0:
            return battle_asset("status/McDead.png")

        elif hp <= 2:
            return battle_asset("status/McHalf.png")

        else:
            return battle_asset("status/McFull.png")


    def duel_shrimp_status_asset(hp):

        if hp <= 0:
            return battle_asset("status/ScyDead.png")

        elif hp <= 2:
            return battle_asset("status/ScyHalf.png")

        else:
            return battle_asset("status/ScyFull.png")


    def duel_shrimp_body_asset(hp, damaged=False):

        if hp <= 0:
            return None

        if damaged:

            if hp <= 2:
                return battle_asset("mantis/LowHPDMG.png")

            return battle_asset("mantis/IdleDMG.png")

        if hp <= 2:
            return battle_asset("mantis/LowHP.png")

        return battle_asset("mantis/Idle.png")


    def duel_player_choice_asset(fighter, choice):

        choice_map = {
            "mc": {
                "rock": "rps/MRock.png",
                "paper": "rps/MPaper.png",
                "scissors": "rps/MScissor.png"
            },

            "cory": {
                "rock": "rps/CRock.png",
                "paper": "rps/CPaper.png",
                "scissors": "rps/CScissor.png"
            }
        }

        return battle_asset(
            choice_map[fighter][choice]
        )


    def duel_shrimp_choice_asset(choice):

        choice_map = {
            "rock": "rps/SRock.png",
            "paper": "rps/SPaper.png",
            "scissors": "rps/SScissor.png"
        }

        return battle_asset(
            choice_map[choice]
        )


# =========================================================
# MAIN RPS SCREEN
# =========================================================

screen rps_round_screen(
    round_num,
    player_wins,
    shrimp_wins,
    fighter,
    player_hp,
    shrimp_hp
):

    modal True

    $ battle_bg = battle_asset(
        "Background.png"
    )

    if battle_bg:

        add battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    $ mantis_idle = duel_shrimp_body_asset(
        shrimp_hp,
        duel_mantis_damaged
    )

    if mantis_idle:

        add mantis_idle:
            xpos 0
            ypos 0


    $ player_status = duel_player_status_asset(
        fighter,
        player_hp
    )

    $ shrimp_status = duel_shrimp_status_asset(
        shrimp_hp
    )


    if player_status:

        add player_status:
            xpos 0
            ypos 0


    if shrimp_status:

        add shrimp_status:
            xpos 0
            ypos 0


    $ rock_button = battle_asset(
        "rps/Rock.png"
    )

    $ paper_button = battle_asset(
        "rps/Paper.png"
    )

    $ scissor_button = battle_asset(
        "rps/Scissor_.png"
    )


    if rock_button:

        imagebutton:

            idle rock_button
            hover rock_button

            xpos 0
            ypos 0

            focus_mask True

            action Return("rock")

    else:

        textbutton "ROCK":

            xalign 0.18
            yalign 0.87

            text_size 34

            action Return("rock")


    if paper_button:

        imagebutton:

            idle paper_button
            hover paper_button

            xpos 0
            ypos 0

            focus_mask True

            action Return("paper")

    else:

        textbutton "PAPER":

            xalign 0.50
            yalign 0.87

            text_size 34

            action Return("paper")


    if scissor_button:

        imagebutton:

            idle scissor_button
            hover scissor_button

            xpos 0
            ypos 0

            focus_mask True

            action Return("scissors")

    else:

        textbutton "SCISSORS":

            xalign 0.82
            yalign 0.87

            text_size 34

            action Return("scissors")


# =========================================================
# COUNTDOWN
# =========================================================

screen rps_countdown_screen(
    count_number,
    fighter,
    player_hp,
    shrimp_hp,
    countdown_time=1.0
):

    modal True

    $ battle_bg = battle_asset(
        "Background.png"
    )

    if battle_bg:

        add battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    $ mantis_idle = duel_shrimp_body_asset(
        shrimp_hp,
        duel_mantis_damaged
    )

    if mantis_idle:

        add mantis_idle:
            xpos 0
            ypos 0


    $ player_status = duel_player_status_asset(
        fighter,
        player_hp
    )

    $ shrimp_status = duel_shrimp_status_asset(
        shrimp_hp
    )


    if player_status:

        add player_status:
            xpos 0
            ypos 0


    if shrimp_status:

        add shrimp_status:
            xpos 0
            ypos 0


    $ countdown_asset = battle_asset(
        "rps/" + str(count_number) + ".png"
    )


    if countdown_asset:

        add countdown_asset:
            xpos 0
            ypos 0

    else:

        text "[count_number]":

            xalign 0.5
            yalign 0.53

            size 96

            color "#ffffff"

            outlines [
                (4, "#000000", 0, 0)
            ]


    timer countdown_time action Return()


# =========================================================
# RPS REVEAL
# =========================================================

screen rps_reveal_screen(
    player_choice,
    shrimp_choice,
    fighter,
    player_hp,
    shrimp_hp
):

    modal True

    $ battle_bg = battle_asset(
        "Background.png"
    )

    if battle_bg:

        add battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    $ mantis_idle = duel_shrimp_body_asset(
        shrimp_hp,
        duel_mantis_damaged
    )

    if mantis_idle:

        add mantis_idle:
            xpos 0
            ypos 0


    $ player_status = duel_player_status_asset(
        fighter,
        player_hp
    )

    $ shrimp_status = duel_shrimp_status_asset(
        shrimp_hp
    )


    if player_status:

        add player_status:
            xpos 0
            ypos 0


    if shrimp_status:

        add shrimp_status:
            xpos 0
            ypos 0


    $ player_pick_asset = duel_player_choice_asset(
        fighter,
        player_choice
    )

    if player_pick_asset:

        add player_pick_asset:
            xpos 0
            ypos 0


    $ shrimp_pick_asset = duel_shrimp_choice_asset(
        shrimp_choice
    )

    if shrimp_pick_asset:

        add shrimp_pick_asset:
            xpos 0
            ypos 0


    timer 1.2 action Return()




# =========================================================
# APPLY SHRIMP DAMAGE
# =========================================================

label mantis_apply_damage:

    if duel_weakened:

        $ duel_player_hp = max(
            0,
            duel_player_hp - 1
        )

    else:

        $ duel_player_hp = max(
            0,
            duel_player_hp - 3
        )

    return


# =========================================================
# BEST OF THREE
# =========================================================

label rps_best_of_three(
    fighter="mc",
    weakened=False
):

    $ duel_fighter = fighter
    $ duel_weakened = weakened

    $ duel_round_num = 1

    $ duel_player_wins = 0
    $ duel_shrimp_wins = 0
    $ duel_player_history = []

    $ duel_result = None

    $ duel_player_choice = None
    $ duel_shrimp_choice = None
    $ duel_outcome = None

    $ duel_player_hp = 3
    $ duel_shrimp_hp = 3

    $ duel_mantis_damaged = False

    while duel_result is None:

        $ duel_mantis_damaged = False


        # -----------------------------------------------------
        # PLAYER CHOICE
        # -----------------------------------------------------

        call screen rps_round_screen(
            duel_round_num,
            duel_player_wins,
            duel_shrimp_wins,
            duel_fighter,
            duel_player_hp,
            duel_shrimp_hp
        )

        $ duel_player_choice = _return


        # -----------------------------------------------------
        # COUNTDOWN
        # -----------------------------------------------------

        $ _countdown_steps = [
            3,
            2,
            1
        ]

        python:

            if duel_round_num == 1:
                countdown_time = 1.0

            elif duel_round_num == 2:
                countdown_time = 0.9

            else:
                countdown_time = 0.8

            for _count in _countdown_steps:

                renpy.call_screen(
                    "rps_countdown_screen",
                    _count,
                    duel_fighter,
                    duel_player_hp,
                    duel_shrimp_hp,
                    countdown_time
                )


        # -----------------------------------------------------
        # SHRIMP CHOICE
        # -----------------------------------------------------

        $ duel_shrimp_choice = rps_shrimp_pick(
            duel_player_history,
            duel_round_num
        )

        $ duel_player_history.append(
            duel_player_choice
        )


        $ duel_outcome = rps_resolve(
            duel_player_choice,
            duel_shrimp_choice
        )


        # -----------------------------------------------------
        # ROUND RESULT
        # -----------------------------------------------------

        if duel_outcome == "win":

            $ duel_player_wins += 1

            $ duel_shrimp_hp = max(
                0,
                duel_shrimp_hp - 1
            )

            $ duel_mantis_damaged = True


        elif duel_outcome == "lose":

            $ duel_shrimp_wins += 1


        # -----------------------------------------------------
        # REVEAL
        # -----------------------------------------------------

        call screen rps_reveal_screen(
            duel_player_choice,
            duel_shrimp_choice,
            duel_fighter,
            duel_player_hp,
            duel_shrimp_hp
        )


        # -----------------------------------------------------
        # DRAW
        # -----------------------------------------------------

        if duel_outcome == "draw":

            $ duel_round_num += 1



        # -----------------------------------------------------
        # PLAYER WINS
        # -----------------------------------------------------

        elif duel_outcome == "win":

            $ duel_mantis_damaged = False

            if duel_player_wins >= 2:

                $ duel_result = "player_win"



            if duel_shrimp_hp <= 0:

                $ duel_result = "player_win"



            $ duel_round_num += 1



        # -----------------------------------------------------
        # SHRIMP WINS
        # -----------------------------------------------------

        else:

            # Mantis gets to attack after winning the RPS round.

            call mantis_dodge


            if dodge_result:

                # Successful dodge means no damage.

                if duel_shrimp_wins >= 2:

                    $ duel_result = "ko"



                $ duel_round_num += 1



            else:

                # Failed dodge means the punch lands.

                call mantis_apply_damage


                if duel_player_hp <= 0:

                    $ duel_result = "ko"



                if duel_shrimp_wins >= 2:

                    $ duel_result = "ko"



                $ duel_round_num += 1


    return
