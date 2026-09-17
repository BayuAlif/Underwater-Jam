default duel_fighter = "mc"
default duel_player_wins = 0
default duel_shrimp_wins = 0
default duel_player_hp = 3
default duel_shrimp_hp = 3
default duel_round = 1
default duel_z_taps = 0
default duel_z_target = 10
default duel_result = None
default coal_tar_effective = False
default dodge_result = False

init python:
    import random

    def duel_press_z():
        store.duel_z_taps += 1


screen mantis_z_round():
    modal True

    add "ch2_night"

    if duel_fighter == "mc":
        add "mc default" at mc_left
    else:
        add "cory talk" at cory_left

    add "shrimp default" at shrimp_right

    text "ROUND [duel_round]":
        xalign 0.5
        yalign 0.08
        size 42
        bold True

    text "SPAM Z! [duel_z_taps] / [duel_z_target]":
        xalign 0.5
        yalign 0.16
        size 34
        bold True

    frame:
        xalign 0.5
        yalign 0.30
        xsize 900
        ysize 36
        background Solid("#00000099")

        bar value duel_z_taps range duel_z_target:
            left_bar Solid("#FFFFFF")
            right_bar Solid("#555555")
            ysize 36

    text "PRESS Z!":
        xalign 0.5
        yalign 0.55
        size 60
        bold True

    text "Your HP: [duel_player_hp]   Mantis HP: [duel_shrimp_hp]":
        xalign 0.5
        yalign 0.68
        size 30

    key "K_z" action Function(duel_press_z)

    timer 1.8 action Return(duel_z_taps >= duel_z_target)


label mantis_duel:

    $ duel_player_wins = 0
    $ duel_shrimp_wins = 0
    $ duel_player_hp = 3
    $ duel_shrimp_hp = 3
    $ duel_round = 1
    $ duel_result = None

    while duel_round <= 3 and duel_player_wins < 2 and duel_shrimp_wins < 2 and duel_player_hp > 0 and duel_shrimp_hp > 0:

        $ duel_z_target = random.randint(9, 12)
        $ duel_z_taps = 0

        call screen mantis_z_round

        $ duel_won_round = _return

        if duel_won_round:
            $ duel_player_wins += 1
            $ duel_shrimp_hp = max(0, duel_shrimp_hp - 1)
        else:
            $ duel_shrimp_wins += 1
            if coal_tar_effective:
                $ duel_player_hp = max(0, duel_player_hp - 1)
            else:
                $ duel_player_hp = 0

        $ duel_round += 1

    if duel_player_wins >= 2 or duel_shrimp_hp <= 0:
        $ duel_result = "player_win"
        return "player_win"

    $ duel_result = "lose"
    return "lose"
