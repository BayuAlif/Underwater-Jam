# =====================================
# Progress Manager
# =====================================

default current_day = 1
default depth_meters = 100


# =====================================
# Clue System
# =====================================

default clues = []


# =====================================
# Chapter 1 NPC Flags
# =====================================

default fish01_talked = False
default fish02_talked = False
default fish03_talked = False
default fish04_talked = False


# =====================================
# Chapter 2 NPC Flags
# =====================================

default salmon_talked = False
default wana_talked = False

# Flag tambahan dari dialog NPC
default uceng_told_lore = False


# =====================================
# Chapter 2 Night Flags
# =====================================

default ghost_talked = False
default shrimp_confronted = False
default shrimp_weakened = False
default shrimp_duel_won = False
default shrimp_joined = False

# =====================================
# Chapter 3 Flags
# =====================================

default seabunny_talked = False
default seaturtle_talked = False
default ch3_rotation_warning_shown = False
default bunny_hugged = False
default bunny_fed = False


init python:

    # =================================
    # Clue Management
    # =================================

    def add_clue(clue):

        if clue not in store.clues:

            store.clues.append(clue)


    def has_clue(clue):

        return clue in store.clues


    # =================================
    # General Progress
    # =================================

    def get_current_day():

        return store.current_day


    def get_depth():

        return store.depth_meters


    def next_day():

        store.current_day += 1


    def increase_depth(amount):

        store.depth_meters += amount


    # =================================
    # CHAPTER 1 DAY OBJECTIVE
    # =================================
    #
    # Bass + Uceng + Gold
    #

    def day_objectives_complete():

        return (
            store.fish01_talked
            and store.fish02_talked
            and store.gold_nugget_taken
        )


    # =================================
    # CHAPTER 1 NIGHT OBJECTIVE
    # =================================
    #
    # Lele + Gator
    #

    def night_objectives_complete():

        return (
            store.fish03_talked
            and store.fish04_talked
        )


    # =================================
    # CHAPTER 2 DAY OBJECTIVE
    # =================================
    #
    # Salmon + Arowana + Tiny Krill
    #

    def chapter2_day_objectives_complete():

        return (
            store.salmon_talked
            and store.wana_talked
            and store.tiny_krill_taken
        )


    # =================================
    # CHAPTER 2 NIGHT OBJECTIVE
    # =================================
    #
    # Ghost Fish + Mantis Shrimp victory
    #

    def chapter2_night_objectives_complete():

        return (
            store.ghost_talked
            and store.shrimp_duel_won
        )