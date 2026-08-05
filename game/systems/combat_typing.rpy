# Combat typing
init python:
    import random

    #Daftar kata yang harus diketik
    TYPING_WORDS = [
        "SERANGAN LAUT",
        "KABUR SEKARANG",
        "TANGKIS SERANGAN",
        "PALUNG DALAM",
        "GULITA MALAM",
        "DOSA IKAN"
    ]

    def start_typing_game():
        # Pilih kata secara acak dari daftar
        store.target_word = random.choice(TYPING_WORDS)
        store.player_input = ""

#Variabel global untuk minigames typing
default target_word = ""
default player_input = ""

transform timer_bar_anim(time_limit):
    xsize 600
    # Berubah ukuran xsize dari 600px ke 0px dalam durasi time_limit detik
    linear time_limit xsize 0

screen combat_typing_minigame(time_limit=5.0):
    modal True

    on "show" action Function(start_typing_game)

    # Background Gelap/Panic Overlay
    add "#000000bb"

    # TIMER (Batas Waktu)
    # Jika waktu habis (timer mencapai 0), Return "failed"
    timer time_limit action Return("failed")

    # Ui timer bar
    frame:
        xalign 0.5
        yalign 0.2
        xsize 604
        ysize 24
        background Solid("#333333") 
        
        add Solid("#ff4444", ysize=16, xalign=0.0, yalign=0.5):
            at timer_bar_anim(time_limit)

    vbox:
        xalign 0.5
        yalign 0.45
        spacing 20

        text "⚠️ COMBAT TYPING! KETIK KATA DI BAWAH INI! ⚠️" color "#ff4444" size 22 bold True xalign 0.5
        
        # Display Kata Target
        text "[target_word]" color "#f9d71c" size 36 bold True xalign 0.5

        # Input Box Tempat Player Ngetik
        input:
            default ""
            value VariableInputValue("player_input")
            length len(target_word) + 5
            xalign 0.5
            style "typing_input_style"
            changed Function(renpy.restart_interaction)

        # Tombol Submit via Enter / Klik Manual
        textbutton "SERANG! (ENTER)":
            xalign 0.5
            action If(
                player_input.strip().upper() == target_word.upper(),
                true=Return("success"),
                false=Notify("Kata belum sesuai!")
            )

style typing_input_style:
    color "#ffffff"
    size 28
    outlines [ (2, "#000000", 0, 0) ]