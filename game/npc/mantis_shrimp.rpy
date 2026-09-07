# =========================================================
# MANTIS SHRIMP CONFRONTATION & RPS DUEL
# =========================================================

default coal_tar_effective = False
default mantis_scene_active = False

label mantis_shrimp:

    $ mantis_scene_active = True
    $ mantis_last_sprite_attrs = {}

    scene expression get_dialogue_background()

    hide mc
    hide cory
    hide shrimp

    "The night settles in heavy, and so does the overbearing crowd dying to just quiet murmurs of protests"
    "Two pairs of eyes peek from behind a flock of corals. Analyzing the situation at hand carefully"

    show cory side at mantis_scene_cory_pos

    cory "This is our best chance, guppy.."

    show mc o at mantis_scene_mc_pos

    mc "mm! We strike now!"

    "With a deep inhale I jumped out the coral while Mr.Cory trails behind slowly, we walked over to where the shrimp still stood its ground as straight as he was in the morning. Though he didn't immediately notice me."

    mc "Good evening.. Mr shrimp!"

    show shrimp surprise at mantis_scene_shrimp_pos
    shrimp "Huh?! A little kid?!"
    show shrimp default at mantis_scene_shrimp_pos
    shrimp "Go back to your parents!"
    shrimp "Using a young guppy won't make me go soft on you!"
    shrimp "I will still punch you if you lose!"

    "Oh to be punched by a mantis shrimp.. I wonder how much powerful it will feel than my friend's at school"

    show cory side at mantis_scene_cory_pos

    cory "oooh.. That's not very nice... you can't be saying young fish..."

    shrimp "and who are you!!"

    cory "I'm the young guppy's guardian..."

    shrimp "I'm still not letting an elderly and a young guppy pass!"
    shrimp "Especially the elder.... *squints*"
    shrimp "You have to prove yourself worthy through a duel!"
    shrimp "Only then I shall let you pass!"

    call select_interactor

    if _return == "mc":

        jump mantis_as_mc

    else:

        jump mantis_as_cory


# =========================================================
# CONFRONT AS MC
# =========================================================

