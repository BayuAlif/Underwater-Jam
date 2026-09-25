label mantis_interaction:
    hide mc
    scene ch2_night
    $ focus()
    show shrimp default:
        full
        center
    show mc o:
        full
        right

    "The night settles in heavy, and so does the overbearing crowd dying to just quiet murmurs of protests."
    "Two pairs of eyes peek from behind a flock of corals. Analyzing the situation at hand carefully."

    show cory side_close:
        full
        leftish
        vibrate
    with moveinleft

    show shrimp laugh:
        full
        centerright
    with move

    cory "This is our best chance, guppy.."

    show mc excited at mc_npc

    mc "mm! We strike now!"

    "With a deep inhale I jumped out the coral while Mr.Cory trails behind slowly, we walked over to where the shrimp still stood its ground as straight as he was in the morning."

    show mc happy at mc_npc

    mc "Good evening.. Mr shrimp!"

    show shrimp surprise at shrimp_right

    shrimp "Huh?! A little kid?!"

    show shrimp default at shrimp_right

    shrimp "Go back to your parents!"
    shrimp "Using a young guppy won't make me go soft on you!"

    show shrimp default at shrimp_right

    shrimp "I will still punch you if you lose!"

    show cory upset at cory_npc

    cory "oooh.. That's not very nice... you can't be saying young fish..."

    show shrimp surprise at shrimp_right

    shrimp "and who are you!!"

    show cory smile at cory_npc

    cory "I'm the young guppy's guardian..."

    show shrimp sepet at shrimp_right

    shrimp "I'm still not letting an elderly and a young guppy pass!"
    shrimp "Especially the elder.... Squints"

    show shrimp default at shrimp_right

    shrimp "You have to prove yourself worthy through a duel!"
    shrimp "Only then I shall let you pass!"

    hide mc
    hide cory
    hide mc
    hide cory
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

    show mc default at mc_npc
    show cory talk at cory_npc
    show shrimp default at shrimp_right

    menu:

        "Ask why he's guarding the gate":

            mc "mm.. say mr shrimp.. why do you guard the gate so strictly...?"

            shrimp "Because I was told to!"

            show mc o at mc_npc

            mc "told to..? By who?"

            show shrimp proud at shrimp_right

            shrimp "The great empress I owe my life to!"
            shrimp "She saved me in my lowest moment in life.."

            show shrimp laugh at shrimp_right

            shrimp "And in exchange I devote my life to her compelling regime!"

            show mc dizzy at mc_npc

            mc "regime..? What's a regime :o"

            show shrimp default at shrimp_right

            shrimp "a regime is some sort of propaganda! Maybe!"

            show shrimp shy at shrimp_right

            shrimp "I'm not too good with politics either so I wouldn't know!"

            show mc pout at mc_npc

            mc "blehh you're right politics suck.. All the grown ups are so invested in it"
            mc "Is it so hard for everyone to just be friends, hold hands and help each other? :("

            show shrimp sepet at shrimp_right

            shrimp "hmm! Maybe you're right!"

            show shrimp default at shrimp_right

            shrimp "but it's hard to hold hands when you've got big claws this strong!"
            shrimp "It'd always hurt someone that's a different species!"
            shrimp "No matter how hard you try to be gentle."

            show mc o at mc_npc

            mc "..."

            menu:

                "Ask to touch his arm":

                    mc "Mr shrimp.."
                    mc "what if I were to hypothetically ask to..."
                    mc "touch your claws..?"

                    show shrimp surprise at shrimp_right

                    shrimp "No!"

                    show mc pout at mc_npc

                    mc "huh? Why not..?"

                    show shrimp default at shrimp_right

                    shrimp "Because it will hurt your tiny hands!"

                    show mc o at mc_npc

                    mc "but you said you won't hesitate to punch me in a duel.."
                    mc "why are you worried now Mr.shrimp?"

                    show shrimp default at shrimp_right

                    shrimp "... that's different! This is a no duel context!"
                    shrimp "I would minimize as much damage as possible!"

                    show mc happy at mc_npc

                    mc "But it's okay Mr.shrimp, I don't mind pain!"

                    show shrimp surprise at shrimp_right

                    shrimp "huh...?"

                    show mc default at mc_npc

                    mc "Some pain is worth it for the sake of knowledge."
                    mc "And also for the sake of easing other people's pain.."

                    shrimp "You're saying you'd hurt yourself just to feel my claws...?!"

                    show mc excited at mc_npc

                    mc "I've never met a mantis shrimp before!"
                    mc "So it made me suuuper curious on how your claws work!"

                    show shrimp sepet at shrimp_right

                    shrimp "... hmph. Fine then touch you shall!"

                    show shrimp default at shrimp_right

                    shrimp "But don't come crying if you scrape yourself!"

                    show mc pout at mc_npc

                    mc "im a good guppy! Good guppies don't cry!"

                    "Quenching curiosity, I started with poking its left claw with a finger repeatedly, assessing. With each poke, my finger easily bends under the rigid calloused textured shell."

                    show mc excited at mc_npc

                    mc "ooo..! So THIS is what a 150-kilo punch feels like..!"

                    show shrimp proud at shrimp_right

                    shrimp "How's it?! Fastest moving claws in all of animal kingdom!"

                    show shrimp laugh at shrimp_right

                    shrimp "Grace upon the excellent anatomy of a mantis shrimp! kakaka!"

                "Ask for a duel":

                    show mc shock at mc_npc

                    mc "Mr. shrimp.. Is winning a duel the only way to pass the gate..?"

                    show shrimp default at shrimp_right

                    shrimp "I'm afraid, yes little guppy!"
                    shrimp "You have to prove yourself worthy of the sea!"

                    show shrimp default at shrimp_right

                    shrimp "The beauty of it is not for the weak!"

                    show mc excited at mc_npc

                    mc "it leaves me no choice then.. bring it on!"

                    show shrimp laugh at shrimp_right

                    shrimp "Kakaka! That's the spirit"

        "I'm here to offer you snacks.. You seem veeery tired.." if has_item("coal_tar"):

            show mc happy at mc_npc

            mc "I'm here to offer you snacks.. You seem veeery tired.."

            show shrimp surprise at shrimp_right

            shrimp "Huh...!"

            show shrimp proud at shrimp_right

            shrimp "Wait me? TIRED? Tiredness can't affect a warrior!"

            shrimp "But I won't say no to delicious looking delicacies"

            "Without second guessing, Mr.shrimp took about three clams, breaking the shell with his punch before stuffing it into his mouth enthusiastically."

            show shrimp default at shrimp_right

            shrimp "mm? What is it! Why are you staring!"

            shrimp "Staring won't make me share a thing with you!"

            show mc default at mc_npc

            mc "ah nonono am not hungry... *stomach growls*"

            show shrimp surprise at shrimp_right

            shrimp "...."

            show shrimp sepet at shrimp_right

            shrimp "Let's hypothetically say, I shared one clam!"

            show shrimp shy at shrimp_right

            shrimp "Would you eat it?!"

            show mc o at mc_npc

            mc "...!"

            show mc happy at mc_npc

            mc "hehe don't worry you can have all of it, mr shrimp"
            mc "you look like you need it more"

            show shrimp surprise at shrimp_right

            shrimp "I never said that I WOULD share it with you!"

            show shrimp default at shrimp_right

            shrimp "That was a merely hypothetical!"
            shrimp "Don't get too into yourself now!"

            $ coal_tar_effective = True
            $ remove_item("coal_tar")

            menu:

                "Is clam your favorite food?":

                    show mc o at mc_npc

                    mc "Is clam your favorite food?"

                    show shrimp smile at shrimp_right

                    shrimp "maybe!"

                    show mc happy at mc_npc

                    mc "mm you seem starving.."

                    show shrimp surprise at shrimp_right

                    shrimp "Starving?! A mantis shrimp is able to not eat anything for weeks without hunger!"

                    show mc o at mc_npc

                    mc "and when's the last time you eat?"

                    show shrimp default at shrimp_right

                    shrimp "I don't keep count!"

                    show shrimp smile at shrimp_right

                    shrimp "Though I must say these are oddly rich tasted clams! Very scrumptious!"
                    shrimp "What did you put in them?!"

                    show mc shock at mc_npc

                    mc "ah that's.."
                    mc "mmn it's a secret ingredient I can't tell you!"

                    show mc happy at mc_npc

                    mc "unless you let me pass then maybe I'll tell.."

                    show shrimp surprise at shrimp_right

                    shrimp "guh...!!"

                    show shrimp shy at shrimp_right

                    shrimp "O-okay.. fine. pass you shall!"

                    show mc excited at mc_npc

                    mc "Really?!"

                    show shrimp surprise at shrimp_right

                    shrimp "WAIT WAIT WAIT! NO! PASS YOU SHALL NOT!"

                    show shrimp sepet at shrimp_right

                    shrimp "bad! bad Clarus! You can't let good food cloud your judgement!"

                    shrimp "even when said food.. reminds you of your mother's cooking..."

                    show mc o at mc_npc

                    mc "mm.. but i say your mother's cooking is worth fighting for!"

                    show mc happy at mc_npc

                    mc "sometimes it's the reason to keep going for another day and the next!"

                    show shrimp default at shrimp_right

                    shrimp ".... you might be right!"

                    show shrimp smile at shrimp_right

                    shrimp "My mother's food always gave me a calming effect!"
                    shrimp "One that would make you rest easier!"

                    show mc shock at mc_npc

                    "Was tiny mr shrimp so active that his mother had to feed him coal tar to make him less energized..?"

                    show shrimp laugh at shrimp_right

                    shrimp "So, I must thank you for the food and the memories!"

                    show shrimp default at shrimp_right

                    shrimp "I'm still not letting you pass though!"

                    show shrimp shy at shrimp_right

                    shrimp "Please bring me more of it..."

                "Ask for a duel":

                    show mc shock at mc_npc

                    mc "Mr. shrimp.. Is winning a duel the only way to pass the gate..?"

                    show shrimp default at shrimp_right

                    shrimp "I'm afraid, yes little guppy!"

                    show shrimp default at shrimp_right

                    shrimp "You have to prove yourself worthy of the sea!"
                    shrimp "The beauty of it is not for the weak!"

                    show mc excited at mc_npc

                    mc "it leaves me no choice then.. bring it on!"

                    show shrimp laugh at shrimp_right

                    shrimp "Kakaka! That's the spirit"

    jump mantis_start_duel

