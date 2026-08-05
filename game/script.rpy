# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Jose", color="#4a90e2")
define kn = Character("Kankan", color="#f5a623")
define system = Character("System", color="#888888")

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


# The game starts here.

label start:
    show screen day_night_hud

    # ---------------------------------------------------------
    # SCENE 1-5 (DAY CYCLE)

    $ load_area("beach")
    scene expression get_background() with fade
    
    system "--- SCENE 1-5: DAY CYCLE ---"
    k "Semua objective siang beres! Waktunya masuk ke malam hari..."


    # ---------------------------------------------------------
    # SCENE 6: NIGHT CYCLE (AUTOMATIC ITEM CHECK)

    # Ganti cycle ke night 
    $ change_cycle()
    scene expression get_background() with fade

    system "--- SCENE 6: EKSPLORASI MALAM ---"
    k "Suasana area [get_current_area()] berubah jadi gelap!"
    kn "Jose, cari dan bersihkan semua item yang ada di area ini biar kita bisa lanjut!"

    # Panggil screen eksplorasi

    call screen scene6_night

    # ---------------------------------------------------------
    # SCENE 7: OTOMATIS BERLANJUT KE SINI

    system "Semua item berhasil ditemukan!"
    
    kn "Bagus Jose, semua item di area ini udah terkumpul!"
    k "Sip, sekarang ayo kita lanjut ke interogasi NPC Malam!"


    system "Semua item berhasil ditemukan!"
    
    kn "Bagus Jose, semua item di area ini udah terkumpul!"
    k "Sip, sekarang ayo kita dekati makhluk yang ada di depan sana..."

    # Deklarasi NPC Malam 
    define npc_night = Character("Angler Fish", color="#ff4444")

    # Tampilkan sprite NPC Malam (Sementara pakai placeholder text/show)
    # show angler_fish_night at center with dissolve

    system "--- SCENE 7: INTERACTION WITH NIGHT NPC ---"

    # Introduction / Obrolan pendek sesuai deskripsi Scene 7
    npc_night "Suh dude... Berani banget kalian berkeliaran di area ini saat malam hari."

    k "Uwooh! Kankan, lihat! Bentuknya beda banget sama ikan-ikan yang kita temui tadi siang!"

    kn "Tetap waspada Jose. Dia kelihatan misterius... Ayo coba kita korek informasi dari dia."

    npc_night "Heh... Kalian mau tanya-tanya soal laut dalam ini? Boleh saja, tapi tergantung siapa yang bicara kepadaku."

    # ---------------------------------------------------------
    # SCENE 8: ROTASI IKAN / INTEROGASI (LANJUTAN)
    # ---------------------------------------------------------
    # (Siap masuk ke sesi milih respon Jose / Kankan di Scene 8)
    return