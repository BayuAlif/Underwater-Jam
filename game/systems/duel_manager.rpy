default duel_fighter = "mc"
default duel_player_wins = 0
default duel_shrimp_wins = 0
default duel_player_hp = 3
default duel_shrimp_hp = 3
default duel_round = 1
default duel_player_choice = None
default duel_shrimp_choice = None
default duel_round_result = None
default duel_player_history = []
default duel_z_taps = 0
default duel_z_target = 10
default duel_result = None
default coal_tar_effective = False
default dodge_result = False

# ---------------------------------------------------------------------------
# TEMPORARY DEV BYPASS - Mantis Shrimp boss fight (Chapter 2)
# Set to False to restore the real minigame once it's ready to be worked on
# again. While True, "label mantis_duel" below skips the whole RPS/dodge
# minigame (and therefore the "Try again? / Return to Hub" lose-loop) and
# always resolves as a win, so the existing post-duel story/flags still run
# normally.
# ---------------------------------------------------------------------------
define MANTIS_DUEL_BYPASS = True


image mantis dodge rock = "images/jankenpon/Rock/RockDodge.png"
image mantis dodge paper = "images/jankenpon/Paper/PaperDodge.png"
image mantis dodge scissors = "images/jankenpon/Scissor/ScissorDodge.png"

image mantis key idle = "images/jankenpon/Paper/KeyIdle.png"
image mantis key smash = "images/jankenpon/Paper/KeySmash.png"

image mantis arrow blue = "images/jankenpon/Paper/ArrowBlue.png"
image mantis arrow red = "images/jankenpon/Paper/ArrowRed.png"

image mantis bar red = "images/jankenpon/Paper/PressBar/RedFull.png"
image mantis bar blue1 = "images/jankenpon/Paper/PressBar/Blue1.png"
image mantis bar blue2 = "images/jankenpon/Paper/PressBar/Blue2.png"
image mantis bar blue3 = "images/jankenpon/Paper/PressBar/Blue3.png"
image mantis bar blue4 = "images/jankenpon/Paper/PressBar/Blue4.png"
image mantis bar blue5 = "images/jankenpon/Paper/PressBar/Blue5.png"
image mantis bar blue6 = "images/jankenpon/Paper/PressBar/Blue6.png"
image mantis bar full = "images/jankenpon/Paper/PressBar/BlueFull.png"


init python:

    import random

    def duel_press_z():
        store.duel_z_taps += 1

    def mantis_ai_pick(history):
        moves = ["rock", "paper", "scissors"]

        if not history or random.random() < 0.4:
            return random.choice(moves)

        recent = history[-3:]

        counts = {
            "rock": recent.count("rock"),
            "paper": recent.count("paper"),
            "scissors": recent.count("scissors")
        }

        favorite = max(counts, key=counts.get)

        beats = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }

        return beats[favorite]


screen mantis_battle_stage():

    add "dunge battle bg"

    if duel_shrimp_hp <= 1:
        add "dunge damaged":
            xalign 0.5
            yalign 0.5
    else:
        add "dunge idle":
            xalign 0.5
            yalign 0.5

    if duel_fighter == "mc":

        if duel_player_hp <= 0:
            add "mc icon dead":
                xalign 0.12
                yalign 0.12

        elif duel_player_hp == 1:
            add "mc icon half":
                xalign 0.12
                yalign 0.12

        else:
            add "mc icon full":
                xalign 0.12
                yalign 0.12

    else:

        if duel_player_hp <= 0:
            add "cory icon dead":
                xalign 0.12
                yalign 0.12

        elif duel_player_hp == 1:
            add "cory icon half":
                xalign 0.12
                yalign 0.12

        else:
            add "cory icon full":
                xalign 0.12
                yalign 0.12

    if duel_shrimp_hp <= 0:
        add "dunge icon dead":
            xalign 0.88
            yalign 0.12

    elif duel_shrimp_hp <= 1:
        add "dunge icon half":
            xalign 0.88
            yalign 0.12

    else:
        add "dunge icon full":
            xalign 0.88
            yalign 0.12


screen mantis_rps_screen():

    modal True

    imagebutton:
        idle "jankenpon button rock"
        focus_mask True
        xalign 0.20
        yalign 0.90
        action Return("rock")

    imagebutton:
        idle "jankenpon button scissors"
        focus_mask True
        xalign 0.50
        yalign 0.90
        action Return("scissors")

    imagebutton:
        idle "jankenpon button paper"
        focus_mask True
        xalign 0.80
        yalign 0.90
        action Return("paper")


