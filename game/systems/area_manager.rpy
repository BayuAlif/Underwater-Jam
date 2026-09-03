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

            "day_bg": "bg room",
            "night_bg": "bg room",

            "day_dialogue_bg": "bg room",
            "night_dialogue_bg": "bg room",

        },


        "cave": {

            "day_bg": "bg room",
            "night_bg": "bg room",

            "day_dialogue_bg": "bg room",
            "night_dialogue_bg": "bg room",

        },


        # =====================================
        # CHAPTER 2 - NORTHERN CURRENT / BORDER
        # =====================================

        "border": {

            # -----------------------------
            # DAY
            # -----------------------------

            "day_bg":
                "images/backgrounds/chapter 2/bg day2.jpg",

            "day_dialogue_bg":
                "images/backgrounds/chapter 2/bg day2_bordered.jpg",


            # -----------------------------
            # NIGHT
            # -----------------------------

            "night_bg":
                "images/backgrounds/chapter 2/bg night2.jpg",

            "night_dialogue_bg":
                "images/backgrounds/chapter 2/bg night2_bordered.jpg",

        },

    }


    # =====================================
    # Load Area
    # =====================================

    def load_area(area_name):

        if area_name not in AREA_DATA:

            raise Exception(
                "Area '{}' tidak ditemukan.".format(area_name)
            )


        store.current_area = area_name

        area = AREA_DATA[area_name]


        # =================================
        # Background utama
        # =================================

        set_background(
            area["day_bg"],
            area["night_bg"]
        )


        # =================================
        # Background dialogue
        # =================================

        set_dialogue_background(
            area["day_dialogue_bg"],
            area["night_dialogue_bg"]
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