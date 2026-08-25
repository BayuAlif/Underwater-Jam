# =====================================
# Area Manager
# Mengatur data tiap area
# =====================================

# Area yang sedang aktif
default current_area = None

init python:

    # =====================================
    # Data seluruh area
    # =====================================

    AREA_DATA = {

        "beach": {

            "day_bg": "background/night-bg.png",
            "night_bg": "background/FIXbgnight1.png",

        },

        "cave": {

            "day_bg": "background/FIXbgnight1.png",
            "night_bg": "background/FIXbgnight1.png",

        },

    }


    # =====================================
    # Load Area
    # =====================================

    def load_area(area_name):

        # Pastikan area ada
        if area_name not in AREA_DATA:
            raise Exception("Area '{}' tidak ditemukan.".format(area_name))

        # Simpan area aktif
        store.current_area = area_name

        # Ambil data area
        area = AREA_DATA[area_name]

        # Kirim background ke Background Manager
        set_background(
            area["day_bg"],
            area["night_bg"]
        )


    # =====================================
    # Ambil area aktif
    # =====================================

    def get_current_area():
        return store.current_area


    # =====================================
    # Ambil data area
    # =====================================

    def get_current_area_data():
        return AREA_DATA[store.current_area]