label mantis_as_cory:

    show mc default at mc_npc
    show cory smile_hu at cory_npc
    show shrimp default at shrimp_right

    cory "hello.. young fish..."

    shrimp "no!"

    show cory upset at cory_npc

    cory "fugu you mean no?!"

    show cory smile at cory_npc

    cory "I mean! oooh that's not a very nice thing to say to an elderly.. young fish..."

    shrimp "no! Most elders always have something up their sleeves!"

    show shrimp sepet at shrimp_right

    shrimp "They call me sweet names and caress me without permission!"
    shrimp "And they think they can pass with that!"

    show cory side at cory_npc

    cory "Mane.. That's rough, I'm sorry for you buddy.."
    cory "Don't worry I'm not that type of old.."

    show shrimp default at shrimp_right

    shrimp "I don't need your pity! I'm fine! Just surprised!"

    menu:

        "Negotiate with Mr. Shrimp to ease it out":

            cory "say young fish could you.."

            show shrimp default at shrimp_right

            shrimp "No!"

            cory "Would you be so kind to at least hear me out-"

            shrimp "No!"

            cory "okay mane.."

            cory "Imma be real with you for a second."

            shrimp "...? But you're already real!"

            show shrimp sepet at shrimp_right

            shrimp "Are you saying I'm talking to a ghost right now?!"

            cory "I ain't no meemaw or peepaw"

            show cory side at cory_npc

            cory "remember me?"

            show shrimp surprise at shrimp_right

            shrimp "...you!"
            shrimp "The one that sneaked in a young fish!"

            show cory side_close at cory_npc

            cory "Yes... and I apologize with what I did"
            cory "But this ain't you brother."
            cory "You were actively helpin out fishes in need"
            cory "Those who couldn't pay the prices of this gate"
            cory "You helped my family when we had none.."

            show shrimp sepet at shrimp_right

            shrimp "....!"

        "May I interest you in some snack young fish.." if has_item("coal_tar"):

            cory "may I interest you in some snack young fish..?"

            show shrimp default at shrimp_right

            shrimp "no!"

            cory "oh please? I've worked so hard to make these extra tasty..."
            cory "and you must be tired, guarding the entrance all day.."

            show shrimp default at shrimp_right

            shrimp "No! That sounds suspicious!"

            show shrimp sepet at shrimp_right

            shrimp "But fine! Maybe.. maybe just a bite!"

            "Mr shrimp took a small bite out of the algae. It's not very effective it seems."

            shrimp "hmm! As much as i like how it tastes..."

            show shrimp default at shrimp_right

            shrimp "I shouldn't be indulging myself more in this delicacy!"

            "Mr. Shrimp didn't eat enough coal tar for it to take effect."

            $ coal_tar_effective = False
            $ remove_item("coal_tar")

            cory "oh fugu me..."

    jump mantis_start_duel

