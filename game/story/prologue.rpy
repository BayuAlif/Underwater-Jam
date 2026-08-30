# =====================================
# PROLOGUE
# =====================================

label prologue:

    $ set_cycle("day")
    $ load_area("beach")

    scene expression get_background()

    f1 "===== PROLOGUE ====="

    f1 "Di suatu pagi..."

    f1 "Aku terbangun di tepi laut."

    f1 "Hari ini petualangan dimulai."

    call chapter1

    return