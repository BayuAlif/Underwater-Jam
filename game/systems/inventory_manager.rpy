# =====================================
# INVENTORY MANAGER
# =====================================

default inventory = []

# Flag terpisah dari inventory, supaya Shell tetap
# tercatat "sudah pernah diambil" walau nanti
# dihapus lagi dari inventory (misal setelah
# diberikan ke NPC).
default shell_taken = False

init python:

    def add_item(item):
        if item not in inventory:
            inventory.append(item)

    def has_item(item):
        return item in inventory

    def remove_item(item):
        if item in inventory:
            inventory.remove(item)