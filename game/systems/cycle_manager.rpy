init python:

    def add_clue(clue):
        if clue not in store.clues:
            store.clues.append(clue)

    def has_clue(clue):
        return clue in store.clues