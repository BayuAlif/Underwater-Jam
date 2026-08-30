# =====================================
# Combat Typing
# Dipakai oleh Chapter 1 Night Cycle.
# =====================================


# =====================================
# PYTHON
# =====================================

init python:

    import random

    TYPING_WORDS = [
        "SERANGAN LAUT",
        "KABUR SEKARANG",
        "TANGKIS SERANGAN",
        "PALUNG DALAM",
        "GULITA MALAM",
        "DOSA IKAN"
    ]


    def start_typing_game():

        store.target_word = random.choice(TYPING_WORDS)
        store.player_input = ""


# =====================================
# DEFAULT VARIABLES
# =====================================

default target_word = ""
default player_input = ""


# =====================================
# TIMER BAR ANIMATION
# =====================================

transform timer_bar_anim(time_limit):

    xsize 600
    linear time_limit xsize 0


# =====================================
# COMBAT TYPING SCREEN
# =====================================

screen combat_typing_minigame(time_limit=5.0):

    modal True

    # Saat screen dibuka,
    # pilih kata baru dan reset input.
    on "show" action Function(start_typing_game)


    # Background gelap
    add Solid("#000000bb")


    # =================================
    # TIMER
    # =================================

    timer time_limit action Return("failed")


    # =================================
    # TIMER BAR BACKGROUND
    # =================================

    frame:

        xalign 0.5
        yalign 0.2

        xsize 604
        ysize 24

        background Solid("#333333")


        # Timer merah
        add Solid("#ff4444"):

            xsize 600
            ysize 16

            xalign 0.0
            yalign 0.5

            at timer_bar_anim(time_limit)


    # =================================
    # TEXT & INPUT
    # =================================

    vbox:

        xalign 0.5
        yalign 0.45

        spacing 20


        text "COMBAT TYPING! KETIK KATA DI BAWAH INI!":

            color "#ff4444"
            size 22
            bold True

            xalign 0.5


        text "[target_word]":

            color "#f9d71c"
            size 36
            bold True

            xalign 0.5


        input:

            value VariableInputValue("player_input")

            length len(target_word) + 5

            xalign 0.5

            style "typing_input_style"


        textbutton "SERANG! (ENTER)":

            xalign 0.5

            action If(
                player_input.strip().upper() == target_word.upper(),

                true=Return("success"),

                false=Notify("Kata belum sesuai!")
            )


    # =================================
    # TEKAN ENTER
    # =================================

    key "K_RETURN" action If(
        player_input.strip().upper() == target_word.upper(),

        true=Return("success"),

        false=Notify("Kata belum sesuai!")
    )


# =====================================
# INPUT STYLE
# =====================================

style typing_input_style:

    color "#ffffff"

    size 28

    outlines [
        (2, "#000000", 0, 0)
    ]