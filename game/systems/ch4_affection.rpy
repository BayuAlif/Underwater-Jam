# Affection System for Chapter 4
# Displays companion banner HUD in the top right corner and tracks affection points.

default ch4_current_companion = None

init python:
    def ch4_get_affection(char_id):
        if char_id in ("cory",):
            return getattr(store, "ch4_cory_affection", 0)
        elif char_id in ("scy", "scyllarus", "clarus"):
            return getattr(store, "ch4_scy_affection", 0)
        elif char_id in ("leo",):
            return getattr(store, "ch4_leo_affection", 0)
        return 0

    def ch4_get_name(char_id):
        if char_id in ("cory",):
            return "Cory"
        elif char_id in ("scy", "scyllarus", "clarus"):
            return "Scyllarus"
        elif char_id in ("leo",):
            return "Leo"
        return "Companion"

    def ch4_add_affection(char_id, amount=1, notify=True):
        c_id = "scy" if char_id in ("scy", "scyllarus", "clarus") else char_id
        old_val = ch4_get_affection(c_id)
        name = ch4_get_name(c_id)

        if c_id == "cory":
            store.ch4_cory_affection = min(3, max(0, store.ch4_cory_affection + amount))
        elif c_id == "scy":
            store.ch4_scy_affection = min(3, max(0, store.ch4_scy_affection + amount))
        elif c_id == "leo":
            store.ch4_leo_affection = min(3, max(0, store.ch4_leo_affection + amount))

        new_val = ch4_get_affection(c_id)
        if notify:
            if new_val > old_val:
                renpy.notify(_("%s's affection increased! (+%d)") % (name, amount))
                try:
                    renpy.play("audio/sfx/pixel_save_game.mp3", channel="sound")
                except Exception:
                    pass
            elif new_val == 3 and old_val == 3 and amount > 0:
                renpy.notify(_("%s's affection is at MAX! (3 Hearts)") % name)
        return new_val

transform ch4_affection_hud_trans:
    on show:
        alpha 0.0 yoffset -30
        easein 0.4 alpha 1.0 yoffset 0
    on hide:
        easeout 0.3 alpha 0.0 yoffset -30

screen ch4_affection_hud(companion=None):
    zorder 95

    $ comp = companion if companion is not None else store.ch4_current_companion

    if comp in ("cory", "scy", "leo", "scyllarus", "clarus"):
        $ c_key = "scy" if comp in ("scy", "scyllarus", "clarus") else comp
        $ aff = ch4_get_affection(c_key)
        $ aff_clamped = max(0, min(3, aff))
        $ banner_file = "images/ui/ch4_affection/banner_%s_%d.png" % (c_key, aff_clamped)

        fixed at ch4_affection_hud_trans:
            xalign 0.98
            yalign 0.0
            xsize 340
            ysize 560

            add banner_file
