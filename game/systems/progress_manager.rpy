# =====================================
# Progress Manager
# Mengatur progress permainan
# =====================================

# Progress game
default current_day = 1
default depth_meters = 100

# Status NPC & Item Objective
default fish01_talked = False
default fish02_talked = False
default fish03_talked = False
default fish04_talked = False
default shell_taken = False
default trigger_combat = False
default interrogator = ""

init python:

    # Mengembalikan hari saat ini
    def get_current_day():
        return getattr(store, "current_day", 1)


    # Mengembalikan kedalaman saat ini
    def get_depth():
        return getattr(store, "depth_meters", 100)


    # Menambah hari
    def next_day():
        store.current_day = getattr(store, "current_day", 1) + 1


    # Menambah kedalaman
    def increase_depth(amount):
        store.depth_meters = getattr(store, "depth_meters", 100) + amount


    # =====================================
    # Objective Helpers - Beach (Chapter 1)
    # =====================================

    # Semua objective Day selesai:
    # ngobrol Fish01, Fish02, dan ambil Shell
    def day_objectives_complete():
        return (
            getattr(store, "fish01_talked", False)
            and getattr(store, "fish02_talked", False)
            and getattr(store, "shell_taken", False)
        )


    # Semua objective Night selesai:
    # ngobrol Buaya (Fish01/Fish04) dan Lele (Fish03)
    def night_objectives_complete():
        gator_done = getattr(store, "fish01_talked", False) or getattr(store, "fish04_talked", False)
        catfish_done = getattr(store, "fish03_talked", False)
        return gator_done and catfish_done
    
    # Untuk nandain NPC yang udah diajak bicara
    def mark_fish_talked(fish_number):
        if fish_number == 1:
            store.fish01_talked = True
        elif fish_number == 2:
            store.fish02_talked = True
        elif fish_number == 3:
            store.fish03_talked = True
        elif fish_number == 4:
            store.fish04_talked = True

    # Untuk ambil item Shell
    def collect_shell():
        if not getattr(store, "shell_taken", False):
            store.shell_taken = True
            add_item("Shell")
            return True
        return False

    # Fungsi untuk mengatur / mereset status combat
    def set_combat_trigger(status):
        store.trigger_combat = status
    
    # Fungsi untuk mencatat siapa interogator yang dipilih
    def set_interrogator(name):
        store.interrogator = name

    # Fungsi otomatis saat menyelesaikan satu Night Cycle
    def complete_night_cycle(depth_reward=50):
        next_day()
        increase_depth(depth_reward)
        change_cycle()