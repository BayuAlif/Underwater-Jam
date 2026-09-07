# =========================================================
# DODGE MANAGER
# Chapter 2 - Mantis Shrimp
# =========================================================


# =========================================================
# DODGE VARIABLES
# =========================================================

default dodge_result = False

default scissor_position = 0.0
default scissor_direction = 1.0

default rock_punches = []
default rock_hits = 0
default rock_time_left = 5.0

default paper_progress = 50.0
default paper_time_left = 3.0
default paper_smashing = False
default paper_last_press_time = 0.0


# =========================================================
# DODGE ASSET HELPER
# =========================================================

init python:

    def dodge_asset(path):

        full_path = "images/battle/dodge/" + path

        if renpy.loadable(full_path):
            return full_path

        return None


    # ---------------------------------------------------
    # Loads an asset straight from images/battle/, used
    # for the shared battle Background.png. This mirrors
    # battle_asset() from duel_manager.rpy but is kept
    # local here so dodge_manager.rpy does not depend on
    # load order between the two files.
    # ---------------------------------------------------

    def dodge_battle_asset(path):

        full_path = "images/battle/" + path

        if renpy.loadable(full_path):
            return full_path

        return None


# =========================================================
# SCISSORS DODGE
# TIMING BAR
# =========================================================

init python:

    # ---------------------------------------------------
    # GEOMETRY
    #
    # ScissorRunningRed.png, ScissorBlueBar.png and all
    # ScissorGreenBar*.png are full 1920x1080 canvases, not
    # small cropped sprites. That means they can NOT just be
    # nudged by a guessed xpos number - the offset has to be
    # calculated from where the actual bar/track sits inside
    # that canvas, or the red indicator drifts off the track.
    #
    # These values were measured directly from the PNGs
    # (pixel bounding box of the opaque area):
    #
    #   ScissorBlueBar.png   -> track spans x = 93 .. 1869
    #   ScissorRunningRed.png -> red bar spans x = 934 .. 964,
    #                             y = 954 .. 1053 (center = 949)
    #   ScissorGreenBar.png   -> safe zone x = 631  .. 1337
    #   ScissorGreenBar2.png  -> safe zone x = 893  .. 1188
    #   ScissorGreenBar3.png  -> safe zone x = 953  .. 1074
    #
    # FIX: ScissorRunningRed.png is a full 1920x1080 canvas
    # where only that small x934-964 / y954-1053 box is
    # opaque. Moving the image with xpos alone drags the
    # WHOLE transparent canvas across the screen, which is
    # harmless visually (transparent stays transparent) but
    # means the canvas' left edge - not the red line - is
    # what "xpos" actually refers to, and any layout code
    # downstream that assumes running_red is a small sprite
    # breaks. To make the red line the only thing that
    # visually moves and to keep xpos meaning "position of
    # the line itself", the image is first cropped down to
    # just that small box (crop transform property below),
    # and THEN positioned/animated. crop is applied against
    # the untransformed source image, so the coordinates
    # below are the same raw pixel box measured above.
    # ---------------------------------------------------

    SCISSOR_TRACK_LEFT = 93
    SCISSOR_TRACK_RIGHT = 1869
    SCISSOR_TRACK_WIDTH = SCISSOR_TRACK_RIGHT - SCISSOR_TRACK_LEFT

    SCISSOR_RED_BAR_CENTER = 949

    SCISSOR_RED_CROP_LEFT = 934
    SCISSOR_RED_CROP_TOP = 954
    SCISSOR_RED_CROP_RIGHT = 964
    SCISSOR_RED_CROP_BOTTOM = 1053

    SCISSOR_RED_CROP_WIDTH = (
        SCISSOR_RED_CROP_RIGHT - SCISSOR_RED_CROP_LEFT
    )
    SCISSOR_RED_CROP_HEIGHT = (
        SCISSOR_RED_CROP_BOTTOM - SCISSOR_RED_CROP_TOP
    )

    # round_num -> (asset path, safe zone left, safe zone right)
    # Round 1 gets the widest (easiest) window, and it narrows
    # as the duel goes on, using all three green bar variants.
    SCISSOR_GREEN_ZONES = {
        1: ("scissors/ScissorGreenBar.png", 631, 1337),
        2: ("scissors/ScissorGreenBar2.png", 893, 1188),
        3: ("scissors/ScissorGreenBar3.png", 953, 1074),
    }


    def scissor_green_zone_for_round(round_num):

        if round_num in SCISSOR_GREEN_ZONES:
            return SCISSOR_GREEN_ZONES[round_num]

        # Round 4 and beyond keep the hardest (narrowest) zone.
        return SCISSOR_GREEN_ZONES[3]


    def scissor_red_xpos(position):

        # Where the red bar's center should land on screen,
        # sliding from the left edge to the right edge of the
        # blue track as position goes 0.0 -> 1.0.
        target_center = (
            SCISSOR_TRACK_LEFT
            + position * SCISSOR_TRACK_WIDTH
        )

        # running_red is now cropped down to just the small
        # SCISSOR_RED_CROP_* box (see the crop transform
        # property used where it's added in dodge_scissors),
        # so xpos here positions the LEFT edge of that small
        # cropped piece - not the left edge of the original
        # 1920px canvas. Shifting by half its width centers
        # the cropped piece on target_center.
        return target_center - (SCISSOR_RED_CROP_WIDTH / 2.0)


    def scissor_update():

        global scissor_position
        global scissor_direction

        speed = 0.012

        scissor_position += speed * scissor_direction

        if scissor_position >= 1.0:
            scissor_position = 1.0
            scissor_direction = -1.0

        elif scissor_position <= 0.0:
            scissor_position = 0.0
            scissor_direction = 1.0


    def scissor_try_dodge():

        # duel_round_num comes from duel_manager.rpy and is
        # only read here, never modified, so RPS/story logic
        # stays untouched.
        _asset, zone_left, zone_right = scissor_green_zone_for_round(
            duel_round_num
        )

        pos_min = (
            (zone_left - SCISSOR_TRACK_LEFT)
            / float(SCISSOR_TRACK_WIDTH)
        )

        pos_max = (
            (zone_right - SCISSOR_TRACK_LEFT)
            / float(SCISSOR_TRACK_WIDTH)
        )

        if pos_min <= scissor_position <= pos_max:
            return True

        return False