label mantis_start_duel:

    $ duel_fighter = "mc"

    hide mc
    scene ch2_dialogue

    show mc default at mc_npc
    show cory talk at cory_npc
    show shrimp default at shrimp_right

    shrimp "You've bothered me enough!"
    shrimp "It is time for us to duel if you're so insistent on passing through!"

    show cory side at cory_npc

    cory "Guess we got no other choice huh.."
    cory "prepare yerself to fight guppy..."

    show shrimp default at shrimp_right

    shrimp "We shall now start a sacred duel! Get ready to SPAM Z!"

    show cory surprise at cory_npc

    cory "whuh?"

    show mc shock at mc_npc

    mc "eh?"

    show cory upset at cory_npc

    cory "mane all that trouble just for some guppy games?!"
    cory "Why don't everyfish just play and pass then?!"

    shrimp "The moment i mention a duel they all cower in fear and retreat!"
    shrimp "You're the second bravest soul to duel with me today!"

    show mc o at mc_npc

    mc "Did the first fish pass?"

    show shrimp proud at shrimp_right

    shrimp "No! They died under the weight of my mighty punch!"

    show cory unimpressed at cory_npc

    cory "glup..."

    show mc excited at mc_npc

    mc "oh...!"

    show shrimp default at shrimp_right

    shrimp "The rules are easy!"
    shrimp "Each of you, have three rounds to go against me!"
    shrimp "And each round, whoever wins gets to attack the loser!"
    shrimp "Winning condition! Best two out of three wins!"

    show shrimp sepet at shrimp_right

    shrimp "Or if one of us is dead!"

    show shrimp proud at shrimp_right

    shrimp "Since you came in a pair, and I'm a generous mantis shrimp!"
    shrimp "One of you wins, and you both get through the gate!"

    show mc o at mc_npc

    mc "question! Are we allowed to dodge the attack"

    show shrimp default at shrimp_right

    shrimp "yes, dodge you shall!"

    show shrimp proud at shrimp_right

    shrimp "hmph! But can you really dodge my fast punches?!"

    show mc happy at mc_npc

    mc "hehe we'll see about that"

    show cory talk_hu at cory_npc

    cory "you ready to start, guppy?"

    mc "Sir yes sir mr. cory!"

    call mantis_duel

    if _return == "win":

        call mantis_win

        return

    hide mc
    scene ch2_dialogue

    show mc dizzy at mc_npc
    mc "nnguuh-!"

    show cory surprise at cory_npc
    cory "GUPPY!"

    show cory upset at cory_npc
    cory "ghhrr I'll avenge you guppy!"

    show shrimp default at shrimp_right
    shrimp "Hah! Bring it On!"

    $ duel_fighter = "cory"
    $ coal_tar_effective = False

    call mantis_duel

    if _return == "win":
        call mantis_win
        return

    hide mc
    scene ch2_dialogue

    show mc dizzy at mc_npc
    show cory dizzy at cory_npc
    show shrimp proud at shrimp_right

    "You were defeated by the Mantis Shrimp..."

    menu:

        "Try again?":

            jump mantis_start_duel

        "Return to Hub":

            return

