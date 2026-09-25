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

        if current_chapter >= 3 and current_cycle == "day":
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

        imagebutton:
            idle n_idle
            hover n_hover

            if n_xpos is not None:
                pos (n_xpos, n_ypos)
            else:
                xalign npc["x"]
                yalign npc["y"]

            focus_mask True

            action Return(npc["id"])

        if npc["id"] in explored_npcs:

            text "✓":
                if n_chk_x is not None:
                    pos (n_chk_x, n_chk_y)
                    anchor (0.5, 0.5)
                else:
                    xalign npc["x"]
                    yalign npc.get("check_y", max(0.04, npc["y"] - 0.16))
                size 36
                bold True
                color "#4EFA74"
                outlines [(2, "#000000", 0, 0)]

    if exploration_item and not item_collected:

        $ itm_xpos = exploration_item.get("xpos")
        $ itm_ypos = exploration_item.get("ypos")

        if current_chapter >= 3 and current_cycle == "day":
            $ itm_xpos = 809
            $ itm_ypos = 807

        imagebutton:
            idle exploration_item["idle"]
            hover exploration_item["hover"]

            if itm_xpos is not None:
                pos (itm_xpos, itm_ypos)
            else:
                xalign exploration_item.get("x", 0.50)
                yalign exploration_item.get("y", 0.83)

            focus_mask True

            action Return("item")

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
