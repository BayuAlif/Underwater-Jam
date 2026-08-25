# =========================================================
# UI SCENE 8: ROTASI IKAN (CHARACTER CARDS CHOICE)
# =========================================================

screen rotasi_ikan_select(title="PILIH KARAKTER UNTUK MEMULAI INTEROGASI", subtitle="Pilih karakter yang akan berbicara"):
    modal True
    zorder 200

    add "#000000bb" # Dim background

    vbox:
        xalign 0.5
        yalign 0.08
        spacing 10

        text title:
            xalign 0.5
            color "#ffffff"
            size 28
            bold True
            outlines [(2, "#000000", 0, 0)]

        if subtitle:
            text subtitle:
                xalign 0.5
                color "#f9d71c"
                size 18
                outlines [(1, "#000000", 0, 0)]

    hbox:
        xalign 0.5
        yalign 0.58
        spacing 80

        # KARTU 1: MC
        vbox:
            xalign 0.5
            spacing 12

            imagebutton:
                idle Transform("images/Rotation/McIdle.png", zoom=0.55)
                hover Transform("images/Rotation/McHover.png", zoom=0.55)
                focus_mask True
                action Return("mc")

            text "MC" xalign 0.5 color "#ffffff" size 24 bold True outlines [(2, "#000000", 0, 0)]

        # KARTU 2: CORY
        vbox:
            xalign 0.5
            spacing 12

            imagebutton:
                idle Transform("images/Rotation/CoryIdle.png", zoom=0.55)
                hover Transform("images/Rotation/CoryHover.png", zoom=0.55)
                focus_mask True
                action Return("cory")

            text "CORY" xalign 0.5 color "#00a86b" size 24 bold True outlines [(2, "#000000", 0, 0)]