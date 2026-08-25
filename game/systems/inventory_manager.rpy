# =====================================
# Inventory Manager
# Mengatur inventori item pemain
# =====================================

default player_inventory = []

init python:

    def add_item(item_name):
        if not hasattr(store, "player_inventory"):
            store.player_inventory = []
        if item_name not in store.player_inventory:
            store.player_inventory.append(item_name)

    def has_item(item_name):
        return item_name in getattr(store, "player_inventory", [])

    def remove_item(item_name):
        if hasattr(store, "player_inventory") and item_name in store.player_inventory:
            store.player_inventory.remove(item_name)
            return True
        return False