label mantis_as_mc:

    hide cory
    show mc default at mantis_scene_mc_pos

    menu:

        "Ask why he's guarding the gate":

            mc "mm.. say Mr shrimp.. why do you guard the gate so strictly...?"

            shrimp "Because I was told to!"

            show mc o at mantis_scene_mc_pos

            mc "told to..? By who?"

            shrimp "The great empress I owe my life to!"
            shrimp "She saved me in my lowest moment in life.."
            shrimp "And in exchange I devote my life to her compelling regime!"

            mc "regime..? What's a regime :0"

            show shrimp smile at mantis_scene_shrimp_pos
            shrimp "a regime is some sort of propaganda! Maybe!"
            show shrimp default at mantis_scene_shrimp_pos
            shrimp "I'm not too good with politics either so I wouldn't know!"

            show mc pout at mantis_scene_mc_pos

            mc "blehh you're right politics suck.. All the grown ups are so invested in it"
            mc "Is it so hard for everyone to just be friends, hold hands and help each other? :("

            shrimp "hmm! Maybe you're right!"
            shrimp "but it's hard to hold hands when you've got big claws this strong!"
            shrimp "It'd always hurt someone that's a different species!"
            shrimp "No matter how hard you try to be gentle."

            mc "..."

            menu:

                "Ask to touch his arm":

                    mc "Mr shrimp.."
                    mc "what if I were to hypothetically ask to..."
                    mc "touch your claws..?"

                    show shrimp seppet at mantis_scene_shrimp_pos
                    shrimp "No!"

                    mc "huh? Why not..?"

                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "Because it will hurt your tiny hands!"

                    show mc o at mantis_scene_mc_pos

                    mc "but you said you won't hesitate to punch me in a duel.."
                    mc "why are you worried now Mr.shrimp?"

                    shrimp "... that's different! This is a no duel context!"
                    shrimp "I would minimize as much damage as possible!"

                    show mc happy at mantis_scene_mc_pos

                    mc "But it's okay Mr.shrimp, I don't mind pain!"

                    show shrimp surprise at mantis_scene_shrimp_pos
                    shrimp "huh...?"

                    show mc default at mantis_scene_mc_pos

                    mc "Some pain is worth it for the sake of knowledge."
                    mc "And also for the sake of easing other people's pain.."

                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "You're saying you'd hurt yourself just to feel my claws..?!"

                    show mc excited at mantis_scene_mc_pos

                    mc "I've never met a mantis shrimp before!"
                    mc "So it made me suuuper curious on how your claws work!"

                    show shrimp smile at mantis_scene_shrimp_pos
                    shrimp "... hmph. Fine then touch you shall!"
                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "But don't come crying if you scrape yourself!"

                    show mc pout at mantis_scene_mc_pos

                    mc "im a good guppy! Good guppies don't cry!"

                    "Quenching curiosity, I started with poking its left claw with a finger repeatedly, assessing. With each poke, my finger easily bends under the rigid calloused textured shell."

                    show mc excited at mantis_scene_mc_pos

                    mc "ooo..! So THIS is what a 150-kilo punch feels like..!"

                    show shrimp proud at mantis_scene_shrimp_pos
                    shrimp "How's it?! Fastest moving claws in all of animal kingdom!"
                    show shrimp laugh at mantis_scene_shrimp_pos
                    shrimp "Grace upon the excellent anatomy of a mantis shrimp! kakaka!"

                "Ask for a duel":

                    show mc shock at mantis_scene_mc_pos

                    mc "Mr. shrimp.. Is winning a duel the only way to pass the gate..?"

                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "I'm afraid, yes little guppy!"
                    shrimp "You have to prove yourself worthy of the sea!"

                    show mc excited at mantis_scene_mc_pos

                    mc "it leaves me no choice then.. bring it on!"

                    show shrimp laugh at mantis_scene_shrimp_pos
                    shrimp "haha! That's the spirit"

        "Offer Mr Shrimp a snack (Coal Tar)" if has_item("coal_tar"):

            mc "oh no, I'm not here for a duel!"
            mc "I'm here to offer you snacks.. You seem veeery tired.."

            show shrimp surprise at mantis_scene_shrimp_pos
            shrimp "Huh...!"
            show shrimp proud at mantis_scene_shrimp_pos
            shrimp "Wait me? TIRED? Tiredness can't affect a warrior!"
            show shrimp default at mantis_scene_shrimp_pos
            shrimp "But I won't say no to delicious looking delicacies"

            "Without second guessing, Mr.shrimp took about three clams, breaking the shell with his punch before stuffing it into his mouth enthusiastically."

            shrimp "mm? What is it! Why are you staring!"
            shrimp "Staring won't make me share a thing with you!"

            mc "ah nonono am not hungry... *stomach growls*"

            shrimp "...."
            shrimp "Let's hypothetically say, I shared one clam!"
            shrimp "Would you eat it?!"

            show mc o at mantis_scene_mc_pos

            mc "...!"

            show mc happy at mantis_scene_mc_pos

            mc "hehe don't worry you can have all of it, Mr shrimp"
            mc "you look like you need it more"

            shrimp "I never said that I WOULD share it with you!"
            shrimp "That was a merely hypothetical!"
            shrimp "Don't get too into yourself now!"

            $ coal_tar_effective = True
            $ remove_item("coal_tar")

            menu:

                "Ask for his favorite food":

                    mc "Is clam your favorite food?"

                    show shrimp smile at mantis_scene_shrimp_pos
                    shrimp "maybe!"

                    mc "mm you seem very hungry eating it.."

                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "Hungry?! A mantis shrimp is able to not eat anything for weeks without hunger!"

                    show mc o at mantis_scene_mc_pos

                    mc "and when's the last time you eat?"

                    shrimp "I don't keep count!"
                    show shrimp smile at mantis_scene_shrimp_pos
                    shrimp "Though I must say these are oddly rich tasted clams! Very scrumptious!"
                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "What did you put in them?!"

                    show mc shock at mantis_scene_mc_pos

                    mc "ah that's.."
                    mc "mmn it's a secret ingredient I can't tell you!"

                    show mc happy at mantis_scene_mc_pos

                    mc "unless you let me pass then maybe I'll tell.."

                    show shrimp surprise at mantis_scene_shrimp_pos
                    shrimp "guh...!!"
                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "O-okay.. fine. pass you shall!"

                    show mc excited at mantis_scene_mc_pos

                    mc "Really?!"

                    show shrimp seppet at mantis_scene_shrimp_pos
                    shrimp "WAIT WAIT WAIT! NO! PASS YOU SHALL NOT!"
                    shrimp "bad! bad manti! You can't let good food cloud your judgement!"
                    show shrimp shy at mantis_scene_shrimp_pos
                    shrimp "even when said food.. reminds you of your mother's cooking..."

                    show mc o at mantis_scene_mc_pos

                    mc "mm.. but I say your mother's cooking is worth fighting for!"

                    show mc happy at mantis_scene_mc_pos

                    mc "sometimes it's the reason to keep going for another day and the next!"

                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp ".... you might be right!"
                    show shrimp shy at mantis_scene_shrimp_pos
                    shrimp "My mother's food always gave me a calming effect!"
                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "One that would make you rest easier!"

                    show mc shock at mantis_scene_mc_pos

                    "Was tiny Mr shrimp so active that his mother had to feed him coal tar to make him less energized..?"

                    show shrimp smile at mantis_scene_shrimp_pos
                    shrimp "So, I must thank you for the food and the memories!"
                    show shrimp default at mantis_scene_shrimp_pos
                    shrimp "I'm still not letting you pass though!"
                    shrimp "Please bring me more of it..."

                "Ask for a duel":

                    show mc shock at mantis_scene_mc_pos

                    mc "Mr. shrimp, Is winning a duel the only way to pass the gate..?"

                    shrimp "I'm afraid, yes little guppy!"
                    shrimp "You have to prove yourself worthy of the sea!"

                    show mc excited at mantis_scene_mc_pos

                    mc "it leaves me no choice then!"

                    show shrimp laugh at mantis_scene_shrimp_pos
                    shrimp "haha! That's the spirit"

    jump mantis_start_duel


