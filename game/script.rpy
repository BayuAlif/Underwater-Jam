# The script of the game goes in this file.

# Declare characters used by this game.
define k = Character("Jose", color="#4a90e2")
define kn = Character("Kankan", color="#f5a623")
define system = Character("System", color="#888888")
define npc_night = Character("Angler Fish", color="#ff4444")
define cory = Character("Cory", color="#00a86b")

default trigger_combat = False
default interrogator = ""

# The game starts here.

label start:
    show screen day_night_hud

   
    # SCENE 1-5 (DAY CYCLE)

    $ load_area("beach")
    scene expression get_background() with fade
    
    system "--- SCENE 1-5: DAY CYCLE ---"
    k "Semua objective siang beres! Waktunya masuk ke malam hari..."



    # SCENE 6: NIGHT CYCLE (EKSPLORASI ITEM)

    # Ganti cycle ke night via Cycle Manager
    $ change_cycle()
    scene expression get_background() with fade

    system "--- SCENE 6: EKSPLORASI MALAM ---"
    k "Suasana area [get_current_area()] berubah jadi gelap!"
    kn "Jose, cari dan bersihkan semua item yang ada di area ini biar kita bisa lanjut!"

    # Panggil screen dari file game/screens/scene6_screens.rpy
    call screen scene6_night


   
    # SCENE 7: INTERACT WITH NIGHT NPC (INTRO)

    system "Semua item berhasil ditemukan!"
    
    kn "Bagus Jose, semua item di area ini udah terkumpul!"
    k "Sip, sekarang ayo kita dekati makhluk yang ada di depan sana..."

    system "--- SCENE 7: INTERACTION WITH NIGHT NPC ---"

    # Introduction / Obrolan pendek sesuai deskripsi Scene 7
    npc_night "Suh dude... Berani banget kalian berkeliaran di area ini saat malam hari."
    k "Uwooh! Kankan, lihat! Bentuknya beda banget sama ikan-ikan yang kita temui tadi siang!"
    kn "Tetap waspada Jose. Dia kelihatan misterius... Ayo coba kita korek informasi dari dia."
    npc_night "Heh... Kalian mau tanya-tanya soal laut dalam ini? Boleh saja, tapi tergantung siapa yang bicara kepadaku."


   
    # SCENE 8: ROTASI IKAN (PILIH KARTU KARAKTER)

    system "--- SCENE 8: ROTASI IKAN ---"

    $ trigger_combat = False

    # Panggil UI Kartu dari file game/screens/scene8_screens.rpy
    call screen rotasi_ikan_select

    # Percabangan Dialog Berdasarkan Karakter Penanya yang Dipilih
    if _return == "select_jose":
        $ interrogator = "jose"
        k "Biar aku saja yang maju! Woi Ikan Misterius!"
        npc_night "Cih... Manusia berisik dan tidak ada sopan-santunnya! Mau apa kau?!"
        
        # Multiple Options Versi Jose
        menu:
            "Tanya lokasi Ikan Emas (Sopan)":
                k "Permisi, apa kamu tahu di mana lokasi Ikan Emas berada?"
                npc_night "Mana aku tahu! Lagipula tidak akan kuberi tahu manusia!"
                $ trigger_combat = False

            "Tantang NPC Malam (Provokasi)":
                k "Woi muka serem! Jangan belagu deh, cepet kasih tahu petunjuknya!"
                npc_night "GRRRR!! Beraninya manusia kerdil menyerang kehormatanku! Rasakan ini!"
                # Memicu Panic/Combat Typing di Scene 9!
                $ trigger_combat = True

    elif _return == "select_cory":
        $ interrogator = "cory"
        cory "Olá meu amigo! Suasana malam ini lumayan tenang ya, boleh kami bertanya?"
        npc_night "Hmm... Kelihatan lebih ramah dibanding manusiamu. Mau tanya apa, kawan?"
        
        # Multiple Options Versi Cory (Aman / Tanpa Combat)
        menu:
            "Tanya petunjuk rahasia":
                cory "Bisa berikan kami petunjuk jalan ke Palung Selatan?"
                npc_night "Karena kau sopan, dengarkan ini... Hati-hati dengan arus di sebelah kiri."
            "Tanya soal ikan lain":
                cory "Apa ada ikan lain yang berkeliaran jam segini?"
                npc_night "Hanya beberapa predator, tapi kalau lewat tengah aman."
        
        $ trigger_combat = False

    elif _return == "select_char3":
        $ interrogator = "kankan"
        kn "Permisi... aku ingin bertanya sedikit."
        npc_night "Oh, kau rupanya. Ada apa?"
        $ trigger_combat = False

   
    # SCENE 9: COMBAT TYPING 
    system "Interogasi Scene 8 Selesai!"
    # Pengecekan apakah interogasi berakhir damai atau memicu perkelahian
    if trigger_combat:
        system "--- SCENE 9: COMBAT TYPING (PANIC MODE) ---"
        
        k "Waduh! Dia ngamuk, Kankan! Siap-siap!"
        kn "Tuh kan Jose! Dibilang jangan provokasi NPC Malam!"

        # Panggil Minigame Combat Typing (Batas waktu 6.0 detik)
        call screen combat_typing_minigame(time_limit=6.0)

        # Cek Hasil Minigame dari Return Screen
        if _return == "success":
            system "BERHASIL! Kamu mengetik kata dengan cepat dan menangkis serangan!"
            k "Hosh... Hosh... Untung refleksku cepat!"
            npc_night "Cih... Boleh juga refleksmu, Manusia. Pergi sana!"
            
        elif _return == "failed":
            system "GAGAL! Waktu habis atau kata yang diketik salah!"
            kn "Aduuh! Kita terkena sabetan buntut NPC Malam!"
            k "Ampunnn! Ayo kaburrr!"

    else:
        system "--- SCENE 9: SKIPPED (Interaksi berjalan damai tanpa combat) ---"


    # SCENE 10: AREA CLEAR & TRANSISI KE AREA BARU

    system "--- SCENE 10: AREA CLEAR ---"
    
    kn "Yayyy! Semua urusan dan interogasi di area ini akhirnya selesai!"
    k "Baguslah! Sekarang ayo kita lanjut pindah ke area laut berikutnya!"

    # Memanggil fungsi transisi area & cycle buatan temenmu
    $ load_area("beach")   # Ganti nama area selanjutnya
    $ change_cycle()            # Kembali berubah jadi Day Cycle
    
    scene expression get_background() with fade
    
    system "Kamu telah berpindah ke Area Baru: [get_current_area()]!"
    k "Wah, pemandangannya beda lagi nih pas siang hari..."

    return

    return