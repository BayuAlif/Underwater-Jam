# =====================================
# Progress Manager
# Mengatur progress permainan
# =====================================

# Progress game
default current_day = 1
default depth_meters = 100

# =====================================
# Chapter 1 - Beach Objective Flags
# Menandai NPC mana saja yang sudah
# diajak bicara, dipakai untuk mengunci
# opsi "Lanjut" di Beach sampai semua
# objective selesai.
# =====================================

default fish01_talked = False
default fish02_talked = False
default fish03_talked = False
default fish04_talked = False

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


    # =====================================
    # Objective Helpers - Beach (Chapter 1)
    # =====================================

    # Semua objective Day selesai:
    # ngobrol Fish01, Fish02, dan ambil Shell
    def day_objectives_complete():
        return (
            store.fish01_talked
            and store.fish02_talked
            and store.shell_taken
        )


    # Semua objective Night selesai:
    # ngobrol Fish03 dan Fish04
    def night_objectives_complete():
        return (
            store.fish03_talked
            and store.fish04_talked
        )