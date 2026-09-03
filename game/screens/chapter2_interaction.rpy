# =====================================
# CHAPTER 2 - INTERACTION
#
# Day:
#   kiri   = Mr. Wana (Arowana)
#   kanan  = Mrs. Salmon
#   bawah  = Tiny Krill
#
# Night:
#   kiri   = Ghost Fish
#   kanan  = Mantis Shrimp
#   bawah  = Coal Tar
# =====================================


screen chapter2_interaction():


    # =================================
    # KIRI
    # DAY   = AROWANA
    # NIGHT = GHOST FISH
    # =================================

    if is_day():

        imagebutton:

            idle safe_hotspot_image(
                "images/npc/chapter2/arowana_idle.png",
                "images/backgrounds/chapter 2/arowana_idle.png"
            )

            hover safe_hotspot_image(
                "images/npc/chapter2/arowana_hover.png",
                "images/backgrounds/chapter 2/arowana_hover.png"
            )

            focus_mask True

            xpos 269
            ypos 112

            action Return("arowana")


    else:

        imagebutton:

            idle safe_hotspot_image(
                "images/npc/chapter2/ghost_idle.png",
                "images/backgrounds/chapter 2/ghost_idle.png"
            )

            hover safe_hotspot_image(
                "images/npc/chapter2/ghost_hover.png",
                "images/backgrounds/chapter 2/ghost_hover.png"
            )

            focus_mask True

            xpos 400
            ypos 112

            action Return("ghostfish")


    # =================================
    # KANAN
    # DAY   = SALMON
    # NIGHT = MANTIS SHRIMP
    # =================================

    if is_day():

        imagebutton:

            idle safe_hotspot_image(
                "images/npc/chapter2/salmon_idle.png",
                "images/backgrounds/chapter 2/salmon_idle.png"
            )

            hover safe_hotspot_image(
                "images/npc/chapter2/salmon_hover.png",
                "images/backgrounds/chapter 2/salmon_hover.png"
            )

            focus_mask True

            xpos 1282
            ypos 247

            action Return("salmon")


    else:

        imagebutton:

            idle safe_hotspot_image(
                "images/npc/chapter2/mantis_idle.png",
                "images/backgrounds/chapter 2/mantis_hover.png"
            )

            hover safe_hotspot_image(
                "images/npc/chapter2/mantis_hover.png",
                "images/backgrounds/chapter 2/mantis_hover.png"
            )

            focus_mask True

            xpos 1440
            ypos 240

            action Return("mantis_shrimp")


    # =================================
    # ITEM: TINY KRILL - DAY
    # =================================

    if is_day() and not tiny_krill_taken:

        imagebutton:

            idle safe_hotspot_image(
                "images/item/chapter2/tiny_krill_idle.png",
                "images/backgrounds/chapter 2/krill_idle.png"
            )

            hover safe_hotspot_image(
                "images/item/chapter2/tiny_krill_hover.png",
                "images/backgrounds/chapter 2/krill_hover.png"
            )

            focus_mask True

            xpos 808
            ypos 731

            action Return("tiny_krill")


    # =================================
    # ITEM: COAL TAR - NIGHT
    # =================================

    if is_night() and not coal_tar_taken:

        imagebutton:

            idle safe_hotspot_image(
                "images/item/chapter2/coal_idle.png",
                "images/backgrounds/chapter 2/coal_idle.png"
            )

            hover safe_hotspot_image(
                "images/item/chapter2/coal_hover.png",
                "images/backgrounds/chapter 2/coal_hover.png"
            )

            focus_mask True

            xpos 1125
            ypos 560

            action Return("coal_tar")


    # =================================
    # DAY COMPLETE
    # =================================

    if is_day() and chapter2_day_objectives_complete():

        textbutton "Lanjut":

            xalign 0.5
            yalign 0.93

            action Return("continue_chapter2_day")


    # =================================
    # NIGHT COMPLETE
    # =================================

    if is_night() and chapter2_night_objectives_complete():

        textbutton "Lanjut":

            xalign 0.5
            yalign 0.93

            action Return("continue_chapter2_night")


# =========================================================
# PENANGAN HASIL RETURN SCREEN
# =========================================================

label chapter2_hub_interaction:

    call screen chapter2_interaction
    $ result = _return

    if result == "arowana":
        if renpy.has_label("arowana"):
            call arowana
        elif renpy.has_label("arowana_talk"):
            call arowana_talk
        else:
            "Arowana belum siap berbicara."

    elif result == "salmon":
        if renpy.has_label("salmon"):
            call salmon
        elif renpy.has_label("salmon_talk"):
            call salmon_talk
        else:
            "Salmon belum siap berbicara."

    elif result == "tiny_krill":
        $ tiny_krill_taken = True
        $ add_item("tiny_krill")
        "Mendapatkan Tiny Krill!"

    elif result == "ghostfish":
        if renpy.has_label("ghostfish"):
            call ghostfish
        else:
            "Ghostfish belum siap berbicara."

    elif result == "mantis_shrimp":
        jump mantis_shrimp

    elif result == "coal_tar":
        $ coal_tar_taken = True
        $ add_item("coal_tar")
        "Mendapatkan Coal Tar!"

    elif result == "continue_chapter2_day":
        $ set_cycle("night")

    elif result == "continue_chapter2_night":
        jump mantis_shrimp

    jump chapter2_hub_interaction