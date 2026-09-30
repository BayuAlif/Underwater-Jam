image dunge battle bg = "images/jankenpon/Bg1.png"

image dunge idle = "images/jankenpon/Idle1.png"
image dunge damaged = "images/jankenpon/IdleDMG.png"

image jankenpon countdown 3 = "images/jankenpon/Button Rock Paper Scissor/3.png"
image jankenpon countdown 2 = "images/jankenpon/Button Rock Paper Scissor/2.png"
image jankenpon countdown 1 = "images/jankenpon/Button Rock Paper Scissor/1.png"

image player rock = "images/jankenpon/Button Rock Paper Scissor/CRock.png"
image player paper = "images/jankenpon/Button Rock Paper Scissor/CPaper.png"
image player scissors = "images/jankenpon/Button Rock Paper Scissor/CScissor.png"

image boss rock = "images/jankenpon/Button Rock Paper Scissor/SRock.png"
image boss paper = "images/jankenpon/Button Rock Paper Scissor/SPaper.png"
image boss scissors = "images/jankenpon/Button Rock Paper Scissor/SScissor.png"

image draw rock = "images/jankenpon/Button Rock Paper Scissor/MRock.png"
image draw paper = "images/jankenpon/Button Rock Paper Scissor/MPaper.png"
image draw scissors = "images/jankenpon/Button Rock Paper Scissor/MScissor.png"

image jankenpon button rock = "images/jankenpon/Button Rock Paper Scissor/Rock.png"
image jankenpon button paper = "images/jankenpon/Button Rock Paper Scissor/Paper.png"
image jankenpon button scissors = "images/jankenpon/Button Rock Paper Scissor/Scissor_.png"

image mantis icon full = "images/jankenpon/ICON/ScyFull.png"
image mantis icon half = "images/jankenpon/ICON/ScyHalf.png"
image mantis icon one  = "images/jankenpon/ICON/ScyOne.png"
image mantis icon dead = "images/jankenpon/ICON/ScyDead.png"

image dunge icon full = "images/jankenpon/ICON/ScyFull.png"
image dunge icon half = "images/jankenpon/ICON/ScyHalf.png"
image dunge icon one  = "images/jankenpon/ICON/ScyOne.png"
image dunge icon dead = "images/jankenpon/ICON/ScyDead.png"

image mc icon full = "images/jankenpon/ICON/McFull.png"
image mc icon half = "images/jankenpon/ICON/McHalf.png"
image mc icon one  = "images/jankenpon/ICON/McOne.png"
image mc icon dead = "images/jankenpon/ICON/McDead.png"

image cory icon full = "images/jankenpon/ICON/CoryFull.png"
image cory icon half = "images/jankenpon/ICON/CoryHalf.png"
image cory icon one  = "images/jankenpon/ICON/CoryOne.png"
image cory icon dead = "images/jankenpon/ICON/CoryDead.png"

default dunge_cory_start_hp = 3
default dunge_boss_hp = 5
default dunge_mc_hp = 3
default dunge_cory_hp = 3

default dunge_mc_losses = 0
default dunge_cory_losses = 0

default dunge_player_choice = None
default dunge_boss_choice = None
default dunge_round_result = None
default dunge_active_fighter = "mc"

default dunge_laststand_taps = 0
default dunge_laststand_target = 10
default dunge_laststand_success = False

default dunge_battle_encounter = "dunge"
default dunge_battle_result = None

init python:

    import random

    def dunge_boss_pick():
        if "duel_ai_pick" in globals():
            return duel_ai_pick(getattr(store, "player_choice_history", []), getattr(store, "duel_boss", "dunge"))
        return random.choice(["rock", "paper", "scissors"])

    def dunge_jankenpon_result(player, boss):
        p = "scissors" if player in ("scissor", "scissors") else str(player).lower()
        b = "scissors" if boss in ("scissor", "scissors") else str(boss).lower()

        if p == b:
            return "tie"

        if (
            (p == "rock" and b == "scissors")
            or (p == "paper" and b == "rock")
            or (p == "scissors" and b == "paper")
        ):
            return "win"

        return "lose"

    def dunge_laststand_tap():
        if store.dunge_laststand_taps < store.dunge_laststand_target:
            store.dunge_laststand_taps += 1

