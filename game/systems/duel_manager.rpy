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
default player_choice_history = []
default duel_z_taps = 0
default duel_z_target = 10
default duel_result = None
default coal_tar_effective = False
default dodge_result = False
default duel_is_dodging = False
default duel_boss = "mantis"

default duel_boss_name = "Mantis Shrimp"
default duel_boss_bg = "duel_bg_mantis"
default duel_boss_hp = 3
default duel_boss_max_hp = 3
default duel_boss_low_threshold = 1
default duel_boss_idle_normal = "boss_mantis_idle_normal"
default duel_boss_dmg_normal = "boss_mantis_dmg_normal"
default duel_boss_idle_low = "boss_mantis_idle_low"
default duel_boss_dmg_low = "boss_mantis_dmg_low"
default duel_current_boss_sprite = "boss_mantis_idle_normal"
default empress_current_sprite = "boss_mantis_idle_normal"

define MANTIS_DUEL_BYPASS = False

define AI_COUNTER_CHANCE = 0.35
define AI_COUNTER_ACCURACY = 0.80
define EMPRESS_LOW_HP_THRESHOLD = 1
define DUEL_DEFAULT_LOW_HP_THRESHOLD = 1
define DUEL_COUNTDOWN_SPEED = 0.6

image duel_bg_animated:
    contains:
        "images/jankenpon/Bg1.png"
        pause 1.2
        alpha 0.0
        pause 1.2
        ease 1.2 alpha 1.0
        repeat
    contains:
        "images/jankenpon/Bg2.png"
        alpha 0.0
        ease 1.2 alpha 1.0
        pause 1.2
        alpha 0.0
        pause 1.2
        repeat
    contains:
        "images/jankenpon/Bg3.png"
        alpha 0.0
        pause 1.2
        ease 1.2 alpha 1.0
        pause 1.2
        alpha 0.0
        repeat

image duel_bg_mantis = "duel_bg_animated"
image duel_bg_empress = "duel_bg_animated"
image duel_bg_dunge = "duel_bg_animated"

image empress_idle1 = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_idle2 = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_idle3 = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_idledmg = "images/jankenpon/VS GOBYTETO/TetoDMG.png"
image empress_lowhp = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_lowhp1 = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_lowhp2 = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_lowhp3 = "images/jankenpon/VS GOBYTETO/TetoDefault.png"
image empress_lowhpdmg = "images/jankenpon/VS GOBYTETO/TetoDMG.png"

image empress_idle_normal = "empress_idle1"
image empress_dmg_normal = "empress_idledmg"
image empress_idle_low = "empress_lowhp"
image empress_dmg_low = "empress_lowhpdmg"

image empress_icon_full = "images/jankenpon/VS GOBYTETO/ICON/TetoFull.png"
image empress_icon_half = "images/jankenpon/VS GOBYTETO/ICON/TetoHalf.png"
image empress_icon_one = "images/jankenpon/VS GOBYTETO/ICON/TetoOne.png"
image empress_icon_dead = "images/jankenpon/VS GOBYTETO/ICON/TetoDead.png"

image empress dodge bg = "images/jankenpon/VS GOBYTETO/Dodge/BgDodge.png"
image empress dodge = "images/jankenpon/VS GOBYTETO/Dodge/TetoDodge.png"
image empress dodge vfx = "images/jankenpon/VS GOBYTETO/Dodge/Dodge.png"

image boss_mantis_idle_normal = "images/jankenpon/Idle1.png"

image boss_mantis_dmg_normal = "images/jankenpon/IdleDMG.png"

image boss_mantis_idle_low = "images/jankenpon/LowHP.png"

image boss_mantis_dmg_low = "images/jankenpon/LowHPDMG.png"

image boss_mantis_dmg_low = "images/jankenpon/LowHPDMG.png"

image duel_boss_mantis = "boss_mantis_idle_normal"
image duel_boss_mantis_damaged = "boss_mantis_idle_low"
image duel_boss_empress = "boss_mantis_idle_normal"
image duel_boss_empress_damaged = "boss_mantis_idle_low"

image boss_dunge_idle_normal = "images/jankenpon/Idle1.png"
image boss_dunge_dmg_normal = "images/jankenpon/IdleDMG.png"
image boss_dunge_idle_low = "images/jankenpon/LowHP1.png"
image boss_dunge_dmg_low = "images/jankenpon/LowHPDMG.png"

image duel_boss_dunge = "boss_dunge_idle_normal"
image duel_boss_dunge_damaged = "boss_dunge_idle_low"

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

