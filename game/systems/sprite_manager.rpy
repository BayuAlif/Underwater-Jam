# =====================================
# Sprite Display System
# =====================================

define MC_ZOOM = 0.85
define CORY_ZOOM = 0.85
define NPC_ZOOM = 0.85


# =====================================
# Posisi Sprite (Posisi Murni, Ukuran Bersifat Global)
# =====================================

# MC (posisi kanan layar)
transform mc_pos:
    xanchor 0.69
    xpos 0.77
    yanchor 1.0
    ypos 1.0

# Posisi MC jika di sisi kiri
transform mc_left_pos:
    xanchor 0.69
    xpos 0.24
    yanchor 1.0
    ypos 1.0

# Cory di posisi kiri (default interaksi dengan MC)
transform cory_pos:
    xanchor 0.66
    xpos 0.24
    yanchor 1.0
    ypos 1.0

transform cory_left_pos:
    xanchor 0.66
    xpos 0.24
    yanchor 1.0
    ypos 1.0

# Cory di posisi kanan samping/menggantikan MC saat berbicara dengan NPC
transform cory_right_pos:
    xzoom -1.0
    xanchor 0.66
    xpos 0.77
    yanchor 1.0
    ypos 1.0

# Default NPC (posisi kiri layar saat berbicara dengan MC di kanan)
transform npc_pos:
    xanchor 0.28
    xpos 0.24
    yanchor 1.0
    ypos 1.0

# Transform spesifik tiap karakter agar pas di layar
transform bass_pos:
    xanchor 0.26
    xpos 0.24
    yanchor 1.0
    ypos 1.0

transform uceng_pos:
    xanchor 0.30
    xpos 0.24
    yanchor 1.0
    ypos 1.0

transform lele_pos:
    xanchor 0.30
    xpos 0.24
    yanchor 1.0
    ypos 1.0

# Gator di posisi kiri
transform gator_pos:
    xanchor 0.28
    xpos 0.24
    yanchor 1.0
    ypos 1.0

# Chapter 2 NPCs
transform salmon_pos:
    xanchor 0.28
    xpos 0.24
    yanchor 1.0
    ypos 1.0

transform wana_pos:
    xanchor 0.28
    xpos 0.24
    yanchor 1.0
    ypos 1.0


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

default cory_at_right = False

init -10 python:

    SPEAKER_POSITIONS = {
        "mc": "mc_pos",
        "cory": "cory_pos",

        "bass": "bass_pos",
        "uceng": "uceng_pos",
        "lele": "lele_pos",
        "gator": "gator_pos",

        "salmon": "salmon_pos",
        "wana": "wana_pos",
        "arowana": "wana_pos",
    }


    def get_speaker_pos(tag):

        if tag == "cory":
            if store.cory_at_right:
                return store.cory_right_pos
            return store.cory_pos

        pos_name = SPEAKER_POSITIONS.get(tag, "npc_pos")
        return getattr(store, pos_name)


    def _refresh_speaker_highlight(active_tag):

        for tag in SPEAKER_POSITIONS:

            if not renpy.showing(tag):
                continue

            pos = get_speaker_pos(tag)

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