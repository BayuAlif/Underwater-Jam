# =====================================
# NPC Interaction
# =====================================

label interact_with_npc(npc_name):

    # Bersihkan sprite yang mungkin masih tertinggal
    hide mc
    hide cory
    hide lele
    hide gator
    hide salmon
    hide wana
    hide ghost
    hide shrimp

    scene expression get_dialogue_background()

    if npc_name == "fish01":

        call dialogue_fish01

    elif npc_name == "fish02":

        call dialogue_fish02

    elif npc_name == "fish03":

        call fish03

    elif npc_name == "fish04":

        call fish04

    elif npc_name == "salmon":

        call salmon

    elif npc_name == "arowana":

        call arowana

    elif npc_name == "ghostfish":

        call ghostfish

    elif npc_name == "mantis_shrimp":

        call mantis_shrimp

    else:

        "NPC ERROR."

    scene expression get_background()

    return