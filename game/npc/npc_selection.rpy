# =====================================
# NPC Selection
# =====================================

default selected_npc = None

init python:

    # Daftar NPC berdasarkan cycle
    NPC_REGISTRY = {

        "fish01": {
            "display_name": "Bass",
            "cycle": "day",
        },

        "fish02": {
            "display_name": "Uceng",
            "cycle": "day",
        },

        "fish03": {
            "display_name": "Lele",
            "cycle": "night",
        },

        "fish04": {
            "display_name": "Gator",
            "cycle": "night",
        },

    }


    # Menandai NPC sudah diajak bicara
    def mark_npc_talked(npc_id):

        flag_name = f"{npc_id}_talked"

        if hasattr(store, flag_name):
            setattr(store, flag_name, True)


# =====================================
# NPC Selection
# =====================================

label npc_selection:

    $ selected_npc = renpy.call_screen("npc_select")

    if selected_npc is not None:

        call interact_with_npc(selected_npc)
        $ mark_npc_talked(selected_npc)

    return