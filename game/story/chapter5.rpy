screen ch5_anomaly_exploration():
    modal True

    $ _ch5_explored_count = (1 if ch5_scy_explored else 0) + (1 if ch5_cory_explored else 0) + (1 if ch5_leo_explored else 0)

    # Keyboard navigation (Left / A, Right / D)
    key "K_LEFT" action If(ch5_exploration_zone == "right", SetVariable("ch5_exploration_zone", "center"), If(ch5_exploration_zone == "center", SetVariable("ch5_exploration_zone", "left"), None))
    key "a" action If(ch5_exploration_zone == "right", SetVariable("ch5_exploration_zone", "center"), If(ch5_exploration_zone == "center", SetVariable("ch5_exploration_zone", "left"), None))
    key "K_RIGHT" action If(ch5_exploration_zone == "left", SetVariable("ch5_exploration_zone", "center"), If(ch5_exploration_zone == "center", SetVariable("ch5_exploration_zone", "right"), None))
    key "d" action If(ch5_exploration_zone == "left", SetVariable("ch5_exploration_zone", "center"), If(ch5_exploration_zone == "center", SetVariable("ch5_exploration_zone", "right"), None))

    # =================================================================
    # CURRENT ZONE DISPLAY (West / Central / East)
    # Guaranteed 1920x1080 rendering with matching background slices
    # =================================================================

    if ch5_exploration_zone == "left":
        # -------------------------------------------------------------
        # ZONE 1: WEST (Mr. Scyllarus Anomaly)
        # -------------------------------------------------------------
        add "bg abyss_zone_left"
        add Solid("#02081320")

        if ch5_scy_explored:
            # Explored: dim sprite, green checkmark above head
            add Transform("ch5_mantis_idle", alpha=0.65):
                xcenter 960
                ypos 620
                at ch5_mirage_hub_scy

            text "✓":
                xcenter 960
                ypos 230
                size 46
                bold True
                color "#4EFA74"
                outlines [(2, "#033b1c", 0, 0), (1, "#000000", 0, 0)]

            text _("Unresponsive (Lost in guilt)"):
                xcenter 960
                ypos 940
                size 17
                color "#83c5be"
                outlines [(2, "#000000", 0, 0)]
        else:
            imagebutton:
                focus_mask True
                xcenter 960
                ypos 620
                idle "ch5_mantis_idle"
                hover "ch5_mantis_hover"
                at ch5_mirage_hub_scy
                action Return("scy")
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"

            textbutton _("✦ Inspect Mirage ✦"):
                xcenter 960
                ypos 935
                style "sea_nav_button"
                text_size 20
                text_bold True
                text_color "#ffd166"
                text_hover_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"
                action Return("scy")

    elif ch5_exploration_zone == "right":
        # -------------------------------------------------------------
        # ZONE 3: EAST (Miss Leo Anomaly)
        # -------------------------------------------------------------
        add "bg abyss_zone_right"
        add Solid("#02081320")

        if ch5_leo_explored:
            # Explored: dim sprite, green checkmark above head
            add Transform("ch5_leo_idle", alpha=0.65):
                xcenter 960
                ypos 620
                at ch5_mirage_hub_leo

            text "✓":
                xcenter 960
                ypos 230
                size 46
                bold True
                color "#4EFA74"
                outlines [(2, "#033b1c", 0, 0), (1, "#000000", 0, 0)]

            text _("Mimic dismissed (Leo joined your side)"):
                xcenter 960
                ypos 940
                size 17
                color "#83c5be"
                outlines [(2, "#000000", 0, 0)]
        else:
            imagebutton:
                focus_mask True
                xcenter 960
                ypos 620
                idle "ch5_leo_idle"
                hover "ch5_leo_hover"
                at ch5_mirage_hub_leo
                action Return("leo")
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"

            textbutton _("✦ Inspect Mirage ✦"):
                xcenter 960
                ypos 935
                style "sea_nav_button"
                text_size 20
                text_bold True
                text_color "#ffd166"
                text_hover_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"
                action Return("leo")

    else:
        # -------------------------------------------------------------
        # ZONE 2: CENTER (Mr. Cory Anomaly)
        # -------------------------------------------------------------
        add "bg abyss_zone_center"
        add Solid("#02081320")

        if ch5_cory_explored:
            # Explored: dim sprite, green checkmark above head
            add Transform("ch5_cory_idle", alpha=0.65):
                xcenter 960
                ypos 620
                at ch5_mirage_hub_cory

            text "✓":
                xcenter 960
                ypos 230
                size 46
                bold True
                color "#4EFA74"
                outlines [(2, "#033b1c", 0, 0), (1, "#000000", 0, 0)]

            text _("Unresponsive (Lost in grief)"):
                xcenter 960
                ypos 940
                size 17
                color "#83c5be"
                outlines [(2, "#000000", 0, 0)]
        else:
            imagebutton:
                focus_mask True
                xcenter 960
                ypos 620
                idle "ch5_cory_idle"
                hover "ch5_cory_hover"
                at ch5_mirage_hub_cory
                action Return("cory")
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"

            textbutton _("✦ Inspect Mirage ✦"):
                xcenter 960
                ypos 935
                style "sea_nav_button"
                text_size 20
                text_bold True
                text_color "#ffd166"
                text_hover_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"
                action Return("cory")

        # When all 3 explored: path deeper unlocks in Center!
        if ch5_scy_explored and ch5_cory_explored and ch5_leo_explored:
            frame:
                xcenter 960
                ypos 855
                background Solid("#0b3c5df0")
                xpadding 28
                ypadding 12
                textbutton _("★ Chase the Real Golden Fish with Miss Leo >>"):
                    text_size 24
                    text_bold True
                    text_color "#ffd700"
                    text_hover_color "#ffffff"
                    text_outlines [(2, "#000000", 0, 0)]
                    hover_sound "audio/sfx/pixel_ui_1.mp3"
                    activate_sound "audio/sfx/pixel_ui_2.mp3"
                    action Return("proceed")

    # =================================================================
    # POV HUD OVERLAY & TABS (1920x1080)
    # Clear, spacious, interactive navigation
    # =================================================================

    # Interactive Zone Tabs & Progress Pill at Top Center
    frame:
        xalign 0.5
        ypos 30
        background Solid("#03121ecc")
        xpadding 22
        ypadding 8

        hbox:
            spacing 16
            yalign 0.5

            textbutton _("◄ WEST: MR. SCYLLARUS"):
                action SetVariable("ch5_exploration_zone", "left")
                text_size 16
                text_bold True
                text_color ("#ffd166" if ch5_exploration_zone == "left" else "#83c5be")
                text_hover_color "#ffffff"
                text_outlines [(1, "#000000", 0, 0)]

            text "|":
                color "#495057"
                size 16

            textbutton _("• CENTER: MR. CORY •"):
                action SetVariable("ch5_exploration_zone", "center")
                text_size 16
                text_bold True
                text_color ("#ffd166" if ch5_exploration_zone == "center" else "#83c5be")
                text_hover_color "#ffffff"
                text_outlines [(1, "#000000", 0, 0)]

            text "|":
                color "#495057"
                size 16

            textbutton _("EAST: MISS LEO ►"):
                action SetVariable("ch5_exploration_zone", "right")
                text_size 16
                text_bold True
                text_color ("#ffd166" if ch5_exploration_zone == "right" else "#83c5be")
                text_hover_color "#ffffff"
                text_outlines [(1, "#000000", 0, 0)]

            text "|":
                color "#495057"
                size 16

            text "Echoes: [_ch5_explored_count]/3":
                size 16
                color "#90e0ef"
                outlines [(1, "#000000", 0, 0)]

            if _ch5_explored_count >= 3:
                text "★ Ready!":
                    size 16
                    color "#4EFA74"
                    bold True

    # -----------------------------------------------------------------
    # NAVIGATION ARROWS (Hand-drawn buttons on left & right margins)
    # -----------------------------------------------------------------
    # Left Navigation Arrow (shown when at Center or Right)
    if ch5_exploration_zone != "left":
        vbox:
            xpos 45
            yalign 0.50
            spacing 8
            at ch5_arrow_bob_left

            imagebutton:
                idle "ch5_arrow_left"
                hover Transform("ch5_arrow_left", zoom=1.08)
                action If(ch5_exploration_zone == "right", SetVariable("ch5_exploration_zone", "center"), SetVariable("ch5_exploration_zone", "left"))
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"

            text ("◄ Mr. Cory" if ch5_exploration_zone == "right" else "◄ Mr. Scyllarus"):
                xalign 0.5
                size 15
                bold True
                color "#caf0f8"
                outlines [(2, "#000000", 0, 0)]

    # Right Navigation Arrow (shown when at Center or Left)
    if ch5_exploration_zone != "right":
        vbox:
            xpos 1755
            yalign 0.50
            spacing 8
            at ch5_arrow_bob_right

            imagebutton:
                idle "ch5_arrow_right"
                hover Transform("ch5_arrow_right", zoom=1.08)
                action If(ch5_exploration_zone == "left", SetVariable("ch5_exploration_zone", "center"), SetVariable("ch5_exploration_zone", "right"))
                hover_sound "audio/sfx/pixel_ui_1.mp3"
                activate_sound "audio/sfx/pixel_ui_2.mp3"

            text ("Mr. Cory ►" if ch5_exploration_zone == "left" else "Miss Leo ►"):
                xalign 0.5
                size 15
                bold True
                color "#caf0f8"
                outlines [(2, "#000000", 0, 0)]

