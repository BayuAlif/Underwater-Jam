default inventory_items = []

init python:

    def add_item(item):
        if item not in store.inventory_items:
            store.inventory_items.append(item)

    def remove_item(item):
        if item in store.inventory_items:
            store.inventory_items.remove(item)

    def has_item(item):
        return item in store.inventory_items
