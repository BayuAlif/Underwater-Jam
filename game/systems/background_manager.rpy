# =====================================
# Background Manager
# Mengatur background berdasarkan cycle
# =====================================

default current_background_day = None
default current_background_night = None

init python:

    def set_background(day_bg, night_bg):

        store.current_background_day = day_bg
        store.current_background_night = night_bg


    def get_background():

        if is_day():
            return store.current_background_day
        else:
            return store.current_background_night