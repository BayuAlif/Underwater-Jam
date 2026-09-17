screen exploration_screen():

    modal True

    if current_chapter == 1:

        if current_cycle == "day":
            add "ch1_day"
        else:
            add "ch1_night"

    else:

        if current_cycle == "day":
            add "ch2_day"
        else:
            add "ch2_night"


    for npc in exploration_npcs:

        imagebutton:
            idle npc["idle"]
            hover npc["hover"]

            xalign npc["x"]
            yalign npc["y"]

            focus_mask True

            action Return(npc["id"])


        if npc["id"] in explored_npcs:

            text "✓":
                xalign npc["x"]
                yalign npc["y"] - 0.20
                size 34
                bold True


    if exploration_item and not item_collected:

        imagebutton:
            idle exploration_item["idle"]
            hover exploration_item["hover"]

            xalign 0.50
            yalign 0.83

            focus_mask True

            action Return("item")


    if exploration_complete():

        textbutton "Continue":

            xalign 0.93
            yalign 0.94

            action Return("continue")

# Chapter 2 uses the same point-and-click exploration data model as Chapter 1.
screen chapter2_exploration_day():
    use exploration_screen

screen chapter2_exploration_night():
    use exploration_screen
