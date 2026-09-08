# =====================================================
# NPC Interaction — Character Selector
# =====================================================
#
# Screen + label ini menggantikan menu teks lama
# ("Ask as MC" / "Ask as Cory", "Confront as MC" /
# "Confront as Cory", "Choose who should ask...")
# di SEMUA interaksi NPC Chapter 1 & Chapter 2 yang
# memungkinkan player memilih MC atau Cory sebagai
# karakter yang berinteraksi dengan NPC.
#
# Asset (sudah ada, tidak ada asset baru dibuat):
#   game/images/backgrounds/chapter1/rotation_chara/
#       - McIdle.png   / McHover.png
#       - CoryIdle.png / CoryHover.png
#
# Cara pakai di label manapun (Chapter 1 & Chapter 2):
#
#     call select_interactor
#
#     if _return == "mc":
#         # ... lanjut interaksi sebagai MC
#     else:
#         # ... lanjut interaksi sebagai Cory
#         # (ingat: show Cory di sini pakai cory_right_pos,
#         # BUKAN cory_pos, supaya Cory ada di posisi kanan
#         # seperti MC saat dia jadi karakter yang berinteraksi)
#
# =====================================================

define ROTATION_CHARA_DIR = "images/backgrounds/chapter1/rotation_chara/"

# FIX: card pemilihan karakter sebelumnya terlalu besar
# (imagebutton full-size + teks size 40/28). Sekarang
# imagebutton di-zoom ke CHAR_SELECT_ZOOM dan teks/spacing
# diperkecil supaya proporsional di layar.
define CHAR_SELECT_ZOOM = 0.55

transform char_select_zoom:
    zoom CHAR_SELECT_ZOOM

transform char_select_scy_zoom:
    zoom 0.36


# -----------------------------------------------------
# Warning Screen: Chapter 3 High Stakes Warning
# -----------------------------------------------------

screen chapter3_rotation_warning():

    modal True
    zorder 250

    add "#000000dd"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 820
        ysize 450
        background Solid("#101b2bee")
        padding (36, 30)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text "⚠️ WARNING: DANGERS OF THE SEA ⚠️":
                xalign 0.5
                size 26
                color "#ffd700"
                bold True
                outlines [(2, "#000000", 0, 0)]

            text "The open sea is far more treacherous than the river or border. Your choice of companion now carries heavier consequences and higher stakes!":
                xalign 0.5
                size 18
                color "#ffffff"
                text_align 0.5

            vbox:
                xalign 0.5
                spacing 12

                text "☀️ [b]Day Cycle:[/b] Choosing the wrong companion could waste your precious items in vain, or cause wary fishes to reject your presence." size 16 color "#a0d2eb"

                text "🌙 [b]Night Cycle:[/b] Choosing the wrong companion can provoke deadly ambushes and plunge you directly into combat!" size 16 color "#ff9999"

            null height 10

            textbutton "I Understand — Choose Companion":
                xalign 0.5
                text_size 20
                text_bold True
                text_color "#ffffff"
                text_hover_color "#ffd700"
                action Return()


# -----------------------------------------------------
# Screen pemilihan karakter (Chapter 1 & 2: MC, Cory)
# -----------------------------------------------------

screen character_select_screen():

    modal True
    zorder 200

    # Dim latar belakang scene NPC yang sedang tampil,
    # supaya tombol pilihan lebih terbaca.
    add "#000000aa"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 24

        text "Who will interact?":
            xalign 0.5
            size 28
            color "#ffffff"
            outlines [(2, "#000000", 0, 0)]

        hbox:
            xalign 0.5
            spacing 60

            vbox:
                xalign 0.5
                spacing 6

                imagebutton:
                    idle ROTATION_CHARA_DIR + "McIdle.png"
                    hover ROTATION_CHARA_DIR + "McHover.png"
                    action Return("mc")
                    xalign 0.5
                    at char_select_zoom

                text "MC":
                    xalign 0.5
                    size 20
                    color "#ffffff"
                    outlines [(2, "#000000", 0, 0)]

            vbox:
                xalign 0.5
                spacing 6

                imagebutton:
                    idle ROTATION_CHARA_DIR + "CoryIdle.png"
                    hover ROTATION_CHARA_DIR + "CoryHover.png"
                    action Return("cory")
                    xalign 0.5
                    at char_select_zoom

                text "Cory":
                    xalign 0.5
                    size 20
                    color "#ffffff"
                    outlines [(2, "#000000", 0, 0)]


# -----------------------------------------------------
# Screen pemilihan 3 karakter (Chapter 3: MC, Cory, Scyllarus)
# -----------------------------------------------------

screen chapter3_character_select_screen():

    modal True
    zorder 200

    # Dim latar belakang scene NPC yang sedang tampil
    add "#000000aa"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 24

        text "Who will interact?":
            xalign 0.5
            size 28
            color "#ffffff"
            outlines [(2, "#000000", 0, 0)]

        hbox:
            xalign 0.5
            spacing 48

            # MC
            vbox:
                xalign 0.5
                spacing 6

                imagebutton:
                    idle ROTATION_CHARA_DIR + "McIdle.png"
                    hover ROTATION_CHARA_DIR + "McHover.png"
                    action Return("mc")
                    xalign 0.5
                    at char_select_zoom

                text "MC":
                    xalign 0.5
                    size 20
                    color "#ffffff"
                    outlines [(2, "#000000", 0, 0)]

            # Cory
            vbox:
                xalign 0.5
                spacing 6

                imagebutton:
                    idle ROTATION_CHARA_DIR + "CoryIdle.png"
                    hover ROTATION_CHARA_DIR + "CoryHover.png"
                    action Return("cory")
                    xalign 0.5
                    at char_select_zoom

                text "Cory":
                    xalign 0.5
                    size 20
                    color "#ffffff"
                    outlines [(2, "#000000", 0, 0)]

            # Scyllarus
            vbox:
                xalign 0.5
                spacing 6

                imagebutton:
                    idle safe_hotspot_image(ROTATION_CHARA_DIR + "ScyIdle.png", "images/npc/chapter2/mantis/ScyDefault.png")
                    hover safe_hotspot_image(ROTATION_CHARA_DIR + "ScyHover.png", "images/npc/chapter2/mantis/ScySmile.png")
                    action Return("scy")
                    xalign 0.5
                    at char_select_scy_zoom

                text "Scyllarus":
                    xalign 0.5
                    size 20
                    color "#ffffff"
                    outlines [(2, "#000000", 0, 0)]


# -----------------------------------------------------
# Label wrapper
# -----------------------------------------------------

label select_interactor:

    call screen character_select_screen

    return _return


label select_interactor_ch3:

    if not ch3_rotation_warning_shown:
        $ ch3_rotation_warning_shown = True
        call screen chapter3_rotation_warning

    call screen chapter3_character_select_screen

    return _return