label chapter5_start:

    $ current_chapter = 5
    $ current_cycle = "night"

    scene black
    with fade
    stop music fadeout 2.0
    play music "audio/bgm/unsettling_moment.ogg" volume 0.7 fadein 2.0

    "It’s dark.."
    "it’s so dark in here.."
    "I can't be scared now..!"
    "I can't go back now… *sniffle*"

    "It’s so quiet… yet somehow, I also hear a chorus of strange whispers tickling my ears."
    "I can’t help but close my eyes."

    show mc holdcry at mc_left
    with dissolve

    mc "Mama.. It’s so scary down here..."

    "I trudged forward blindly, but no matter where I turned, darkness was all that greeted me."
    "Has it been five minutes...? Ten minutes...? Twenty...? Minutes blurred together until I lost all concept of time.."
    "My legs finally gave out."
    "Collapsing to the cold seabed, I curled, hugging my knees against my chest."

    "......................."
    ".... alone."
    ".... will always be alone…….."

    cory_fake "Don’t be scared guppy we’re here for ya…"

    show mc shock at mc_left
    mc "M- mr. Cory...?!"

    "I whipped around immediately, but found nothing."

    scy_fake "That’s right guppy, we’ll protect you! {font=DejaVuSans.ttf}K̷̺͗a̷̹̅ķ̷̋a̸̞͊k̵͆͜ä̴̫{/font}"

    show mc o at mc_left
    mc ".......m-mr Larus?"

    cory_fake "Right here, guppy,"

    "Scrambling frantically to my feet, I sprinted straight toward the direction of Mr. Cory’s voice."

    hide mc
    with dissolve

    jump ch5_exploration_hub

label ch5_exploration_hub:

    scene bg abyss_depths
    with dissolve
    play music "audio/bgm/chap_5_exploration.ogg" volume 0.7

    if ch5_scy_explored and ch5_cory_explored and ch5_leo_explored:
        jump ch5_chase_real_gold

    call screen ch5_anomaly_exploration
    $ _ch5_pick = _return

    if _ch5_pick == "scy":
        jump ch5_scy_sequence
    elif _ch5_pick == "cory":
        jump ch5_cory_sequence
    elif _ch5_pick == "leo":
        jump ch5_leo_sequence
    else:
        jump ch5_chase_real_gold

