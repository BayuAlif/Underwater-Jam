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


# -----------------------------------------------------
# Screen pemilihan karakter
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
# Label wrapper
#
# Dipanggil dengan `call select_interactor`.
# Hasil pilihan tersedia lewat `_return`
# ("mc" atau "cory") di label pemanggil.
# -----------------------------------------------------

label select_interactor:

    call screen character_select_screen

    return _return
