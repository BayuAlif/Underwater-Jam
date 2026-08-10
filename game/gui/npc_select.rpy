screen npc_select():

    tag npc_select

    add Solid("#0008")

    vbox:

        xalign 0.5
        yalign 0.5
        spacing 40

        text "Pilih NPC":
            xalign 0.5
            size 50

        hbox:

            xalign 0.5
            spacing 120

            if is_day():

                imagebutton:

                    idle "images/npc/fish01_idle.png"
                    hover "images/npc/fish01_hover.png"

                    focus_mask True

                    at Transform(zoom=0.60)

                    action Return("fish01")


                imagebutton:

                    idle "images/npc/fish02_idle.png"
                    hover "images/npc/fish02_hover.png"

                    focus_mask True

                    at Transform(zoom=0.60)

                    action Return("fish02")

            else:

                imagebutton:

                    idle "images/npc/fish03_idle.png"
                    hover "images/npc/fish03_hover.png"

                    focus_mask True

                    at Transform(zoom=0.60)

                    action Return("fish03")


                imagebutton:

                    idle "images/npc/fish04_idle.png"
                    hover "images/npc/fish04_hover.png"

                    focus_mask True

                    at Transform(zoom=0.60)

                    action Return("fish04")

        textbutton "Kembali":

            xalign 0.5

            action Return(None)