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
