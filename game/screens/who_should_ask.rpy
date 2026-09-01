# =====================================
# SCREEN: WHO SHOULD ASK
# Memilih karakter yang akan bertanya ke NPC (MC atau Cory)
# =====================================

screen who_should_ask(title="Choose who should ask mr catfish!", subtitle="The answers it gives may vary based on its relationship with the character."):

    modal True
    zorder 100

    # Dim background overlay
    add "#000000aa"

    # Header Text
    vbox:
        xalign 0.5
        ypos 70
        spacing 12

        text title:
            xalign 0.5
            size 42
            color "#ffffff"
            bold True
            outlines [ (2, "#000000bb", 0, 0) ]

        text subtitle:
            xalign 0.5
            size 22
            color "#a0d2eb"
            text_align 0.5
            outlines [ (1, "#000000aa", 0, 0) ]

    # Character choices (Left: MC, Right: Cory)
    hbox:
        xalign 0.5
        yalign 0.62
        spacing 200

        # MC Card (Left)
        vbox:
            xalign 0.5
            spacing 16

            imagebutton:
                xalign 0.5
                idle Transform("images/backgrounds/chapter1/rotation_chara/McIdle.png", size=(540, 540))
                hover Transform("images/backgrounds/chapter1/rotation_chara/McHover.png", size=(540, 540))
                action Return("mc")

            textbutton "Ask as MC":
                xalign 0.5
                text_size 28
                text_bold True
                text_color "#ffffff"
                text_hover_color "#ffd700"
                text_outlines [ (2, "#000000bb", 0, 0) ]
                action Return("mc")

        # Cory Card (Right)
        vbox:
            xalign 0.5
            spacing 16

            imagebutton:
                xalign 0.5
                idle Transform("images/backgrounds/chapter1/rotation_chara/CoryIdle.png", size=(540, 540))
                hover Transform("images/backgrounds/chapter1/rotation_chara/CoryHover.png", size=(540, 540))
                action Return("cory")

            textbutton "Ask as Cory":
                xalign 0.5
                text_size 28
                text_bold True
                text_color "#ffffff"
                text_hover_color "#ffd700"
                text_outlines [ (2, "#000000bb", 0, 0) ]
                action Return("cory")

