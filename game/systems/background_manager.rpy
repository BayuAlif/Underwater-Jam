# =====================================
# Background Manager
# Mengatur background berdasarkan cycle
# =====================================

default current_background_day = "images/backgrounds/chapter1/chapter1_beach_day.png"
default current_background_night = "images/backgrounds/chapter1/bg night1.jpg"

default current_dialogue_bg_day = "images/backgrounds/chapter1/bg day1_bordered.jpg"
default current_dialogue_bg_night = "images/backgrounds/chapter1/bg night1_bordered.jpg"

init python:

    def set_background(day_bg, night_bg):

        store.current_background_day = day_bg
        store.current_background_night = night_bg


    def set_dialogue_background(day_bg, night_bg):

        store.current_dialogue_bg_day = day_bg
        store.current_dialogue_bg_night = night_bg


    def get_background():

        if is_day():
            return store.current_background_day
        else:
            return store.current_background_night


    def get_dialogue_background():

        if is_day():
            return store.current_dialogue_bg_day
        else:
            return store.current_dialogue_bg_night