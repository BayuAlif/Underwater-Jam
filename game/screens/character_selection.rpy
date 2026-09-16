screen choose_character():

    modal True

    add Solid("#00000099")

    text "Choose who should ask!":
        xalign 0.5
        yalign 0.08
        size 42

    text "The answers may vary depending on who asks.":
        xalign 0.5
        yalign 0.15
        size 24

    imagebutton:
        idle "images/backgrounds/chapter1/rotation_chara/McIdle.png"
        hover "images/backgrounds/chapter1/rotation_chara/McHover.png"
        xpos 180
        ypos 230
        action Return("mc")

    imagebutton:
        idle "images/backgrounds/chapter1/rotation_chara/CoryIdle.png"
        hover "images/backgrounds/chapter1/rotation_chara/CoryHover.png"
        xpos 900
        ypos 230
        action Return("cory")

    imagebutton:
        idle "images/backgrounds/chapter1/rotation_chara/ScyIdle.png"
        hover "images/backgrounds/chapter1/rotation_chara/ScyHover.png"
        action Return("cory")


    textbutton "Ask as MC":
        xalign 0.28
        yalign 0.83
        action Return("mc")

    textbutton "Ask as Cory":
        xalign 0.72
        yalign 0.83
        action Return("cory")

