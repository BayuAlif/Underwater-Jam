# =========================================================
# MANTIS SHRIMP WARNING
# =========================================================

screen mantis_warning():

    modal True

    text "If you interact with the shrimp, you can't go back to get item unless you had a save. Proceed to continue?":
        xalign 0.5
        yalign 0.42
        text_align 0.5

    textbutton "Yes, confront the Mantis Shrimp.":
        xalign 0.5
        yalign 0.55
        action Return(True)

    textbutton "Not yet..":
        xalign 0.5
        yalign 0.62
        action Return(False)


# =========================================================
# CHAPTER 2 MAIN FLOW & HUB
# =========================================================

label chapter2:

    # =================================
    # DAY SETUP
    # =================================

    $ set_cycle("day")
    $ load_area("border")

    $ set_background(
        "images/backgrounds/chapter 2/bg day2.jpg",
        "images/backgrounds/chapter 2/bg night2.jpg"
    )

    $ set_dialogue_background(
        "images/backgrounds/chapter 2/bg day2_bordered.jpg",
        "images/backgrounds/chapter 2/bg night2_bordered.jpg"
    )

    scene expression get_background()

    call chapter2_opening

    jump chapter2_hub


# =========================================================
# CHAPTER 2 OPENING
# =========================================================

label chapter2_opening:

    scene expression get_dialogue_background()

    "===== CHAPTER 2 ====="

    "The river flowed faster, slowly giving way to larger stones."

    "The sunlight above grew softer, hiding themself behind layers of drifting water plants."

    show mc o at mc_pos
    show cory netral at cory_pos

    mc "Have you been to the sea mr. Cory?"

    show cory smile_hu at cory_pos

    cory "Sea? Nah that's waaay past my territory"
    cory "Nearest I've been at is meters before saltwater and freshwater collides"
    cory "Besides, I'm a freshwater fish guppy, one step into sea, and I explode"

    show mc shock at mc_pos

    mc "EXPLODE?? NOOO MR CORY PLEASE DONT EXPLODE!! I LEFT MY GLUE AT HOME D:"

    show cory smile at cory_pos

    cory "Ay easy, easy! I won't be exploding now..!"

    show cory side at cory_pos

    cory "Ah but.. that woulda mean we have to part ways-"

    show mc o at mc_pos

    mc "Woah look ahead! that's a lotta shoal!"

    show cory netral at cory_pos

    cory "Huh..?"

    "Several tens of fishes crowd at what looks like a border built out of tall reefs, a small cave sits in the middle where a speckle of colorful creature stands firm guarding the entrance."

    show cory netral_hu at cory_pos

    cory "That's the border of salt fresh.."
    cory "Itsa always been a busy place but this amount is unnatural..."

    show mc o at mc_pos

    mc "Is that a shrimp guarding the cave hole?"

    "I squint my eyes into thin lines to take a better look on the eccentric colored guardian right before the cave's entrance"

    show mc excited at mc_pos

    mc "Oh oh! That's a mantis shrimp!! He looks really though!"

    show mc excited at mc_pos

    mc "Mr cory can we give it a handshake? :D"

    show cory unimpressed2 at cory_pos

    cory "Nuh uh! unless you want your hand gone for good"
    cory "But eh, that mantis shrimp.. He had been around for a good while"
    cory "He's quite friendly, it's hard to believe if the fuss is his doing."

    show mc o at mc_pos

    mc "really?! You know him?"

    show cory netral_hu at cory_pos

    cory "Yeah, But I say we ask around first to know what the crowd's about.."

    show mc happy at mc_pos

    mc "Sir yes sir mr cory!"

    show cory fond at cory_pos

    cory "Heh, atta fish"

    hide mc
    hide cory

    scene expression get_background()

    return


# =========================================================
# CHAPTER 2 HUB
# DAY + NIGHT
# =========================================================