screen dodge_scissors():

    modal True

    # -----------------------------------------------------
    # BACKGROUND
    # Must be the FIRST thing drawn so it fully covers
    # whatever scene is showing behind this modal screen
    # (mc sprite, mantis npc, day/night cycle background).
    # Without this, the transparent parts of every asset
    # below reveal the underlying scene instead of the
    # dedicated battle background.
    # -----------------------------------------------------

    $ scissor_battle_bg = dodge_battle_asset(
        "Background.png"
    )

    if scissor_battle_bg:

        add scissor_battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    # -----------------------------------------------------
    # SCISSOR ATTACK ART
    # -----------------------------------------------------

    $ scissor_bg = dodge_asset(
        "scissors/Scissor.png"
    )

    if scissor_bg:
        add scissor_bg:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # DODGE TEXT
    # -----------------------------------------------------

    $ scissor_dodge = dodge_asset(
        "scissors/ScissorDodge.png"
    )

    if scissor_dodge:
        add scissor_dodge:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # BAR
    # -----------------------------------------------------

    $ blue_bar = dodge_asset(
        "scissors/ScissorBlueBar.png"
    )

    if blue_bar:
        add blue_bar:
            xpos 0
            ypos 0


    $ _green_asset, _green_left, _green_right = scissor_green_zone_for_round(
        duel_round_num
    )

    $ green_bar = dodge_asset(
        _green_asset
    )

    if green_bar:
        add green_bar:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # MOVING RED INDICATOR
    # Full-canvas PNG - shifted using scissor_red_xpos(),
    # which is derived from the real measured bar/track
    # positions instead of a guessed offset.
    # -----------------------------------------------------

    $ running_red = dodge_asset(
        "scissors/ScissorRunningRed.png"
    )

    if running_red:

        # crop cuts the displayable down to just the
        # SCISSOR_RED_CROP_* box BEFORE xpos/ypos are
        # applied, so only that small red-line region is
        # drawn and moved - the rest of the 1920x1080
        # transparent canvas is discarded, not just hidden.
        add running_red:
            crop (
                SCISSOR_RED_CROP_LEFT,
                SCISSOR_RED_CROP_TOP,
                SCISSOR_RED_CROP_WIDTH,
                SCISSOR_RED_CROP_HEIGHT
            )
            xpos scissor_red_xpos(scissor_position)
            ypos SCISSOR_RED_CROP_TOP

    else:

        # ---------------------------------------------------
        # DEBUG FALLBACK
        # If ScissorRunningRed.png can't be found/loaded,
        # dodge_asset() returns None and the indicator would
        # otherwise just silently not draw at all. This bright
        # marker takes its place instead, at the same moving
        # position and the same real size as the cropped red
        # line, so a missing asset is obvious in-game instead
        # of looking like "nothing happens".
        #
        # If you see this magenta bar instead of the hand-drawn
        # red one, ScissorRunningRed.png is not being found at:
        #   game/images/battle/dodge/scissors/ScissorRunningRed.png
        # Double check the file is actually there (exact name,
        # exact folder) and clear out any old .rpyc cache files
        # in game/cache, then relaunch.
        # ---------------------------------------------------

        add Solid("#ff00ffcc"):
            xpos scissor_red_xpos(scissor_position)
            ypos SCISSOR_RED_CROP_TOP
            xsize SCISSOR_RED_CROP_WIDTH
            ysize SCISSOR_RED_CROP_HEIGHT


    # ---------------------------------------------------
    # INPUT
    # ---------------------------------------------------

    key "K_SPACE" action Return(
        scissor_try_dodge()
    )

    key "z" action Return(
        scissor_try_dodge()
    )

    timer 0.01 repeat True action Function(
        scissor_update
    )


