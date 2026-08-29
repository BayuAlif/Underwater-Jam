# =========================================================
# FLASH STICKERS SYSTEM & TRANSFORMS
# =========================================================

init -1:
    # ---------------------------------------------------------
    # TRANSFORM POSISI & ANIMASI FLASH STIKER
    # (Ukuran stiker dibuat seragam secara global: 280x280)
    # (Muncul instan / entry 0s, tampil 0.5 detik, lalu otomatis hilang)
    # ---------------------------------------------------------
    
    # Menempatkan stiker di kepala Mr. Catfish (Lele) dengan efek Flash instan (0.5 detik lalu hilang)
    transform stiker_lele:
        xanchor 0.5
        yanchor 0.5
        xpos 1350
        ypos 320
        xsize 280
        ysize 280
        fit "contain"
        
        # Muncul instan (pop-in entry = 0) -> Tampil 0.5s -> Fade Out
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0

    # Alias alternatif untuk penamaan transform
    transform stiker_lele_pop:
        xanchor 0.5
        yanchor 0.5
        xpos 1350
        ypos 320
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0

    transform sticker_lele:
        xanchor 0.5
        yanchor 0.5
        xpos 1350
        ypos 320
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0

    transform stiker_head_lele:
        xanchor 0.5
        yanchor 0.5
        xpos 1350
        ypos 320
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0

    # Versi stiker statis di lele (jika suatu saat ingin stiker tetap diam tanpa auto-hilang)
    transform stiker_lele_stay:
        xanchor 0.5
        yanchor 0.5
        xpos 1350
        ypos 320
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0

    # Transform global untuk posisi lainnya bila diperlukan
    transform stiker_mc:
        xanchor 0.5
        yanchor 0.5
        xpos 470
        ypos 375
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0

    transform stiker_cory:
        xanchor 0.5
        yanchor 0.5
        xpos 320
        ypos 260
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0

    transform stiker_center:
        xanchor 0.5
        yanchor 0.5
        xpos 960
        ypos 360
        xsize 280
        ysize 280
        fit "contain"
        alpha 1.0
        pause 0.5
        easeout 0.25 alpha 0.0


    # ---------------------------------------------------------
    # DEKLARASI GAMBAR STIKER (UKURAN ASLI FILE 1:1)
    # ---------------------------------------------------------

    # 1. Ada Info Doksli Pakcik
    image stiker ada_info_doksli_pakcik = "images/flash_stickers/ada info doksli pakcik.png"
    image stiker doksli = "stiker ada_info_doksli_pakcik"
    image stiker ada_info_doksli = "stiker ada_info_doksli_pakcik"
    image sticker doksli = "stiker ada_info_doksli_pakcik"

    # 2. Admin Datang
    image stiker admin_datang = "images/flash_stickers/admin_datang.jpg"
    image sticker admin_datang = "stiker admin_datang"

    # 3. Aku Mau Sepuluh
    image stiker aku_mau_sepuluh = "images/flash_stickers/aku mau sepuluh.png"
    image sticker aku_mau_sepuluh = "stiker aku_mau_sepuluh"

    # 4. Alhamdulillah
    image stiker alhamdulillah = "images/flash_stickers/alhamdulillah.png"
    image sticker alhamdulillah = "stiker alhamdulillah"

    # 5. Apa Boleh Buat
    image stiker apa_boleh_buat = "images/flash_stickers/apa boleh buat.png"
    image sticker apa_boleh_buat = "stiker apa_boleh_buat"

    # 6. Awas Kamu Yah
    image stiker awas_kamu_yah = "images/flash_stickers/awas kamu yah.png"
    image stiker awas_kamu = "stiker awas_kamu_yah"
    image sticker awas_kamu_yah = "stiker awas_kamu_yah"

    # 7. Besok Aja
    image stiker besok_aja = "images/flash_stickers/besok aja.png"
    image sticker besok_aja = "stiker besok_aja"

    # 8. Cerdas
    image stiker cerdas = "images/flash_stickers/cerdas.png"
    image sticker cerdas = "stiker cerdas"

    # 9. Fih
    image stiker fih = "images/flash_stickers/Fih.jpg"
    image sticker fih = "stiker fih"

    # 10. Gokil
    image stiker gokil = "images/flash_stickers/gokil.png"
    image sticker gokil = "stiker gokil"

    # 11. Terdeteksi Suki / Hati-hati Suki
    image stiker terdeteksi_suki = "images/flash_stickers/hati hati terdeteksi suki harap waspada ygy.jpg"
    image stiker suki_waspada = "stiker terdeteksi_suki"
    image sticker terdeteksi_suki = "stiker terdeteksi_suki"

    # 12. Logikanya Dimana / Mana
    image stiker logikanya_dimana = "images/flash_stickers/logikanya mana.png"
    image stiker logikanya_mana = "stiker logikanya_dimana"
    image stiker apa_makna_dari_hal_tersebut = "stiker logikanya_dimana"
    image sticker logikanya_dimana = "stiker logikanya_dimana"

    # 13. Luar Biasa
    image stiker luar_biasa = "images/flash_stickers/luar biasa.png"
    image sticker luar_biasa = "stiker luar_biasa"

    # 14. Main Sini Ke Kalimantan
    image stiker main_sini_ke_kalimantan = "images/flash_stickers/main sini ke kalimantan.png"
    image stiker kalimantan = "stiker main_sini_ke_kalimantan"
    image sticker main_sini_ke_kalimantan = "stiker main_sini_ke_kalimantan"

    # 15. Makanya Dibaca / Makanya Kalau Ada Ingpo Dibaca
    image stiker makanya_dibaca = "images/flash_stickers/makanya kalau ada ingpo itu dibaca.png"
    image stiker makanya_kalau_ada_ingpo = "stiker makanya_dibaca"
    image sticker makanya_dibaca = "stiker makanya_dibaca"

    # 16. Malas
    image stiker malas = "images/flash_stickers/malas.jpg"
    image sticker malas = "stiker malas"

    # 17. Mencari Tahu
    image stiker mencari_tahu = "images/flash_stickers/mencari tahu.jpg"
    image sticker mencari_tahu = "stiker mencari_tahu"

    # 18. Menggoda
    image stiker menggoda = "images/flash_stickers/menggoda.jpg"
    image sticker menggoda = "stiker menggoda"

    # 19. Menggugah Selera
    image stiker menggugah_selera = "images/flash_stickers/menggugah selera.jpg"
    image sticker menggugah_selera = "stiker menggugah_selera"

    # 20. Nah Ini
    image stiker nah_ini = "images/flash_stickers/nah ini.png"
    image sticker nah_ini = "stiker nah_ini"

    # 21. Pembohonk Publik
    image stiker pembohonk_publik = "images/flash_stickers/pembohonk publik.jpg"
    image sticker pembohonk_publik = "stiker pembohonk_publik"

    # 22. Pergi Kau Suki
    image stiker pergi_kau_suki = "images/flash_stickers/pergi kau suki.png"
    image sticker pergi_kau_suki = "stiker pergi_kau_suki"

    # 23. Perlu Pencahayaan
    image stiker perlu_pencahayaan = "images/flash_stickers/perlu pencahayaan.webp"
    image sticker perlu_pencahayaan = "stiker perlu_pencahayaan"

    # 24. Super Gokil
    image stiker super_gokil = "images/flash_stickers/super gokil.png"
    image sticker super_gokil = "stiker super_gokil"

    # 25. Es Teh
    image stiker es_teh = "images/flash_stickers/tengkorak pake es teh.png"
    image stiker pake_es_teh = "stiker es_teh"
    image sticker es_teh = "stiker es_teh"

    # 26. Pake Nasi
    image stiker pake_nasi = "images/flash_stickers/tengkorak pake nasi.png"
    image sticker pake_nasi = "stiker pake_nasi"

    # 27. Pake Sambal
    image stiker pake_sambal = "images/flash_stickers/tengkorak pake sambal.png"
    image sticker pake_sambal = "stiker pake_sambal"

    # 28. Tempe Goreng
    image stiker tempe_goreng = "images/flash_stickers/tengkorakwe tempe goreng.png"
    image sticker tempe_goreng = "stiker tempe_goreng"

    # 29. Waduh
    image stiker waduh = "images/flash_stickers/waduh.jpg"
    image sticker waduh = "stiker waduh"

    # 30. Waspadalah Sosok Hitam
    image stiker waspadalah_sosok_hitam = "images/flash_stickers/waspada sosok hitam.jpg"
    image stiker waspada_sosok_hitam = "stiker waspadalah_sosok_hitam"
    image sticker waspadalah_sosok_hitam = "stiker waspadalah_sosok_hitam"

    # 31. Ya Ya Ya
    image stiker ya_ya_ya = "images/flash_stickers/ya ya ya.jpg"
    image sticker ya_ya_ya = "stiker ya_ya_ya"