label ch5_scy_sequence:

    scene bg abyss_zone_left
    with dissolve

    show scy_mirage at npc_right
    with dissolve

    show mc excited at mc_left
    with dissolve

    mc "Mr Larus!! There you are!!"

    "My eyes caught a familiar glow from Mr. Larus's hand."

    show mc o at mc_left
    mc "Wait, is that the golden fish? You actually caught it?!"

    scy_fake "Sure did! This magnificent Mr. Larus has successfully captured the very fish you were after."

    show mc happy at mc_left
    mc "Yes!! Then we did it! We just have to find a way back up and my mom can finally get better!"

    scy_fake "I can’t…"
    scy_fake "not yet…"

    show mc shock at mc_left
    mc "But why Mr. Larus?"

    scy_fake "It’s them. I can still hear them."

    show mc o at mc_left
    mc "Who..?"

    scy_fake "Don’t you hear them?"

    mc "Hear what?"

    scy_fake "Come closer guppy, you are too far away."

    "I swam closer."

    play sound "audio/sfx/attack_1.mp3"
    "Audio effect bisikan bisikan (\"No please dont...\" *knife slice* \"I have a family.\" *screams of pain*)"

    "The voices grew louder the closer I got. They overlapped until I could no longer tell what they were saying."

    scy_fake "Please make them stop guppy..."

    "Mr. Larus holds out his hand to me, a crazed, desperate look in his eyes terrifies me."

    show mc holdcry at mc_left
    mc "I- I cant"

    show scy_mirage burst at npc_right with vpunch
    scy_fake "{font=DejaVuSans.ttf}w̷̳̓ͅĥ̶̥̩̋y̷̒̓͜ ̶̦̣̔̕w̸̜̋o̴͎̪̭͆̌n̴̬͂ṫ̸̛͇̳̤ ̷͓̎̀͜͝y̵̙̦̣̔̂ö̸̩͈́ũ̴͚͐ ̴̱̰̗͐͊m̴̛̜̑̈́a̷̡̗͊̋͝k̵̰̻͕͆͊e̶͈͋̈́ ̴̱̦͑̈́̈́t̸͈̳̎h̸̢͎̟̿ê̸̘̕m̷͔͌̚̕ ̵̟̠̺̆́͘s̶̻͚̺̒̂t̶͓̃ŏ̶̟͕͐p̵̺̰̪̀̍̃{/font}"
    scy_fake "{font=DejaVuSans.ttf}M̵̢̼̦̩̝͙͈͖̟̞͚̟̿̉̿͐ȃ̶̡̧̗̜̩͕̖͚̦̬̟̮̾͑̏̓̈́͗̎͘̚͜k̴̙̽̒e̷̢̓ ̵̨͈͇̙̙̩̗̖͇͚̟̘̣̇̀͑̃̎͒̽̉͝͝t̵̛̥̟͐̄̿̿̌̾̽̌̎͆̄̅̈̕ȟ̸̢͎̭͉̤̖̝͍̤̇̒̆̈́̍̾͘ͅē̸͈̊̐͠m̶̨̟̬͎̬̔̋̐ͅ ̶̠̦̊̒̊̀̅ͅs̸̖͚̞̳̙͚͐͒̒̌̈̾̈́̿̃͛̚͘͝t̷̳̟̤͇̬͚͎̫̲̪͋͋̒͑̀̓͆̈͜͠͝o̴̲̥͉̅́p̸̺̬̠͈͎̥̖̝̲̼̱̱̠̖̌̓̈́̄̆{/font}"
    scy_fake "{font=DejaVuSans.ttf}Ȋ̶͎͂ ̶̛̗̇͝ń̷̝̘̦e̷̢̱̫͒̇e̵̫̹͌ͅḏ̶͋̂͜ ̵͔͕̗̏͑y̴̰͇̅̀̌o̸̫̝͚͒̆u̷̮̼͉̐ ̴̲̩̅t̸͚͗̇o̸̳̦͆̀͜ ̵̘͐̕m̸͎̋à̵̝̥̎͝k̴̳̪̀e̴͓̓͂ ̵͔̉́t̸̨̑̒̚ḩ̸̭̅ë̴̼̆͝m̸͎͉͛̾ ̶͕̱͎͗̀̒s̵̫͕̠͆ẗ̸̺̞̻́̽ô̴̢͙̬p̸̢̠̼̋͊{/font}"

    show mc shock at mc_left
    mc "you’re scaring me…"
    "I backed away."

    scy_fake "Make them stop, guppy."

    show mc holdcry at mc_left
    mc "I-I don’t know how!"

    scy_fake "{font=DejaVuSans.ttf}You do. You can make them stop if you’d just g̴̜̽ḭ̷̄v̴̥͛ë̶̲́ ̵̱͘m̶̛̯e̶̖͊ ̸̗̋ỹ̸̮o̷̙͌u̶̝͊r̷̖͠ ̸̬̇h̷̭͝a̴̬͝n̵͚̈́d̴̛̳.̷̳́{/font}"

    "I hesitate, before slowly reaching out to grab his hand. Before I could, a voice screams out."

    play sound "audio/sfx/thump.mp3"
    show scy surprise at farright
    with vpunch

    scy "Stay away from it!"

    "Hearing another Mr.Larus I take my hand back looking towards the voice."

    scy "That wretched thing is not me!"

    show mc shock_hu at mc_left
    mc "T-Two M- Mr.Larus!? 0.0"

    scy_fake "Guppy don’t be fooled, that buffoon isn’t me! It’s trying to stop you from helping me."
    scy_fake "Just take my hand and we can finally end this charade."

    scy "No! Don’t listen to it Guppy, it’s trying to fool you, I’m the real one! You mustn’t give yourself to it!"

    menu:
        "“If I give you my hand... will the voices stop?”":
            scy_fake "Yes."
            scy_fake "You will free me from these burdens."
            scy_fake "Then we can go back to our adventures.. with you as a fish."
            "I slowly reached toward him."
            scy_fake "That’s right, Guppy. Just a little closer..."
            "Before I could take his hand, Mr. Larus suddenly shoved me aside."

            play sound "audio/sfx/attack_3.mp3"
            show scy default at center with vpunch
            scy "Get away from her, you slugtardly thing!"
            "Mr. Larus charged forward, throwing a punch at the Mirage."
            "The second Mr. Larus easily dodged."

            scy_fake "There it is. Violence."
            scy "shut up!"
            scy_fake "That is all you know."
            scy "You know nothing about me!"
            scy_fake "A soldier. A weapon. A murderer."
            scy "...No."
            scy_fake "No matter how hard you try to change, a murderer will always be a murderer."
            scy "I’m not—"
            scy_fake "Then prove it."
            "The Mirage held out its hand."
            scy_fake "Give me your hand, Scyllarus. Give up your life. This is the only way you can atone for your sins."
            "The moment their hands touched, his body went completely still and Mr.Larus’s eyes lost their focus."

        "“No! I’m not giving you my hand!”":
            "I swim away and hide behind the new Mr. Larus."
            show scy default at mc_center_left
            show mc sad at farleft
            scy "Guppy, stay behind me!"
            scy_fake "Well, well, well..."
            scy_fake "If it isn’t the great hero of the sea!"
            scy_fake "The mighty Scyllarus. The Empress’s finest soldier."
            scy "Shut up."
            scy_fake "The loyal little weapon who did exactly as he was told."
            mc "Mr. Larus..."
            scy_fake "How many were there again?"
            scy "Enough."
            scy_fake "How many did you kill?"
            scy "I said enough!"
            scy_fake "You remember them, don’t you?"
            scy_fake "All those innocent lives you took."
            "Mr. Larus clutched his head."
            scy "Stop..."
            scy_fake "No matter what you do, you will always be a murderer."
            "The screams grew louder."
            scy "It’s not my fault! I’m not a murderer!"
            scy "I only did what I was ordered to!"
            show mc holdcry at farleft
            mc "Mr. Larus! Don’t listen to it!"
            scy "Make them stop! Make them stop!"
            "He dropped to his knees, covering his ears to try and block out the voices."
            scy "Please"

    hide scy_mirage
    with dissolve

    show mc holdcry at mc_left
    mc "Mr. Larus!"
    "Mr. Larus is clutching his head, trembling as the endless cries echoed around him."

    mc "Mr. Larus! snap out of it!“"
    "It was as though he couldn't hear me at all."

    show mc sad at mc_left
    mc "My voice can’t seem to reach him right now…"
    "I looked around desperately."
    mc "I need to find another way to bring him back."

    $ ch5_scy_explored = True
    hide scy
    hide mc
    with dissolve

    jump ch5_exploration_hub