# =========================================================
# ROCK DODGE
# CLICKING / OSU STYLE
# =========================================================

init python:

    import random


    # ---------------------------------------------------
    # TUNING
    #
    # Total seconds the player has to clear every spawned
    # punch target. Previously this minigame used a silent
    # "timer 5.0 action Return(False)" deadline with no
    # visible countdown, so the player had no way to gauge
    # the pressure. It's now driven by rock_time_left, which
    # actually counts down every ROCK_TICK_INTERVAL seconds
    # (see rock_tick() below) and is shown on screen. The
    # limit itself was also tightened from the old 5.0s to
    # make the mash-to-dodge feel more urgent - tune this one
    # number if it needs to be easier/harder.
    # ---------------------------------------------------

    ROCK_TIME_LIMIT = 3.2
    ROCK_TICK_INTERVAL = 0.1


    def setup_rock_dodge():

        global rock_punches
        global rock_hits
        global rock_time_left

        rock_hits = 0
        rock_time_left = ROCK_TIME_LIMIT
        rock_punches = []

        punch_path = "images/battle/dodge/rock/PUNCHES/"

        files = [
            f for f in renpy.list_files()
            if f.startswith(punch_path)
            and f.lower().endswith(
                (".png", ".jpg", ".jpeg", ".webp")
            )
        ]

        if not files:
            return

        selected = files[:7]

        for i, asset in enumerate(selected):

            rock_punches.append({
                "id": i,
                "asset": asset,
                "x": 0,
                "y": 0
            })


    def rock_hit(punch_id):

        global rock_hits
        global rock_punches
        global rock_time_left

        rock_hits += 1

        rock_punches = [
            punch for punch in rock_punches
            if punch["id"] != punch_id
        ]

        if not rock_punches:
            rock_time_left = 0.0

        renpy.restart_interaction()


    def rock_tick():

        # Ticks rock_time_left down in real time so the
        # on-screen countdown (and the round's actual fail
        # condition) reflect the same number. No-ops once
        # time has already run out or the round is about to
        # end, so it can't push the value negative or fight
        # with rock_hit() zeroing it out on the final punch.

        global rock_time_left

        if rock_time_left <= 0.0:
            return

        rock_time_left -= ROCK_TICK_INTERVAL

        if rock_time_left < 0.0:
            rock_time_left = 0.0

        renpy.restart_interaction()


