# =====================================
# Chapter 1
# =====================================

label chapter1:

    # Day Cycle
    $ set_cycle("day")
    $ load_area("beach")

    call beach_hub

    jump chapter2


# =====================================
# Beach Hub
# =====================================

label beach_hub:

    menu:

        "Ajak bicara NPC":
            call npc_selection
            jump beach_hub

        "Ambil Kerang" if is_day() and not shell_taken:
            $ add_item("shell")
            $ shell_taken = True
            "Kamu menemukan sebuah Kerang di pasir."
            jump beach_hub

        "Lanjut" if is_day() and day_objectives_complete():
            $ change_cycle()
            scene expression get_background()
            "Hari berganti menjadi malam."
            jump beach_hub

        "Lanjut" if is_night() and night_objectives_complete():
            "Malam ini selesai."
            return