# =========================================================
# CONFRONT AS CORY
# =========================================================

label mantis_as_cory:

    $ cory_at_right = False
    hide mc
    show cory unimpressed at mantis_scene_cory_pos

    cory "hello.. young fish..."

    show shrimp seppet at mantis_scene_shrimp_pos
    shrimp "no!"

    show cory upset at mantis_scene_cory_pos

    cory "fugu you mean no?!"
    cory "I mean! oooh that's not a very nice thing to say to an elderly.. young fish..."

    shrimp "no! Most elders always have something up their sleeves!"
    show shrimp default at mantis_scene_shrimp_pos
    shrimp "They call me sweet names and caress me without permission!"
    shrimp "And they think they can pass with that!"

    cory "Mane.. That's rough, I'm sorry for you buddy.."
    cory "Don't worry I'm not that type of old.."

    shrimp "I don't need your pity! I'm fine! Just surprised!"

    menu:

        "Negotiate with Mr Shrimp to ease it out":

            cory "say young fish could you.."

            show shrimp seppet at mantis_scene_shrimp_pos
            shrimp "No!"

            cory "Would you be so kind to at least hear me out-"

            shrimp "No!"

            cory "okay mane.."
            cory "Imma be real with you for a second."

            show shrimp default at mantis_scene_shrimp_pos
            shrimp "...? But you're already real!"
            shrimp "Are you saying I'm talking to a ghost right now?!"

            cory "I ain't no meemaw or peepaw"

            show cory smile_hu at mantis_scene_cory_pos

            cory "remember me?"

            shrimp "...you!"
            shrimp "The one that sneaked in a young fish!"

            show cory side at mantis_scene_cory_pos

            cory "Yes... and I apologize with what I did"

            show cory netral_hu at mantis_scene_cory_pos

            cory "But this ain't you brother."
            cory "You were actively helpin out fishes in need"
            cory "Those who couldn't pay the prices of this gate"

            show cory sideclose at mantis_scene_cory_pos

            cory "You helped my family when we had none.."

            show shrimp surprise at mantis_scene_shrimp_pos
            shrimp "....!"

        "Offer Mr Shrimp a snack (Coal Tar)" if has_item("coal_tar"):

            cory "may I interest you in some snack young fish..?"

            show shrimp seppet at mantis_scene_shrimp_pos
            shrimp "no!"

            cory "oh please? I've worked so hard to make these extra tasty..."
            cory "and you must be tired, guarding the entrance all day.."

            shrimp "No! That sounds suspicious!"
            show shrimp default at mantis_scene_shrimp_pos
            shrimp "But fine! Maybe.. maybe just a bite!"

            "Mr shrimp took a small bite out of the algae. It's not very effective it seems."

            shrimp "hmm! As much as I like how it tastes..."
            show shrimp smile at mantis_scene_shrimp_pos
            shrimp "I shouldn't be indulging myself more in this delicacy!"

            "Mr. Shrimp didn't eat enough coal tar for it to take effect."

            $ coal_tar_effective = False
            $ remove_item("coal_tar")

            cory "oh fugu me..."

    jump mantis_start_duel


