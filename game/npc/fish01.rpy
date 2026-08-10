label fish01:

    "Seekor ikan mendekatimu."

    "Fish 01"
    "Halo manusia."

    menu:

        "Siapa kamu?":

            "Fish 01"
            "Aku tinggal di daerah Beach."

        "Kasih Kerang" if has_item("shell"):

            $ remove_item("shell")

            "Fish 01"
            "Terima kasih! Kerangnya enak sekali."

        "Ada yang bisa kubantu?":

            "Fish 01"
            "Kalau menemukan Kerang, bawakan padaku."

        "Pergi":

            "Fish 01"
            "Sampai jumpa."

    return