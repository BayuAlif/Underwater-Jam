# =====================================
# PROLOGUE
# =====================================

label prologue:

    $ set_cycle("day")
    $ load_area("beach")

    scene expression get_background()

    mc "===== PROLOGUE ====="

    mc "Di suatu pagi..."

    mc "Aku terbangun di tepi laut."

    mc "Hari ini petualangan dimulai."

    call chapter1

    return