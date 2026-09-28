## Motion Sells Emotion: an ATL animation pack for Ren'Py, by EdgesSystem ######
## https://edgessystem.itch.io/motion-sells-emotion ############################
## This work is licensed under Creative Commons Attribution 4.0 International ##
## https://creativecommons.org/licenses/by/4.0/ ################################

## Keep the above banner at the top of the file if you are using the whole
## thing in your project. If you plan to copy bits and pieces of it, copy the
## banner with them.

## This pack is meant to be used as a starting point and a set of examples. It
## assumes that your sprites are full-body, that they are all in scale with
## each other, and that they all face the same direction. If your sprites do
## not meet this criteria, you will need to play with some numbers.

## At least a basic understanding of ATL animation is required. For the more
## complicated animations, you will innevitably have to do some trouble-
## shooting. Additionally, If you are using multiple animation packs from
## different people, or you already have your own infratsructure, there may be
## some incompatibilities.

## If you need assistance, post your code to MSE's troubleshooting board.

define scale = 1.05 ## Change this multiplier based on the height of your tallest
                 ## sprite at a ratio of 1 for every 1000px.
                 ## For example, for sprites that are 1080px tall, use 1.08
                 ## Default is 3 for the 3000px tall sprites included in the
                 ## Ren'Py project file.

transform toleft: ##swap which is positive or negative depending on which way
                  ##your sprites face;
    xzoom 1

transform toright:
    xzoom -1

################################################################################
## Shot Lengths
################################################################################

transform full:
    ypos 1.0
    zoom 1/scale

transform medlong:
    ypos 1.45
    zoom 1.5/scale

transform medium:
    ypos 1.9
    zoom 2.0/scale

transform medclose:
    ypos 2.7
    zoom 3/scale

transform close:
    ypos 4.4
    zoom 5.0/scale

transform closeshort:
    ypos 4.2
    zoom 5.0/scale

################################################################################
## Positions
################################################################################

transform offscreenleft: #redefined to prevent weird stuff on closer shots
    anchor (1.0,1.0)
    xpos 0.0

transform farleft:
    anchor (0.5,1.0)
    xpos 0.0

transform left: # ^
    anchor (0.5,1.0)
    xpos 0.1

transform leftish:
    anchor (0.5,1.0)
    xpos 0.25

transform centerleft:
    anchor (0.5,1.0)
    xpos 0.4

transform center: # ^
    anchor (0.5,1.0)
    xpos 0.5

transform centerright:
    anchor (0.5,1.0)
    xpos 0.6

transform rightish:
    anchor (0.5,1.0)
    xpos 0.75

transform right: # ^
    anchor (0.5,1.0)
    xpos 0.9

transform farright:
    anchor (0.5,1.0)
    xpos 1.0

transform offscreenright: # ^
    anchor (0.0,1.0)
    xpos 1.0

## Non-overlapping Duo and Trio layout presets
transform duo_left:
    anchor (0.5, 1.0)
    xpos 0.26

transform duo_right:
    anchor (0.5, 1.0)
    xpos 0.74

transform duo_left_mantis:
    anchor (0.5, 1.0)
    xpos 0.28
    ypos 1.0
    zoom (0.80 / scale)

transform duo_right_mantis:
    anchor (0.5, 1.0)
    xpos 0.72
    ypos 1.0
    zoom (0.80 / scale)

transform trio_left:
    anchor (0.5, 1.0)
    xpos 0.20

transform trio_center:
    anchor (0.5, 1.0)
    xpos 0.60

transform trio_center_mantis:
    anchor (0.5, 1.0)
    xpos 0.58
    ypos 1.0
    zoom (0.80 / scale)

transform trio_right_mantis:
    anchor (0.5, 1.0)
    xpos 0.74
    ypos 1.0
    zoom (0.78 / scale)

transform trio_right:
    anchor (0.5, 1.0)
    xpos 0.90

################################################################################
## Movement between positions
################################################################################

transform walkto(location,steps=5,walktime=2.0,bounce=1,sway=1):
    parallel:
        ease walktime location
    parallel:
        linear walktime/(steps*2) yoffset -10*bounce
        linear walktime/(steps*2) yoffset 0
        repeat steps
    parallel:
        linear walktime/(steps*4) rotate -sway
        linear walktime/(steps*2) rotate sway
        linear walktime/(steps*4) rotate 0
        repeat steps

transform leapto(location,windup=1,power=1,airtime=1):
    ease windup yoffset 10*windup
    parallel:
        easein 0.4*airtime yoffset -100*power
        easeout 0.4*airtime yoffset 0
        easein_circ 0.1*airtime yoffset 10*power
        ease 0.1*airtime yoffset 0
    parallel:
        easein airtime location