screen dunge_battle_stage():

    add "dunge battle bg"

    if dunge_boss_hp <= 2:
        add "dunge damaged":
            xalign 0.5
            yalign 0.5
    else:
        add "dunge idle":
            xalign 0.5
            yalign 0.5

    if dunge_mc_losses >= 2:

        if dunge_cory_losses >= 2:
            add "cory icon dead":
                xalign 0.12
                yalign 0.12
        elif dunge_cory_losses == 1:
            add "cory icon half":
                xalign 0.12
                yalign 0.12
        else:
            add "cory icon full":
                xalign 0.12
                yalign 0.12

        add "mc icon dead":
            xalign 0.25
            yalign 0.16
            zoom 0.5

    else:

        if dunge_mc_losses >= 2:
            add "mc icon dead":
                xalign 0.12
                yalign 0.12
        elif dunge_mc_losses == 1:
            add "mc icon half":
                xalign 0.12
                yalign 0.12
        else:
            add "mc icon full":
                xalign 0.12
                yalign 0.12

    if dunge_boss_hp <= 0:
        add "dunge icon dead":
            xalign 0.88
            yalign 0.12
    elif dunge_boss_hp <= 2:
        add "dunge icon half":
            xalign 0.88
            yalign 0.12
    else:
        add "dunge icon full":
            xalign 0.88
            yalign 0.12

    frame:
        xalign 0.5
        yalign 0.04
        padding (18, 10)

        vbox:
            spacing 4
            text "DUNGE BATTLE" size 30
            text "Dunge HP: [dunge_boss_hp] / 5" size 22

            if dunge_mc_losses >= 2:
                text "Cory's turn" size 20
            else:
                text "MC's turn" size 20

screen dunge_jankenpon_screen():
    modal True

    button:
        xalign 0.0
        yalign 0.0
        xsize int(config.screen_width / 3)
        ysize config.screen_height
        background None
        hover_background None
        action Return("rock")

    button:
        xalign 0.5
        yalign 0.0
        xsize int(config.screen_width / 3)
        ysize config.screen_height
        xoffset -int(config.screen_width / 6)
        background None
        hover_background None
        action Return("scissors")

    button:
        xalign 1.0
        yalign 0.0
        xsize int(config.screen_width / 3)
        ysize config.screen_height
        xoffset 0
        background None
        hover_background None
        action Return("paper")

    add "jankenpon button rock":
        xalign 0.20
        yalign 0.90
        zoom 0.75

    add "jankenpon button scissors":
        xalign 0.50
        yalign 0.90
        zoom 0.75

    add "jankenpon button paper":
        xalign 0.80
        yalign 0.90
        zoom 0.75

screen dunge_countdown_screen(number, count_delay=0.6):

    modal True
    on "show" action Play("sound", "audio/sfx/pixel_ui_3.mp3")

    if number == 3:
        add "jankenpon countdown 3":
            xalign 0.5
            yalign 0.5

    elif number == 2:
        add "jankenpon countdown 2":
            xalign 0.5
            yalign 0.5

    else:
        add "jankenpon countdown 1":
            xalign 0.5
            yalign 0.5

    timer count_delay action Return()