label ch5_cory_sequence:

    scene bg abyss_zone_center
    with dissolve

    show cory_mirage at npc_right
    with dissolve

    show mc excited at mc_left
    with dissolve

    "My eyes caught a familiar glow from Mr. Cory's hand."
    mc "Mr cory!! You found the golden fish!"

    cory_fake "Hah sure did.. all for you to take guppy.."
    cory_fake "Now all there is left is to find my sister…"

    show mc happy at mc_left
    mc "mhm! We'll surely find her Mr.Cory!"

    cory_fake "Yeah.. I'll drag her back home by my own fins.. back to freshwater.. back where.. Family is…"

    show mc o at mc_left
    mc "huh…?"
    mc "but..! But your sister isn't made for-"

    cory_fake "Shut up..! I’ll keep her safe.. I'll keep her by my side… even if it kills her.."
    cory_fake "So I can focus on taking care of her…"
    cory_fake "At least Im good at taking care of guppies ay..?"
    cory_fake "Even when I don’t have zillions of clams or.. a job in ocean-"
    cory_fake "Then you can play with her guppy, we'll have the bestest of times…"

    show mc shock at mc_left
    mc "I.. I don't want to play with.. a deadbody…"

    cory_fake "Then we can all hit up the samba festival at amazon together."
    cory_fake "Tomorrow, and tomorrow, and tomorrow..."
    cory_fake "The future is suffocatingly beautiful."
    cory_fake "I can see my sister’s face, healthy and laughing at you while you’re wearing that ridiculous anemone costume."
    cory_fake "We wouldn’t give a damn about anything in this world."
    cory_fake "Not even a tiny bit."
    cory_fake "Even if a supernova shattered the sky that very night and crushed everything to dust."

    show mc holdcry at mc_left
    mc ".... mr. cory…."

    cory_fake "Just take my hand, guppy…"
    cory_fake "Help me search for her.."
    cory_fake "{font=DejaVuSans.ttf}Y̸̩͗o̵̱͝u̷̼̾’̴̻͌l̶̳͠l̵̰͘ ̴̰͂n̵̛̳ẹ̴̇v̸͓̓e̵̘͛r̴̬̋ ̸̬̂b̷̼͋e̷̘̍ ̷̢̿a̴̜͊l̵̳̈́o̴̙͛ņ̶̇e̶̠̐ ̸̢̋a̶̼̋g̸̝͝a̷̫͗i̵͉͊n̶̗͑,̶̞̊ ̴͍̏{/font}"

    play sound "audio/sfx/splash.mp3"
    show cory upset at farright with vpunch
    cory "Guppy, That ain't me-!!"

    "I was suddenly swept away from him."
    mc "...?!"

    cory "what in the eel..?? Sthat supposed to be me?!"

    cory_fake "Hah.. well look what we got here…"

    show mc shock_hu at mc_left
    mc "Two Mr.. Cory's…? o.o"

    cory_fake "How much longer are you going to keep her waiting?"

    cory "I ain’t know what you talking about.."

    cory_fake "Don’t play fool with me, I know you."
    cory_fake "I know you better than you’ll ever know yourself."
    cory_fake "And I know you want your sunshine of a little sister back more than anything."

    cory "Don’t you dare.. talk about her…!"

    cory_fake "Poor little thing eh? Had to be separated from her precious brother"

    menu:
        "“Mr. Cory don’t listen to the other Mr.Cory..!”":
            cory_fake "Are ya really going to let a one minute old kid dictate your life choices?"
            cory_fake "Aye, we’re better than that Cara…"
            cory_fake "Besides, she’s more worth the hassle than some random guppy would ever be.."
            cory "...!!"
            cory_fake "They didn’t help you through the toughest time in your life like she did.."
            cory "They did..! I learnt a lot from the little guppy"
            cory_fake "Ah but did they shield you from your familia’s expectations..?"
            cory_fake "Were they there when you were thinkin about.. how worthless you are?"
            cory_fake "And what did you do to repay her, huh?"
            cory "I didn’t.. have any choice..!"
            cory_fake "I bet she cried for days.. havin to defend herself in a brand new world"
            cory_fake "How could ya, even after hearin how dangerous sea is at night.. You still—"
            show cory_mirage scream at npc_right with vpunch
            cory "SHUT THE FUGU UP…!"

        "“Mr. Cory.. Mr Cory’s right.. we should search for your sister!”":
            cory_fake "See even the guppy agreed.."
            cory_fake "They’re basically givin you free pass to abandon them, cara"
            cory_fake "All for your precious little sister"
            show mc pout at mc_left
            mc "Hey! That’s not what I said-!"
            cory "... No! I can’t.. I can’t face her anymore..!"
            cory "I left her.. Even after she was beggin to stay.."
            cory_fake "Then why are ya wastin’ time here?"
            cory "...What?"
            cory_fake "Our sister’s out there, Cory. She’s been waitin’ for you all this time."
            cory_fake "You can’t fix what happened by babysittin’ some guppy."
            cory_fake "Come on, Cory. How many more times are ya gonna choose someone else before you finally choose your own familia?"
            cory_fake "Leave the damn Guppy behind.."

    hide cory_mirage
    with dissolve

    "Mr Cory is way too deep in his guilt and grief."
    "My voice can’t seem to reach him right now…"
    "When adults argue, it’s better to not bother them…"
    "I have to find another way."

    $ ch5_cory_explored = True
    hide cory
    hide mc
    with dissolve

    jump ch5_exploration_hub

