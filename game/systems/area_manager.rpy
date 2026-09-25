default exploration_npcs = []
default exploration_item = None
default explored_npcs = []
default item_collected = False

init python:

    def setup_exploration(npcs, item):
        store.exploration_npcs = npcs
        store.exploration_item = item
        store.explored_npcs = []
        store.item_collected = False

    def mark_npc_explored(npc_id):
        if npc_id not in store.explored_npcs:
            store.explored_npcs.append(npc_id)

    def collect_exploration_item():
        if store.exploration_item and not store.item_collected:
            add_item(store.exploration_item["id"])
            store.item_collected = True

    def exploration_complete():
        return (
            store.item_collected
            and len(store.explored_npcs) >= len(store.exploration_npcs)
        )
