default duel_fighter = "mc"
default duel_player_wins = 0
default duel_shrimp_wins = 0
default duel_player_hp = 3
default duel_shrimp_hp = 3
default duel_round = 1

default duel_player_choice = None
default duel_shrimp_choice = None
default duel_outcome = None
default duel_result = None

default coal_tar_effective = False
default dodge_result = False

init python:

    import random

    RPS_BEATS = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def resolve_rps(player, shrimp):

        if player == shrimp:
            return "draw"

        if RPS_BEATS[player] == shrimp:
            return "win"

        return "lose"

    def shrimp_pick(history):

        choices = ["rock", "paper", "scissors"]

        if not history:
            return random.choice(choices)

        counts = {
            "rock": history.count("rock"),
            "paper": history.count("paper"),
            "scissors": history.count("scissors")
        }

        most_used = max(counts, key=counts.get)

        counter = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }

        if random.random() < 0.65:
            return counter[most_used]

        return random.choice(choices)


screen rps_round():

    modal True

    add "battle_background"

    if duel_shrimp_hp >= 3:
        add "mantis_battle"
    elif duel_shrimp_hp > 0:
        add "mantis_battle_low"


    if duel_fighter == "mc":

        if duel_player_hp >= 3:
            add "images/battle/status/McFull.png"
        elif duel_player_hp > 0:
            add "images/battle/status/McHalf.png"
        else:
            add "images/battle/status/McDead.png"

    else:

        if duel_player_hp >= 3:
            add "images/battle/status/CoryFull.png"
        elif duel_player_hp > 0:
            add "images/battle/status/CoryHalf.png"
        else:
            add "images/battle/status/CoryDead.png"


    if duel_shrimp_hp >= 3:
        add "images/battle/status/ScyFull.png"
    elif duel_shrimp_hp > 0:
        add "images/battle/status/ScyHalf.png"
    else:
        add "images/battle/status/ScyDead.png"


    imagebutton:
        idle "images/battle/rps/Rock.png"
        hover "images/battle/rps/Rock.png"
        focus_mask True
        action Return("rock")


    imagebutton:
        idle "images/battle/rps/Paper.png"
        hover "images/battle/rps/Paper.png"
        focus_mask True
        action Return("paper")


    imagebutton:
        idle "images/battle/rps/Scissor_.png"
        hover "images/battle/rps/Scissor_.png"
        focus_mask True
        action Return("scissors")


screen rps_reveal():

    modal True

    add "battle_background"

    if duel_shrimp_hp >= 3:
        add "mantis_battle"
    elif duel_shrimp_hp > 0:
        add "mantis_battle_low"


    if duel_fighter == "mc":

        if duel_player_hp >= 3:
            add "images/battle/status/McFull.png"
        elif duel_player_hp > 0:
            add "images/battle/status/McHalf.png"
        else:
            add "images/battle/status/McDead.png"

        if duel_player_choice == "rock":
            add "images/battle/rps/MRock.png"
        elif duel_player_choice == "paper":
            add "images/battle/rps/MPaper.png"
        else:
            add "images/battle/rps/MScissor.png"

    else:

        if duel_player_hp >= 3:
            add "images/battle/status/CoryFull.png"
        elif duel_player_hp > 0:
            add "images/battle/status/CoryHalf.png"
        else:
            add "images/battle/status/CoryDead.png"

        if duel_player_choice == "rock":
            add "images/battle/rps/CRock.png"
        elif duel_player_choice == "paper":
            add "images/battle/rps/CPaper.png"
        else:
            add "images/battle/rps/CScissor.png"


    if duel_shrimp_hp >= 3:
        add "images/battle/status/ScyFull.png"
    elif duel_shrimp_hp > 0:
        add "images/battle/status/ScyHalf.png"
    else:
        add "images/battle/status/ScyDead.png"


    if duel_shrimp_choice == "rock":
        add "images/battle/rps/SRock.png"
    elif duel_shrimp_choice == "paper":
        add "images/battle/rps/SPaper.png"
    else:
        add "images/battle/rps/SScissor.png"

    timer 1.0 action Return()


screen dodge_simple():

    modal True

    add "battle_background"

    if duel_shrimp_choice == "rock":
        add "images/battle/dodge/rock/Rock.png"
        add "images/battle/dodge/rock/RockDodge.png"

    elif duel_shrimp_choice == "paper":
        add "images/battle/dodge/paper/Paper.png"
        add "images/battle/dodge/paper/PaperDodge.png"

    else:
        add "images/battle/dodge/scissors/Scissor.png"
        add "images/battle/dodge/scissors/ScissorDodge.png"


    text "DODGE!":
        xalign 0.5
        yalign 0.20
        size 60
        bold True


    textbutton "DODGE":
        xalign 0.5
        yalign 0.78
        xsize 350
        ysize 100
        action Return(True)


    timer 1.2 action Return(False)


label mantis_duel:

    $ duel_fighter = "mc"

    $ duel_player_wins = 0
    $ duel_shrimp_wins = 0

    $ duel_player_hp = 3
    $ duel_shrimp_hp = 3

    $ duel_round = 1

    $ history = []

    while duel_player_wins < 2 and duel_shrimp_wins < 2:

        call screen rps_round

        $ duel_player_choice = _return

        $ duel_shrimp_choice = shrimp_pick(history)

        $ history.append(duel_player_choice)

        $ duel_outcome = resolve_rps(
            duel_player_choice,
            duel_shrimp_choice
        )

        if duel_outcome == "win":

            $ duel_player_wins += 1
            $ duel_shrimp_hp = max(0, duel_shrimp_hp - 1)

        elif duel_outcome == "lose":

            $ duel_shrimp_wins += 1

            call screen dodge_simple

            $ dodge_result = _return

            if not dodge_result:

                if coal_tar_effective:
                    $ duel_player_hp = max(0, duel_player_hp - 1)
                else:
                    $ duel_player_hp = max(0, duel_player_hp - 3)

        call screen rps_reveal

        if duel_player_hp <= 0 or duel_shrimp_hp <= 0:
            $ duel_round = 3
        else:
            $ duel_round += 1

    if duel_player_wins >= 2 or duel_shrimp_hp <= 0:
        $ duel_result = "player_win"
        return "player_win"

    return "lose"