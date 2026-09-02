# =====================================
# CHAPTER 2 - INTERACTION SCREEN
# Day:
#   Kiri   = Mr. Wana (Arowana)
#   Kanan  = Mrs. Salmon
#   Tengah = Tiny Krill
# =====================================

screen chapter2_interaction():

    # =================================
    # MR. WANA / AROWANA - KIRI
    # =================================

    imagebutton:

        idle safe_hotspot_image("images/npc/chapter2/arowana_idle.png", "images/backgrounds/chapter 2/arowana_idle.png")
        hover safe_hotspot_image("images/npc/chapter2/arowana_hover.png", "images/backgrounds/chapter 2/arowana_hover.png")

        focus_mask True

        xpos 269
        ypos 112

        action Return("arowana")


    # =================================
    # MRS. SALMON - KANAN
    # =================================

    imagebutton:

        idle safe_hotspot_image("images/npc/chapter2/salmon_idle.png", "images/backgrounds/chapter 2/salmon_idle.png")
        hover safe_hotspot_image("images/npc/chapter2/salmon_hover.png", "images/backgrounds/chapter 2/salmon_hover.png")

        focus_mask True

        xpos 1282
        ypos 247

        action Return("salmon")


    # =================================
    # ITEM: TINY KRILL - TENGAH / BATU
    # =================================

    if not tiny_krill_taken:

        imagebutton:

            idle safe_hotspot_image("images/item/chapter2/tiny_krill_idle.png", "images/backgrounds/chapter 2/krill_idle.png")
            hover safe_hotspot_image("images/item/chapter2/tiny_krill_hover.png", "images/backgrounds/chapter 2/krill_hover.png")

            focus_mask True

            xpos 808
            ypos 731

            action Return("tiny_krill")


    # =================================
    # DAY COMPLETE
    # =================================

    if salmon_talked and wana_talked:

        textbutton "Lanjut":

            xalign 0.5
            yalign 0.93

            action Return("continue_chapter2_day")
