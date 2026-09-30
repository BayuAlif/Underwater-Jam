# Screens and variables for Chapter 4 Exploration

default ch4_scy_affection = 0
default ch4_cory_affection = 0
default ch4_leo_affection = 0

default ch4_rin_talked = False
default ch4_leo_talked = False

default ch4_chore1_done = False
default ch4_chore2_done = False
default ch4_chore1_companion = None
default ch4_chore2_companion = None

default ch4_game1_done = False
default ch4_game2_done = False
default ch4_game1_companion = None
default ch4_game2_companion = None

default ch4_ritual_companion = None
default ch4_chapter_complete = False

transform ch4_float_rin:
    subpixel True
    ease 3.2 yoffset -12
    ease 3.2 yoffset 0
    ease 3.2 yoffset 12
    ease 3.2 yoffset 0
    repeat

transform ch4_float_leo:
    subpixel True
    ease 2.6 yoffset 10
    ease 2.6 yoffset 0
    ease 2.6 yoffset -10
    ease 2.6 yoffset 0
    repeat

screen ch4_npc_exploration():
    modal True

    add "ch4_festival_day"

    # Header / Guidance HUD
    frame:
        xalign 0.5
        ypos 30
        xsize 860
        ysize 72
        background Frame(Solid("#021a2cCC"), 12, 12)
        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 2

        text _("Golden Sea Village - Festival Grounds"):
            xalign 0.5
            size 22
            bold True
            color "#f5f3c6"
            outlines [(2, "#011627", 0, 0)]

        text _("Talk with the seafolks to learn about the village and the golden fish."):
            xalign 0.5
            size 15
            color "#b8e2f2"
            outlines [(1, "#011627", 0, 0)]

    # 1. Chief Rin (Whale Shark) - Left side (pos: 174, 180)
    imagebutton:
        pos (174, 180)
        idle "rin_explore_idle"
        hover "rin_explore_hover"
        focus_mask True
        hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
        action Return("rin")
        at ch4_float_rin

    if ch4_rin_talked:
        text _("Chief Rin (Talked)"):
            xcenter 562
            ypos 145
            size 18
            bold True
            color "#4EFA74"
            outlines [(2, "#000000", 0, 0)]
    else:
        text _("Chief Rin"):
            xcenter 562
            ypos 145
            size 18
            bold True
            color "#ffdd80"
            outlines [(2, "#000000", 0, 0)]

    # 2. Miss Leo (Leopard Seal) - Right side (pos: 1246, 556)
    imagebutton:
        pos (1246, 556)
        idle "leo_explore_idle"
        hover "leo_explore_hover"
        focus_mask True
        hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
        action Return("leo")
        at ch4_float_leo

    if ch4_leo_talked:
        text _("Leo (Joined)"):
            xcenter 1320
            ypos 510
            size 18
            bold True
            color "#4EFA74"
            outlines [(2, "#000000", 0, 0)]
    else:
        text _("Curious Seal"):
            xcenter 1320
            ypos 510
            size 18
            bold True
            color "#ffdd80"
            outlines [(2, "#000000", 0, 0)]

    # If both talked to, show proceed button
    if ch4_rin_talked and ch4_leo_talked:
        frame:
            xalign 0.5
            ypos 970
            background Frame(Solid("#0d486bcc"), 8, 8)
            padding (25, 10)
            textbutton _("Begin Festival Preparation"):
                text_size 22
                text_bold True
                text_color "#ffeaa7"
                text_hover_color "#ffffff"
                action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("proceed")]