################################################################################
## Poses
################################################################################

transform bowleft(depth=1):
    transform_anchor True
    toleft
    parallel:
        ease 1.0 rotate min(depth,3)*(-15)
    parallel:
        ease 1.0 offset (depth*80,depth*(-30))

transform bowright(depth=1):
    transform_anchor True
    toright
    parallel:
        ease 1.0 rotate min(depth,3)*(15)
    parallel:
        ease 1.0 offset (depth*(-80),depth*(-30))

transform unpose: ## Return to default
    transform_anchor True
    parallel:
        ease 1.0 rotate 0
    parallel:
        ease 1.0 offset (0,0)

################################################################################
## Action Animations
################################################################################

transform jump(windup=1,power=1,airtime=1):
    ease windup yoffset 10*windup
    easein 0.4*airtime yoffset -100*power
    easeout 0.4*airtime yoffset 0
    easein_circ 0.1*airtime yoffset 10*power
    ease 0.1*airtime yoffset 0

transform jumpmc(windup=1,power=2,airtime=1):
    ease windup yoffset 10*windup
    easein 0.4*airtime yoffset -50*power
    easeout 0.4*airtime yoffset 0
    easein_circ 0.1*airtime yoffset 10*power
    ease 0.1*airtime yoffset 0

transform surprise(windup=0,power=1,airtime=1):
    ease windup yoffset 10*windup
    easein 0.4*airtime yoffset -100*power
    easeout 0.4*airtime yoffset 0
    easein_circ 0.1*airtime yoffset 10*power
    ease 0.1*airtime yoffset 0



transform fallingleaf(startpos=(0.5,0.5)):
    align (startpos)
    parallel:
        easein 2.5 ypos 1.2
    parallel:
        ease 0.4 xoffset 20
        ease 0.5 xoffset -10
        ease 0.6 xoffset 10
        ease 0.5 xoffset 0
    parallel:
        easein 0.4 rotate -20
        easein 0.5 rotate 10
        ease 0.6 rotate -30
        ease 0.5 rotate -40
    parallel:
        easein 0.4 yzoom 0.5
        easein 0.5 yzoom 0.6
        ease 0.6 yzoom 0.3
        ease 0.5 yzoom 0

################################################################################
## Looping Animations
################################################################################

transform walkloop(stepspeed=1,bounce=1,sway=1):
    parallel:
        linear 1/(stepspeed*2) yoffset -10*bounce
        linear 1/(stepspeed*2) yoffset 0
        repeat
    parallel:
        linear 1/(stepspeed*4) rotate -sway
        linear 1/(stepspeed*2) rotate sway
        linear 1/(stepspeed*4) rotate 0
        repeat

transform dancing(wait=1,steps=3,walktime=3,bounce=4,sway=5):
    walkto(rightish,steps,walktime,bounce,sway)
    wait
    toleft
    walkto(leftish,steps,walktime,bounce,-sway)
    wait
    toright
    repeat

transform pacing(wait=1,steps=5,walktime=2,bounce=1,sway=1):
    walkto(rightish,steps,walktime,bounce,sway)
    wait
    toleft
    walkto(leftish,steps,walktime,bounce,-sway)
    wait
    toright
    repeat


transform vibrate(intensity = 2):
    linear 1/(2*intensity) xoffset intensity
    linear 1/(2*intensity) xoffset -intensity
    repeat

default zoomies_rate = 0.2

transform zoomies:
    animation
    transform_anchor True
    toright
    parallel:
        easeout zoomies_rate farright
    parallel:
        easein zoomies_rate rotate 10
    block:
        parallel:
            easeout zoomies_rate pos (0.8,0.5)
            linear zoomies_rate pos (0.4,0.9)
            easeout zoomies_rate pos (0.0,1.0)
            easeout zoomies_rate pos (0.2,0.5)
            linear zoomies_rate pos (0.6,0.9)
            easeout zoomies_rate pos (1.0,1.0)
        parallel:
            easein zoomies_rate rotate -20
            linear zoomies_rate rotate -50
            easeout zoomies_rate rotate 20
            easein zoomies_rate rotate 20
            linear zoomies_rate rotate 50
            easeout zoomies_rate rotate -20
        parallel:
            toleft
            easeout zoomies_rate zoom 0.7/scale
            linear zoomies_rate zoom 1/scale
            easeout zoomies_rate zoom 1.2/scale
            toright
            easeout zoomies_rate zoom 1.4/scale
            linear zoomies_rate zoom 1.2/scale
            easeout zoomies_rate zoom 1/scale
        repeat

