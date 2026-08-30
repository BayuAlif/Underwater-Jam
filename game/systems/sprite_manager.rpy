# =====================================
# Sprite Display System
# =====================================

define SPRITE_ZOOM = 0.75


# =====================================
# Posisi Sprite
# =====================================

# Cory / MC selalu di kiri
transform mc_pos:
    xalign 0.22
    yalign 1.0
    zoom SPRITE_ZOOM

# NPC selalu di kanan
transform npc_pos:
    xalign 0.78
    yalign 1.0
    zoom SPRITE_ZOOM


# =====================================
# Active / Inactive
# =====================================

transform sprite_active:
    linear 0.15 alpha 1.0 matrixcolor BrightnessMatrix(0.0)


transform sprite_inactive:
    linear 0.15 alpha 0.85 matrixcolor BrightnessMatrix(-0.4)


# =====================================
# Speaker Highlight System
# =====================================

init -10 python:

    SPEAKER_POSITIONS = {
        "f1": "mc_pos",

        "bass": "npc_pos",
        "uceng": "npc_pos",
        "lele": "npc_pos",
        "gator": "npc_pos",
    }


    def _refresh_speaker_highlight(active_tag):

        for tag, pos_name in SPEAKER_POSITIONS.items():

            if not renpy.showing(tag):
                continue

            pos = getattr(store, pos_name)

            if tag == active_tag:
                renpy.show(
                    tag,
                    at_list=[pos, sprite_active]
                )

            else:
                renpy.show(
                    tag,
                    at_list=[pos, sprite_inactive]
                )


    def speaker_callback(tag):

        def _callback(event, interact=True, **kwargs):

            if event == "show" and interact:
                _refresh_speaker_highlight(tag)

        return _callback