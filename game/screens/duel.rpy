screen rps_screen():

    modal True

    add battle_background

    text "ROCK PAPER SCISSORS":
        xalign 0.5
        yalign 0.10
        size 42

    imagebutton:
        idle rps_rock
        xpos 250
        ypos 620
        action Return("rock")

    imagebutton:
        idle rps_paper
        xpos 700
        ypos 620
        action Return("paper")

    imagebutton:
        idle rps_scissor
        xpos 1150
        ypos 620
        action Return("scissor")