transform loopfromleft(looptime = 5.0, delaytime = 1.0, initialdelay = 0):
    offscreenleft
    initialdelay
    block:
        linear looptime offscreenright
        delaytime
        offscreenleft
        repeat
transform loopfromright(looptime = 5.0, delaytime = 1.0, initialdelay = 0):
    offscreenright
    initialdelay
    block:
        linear looptime offscreenleft
        delaytime
        offscreenright
        repeat

transform flicker(rate=1,min=0.45,max=0.5):
    alpha max
    choice:
        rate+0.2*rate
    choice:
        rate
    choice:
        rate-0.2*rate
    linear 0.1*rate alpha min
    linear 0.1*rate alpha max
    repeat

################################################################################
## Multi-part Animations
################################################################################


## Ballroom Dancing ####################

## This animation requires both dancers to have a back sprite, and for one of
## the dancers to be on screen twice at the same time. PLEASE reference
## script.rpy to see how to properly set this up.

default tempo = 1.5 ## adjust this to match the beat of your music.
## recommended no faster than the 1.5 default

transform waltz_lead:
    animation
    parallel:
        toright
        ease tempo xpos 0.35
        easeout tempo/2 xpos 0.5
        toleft
        easein tempo/2 xpos 0.65
        ease tempo xpos 0.5
    parallel:
        ease tempo zoom 1.5/scale
        easeout tempo/2 zoom 1.6/scale
        easein tempo/2 zoom 1.5/scale
        ease tempo zoom 1.4/scale
    parallel:
        ease tempo ypos 1.45
        easeout tempo/2 ypos 1.5
        easein tempo/2 ypos 1.45
        ease tempo ypos 1.4
    repeat

transform waltz_follow:
    animation
    parallel:
        toleft
        ease tempo xpos 0.65
        easeout tempo/2 xpos 0.5
        toright
        easein tempo/2 xpos 0.35
        ease tempo xpos 0.5
    parallel:
        ease tempo zoom 1.5/scale
        easeout tempo/2 zoom 1.4/scale
        easein tempo/2 zoom 1.5/scale
        ease tempo zoom 1.6/scale
    parallel:
        ease tempo ypos 1.45
        easeout tempo/2 ypos 1.4
        easein tempo/2 ypos 1.45
        ease tempo ypos 1.5
    repeat

## See-Saw #############################

default seesaw_rate = 3.0
default seesaw_height = 0

transform seesaw_left:
    animation
    transform_anchor True
    subpixel True
    medclose
    left
    toright
    ypos 2.7-seesaw_height
    parallel:
        ease seesaw_rate/2 yoffset 50
    parallel:
        ease seesaw_rate/2 rotate -2
    block:
        parallel:
            pause seesaw_rate/10
            ease seesaw_rate yoffset -50
            pause seesaw_rate/10
            ease seesaw_rate yoffset 50
            repeat
        parallel:
            pause seesaw_rate/10
            ease seesaw_rate rotate 2
            pause seesaw_rate/10
            ease seesaw_rate rotate -2
            repeat

transform seesaw_right:
    animation
    transform_anchor True
    subpixel True
    medclose
    right
    toleft
    ypos 2.7-seesaw_height
    parallel:
        ease seesaw_rate/2 yoffset -50
    parallel:
        ease seesaw_rate/2 rotate -2
    block:
        parallel:
            pause seesaw_rate/10
            ease seesaw_rate yoffset 50
            pause seesaw_rate/10
            ease seesaw_rate yoffset -50
            repeat
        parallel:
            pause seesaw_rate/10
            ease seesaw_rate rotate 2
            pause seesaw_rate/10
            ease seesaw_rate rotate -2
            repeat

## Pickup ##############################

transform sink(depth=1):
    ease 0.3 yoffset 100*depth

transform pickup(depth=1):
    ease 0.5 yoffset 100*depth
    ease 0.5 yoffset 0
transform itempickup(location=(0.5,0.5)):
    anchor (0.5,0.5)
    pos (location[0],1.0)
    rotate 20
    alpha 0.0
    0.5
    parallel:
        easeout 0.2 alpha 1.0
    parallel:
        easeout 0.5 pos location
    parallel:
        easeout 0.5 rotate 0

transform shake:
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

transform float_idle(bob=6, sway=3, speed=2.5):
    subpixel True
    parallel:
        ease speed yoffset -bob
        ease speed yoffset bob
        repeat
    parallel:
        ease speed*1.3 xoffset sway
        ease speed*1.3 xoffset -sway
        repeat
    parallel:
        ease speed*1.1 rotate 1
        ease speed*1.1 rotate -1
        repeat