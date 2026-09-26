init python:
    def ch5_get_zone_x(zone):
        if zone == "left":
            return 0
        elif zone == "right":
            return -3840
        return -1920

transform ch5_pano_shift(target_x):
    subpixel True
    on show:
        xpos target_x
    on replace:
        easein_cubic 0.55 xpos target_x

transform ch5_mirage_float:
    subpixel True
    easein 2.5 yoffset -12
    easeout 2.5 yoffset 12
    repeat

transform ch5_mirage_hub_scy:
    subpixel True
    zoom 0.88
    anchor (0.5, 0.5)
    easein 2.5 yoffset -12
    easeout 2.5 yoffset 12
    repeat

transform ch5_mirage_hub_cory:
    subpixel True
    zoom 0.62
    anchor (0.5, 0.5)
    easein 2.5 yoffset -12
    easeout 2.5 yoffset 12
    repeat

transform ch5_mirage_hub_leo:
    subpixel True
    zoom 0.62
    anchor (0.5, 0.5)
    easein 2.5 yoffset -12
    easeout 2.5 yoffset 12
    repeat

transform ch5_arrow_bob_left:
    subpixel True
    easein 1.2 xoffset -6
    easeout 1.2 xoffset 0
    repeat

transform ch5_arrow_bob_right:
    subpixel True
    easein 1.2 xoffset 6
    easeout 1.2 xoffset 0
    repeat

transform ch5_mirage_hub_scy_panel:
    subpixel True
    zoom 0.55
    anchor (0.5, 0.5)
    easein 2.5 yoffset -10
    easeout 2.5 yoffset 10
    repeat

transform ch5_mirage_hub_cory_panel:
    subpixel True
    zoom 0.42
    anchor (0.5, 0.5)
    easein 2.5 yoffset -10
    easeout 2.5 yoffset 10
    repeat

transform ch5_mirage_hub_leo_panel:
    subpixel True
    zoom 0.42
    anchor (0.5, 0.5)
    easein 2.5 yoffset -10
    easeout 2.5 yoffset 10
    repeat
