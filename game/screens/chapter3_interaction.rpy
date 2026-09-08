# =====================================
# CHAPTER 3 - INTERACTION
#
# Day:
#   kiri   = Sea Bunny (Joruna Parva)
#   kanan  = Sea Turtle (Gran Hawk)
#   bawah  = Rainbow Algae
# =====================================

screen chapter3_interaction():

    # =================================
    # KIRI
    # DAY = SEA BUNNY
    # =================================

    if is_day():

        imagebutton:

            idle safe_hotspot_image(
                "images/backgrounds/chapter 3/seabunny_idle.png",
                "images/npc/chapter2/arowana_idle.png"
            )

            hover safe_hotspot_image(
                "images/backgrounds/chapter 3/seabunny_hover.png",
                "images/npc/chapter2/arowana_hover.png"
            )

            focus_mask True

            xpos 269
            ypos 112

            action Return("seabunny")


    # =================================
    # KANAN
    # DAY = SEA TURTLE (GRAN HAWK)
    # =================================

    if is_day():

        imagebutton:

            idle safe_hotspot_image(
                "images/backgrounds/chapter 3/turtle_idle.png",
                "images/npc/chapter2/salmon_idle.png"
            )

            hover safe_hotspot_image(
                "images/backgrounds/chapter 3/turtle_hover.png",
                "images/npc/chapter2/salmon_hover.png"
            )

            focus_mask True

            xpos 1282
            ypos 247

            action Return("seaturtle")


    # =================================
    # ITEM: RAINBOW ALGAE - DAY
    # =================================

    if is_day() and not rainbow_algae_taken:

        imagebutton:

            idle safe_hotspot_image(
                "images/backgrounds/chapter 3/algae_idle.png",
                "images/item/chapter2/tiny_krill_idle.png"
            )

            hover safe_hotspot_image(
                "images/backgrounds/chapter 3/algae_hover.png",
                "images/item/chapter2/tiny_krill_hover.png"
            )

            focus_mask True

            xpos 808
            ypos 731

            action Return("rainbow_algae")


    # =================================
    # ADVANCE CYCLE BUTTON
    # =================================

    if is_day():

        frame:
            xalign 0.98
            yalign 0.04
            background Solid("#101b2bee")
            padding (14, 8)

            textbutton "Wait for Nightfall →":
                text_size 18
                text_color "#ffffff"
                text_hover_color "#ffd700"
                action Return("continue_chapter3_day")
