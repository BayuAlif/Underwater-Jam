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

default duel_boss_stance_name = ""
default duel_boss_stance_hint = ""
default duel_boss_telegraph = ""
default duel_boss_planned_move = "rock"
default duel_boss_is_feint = False
default duel_match_history = []

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

image boss_dunge_idle_normal = "images/jankenpon/DUNGE/DungeIdleNormal.png"
image boss_dunge_dmg_normal = "images/jankenpon/DUNGE/DungeDmgNormal.png"
image boss_dunge_idle_low = "images/jankenpon/DUNGE/DungeIdleLow.png"
image boss_dunge_dmg_low = "images/jankenpon/DUNGE/DungeDmgLow.png"

image duel_boss_dunge = "boss_dunge_idle_normal"
image duel_boss_dunge_damaged = "boss_dunge_idle_low"

image mantis_icon_full = "images/jankenpon/ICON/ScyFull.png"
image mantis_icon_half = "images/jankenpon/ICON/ScyHalf.png"
image mantis_icon_one = "images/jankenpon/ICON/ScyOne.png"
image mantis_icon_dead = "images/jankenpon/ICON/ScyDead.png"

image dunge_icon_full = "images/jankenpon/ICON/DungeFull.png"
image dunge_icon_half = "images/jankenpon/ICON/DungeHalf.png"
image dunge_icon_one = "images/jankenpon/ICON/DungeOne.png"
image dunge_icon_dead = "images/jankenpon/ICON/DungeDead.png"

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
            "has_full_assets": True,
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
            renpy.sound.play("audio/sfx/click.mp3")

    def get_battle_tracks():
        tracks = []
        try:
            for f in renpy.list_files():
                if f.startswith("audio/bgm/battle/") and f.lower().endswith((".ogg", ".wav", ".mp3", ".opus")):
                    tracks.append(f)
        except Exception:
            pass

        if not tracks:
            import os
            battle_dir = os.path.join(renpy.config.gamedir, "audio", "bgm", "battle")
            if os.path.isdir(battle_dir):
                for fname in os.listdir(battle_dir):
                    if fname.lower().endswith((".ogg", ".wav", ".mp3", ".opus")):
                        tracks.append("audio/bgm/battle/" + fname)

        if not tracks:
            tracks = [
                "audio/bgm/battle/a_battle.ogg",
                "audio/bgm/battle/jankenpon.ogg",
                "audio/bgm/battle/mysterious golden looking.ogg"
            ]
        return tracks

    def get_random_battle_music():
        tracks = get_battle_tracks()
        if tracks:
            return random.choice(tracks)
        return None

    def play_random_battle_music(volume=0.5):
        selected = get_random_battle_music()
        if selected:
            renpy.music.play(selected, channel="music", loop=True, if_changed=True, relative_volume=volume)
            return selected
        return None

    DUEL_STRATEGY_DATA = {
        "mantis": {
            "name": "Mantis Shrimp",
            "stances": {
                "rock": {
                    "name": "Heavy Hammer Stance",
                    "quotes": [
                        "Feel the crushing impact of my hammer claws! KAKAKA!",
                        "A direct supersonic punch shatters all resistance!",
                        "Prepare yourself! Here comes my heavyweight strike!"
                    ],
                    "hint": "Winding up a crushing blunt strike! (Favors Rock - Counter with Paper)",
                    "weights": {"rock": 0.80, "scissors": 0.10, "paper": 0.10}
                },
                "scissors": {
                    "name": "Pincer Snap Stance",
                    "quotes": [
                        "Too slow! I'll snip your fins before you can even blink!",
                        "My claws can cut through steel! Watch your edges!",
                        "Speed and sharpness! Let's see you dodge this snip!"
                    ],
                    "hint": "Cocking claws for a piercing snip! (Favors Scissors - Counter with Rock)",
                    "weights": {"scissors": 0.80, "rock": 0.10, "paper": 0.10}
                },
                "paper": {
                    "name": "Current Sweep Stance",
                    "quotes": [
                        "A true warrior defends from every angle! Come at me!",
                        "My domain covers the entire current! Nowhere to slip past!",
                        "Sweeping the battlefield! Let the waves swallow you!"
                    ],
                    "hint": "Sweeping outward to parry and envelop! (Favors Paper - Counter with Scissors)",
                    "weights": {"paper": 0.80, "scissors": 0.10, "rock": 0.10}
                }
            },
            "anti_spam_quote": "Kakaka! Trying the same trick twice?! I saw that coming!",
            "anti_spam_hint": "Anti-Spam: Mantis counters your repeated move!",
            "enrage_feint_quote": "GAAHH! Don't look down on me! You think you can read my punch?!",
            "enrage_feint_hint": "[FEINT ALERT] Mantis feints a heavy punch to bait Paper! (Favors Scissors)",
        },
        "dunge": {
            "name": "Dunge Crab",
            "stances": {
                "rock": {
                    "name": "Iron Shell Stance",
                    "quotes": [
                        "Hah! Good luck scratchin' this thick shell, guppy!",
                        "Nothin' in these waters breaks through solid stone!",
                        "Bunker down! Let's see ya bounce right off my carapace!"
                    ],
                    "hint": "Hunkering behind dense armored shell! (Favors Rock - Counter with Paper)",
                    "weights": {"rock": 0.82, "scissors": 0.09, "paper": 0.09}
                },
                "scissors": {
                    "name": "Razor Vise Stance",
                    "quotes": [
                        "Snip snip! One pinch and yer fresh fins are mine!",
                        "These pincers were made for crunchin' bones!",
                        "Keep yer distance if ya don't wanna get clipped in half!"
                    ],
                    "hint": "Snapping iron pincers forward! (Favors Scissors - Counter with Rock)",
                    "weights": {"scissors": 0.82, "rock": 0.09, "paper": 0.09}
                },
                "paper": {
                    "name": "Silt Cloak Stance",
                    "quotes": [
                        "Kickin' up sand! Can't hit what ya can't see, kid!",
                        "Blanketin' the whole seabed! Try finding an opening in this!",
                        "A smokescreen of mud and silt! Yer trapped!"
                    ],
                    "hint": "Spreading a wide shroud of sand! (Favors Paper - Counter with Scissors)",
                    "weights": {"paper": 0.82, "scissors": 0.09, "rock": 0.09}
                }
            },
            "anti_spam_quote": "Mane, you're predictable! Ain't no way that works twice on an old crab!",
            "anti_spam_hint": "Anti-Spam: Crab blocks and counters your repeated move!",
            "enrage_feint_quote": "Tch... yer hits sting like jellyfish! Time for a dirty trick!",
            "enrage_feint_hint": "[FEINT ALERT] Crab fakes a defensive shell to bait Paper! (Favors Scissors)",
        },
        "empress": {
            "name": "Crustacean Empress VIII",
            "stances": {
                "scissors": {
                    "name": "Imperial Execution Stance",
                    "quotes": [
                        "Your insubordination shall be severed here and now.",
                        "Bow your head before the royal guillotine.",
                        "A single decree is enough to slice away your defiance."
                    ],
                    "hint": "Aiming for a swift royal execution! (Favors Scissors - Counter with Rock)",
                    "weights": {"scissors": 0.82, "rock": 0.09, "paper": 0.09}
                },
                "rock": {
                    "name": "Monarch's Mountain Stance",
                    "quotes": [
                        "The imperial throne is an immovable mountain. You cannot shake it.",
                        "Crush beneath the royal weight of my empire!",
                        "Absolute authority cannot be penetrated by petty rebels."
                    ],
                    "hint": "Immovable imperial fortress! (Favors Rock - Counter with Paper)",
                    "weights": {"rock": 0.82, "scissors": 0.09, "paper": 0.09}
                },
                "paper": {
                    "name": "Royal Decree Stance",
                    "quotes": [
                        "My sovereign will envelops the entire ocean.",
                        "A grand net leaves no commoner an escape.",
                        "You struggle within the palm of my kingdom."
                    ],
                    "hint": "Unfurling an all-encompassing royal decree! (Favors Paper - Counter with Scissors)",
                    "weights": {"paper": 0.82, "scissors": 0.09, "rock": 0.09}
                }
            },
            "anti_spam_quote": "How delightfully predictable! Did you think mere repetition could topple an Empress?!",
            "anti_spam_hint": "Anti-Spam: The Empress punishes your repeated move with absolute precision!",
            "enrage_feint_quote": "You insolent worm! I see through your meager counter-tactics!",
            "enrage_feint_hint": "[ROYAL FEINT] The Empress anticipates your counter and feints to trap you!",
        },
        "banished": {
            "name": "The Banished One",
            "stances": {
                "rock": {
                    "name": "Abyssal Crush Stance",
                    "quotes": [
                        "The crushing pressure of the depths shall shatter you...",
                        "A mountain of sunken stones bears down upon your soul...",
                        "Drown beneath the weight of forgotten darkness..."
                    ],
                    "hint": "Gathering heavy crushing pressure! (Favors Rock - Counter with Paper)",
                    "weights": {"rock": 0.80, "scissors": 0.10, "paper": 0.10}
                },
                "scissors": {
                    "name": "Shadow Rend Stance",
                    "quotes": [
                        "Torn to shreds in the perpetual night...",
                        "Claws of shadow slice through the faint glimmer of your hope...",
                        "Bleed into the abyss..."
                    ],
                    "hint": "Sharpening lethal shadow claws! (Favors Scissors - Counter with Rock)",
                    "weights": {"scissors": 0.80, "rock": 0.10, "paper": 0.10}
                },
                "paper": {
                    "name": "Void Shroud Stance",
                    "quotes": [
                        "The endless void engulfs all light...",
                        "Suffocate within the black shroud of the deep...",
                        "There is no boundary where the abyss ends..."
                    ],
                    "hint": "Enfolding the arena in suffocating void! (Favors Paper - Counter with Scissors)",
                    "weights": {"paper": 0.80, "scissors": 0.10, "rock": 0.10}
                }
            },
            "anti_spam_quote": "Futility repeats itself... your habits are laid bare...",
            "anti_spam_hint": "Anti-Spam: The abyss consumes repeated techniques!",
            "enrage_feint_quote": "You think the dark can be anticipated?! Fall into the trap...",
            "enrage_feint_hint": "[ABYSSAL FEINT] Shadows shift deceptively to counter your expected read!",
        }
    }

    def duel_prepare_round_strategy(boss=None):
        b_key = boss if boss else getattr(store, "duel_boss", "mantis")
        b_data = DUEL_STRATEGY_DATA.get(b_key, DUEL_STRATEGY_DATA["mantis"])
        b_cfg = DUEL_BOSS_REGISTRY.get(b_key, {})
        b_hp = getattr(store, "duel_boss_hp", 3)
        low_hp = b_hp <= b_cfg.get("low_hp_threshold", 1)

        history = getattr(store, "player_choice_history", [])
        cleaned_history = []
        for m in (history or []):
            if m in ("scissor", "scissors"):
                cleaned_history.append("scissors")
            else:
                cleaned_history.append(str(m).lower())

        counter_map = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        beats_map = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        # 1. Anti-Spam Check: Did player play the exact same move twice in a row?
        if len(cleaned_history) >= 2 and cleaned_history[-1] == cleaned_history[-2]:
            repeated_move = cleaned_history[-1]
            punish_move = counter_map[repeated_move]
            punish_counter = counter_map[punish_move]
            store.duel_boss_stance_name = "Punish Stance"
            store.duel_boss_telegraph = b_data.get("anti_spam_quote", "Trying the same move twice won't work!")
            store.duel_boss_stance_hint = "Anti-Spam: Countering repeated %s! (Favors %s - Counter with %s)" % (
                repeated_move.upper(),
                punish_move.upper(),
                punish_counter.upper()
            )
            store.duel_boss_planned_move = punish_move
            store.duel_boss_is_feint = False
            return

        # 2. Enrage Feint Check: If low HP, 30% chance to execute a feint
        if low_hp and random.random() < 0.30:
            fake_intent = random.choice(["rock", "scissors", "paper"])
            player_expected_counter = counter_map[fake_intent]
            boss_feint_move = counter_map[player_expected_counter]
            player_counter_feint = counter_map[boss_feint_move]

            store.duel_boss_stance_name = "Feint Stance"
            store.duel_boss_telegraph = b_data.get("enrage_feint_quote", "Think you can read my moves?! Think again!")
            store.duel_boss_stance_hint = "[FEINT ALERT] Feigning %s to bait %s! (Boss throws %s - Counter with %s)" % (
                fake_intent.upper(),
                player_expected_counter.upper(),
                boss_feint_move.upper(),
                player_counter_feint.upper()
            )
            store.duel_boss_planned_move = boss_feint_move
            store.duel_boss_is_feint = True
            return

        # 3. Standard Stance with Clear Telegraph
        stances = list(b_data["stances"].keys())
        chosen_stance_key = random.choice(stances)
        sdata = b_data["stances"][chosen_stance_key]

        w = sdata["weights"]
        r = random.random()
        if r < w.get(chosen_stance_key, 0.80):
            actual_move = chosen_stance_key
        elif r < w.get(chosen_stance_key, 0.80) + 0.10:
            actual_move = counter_map[chosen_stance_key]
        else:
            actual_move = beats_map[chosen_stance_key]

        store.duel_boss_stance_name = sdata["name"]
        store.duel_boss_telegraph = random.choice(sdata["quotes"])
        store.duel_boss_stance_hint = sdata["hint"]
        store.duel_boss_planned_move = actual_move
        store.duel_boss_is_feint = False

    def duel_ai_pick(history=None, boss="mantis"):
        if hasattr(store, "duel_boss_planned_move") and store.duel_boss_planned_move:
            move = store.duel_boss_planned_move
            store.duel_boss_planned_move = None
            return move
        duel_prepare_round_strategy(boss)
        move = getattr(store, "duel_boss_planned_move", "rock")
        store.duel_boss_planned_move = None
        return move

    def mantis_ai_pick(history):
        return duel_ai_pick(history, getattr(store, "duel_boss", "mantis"))

    def duel_record_round_result(round_num, p_choice, b_choice, result):
        if not hasattr(store, "duel_match_history") or store.duel_match_history is None:
            store.duel_match_history = []
        store.duel_match_history.append({
            "round": round_num,
            "player": str(p_choice).capitalize(),
            "boss": str(b_choice).capitalize(),
            "result": str(result).lower()
        })

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
        elif duel_boss == "dunge":
            if duel_shrimp_hp <= 0:
                add "dunge_icon_dead":
                    xalign 0.88
                    yalign 0.12
            elif duel_shrimp_hp == 1:
                add "dunge_icon_one":
                    xalign 0.88
                    yalign 0.12
            elif duel_shrimp_hp == 2:
                add "dunge_icon_half":
                    xalign 0.88
                    yalign 0.12
            else:
                add "dunge_icon_full":
                    xalign 0.88
                    yalign 0.12
        else:
            if duel_shrimp_hp <= 0:
                add "mantis_icon_dead":
                    xalign 0.88
                    yalign 0.12
            elif duel_shrimp_hp == 1:
                add "mantis_icon_one":
                    xalign 0.88
                    yalign 0.12
            elif duel_shrimp_hp == 2:
                add "mantis_icon_half":
                    xalign 0.88
                    yalign 0.12
            else:
                add "mantis_icon_full":
                    xalign 0.88
                    yalign 0.12

