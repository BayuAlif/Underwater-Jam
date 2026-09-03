# =====================================
# NPC 4 - ALIGATOR
# =====================================

label fish04:

    $ cory_at_right = False

    show mc default at mc_pos

    "An alligator lounging beside a large rock. It looked completely unbothered by anything that would be around it. One of its claws casually tapped against the rock."

    show gator default at gator_pos

    "The alligator slowly turned its head toward me."

    gator "Huh?"

    gator "Oh."

    show gator annoyed at gator_pos

    gator "A guppy."

    show mc happy at mc_pos

    mc "anyway ms gator I’m looking for a golden fish!"

    show gator surprised at gator_pos

    gator "wait ya can tell I'm a gator?"

    gator "Even down to the fact that I'm no male. Impressive."

    show gator annoyed at gator_pos

    gator "Most thought that I'm a.. ugh, a croc."

    show mc o at mc_pos

    mc "mm it's pretty easy to tell an alligator and a crocodile apart.."

    show mc actual at mc_pos

    mc "alligators have a U shaped snout while crocodiles have it V shaped!"

    mc "also alligators only have their upper teeth visible when the jaw is closed, while crocodiles have them both shown!"

    mc "as to how to tell the sex apart, it's the size and how slim you are"

    show gator smile at gator_pos

    gator "*whistle* I like this guppy."

    gator "you were saying golden fish?"

    show mc default at mc_pos

    mc "Mhm! Suuuper shiny!"

    show gator default at gator_pos

    gator "Oh, THAT pretty thing."

    show mc o at mc_pos

    mc "You know it!??"

    show gator surprised at gator_pos

    gator "Know it?"

    gator "Kid, half the river’s been staring at the swimming gem."

    gator "Thing practically lights up the whole river."

    show gator default at gator_pos

    gator "I saw it zoom past me earlier."

    mc "Which direction did it go?"

    gator "mm.. pretty sure North…"

    show mc happy at mc_pos

    mc "All leads road to north!"


    # =====================================
    # CORY MASUK - CORY DI KANAN
    # MC DIHIDE
    # =====================================

    $ cory_at_right = True
    hide mc
    show cory side at cory_right_pos

    cory "ay.. i think ya got it mixed up there guppy"

    show gator default at gator_pos

    gator "shut up. They can think on their own"

    show gator smile at gator_pos

    gator "Right, guppy?"

    show cory upset at cory_right_pos

    cory "what did ya get so defensive for!"

    show gator default at gator_pos

    gator "just teaching you on how to babysit."

    show cory upset at cory_right_pos

    cory "who's saying what about babysitting?! I'm just accompanying the little thing!"

    show gator annoyed at gator_pos

    gator "you just defined babysitting."

    cory "since when did you care so much for a guppy anyway?"

    cory "You always eat them for lunch, especially on Tuesdays."


    # =====================================
    # MC MENYELA - CORY DIHIDE
    # =====================================

    $ cory_at_right = False
    hide cory
    show mc o at mc_pos

    mc "mm, it is Tuesday today…"


    # =====================================
    # CORY KEMBALI - MC DIHIDE
    # =====================================

    $ cory_at_right = True
    hide mc
    show cory disrespectful at cory_right_pos

    gator "I could say the same to ya. Last time I seen you with a guppy it was when you were-"

    cory "LA LA LA CANT HEAR YA OVER THESE THIIICK FINS O’ MINE"

    show gator upset at gator_pos

    gator "OH YOU SHUT YOUR MOUTH BOY I CAN EAT YOU RIGHT ABOUT NOW."

    gator "YOUR FOUL TASTE IS THE ONLY THING STOPPING ME."

    "I stare at both of them from the sidelines. Feeling a stiff electric tension swells between them as it goes on. It was like watching mama and papa speak to each other. Maybe I should try stopping them.."


    # =====================================
    # MENU
    # =====================================

    menu:

        "Don't stop them":

            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc shock at mc_pos

            "I continue to stare as they exhaust themselves"

            show gator upset at gator_pos

            gator "you.. Motherfucker"

            show mc o at mc_pos

            mc "..."


            # ---------------------------------
            # CORY
            # ---------------------------------

            $ cory_at_right = True
            hide mc
            show cory upset at cory_right_pos

            cory "nasty NASTY gator..!"


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc o at mc_pos

            mc "what does a motherfucker mean? :o my parents said that thing a lot too.."

            show mc shock at mc_pos


            # ---------------------------------
            # CORY
            # ---------------------------------
            # FIX:
            # MC harus di-hide sebelum Cory bicara.

            $ cory_at_right = True
            hide mc
            show cory upset at cory_right_pos

            cory "....."

            show gator surprised at gator_pos

            gator "......."


            # ---------------------------------
            # CORY
            # ---------------------------------

            show cory side at cory_right_pos

            cory "it means uhh-!"

            show cory smile_hu at cory_right_pos

            cory "Means that you love your mother a lot!"


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc happy at mc_pos

            mc "ohh I love my mama! so I'm a motherfucker too! :D"

            show gator annoyed at gator_pos

            gator ".... No! Motherfucker means you HATE your mother, guppy."

            gator "don't listen to that fish"

            show mc shock at mc_pos

            mc "ohh.. okay I'm not a motherfucker then :("


            # ---------------------------------
            # CORY
            # ---------------------------------

            $ cory_at_right = True
            hide mc
            show cory talk at cory_right_pos

            cory "ya know what truce on that."

            show gator default at gator_pos

            gator "Anyway."


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc default at mc_pos

            gator "You better run now"

            gator "Everyone’s chasing it."

            show mc o at mc_pos

            mc "Everyone?"

            gator "Mhm, all creatures on water. Perhaps on land too like you are."

            gator "Pretty thing like that doesn’t stay a secret for long"

            gator "And once the whole water starts wanting the same thing…"

            show gator annoyed at gator_pos

            gator "Things get messy."

            show mc default at mc_pos

            mc "I’ll be careful!"

            show gator smile at gator_pos

            gator "Good, I’d hate to hear some little guppy got swept away."


            # ---------------------------------
            # CORY
            # ---------------------------------

            $ cory_at_right = True
            hide mc
            show cory netral_hu at cory_right_pos

            cory "Don’t worry gatha."

            cory "I’ve got an eye on him."

            show gator annoyed at gator_pos

            gator "I don't trust you, you're bad at babysitting"

            show cory upset at cory_right_pos

            cory "no I'm not!"


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc happy at mc_pos

            mc "but Mr Cory is kind to me! I trust him!"

            show gator smile at gator_pos

            gator "Ha!"

            gator "Go on then, little guppy."

            gator "Chase your shiny thing."

            gator "Just don’t let the river chase you back."

            gator "and if you got lost in the way?"

            gator "punch Cory in the face, I'll come running"


            # ---------------------------------
            # CORY
            # ---------------------------------

            $ cory_at_right = True
            hide mc
            show cory surprise at cory_right_pos

            cory "ay!"


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc default at mc_pos

            mc "Okay! Thank you!"


        # =====================================
        # DISTRACT THEM
        # =====================================

        "Distract them":

            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc shock at mc_pos

            mc "i uhm.. Ms.. gator why did you not follow the golden fish when it's so shiny?"

            show gator surprised at gator_pos

            "At the sound of my voice they both turn to me with a realizing look on their face. Distancing from one another with a firm ehem."

            show gator default at gator_pos

            gator "Because it was fast."

            show mc o at mc_pos

            mc "Oh! :o"


            # ---------------------------------
            # CORY
            # ---------------------------------

            $ cory_at_right = True
            hide mc
            show cory disrespectful at cory_right_pos

            cory ".... Heh"

            show gator default at gator_pos

            gator "..."

            show gator annoyed at gator_pos

            gator "Don’t give me that look."


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc o at mc_pos

            mc "What look?"

            gator "The look."

            gator "The ‘wow, the big scary alligator is lost to a fish’ look."

            show mc shock at mc_pos

            mc "I wasn’t at all thinking that!"


            # ---------------------------------
            # CORY
            # ---------------------------------

            $ cory_at_right = True
            hide mc
            show cory smile at cory_right_pos

            cory "I was sure as eel thinking that"

            show gator default at gator_pos

            gator "I definitely could’ve caught it if I wanted."

            show cory smile_hu at cory_right_pos

            cory "Ya sure could."

            show gator annoyed at gator_pos

            gator "I COULD."

            show cory disrespectful at cory_right_pos

            cory "mhm"

            show gator upset at gator_pos

            gator "oh I CAN."

            cory "whatever you say guppy."


            # ---------------------------------
            # MC
            # ---------------------------------

            $ cory_at_right = False
            hide cory
            show mc shock at mc_pos

            "I heard a loud snap from miss Gator’s direction"

            show gator annoyed at gator_pos

            gator "Oh fine you wanna go, punk?"

            gator "I'm getting to that fish first.."

            show gator upset at gator_pos

            gator "and eat im going to eat it right on your face"

            show gator smile at gator_pos

            gator "See how you'll like that"

            hide gator

            "With a face of determination and disdain Ms gator left in a hurry. The current swirling in her wake."


            # =====================================
            # GATOR LEAVES
            # MC + CORY NORMAL POSITION
            # =====================================

            $ cory_at_right = False
            show cory side at cory_pos
            show mc shock at mc_pos

            mc "...."

            mc "Mr.. Cory.. alligators can actually swim up to thirty kilometers per hour"

            mc "which is.. faster than both of us combined.."

            show cory surprise at cory_pos

            cory "they can WHAT."

            cory "sweet mother of kraken.."

            cory "WE SPRINTING GUPPY COME ON!"


    # =====================================
    # CLEANUP
    # =====================================

    $ cory_at_right = False

    hide mc
    hide gator
    hide cory

    return