# =====================================
# CHAPTER 2 - INTERACTION SCREEN
# Day:
#   Kiri  = Mrs. Salmon
#   Kanan = Mr. Wana (Arowana)
#   Item  = Tiny Krill
# =====================================

screen chapter2_interaction():

    # =================================
    # MRS. SALMON - KIRI
    # =================================

    imagebutton:

        idle safe_hotspot_image("images/npc/chapter2/salmon_idle.png", "images/npc/chapter1/fish01_idle.png")
        hover safe_hotspot_image("images/npc/chapter2/salmon_hover.png", "images/npc/chapter1/fish01_hover.png")

        focus_mask True

        xpos 220
        ypos 300

        action Return("salmon")


    # =================================
    # MR. WANA / AROWANA - KANAN
    # =================================

    imagebutton:

        idle safe_hotspot_image("images/npc/chapter2/arowana_idle.png", "images/npc/chapter1/fish02_idle.png")
        hover safe_hotspot_image("images/npc/chapter2/arowana_hover.png", "images/npc/chapter1/fish02_hover.png")

        focus_mask True

        xpos 1150
        ypos 260

        action Return("arowana")


    # =================================
    # ITEM: TINY KRILL
    # =================================

    if not tiny_krill_taken:

        imagebutton:

            idle safe_hotspot_image("images/item/chapter2/tiny_krill_idle.png", "images/item/chapter1/gold_nugget_idle.png")
            hover safe_hotspot_image("images/item/chapter2/tiny_krill_hover.png", "images/item/chapter1/gold_nugget_hover.png")

            focus_mask True

            xpos 800
            ypos 700

            action Return("tiny_krill")


    # =================================
    # DAY COMPLETE
    # =================================

    if salmon_talked and wana_talked:

        textbutton "Lanjut":

            xalign 0.5
            yalign 0.93

            action Return("continue_chapter2_day")