image mantis punch hit:
    "images/jankenpon/Paper/PaperImpact1.png"
    0.1
    "images/jankenpon/Paper/PaperImpact2.png"
    0.1
    Null()

image mantis rock hit:
    "images/jankenpon/Rock/RockImpact1.png"
    0.1
    "images/jankenpon/Rock/RockImpact2.png"
    0.1
    Null()

image mantis scissor hit:
    "images/jankenpon/Scissor/ScissorImpact1.png"
    0.1
    "images/jankenpon/Scissor/ScissorImpact2.png"
    0.1
    Null()

screen mantis_punch_effect(boss_choice="paper"):
    zorder 100
    if boss_choice == "rock":
        add "mantis rock hit"
    elif boss_choice in ("scissor", "scissors"):
        add "mantis scissor hit"
    else:
        add "mantis punch hit"
    timer 0.2 action Return()

transform mantis_incoming_attack:
    zoom 0.5 align (0.5, 0.5) alpha 0.0
    parallel:
        easein 2.6 zoom 1.0
    parallel:
        easein 0.2 alpha 1.0

init python:

    import random

    DUEL_BOSS_REGISTRY = {
        "empress": {
            "name": "Crustacean Empress VIII",
            "bg": "duel_bg_empress",
            "hp": 3,
            "low_hp_threshold": 1,
            "idle_normal": "empress_idle_normal",
            "dmg_normal": "empress_dmg_normal",
            "idle_low": "empress_idle_low",
            "dmg_low": "empress_dmg_low",
            "weights_normal": {"rock": 0.33, "paper": 0.34, "scissors": 0.33},
            "weights_enraged": {"rock": 0.35, "paper": 0.35, "scissors": 0.30},
            "dodge_target_range": (8, 10),
            "dodge_tar_range": (6, 8),
            "ai_counter_chance": 0.25,
            "ai_counter_accuracy": 0.60,
            "has_full_assets": True,
        },
        "mantis": {
            "name": "Mantis Shrimp",
            "bg": "duel_bg_mantis",
            "hp": 3,
            "low_hp_threshold": 1,
            "idle_normal": "boss_mantis_idle_normal",
            "dmg_normal": "boss_mantis_dmg_normal",
            "idle_low": "boss_mantis_idle_low",
            "dmg_low": "boss_mantis_dmg_low",
            "weights_normal": {"rock": 0.45, "paper": 0.25, "scissors": 0.30},
            "weights_enraged": {"rock": 0.55, "paper": 0.20, "scissors": 0.25},
            "dodge_target_range": (7, 9),
            "dodge_tar_range": (5, 7),
            "ai_counter_chance": 0.25,
            "ai_counter_accuracy": 0.60,
            "has_full_assets": True,
        },
        "dunge": {
            "name": "Dunge Crab",
            "bg": "duel_bg_dunge",
            "hp": 3,
            "low_hp_threshold": 1,
            "idle_normal": "boss_dunge_idle_normal",
            "dmg_normal": "boss_dunge_dmg_normal",
            "idle_low": "boss_dunge_idle_low",
            "dmg_low": "boss_dunge_dmg_low",
            "weights_normal": {"rock": 0.30, "paper": 0.25, "scissors": 0.45},
            "weights_enraged": {"rock": 0.50, "paper": 0.20, "scissors": 0.30},
            "dodge_target_range": (6, 8),
            "dodge_tar_range": (5, 7),
            "ai_counter_chance": 0.25,
            "ai_counter_accuracy": 0.60,
            "has_full_assets": False,
        },
        "banished": {
            "name": "The Banished One",
            "bg": "duel_bg_mantis",
            "hp": 3,
            "low_hp_threshold": 1,
            "idle_normal": "boss_mantis_idle_normal",
            "dmg_normal": "boss_mantis_dmg_normal",
            "idle_low": "boss_mantis_idle_low",
            "dmg_low": "boss_mantis_dmg_low",
            "weights_normal": {"rock": 0.35, "paper": 0.35, "scissors": 0.30},
            "weights_enraged": {"rock": 0.40, "paper": 0.35, "scissors": 0.25},
            "dodge_target_range": (7, 9),
            "dodge_tar_range": (5, 7),
            "ai_counter_chance": 0.30,
            "ai_counter_accuracy": 0.65,
            "has_full_assets": True,
        }
    }

    def duel_press_z():
        if store.duel_z_taps < store.duel_z_target:
            store.duel_z_taps += 1

    def duel_ai_pick(history, boss="mantis"):
        moves = ["rock", "paper", "scissors"]
        counter_map = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        loses_to_map = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        cleaned_history = []
        for m in (history or []):
            if m in ("scissor", "scissors"):
                cleaned_history.append("scissors")
            else:
                cleaned_history.append(str(m).lower())

        cfg = DUEL_BOSS_REGISTRY.get(boss, DUEL_BOSS_REGISTRY.get("mantis", {}))
        boss_hp = getattr(store, "duel_boss_hp", 3)
        low_threshold = cfg.get("low_hp_threshold", 1)
        is_low = boss_hp <= low_threshold

        weights_cfg = cfg.get("weights_enraged" if is_low else "weights_normal", {})
        w_rock = weights_cfg.get("rock", 0.334)
        w_paper = weights_cfg.get("paper", 0.333)
        w_scissors = weights_cfg.get("scissors", 0.333)

        def weighted_pick():
            r = random.random()
            if r < w_rock:
                return "rock"
            elif r < w_rock + w_paper:
                return "paper"
            return "scissors"

        if not cleaned_history or len(cleaned_history) < 2:
            return weighted_pick()

        last_move = cleaned_history[-1]
        prev_move = cleaned_history[-2]

        if last_move == prev_move:
            roll = random.random()
            if roll < 0.40:
                return last_move
            elif roll < 0.75:
                return loses_to_map.get(last_move, "rock")
            else:
                return counter_map.get(last_move, "scissors")

        if random.random() < 0.65:
            return weighted_pick()
        else:
            alternatives = [m for m in moves if m != last_move]
            predicted = random.choice(alternatives)
            return counter_map[predicted]

    def mantis_ai_pick(history):
        return duel_ai_pick(history, getattr(store, "duel_boss", "mantis"))

    import math
    def smooth_spark_transform(trans, st, at):
        target_progress = min(1.0, float(store.duel_z_taps) / max(1.0, float(store.duel_z_target)))
        target_offset = (target_progress * 1687.0) - 447.0

        if not hasattr(trans, 'current_offset') or (store.duel_z_taps == 0 and trans.current_offset > -440.0):
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

