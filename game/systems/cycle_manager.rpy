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