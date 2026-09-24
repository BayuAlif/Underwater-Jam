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
default duel_is_dodging = False

# ---------------------------------------------------------------------------
# TEMPORARY DEV BYPASS - Mantis Shrimp boss fight (Chapter 2)
# Set to False to restore the real minigame once it's ready to be worked on
# again. While True, "label mantis_duel" below skips the whole RPS/spam-Z
# minigame (and therefore the "Try again? / Return to Hub" lose-loop) and
# always resolves as a win, so the existing post-duel story/flags still run
# normally.
# ---------------------------------------------------------------------------
define MANTIS_DUEL_BYPASS = False


# ---------------------------------------------------------------------------
# ASSETS
# ---------------------------------------------------------------------------

# Dodge/spam-Z background images (still used by mantis_spamz_screen below)
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

# Punch impact animation
image mantis punch hit:
    "images/jankenpon/Paper/PaperImpact1.png"
    0.1
    "images/jankenpon/Paper/PaperImpact2.png"
    0.1
    Null()

screen mantis_punch_effect():
    zorder 100
    add "mantis punch hit"
    timer 0.2 action Return()

transform mantis_incoming_attack:
    zoom 0.5 align (0.5, 0.5) alpha 0.0
    parallel:
        easein 2.2 zoom 1.0
    parallel:
        easein 0.2 alpha 1.0


# ---------------------------------------------------------------------------
# PYTHON HELPERS
# ---------------------------------------------------------------------------

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

    import math
    def smooth_spark_transform(trans, st, at):
        target_progress = min(1.0, float(store.duel_z_taps) / max(1.0, float(store.duel_z_target)))
        target_offset = (target_progress * 1687.0) - 447.0
        
        if not hasattr(trans, 'current_offset'):
            trans.current_offset = -447.0
            trans.last_st = st
            
        dt = st - trans.last_st
        trans.last_st = st
        
        if dt > 0.1:
            dt = 0.1
            
        diff = target_offset - trans.current_offset
        trans.current_offset += diff * (1.0 - math.exp(-15.0 * dt))
        
        trans.xoffset = int(trans.current_offset)
        return 0.0

transform smooth_spark:
    function smooth_spark_transform


# ---------------------------------------------------------------------------
# BATTLE STAGE (HP display overlay — shown throughout the fight)
# ---------------------------------------------------------------------------

screen mantis_battle_stage():

    add "dunge battle bg"

    if not duel_is_dodging:
        if duel_shrimp_hp <= 1:
            add "dunge damaged":
                xalign 0.5
                yalign 0.5
        else:
            add "dunge idle":
                xalign 0.5
                yalign 0.5

    if not duel_is_dodging:

        if duel_fighter == "mc":

            if duel_player_hp <= 0:
                add "mc icon dead":
                    xalign 0.12
                    yalign 0.12

            elif duel_player_hp == 1:
                add "mc icon one":
                    xalign 0.12
                    yalign 0.12

            elif duel_player_hp == 2:
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
                add "cory icon one":
                    xalign 0.12
                    yalign 0.12

            elif duel_player_hp == 2:
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

        elif duel_shrimp_hp == 1:
            add "dunge icon one":
                xalign 0.88
                yalign 0.12

        elif duel_shrimp_hp == 2:
            add "dunge icon half":
                xalign 0.88
                yalign 0.12

        else:
            add "dunge icon full":
                xalign 0.88
                yalign 0.12


# ---------------------------------------------------------------------------
# RPS CHOICE SCREEN
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# SPAM-Z MINIGAME SCREEN
# This is the ONE minigame used for every round, regardless of RPS choice.
# It shows the relevant background art for whichever RPS option the player
# picked, then waits for Z-key spam until the timer expires.
#   Returns True  → player reached the target (spam success)
#   Returns False → timer ran out before target reached (spam fail)
# ---------------------------------------------------------------------------

