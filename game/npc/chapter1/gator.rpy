label gator_interaction:

    scene ch1_night

    $ focus()
    show mc default:
        full
        right
    show gator default:
        full 
        center
    "An alligator lounging beside a large rock. It looked completely unbothered by anything that would be around it. One of its claws casually tapped against the rock."

    show mc happy:
        full
        right
        surprise
    mc "Hello! Good evening!"
    gator "Huh?"

    show gator surprised:
        full 
        center
    gator "Oh."

    show gator annoyed:
        full 
        center
    gator "A guppy."

    show mc default:
        full
        right
    mc "anyway ms gator I'm looking for a golden fish!"

    show gator surprised:
        full 
        center
    gator "wait ya can tell I'm a gator?"
    gator "Even down to the fact that I'm no male. Impressive."

    show gator annoyed:
        full 
        center
    gator "Most thought that I'm a.. ugh, {b}{i}{size=25}a croc...{/i}{/b}"

    show mc o:
        full
        right
    mc "mm it's pretty easy to tell an alligator and a crocodile apart.."
    show mc actually:
        full
        right
        surprise
    mc "{cps=40}alligators have a U shaped snout while crocodiles have it V shaped! also alligators only have their upper teeth visible when the jaw is closed, while crocodiles have them both shown!{/cps}"
    show mc happy:
        full
        right
    mc "as to how to tell the sex apart, it's the size and how slim you are"

    show gator smile:
        full 
        center
    gator "{bt=10}*whistle*{/bt} I like this guppy."
    gator "you were saying golden fish?"

    show mc default:
        full
        right
        surprise
    mc "Mhm! Suuuper shiny!"

    show gator default:
        full 
        center
    gator "Oh, THAT pretty thing."

    show mc excited:
        full
        right
        surprise
    mc "You know it!??"

    show gator surprised:
        full 
        center
    gator "Know it?"
    gator "Kid, half the river's been staring at the swimming gem."

    show gator default:
        full 
        center
    gator "Thing practically lights up the whole river."
    gator "I saw it zoom past me earlier."

    show mc o:
        full
        right
    mc "Which direction did it go?"
    gator "mm.. pretty sure North..."

    show mc happy:
        full
        right
        surprise
    mc "All leads road to north!"

    show cory side:
        full 
        leftish
    with moveinleft
    show gator default:
        full 
        centerright
    with move
    cory "ay.. i think ya got it mixed up there guppy"

    show gator default:
        full 
        centerright
    gator "shut up. They can think on their own."

    show gator smile:
        full 
        centerright
    gator "Right, guppy?"

    show cory upset:
        full 
        leftish
    cory "what did ya get so defensive for!"

    show gator default:
        full 
        centerright
    gator "just teaching you on how to babysit."

    show cory upset:
        full 
        leftish
        surprise
    cory "who's saying what about babysitting?! I'm just accompanying the little thing!"

    show gator annoyed:
        full 
        centerright
    gator "you just defined babysitting."

    cory "since when did you care so much for a guppy anyway?"
    cory "You always eat them for lunch, especially on Tuesdays."

    show mc o:
        full
        right
    mc "mm, it is Tuesday today..."

    show gator annoyed:
        full 
        centerright
        surprise
    gator "I could say the same to ya. Last time I seen you with a guppy it was when you were-"

    show cory disrespect:
        full 
        leftish
        surprise
    cory "LA LA LA CANT HEAR YA OVER THESE THIIICK FINS O' MINE"

    show gator upset:
        full 
        centerright
        vibrate
        ease 0.1 medlong
    gator "OH YOU SHUT YOUR MOUTH BOY I CAN EAT YOU RIGHT ABOUT NOW."
    show gator upset:
        full 
        center
        vibrate
        surprise
        ease 0.1 medlong
    gator "YOUR FOUL TASTE IS THE ONLY THING STOPPING ME."
    
    show cutchap5 with vibrate
    "I stare at both of them from the sidelines. Feeling a stiff electric tension swell between them as it goes on."
    $ focus()

    menu:

        "Don't stop them":
            hide cutchap5
            $ focus()
            show mc shock:
                full
                right   
            "I continue to stare as they exhaust themselves."

            show gator upset:
                full 
                centerright
                vibrate
            gator "you.. Motherfucker"

            show cory upset:
                full 
                leftish
                surprise
            cory "nasty NASTY gator..!"

            show mc o:
                full
                right
                surprise
            show cory surprise:
                full 
                leftish
            show gator surprised:
                full 
                centerright
            mc "what does a motherfucker mean? :o my parents said that thing a lot too.."

            show cory side:
                full 
                leftish
            cory "It means uhh... that you love your mother a lot!"

            show mc happy:
                full
                right
                surprise
            mc "ohh I love my mama! so I'm a motherfucker too! :D"

            show gator surprised:
                full 
                centerright
                surprise
            gator ".... No! Motherfucker means you HATE your mother's guts, guppy."

            show gator annoyed:
                full 
                center
            gator "don't listen to that fish"

            show mc shock:
                full
                right
                sink
            mc "ohh.. okay I'm not a motherfucker then :("

            show cory side close:
                full 
                leftish
            cory "ya know what truce on that."

            show gator default:
                full 
                centerright
            gator "Anyway."
            gator "You better run now."

            show mc o:
                full
                right
            mc "whah? why"

            show gator default:
                full 
                centerright
                surprise
            gator "Pretty thing like that doesn't stay a secret for long"
            gator "And once the whole water starts wanting the same thing..."
            show gator annoyed:
                full 
                centerright
            gator "Things get messy."

            show mc serious_hu:
                full
                right
                surprise
            mc "I'll be careful!"

            show gator smile:
                full 
                centerright
            gator "Good, I'd hate to hear some little guppy got swept away."

            show cory talk_hu:
                full 
                leftish
            cory "Don't worry gatha."
            cory "I've got an eye on him."

            show gator annoyed:
                full 
                centerright
                surprise
            gator "I don't trust you, you're bad at babysitting"

            show cory upset_hu:
                full 
                leftish
                surprise
            cory "no I'm not!"

            show mc happy:
                full
                right
                surprise
            mc "but Mr Cory is kind to me! I trust him!"

            show gator smile:
                full 
                centerright
                surprise
            gator "Ha! Go on then, little guppy."
            gator "Chase your shiny thing. Just don't let the river chase you back."

            show gator default:
                full 
                centerright
            gator "and if you got lost in the way?"
            show gator smile:
                full 
                centerright
                surprise
            gator "punch Cory in the face, I'll come running"

            show cory surprise:
                full 
                leftish
                surprise
            cory "ay!"

            show mc default:
                full
                right
                surprise
            mc "Okaay! Thank you!"

            $ focus()


        "Distract them":
            $ focus()
            hide cutchap5
            show mc sad:
                full
                right
                surprise
            show gator upset:
                full 
                centerright
            mc "i uhm.. Ms.. gator why did you not follow the golden fish when it's so shiny?"

            show gator surprised:
                full 
                centerright
            show cory surprise:
                full 
                leftish
            "At the sound of my voice they both turn to me with a realizing look on their face."

            show gator default:
                full 
                centerright
            gator "Because it was fast."

            show mc o:
                full
                right
            mc "Oh! :o"

            show cory disrespect:
                full 
                leftish
            cory ".... Heh"

            show gator annoyed:
                full 
                centerright
            gator "Don't give me that look."

            show mc o:
                full
                right
            mc "What look?"

            show gator default:
                full 
                centerright
            gator "The look."
            show gator annoyed:
                full 
                centerright
            gator "The 'wow, the big scary alligator is lost to a fish' look."

            show mc serious:
                full
                right
                surprise
            mc "I wasn't at all thinking that!"

            show cory smile:
                full 
                leftish
            cory "I was sure as eel thinking that"

            show gator annoyed:
                full 
                centerright
            gator "I definitely could've caught it if I wanted."

            show cory smile:
                full 
                leftish
            cory "Ya sure could."

            show gator annoyed:
                full 
                centerright
                vibrate
            gator "I COULD."

            show cory disrespect:
                full 
                leftish
            cory "mhm"

            show gator upset:
                full 
                centerright
                vibrate
            gator "oh I CAN."

            show cory smile_hu:
                full 
                leftish
                surprise
            cory "whatever you say scaled guppy."

            show gator annoyed:
                full 
                centerright
                vibrate
            gator "Oh fine you wanna go, punk?"
            gator "I'm getting to that fish first.."

            show gator upset:
                full 
                centerright
                vibrate
            gator "and eat im going to eat it right on your face"
            show gator annoyed:
                full 
                centerright
            gator "See how you'll like that"

            "With a face of determination and disdain Ms Gator left in a hurry. The current swirling in her wake."

            show mc shock:
                full
                right
                surprise
            mc "...."
            mc "Mr.. Cory.. alligators can actually swim up to thirty kilometers per hour"
            show mc shock:
                full
                right
                sink
            mc "which is.. faster than both of us combined.."

            show cory surprise:
                full 
                leftish
                surprise
            cory "they can WHAT."
            cory "sweet mother of kraken.."
            show cory surprise:
                full 
                toleft
                walkto(offscreenleft,10,2,3,5)
            cory "WE SPRINTING GUPPY COME ON!"

            $ focus()

    $ add_clue("All leads point north.")

    return