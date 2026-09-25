screen negotiation_timer():

    modal True

    default time_left = 8.0

    timer 0.05 repeat True action SetScreenVariable(
        "time_left",
        max(0.0, time_left - 0.05)
    )

    if time_left <= 0.0:
        timer 0.01 action Return("timeout")

    frame:
        xalign 0.5
        yalign 0.12
        xsize 600
        padding (20, 15)

        vbox:
            spacing 10

            text "TIME LEFT: [int(time_left)]" size 28

            bar:
                value time_left
                range 8.0
                xsize 550
                ysize 25

            text "Choose your words carefully!" size 20

    frame:
        xalign 0.5
        yalign 0.55
        xsize 800
        padding (25, 25)

        vbox:
            spacing 15

            text "What do you propose?" size 30

            textbutton "I propose crustaceans and every creature in the sea hold hands until the end of time!":
                action Return("hands")

            textbutton "I propose that the crustaceans apologize to everyone in the sea!":
                action Return("apology")

            textbutton "I think this might be a great addition to your red collection! (Give red seaweed)":
                action Return("seaweed")
