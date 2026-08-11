# =====================================
# Cycle Manager
# Mengatur Day dan Night
# =====================================

default current_cycle = "day"

init python:

    def get_cycle():
        return store.current_cycle


    def is_day():
        return store.current_cycle == "day"


    def is_night():
        return store.current_cycle == "night"


    def set_cycle(cycle):

        if cycle not in ["day", "night"]:
            raise Exception("Cycle harus 'day' atau 'night'.")

        store.current_cycle = cycle


    def change_cycle():

        if store.current_cycle == "day":
            store.current_cycle = "night"
        else:
            store.current_cycle = "day"


screen day_night_hud():
    $ day_text = get_current_day() 
    $ depth_text = get_depth()

    frame:
        xalign 0.98
        yalign 0.02
        padding (15, 10)
        background Solid("#000000aa")

        vbox:
            spacing 2
            
            if is_day():
                text "{color=#f9d71c}☀️ HARI [day_text] - SIANG{/color}" size 18 bold True
            else:
                text "{color=#4a90e2}🌙 HARI [day_text] - MALAM{/color}" size 18 bold True
            
            text "Kedalaman: [depth_text]m" size 14 color "#ffffff"