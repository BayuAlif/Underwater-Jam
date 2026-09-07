# =====================================
# SPRITE DISPLAY SYSTEM
# =====================================
#
# Sprite show/hide dikontrol langsung
# oleh file chapter / NPC.
#
# speaker_callback() mengatur sprite
# khusus saat Mantis Shrimp scene aktif.
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
# MANTIS SCENE POSITIONS
# =====================================
#
# Posisi KHUSUS scene Mantis.
#
# Masing-masing karakter punya
# transform sendiri supaya bisa diatur
# tanpa mempengaruhi karakter lain.
#
# Mantis  = kiri
# MC      = kanan
# Cory    = kanan
#
# MC dan Cory memiliki posisi terpisah
# walaupun keduanya menggunakan sisi
# kanan.
#
# =====================================


# -------------------------------------
# MANTIS / SHRIMP
# -------------------------------------

transform mantis_scene_shrimp_pos:
    xanchor 0.50
    xpos 0.15
    yanchor 1.0
    ypos 1.0


# -------------------------------------
# MC - MANTIS SCENE
# -------------------------------------

transform mantis_scene_mc_pos:
    xanchor 0.69
    xpos 0.77
    yanchor 1.0
    ypos 1.0


# -------------------------------------
# CORY - MANTIS SCENE
# -------------------------------------

transform mantis_scene_cory_pos:
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


# Arowana expressions with different transparent margins.
# These offsets only apply to the affected expressions.
transform wana_mad_pos:
    xanchor 0.69
    xpos 0.212
    yanchor 1.0
    ypos 1.0


transform wana_squint_pos:
    xanchor 0.69
    xpos 0.249
    yanchor 1.0
    ypos 1.0


transform ghost_pos:
    xanchor 0.73
    xpos 0.28
    yanchor 1.0
    ypos 1.0


# =====================================
# NORMAL MANTIS POSITION
# =====================================

transform shrimp_pos:
    xanchor 0.50
    xpos 0.15
    yanchor 1.0
    ypos 1.0


# =====================================
# SPRITE ACTIVE / INACTIVE
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

        # =================================
        # MANTIS SCENE
        # =================================

        if getattr(
            store,
            "mantis_scene_active",
            False
        ):

            # MC menggunakan posisi khusus
            # scene Mantis.
            if tag == "mc":
                return store.mantis_scene_mc_pos

            # Cory menggunakan posisi khusus
            # scene Mantis.
            if tag == "cory":
                return store.mantis_scene_cory_pos

            # Mantis menggunakan posisi khusus
            # scene Mantis.
            if tag == "shrimp":
                return store.mantis_scene_shrimp_pos


        # =================================
        # NORMAL SCENE
        # =================================

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
# MANTIS SPRITE MEMORY
# =====================================
#
# Menyimpan expression terakhir dari
# MC, Cory, dan Mantis.
#
# Memory hanya digunakan untuk
# kebutuhan scene Mantis.
#
# =====================================

default mantis_last_sprite_attrs = {}


# =====================================
# SPEAKER CALLBACK
# =====================================
#
# NORMAL SCENE:
# Tidak melakukan apa-apa.
#
# MANTIS SCENE:
#
# Mantis tetap di kiri.
#
# MC:
#   MC      = kanan
#   Cory    = hidden
#
# Cory:
#   Cory    = kanan
#   MC      = hidden
#
# Mantis:
#   Mantis  = kiri
#   MC/Cory terakhir tetap di kanan.
#
# Callback TIDAK mengganti expression
# karakter yang sedang aktif.
#
# =====================================

init -10 python:

    def speaker_callback(active_tag):

        def _callback(
            event,
            interact=True,
            **kwargs
        ):

            # =================================
            # NORMAL SCENE
            # =================================
            #
            # Jangan menyentuh NPC lain
            # di luar scene Mantis.
            #

            if not getattr(
                store,
                "mantis_scene_active",
                False
            ):
                return


            # =================================
            # SAVE CURRENT EXPRESSIONS
            # =================================
            #
            # Hanya menyimpan expression
            # yang sedang benar-benar tampil.
            #

            for tag in (
                "mc",
                "cory",
                "shrimp"
            ):

                if renpy.showing(tag):

                    attrs = renpy.get_attributes(
                        tag,
                        layer="master"
                    )

                    if attrs:

                        store.mantis_last_sprite_attrs[
                            tag
                        ] = attrs


            # =================================
            # MC SPEAKING
            # =================================

            if active_tag == "mc":

                # Cory tidak boleh tampil bersamaan dengan MC.
                renpy.hide("cory")

                # Kalau MC belum tampil, pulihkan expression
                # terakhir yang sudah dipakai di scene Mantis.
                if not renpy.showing("mc"):
                    mc_attrs = store.mantis_last_sprite_attrs.get(
                        "mc",
                        ()
                    )

                    if mc_attrs:
                        renpy.show(
                            "mc " + " ".join(mc_attrs),
                            at_list=[
                                store.mantis_scene_mc_pos
                            ],
                            layer="master"
                        )

                return


            # =================================
            # CORY SPEAKING
            # =================================

            if active_tag == "cory":

                # MC tidak boleh tampil bersamaan dengan Cory.
                renpy.hide("mc")

                # Kalau Cory belum tampil, pulihkan expression
                # terakhir yang sudah dipakai di scene Mantis.
                if not renpy.showing("cory"):
                    cory_attrs = store.mantis_last_sprite_attrs.get(
                        "cory",
                        ()
                    )

                    if cory_attrs:
                        renpy.show(
                            "cory " + " ".join(cory_attrs),
                            at_list=[
                                store.mantis_scene_cory_pos
                            ],
                            layer="master"
                        )

                return


            # =================================
            # MANTIS SPEAKING
            # =================================

            if active_tag == "shrimp":

                # MC / Cory terakhir tetap
                # berada di sisi kanan.
                #
                # Jangan hide MC/Cory.

                return


            # =================================
            # OTHER NPC
            # =================================

            # Jangan menyentuh NPC lain.
            return


        return _callback