label chapter2_hub:

    scene expression get_background()

    call screen chapter2_interaction

    $ hub_choice = _return

    # =====================================================
    # DAY - SALMON
    # =====================================================

    if hub_choice == "salmon":

        call interact_with_npc("salmon")

        $ salmon_talked = True

        jump chapter2_hub

    # =====================================================
    # DAY - AROWANA
    # =====================================================

    elif hub_choice == "arowana":

        call interact_with_npc("arowana")

        $ wana_talked = True

        jump chapter2_hub

    # =====================================================
    # DAY - TINY KRILL
    # =====================================================

    elif hub_choice == "tiny_krill":

        if not tiny_krill_taken:

            $ add_item("tiny_krill")
            $ tiny_krill_taken = True

            scene expression get_dialogue_background()

            show mc happy at mc_pos

            mc "A tiny krill!"

            "Eah!"

            show cory disrespectful at cory_pos

            cory "Heh.. you could say it's.. One in a krillion"

            "Your joke sucks ass!"

            show cory unimpressed at cory_pos

            cory "...."
            cory "... I say we feed that thing to a fish, guppy"

            show mc shock at mc_pos

            mc "Aw shucks, do we really have to krill it mr cory? :("

            "Suffer in eternal torment both of you!"

            "I obtained a tiny krill"

            hide mc
            hide cory

            scene expression get_background()

        jump chapter2_hub

    # =====================================================
    # DAY -> NIGHT
    # =====================================================

    elif hub_choice == "continue_chapter2_day":

        $ change_cycle()

        scene expression get_dialogue_background()

        "The crowd at the gate slowly thinned as daylight began to fade."

        show mc o at mc_pos
        show cory side at cory_pos

        mc "Mr. Cory, it's getting dark already.."

        show cory netral at cory_pos

        cory "Border's always like this come nightfall."
        cory "Fishes settle down, but that shrimp never budges."

        show mc excited at mc_pos

        mc "Then it's the perfect time to figure him out!"

        show cory smile at cory_pos

        cory "Heh, that's the spirit."
        cory "Let's see what the dark's got in store for us."

        hide mc
        hide cory

        scene expression get_background()

        jump chapter2_hub

    # =====================================================
    # NIGHT - COAL TAR
    # =====================================================

    elif hub_choice == "coal_tar":

        if not coal_tar_taken:

            $ add_item("coal_tar")
            $ coal_tar_taken = True

            call chapter2_coal_tar_pickup

        jump chapter2_hub

    # =====================================================
    # NIGHT - GHOST FISH
    # =====================================================

    elif hub_choice == "ghostfish":

        call interact_with_npc("ghostfish")

        $ ghost_talked = True

        jump chapter2_hub

    # =====================================================
    # NIGHT - MANTIS SHRIMP
    # =====================================================

    elif hub_choice == "mantis_shrimp":

        call screen mantis_warning

        if _return:
            call mantis_shrimp

            # mantis_shrimp now always returns to this point (win,
            # or lose -> "Return to Hub"). duel_result tells us which
            # one just happened, since it's set by rps_best_of_three()
            # every time a duel finishes ("player_win" on a win, "ko"
            # on a loss) and mantis_shrimp.rpy already relies on this
            # same variable to route "player_win" to rps_check_winner.
            if duel_result == "player_win":
                call chapter2_night_ending
                return

            jump chapter2_hub

        jump chapter2_hub


# =========================================================
# CHAPTER 2 NIGHT ENDING
# =========================================================

label chapter2_coal_tar_pickup:

    scene expression get_dialogue_background()

    # MC
    show mc o at mc_pos
    hide cory

    mc "Mr. Cory, do you know what this black lump is?"

    # CORY
    hide mc
    show cory netral_hu at cory_pos

    cory "Mmmn.. no clue."

    show cory unimpressed2 at cory_pos

    cory "Almost looks like poo to me, you better drop that thing guppy."

    # MC
    hide cory
    show mc shock at mc_pos

    mc "Yuck! it smells... weird."

    # GHOST
    show ghost deadpan at ghost_pos

    "???" "You shouldn't be carrying things you don't understand."

    # CORY
    hide ghost
    show cory smile_hu at cory_pos

    cory "Yeah.. that's right guppy.."
    cory "Finally, Some self preservation in ya!"

    # MC
    hide cory
    show mc o at mc_pos

    mc "That.. wasn't me..."

    "The water around us suddenly grows eerily still."

    "Faint glow pair of eyes emerges from the darkness."

    # CORY
    hide mc
    show cory surprise at cory_pos

    cory "GYAAAAAAA-"

    "Mr Cory jumped and immediate cower behind my back with a loud screech"

    # MC
    hide cory
    show mc o at mc_pos

    mc ":0"

    show mc excited at mc_pos

    mc "Woah! What are you?"

    # GHOST
    show ghost default at ghost_pos

    ghost "A fish."

    # MC
    hide ghost
    show mc pout at mc_pos

    mc "I can see that."

    # GHOST
    show ghost default at ghost_pos

    ghost "Then you needn't know more."

    # MC
    show mc o at mc_pos

    mc "Why are you here... fish?"

    # GHOST
    show ghost side at ghost_pos

    ghost "You were meant to find me."

    show ghost close at ghost_pos

    ghost "But this second is not the time"
    ghost "We shall meet again.. very soon."

    show ghost side at ghost_pos

    ghost "Or perhaps.. we have met before."

    # MC
    hide ghost
    show mc happy at mc_pos

    mc "Okay! Looking forward to meeting you again, fish!"
    mc "Mr Cory you can come out, it's fine now."

    # CORY
    hide mc
    show cory upset at cory_pos

    cory "What the eel even was that?!"
    cory "Straight out of deep sea I swear!"

    "I obtained: a mysterious stinky black lump"

    hide mc
    hide cory
    hide ghost

    scene expression get_background()

    return