# =========================================================
# MANTIS DUEL PREPARATION & MINIGAME
# =========================================================

label mantis_start_duel:

    $ cory_at_right = False

    show shrimp default at mantis_scene_shrimp_pos
    shrimp "You've bothered me enough!"
    shrimp "It is time for us to duel if you're so insistent on passing through!"

    show cory netral_hu at mantis_scene_cory_pos

    cory "Guess we got no other choice huh.."
    cory "prepare yerself to fight guppy..."

    shrimp "We shall now start a sacred duel of... ROCK PAPER SCISSORS!"

    show cory surprise at mantis_scene_cory_pos

    cory "whuh?"

    show mc shock at mantis_scene_mc_pos

    mc "eh?"

    show cory upset at mantis_scene_cory_pos

    cory "mane all that trouble just for some guppy games?!"
    cory "Why don't everyfish just play and pass then?!"

    shrimp "The moment I mention a duel they all cower in fear and retreat!"
    shrimp "You're the second bravest soul to duel with me today!"

    show mc o at mantis_scene_mc_pos

    mc "Did the first fish pass?"

    show shrimp proud at mantis_scene_shrimp_pos
    shrimp "No! They died under the weight of my mighty punch!"

    show cory unimpressed at mantis_scene_cory_pos

    cory "glup..."

    show mc excited at mantis_scene_mc_pos

    mc "oh...!"

    show shrimp default at mantis_scene_shrimp_pos
    shrimp "The rules are easy!"
    shrimp "Each of you, have three rounds to go against me!"
    shrimp "And each round, whoever wins gets to attack the loser!"
    shrimp "Winning condition! Best two out of three wins!"
    shrimp "Or if one of us is dead!"
    show shrimp proud at mantis_scene_shrimp_pos
    shrimp "Since you came in a pair, and I'm a generous mantis shrimp!"
    show shrimp default at mantis_scene_shrimp_pos
    shrimp "One of you wins, and you both get through the gate!"

    mc "question! Are we allowed to dodge the attack"

    shrimp "yes, dodge you shall!"
    show shrimp seppet at mantis_scene_shrimp_pos
    shrimp "hmph! But can you really dodge my fast punches?!"

    mc "hehe we'll see about that"

    cory "you ready to start, guppy?"

    mc "Sir yes sir Mr. Cory!"

    $ player_score = 0
    $ shrimp_score = 0
    $ current_round = 1

    call rps_best_of_three(
        fighter="mc",
        weakened=coal_tar_effective
    )

    $ player_score = duel_player_wins
    $ shrimp_score = duel_shrimp_wins

    if duel_result == "player_win":

        jump rps_check_winner

    if coal_tar_effective:

        jump rps_check_winner

    # MC was knocked out. Keep the original story flow:
    # Cory takes over for the next duel.
    scene expression get_dialogue_background()

    show mc dizzy at mantis_scene_mc_pos

    mc "nnguuh-!"

    hide mc
    show cory surprise at mantis_scene_cory_pos

    cory "GUPPY!"

    show cory upset at mantis_scene_cory_pos

    cory "ghhrr I'll avenge you guppy!"

    hide cory
    show shrimp default at mantis_scene_shrimp_pos
    shrimp "Hah! Bring it On!"

    $ player_score = 1
    $ shrimp_score = 0
    $ current_round = 1

    call rps_best_of_three(
        fighter="cory",
        weakened=False
    )

    $ player_score = duel_player_wins
    $ shrimp_score = duel_shrimp_wins

    jump rps_check_winner


