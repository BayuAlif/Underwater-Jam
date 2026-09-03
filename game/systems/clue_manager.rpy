# =====================================
# Clue Manager
# =====================================

init python:

    def set_clue(text):
        if text not in store.clues:
            store.clues.append(text)

    def has_clue(text):
        return text in store.clues

    def remove_clue(text):
        if text in store.clues:
            store.clues.remove(text)

    def get_clues():
        return store.clues