label ch5_leo_sequence:

    scene bg abyss_zone_right
    with dissolve

    show leo_mirage at npc_right
    with dissolve

    show mc o at mc_left
    with dissolve

    mc "Miss Leo..! Is that the.. Golden fish in your hand?"

    "A familiar glow of gold pulses in her flippers."

    leo_fake "Mhm it sure is, I caught it for us."

    show mc happy at mc_left
    mc "yaay! Thank you miss Leo!"

    leo_fake "..."
    leo_fake "I have become what I’ve always dreamt to be…"
    leo_fake "And yet I…"

    show mc o at mc_left
    mc "Huh what do you mean..?"

    leo_fake "You understand don’t you?"

    mc "me…?"

    leo_fake "The hunger to become something greater than what you are."
    leo_fake "To finally become the creature you always wished you could be."

    "Miss Leo caresses the dimming golden fish in her flippers with a conflicted expression."

    mc "mn.. I think I get it..?"
    mc "If I were to become a fish, I’d wanna be the coolest fish ever!"

    leo_fake "Hah.. but will everything really be as beautiful as you imagined..?"
    leo_fake "Will it really be worth it..?"
    leo_fake "To become a prisoner of your own body"
    leo_fake "To become something you no longer have control of…"
    leo_fake "What if.. what you become, is something that you never thought you'd be..?"

    show mc pout at mc_left
    mc "nnn.. I’ll.."

    "A second miss Leo steps between us, studying her reflection with piqued interest."

    show leo default at center
    with dissolve

    leo "Oh? Heh.. Are you supposed to be me? Interesting~!"

    show mc shock at mc_left
    mc "Two miss leos…?"

    show leo_mirage scream at npc_right with dissolve
    leo_fake "It’s like looking into your own unsightly reflection doesn’t it?"

    leo "Nah, for something that’s imitating me, you sure look pretty ugly~!"
    leo "What, are you supposed to cast depression upon me?"

    leo_fake "You’ve lost so much-"

    leo "Oh no~! Woe is me~! I'm just a misunderstood biiiig leopard seal who needs some reaaaal love~!"
    leo "Especially when I have grown so big and scaaary and ugly and everybody leaaaaves me~!"
    leo "And that I hurt eeeveryone around me even when I waaaant them to staaay~!"

    leo_fake "Not only that but you’ve-"

    leo "I’ve killed my friends, with my own teeth and claws.."

    show mc shock_hu at mc_left
    mc "...!"

    leo "you’ve got any jabs left to say, dear?"

    leo_fake "I...."

    leo "Mhm, exactly what I thought~!"
    leo "Come on Guppy, let’s leave this chopped mimic alone."
    leo "Their words aren’t worth paying attention to."

    show mc o at mc_left
    mc "Ah but what about the golden fish..?"

    leo "mm? It’s fake.. They’re not glowing as bright as the scales you have.."

    hide leo_mirage
    with dissolve

    "Her flippers hastily gripped my hand, tugging me as she start to swam."

    mc "Is it.. true that you’ve.. killed…?"

    leo "... what of it? Don’t tell me you’re scared~?"
    leo "Don’t worry I’m not going to kill you~!"
    leo "You’re more than a friend to me, little guppy"

    $ ch5_leo_explored = True
    hide leo
    hide mc
    with dissolve

    jump ch5_exploration_hub