label rps_check_winner:

    if player_score > shrimp_score:

        show mc excited at mantis_scene_mc_pos

        mc "We did it!! We won Mr.Cory!!"

        show cory proud at mantis_scene_cory_pos

        cory "EEEL YEAHH THAT'S WHAT I'M TALKING ABOUT GUPPY!!"

        show shrimp seppet at mantis_scene_shrimp_pos
        shrimp "Hmph! Very well!"
        show shrimp proud at mantis_scene_shrimp_pos
        shrimp "You have proven yourself worthy of the sea's grace!"

        "Mr shrimp moves aside to reveal the cave's entrance and its long tunnel."
        "But we couldn't just go yet.."

        mc "Mr shrimp.. Why don't you come along with us?"

        show shrimp surprise at mantis_scene_shrimp_pos
        shrimp "WHAT?!"

        show cory surprise at mantis_scene_cory_pos

        cory "HUH?!"
        cory "Guppy did you see how deadly those punches are?!"

        mc "I know! But it was part of the duel.."
        mc "He didn't even once hurt us before it started..."

        show cory side at mantis_scene_cory_pos

        cory "... can't argue with that."

        show shrimp default at mantis_scene_shrimp_pos
        shrimp "... But why the sudden preposterous preposition?!"
        shrimp "I'm the guardian of the sacred sea-salt gate!"
        shrimp "I mustn't leave my post! I mustn't let the unworthy pass!"

        mc "but you can't keep doing this Mr shrimp.."
        mc "there are fishes that reeaaally need to pass the gate.."

        cory "They're right.."
        cory "There's a pregnant fish.. And some fish gone mad because of this carp"
        cory "Before this, You were actively helpin out fishes in need"
        cory "Those who couldn't pay the prices of this gate, you'd help them pass.."
        cory "You've changed, what's up with that? Really."

        shrimp "...."
        shrimp "I was..!"
        shrimp "What I did was a moment of weakness! One that I wouldn't repeat!"
        shrimp "And the cost of it was.. something irreversible..."
        shrimp "The one moment I let my guard down.."
        shrimp "a sudden golden burst of incredible power dashed past me!"

        show mc o at mantis_scene_mc_pos

        mc "the golden fish...!"

        shrimp "It's thousand suns way stronger than what my claws, my whole body can endure!"
        shrimp "I have never felt more powerless in my life than that moment!"
        shrimp "and it was I that let such a dangerous powerful entity into the sea..."
        shrimp "One that doesn't bend down to rules... not even negotiation"
        shrimp "Since that moment, the empress has tightened security at every gate that leads to the sea."
        shrimp "And even when the empress had known of my crimes of letting fishes that didn't qualify pass through..."
        shrimp "She still forgave me!"
        shrimp "I swore to her that I won't repeat the same mistake!"

        mc "But Mr shrimp.. It wasn't your fault that the golden fish pass through!"
        mc "it wasn't something you can stop.. Nor something you can expect"
        mc "and me and Mr Cory are heading to sea in search of the golden fish!"
        mc "We can search for it together! To prevent it from doing more harm"

        show shrimp surprise at mantis_scene_shrimp_pos
        shrimp "YOU ARE?!"
        show shrimp default at mantis_scene_shrimp_pos
        shrimp "But.. who will guard the gates.. If not me?"

        cory "Naaah I don't think it needs guarding."
        cory "That shrimp empress's regime.. Is total bullshrimp"

        mc "the sea is big enough for everyone! And the sea can defend itself.."

        cory "There are fishes who just want to survive and meet their family.."
        cory "They don't mean no harm to the sea I guarantee.."

        shrimp ".... Fine! I'll go! But only if we talk it out first with the shrimp empress!"
        shrimp "I can't just abandon my post without notice"
        shrimp "That would be betrayal of the highest order!"

        $ mantis_scene_active = False

        return

    else:

        show mc dizzy at mantis_scene_mc_pos
        show shrimp proud at mantis_scene_shrimp_pos

        "You were defeated by the Mantis Shrimp..."

        menu:

            "Try again?":

                jump mantis_start_duel

            "Return to Hub":

                $ mantis_scene_active = False

                # mantis_shrimp is entered from chapter2.rpy via
                # `call mantis_shrimp`, so it must always finish with
                # `return` (never `jump`) or the call frame pushed by
                # that `call` is left on the stack forever.
                #
                # duel_result stays whatever rps_best_of_three() last
                # set it to (e.g. "ko"), so the caller in chapter2.rpy
                # can tell this was a loss and route back to the hub
                # itself instead of continuing into chapter2_night_ending.
                return