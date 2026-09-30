screen exploration_screen():

    modal True

    if current_chapter == 1:

        if current_cycle == "day":
            add "ch1_day"
        else:
            add "ch1_night"

    elif current_chapter == 2:

        if current_cycle == "day":
            add "ch2_day"
        else:
            add "ch2_night"

    else:

        if current_cycle == "day":
            add "ch3_day"
        else:
            add "ch3_night"

    for npc in exploration_npcs:

        $ n_idle = npc["idle"]
        $ n_hover = npc["hover"]
        $ n_xpos = npc.get("xpos")
        $ n_ypos = npc.get("ypos")
        $ n_chk_x = npc.get("check_xpos")
        $ n_chk_y = npc.get("check_ypos")

        # Coordinate mappings for checkmarks across all chapters:
        if current_chapter == 1 and current_cycle == "day":
            if npc["id"] == "bass":
                $ n_chk_x = 608
                $ n_chk_y = 270
            elif npc["id"] == "uceng":
                $ n_chk_x = 1384
                $ n_chk_y = 480
        elif current_chapter == 1 and current_cycle == "night":
            if npc["id"] == "lele":
                $ n_chk_x = 480
                $ n_chk_y = 265
            elif npc["id"] == "gator":
                $ n_chk_x = 1100
                $ n_chk_y = 210
        elif current_chapter == 2 and current_cycle == "day":
            if npc["id"] == "salmon":
                $ n_chk_x = 1445
                $ n_chk_y = 160
            elif npc["id"] == "arowana":
                $ n_chk_x = 472
                $ n_chk_y = 180
        elif current_chapter == 2 and current_cycle == "night":
            if npc["id"] == "ghostfish":
                $ n_chk_x = 730
                $ n_chk_y = 80
            elif npc["id"] == "mantis":
                $ n_chk_x = 1500
                $ n_chk_y = 195
        elif current_chapter >= 3 and current_cycle == "day":
            if npc["id"] in ("hawk", "turtle"):
                $ n_idle = "turtle idle"
                $ n_hover = "turtle hover"
                $ n_xpos = 307
                $ n_ypos = 162
                $ n_chk_x = 518
                $ n_chk_y = 120
            elif npc["id"] in ("bunny", "seabunny"):
                $ n_idle = "seabunny idle"
                $ n_hover = "seabunny hover"
                $ n_xpos = 1370
                $ n_ypos = 592
                $ n_chk_x = 1411
                $ n_chk_y = 550
        elif current_chapter >= 3 and current_cycle == "night":
            if npc["id"] in ("dunge", "crab"):
                $ n_idle = "crab idle"
                $ n_hover = "crab hover"
                $ n_xpos = 456
                $ n_ypos = 762
                $ n_chk_x = 690
                $ n_chk_y = 730
            elif npc["id"] in ("teto", "goby"):
                $ n_idle = "teto idle"
                $ n_hover = "teto hover"
                $ n_xpos = 860
                $ n_ypos = 374
                $ n_chk_x = 1089
                $ n_chk_y = 340

        $ n_name = npc.get("name", "NPC")
        if npc["id"] == "bass":
            $ n_name = "Ms. Bass"
        elif npc["id"] == "uceng":
            $ n_name = "Uceng"
        elif npc["id"] == "lele":
            $ n_name = "Lele"
        elif npc["id"] == "gator":
            $ n_name = "Gator"
        elif npc["id"] == "salmon":
            $ n_name = "Mrs. Salmon"
        elif npc["id"] == "arowana":
            $ n_name = "Mr. Wana"
        elif npc["id"] == "ghostfish":
            $ n_name = "Ghostfish"
        elif npc["id"] == "mantis":
            $ n_name = "Mantis Shrimp"
        elif npc["id"] in ("hawk", "turtle"):
            $ n_name = "Elder Turtle"
        elif npc["id"] in ("bunny", "seabunny"):
            $ n_name = "Sea Bunny"
        elif npc["id"] in ("dunge", "crab"):
            $ n_name = "Dunge Crab"
        elif npc["id"] in ("teto", "goby"):
            $ n_name = "Teto"
        elif npc["id"] == "leo":
            $ n_name = "Leo"
        elif npc["id"] == "rin":
            $ n_name = "Chief Rin"

        $ is_joined = (npc.get("joined", False) or npc["id"] == "leo")

        imagebutton:
            idle n_idle
            hover n_hover

            if n_xpos is not None:
                pos (n_xpos, n_ypos)
            else:
                xalign npc["x"]
                yalign npc["y"]

            focus_mask True
            hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")

            action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return(npc["id"])]

        if npc["id"] in explored_npcs:
            if is_joined:
                if n_chk_x is not None:
                    text _(n_name + " (Joined)"):
                        xcenter n_chk_x
                        ypos n_chk_y
                        size 18
                        bold True
                        color "#4EFA74"
                        outlines [(2, "#000000", 0, 0)]
                else:
                    text _(n_name + " (Joined)"):
                        xalign npc["x"]
                        yalign npc.get("check_y", max(0.04, npc["y"] - 0.16))
                        size 18
                        bold True
                        color "#4EFA74"
                        outlines [(2, "#000000", 0, 0)]
            else:
                if n_chk_x is not None:
                    text _(n_name + " (Talked)"):
                        xcenter n_chk_x
                        ypos n_chk_y
                        size 18
                        bold True
                        color "#4EFA74"
                        outlines [(2, "#000000", 0, 0)]
                else:
                    text _(n_name + " (Talked)"):
                        xalign npc["x"]
                        yalign npc.get("check_y", max(0.04, npc["y"] - 0.16))
                        size 18
                        bold True
                        color "#4EFA74"
                        outlines [(2, "#000000", 0, 0)]
        else:
            if n_chk_x is not None:
                text _(n_name):
                    xcenter n_chk_x
                    ypos n_chk_y
                    size 18
                    bold True
                    color "#ffeaa7"
                    outlines [(2, "#000000", 0, 0)]
            else:
                text _(n_name):
                    xalign npc["x"]
                    yalign npc.get("check_y", max(0.04, npc["y"] - 0.16))
                    size 18
                    bold True
                    color "#ffeaa7"
                    outlines [(2, "#000000", 0, 0)]

    if exploration_item:

        $ itm_xpos = exploration_item.get("xpos")
        $ itm_ypos = exploration_item.get("ypos")
        $ itm_idle = exploration_item.get("idle", "seaweed idle")
        $ itm_hover = exploration_item.get("hover", "seaweed hover")
        if current_chapter >= 3 and current_cycle == "day":
            $ itm_xpos = 809
            $ itm_ypos = 807
        elif current_chapter >= 3 and current_cycle == "night":
            $ itm_xpos = 862
            $ itm_ypos = 598
            $ itm_idle = "seaweed idle"
            $ itm_hover = "seaweed hover"

        if not item_collected:
            imagebutton:
                idle itm_idle
                hover itm_hover

                if itm_xpos is not None:
                    pos (itm_xpos, itm_ypos)
                else:
                    xalign exploration_item.get("x", 0.50)
                    yalign exploration_item.get("y", 0.83)

                focus_mask True
                hovered Play("sound", "audio/sfx/pixel_ui_1.mp3")

                action [Play("sound", "audio/sfx/pixel_ui_2.mp3"), Return("item")]
        else:
            imagebutton:
                idle itm_idle
                hover itm_idle
                at Transform(alpha=0.55)

                if itm_xpos is not None:
                    pos (itm_xpos, itm_ypos)
                else:
                    xalign exploration_item.get("x", 0.50)
                    yalign exploration_item.get("y", 0.83)

                focus_mask True

                action NullAction()

    if exploration_complete():

        textbutton _("Continue >>"):
            xalign 0.93
            yalign 0.94
            text_size 28
            text_bold True
            text_color "#ffffff"
            text_hover_color "#ffd700"
            text_outlines [(2, "#000000", 0, 0)]
            action Return("continue")

screen chapter2_exploration_day():
    use exploration_screen

screen chapter2_exploration_night():
    use exploration_screen

screen chapter3_exploration_day():
    use exploration_screen

screen chapter3_exploration_night():
    use exploration_screen
