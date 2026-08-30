# =====================================
# INVENTORY MANAGER
# =====================================

default inventory = []

# =====================================
# Chapter 1 - Bongkahan Emas
# =====================================

default gold_nugget_taken = False


init python:

    def add_item(item):

        if item not in store.inventory:

            store.inventory.append(item)


    def has_item(item):

        return item in store.inventory


    def remove_item(item):

        if item in store.inventory:

            store.inventory.remove(item)