# =====================================
# NPC Interaction
# =====================================

# Menghubungkan NPC yang dipilih ke dialog yang sesuai.

label interact_with_npc(npc_name):

    "Kamu mendekati NPC."

    if renpy.has_label(npc_name):
        call expression npc_name

    else:
        "NPC belum tersedia."

    "Kamu menjauh dari NPC."

    return