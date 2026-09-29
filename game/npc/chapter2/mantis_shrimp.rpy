label mantis_interaction:
    hide mc
    hide cory
    scene ch2_night with dissolve
    $ focus()

    "The night settles in heavy, and so does the overbearing crowd dying to just quiet murmurs of protests"
    "Two pairs of eyes peek from behind a flock of corals. Analyzing the situation at hand carefully"

    show cory talk:
        full
        unpose
        offscreenleft
    show cory talk:
        leftish
    with moveinleft

    show mc serious:
        full
        unpose
        offscreenright
    show mc serious:
        right
    with moveinright

    cory "This is our best chance, guppy.."
    mc "mm! We strike now!"

    "With a deep inhale I jumped out the coral while Mr.Cory trails behind slowly, we walked over to where the shrimp still stood its ground as straight as he was in the morning. Though he didn’t immediately notice me."

    show mc happy:
        full
        right
        jump
    with move
    mc "Good evening.. Mr shrimp!"

    show shrimp surprise:
        full
        center
        surprise
    with moveinright
    shrimp "Huh?! A little kid?!"

    show shrimp default:
        full
        center
    shrimp "Go back to your parents!"
    shrimp "Using a young guppy won’t make me go soft on you!"

    show shrimp default_om:
        full
        center
    shrimp "I will still punch you if you lose!"

    "Oh to be punched by a mantis shrimp.. I wonder how much powerful it will feel than my friend’s at school"

    show cory smile:
        full
        trio_left
    with move
    show shrimp default:
        trio_center_mantis
        toleft
    with move
    show mc happy:
        full
        trio_right
    with move
    cory "oooh.. That’s not very nice… you can’t be saying young fish…"

    show shrimp surprise:
        trio_center_mantis
        toleft
        surprise
    shrimp "and who are you!!"

    show cory smile:
        full
        trio_left
    cory "I’m the young guppy’s guardian…"

    show shrimp sepet:
        trio_center_mantis
        toleft
    shrimp "I’m still not letting an elderly and a young guppy pass!"
    shrimp "Especially the elder…. Squints"

    show shrimp default_om:
        trio_center_mantis
        toleft
    shrimp "You have to prove yourself worthy through a duel!"
    shrimp "Only then I shall let you pass!"

    hide mc
    hide cory
    hide shrimp
    with dissolve

    call screen choose_interactor(
        "Choose who should confront Mr. Shrimp!",
        "The approach and answers may vary based on the character"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump mantis_as_mc

    jump mantis_as_cory

label mantis_as_mc:

    $ duel_fighter = "mc"
    $ focus()

    hide cory with dissolve
    show shrimp default:
        duo_left_mantis
    show mc default:
        full
        duo_right
    with dissolve

    menu:

        "Ask why he’s guarding the gate":
            $ focus()
            show mc o:
                full
                duo_right
            show shrimp default:
                duo_left_mantis
            mc "mm.. say mr shrimp.. why do you guard the gate so strictly…?"

            shrimp "Because I was told to!"

            show mc o:
                full
                duo_right
            mc "told to..? By who?"

            show shrimp proud:
                duo_left_mantis
                surprise
            shrimp "The great empress I owe my life to!"
            shrimp "She saved me in my lowest moment in life.."

            show shrimp laugh:
                duo_left_mantis
                jump
            shrimp "And in exchange I devote my life to her compelling regime!"

            show mc dizzy:
                full
                duo_right
            mc "regime..? What’s a regime :o"

            show shrimp default:
                duo_left_mantis
            shrimp "a regime is some sort of propaganda! Maybe!"

            show shrimp shy:
                duo_left_mantis
            shrimp "I’m not too good with politics either so I wouldn’t know!"

            show mc pout:
                full
                duo_right
                sink
            mc "blehh you’re right politics suck.. All the grown ups are so invested in it"
            mc "Is it so hard for everyone to just be friends, hold hands and help each other? :("

            show shrimp default:
                duo_left_mantis
            shrimp "but it’s hard to hold hands when you’ve got big claws this strong!"
            shrimp "It’d always hurt someone that’s a different species!"

            show shrimp shy:
                duo_left_mantis
            shrimp "No matter how hard you try to be gentle."

            show mc o:
                full
                duo_right
            mc "..."

            menu:

                "asks to touch his arm":
                    $ focus()
                    show mc o:
                        full
                        duo_right
                    mc "mr shrimp.."

                    show mc excited:
                        full
                        duo_right
                        surprise
                    mc "what if i were to hypothetically ask to…"
                    mc "touch your claws..?"

                    show shrimp surprise:
                        duo_left_mantis
                        surprise
                    shrimp "No!"

                    show mc pout:
                        full
                        duo_right
                    mc "huh? Why not..?"

                    show shrimp default_om:
                        duo_left_mantis
                    shrimp "Because it will hurt your tiny hands!"

                    show mc pout:
                        full
                        duo_right
                    mc "but you said you won’t hesitate to punch me in a duel.."

                    show mc o:
                        full
                        duo_right
                    mc "why are you worried now Mr.shrimp?"

                    show shrimp default:
                        duo_left_mantis
                    shrimp "... that’s different! This is a no duel context!"

                    show shrimp default_om:
                        duo_left_mantis
                    shrimp "I would minimize as much damage as possible!"

                    show mc happy:
                        full
                        duo_right
                    mc "But it’s okay Mr.shrimp, I don’t mind pain!"

                    show shrimp surprise:
                        duo_left_mantis
                        surprise
                    shrimp "huh…?"

                    show mc default:
                        full
                        duo_right
                    mc "Some pain is worth it for the sake of knowledge."
                    mc "And also for the sake of easing other people’s pain.."

                    shrimp "You’re saying you’d hurt yourself just to feel my claws...?!"

                    show mc excited:
                        full
                        duo_right
                        surprise
                    mc "I’ve never met a mantis shrimp before!"
                    mc "So it made me suuuper curious on how your claws work!"

                    show shrimp sepet:
                        duo_left_mantis
                    shrimp "... hmph. Fine then touch you shall!"

                    show shrimp default_om:
                        duo_left_mantis
                    shrimp "But don’t come crying if you scrape yourself!"

                    show mc pout:
                        full
                        duo_right
                    mc "im a good guppy! Good guppies don’t cry!"

                    "Quenching curiosity, I started with poking its left claw with a finger repeatedly, assessing. With each poke, my finger easily bends under the rigid calloused textured shell. I can tell the mechanism that lies beneath the hard surface is very advanced just by the feel of it. Would one punch of it really instant kill me?"

                    show mc excited:
                        full
                        duo_right
                        jump
                    mc "ooo..! So THIS is what a 150-kilo punch feels like..!"

                    show shrimp proud:
                        duo_left_mantis
                        surprise
                    shrimp "How’s it?! Fastest moving claws in all of animal kingdom!"

                    show shrimp laugh:
                        duo_left_mantis
                        jump
                    shrimp "Grace upon the excellent anatomy of a mantis shrimp! kakaka!"

                    "Mr. shrimp puffs up like a peacock the more I shower it with giddy attention. Soon enough he would break into all kinds of different poses to showboat his cool anatomy more. His flexed sturdy shells sparkle under the dim scale’s light. I can only squeak in delight as this happens."

                    jump mantis_mc_duel_convo

                "asks for a duel":

                    jump mantis_mc_duel_convo

        "oh no, I’m not here for a duel!" if has_item("coal_tar"):
            $ focus()
            show mc happy:
                full
                duo_right
            mc "I’m here to offer you snacks.. You seem veeery tired.."

            show shrimp surprise:
                duo_left_mantis
                surprise
            shrimp "Huh…!"
            shrimp "Wait me? TIRED? Tiredness can’t affect a warrior!"

            show shrimp proud:
                duo_left_mantis
            shrimp "But I won’t say no to delicious looking delicacies"

            "Without second guessing, Mr.shrimp took about three clams, breaking the shell with his punch before stuffing it into his mouth enthusiastically. I watched the interesting process with rapt attention.. I’ve never seen a mantis shrimp eat before…"

            show shrimp default:
                duo_left_mantis
            shrimp "mm? What is it! Why are you staring!"

            show shrimp default_om:
                duo_left_mantis
            shrimp "Staring won’t make me share a thing with you!"

            show mc default:
                full
                duo_right
            mc "ah nonono am not hungry… *stomach growls*"

            show shrimp surprise:
                duo_left_mantis
                surprise
            shrimp "...."

            show shrimp sepet:
                duo_left_mantis
            shrimp "Let’s hypothetically say, I shared one clam!"

            show shrimp shy:
                duo_left_mantis
            shrimp "Would you eat it?!"

            show mc o:
                full
                duo_right
                surprise
            mc "...!"

            show mc happy:
                full
                duo_right
            mc "hehe don’t worry you can have all of it, mr shrimp"
            mc "you look like you need it more"

            show shrimp surprise:
                duo_left_mantis
                surprise
            shrimp "I never said that I WOULD share it with you!"

            show shrimp default_om:
                duo_left_mantis
            shrimp "That was a merely hypothetical!"

            show shrimp shy:
                duo_left_mantis
            shrimp "Don’t get too into yourself now!"

            "Mr. Shrimp ate enough coal tar for it to take effect."
            $ coal_tar_effective = True
            $ remove_item("coal_tar")

            menu:

                "Is clam your favorite food?":
                    $ focus()
                    show mc o:
                        full
                        duo_right
                    show shrimp default:
                        duo_left_mantis
                    shrimp "maybe!"

                    show mc happy:
                        full
                        duo_right
                    mc "mm you seem starving.."

                    show shrimp surprise:
                        duo_left_mantis
                        surprise
                    shrimp "Starving?! A mantis shrimp is able to not eat anything for weeks without hunger!"

                    show mc o:
                        full
                        duo_right
                    mc "and when’s the last time you eat?"

                    show shrimp default_om:
                        duo_left_mantis
                    shrimp "I don’t keep count!"

                    show shrimp smile:
                        duo_left_mantis
                    shrimp "Though I must say these are oddly rich tasted clams! Very scrumptious!"
                    shrimp "What did you put in them?!"

                    show mc shock:
                        full
                        duo_right
                        surprise
                    mc "ah that's.."
                    mc "mmn it's a secret ingredient I can't tell you!"

                    show mc happy:
                        full
                        duo_right
                    mc "unless you let me pass then maybe I'll tell.."

                    show shrimp surprise:
                        duo_left_mantis
                        surprise
                    shrimp "guh…!!"

                    show shrimp shy:
                        duo_left_mantis
                    shrimp "O-okay.. fine. pass you shall!"

                    show mc excited:
                        full
                        duo_right
                        jump
                    mc "Really?!"

                    show shrimp surprise:
                        duo_left_mantis
                        jump
                        vibrate
                    shrimp "WAIT WAIT WAIT! NO! PASS YOU SHALL NOT!"

                    show shrimp sepet:
                        duo_left_mantis
                        vibrate
                    shrimp "bad! bad Scyllarus! You can't let good food cloud your judgement!"
                    shrimp "even when said food.. reminds you of your mother’s cooking…"

                    show mc o:
                        full
                        duo_right
                    mc "mm.. but i say your mother’s cooking is worth fighting for!"

                    show mc happy:
                        full
                        duo_right
                    mc "sometimes it’s the reason to keep going for another day and the next!"

                    show shrimp default:
                        duo_left_mantis
                    shrimp ".... you might be right!"

                    show shrimp smile:
                        duo_left_mantis
                    shrimp "My mother’s food always gave me a calming effect!"
                    shrimp "One that would make you rest easier!"

                    show mc shock:
                        full
                        duo_right
                    "Was tiny mr shrimp so active that his mother had to feed him coal tar to make him less energized..?"

                    show shrimp laugh:
                        duo_left_mantis
                        jump
                    shrimp "So, I must thank you for the food and the memories!"

                    show shrimp default:
                        duo_left_mantis
                    shrimp "I’m still not letting you pass though!"

                    show shrimp shy:
                        duo_left_mantis
                    shrimp "{size=20}Please bring me more of it…{/size}"

                    jump mantis_mc_duel_convo_2

                "asks for a duel":

                    jump mantis_mc_duel_convo_2

label mantis_mc_duel_convo:
    $ focus()
    show mc shock:
        full
        duo_right
    mc "Mr. shrimp.. Is winning a duel the only way to pass the gate..?"

    show shrimp default:
        duo_left_mantis
    shrimp "I’m afraid, yes little guppy!"

    show shrimp default_om:
        duo_left_mantis
    shrimp "You have to prove yourself worthy of the sea!"
    shrimp "The beauty of it is not for the weak!"

    show mc excited:
        full
        duo_right
        jump
    mc "it leaves me no choice then.. bring it on!"

    show shrimp laugh:
        duo_left_mantis
        jump
    shrimp "Kakaka! That’s the spirit"
    jump mantis_pre_duel

label mantis_mc_duel_convo_2:
    $ focus()
    show mc shock:
        full
        duo_right
    mc "Mr. shrimp.. Is winning a duel the only way to pass the gate..?"

    show shrimp default:
        duo_left_mantis
    shrimp "I’m afraid, yes little guppy!"

    show shrimp default_om:
        duo_left_mantis
    shrimp "You have to prove yourself worthy of the sea!"
    shrimp "The beauty of it is not for the weak!"

    show mc excited:
        full
        duo_right
        jump
    mc "it leaves me no choice then.. bring it on!"

    show shrimp laugh:
        duo_left_mantis
        jump
    shrimp "Kakaka! That’s the spirit"
    jump mantis_pre_duel

label mantis_as_cory:
    $ focus()
    hide mc with dissolve

    show cory anon:
        full
        unpose
        offscreenleft
    show cory anon:
        duo_left
    with moveinleft

    show shrimp default:
        duo_right_mantis
        toleft
    with dissolve

    cory "hello.. young fish…"

    show shrimp default_om:
        duo_right_mantis
        toleft
    shrimp "no!"

    show cory anon:
        full
        duo_left
        vibrate
    cory "fugu you mean no?!"

    show cory anon:
        full
        duo_left
    cory "I mean! oooh that’s not a very nice thing to say to an elderly.. young fish…"

    show shrimp default_om:
        duo_right_mantis
        toleft
    shrimp "no! Most elders always have something up their sleeves!"

    show shrimp sepet:
        duo_right_mantis
        toleft
    shrimp "They call me sweet names and caress me without permission!"
    shrimp "And they think they can pass with that!"

    show cory anon:
        full
        duo_left
    cory "Mane.. That’s rough, I’m sorry for you buddy.."
    cory "Don’t worry I’m not that type of old.."

    show shrimp default_om:
        duo_right_mantis
        toleft
    shrimp "I don’t need your pity! I’m fine! Just surprised!"

    menu:

        "Negotiate with mr shrimp to ease it out":
            $ focus()
            cory "say young fish could you.."

            show shrimp default_om:
                duo_right_mantis
                toleft
            shrimp "No!"

            cory "Would you be so kind to at least hear me out-"

            show shrimp default_om:
                duo_right_mantis
                toleft
            shrimp "No!"

            cory "okay mane.."
            cory "Imma be real with you for a second."

            shrimp "...? But you're already real!"

            show shrimp sepet:
                duo_right_mantis
                toleft
            shrimp "Are you saying I'm talking to a ghost right now?!"

            cory "I ain’t no meemaw or peepaw"

            show cory talk:
                full
                duo_left
            with dissolve
            cory "remember me?"

            show shrimp surprise:
                duo_right_mantis
                toleft
                surprise
            shrimp "...you!"
            shrimp "The one that sneaked in a young fish!"

            show cory side:
                full
                duo_left
            cory "Yes… and I apologize with what I did"

            show cory talk_hu:
                full
                duo_left
            cory "But this ain’t you brother."
            cory "You were actively helpin out fishes in need"
            cory "Those who couldn’t pay the prices of this gate"

            show cory side_close:
                full
                duo_left
            cory "You helped my family when we had none.."

            show shrimp sepet:
                duo_right_mantis
                toleft
            shrimp "....!"

        "offers mr shrimp a snack" if has_item("coal_tar"):
            $ focus()
            cory "may I interest you in some snack young fish..?"

            show shrimp default_om:
                duo_right_mantis
                toleft
            shrimp "no!"

            cory "oh please? I've worked so hard to make these extra tasty…"
            cory "and you must be tired, guarding the entrance all day.."

            show shrimp default_om:
                duo_right_mantis
                toleft
            shrimp "No! That sounds suspicious!"

            show shrimp sepet:
                duo_right_mantis
                toleft
            shrimp "But fine! Maybe.. maybe just a bite!"

            "Mr shrimp took a small bite out of the algae. It's not very effective it seems."

            shrimp "hmm! As much as i like how it tastes…"

            show shrimp default_om:
                duo_right_mantis
                toleft
            shrimp "I shouldn’t be indulging myself more in this delicacy!"

            "Mr. Shrimp didn’t eat enough coal tar for it to take effect."
            $ coal_tar_effective = False
            $ remove_item("coal_tar")

            show cory side_close:
                full
                duo_left
                sink
            cory "oh fugu me…"

            show cory talk:
                full
                duo_left
            with dissolve

    show shrimp default_om:
        duo_right_mantis
        toleft
    shrimp "You’ve bothered me enough!"
    shrimp "It is time for us to duel if you’re so insistent on passing through!"

    show cory side:
        full
        duo_left
    cory "Guess we got no other choice huh.."

    show cory talk:
        full
        duo_left
    cory "prepare yerself to fight guppy…"

    jump mantis_pre_duel

label mantis_pre_duel:
    $ focus()

    show shrimp default_om:
        full
        trio_center_mantis
        toleft
        jump
    shrimp "We shall now start a sacred duel of… ROCK PAPER SCISSORS!"

    show cory surprise:
        full
        trio_left
        surprise
    cory "whuh?"

    show mc shock:
        full
        trio_right
        surprise
    mc "eh?"

    show cory upset:
        full
        trio_left
        vibrate
    cory "mane all that trouble just for some guppy games?!"
    cory "Why don’t everyfish just play and pass then?!"

    show shrimp proud:
        full
        trio_center_mantis
        toleft
    shrimp "The moment i mention a duel they all cower in fear and retreat!"
    shrimp "You’re the second bravest soul to duel with me today!"

    show mc o:
        full
        trio_right
    mc "Did the first fish pass?"

    show shrimp default:
        full
        trio_center_mantis
        toleft
    shrimp "No! They died under the weight of my mighty punch!"

    show cory unimpressed:
        full
        trio_left
        sink
    cory "glup…"

    show mc excited:
        full
        trio_right
        surprise
    mc "oh…!"

    show shrimp default_om:
        full
        trio_center_mantis
        toleft
    shrimp "The rules are easy!"
    shrimp "Each of you, have three rounds to go against me!"
    shrimp "And each round, whoever wins gets to attack the loser!"
    shrimp "Winning condition! Best two out of three wins!"

    show shrimp sepet:
        full
        trio_center_mantis
        toleft
    shrimp "Or if one of us is dead!"

    show shrimp proud:
        full
        trio_center_mantis
        toleft
    shrimp "Since you came in a pair, and I’m a generous mantis shrimp!"
    shrimp "One of you wins, and you both get through the gate!"

    show mc o:
        full
        trio_right
    mc "question! Are we allowed to dodge the attack"

    show shrimp default_om:
        full
        trio_center_mantis
        toleft
    shrimp "yes, dodge you shall!"

    show shrimp proud:
        full
        trio_center_mantis
        toleft
    shrimp "hmph! But can you really dodge my fast punches?!"

    show mc happy:
        full
        trio_right
    mc "hehe we’ll see about that"

    show cory talk_hu:
        full
        trio_left
    cory "you ready to start, guppy?"

    menu:
        "Sir yes sir mr. cory!":
            pass

    $ duel_fighter = "mc"
    call mantis_duel

    if _return == "win":
        jump mantis_win

    hide mc
    hide cory
    scene ch2_night with dissolve
    $ focus()

    if coal_tar_effective:
        "The coal tar is effectively weakening Mr Shrimp's punch. -1 HP"
        show shrimp default:
            full
            trio_center_mantis
            toleft
            vibrate
        shrimp "guh..! My punches aren’t as effective tonight…!"
        $ duel_fighter = "cory"
        call mantis_duel
        if _return == "win":
            jump mantis_win
    else:
        "Mr shrimp punch is as strong as ever, it knocked me far away hard. -3 HP"
        show shrimp default:
            full
            trio_center_mantis
            toleft
        shrimp "Hah! Witness the might of a peacock mantis shrimp!"

        show mc dizzy:
            full
            trio_right
            sink
            vibrate
        mc "nnguuh-!"

        show cory surprise:
            full
            trio_left
            jump
        cory "GUPPY!"

        show cory upset:
            full
            trio_left
            vibrate
        cory "ghhrr I’ll avenge you guppy!"

        show shrimp default:
            full
            trio_center_mantis
            toleft
        shrimp "Hah! Bring it On!"

        $ duel_fighter = "cory"
        $ coal_tar_effective = False
        call mantis_duel
        if _return == "win":
            jump mantis_win

    hide mc
    hide cory
    scene ch2_night with dissolve
    $ focus()

    show mc dizzy:
        full
        trio_right
        sink
    show cory dizzy:
        full
        trio_left
        sink
    show shrimp proud:
        trio_center_mantis
        toleft
    with dissolve
    "You were defeated by the Mantis Shrimp..."

    menu:
        "Try again?":
            jump mantis_pre_duel
        "Return to Hub":
            return

label mantis_win:
    $ focus()
    hide mc
    hide cory
    hide shrimp
    scene ch2_night with dissolve

    show mc excited:
        full
        trio_right
        jump
    show cory proud:
        full
        trio_left
        jump
    show shrimp sepet:
        trio_center_mantis
        toleft
    with dissolve

    mc "We did it!! We won mr.Cory!!"

    cory "EEEL YEAHH THAT’S WHAT I’M TALKING ABOUT GUPPY!!"

    show shrimp default_om:
        trio_center_mantis
        toleft
    shrimp "Hmph! Very well!"
    shrimp "You have proven yourself worthy of the sea’s grace!"

    "Mr shrimp moves aside to reveal the cave’s entrance and its long tunnel."
    "But we couldn’t just go yet.."

    mc "mr shrimp.. Why don’t you come along with us?"

    show shrimp surprise:
        trio_center_mantis
        toleft
        surprise
    shrimp "WHAT?!"

    show cory surprise:
        full
        trio_left
        surprise
    cory "HUH?!"
    cory "Guppy did you see how deadly those punches are?!"

    mc "I know! But it was part of the duel.."
    mc "He didn’t even once hurt us before it started…"

    show cory side:
        full
        trio_left
    cory "... can’t argue with that."

    show shrimp default:
        trio_center_mantis
        toleft
    shrimp "... But why the sudden preposterous preposition?!"
    shrimp "I’m the guardian of the sacred sea-salt gate!"
    shrimp "I mustn't leave my post! I mustn't let the unworthy pass!"

    mc "but you can’t keep doing this mr shrimp.."
    mc "there are fishes that reeaaally need to pass the gate.."

    show cory talk:
        full
        trio_left
    cory "They’re right.."
    cory "There’s a pregnant fish.. And some fish gone mad because of this carp"
    cory "Before this, You were actively helpin out fishes in need"
    cory "Those who couldn’t pay the prices of this gate, you’d help them pass.."
    cory "You’ve changed, what’s up with that? Really."

    show shrimp shy:
        trio_center_mantis
        toleft
    shrimp "...."
    shrimp "I was..!"

    show shrimp sepet:
        trio_center_mantis
        toleft
    shrimp "What I did was a moment of weakness! One that I wouldn’t repeat!"
    shrimp "And the cost of it was.. something irreversible…"
    shrimp "The one moment I let my guard down.."

    show shrimp surprise:
        trio_center_mantis
        toleft
        surprise
    shrimp "a sudden golden burst of incredible power dashed past me!"

    show mc o:
        full
        trio_right
        surprise
    mc "the golden fish…!"

    show shrimp default_om:
        trio_center_mantis
        toleft
    shrimp "It’s thousand suns way stronger than what my claws, my whole body can endure!"
    shrimp "I have never felt more powerless in my life than that moment!"
    shrimp "and it was I that let such a dangerous powerful entity into the sea…"
    shrimp "One that doesn’t bend down to rules… not even negotiation"
    shrimp "Since that moment, the empress has tightened security at every gate that leads to the sea."

    show shrimp shy:
        trio_center_mantis
        toleft
    shrimp "And even when the empress had known of my crimes of letting fishes that didn't qualify pass through…"

    show shrimp smile:
        trio_center_mantis
        toleft
    shrimp "She still forgave me!"

    show shrimp default_om:
        trio_center_mantis
        toleft
    shrimp "I swore to her that I won’t repeat the same mistake!"

    show mc o:
        full
        trio_right
    mc "But mr shrimp.. It wasn’t your fault that the golden fish pass through!"
    mc "it wasn’t something you can stop.. Nor something you can expect"
    mc "and me and mr cory are heading to sea in search of the golden fish!"
    mc "We can search for it together! To prevent it from doing more harm"

    show shrimp surprise:
        trio_center_mantis
        toleft
        surprise
    shrimp "YOU ARE?!"

    show shrimp shy:
        trio_center_mantis
        toleft
    shrimp "But.. who will guard the gates.. If not me?"

    show cory side:
        full
        trio_left
    cory "Naaah i don’t think it needs guarding."
    cory "That shrimp empress’s regime.. Is total bullshrimp"

    mc "the sea is big enough for everyone! And the sea can defend itself.."

    cory "There are fishes who just want to survive and meet their family.."
    cory "They don’t mean no harm to the sea i guarantee.."

    show shrimp default_om:
        trio_center_mantis
        toleft
    shrimp ".... Fine! I'll go! But only if we talk it out first with the shrimp empress!"

    show shrimp shy:
        trio_center_mantis
        toleft
    shrimp "I can't just abandon my post without notice"
    shrimp "That would be betrayal of the highest order!"

    $ chapter2_mantis_done = True
    $ mantis_trust = True
    $ focus()

    hide mc
    hide cory
    hide shrimp
    with dissolve

    return