screen mantis_dodge_screen(boss_choice):

    modal True

    if boss_choice == "rock":
        add "mantis dodge rock"

    elif boss_choice == "paper":
        add "mantis dodge paper"

    else:
        add "mantis dodge scissors"

    if duel_z_taps % 2 == 0:
        add "mantis key idle"
    else:
        add "mantis key smash"

    add "mantis arrow blue"
    add "mantis arrow red"

    if duel_z_taps >= duel_z_target:
        add "mantis bar full"

    elif duel_z_taps >= duel_z_target * 0.78:
        add "mantis bar blue6"

    elif duel_z_taps >= duel_z_target * 0.61:
        add "mantis bar blue5"

    elif duel_z_taps >= duel_z_target * 0.44:
        add "mantis bar blue4"

    elif duel_z_taps >= duel_z_target * 0.28:
        add "mantis bar blue3"

    elif duel_z_taps >= duel_z_target * 0.14:
        add "mantis bar blue2"

    elif duel_z_taps >= duel_z_target * 0.04:
        add "mantis bar blue1"

    else:
        add "mantis bar red"

    key "K_z" action Function(duel_press_z)

    timer 2.2 action Return(
        duel_z_taps >= duel_z_target
    )


label mantis_duel:

    if MANTIS_DUEL_BYPASS:

        # Skip the entire RPS/dodge minigame. No screens are shown, no HP
        # is lost, and there is no lose branch to loop back into - this
        # label simply resolves as an immediate win, exactly like a normal
        # successful duel would, so every caller downstream (mantis_win,
        # chapter2_mantis_done, etc.) still runs untouched.
        $ duel_result = "win"

        return "win"

    hide mc
    hide cory
    hide shrimp

    window hide

    $ duel_fighter = "mc"
    $ duel_player_wins = 0
    $ duel_shrimp_wins = 0

    $ duel_player_hp = 3
    $ duel_shrimp_hp = 3

    $ duel_round = 1
    $ duel_result = None

    $ duel_player_choice = None
    $ duel_shrimp_choice = None
    $ duel_round_result = None

    $ duel_player_history = []

    $ duel_z_taps = 0
    $ duel_z_target = 10
    $ dodge_result = False

    show screen mantis_battle_stage

    while (
        duel_round <= 3
        and duel_player_wins < 2
        and duel_shrimp_wins < 2
        and duel_shrimp_hp > 0
    ):

        call screen mantis_rps_screen
        $ duel_player_choice = _return

        $ duel_player_history.append(duel_player_choice)

        call screen dunge_countdown_screen(3)
        call screen dunge_countdown_screen(2)
        call screen dunge_countdown_screen(1)

        $ duel_shrimp_choice = mantis_ai_pick(duel_player_history)

        $ duel_round_result = dunge_jankenpon_result(
            duel_player_choice,
            duel_shrimp_choice
        )

        call screen dunge_round_reveal(
            duel_player_choice,
            duel_shrimp_choice,
            duel_round_result
        )

        if duel_round_result == "win":

            $ duel_player_wins += 1
            $ duel_shrimp_hp = max(0, duel_shrimp_hp - 1)
            $ duel_round += 1

        elif duel_round_result == "tie":

            $ duel_round += 1

        elif duel_round_result == "lose":

            $ duel_shrimp_wins += 1

            $ duel_z_target = random.randint(9, 12)
            $ duel_z_taps = 0

            call screen mantis_dodge_screen(duel_shrimp_choice)
            $ dodge_result = _return

            if not dodge_result:

                if coal_tar_effective:
                    $ duel_player_hp = max(0, duel_player_hp - 1)

                else:
                    $ duel_player_hp = max(0, duel_player_hp - 2)

            if duel_player_hp <= 0:

                if duel_fighter == "mc":

                    $ duel_fighter = "cory"
                    $ duel_player_hp = 3

                else:

                    $ duel_round = 4

            $ duel_round += 1

    hide screen mantis_battle_stage

    if duel_player_wins >= 2 or duel_shrimp_hp <= 0:

        $ duel_result = "win"

        window auto

        return "win"

    $ duel_result = "lose"

    window auto

    return "lose"