screen dodge_rock():

    modal True

    # -----------------------------------------------------
    # BACKGROUND
    # Same fix as Scissors Dodge: draw the real battle
    # Background.png first so it fully covers whatever is
    # showing behind this modal screen (mc sprite, mantis
    # npc, day/night cycle background).
    # -----------------------------------------------------

    $ rock_battle_bg = dodge_battle_asset(
        "Background.png"
    )

    if rock_battle_bg:

        add rock_battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    # -----------------------------------------------------
    # ROCK ATTACK ART
    # -----------------------------------------------------

    $ rock_bg = dodge_asset(
        "rock/Rock.png"
    )

    if rock_bg:
        add rock_bg:
            xpos 0
            ypos 0


    $ rock_dodge = dodge_asset(
        "rock/RockDodge.png"
    )

    if rock_dodge:
        add rock_dodge:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # COUNTDOWN
    # Live "seconds left" readout, top-left. Driven by
    # rock_time_left, which rock_tick() below actually
    # counts down in real time.
    # -----------------------------------------------------

    text "%.1f" % rock_time_left:
        xpos 40
        ypos 30
        size 60
        color "#ffffff"
        outlines [(4, "#000000", 0, 0)]


    # -----------------------------------------------------
    # PUNCH TARGETS
    # -----------------------------------------------------

    for punch in rock_punches:

        imagebutton:

            idle punch["asset"]
            hover punch["asset"]

            xpos punch["x"]
            ypos punch["y"]

            focus_mask True

            action Function(
                rock_hit,
                punch["id"]
            )


    # -----------------------------------------------------
    # TICK
    # Counts rock_time_left down every ROCK_TICK_INTERVAL
    # seconds, which both updates the countdown text above
    # and feeds the RESULT check below.
    # -----------------------------------------------------

    timer ROCK_TICK_INTERVAL repeat True action Function(
        rock_tick
    )


    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    if not rock_punches:

        timer 0.01 action Return(True)

    elif rock_time_left <= 0.0:

        timer 0.05 action Return(False)


# =========================================================
# PAPER DODGE
# TUG-OF-WAR / SPAM Z
#
# paper_progress is a float from 0.0 (Mantis fully wins,
# red side) to 100.0 (Player fully wins, blue side),
# starting at 50.0 in the middle. This is a push/pull:
#
#   - Pressing Z pushes progress toward the player (up).
#     How HARD it pushes depends on how fast Z is being
#     spammed: a rapid press (short time since the last
#     press) gives a big push, a slow/lone press only
#     gives a small push.
#   - A repeating tick continuously pulls progress back
#     toward the Mantis (down) once the player has been
#     idle (no Z press) for longer than a short grace
#     window. The longer the player stalls, the more
#     ground the Mantis quietly reclaims.
#
# The same 7-stage Blue1..BlueFull art and the RedFull
# bar are reused - paper_progress is simply mapped onto
# that 0..7 stage range for drawing. The ArrowRed/ArrowBlue
# assets are reused too, but are now shifted along the bar
# (instead of sitting static at xpos 0) so they visually
# meet and slide at wherever the current push/pull line is.
# =========================================================