label ch5_chase_real_gold:

    scene bg abyss_zone_center
    with fade

    show mc serious at mc_left
    show leo default at center
    with dissolve

    mc "Let's go miss Leo..! we need to hurry.. before the real gold slips away!"

    leo "You’re leaving behind your friends just like that? That's new.."

    mc "They can wait! I'll free them once we get the golden fish!"
    mc "that's why we need to be fast, miss Leo!"

    leo "Hmm.. you're right, they won't budge even if we try to wake them up.."

    "We swam further down through the trench, until a radiant, genuine rainbow glow pierced through the darkness."

    show mc excited at mc_left
    mc "Miss Leo is that?!"

    leo "Oh why yes, it sure looks like the real-"

    stop music fadeout 1.0
    "Before I can swim any closer, the water around us starts to quake violently without warning."

    play sound "audio/sfx/thump.mp3"
    with vpunch
    play sound "audio/ambience/unsettling_moment.ogg"

    ban_unknown "{size=+12}{b}THOU SHALT NOT PASSETH…!{/b}{/size}"

    "A cracking roar tears through the darkness, loud enough to deafen me."
    "The pressure climbs so high it’s almost bone crushing."
    "It became a sensation that one would describe as close to death."

    show mc shock_hu at mc_left
    mc "guh…!"

    leo "careful now.."

    "I feel her strong slippery limb snaking around me."
    "Once the rumbling stops, what came into view is Kraken? A Chymera of.. several sea mythology creatures mixed into one."
    "Guiding the golden fish with its monstrous abyssal limbs."

    show mc pout at mc_left
    mc "I need that golden fish.. mr.. big deep sea Shakespearean king! Can you move out of the way?"

    ban "The fish thou chase… is no gift. ‘Tis the last scream of the deep."
    ban "I wonneth't alloweth a youth blind'd by gre'd maketh useth of the gold yond couldst end the greatest of wars.."

    leo "I'm riiiight over here too you know~!"
    leo "My apologies for interfering with your grand speech, your highness.."
    leo "But everyone has their right to pursue the golden fish…"
    leo "Besides.. you can't make use of the golden fish’s power yourself.. can you, O banished one?"

    show mc o at mc_left
    mc "Banished one…?"

    ban "{size=+6}{b}BANISHED?{/b}{/size} Child… I was unwritten. The waves scrubbed my name from their pathetic hymns…"
    ban "I'm acknown, therefore i shall useth the young to maketh the divine wish."
    ban "One yond shall finally free us from this centuries of torment.."

    show mc holdcry at mc_left
    mc "You want me to make a wish for you and your kind…?"
    mc "But I need to save my friends.. I need to save mama and papa.. I need to fix the sea.. I need to be a fish..!"

    leo "Personal opinion but I think you should narrow down those wishes~"
    leo "You’re too greedy for your own good, little guppy."
    leo "And I don’t think favoring his wish is a good idea.."
    leo "They’re banished by the Goddess for a reason.."

    ban "A goddess' crown doth not a saint make. Nay, her justice is but pageantry while we rot in her shadow!"
    ban "That wicked golden fish.. she toys with our agony as though it were sport! Are we clowns in her circus of suffering?!"
    ban "If wisdom guides her hand, What madness is this, to arm fools with godfire and call it mercy?!"
    ban "Oh, what cruel irony, to be damned by the very gift meant to save us!"

    leo "I think you’re one of the fools that shouldn’t get anywhere near the sacred gift."

    ban "Silence!"

    show mc o at mc_left
    mc "Are you saying.. That the goddess is.. Not being fair?"

    ban "Precisely what I’ve been saying.."
    ban "If thou won’t lend us its power.."

    "Enormous shadowy tentacles rise like colossi from the seabed."
    leo "Brace yourself, Guppy! We have to fight our way through!"

    call banished_duel

    stop music fadeout 1.5
    scene bg abyss_depths
    with vpunch

    "One of its strong limbs curls around me bringing me close to it."

    show mc shock_hu at mc_left
    mc "waough-!"

    ban "Then I shalt walketh thee to thy deepest nightmare.."

    jump ch5_nightmare_bedroom

