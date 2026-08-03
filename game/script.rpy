# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gulugulu")
define f2 = Character("Fihfriend2")
define f3 = Character("Fihfriend3")

image jumping:
    "testmchappy"
    yalign 1.0
    easeout 0.4 yoffset -50
    easein 0.4 yoffset 0
    repeat

screen riverside_click():
    add "rivershoredaybg"
    modal True

    imagebutton auto "fihfriend2_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "fihfriend2")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("fihfriendsporty")

    imagebutton auto "fihfriend3_%s":
        hovered SetVariable("screen_tooltip", "fihfriend3")
        unhovered SetVariable("screen_tooltip", "")
        focus_mask True
        action Jump("fihfriendgoth")


label start:

    scene rivershorebg

    "The rivershore.. super calm woauh.. so calm you can feel yourself becoming one with everything else around you"
    "A little child then shows up"

    show testmcdefault


    g "like always! its just me and the fishies today :D"

    hide testmcdefault
    show jumping

    g "hehe i wonder what kind of fish i can find today.. i hope i can find something new"


label riverside_click:
    scene rivershoredaybg
    call screen riverside_click
    return

label fihfriendsporty:
    show fihfriend2_idle
    f2 "hi there!"
    jump riverside_click

label fihfriendgoth:
    show fihfriend3_idle
    f3 "greetings..."
    jump riverside_click


    return
