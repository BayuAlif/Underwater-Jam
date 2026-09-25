screen character_question_visual(title, subtitle):

    modal True

    add Solid("#000000B8")

    text title:
        xalign 0.5
        yalign 0.08
        size 42
        bold True

    text subtitle:
        xalign 0.5
        yalign 0.15
        size 24

    if current_chapter >= 3:
        imagebutton:
            idle "images/characters/rotasi/McIdle.png"
            hover "images/characters/rotasi/McHover.png"
            at selector_3_mc
            action Return("mc")

        imagebutton:
            idle "images/characters/rotasi/CoryIdle.png"
            hover "images/characters/rotasi/CoryHover.png"
            at selector_3_cory
            action Return("cory")

        imagebutton:
            idle "images/characters/rotasi/ClarusIdle.png"
            hover "images/characters/rotasi/ClarusHover.png"
            at selector_3_clarus
            action Return("scyllarus")
    else:
        imagebutton:
            idle "images/characters/rotasi/McIdle.png"
            hover "images/characters/rotasi/McHover.png"
            at selector_mc
            action Return("mc")

        imagebutton:
            idle "images/characters/rotasi/CoryIdle.png"
            hover "images/characters/rotasi/CoryHover.png"
            at selector_cory
            action Return("cory")

screen choose_interactor(title, subtitle):
    use character_question_visual(title, subtitle)

screen character_question_select(title):
    use character_question_visual(title, "Choose by character.")

screen ch4_companion_select(title, subtitle="Choose your companion."):

    modal True

    add Solid("#000000B8")

    text title:
        xalign 0.5
        yalign 0.07
        size 42
        bold True

    text subtitle:
        xalign 0.5
        yalign 0.14
        size 24

    imagebutton:
        idle "images/characters/rotasi/ClarusIdle.png"
        hover "images/characters/rotasi/ClarusHover.png"
        at selector_3_mc
        action Return("scy")

    imagebutton:
        idle "images/characters/rotasi/CoryIdle.png"
        hover "images/characters/rotasi/CoryHover.png"
        at selector_3_cory
        action Return("cory")

    imagebutton:
        idle "images/characters/rotasi/LeoIdle.png"
        hover "images/characters/rotasi/LeoHover.png"
        at selector_3_clarus
        action Return("leo")
