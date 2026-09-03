# =====================================
# SPRITE DISPLAY SYSTEM
# =====================================
#
# Sprite show/hide dikontrol langsung
# oleh file chapter / NPC.
#
# speaker_callback() TIDAK mengatur sprite.
#
# =====================================


# =====================================
# SPRITE ZOOM
# =====================================

define MC_ZOOM = 0.85
define CORY_ZOOM = 0.85
define NPC_ZOOM = 0.85


# =====================================
# MC POSITION
# =====================================

transform mc_pos:
    xanchor 0.69
    xpos 0.77
    yanchor 1.0
    ypos 1.0


transform mc_left_pos:
    xanchor 0.69
    xpos 0.24
    yanchor 1.0
    ypos 1.0


# =====================================
# CORY POSITION
# =====================================

transform cory_pos:
    xanchor 0.34
    xpos 0.28
    yanchor 1.0
    ypos 1.0


transform cory_left_pos:
    xanchor 0.34
    xpos 0.24
    yanchor 1.0
    ypos 1.0


# Cory di kanan
# Digunakan saat Cory menggantikan MC.
transform cory_right_pos:
    xanchor 0.69
    xpos 1.1
    yanchor 1.0
    ypos 1.0

# =====================================
# NPC POSITIONS
# =====================================

transform npc_pos:
    xanchor 0.28
    xpos 0.24
    yanchor 1.0
    ypos 1.0


transform bass_pos:
    xanchor 0.74
    xpos 0.32
    yanchor 1.0
    ypos 1.0


transform uceng_pos:
    xanchor 0.70
    xpos 0.26
    yanchor 1.0
    ypos 1.0


transform lele_pos:
    xanchor 0.70
    xpos 0.25
    yanchor 1.0
    ypos 1.0


transform gator_pos:
    xanchor 0.28
    xpos 0.24
    yanchor 1.0
    ypos 1.0


transform salmon_pos:
    xanchor 0.72
    xpos 0.28
    yanchor 1.0
    ypos 1.0


transform wana_pos:
    xanchor 0.69
    xpos 0.28
    yanchor 1.0
    ypos 1.0


transform ghost_pos:
    xanchor 0.73
    xpos 0.28
    yanchor 1.0
    ypos 1.0


transform shrimp_pos:
    xanchor 0.50
    xpos 0.15
    yanchor 1.0
    ypos 1.0


# =====================================
# SPRITE ACTIVE / INACTIVE
# =====================================
#
# Tetap dipertahankan karena mungkin
# masih digunakan oleh file lain.
#
# Tidak dipanggil otomatis oleh callback.
# =====================================

transform sprite_active:
    linear 0.15 alpha 1.0 matrixcolor BrightnessMatrix(0.0)


transform sprite_inactive:
    linear 0.15 alpha 1.0 matrixcolor BrightnessMatrix(0.0)


# =====================================
# STATE
# =====================================

default cory_at_right = False
default speaker_history = []


# =====================================
# SPEAKER POSITION DATA
# =====================================

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

        "ghost": "ghost_pos",

        "shrimp": "shrimp_pos",
    }


# =====================================
# GET SPEAKER POSITION
# =====================================

init -10 python:

    def get_speaker_pos(tag):

        if tag == "cory":

            if store.cory_at_right:
                return store.cory_right_pos

            return store.cory_pos

        pos_name = SPEAKER_POSITIONS.get(
            tag,
            "npc_pos"
        )

        return getattr(
            store,
            pos_name
        )


# =====================================
# GET VISIBLE CHARACTERS
# =====================================

init -10 python:

    def get_visible_characters():

        visible = []

        for tag in SPEAKER_POSITIONS:

            if renpy.showing(tag):
                visible.append(tag)

        return visible


# =====================================
# GET CURRENT SPRITE ATTRIBUTE
# =====================================

init -10 python:

    def get_show_name(tag):

        current_attrs = renpy.get_attributes(
            tag,
            layer="master"
        )

        if not current_attrs:
            return tag

        return tag


# =====================================
# SPEAKER CALLBACK
# =====================================
#
# During the Mantis Shrimp scene, only the
# character currently speaking is shown.
# The last expression is restored when that
# character speaks again.
#
# =====================================

init -10 python:

    def speaker_callback(active_tag):

        def _callback(
            event,
            interact=True,
            **kwargs
        ):

            if not getattr(store, "mantis_scene_active", False):
                return

            if not hasattr(store, "mantis_last_sprite_attrs"):
                store.mantis_last_sprite_attrs = {}

            # Save the current expression of every sprite
            # before hiding the other speakers.
            for tag in ("mc", "cory", "shrimp"):

                if renpy.showing(tag):

                    attrs = renpy.get_attributes(
                        tag,
                        layer="master"
                    )

                    if attrs:
                        store.mantis_last_sprite_attrs[tag] = attrs

            # Only the active speaker remains visible.
            for tag in ("mc", "cory", "shrimp"):

                if tag != active_tag:
                    renpy.hide(tag)

            # If this speaker was hidden by the previous speaker,
            # restore its last known expression.
            if not renpy.showing(active_tag):

                attrs = store.mantis_last_sprite_attrs.get(
                    active_tag,
                    ()
                )

                if attrs:

                    image_name = active_tag + " " + " ".join(attrs)

                    renpy.show(
                        image_name,
                        at_list=[get_speaker_pos(active_tag)]
                    )

            return

        return _callback
