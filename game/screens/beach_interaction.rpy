# =====================================
# CHAPTER 1 - BEACH INTERACTION
#
# Day:
#   kiri  = Bass
#   kanan = Uceng
#   bawah = Bongkahan Emas
#
# Night:
#   kiri  = Lele
#   kanan = Gator
# =====================================


init python:

    # PENTING: file images/npc/chapter1/fish03_idle.png, fish03_hover.png,
    # fish04_idle.png, fish04_hover.png BELUM ADA di project (untuk hotspot
    # Lele & Gator saat Night Cycle). Supaya screen ini tidak crash saat
    # masuk Night Cycle, fungsi ini akan otomatis pakai gambar fish01/fish02
    # sebagai pengganti sementara SELAMA file asli belum tersedia.
    # Begitu kamu tambahkan file fish03_idle/hover & fish04_idle/hover yang
    # asli ke folder images/npc/chapter1/, kode ini otomatis memakainya
    # tanpa perlu diubah lagi.
    def safe_hotspot_image(path, fallback):

        if renpy.loadable(path):
            return path

        return fallback


screen beach_interaction():

    # =================================
    # BASS / LELE - IKAN KIRI
    # =================================

    if is_day():

        imagebutton:

            idle "images/npc/chapter1/fish01_idle.png"
            hover "images/npc/chapter1/fish01_hover.png"

            focus_mask True

            xpos 140
            ypos 210

            action Return("fish_left")


    else:

        imagebutton:

            idle safe_hotspot_image("images/npc/chapter1/fish03_idle.png", "images/npc/chapter1/fish01_idle.png")
            hover safe_hotspot_image("images/npc/chapter1/fish03_hover.png", "images/npc/chapter1/fish01_hover.png")

            focus_mask True

            xpos 180
            ypos 220

            action Return("fish_left")


    # =================================
    # UCENG / GATOR - IKAN KANAN
    # =================================

    if is_day():

        imagebutton:

            idle "images/npc/chapter1/fish02_idle.png"
            hover "images/npc/chapter1/fish02_hover.png"

            focus_mask True

            xpos 1150
            ypos 260

            action Return("fish_right")


    else:

        imagebutton:

            idle safe_hotspot_image("images/npc/chapter1/fish04_idle.png", "images/npc/chapter1/fish02_idle.png")
            hover safe_hotspot_image("images/npc/chapter1/fish04_hover.png", "images/npc/chapter1/fish02_hover.png")

            focus_mask True

            xpos 880
            ypos 220

            action Return("fish_right")


    # =================================
    # ITEM: BONGKAHAN EMAS (DAY)
    # =================================

    if is_day() and not gold_nugget_taken:

        imagebutton:

            idle "images/item/chapter1/gold_nugget_idle.png"
            hover "images/item/chapter1/gold_nugget_hover.png"

            focus_mask True

            xpos 810
            ypos 700

            action Return("gold_nugget")


    # =================================
    # ITEM: AMBALABU (NIGHT)
    # =================================

    if is_night() and not ambalabu_taken:

        imagebutton:

            idle "images/npc/chapter1/ambalabu_idle.png"
            hover "images/npc/chapter1/ambalabu_hover.png"

            focus_mask True

            xpos 800
            ypos 650

            action Return("ambalabu")


    # =================================
    # DAY COMPLETE
    # =================================

    if is_day() and day_objectives_complete():

        textbutton "Lanjut ke Night Cycle":

            xalign 0.5
            yalign 0.93

            action Return("continue_day")


    # =================================
    # NIGHT COMPLETE
    # =================================

    if is_night() and night_objectives_complete():

        textbutton "Lanjut":

            xalign 0.5
            yalign 0.93

            action Return("continue_night")