screen ch4_chore_exploration():
    modal True

    add "ch4_festival_day"

    # Header / Guidance HUD
    frame:
        xalign 0.5
        ypos 30
        xsize 860
        ysize 72
        background Frame(Solid("#021a2cCC"), 12, 12)
        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 2

        text _("Festival Preparation Grounds"):
            xalign 0.5
            size 22
            bold True
            color "#f5f3c6"
            outlines [(2, "#011627", 0, 0)]

        text _("Choose a chore to help prepare for tonight's festival."):
            xalign 0.5
            size 15
            color "#b8e2f2"
            outlines [(1, "#011627", 0, 0)]

    # Chore 1: Corals & Seaweeds (pos: 152, 674)
    imagebutton:
        pos (152, 674)
        idle "ch4_coral_idle"
        hover "ch4_coral_hover"
        focus_mask True
        hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
        action Return("chore1")

    if ch4_chore1_done:
        text _("Seaweeds & Corals (Done)"):
            xcenter 395
            ypos 630
            size 18
            bold True
            color "#4EFA74"
            outlines [(2, "#000000", 0, 0)]
    else:
        text _("Fetch Seaweeds & Corals"):
            xcenter 395
            ypos 630
            size 19
            bold True
            color "#ffeaa7"
            outlines [(2, "#000000", 0, 0)]

    # Chore 2: Woodbox & Planks (pos: 1381, 725)
    imagebutton:
        pos (1381, 725)
        idle "ch4_woodbox_idle"
        hover "ch4_woodbox_hover"
        focus_mask True
        hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
        action Return("chore2")

    if ch4_chore2_done:
        text _("Festival Stands (Done)"):
            xcenter 1589
            ypos 695
            size 18
            bold True
            color "#4EFA74"
            outlines [(2, "#000000", 0, 0)]
    else:
        text _("Assemble Festival Stands"):
            xcenter 1589
            ypos 695
            size 19
            bold True
            color "#ffeaa7"
            outlines [(2, "#000000", 0, 0)]

    # If both chores are done, show proceed to feast button
    if ch4_chore1_done and ch4_chore2_done:
        frame:
            xalign 0.5
            ypos 970
            background Frame(Solid("#0d486bcc"), 8, 8)
            padding (25, 10)
            textbutton _("All Tasks Completed! Join the Feast >>"):
                text_size 22
                text_bold True
                text_color "#ffeaa7"
                text_hover_color "#ffffff"
                action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("feast")]

screen ch4_festival_night_exploration():
    modal True

    add "ch4_festival_night"

    # Header / Guidance HUD
    frame:
        xalign 0.5
        ypos 30
        xsize 860
        ysize 72
        background Frame(Solid("#021a2cCC"), 12, 12)
        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 2

        text _("Golden Sea Village - Night Festival"):
            xalign 0.5
            size 22
            bold True
            color "#f5f3c6"
            outlines [(2, "#011627", 0, 0)]

        text _("Visit both festival booths to play games and prepare for the sacred ritual!"):
            xalign 0.5
            size 15
            color "#b8e2f2"
            outlines [(1, "#011627", 0, 0)]

    # Booth 1: Krill Catch Stall (pos: 439, 193)
    imagebutton:
        pos (439, 193)
        idle "krillstall_idle"
        hover "krillstall_hover"
        focus_mask True
        hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
        action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("game1")]

    if ch4_game1_done:
        text _("Krill Catch Stall (Done)"):
            xcenter 686
            ypos 150
            size 18
            bold True
            color "#4EFA74"
            outlines [(2, "#000000", 0, 0)]
    else:
        text _("Krill Catch Stall"):
            xcenter 686
            ypos 150
            size 18
            bold True
            color "#ffeaa7"
            outlines [(2, "#000000", 0, 0)]

    # Booth 2: Shell Shooter Booth (pos: 1240, 250)
    imagebutton:
        pos (1240, 250)
        idle "shootstall_idle"
        hover "shootstall_hover"
        focus_mask True
        hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")
        action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("game2")]

    if ch4_game2_done:
        text _("Shell Shooter Booth (Done)"):
            xcenter 1572
            ypos 210
            size 18
            bold True
            color "#4EFA74"
            outlines [(2, "#000000", 0, 0)]
    else:
        text _("Shell Shooter Booth"):
            xcenter 1572
            ypos 210
            size 18
            bold True
            color "#ffeaa7"
            outlines [(2, "#000000", 0, 0)]

    # If both games are completed, show ritual proceed button
    if ch4_game1_done and ch4_game2_done:
        frame:
            xalign 0.5
            ypos 970
            background Frame(Solid("#0d486bcc"), 8, 8)
            padding (25, 10)
            textbutton _("Attend the Sacred Effigy Ritual >>"):
                text_size 22
                text_bold True
                text_color "#ffeaa7"
                text_hover_color "#ffffff"
                action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("ritual")]