screen duel_battle_stage():

    add duel_boss_bg

    if not duel_is_dodging:
        add duel_current_boss_sprite:
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

        if duel_boss == "empress":
            if duel_shrimp_hp <= 0:
                add "empress_icon_dead":
                    xalign 0.88
                    yalign 0.12
            elif duel_shrimp_hp == 1:
                add "empress_icon_one":
                    xalign 0.88
                    yalign 0.12
            elif duel_shrimp_hp == 2:
                add "empress_icon_half":
                    xalign 0.88
                    yalign 0.12
            else:
                add "empress_icon_full":
                    xalign 0.88
                    yalign 0.12
        else:
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

screen mantis_battle_stage():
    use duel_battle_stage

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

screen mantis_spamz_screen(player_choice, boss_choice="paper"):
    modal True

    if duel_boss == "empress":

        add "empress dodge bg"

        add "empress dodge"

        add "empress dodge vfx"

    else:

        if player_choice == "rock":
            add "mantis dodge rock"
        elif player_choice == "paper":
            add "mantis dodge paper"
        else:
            add "mantis dodge scissors"

        if boss_choice == "rock":
            add "images/jankenpon/Rock/Rock.png" at mantis_incoming_attack
        elif boss_choice in ("scissor", "scissors"):
            add "images/jankenpon/Scissor/Scissor.png" at mantis_incoming_attack
        else:
            add "images/jankenpon/Paper/Paper.png" at mantis_incoming_attack

    if duel_z_taps % 2 == 0:
        add "mantis key idle"
    else:
        add "mantis key smash"

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

    add "mantis arrow blue" at smooth_spark
    add "mantis arrow red" at smooth_spark

    frame:
        xalign 0.5
        yalign 0.08
        padding (20, 10)
        text "SPAM Z / CLICK!  [duel_z_taps] / [duel_z_target]" size 36

    key "K_z" action Function(duel_press_z)
    key "K_SPACE" action Function(duel_press_z)
    key "K_RETURN" action Function(duel_press_z)
    key "K_KP_ENTER" action Function(duel_press_z)
    key "button_select" action Function(duel_press_z)

    button:
        xfill True
        yfill True
        action Function(duel_press_z)
        background None
        focus_mask None

    if duel_z_taps >= duel_z_target:
        timer 0.15 action Return(True)
    else:
        timer 2.6 action Return(False)