label ch5_nightmare_bedroom:

    scene black
    with fade
    play music "audio/ambianceprologue.mp3" volume 0.5 fadein 2.0

    "My vision is suddenly engulfed in pitch black leaving me and Mr banished one in a surreal scene."
    "It's as if we're on a whole different dimension.."
    "The once dark abyssal monstrosity shrinks itself to picture.. mama?"

    scene bg bedroom_dream
    with Dissolve(1.2)

    mama "sweetheart.."

    show mc shock at mc_left
    with dissolve

    mc "mama.. "

    "There she is laying down on the bed, her frame engulfed within layers of blankets."
    "I was immensely focused on her to notice that I’m standing in our shared room."
    "My instincts brought me close to her into a hug."
    "She felt… warmer than the last time I held her."

    mama_fake "What kind of herbs did you bring for me today?"

    show mc o at mc_left
    mc "herbs..? Ah!! Right I almost forgot I-"

    "Frantically I checked my bag for greens, pulling up a small container filled with mushed greens and a plastic spoon."

    show mc happy at mc_left
    mc "Here! Today I brought Seabloom!"
    mc "I heard that it can help your heart work better!"

    mama_fake "Thank you, dear.. You always work so hard for me."

    mc "I want you to get better. Then… we can all be together again."

    mama_fake "All of us?"

    mc "Mhm! You, me, and Papa."
    mc "Mama? Do you think Papa is coming home soon?"

    mama_fake "I don't know, sweetheart."

    show mc serious at mc_left
    mc "He'll come back. I'll make sure of it."
    mc "That's why I'm going to catch the shiny golden fish! And if it really can grant wishes…I'll wish for you to get better."
    mc "I'll wish for Papa to come home. And I’ll save my friends. And maybe I can even finally become a fish like I've always dreamed of!"

    mama_fake "Then perhaps you could use it to help Mr. Banished one too."

    show mc o at mc_left
    mc "But why are the deepseafolks banished by the Goddess.."
    mc "The Goddess wouldn’t just banish good people would she..?"
    mc "Wouldn’t that mean they did something wrong..?"

    mama_fake "FALSITIES! Ahem No, sweetheart, they were banished because people feared what they don’t understand."
    mama_fake "Perhaps they were never the monsters everyone believed them to be."
    mama_fake "But who would believe them now? Who would go all the way down here to help them?"
    mama_fake "And that golden fish..? It’s nothing but a tool for chaos, dear."

    show mc shock at mc_left
    mc "huh..? But it can grant wishes! I can wish for the sea to be great again!"

    mama_fake "You see.. when something so powerful only appears when the situation is at its peak of havoc."
    mama_fake "Wouldn’t it cause more trouble?"
    mama_fake "If it fell to the wrong hands.. It could turn the sea upside down."

    show mc o at mc_left
    mc "Then.. wouldn’t it be better if such a thing were to never exist..?"

    mama_fake "Good kid! You’re so smart aren’t you."
    mama_fake "Not just that.. But having one wish be granted.. Doesn’t ensure all goes well."
    mama_fake "It’s not that easy to prevent disasters.."
    mama_fake "Just because someone’s a goddess, doesn’t guarantee that they’re doing it for a good cause.."
    mama_fake "I’m afraid she just wanted free entertainment.. Even after she left.."
    mama_fake "Ah, haha but that aside Mr Banished One still needs that golden fish to break the curse~!"
    mama_fake "And You’re the only one who can help him, my dear."
    mama_fake "All you have to do… is make the wish."

    show leo default at npc_right
    with dissolve

    leo "Mmm but I say, fulfilling your biggest dream would be more rewarding, no?"

    "Miss Leo suddenly made an appearance on the opposite of mama’s bed."

    mama_fake "Impudent! Nobody invited the likes of you to this house-!"

    leo "As if i need permission to enter my own house."

    show mc shock at mc_left
    mc "Huh? Your house? This is my house miss leo."
    mc "I don’t remember having a sealbling?"

    leo "Oh did I say that? You must’ve heard me wrong~"
    leo "Mmn that aside~ would you really let this pathetic imitation of your mother hinder you from acquiring your dream life?"
    leo "There’s only one golden fish in the world, little guppy. You can’t be making the wrong decision now."

    mama_fake "That’s right, sweetheart… you only get one wish."
    mama_fake "You can’t ask it to heal me, bring your father home, and save those friends you care about."

    show mc holdcry at mc_left
    mc "Then… what am I supposed to do?"

    mama_fake "Help the banished one, and he can free your friends."
    mama_fake "Maybe he can even cure me too."

    show mc o at mc_left
    mc "really? How do you know of that, mama? Are you friends with the banished one?"

    mama_fake "Mm, of course I am, we were.. once friends back in the glory days of the city before it was banished down here."

    mc "But mama you can’t swim let alone dive!"

    mama_fake "Oh I.. uhh it was back when.. I used to have the ability to swim..?"

    mc "You’ve never told me that before."

    mama_fake "There are many things you don’t know about me my dear."

    show mc serious at mc_left
    mc "....."
    mc "Mama wouldnt know about any of this, she never knew about any sea city, and she definitely can’t swim."
    mc "Mama.. wouldn’t even speak to me this much.. last time i seen her."
    mc "She would just lay there.. as I feed her my medicines.."
    mc "I thought everything finally went back to normal but.."
    mc "You’re definitely the banished one huh..?"

    leo "Finally! Took you long enough, little guppy!"

    stop music fadeout 1.0
    play sound "audio/sfx/thump.mp3"
    with vpunch

    mama_fake "{size=+8}{b}ENOW OF THIS NO MORE BRAIN THAN STONE GAME!{/b}{/size}"

    jump ch5_the_final_choice

label ch5_the_final_choice:

    play sound "audio/ambience/unsettling_moment.ogg"
    "The walls starts to melt, the perfect picture of home demolished."

    scene bg abyss_depths
    with Dissolve(1.5)

    "The golden fish appears yet again but within the dark engulf of the banished one."
    "It floats toward me, futilely flopping about within my hand."

    ban "Hither's the deal young one."
    ban "Thee maketh a wish f'r the deep."
    ban "And i free thy precious friends out of misery."
    ban "Wish aught other than this.."
    ban "And thy friends gets did trap hither down with us f'r eternity, in an endless torment yond is their own past."
    ban "So little Guppy…"
    ban "{size=+4}What will you wish for?{/size}"

    menu:
        "“Cure Mama and bring papa back home”":
            $ ch5_ending_choice = "bad"
            jump ch5_ending_bad

        "“I wish for the golden fish to never ever exist..!”":
            $ ch5_ending_choice = "true"
            jump ch5_ending_true

        "“I wish to finally become one with the sea!”":
            $ ch5_ending_choice = "feral"
            jump ch5_ending_feral

label ch5_ending_bad:

    show mc holdcry at mc_left
    with dissolve

    "My fingers trembled as i hold the fish in my hand."

    mc "I…I wish for mama to get better and papa to come home!"

    play sound "audio/mysterious_golden_looking.ogg"
    "The golden fish suddenly shines brighter."
    "The entire ocean is engulfed in golden light."

    mc "Ah—!"

    "For a moment, everything disappears."

    scene black
    with fade
    pause 1.0

    scene bg bedroom_dream
    with fade

    "I open my eyes to see that i’m back at home."
    "A familiar scent of food, caught my attention. I run into the kitchen."

    show mc excited at mc_left
    with dissolve

    mc "MAMA!"

    "I run toward mama who’s up right, humming as she made my favorite soup."

    mama "Hello my darling, how have you been?"

    mc "You wouldn’t believe the last few days i’ve had so there’s this–"

    play sound "audio/sfx/thump.mp3"
    with vpunch

    "The front door suddenly flings open in haste."
    "And at the door, I see papa standing.."
    "He looked exactly the same as I remembered.. It’s as if he never left in the first place."
    "But his face.. There’s something off about it… like relief and fear mixed into a face?"

    papa "My loves! There’s no time to explain we need to run, right now-!"

    show mc shock at mc_left
    mc "P-papa?! What’s going on?"

    play sound "audio/sfx/splash.mp3"
    play sound "audio/underwater_current.mp3"

    scene bg tsunami_approaching
    with vpunch

    "As i ran hand in hand with mama and papa, i turn back to see the ocean had begun to rise and an enormous wave is forming in the distance."
    "The wave surges toward the shore."

    scene black
    with fade

    "I may have gotten what I wished for, but the sea did not."
    "It still swells with regret and agony."
    "Perhaps Mr Banished One was right…"
    "It wouldn’t all be that easy huh…"

    pause 1.5

    $ chapter5_done = True

    "{size=+8}{color=#e63946}{b}BAD ENDING: THE RISING TIDE{/b}{/color}{/size}"

    $ MainMenu(confirm=False)()
    return

