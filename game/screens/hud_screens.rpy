# =========================================================
# GAME HUD / STATUS DISPLAY
# =========================================================

screen day_night_hud():
    zorder 100

    # Frame Indikator di Pojok Kanan Atas
    frame:
        xalign 0.98
        yalign 0.02
        background Solid("#000000aa") # Box Hitam Transparan
        padding (15, 10)

        vbox:
            spacing 4
            
            text "📅 HARI: [get_current_day()]" size 14 color "#ffffff" bold True
            text "🌊 KEDALAMAN: [get_depth()] m" size 14 color "#4a90e2" bold True
            
            if is_day():
                text "☀️ SIKLUS: SIANG" size 14 color "#f9d71c" bold True
            else:
                text "🌙 SIKLUS: MALAM" size 14 color "#a569bd" bold True