label mantis_duel:
    call run_duel("mantis")
    return _return

label empress_duel:
    call run_duel("empress")
    return _return

label dunge_duel:
    call run_duel("dunge")
    return _return

label banished_duel:
    call run_duel("banished")
    return _return

label run_duel(boss_target="mantis", custom_hp=None, custom_threshold=None):

    if MANTIS_DUEL_BYPASS:
        $ duel_result = "win"
        $ dunge_battle_result = "victory"
        return "win"

    hide mc
    hide cory
    hide shrimp
    hide dunge
    hide empress

    window hide

    $ duel_boss = boss_target if boss_target else getattr(store, "duel_boss", "mantis")
    $ _bcfg = DUEL_BOSS_REGISTRY.get(duel_boss, DUEL_BOSS_REGISTRY["mantis"])
    $ duel_boss_name = _bcfg["name"]
    $ duel_boss_bg = _bcfg["bg"]
    $ duel_boss_hp = custom_hp if custom_hp is not None else _bcfg["hp"]
    $ duel_boss_max_hp = duel_boss_hp
    $ duel_boss_low_threshold = custom_threshold if custom_threshold is not None else _bcfg["low_hp_threshold"]
    $ duel_boss_idle_normal = _bcfg["idle_normal"]
    $ duel_boss_dmg_normal = _bcfg["dmg_normal"]
    $ duel_boss_idle_low = _bcfg["idle_low"]
    $ duel_boss_dmg_low = _bcfg["dmg_low"]
    $ duel_current_boss_sprite = duel_boss_idle_normal
    $ empress_current_sprite = duel_current_boss_sprite
    $ duel_shrimp_hp = duel_boss_hp

    $ duel_player_wins = 0
    $ duel_shrimp_wins = 0
    $ duel_player_hp = 3
    $ duel_round = 1
    $ duel_result = None

    $ duel_player_choice = None
    $ duel_shrimp_choice = None
    $ duel_round_result = None

    $ duel_player_history = []
    $ player_choice_history = []

    $ duel_z_taps = 0
    $ duel_z_target = 10
    $ dodge_result = False

    if duel_fighter is None:
        $ duel_fighter = "mc"

    python:
        renpy.start_predict(
            "images/jankenpon/Idle1.png",
            "images/jankenpon/Idle2.png",
            "images/jankenpon/Idle3.png",
            "images/jankenpon/IdleDMG.png",
            "images/jankenpon/LowHP.png",
            "images/jankenpon/LowHP1.png",
            "images/jankenpon/LowHP2.png",
            "images/jankenpon/LowHP3.png",
            "images/jankenpon/LowHPDMG.png",
            "images/jankenpon/Button Rock Paper Scissor/Rock.png",
            "images/jankenpon/Button Rock Paper Scissor/Paper.png",
            "images/jankenpon/Button Rock Paper Scissor/Scissor_.png",
            "images/jankenpon/Button Rock Paper Scissor/CRock.png",
            "images/jankenpon/Button Rock Paper Scissor/CPaper.png",
            "images/jankenpon/Button Rock Paper Scissor/CScissor.png",
            "images/jankenpon/Button Rock Paper Scissor/SRock.png",
            "images/jankenpon/Button Rock Paper Scissor/SPaper.png",
            "images/jankenpon/Button Rock Paper Scissor/SScissor.png",
            "images/jankenpon/Button Rock Paper Scissor/MRock.png",
            "images/jankenpon/Button Rock Paper Scissor/MPaper.png",
            "images/jankenpon/Button Rock Paper Scissor/MScissor.png",
            "images/jankenpon/Win, Lose, Draw/Win.png",
            "images/jankenpon/Win, Lose, Draw/Lose.png",
            "images/jankenpon/Win, Lose, Draw/Draw_.png",
            "images/jankenpon/Bg1.png",
            "images/jankenpon/Bg2.png",
            "images/jankenpon/Bg3.png"
        )

    show screen duel_battle_stage

    while (
        duel_player_hp > 0
        and duel_boss_hp > 0
    ):

        call screen mantis_rps_screen
        $ duel_player_choice = _return

        call screen dunge_countdown_screen(3, count_delay=DUEL_COUNTDOWN_SPEED)
        call screen dunge_countdown_screen(2, count_delay=DUEL_COUNTDOWN_SPEED)
        call screen dunge_countdown_screen(1, count_delay=DUEL_COUNTDOWN_SPEED)

        $ duel_shrimp_choice = duel_ai_pick(player_choice_history, duel_boss)
        $ player_choice_history.append(duel_player_choice)
        $ duel_player_history.append(duel_player_choice)

        $ duel_round_result = dunge_jankenpon_result(
            duel_player_choice,
            duel_shrimp_choice
        )

        if duel_round_result == "win":
            if duel_boss_hp <= duel_boss_low_threshold:
                $ duel_current_boss_sprite = duel_boss_dmg_low
                $ empress_current_sprite = duel_boss_dmg_low
            else:
                $ duel_current_boss_sprite = duel_boss_dmg_normal
                $ empress_current_sprite = duel_boss_dmg_normal
            $ renpy.restart_interaction()

        call screen dunge_round_reveal(
            duel_player_choice,
            duel_shrimp_choice,
            duel_round_result
        )

        if duel_round_result == "lose":
            $ _bcfg = DUEL_BOSS_REGISTRY.get(duel_boss, DUEL_BOSS_REGISTRY["mantis"])
            $ _tar_range = _bcfg.get("dodge_tar_range" if coal_tar_effective else "dodge_target_range", (7, 9))
            $ duel_z_target = random.randint(_tar_range[0], _tar_range[1])
            $ duel_z_taps = 0

            $ duel_is_dodging = True
            call screen mantis_spamz_screen(duel_player_choice, duel_shrimp_choice)
            $ dodge_result = _return   # True = spam success, False = spam fail
            $ duel_is_dodging = False

        if duel_round_result == "win":
            $ duel_player_wins += 1
            $ duel_round += 1
            $ duel_boss_hp = max(0, duel_boss_hp - 1)
            $ duel_shrimp_hp = duel_boss_hp
            if duel_boss_hp <= duel_boss_low_threshold:
                $ duel_current_boss_sprite = duel_boss_idle_low
                $ empress_current_sprite = duel_boss_idle_low
            else:
                $ duel_current_boss_sprite = duel_boss_idle_normal
                $ empress_current_sprite = duel_boss_idle_normal
            $ renpy.restart_interaction()

        elif duel_round_result == "lose":
            if not dodge_result:
                call screen mantis_punch_effect(duel_shrimp_choice)
                $ duel_player_hp = max(0, duel_player_hp - 1)
                $ duel_shrimp_wins += 1
                $ duel_round += 1
            else:
                pass

    hide screen duel_battle_stage
    hide screen mantis_battle_stage

    python:
        renpy.stop_predict(
            "images/jankenpon/Idle1.png",
            "images/jankenpon/Idle2.png",
            "images/jankenpon/Idle3.png",
            "images/jankenpon/IdleDMG.png",
            "images/jankenpon/LowHP.png",
            "images/jankenpon/LowHP1.png",
            "images/jankenpon/LowHP2.png",
            "images/jankenpon/LowHP3.png",
            "images/jankenpon/LowHPDMG.png"
        )

    if duel_boss_hp <= 0 or (duel_player_hp > 0 and duel_boss_hp < duel_boss_max_hp):
        $ duel_result = "win"
        $ dunge_battle_result = "victory"
        window auto
        return "win"

    $ duel_result = "lose"
    $ dunge_battle_result = "defeat"
    window auto
    return "lose"

