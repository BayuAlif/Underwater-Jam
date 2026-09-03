# =====================================
# INVENTORY MANAGER
# =====================================

default inventory = []

# =====================================
# Chapter 1 Items
# =====================================

default gold_nugget_taken = False
default ambalabu_taken = False

# =====================================
# Chapter 2 Items
# =====================================

default tiny_krill_taken = False
default coal_tar_taken = False
default saltwater_device_taken = False


init python:

    def add_item(item):

        if item not in store.inventory:

            store.inventory.append(item)


    def has_item(item):

        return item in store.inventory


    def remove_item(item):

        if item in store.inventory:

            store.inventory.remove(item)