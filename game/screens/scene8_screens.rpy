# =========================================================
# UI SCENE 8: ROTASI IKAN (CHARACTER CARDS CHOICE)
# =========================================================

screen rotasi_ikan_select():
    add "#00000088" # Dim background

    text "PILIH KARAKTER UNTUK MEMULAI INTEROGASI" xalign 0.5 yalign 0.08 color "#ffffff" size 22 bold True

    hbox:
        xalign 0.5
        yalign 0.55
        spacing 40

        # KARTU 1 (Jose / Character 1)
        frame:
            xsize 280 ysize 450
            background Solid("#222222")
            vbox:
                xalign 0.5 yalign 0.5
                spacing 15
                imagebutton:
                    idle Solid("#ff4444", xsize=240, ysize=340)
                    action Return("select_jose")
                text "FIH FRIEND 1\n(Jose)" xalign 0.5 color "#ffffff" size 16 bold True

        # KARTU 2 (Cory / Character 2)
        frame:
            xsize 280 ysize 450
            background Solid("#222222")
            vbox:
                xalign 0.5 yalign 0.5
                spacing 15
                imagebutton:
                    idle Solid("#444444", xsize=240, ysize=340)
                    action Return("select_cory")
                text "FIH FRIEND 2\n(Cory)" xalign 0.5 color "#ffffff" size 16 bold True

        # KARTU 3 (Slot Kosong / Character 3)
        frame:
            xsize 280 ysize 450
            background Solid("#222222")
            vbox:
                xalign 0.5 yalign 0.5
                spacing 15
                imagebutton:
                    idle Solid("#888888", xsize=240, ysize=340)
                    action Return("select_char3")
                text "FIH FRIEND 3\n(Kankan)" xalign 0.5 color "#ffffff" size 16 bold True