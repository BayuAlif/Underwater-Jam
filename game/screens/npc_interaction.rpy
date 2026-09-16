screen choose_interactor(title, subtitle):

    modal True

    if current_chapter == 1:
        add "ch1_dialogue"
    else:
        add "ch2_dialogue"

    add Solid("#00000099")


    text title:
        xalign 0.5
        yalign 0.09
        size 42
        bold True


    text subtitle:
        xalign 0.5
        yalign 0.15
        size 24


    add "mc default" at selector_mc

    add "cory talk" at selector_cory


    textbutton "Ask as MC":
        xalign 0.25
        yalign 0.82

        xsize 350
        ysize 80

        action Return("mc")


    textbutton "Ask as Cory":
        xalign 0.75
        yalign 0.82

        xsize 350
        ysize 80

        action Return("cory")