label empress_on_damage_taken:
    call boss_on_damage_taken
    return

label empress_take_damage:
    call boss_on_damage_taken
    return

label boss_on_damage_taken:
    $ was_low = (duel_boss_hp <= duel_boss_low_threshold)
    $ duel_boss_hp = max(0, duel_boss_hp - 1)
    $ duel_shrimp_hp = duel_boss_hp

    if was_low:
        $ duel_current_boss_sprite = duel_boss_dmg_low
        $ empress_current_sprite = duel_boss_dmg_low
        $ renpy.restart_interaction()
        $ renpy.pause(0.4, hard=True)
        $ duel_current_boss_sprite = duel_boss_idle_low
        $ empress_current_sprite = duel_boss_idle_low
        $ renpy.restart_interaction()
    else:
        $ duel_current_boss_sprite = duel_boss_dmg_normal
        $ empress_current_sprite = duel_boss_dmg_normal
        $ renpy.restart_interaction()
        $ renpy.pause(0.4, hard=True)
        if duel_boss_hp <= duel_boss_low_threshold:
            $ duel_current_boss_sprite = duel_boss_idle_low
            $ empress_current_sprite = duel_boss_idle_low
        else:
            $ duel_current_boss_sprite = duel_boss_idle_normal
            $ empress_current_sprite = duel_boss_idle_normal
        $ renpy.restart_interaction()

    return
