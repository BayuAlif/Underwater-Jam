# =====================================
# Progress Manager
# =====================================

default current_day = 1
default depth_meters = 100


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


init python:

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
    # DAY OBJECTIVE
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
    # NIGHT OBJECTIVE
    # =================================
    #
    # Lele + Gator
    #

    def night_objectives_complete():

        return (
            store.fish03_talked
            and store.fish04_talked
        )