screen mantis_spamz_screen(player_choice):

    modal True

    # Background art based on player's RPS choice — purely cosmetic.
    if player_choice == "rock":
        add "mantis dodge rock"
    elif player_choice == "paper":
        add "mantis dodge paper"
    else:
        add "mantis dodge scissors"

    # The incoming punch slowly scales up over the 2.2s timer!
    add "images/jankenpon/Paper/Paper.png" at mantis_incoming_attack

    # Key animation (toggles on each tap)
    if duel_z_taps % 2 == 0:
        add "mantis key idle"
    else:
        add "mantis key smash"

    # Progress bar (rendered before arrows so arrows appear on top)
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

    # Arrows/spark — added last so they render in front of the bar
    add "mantis arrow blue" at smooth_spark
    add "mantis arrow red" at smooth_spark

    # Progress label
    frame:
        xalign 0.5
        yalign 0.08
        padding (20, 10)
        text "SPAM Z!  [duel_z_taps] / [duel_z_target]" size 36

    # Z key binding — only active while this screen is shown
    key "K_z" action Function(duel_press_z)

    # Timer: 2.2 s — returns True if target reached, False otherwise
    timer 2.2 action Return(
        duel_z_taps >= duel_z_target
    )


# ---------------------------------------------------------------------------
# MANTIS DUEL LABEL
# Active flow:
#   mantis_start_duel → call mantis_duel
#
# Round structure:
#   1. Player picks RPS
#   2. Countdown
#   3. Boss picks RPS
#   4. RPS result revealed (who has advantage)
#   5. SPAM-Z minigame (same screen for ALL RPS choices)
#   6. Combine RPS result + spam result to determine round outcome:
#      - RPS win  + spam success → deal 1 HP damage to Mantis
#      - RPS win  + spam fail    → tie (no damage either way)
#      - RPS tie  + spam success → tie
#      - RPS tie  + spam fail    → tie
#      - RPS lose + spam success → player blocks (no HP loss)
#      - RPS lose + spam fail    → player takes damage (coal_tar halves it)
# ---------------------------------------------------------------------------

label mantis_duel:

    if MANTIS_DUEL_BYPASS:

        # Skip the entire RPS/spam-Z minigame. No screens are shown, no HP
        # is lost, and there is no lose branch to loop back into — this
        # label simply resolves as an immediate win, exactly like a normal
        # successful duel would, so every caller downstream (mantis_win,
        # chapter2_mantis_done, etc.) still runs untouched.
        $ duel_result = "win"

        return "win"

    hide mc
    hide cory
    hide shrimp

    window hide

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

        # ── Step 1: Player picks RPS ────────────────────────────────────────
        call screen mantis_rps_screen
        $ duel_player_choice = _return

        $ duel_player_history.append(duel_player_choice)

        # ── Step 2: Countdown ───────────────────────────────────────────────
        call screen dunge_countdown_screen(3)
        call screen dunge_countdown_screen(2)
        call screen dunge_countdown_screen(1)

        # ── Step 3: Boss picks ──────────────────────────────────────────────
        $ duel_shrimp_choice = mantis_ai_pick(duel_player_history)

        # ── Step 4: RPS result reveal ───────────────────────────────────────
        $ duel_round_result = dunge_jankenpon_result(
            duel_player_choice,
            duel_shrimp_choice
        )

        call screen dunge_round_reveal(
            duel_player_choice,
            duel_shrimp_choice,
            duel_round_result
        )

        # ── Step 5: Spam-Z minigame (only on lose) ────────────────────────
        if duel_round_result == "lose":
            $ duel_z_target = random.randint(9, 12)
            $ duel_z_taps = 0

            $ duel_is_dodging = True
            call screen mantis_spamz_screen(duel_player_choice)
            $ dodge_result = _return   # True = spam success, False = spam fail
            $ duel_is_dodging = False

        # ── Step 6: Apply outcome based on RPS result + spam result ─────────
        if duel_round_result == "win":
            # Player won RPS → deal damage to Mantis automatically!
            $ duel_player_wins += 1
            $ duel_shrimp_hp = max(0, duel_shrimp_hp - 1)

        elif duel_round_result == "lose":

            if not dodge_result:
                # Player lost RPS and failed spam → take damage
                call screen mantis_punch_effect

                # Player lost RPS and failed spam → take -1 HP
                $ duel_player_hp = max(0, duel_player_hp - 1)

                if duel_player_hp <= 0:

                    if duel_fighter == "mc":
                        $ duel_fighter = "cory"
                        $ duel_player_hp = 3
                    else:
                        $ duel_round = 4   # force loop exit

            else:
                # Player lost RPS but succeeded spam → blocked the attack
                $ duel_shrimp_wins += 1   # cost: Mantis still gets the round point

        # tie: no effect either way

        $ duel_round += 1

    hide screen mantis_battle_stage

    if duel_player_wins >= 2 or duel_shrimp_hp <= 0:

        $ duel_result = "win"

        window auto

        return "win"

    $ duel_result = "lose"

    window auto

    return "lose"