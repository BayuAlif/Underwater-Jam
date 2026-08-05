# =====================================
# Progress Manager
# Mengatur progress permainan
# =====================================

# Progress game
default current_day = 1
default depth_meters = 100

init python:

    # Mengembalikan hari saat ini
    def get_current_day():
        return store.current_day


    # Mengembalikan kedalaman saat ini
    def get_depth():
        return store.depth_meters


    # Menambah hari
    def next_day():
        store.current_day += 1


    # Menambah kedalaman
    def increase_depth(amount):
        store.depth_meters += amount