screen mantis_battle_stage():
    use duel_battle_stage

screen mantis_rps_screen():

    modal True

    # 1. Boss Strategic Telegraph & Stance Banner (Top Center)
    frame:
        xalign 0.5
        ypos 36
        xsize 940
        background Frame(Solid("#021a2cf0"), 12, 12)
        padding (22, 12)

        has vbox:
            xalign 0.5
            spacing 5

        # Boss Name • Stance • Round
        hbox:
            xalign 0.5
            spacing 14
            text "[duel_boss_name]":
                size 21
                bold True
                color "#ffeaa7"
                outlines [(2, "#011627", 0, 0)]
            text "•":
                size 21
                color "#74b9ff"
            text "[duel_boss_stance_name]":
                size 21
                bold True
                color ("#ff7675" if duel_boss_is_feint else "#fab1a0")
                outlines [(2, "#011627", 0, 0)]
            text "•":
                size 21
                color "#74b9ff"
            text _("Round [duel_round]"):
                size 18
                color "#dfe6e9"
                outlines [(1, "#011627", 0, 0)]

        # Boss Dialogue Quote / Telegraph
        text "\"[duel_boss_telegraph]\"":
            xalign 0.5
            size 20
            italic True
            color "#ffffff"
            outlines [(2, "#000000", 0, 0)]

        # Tactical Clue
        frame:
            xalign 0.5
            background Solid("#00000088")
            padding (14, 4)
            text "[duel_boss_stance_hint]":
                xalign 0.5
                size 15
                bold True
                color ("#fdcb6e" if duel_boss_is_feint else "#55efc4")
                outlines [(1, "#000000", 0, 0)]

    # 2. Match History Tracker (Recent rounds)
    if duel_match_history and len(duel_match_history) > 0:
        hbox:
            xalign 0.5
            ypos 188
            spacing 10
            for item in duel_match_history[-3:]:
                $ hist_r = str(item.get("round", ""))
                $ hist_p = str(item.get("player", ""))
                $ hist_b = str(item.get("boss", ""))
                $ hist_res = str(item.get("result", "")).upper()
                $ hist_color = "#55efc4" if item.get("result") == "win" else ("#74b9ff" if item.get("result") == "dodged" else ("#ff7675" if item.get("result") == "lose" else "#ffeaa7"))
                frame:
                    background Solid("#011422cc")
                    padding (10, 4)
                    has hbox:
                        spacing 6
                    text ("R" + hist_r + ":"):
                        size 14
                        color "#b2bec3"
                    text hist_p:
                        size 14
                        bold True
                        color hist_color
                    text "vs":
                        size 14
                        color "#636e72"
                    text hist_b:
                        size 14
                        color "#dfe6e9"
                    text ("(" + hist_res + ")"):
                        size 14
                        bold True
                        color hist_color

    # 3. Action Buttons with Tactical Guidance
    vbox:
        xalign 0.20
        yalign 0.94
        spacing 6
        imagebutton:
            xalign 0.5
            idle "jankenpon button rock"
            focus_mask True
            hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
            action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("rock")]
        frame:
            xalign 0.5
            background Solid("#011627dd")
            padding (10, 4)
            text _("ROCK (Crushes Scissors)"):
                size 15
                bold True
                color "#dfe6e9"
                outlines [(1, "#000000", 0, 0)]

    vbox:
        xalign 0.50
        yalign 0.94
        spacing 6
        imagebutton:
            xalign 0.5
            idle "jankenpon button scissors"
            focus_mask True
            hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
            action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("scissors")]
        frame:
            xalign 0.5
            background Solid("#011627dd")
            padding (10, 4)
            text _("SCISSORS (Cuts Paper)"):
                size 15
                bold True
                color "#dfe6e9"
                outlines [(1, "#000000", 0, 0)]

    vbox:
        xalign 0.80
        yalign 0.94
        spacing 6
        imagebutton:
            xalign 0.5
            idle "jankenpon button paper"
            focus_mask True
            hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
            action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("paper")]
        frame:
            xalign 0.5
            background Solid("#011627dd")
            padding (10, 4)
            text _("PAPER (Enfolds Rock)"):
                size 15
                bold True
                color "#dfe6e9"
                outlines [(1, "#000000", 0, 0)]

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
    $ duel_fighter = "cory"
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

    $ play_random_battle_music(0.5)

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
    $ duel_match_history = []

    $ duel_boss_stance_name = ""
    $ duel_boss_stance_hint = ""
    $ duel_boss_telegraph = ""
    $ duel_boss_planned_move = None
    $ duel_boss_is_feint = False

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

        $ duel_prepare_round_strategy(duel_boss)

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
            play sound "audio/sfx/attack_1.mp3"
        elif duel_round_result == "lose":
            play sound "audio/sfx/attack_2.mp3"
        else:
            play sound "audio/sfx/tin_metal.mp3"

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
            play wind_sfx "audio/sfx/wind_spell_3.mp3"
            if duel_boss == "dunge":
                $ dodge_result = False
            else:
                $ _bcfg = DUEL_BOSS_REGISTRY.get(duel_boss, DUEL_BOSS_REGISTRY["mantis"])
                $ _tar_range = _bcfg.get("dodge_tar_range" if coal_tar_effective else "dodge_target_range", (7, 9))
                $ duel_z_target = random.randint(_tar_range[0], _tar_range[1])
                $ duel_z_taps = 0

                $ duel_is_dodging = True
                call screen mantis_spamz_screen(duel_player_choice, duel_shrimp_choice)
                $ dodge_result = _return   # True = spam success, False = spam fail
                $ duel_is_dodging = False
                if dodge_result:
                    play sound "audio/sfx/wind_spin_1.mp3"

        # Record round result for tactical HUD
        $ _outcome = "dodged" if (duel_round_result == "lose" and dodge_result) else duel_round_result
        $ duel_record_round_result(duel_round, duel_player_choice, duel_shrimp_choice, _outcome)

        if duel_round_result == "win":
            $ duel_player_wins += 1
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
                if duel_boss != "dunge":
                    play sound "audio/sfx/punch_01.mp3"
                    call screen mantis_punch_effect(duel_shrimp_choice)
                else:
                    play sound "audio/sfx/tin_metal.mp3"
                $ duel_player_hp = max(0, duel_player_hp - 1)
                $ duel_shrimp_wins += 1
            else:
                pass

        $ duel_round += 1

    hide screen duel_battle_stage
    hide screen mantis_battle_stage
    stop music fadeout 1.0
    
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
        play sound "audio/sfx/attack_release.mp3"
        window auto
        return "win"

    $ duel_result = "lose"
    $ dunge_battle_result = "defeat"
    play sound "audio/sfx/pixel_death.mp3"
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