screen dunge_round_reveal(player_move, boss_move, result):

    modal True

    if result == "tie":

        if player_move == "rock":
            add "draw rock":
                xalign 0.28
                yalign 0.5
                zoom 0.65
            add "boss rock":
                xalign 0.72
                yalign 0.5
                zoom 0.65

        elif player_move == "paper":
            add "draw paper":
                xalign 0.28
                yalign 0.5
                zoom 0.65
            add "boss paper":
                xalign 0.72
                yalign 0.5
                zoom 0.65

        else:
            add "draw scissors":
                xalign 0.28
                yalign 0.5
                zoom 0.65
            add "boss scissors":
                xalign 0.72
                yalign 0.5
                zoom 0.65

    else:

        if player_move == "rock":
            add "player rock":
                xalign 0.28
                yalign 0.68
                zoom 0.65

        elif player_move == "paper":
            add "player paper":
                xalign 0.28
                yalign 0.68
                zoom 0.65

        else:
            add "player scissors":
                xalign 0.28
                yalign 0.68
                zoom 0.65

        if boss_move == "rock":
            add "boss rock":
                xalign 0.72
                yalign 0.68
                zoom 0.65

        elif boss_move == "paper":
            add "boss paper":
                xalign 0.72
                yalign 0.68
                zoom 0.65

        else:
            add "boss scissors":
                xalign 0.72
                yalign 0.68
                zoom 0.65

    if result == "win":
        add "images/jankenpon/Win, Lose, Draw/Win.png":
            xalign 0.5
            yalign 0.38
            zoom 0.8

    elif result == "lose":
        add "images/jankenpon/Win, Lose, Draw/Lose.png":
            xalign 0.5
            yalign 0.38
            zoom 0.8

    else:
        add "images/jankenpon/Win, Lose, Draw/Draw_.png":
            xalign 0.5
            yalign 0.38
            zoom 0.8

    button:
        xfill True
        yfill True
        background None
        action Return()

    timer 1.2 action Return()

screen dunge_laststand_screen():

    modal True

    add "dunge battle bg"

    add "dunge idle":
        xalign 0.5
        yalign 0.5

    frame:
        xalign 0.5
        yalign 0.12
        padding (30, 20)

        vbox:
            spacing 12
            text "LAST STAND!" size 42
            text "Press Z as fast as you can!" size 30
            text "[dunge_laststand_taps] / [dunge_laststand_target]" size 32

            bar:
                value dunge_laststand_taps
                range dunge_laststand_target
                xsize 600

    key "K_z" action Function(dunge_laststand_tap)

    timer 3.0 action Return(
        dunge_laststand_taps >= dunge_laststand_target
    )

screen dunge_defeat_screen():

    modal True

    add "dunge battle bg"

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)

        vbox:
            spacing 20

            text "DEFEATED" size 42

            textbutton "Try Again":
                action Return("retry")

            textbutton "Return to Main Menu":
                action MainMenu(confirm=False)

label dunge_play_round:

    call screen dunge_jankenpon_screen
    $ dunge_player_choice = _return

    call screen dunge_countdown_screen(3)
    call screen dunge_countdown_screen(2)
    call screen dunge_countdown_screen(1)

    $ dunge_boss_choice = dunge_boss_pick()
    $ dunge_round_result = dunge_jankenpon_result(
        dunge_player_choice,
        dunge_boss_choice
    )

    call screen dunge_round_reveal(
        dunge_player_choice,
        dunge_boss_choice,
        dunge_round_result
    )

    if dunge_round_result == "win":

        $ dunge_boss_hp -= 1

    elif dunge_round_result == "lose":

        if dunge_active_fighter == "mc":
            $ dunge_mc_losses += 1
            $ dunge_mc_hp = max(0, 3 - dunge_mc_losses)

        elif dunge_active_fighter == "cory":
            $ dunge_cory_losses += 1
            $ dunge_cory_hp = max(0, dunge_cory_start_hp - dunge_cory_losses)

        elif dunge_active_fighter == "laststand":
            $ dunge_mc_hp = 0

    return

label dunge_battle_start(cory_start_hp=3):
    if dunge_battle_encounter == "empress":
        $ duel_boss = "empress"
    else:
        $ duel_boss = "dunge"

    call run_duel(duel_boss)

    return
