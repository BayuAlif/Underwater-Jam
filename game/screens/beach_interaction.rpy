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

            xpos 140
            ypos 210

            xsize 560
            ysize 560

            action Return("fish_left")


    else:

        imagebutton:

            idle safe_hotspot_image("images/npc/chapter1/fish03_idle.png", "images/npc/chapter1/fish01_idle.png")
            hover safe_hotspot_image("images/npc/chapter1/fish03_hover.png", "images/npc/chapter1/fish01_hover.png")

            xpos 140
            ypos 210

            xsize 560
            ysize 560

            action Return("fish_left")


    # =================================
    # UCENG / GATOR - IKAN KANAN
    # =================================

    if is_day():

        imagebutton:

            idle "images/npc/chapter1/fish02_idle.png"
            hover "images/npc/chapter1/fish02_hover.png"

            xpos 1150
            ypos 260

            xsize 350
            ysize 350

            action Return("fish_right")


    else:

        imagebutton:

            idle safe_hotspot_image("images/npc/chapter1/fish04_idle.png", "images/npc/chapter1/fish02_idle.png")
            hover safe_hotspot_image("images/npc/chapter1/fish04_hover.png", "images/npc/chapter1/fish02_hover.png")

            xpos 1150
            ypos 260

            xsize 350
            ysize 350

            action Return("fish_right")


    # =================================
    # BONGKAHAN EMAS
    # =================================

    if not gold_nugget_taken:

        imagebutton:

            idle "images/item/chapter1/gold_nugget_idle.png"
            hover "images/item/chapter1/gold_nugget_hover.png"

            xpos 810
            ypos 700

            xsize 180
            ysize 140

            action Return("gold_nugget")


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