init python:

    import time


    # ---------------------------------------------------
    # GEOMETRY
    #
    # Like the Scissors bar, RedFull.png / Blue1..BlueFull
    # / ArrowRed.png / ArrowBlue.png are full 1920x1080
    # canvases, not small cropped sprites. These values were
    # measured directly from the PNGs:
    #
    #   bar fill track   -> spans x = 144 .. 1780
    #   ArrowBlue.png     -> tip (rightmost opaque px) = 570
    #   ArrowRed.png      -> tip (leftmost opaque px)   = 562
    #
    # At xpos 0 (no shift) the two arrow tips already meet
    # close together around x ~= 566, which is used below as
    # the reference point the arrows shift around as
    # paper_progress moves.
    # ---------------------------------------------------

    PAPER_TRACK_LEFT = 144
    PAPER_TRACK_RIGHT = 1780
    PAPER_TRACK_WIDTH = PAPER_TRACK_RIGHT - PAPER_TRACK_LEFT

    PAPER_ARROW_BASE_X = 566

    # Clamp how far the arrow pair is allowed to slide so
    # the (large, full-canvas) arrow art never gets pushed
    # off the edges of the screen.
    PAPER_ARROW_DX_MIN = -400
    PAPER_ARROW_DX_MAX = 1150

    # ---------------------------------------------------
    # TUNING
    # ---------------------------------------------------

    PAPER_START_PROGRESS = 50.0
    PAPER_WIN_PROGRESS = 100.0
    PAPER_LOSE_PROGRESS = 0.0

    PAPER_TIME_LIMIT = 6.0

    # Spam-speed thresholds: time (seconds) since the
    # previous Z press.
    PAPER_FAST_DT = 0.15
    PAPER_MEDIUM_DT = 0.35

    # How much a press pushes progress toward the player,
    # depending on which speed bucket it lands in.
    PAPER_PUSH_FAST = 4.0
    PAPER_PUSH_MEDIUM = 2.0
    PAPER_PUSH_SLOW = 0.8

    # If the player hasn't pressed Z in longer than this,
    # the Mantis starts quietly pulling progress back.
    PAPER_IDLE_GRACE = 0.3
    PAPER_DECAY_PER_SEC = 7.0

    PAPER_TICK_INTERVAL = 0.05

    # How long the "KeySmash" art stays on screen after a
    # press before falling back to "KeyIdle".
    PAPER_SMASH_FLASH = 0.15


    def paper_boundary_x(progress):

        clamped = max(0.0, min(100.0, progress))

        return (
            PAPER_TRACK_LEFT
            + (clamped / 100.0) * PAPER_TRACK_WIDTH
        )


    def paper_arrow_dx(progress):

        dx = paper_boundary_x(progress) - PAPER_ARROW_BASE_X

        if dx < PAPER_ARROW_DX_MIN:
            dx = PAPER_ARROW_DX_MIN

        if dx > PAPER_ARROW_DX_MAX:
            dx = PAPER_ARROW_DX_MAX

        return dx


    def paper_stage_for_progress(progress):

        clamped = max(0.0, min(100.0, progress))

        # Stage 7 (BlueFull.png, "the player has won" art) is
        # reserved strictly for an ACTUAL win (progress really
        # at PAPER_WIN_PROGRESS). It used to be picked with
        # round(clamped / 100.0 * 7), which reaches stage 7
        # (and shows BlueFull) starting around progress ~92.86
        # - well before the real win check below (which needs
        # progress >= 100.0) fires. That let the bar look fully
        # won while it hadn't actually won yet: the player would
        # see "blue penuh" and stop pressing Z, and the Mantis'
        # idle pull-back (paper_tick) would then drag progress
        # back down before it ever reached the real 100, so the
        # round quietly ended in a loss/damage despite looking
        # like a win on screen.
        if clamped >= PAPER_WIN_PROGRESS:
            return 7

        stage = int(clamped // (100.0 / 7))

        if stage < 0:
            stage = 0

        if stage > 6:
            stage = 6

        return stage


    def paper_reset():

        global paper_progress
        global paper_smashing
        global paper_last_press_time

        paper_progress = PAPER_START_PROGRESS
        paper_smashing = False

        # Give the player a brief grace window at the start
        # of the minigame before the Mantis' pull-back can
        # kick in.
        paper_last_press_time = time.time()


    def paper_register_press():

        global paper_progress
        global paper_smashing
        global paper_last_press_time

        now = time.time()

        if paper_last_press_time:
            dt = now - paper_last_press_time
        else:
            dt = PAPER_MEDIUM_DT + 1.0

        if dt <= PAPER_FAST_DT:
            push = PAPER_PUSH_FAST

        elif dt <= PAPER_MEDIUM_DT:
            push = PAPER_PUSH_MEDIUM

        else:
            push = PAPER_PUSH_SLOW

        paper_progress += push

        if paper_progress > PAPER_WIN_PROGRESS:
            paper_progress = PAPER_WIN_PROGRESS

        paper_last_press_time = now
        paper_smashing = True

        renpy.restart_interaction()


    def paper_tick():

        global paper_progress
        global paper_smashing

        now = time.time()

        if paper_last_press_time:
            idle = now - paper_last_press_time
        else:
            idle = PAPER_IDLE_GRACE + 1.0

        # Mantis slowly reclaims progress once the player
        # has stalled past the grace window.
        if idle > PAPER_IDLE_GRACE:

            paper_progress -= (
                PAPER_DECAY_PER_SEC * PAPER_TICK_INTERVAL
            )

            if paper_progress < PAPER_LOSE_PROGRESS:
                paper_progress = PAPER_LOSE_PROGRESS

        # Let the "smash" key art relax back to idle a
        # short moment after the last press.
        if idle > PAPER_SMASH_FLASH:
            paper_smashing = False


screen dodge_paper():

    modal True

    # -----------------------------------------------------
    # BACKGROUND
    # Same fix as Scissors Dodge: draw the real battle
    # Background.png first so it fully covers whatever is
    # showing behind this modal screen (mc sprite, mantis
    # npc, day/night cycle background).
    # -----------------------------------------------------

    $ paper_battle_bg = dodge_battle_asset(
        "Background.png"
    )

    if paper_battle_bg:

        add paper_battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    # -----------------------------------------------------
    # PAPER ATTACK ART
    # -----------------------------------------------------

    $ paper_bg = dodge_asset(
        "paper/Paper.png"
    )

    if paper_bg:
        add paper_bg:
            xpos 0
            ypos 0


    $ paper_dodge = dodge_asset(
        "paper/PaperDodge.png"
    )

    if paper_dodge:
        add paper_dodge:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # RED PRESS BAR
    # Drawn first as the "Mantis fully wins" base state.
    # -----------------------------------------------------

    $ red_full = dodge_asset(
        "paper/RedFull.png"
    )

    if red_full:
        add red_full:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # BLUE PRESS BAR
    # Blue1 -> Blue6 -> BlueFull, chosen from the current
    # 0.0 - 100.0 tug-of-war progress. Stage 0 means the
    # Mantis is fully in control, so no blue overlay is
    # drawn and RedFull alone shows through.
    # -----------------------------------------------------

    $ paper_stage = paper_stage_for_progress(paper_progress)

    $ blue_bar = None

    if paper_stage >= 7:

        $ blue_bar = dodge_asset(
            "paper/BlueFull.png"
        )

    elif paper_stage == 6:

        $ blue_bar = dodge_asset(
            "paper/Blue6.png"
        )

    elif paper_stage == 5:

        $ blue_bar = dodge_asset(
            "paper/Blue5.png"
        )

    elif paper_stage == 4:

        $ blue_bar = dodge_asset(
            "paper/Blue4.png"
        )

    elif paper_stage == 3:

        $ blue_bar = dodge_asset(
            "paper/Blue3.png"
        )

    elif paper_stage == 2:

        $ blue_bar = dodge_asset(
            "paper/Blue2.png"
        )

    elif paper_stage == 1:

        $ blue_bar = dodge_asset(
            "paper/Blue1.png"
        )


    if blue_bar:

        add blue_bar:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # PRESS ARROWS
    # Both arrows are shifted together by the same amount,
    # sliding along the bar to sit right where the current
    # push/pull line is: further right (into the Mantis'
    # red side) as the player pushes progress up, further
    # left (into the player's side) as the Mantis pulls
    # progress back down.
    # -----------------------------------------------------

    $ arrow_dx = paper_arrow_dx(paper_progress)

    $ arrow_red = dodge_asset(
        "paper/ArrowRed.png"
    )

    if arrow_red:
        add arrow_red:
            xpos arrow_dx
            ypos 0


    $ arrow_blue = dodge_asset(
        "paper/ArrowBlue.png"
    )

    if arrow_blue:
        add arrow_blue:
            xpos arrow_dx
            ypos 0


    # -----------------------------------------------------
    # Z KEY
    # -----------------------------------------------------

    if paper_smashing:

        $ key_asset = dodge_asset(
            "paper/KeySmash.png"
        )

    else:

        $ key_asset = dodge_asset(
            "paper/KeyIdle.png"
        )


    if key_asset:

        add key_asset:
            xpos 0
            ypos 0


    # -----------------------------------------------------
    # INPUT
    # Every Z press is timed against the previous one -
    # rapid spam pushes progress up hard, slow/lone presses
    # only push it up a little.
    # -----------------------------------------------------

    key "z" action Function(
        paper_register_press
    )


    # -----------------------------------------------------
    # TICK
    # Continuously lets the Mantis reclaim progress while
    # the player is idle, and relaxes the key art back to
    # idle a moment after the last press.
    # -----------------------------------------------------

    timer PAPER_TICK_INTERVAL repeat True action Function(
        paper_tick
    )


    # -----------------------------------------------------
    # WIN / LOSE
    # -----------------------------------------------------

    if paper_progress >= PAPER_WIN_PROGRESS:

        timer 0.05 action Return(True)

    elif paper_progress <= PAPER_LOSE_PROGRESS:

        timer 0.05 action Return(False)


    timer PAPER_TIME_LIMIT action Return(
        paper_progress >= 50.0
    )


# =========================================================
# DODGE IMPACT
# =========================================================

screen dodge_impact_screen(
    shrimp_choice,
    dodged
):

    modal True

    # -----------------------------------------------------
    # BACKGROUND
    # Same fix as dodge_scissors / dodge_rock / dodge_paper:
    # draw the real battle Background.png first so it fully
    # covers whatever scene is showing behind this modal
    # screen (mc sprite, mantis npc, chapter 2 night-cycle
    # background). This screen was missing it entirely, so
    # every impact frame - rock, paper, and scissors alike -
    # let the underlying scene bleed through the transparent
    # parts of ScissorImpact*.png / RockImpact*.png /
    # PaperImpact*.png instead of showing a clean battle bg.
    # -----------------------------------------------------

    $ impact_battle_bg = dodge_battle_asset(
        "Background.png"
    )

    if impact_battle_bg:

        add impact_battle_bg:
            xpos 0
            ypos 0

    else:

        add Solid("#160b1b")


    if shrimp_choice == "scissors":

        if dodged:

            $ impact = dodge_asset(
                "scissors/ScissorImpact1.png"
            )

        else:

            $ impact = dodge_asset(
                "scissors/ScissorImpact2.png"
            )


    elif shrimp_choice == "rock":

        if dodged:

            $ impact = dodge_asset(
                "rock/RockImpact1.png"
            )

        else:

            $ impact = dodge_asset(
                "rock/RockImpact2.png"
            )


    else:

        if dodged:

            $ impact = dodge_asset(
                "paper/PaperImpact1.png"
            )

        else:

            $ impact = dodge_asset(
                "paper/PaperImpact2.png"
            )


    if impact:

        add impact:
            xpos 0
            ypos 0


    timer 0.7 action Return()


# =========================================================
# DODGE ENTRY POINT
# =========================================================

label mantis_dodge:

    $ dodge_result = False


    # -----------------------------------------------------
    # SCISSORS
    # -----------------------------------------------------

    if duel_shrimp_choice == "scissors":

        $ scissor_position = 0.0
        $ scissor_direction = 1.0

        call screen dodge_scissors

        $ dodge_result = _return


    # -----------------------------------------------------
    # ROCK
    # -----------------------------------------------------

    elif duel_shrimp_choice == "rock":

        $ setup_rock_dodge()

        call screen dodge_rock

        $ dodge_result = _return


    # -----------------------------------------------------
    # PAPER
    # -----------------------------------------------------

    elif duel_shrimp_choice == "paper":

        $ paper_reset()

        call screen dodge_paper

        $ dodge_result = _return


    call screen dodge_impact_screen(
        duel_shrimp_choice,
        dodge_result
    )

    return dodge_result
