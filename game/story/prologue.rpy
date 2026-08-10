# =====================================
# PROLOGUE
# =====================================

label prologue:

    $ set_cycle("day")
    $ load_area("beach")

    scene expression get_background()

    e "===== PROLOGUE ====="

    e "Di suatu pagi..."

    e "Aku terbangun di tepi laut."

    e "Hari ini petualangan dimulai."

    call chapter1

    return