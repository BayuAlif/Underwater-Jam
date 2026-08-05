# System scene 6 - Night Cycle Map Screen

# Variabel pelacak item scene 6
default day_item_takens = False
default night_item_takens = False

screen scene6_night():
    add get_background()

    # String penanda
    text "Area: [current_area] | Cycle: [current_cycle]" xalign 0.02 yalign 0.08 color "#ffffff" size 16 
    text "Petunjuk: Cari dan ambil semua item di area ini!" xalign 0.02 yalign 0.12 color "#f9d71c" size 14

    # Sisa item dari waktu siang sblmnya yang tidak terambil
    if not day_item_takens:
        imagebutton:
            idle Solid("#f5a623", xsize=35, ysize=35)
            xpos 300 ypos 450
            action [
                SetVariable("day_item_takens", True), 
                Notify("Diambil: Item Day yang ketinggalan!"), # Koma ditambahkan
                If(night_item_takens, Return("all_items_collected"))
            ]

    # Item malam yang baru (dan hanya muncul ketika malam)
    if is_night() and not night_item_takens:
        imagebutton:
            idle Solid("#a569bd", xsize=35, ysize=35)
            xpos 700 ypos 480
            action [
                SetVariable("night_item_takens", True), 
                Notify("Diambil: Item Night!"), # Koma ditambahkan
                If(day_item_takens, Return("all_items_collected"))
            ]