label mantis_win:

    hide mc
    scene ch2_dialogue

    show mc excited at mc_npc
    show cory proud at cory_npc
    show shrimp sepet at shrimp_right

    mc "We did it!! We won Mr.Cory!!"

    cory "EEEL YEAHH THAT'S WHAT I'M TALKING ABOUT GUPPY!!"

    shrimp "Hmph! Very well!"
    shrimp "You have proven yourself worthy of the sea's grace!"

    "Mr shrimp moves aside to reveal the cave's entrance and its long tunnel."

    mc "mr shrimp.. Why don't you come along with us?"

    show shrimp surprise at shrimp_right

    shrimp "WHAT?!"

    show cory surprise at cory_npc

    cory "HUH?!"
    cory "Guppy did you see how deadly those punches are?!"

    mc "I know! But it was part of the duel.."
    mc "He didn't even once hurt us before it started..."

    show cory side at cory_npc

    cory "... can't argue with that."

    show shrimp default at shrimp_right

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

    show shrimp shy at shrimp_right

    shrimp "...."
    shrimp "I was..!"

    show shrimp sepet at shrimp_right

    shrimp "What I did was a moment of weakness! One that I wouldn't repeat!"
    shrimp "And the cost of it was.. something irreversible..."
    shrimp "The one moment I let my guard down.."

    show shrimp surprise at shrimp_right

    shrimp "a sudden golden burst of incredible power dashed past me!"

    show mc o at mc_npc

    mc "the golden fish...!"

    show shrimp default at shrimp_right

    shrimp "It's thousand suns way stronger than what my claws, my whole body can endure!"
    shrimp "I have never felt more powerless in my life than that moment!"
    shrimp "and it was I that let such a dangerous powerful entity into the sea..."
    shrimp "One that doesn't bend down to rules... not even negotiation"
    shrimp "Since that moment, the empress has tightened security at every gate that leads to the sea."

    show shrimp shy at shrimp_right

    shrimp "And even when the empress had known of my crimes of letting fishes that didn't qualify pass through..."

    show shrimp smile at shrimp_right

    shrimp "She still forgave me!"

    show shrimp default at shrimp_right

    shrimp "I swore to her that I won't repeat the same mistake!"

    show mc o at mc_npc

    mc "But mr shrimp.. It wasn't your fault that the golden fish pass through!"
    mc "it wasn't something you can stop.. Nor something you can expect"
    mc "and me and mr cory are heading to sea in search of the golden fish!"
    mc "We can search for it together! To prevent it from doing more harm"

    show shrimp surprise at shrimp_right

    shrimp "YOU ARE?!"

    show shrimp shy at shrimp_right

    shrimp "But.. who will guard the gates.. If not me?"

    show cory side at cory_npc

    cory "Naaah i don't think it needs guarding."
    cory "That shrimp empress's regime.. Is total bullshrimp"

    mc "the sea is big enough for everyone! And the sea can defend itself.."

    cory "There are fishes who just want to survive and meet their family.."
    cory "They don't mean no harm to the sea i guarantee.."

    show shrimp default at shrimp_right

    shrimp ".... Fine! I'll go! But only if we talk it out first with the shrimp empress!"

    show shrimp shy at shrimp_right

    shrimp "I can't just abandon my post without notice"
    shrimp "That would be betrayal of the highest order!"

    $ chapter2_mantis_done = True
    $ mantis_trust = True

    return