# =========================================================
# CHAPTER 2 NIGHT ENDING
# =========================================================

label chapter2_night_ending:

    scene expression get_dialogue_background()

    show mc happy at mc_pos
    show shrimp default at shrimp_pos

    mc "onward! to the sea we go!"

    shrimp "to the sea!"

    hide shrimp
    show cory side at cory_pos

    cory "..."

    show cory sideclose at cory_pos

    cory "......"

    show cory fond at cory_pos

    cory "imp.. I leave the guppy's safety to ya alright?"

    show cory smile_hu at cory_pos

    cory "Shrimps have better resistance in freshwater don't they?"

    if has_item("saltwater_device") or wana_talked:

        cory "And we only have one 50%% effective saltwater device.."

    show mc shock at mc_pos

    mc "...!!"

    hide cory
    show shrimp default at shrimp_pos
    shrimp "yes of course! Protect i shall. it is my utmost duty to protect!"

    show mc pout at mc_pos

    mc "no!"

    hide shrimp
    show cory smile_hu at cory_pos
    cory "guppy.."

    mc "no no no! I'm not going anywhere without Mr. Cory!!"

    cory "guppy, I'd dry the sea to come along but-"

    mc "mr shrimp cant you protect him? With your punches!"
    mc "punch all the freshwater away from mr.cory!"

    hide cory
    show shrimp default at shrimp_pos
    shrimp "..."
    shrimp "I'm afraid I cannot, my dear comrade!"
    shrimp "punching water is akin to fighting a shadow..."

    mc "no.."
    mc "but you promised..."
    mc "that we'd catch that fish together...."

    hide shrimp
    show cory side at cory_pos

    cory "....."
    cory "I'm.. God terribly. sorry guppy.."
    cory "I didn't think far enough that it'd reach the sea.."
    cory "...I'm afraid that I'm a fraud..."

    hide cory
    show shrimp default at shrimp_pos
    shrimp "that makes a good rhyme!"

    "The fish scale in my bag suddenly glows into a blinding sparkly light for one second. Painting the three of us in gold, before it dims once more. But something felt different"

    show mc o at mc_pos

    mc "mm?"

    hide shrimp
    show cory surprise at cory_pos

    cory "I-! Huh? I feel different!"

    mc "Try stepping in the saltwater, Mr.Cory!"

    cory "Are ya sure..? What if it's just my imagination?"

    mc "trust me!"

    cory "Alright..."

    "Mr Cory hesitantly takes one step into where freshwater and saltwater collide with one eye closed."

    show cory proud at cory_pos

    cory "Holy mother of sea...!"

    mc "d-does it hurt-"

    "Before I can finish my line I was swept into a spinning hug"

    cory "I CAN'T BELIEVE IT!! I'M IN SALTWATER GUPPY!!"

    show mc excited at mc_pos

    mc "YAAAAAY"

    "Mr shrimp then lifts the both of us with its strong claws spinning us all into a dizzying spiral"

    hide cory
    show shrimp smile at shrimp_pos

    shrimp "KAKAKA! WAHOO!"

    hide shrimp
    show cory shock at cory_pos

    cory "THAT'S WAY TOO FAAAUUUAASHHTT SHRIMP PUT US DOOOOWN"

    show mc dizzy at mc_pos

    mc "YIPEEEEE FAAASTEEER!!"

    hide cory
    show shrimp smile at shrimp_pos
    shrimp "Ah! My apologies, comrades! And congratulations to Mr. Cory!"

    "Mr shimp then carefully puf us down"

    shrimp "With this, we can now safely travel amongst the seas! KAKAKA!"

    hide shrimp
    show cory shock at cory_pos
    cory "ngnuuurhhhehhkk"

    mc "oaooaooouhh yaaaah lets meef the... crustashan empeees.."

    hide cory
    show shrimp smile at shrimp_pos
    shrimp "Don't worry, my dizzy lieges! I'll carry the both of you until you regain your ground! Or.. your water!"

    "===== END OF CHAPTER 2 ====="

    hide mc
    hide cory
    hide shrimp

    scene black with dissolve

    jump chapter3