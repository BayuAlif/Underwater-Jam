screen inventory_screen():

    frame:
        xalign 0.5
        yalign 0.9

        hbox:
            spacing 30

            for item in inventory_items:
                text item