label ch5_ending_true:

    show mc serious at mc_left
    with dissolve

    "My fingers trembled as i hold the fish in my hand."
    "I stared down at its face, the golden scales reflecting my conflicted expression."
    "At times where I have to choose over big things like these.."
    "I usually let mama decide.. I would ask Mr.Cory and or Mr. Scyllarus but.."
    "But I have to make my own choice now.."
    "I need to grow up and decide things on my own for the better.."

    mc "If.. the golden fish is really a tool that could cause chaos…"
    mc "Then.. I.. I wish for the golden fish to never ever exist..!"

    mc "I…I don’t wanna do this anymore!"

    ban "What?"

    mc "I wish for the golden fish to be gone once and for all!!"

    play sound "audio/sfx/pixel_death.mp3"
    with vpunch

    "{size=+10}{b}CRACK!{/b}{/size}"

    "The golden fish dissolves into countless shimmering particles, scattering into the surrounding waters."
    "The suffocating darkness that had consumed the sea begins to fade."

    show mc o at mc_left
    mc "It’s gone… It’s really gone…"

    ban "Thank you..."

    "I turned to face Mr. Banished one."

    ban "We’ve been cursed down here for centuries, wrongly imprisoned by the goddess. Being down here for so long corrupted our minds. I apologise for how I went about things, and because of you, we can finally be free to return to the surface."

    "I look around for Ms. Leo, but she seems to have disappeared into the shimmering light with a soft, peaceful smile."

    show scy smile at farright
    show cory proud at center
    with dissolve

    scy "You did it, little guppy!"
    cory "Aye, you really did it, cara!"

    show mc happy at mc_left
    mc "You’re back! You’re safe!"

    scy "Whatever you just did, I can feel it... the voices... the screams in my head... they've finally quieted."
    cory "The sea is different now... peaceful..."

    show mc sad at mc_left
    mc "But… What about mama and papa…?"

    cory "Sometimes, doing the right thing means accepting that you can't have everything."
    scy "Indeed. But you possess a strength far greater than any wish, little guppy. You chose truth over an easy escape."

    scene white
    with Dissolve(2.0)

    play music "audio/ambianceprologue.mp3" fadein 2.0
    scene prologue_day
    with Dissolve(1.5)

    "Ah, the rivershore. A serene calming scene adorned by the rustling wind of leaves."
    "I lowered myself to the ground, having my best grin on display ready to greet my fish friends."

    show mc happy at center
    with dissolve

    mc "Good precious morning mr carpado! Morning ms betta! Hello to silly eely billy! And Mr. Cory!"
    mc "You know guys, I had a reaaally strange dream last night!!"
    mc "I went to an adventure in the sea! And I met lots of fishes and they can talk!!"
    mc "mnn I was also chasing something.. But I couldn’t.. really remember what.."
    mc "I wish I can actually.. meet something that could take all my problems away"

    "The corydoras nudges me on the finger, as if it’s offering comfort."

    mc "Aww! Thank you Mr. Cory! Don’t worry I’ll be fine!"
    mc "Just means that I have to work extra hard to fix everything."
    mc "Maybe I’ll.. be a doctor to help cure mama.. or or a marine biologist!"
    mc "So I can help save the endangered sea creatures.. maybe!"
    mc "As long as I have the sea with me… I think I can do it.."

    pause 1.5

    $ chapter5_done = True

    "{size=+8}{color=#06d6a0}{b}TRUE ENDING: ONE WITH THE SEA{/b}{/color}{/size}"

    $ MainMenu(confirm=False)()
    return

label ch5_ending_feral:

    show mc excited at mc_left
    with dissolve

    "My fingers trembled as i hold the fish in my hand."

    mc "I…I wish to finally become one with the sea!"

    leo "Yeeees~! Hehe great choice!"

    play sound "audio/mysterious_golden_looking.ogg"
    "The golden fish melts in my hands."

    show mc shock at mc_left
    mc "w-waugh-??"

    "Its golden scale fusing with my own skin in a grotesque way."
    "A surge of golden heat runs up my veins, rewiring my DNA in real time."

    play sound "audio/sfx/attack_2.mp3"
    show mc holdcry at mc_left with vpunch
    mc "it hurts.. it huuuurts..!! MAMAA..!!"

    "My vision starts to blur from the overwhelming pain of it all."
    "Once everything clears out.. I.. looked down to my hands to notice that I’ve.."
    "Been.. turned into a leopard seal."

    mc "A leopard seal..?"

    leo "what do ya thiiiink? A human as curious as you.."
    leo "of course you'd turn into a creature of the same trait~!"

    show mc happy at mc_left
    mc "I.. it feels.. Awesome..!!"
    mc "Hahah! I can finally swim! And and I’m so big and!"

    stop music fadeout 1.0
    play sound "audio/sfx/thump.mp3"
    with vpunch

    ban "{size=+6}{b}Foolish greedy mortals….!!{/b}{/size}"
    ban "Through countless tides have I awaited this moment."
    ban "Yet thou dost wield my patience as thy hollow pow'r!"
    ban "Not for kin, nor comrades dear - nay, for thy *selfish* gain..!?"

    leo "Well in my humble opinion-"

    ban "{size=+8}{b}SILENCE!{/b}{/size} No more of honeyed words shall pass thy lips!"
    ban "To darkest depths shalt thou be sent - let Neptune's wrath be swift!"
    ban "There in thy briny prison, 'midst the waves' cold embrace, May thy joy turn to anguish in thine self-wrought disgrace!"

    scene black
    with Dissolve(2.0)

    "And just like that.."
    "We were banished to the darkest depth of sea…"
    "I never got to see Mr. Cory again.. Nor Mr. Scyllarus.."
    "Is it so wrong to become a fish…?"

    pause 1.5

    $ chapter5_done = True

    "{size=+8}{color=#f72585}{b}ENDING: FERAL EMBRACE{/b}{/color}{/size}"

    $ MainMenu(confirm=False)()
    return
