# =====================================
# NPC Interaction
# =====================================

label interact_with_npc(npc_name):

    # Ganti ke background bordered (siang/malam) saat berdialog dengan karakter
    scene expression get_dialogue_background()

    if renpy.has_label(npc_name):

        call expression npc_name

    else:

        "NPC ERROR."

    # Bersihkan sprite dan kembalikan ke background full (non-bordered) saat kembali ke hub
    scene expression get_background()

    return