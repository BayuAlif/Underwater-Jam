# =====================================
# SCREEN: WHO SHOULD ASK
# Memilih karakter yang akan bertanya ke NPC (MC atau Cory)
# =====================================

screen who_should_ask(title="Choose who should ask mr catfish!", subtitle="The answers it gives may vary based on its relationship with the character."):

    modal True
    zorder 100

    # Dim background overlay
    add "#00000088"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 650
        background Frame("#0f1d2acc", 20, 20)
        padding (40, 40, 40, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            text title:
                xalign 0.5
                size 36
                color "#ffffff"
                bold True

            text subtitle:
                xalign 0.5
                size 22
                color "#a0d2eb"
                text_align 0.5

            null height 15

            hbox:
                xalign 0.5
                spacing 80

                # MC Card
                vbox:
                    xalign 0.5
                    spacing 12

                    imagebutton:
                        idle Transform("images/backgrounds/chapter1/rotation_chara/McIdle.png", size=(300, 300))
                        hover Transform("images/backgrounds/chapter1/rotation_chara/McHover.png", size=(300, 300))
                        action Return("mc")

                    text "Ask as MC":
                        xalign 0.5
                        size 24
                        color "#ffffff"
                        bold True

                # Cory Card
                vbox:
                    xalign 0.5
                    spacing 12

                    imagebutton:
                        idle Transform("images/backgrounds/chapter1/rotation_chara/CoryIdle.png", size=(300, 300))
                        hover Transform("images/backgrounds/chapter1/rotation_chara/CoryHover.png", size=(300, 300))
                        action Return("cory")

                    text "Ask as Cory":
                        xalign 0.5
                        size 24
                        color "#ffffff"
                        bold True
