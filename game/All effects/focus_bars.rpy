###############################################################################################################
### FOCUS BARS ################################################################################################
###############################################################################################################
#
# Thanks for downloading my Ren'Py Focus Bars plugin! ( https://kigyo.itch.io/renpy-focus-bars )
#
# Although it's technically plug-and-play, I'll walk you through how you can customize this feature to your liking!
# If you run into any difficulties, I'm always happy to help in the Itch.io comments!
#
# If you like this tool, consider dropping a donation: https://ko-fi.com/kigyodev
# Credit to "KigyoDev" would also be appreciated!
#
# Thank you, and may this tool enhance the visual presentation of your games! :D
# - KigyoDev
#
###############################################################################################################


###############################################################################################################
## 1. Variables ###############################################################################################
###############################################################################################################
## 
## These variables set how you want the focus bars to behave most of the time.
## You can always adjust how most of these behave on an individual basis whenever you call "focus()"

# The size / height of the focus bars.
# default value: 350
define FOCUS_YSIZE = 350

# Standard opacity of the focus bars. For example, set this to 1.0 if you want them to not at all be see-through.
# default value: 0.8
define FOCUS_ALPHA = 0.8

# Standard blend mode of the focus bars. Default supported values are "normal", "add", "multiply", "min", and "max"
# Set this to "normal" if you just want regular black bars
# default value: "multiply"
define FOCUS_BLEND = "multiply" 

# Standard z-axis position of the focus bars. Set this to "True" if they should be *behind* your characters
# default value: False
define FOCUS_BACK = True 

# How long the bars should take to show up. Set this to "0.0" if you always want the bars to show up instantly
# default value: 1.0
define FOCUS_ANIMATION_TIME = 1.0 

define FOCUS_CHARAS = ["mc", "cory", "pcory", "bass", "uceng", "lele", "gator", "salmon", "arowana", "ghost", "shrimp", "scy", "dunge", "crab", "hawk", "turtle", "teto", "goby", "bunny", "seabunny", "leo", "orin", "rin", "fakecory", "fakeleo", "fakescy", "mama", "papa", "empress"]


###############################################################################################################
## 2. Focus Bar ###############################################################################################
###############################################################################################################
## 
## This is a solid black image by default, but you can also change this to any other color or an entirely new image.

image focus_bar_base = Solid("#000000", xysize=(config.screen_width,config.screen_height), xcenter=0.5, ycenter=0.5)

###############################################################################################################
## 3. How to Use ##############################################################################################
###############################################################################################################
##
## Now, all you have to do is call...
##  $ focus()
## ...in your game script whenever you want to show OR hide the focus bars.
## (The code remembers whether they've already been shown, so the function works like a toggle.)
##
## EXAMPLE:

label focus_test:
    show eileen
    "Eileen is just standing there."
    $ focus()
    "Now, bars appear."
    $ focus()
    "And they're gone again."

    $ focus(ysize=100, time=0.5)
    "Now, the bars got slimmer. You probably also want to shorten the time then."
    $ focus()
    "And they're hidden."

    $ focus(alpha=0.3, back=not FOCUS_BACK)
    "This time, the bars should be very transparent, and either in front of or behind the sprite, depending on your default setting."
    $ focus(False)
    "When the first parameter (smooth) is set to \"False\", the bars appear or disappear instantly."

    $ focus(False)
    with dissolve
    "Let's try this again. You can also combine the show/hide with transitions if you like!"
    $ focus_off(False)
    with dissolve
    "And if you ever need to, you can also hide the bars manually by using the \"focus_off()\" function."

    "Now go out there and focus!"


###############################################################################################################
## Bonus: The Code ############################################################################################
###############################################################################################################

# These variables just track whatever is *currently* set / active.
# Changing the defaults won't do anything, but they're useful if you need to reference this information elsewhere.
default focus_bars = False
default focus_alpha = 1.0
default focus_animation = 1.0
default focus_layer = "focus_bars"
default focus_blend = "normal"
default focus_ysize = FOCUS_YSIZE

init python:
    renpy.add_layer("focus_bars", above="master", menu_clear=False)

    def focus(smooth=True, alpha=FOCUS_ALPHA, back=FOCUS_BACK, blend=FOCUS_BLEND, ysize=FOCUS_YSIZE, time=FOCUS_ANIMATION_TIME):
        if focus_bars:
            focus_off(smooth)
        else:
            if ysize:
                store.focus_ysize = ysize
            store.focus_bars = True
            store.focus_alpha = alpha
            store.focus_animation = time
            if back:
                store.focus_layer = "master"
            else:
                store.focus_layer = "focus_bars"
            store.focus_blend = blend
            renpy.hide("focus_hide", "master")
            renpy.hide("focus_hide", "focus_bars")
            if smooth:
                renpy.show("focus_smooth", at_list=[Transform(alpha=alpha, blend=blend)], layer=focus_layer, behind=FOCUS_CHARAS)
            else:
                renpy.show("focus_instant", at_list=[Transform(alpha=alpha, blend=blend)], layer=focus_layer, behind=FOCUS_CHARAS)

    def focus_off(smooth=True):
        renpy.hide("focus_smooth", "master")
        renpy.hide("focus_smooth", "focus_bars")
        renpy.hide("focus_instant", "master")
        renpy.hide("focus_instant", "focus_bars")
        if smooth:
            renpy.show("focus_hide", at_list=[Transform(alpha=focus_alpha, blend=focus_blend)], layer=focus_layer, behind=FOCUS_CHARAS)
        store.focus_bars = False
        
    # These make sure this file is archived in a game release. Please don't remove.
    build.classify("**focus_bars.rpy", None)
    build.classify("**focus_bars.rpyc", "archive")

###############################################################################################################
## Bonus: Image Definitions ###################################################################################
###############################################################################################################

image focus_smooth:
    contains:
        Crop((0, 0, 1.0, focus_ysize+50), "focus_bar_base")
        yoffset -focus_ysize-50 ypos 0.0 xalign 0.5
        easein focus_animation yoffset 0 # Note: Edit this line if you want to change how the slide-in effect looks
    contains:
        Crop((0, 0, 1.0, focus_ysize+50), "focus_bar_base")
        yoffset focus_ysize+50 ypos 1.0 xalign 0.5
        easein focus_animation yoffset 0 # Note: Edit this line if you want to change how the slide-in effect looks
        
image focus_instant:
    contains:
        Crop((0, 0, 1.0, focus_ysize+50), "focus_bar_base")
        ypos 0.0 xalign 0.5
    contains:
        Crop((0, 0, 1.0, focus_ysize+50), "focus_bar_base")
        ypos 1.0 xalign 0.5
        
image focus_hide:
    contains:
        Crop((0, 0, 1.0, focus_ysize+50), "focus_bar_base")
        yoffset 0 ypos 0.0 xalign 0.5
        ease 3*(focus_animation/4) yoffset -focus_ysize-50 # Note: Edit this line if you want to change how the slide-out effect looks
    contains:
        Crop((0, 0, 1.0, focus_ysize+50), "focus_bar_base")
        yoffset 0 ypos 1.0 xalign 0.5
        ease 3*(focus_animation/4) yoffset focus_ysize+50 # Note: Edit this line if you want to change how the slide-out effect looks

###############################################################################################################
## License ####################################################################################################
###############################################################################################################

# Copyright 2026 KigyoDev

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions 
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

###############################################################################################################
