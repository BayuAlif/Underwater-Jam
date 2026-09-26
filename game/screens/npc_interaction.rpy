screen character_question_visual(title, subtitle):

    modal True

    add Solid("#000000B8")

    text title:
        xalign 0.5
        yalign 0.08
        size 42
        bold True

    text subtitle:
        xalign 0.5
        yalign 0.15
        size 24

    if current_chapter >= 4:
        imagebutton:
            idle "images/characters/rotasi/McIdle.png"
            hover "images/characters/rotasi/McHover.png"
            at selector_4_mc
            action Return("mc")

        imagebutton:
            idle "images/characters/rotasi/CoryIdle.png"
            hover "images/characters/rotasi/CoryHover.png"
            at selector_4_cory
            action Return("cory")

        imagebutton:
            idle "images/characters/rotasi/ClarusIdle.png"
            hover "images/characters/rotasi/ClarusHover.png"
            at selector_4_clarus
            action Return("scyllarus")

        imagebutton:
            idle "images/characters/rotasi/LeoIdle.png"
            hover "images/characters/rotasi/LeoHover.png"
            at selector_4_leo
            action Return("leo")

    elif current_chapter >= 3:
        imagebutton:
            idle "images/characters/rotasi/McIdle.png"
            hover "images/characters/rotasi/McHover.png"
            at selector_3_mc
            action Return("mc")

        imagebutton:
            idle "images/characters/rotasi/CoryIdle.png"
            hover "images/characters/rotasi/CoryHover.png"
            at selector_3_cory
            action Return("cory")

        imagebutton:
            idle "images/characters/rotasi/ClarusIdle.png"
            hover "images/characters/rotasi/ClarusHover.png"
            at selector_3_clarus
            action Return("scyllarus")
    else:
        imagebutton:
            idle "images/characters/rotasi/McIdle.png"
            hover "images/characters/rotasi/McHover.png"
            at selector_mc
            action Return("mc")

        imagebutton:
            idle "images/characters/rotasi/CoryIdle.png"
            hover "images/characters/rotasi/CoryHover.png"
            at selector_cory
            action Return("cory")

screen choose_interactor(title, subtitle):
    use character_question_visual(title, subtitle)

screen character_question_select(title):
    use character_question_visual(title, "Choose by character.")

screen ch4_companion_select(title, subtitle="Choose your companion.", min_affection=0):

    modal True

    add Solid("#000000B8")

    $ scy_aff = getattr(store, "ch4_scy_affection", 0)
    $ cory_aff = getattr(store, "ch4_cory_affection", 0)
    $ leo_aff = getattr(store, "ch4_leo_affection", 0)

    $ scy_ok = (scy_aff >= min_affection)
    $ cory_ok = (cory_aff >= min_affection)
    $ leo_ok = (leo_aff >= min_affection)

    # Safety fallback: if min_affection > 0 and no characters meet threshold, unlock the one with highest affection to prevent softlock
    python:
        if min_affection > 0 and not (scy_ok or cory_ok or leo_ok):
            highest_id = max([("scy", scy_aff), ("cory", cory_aff), ("leo", leo_aff)], key=lambda x: x[1])[0]
            if highest_id == "scy":
                scy_ok = True
            elif highest_id == "cory":
                cory_ok = True
            else:
                leo_ok = True


    text title:
        xalign 0.5
        yalign 0.07
        size 42
        bold True

    text subtitle:
        xalign 0.5
        yalign 0.14
        size 24

    # Scyllarus
    imagebutton:
        idle "images/characters/rotasi/ClarusIdle.png"
        hover "images/characters/rotasi/ClarusHover.png"
        at selector_3_mc
        if scy_ok:
            action Return("scy")
        else:
            action Notify(_("Requires at least %d affection hearts to choose Scyllarus! (Current: %d)") % (min_affection, scy_aff))

    add ("images/ui/ch4_affection/hearts_%d.png" % max(0, min(3, scy_aff))):
        xpos 0.20
        ypos 0.88
        xanchor 0.5
        yanchor 0.0
        zoom 0.55

    if not scy_ok:
        text _("Locked (Need %d hearts)") % min_affection:
            xpos 0.20
            ypos 0.94
            xanchor 0.5
            color "#ff6b6b"
            size 18
            bold True
            outlines [(1, "#000", 0, 0)]

    # Cory
    imagebutton:
        idle "images/characters/rotasi/CoryIdle.png"
        hover "images/characters/rotasi/CoryHover.png"
        at selector_3_cory
        if cory_ok:
            action Return("cory")
        else:
            action Notify(_("Requires at least %d affection hearts to choose Cory! (Current: %d)") % (min_affection, cory_aff))

    add ("images/ui/ch4_affection/hearts_%d.png" % max(0, min(3, cory_aff))):
        xpos 0.50
        ypos 0.88
        xanchor 0.5
        yanchor 0.0
        zoom 0.55

    if not cory_ok:
        text _("Locked (Need %d hearts)") % min_affection:
            xpos 0.50
            ypos 0.94
            xanchor 0.5
            color "#ff6b6b"
            size 18
            bold True
            outlines [(1, "#000", 0, 0)]

    # Leo
    imagebutton:
        idle "images/characters/rotasi/LeoIdle.png"
        hover "images/characters/rotasi/LeoHover.png"
        at selector_3_clarus
        if leo_ok:
            action Return("leo")
        else:
            action Notify(_("Requires at least %d affection hearts to choose Leo! (Current: %d)") % (min_affection, leo_aff))

    add ("images/ui/ch4_affection/hearts_%d.png" % max(0, min(3, leo_aff))):
        xpos 0.80
        ypos 0.88
        xanchor 0.5
        yanchor 0.0
        zoom 0.55

    if not leo_ok:
        text _("Locked (Need %d hearts)") % min_affection:
            xpos 0.80
            ypos 0.94
            xanchor 0.5
            color "#ff6b6b"
            size 18
            bold True
            outlines [(1, "#000", 0, 0)]
