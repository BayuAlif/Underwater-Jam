label ch3_boss_negotiation:
    hide mc
    hide cory
    hide scy
    hide teto
    hide goby
    call screen choose_interactor(
        "Choose who should negotiate with the Empress!",
        "Each character will present their own proposal"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_boss_negotiate_as_mc
    elif selected_questioner == "cory":
        jump ch3_boss_negotiate_as_cory
    else:
        jump ch3_boss_negotiate_as_scyllarus

label ch3_boss_negotiate_as_mc:
    show mc happy:
        unpose
        full
        right
        walkloop
    with moveinleft
    mc "Hi!! Your highness goby fish!"

    show goby default:
        unpose
        full
        center
    with moveinright
    gob "You have 10 seconds to speak your lies"
    gob "Before my spear goes through you."

    show mc shock_hu:
        full
        right
        surprise
    mc "ah only t-ten seconds?! oh no! oh no!"

    show goby annoy:
        full
        center
    gob "There goes your two seconds."
    hide mc
    hide goby
    show screen ch3_boss_negotiation_timer(8.0)

    menu:
        "I propose crustaceans and every creature in the sea hold hands until the end of time!":
            hide screen ch3_boss_negotiation_timer
            jump ch3_boss_negotiate_mc_opt1

        "I propose that the crustaceans apologize to everyone in sea!":
            hide screen ch3_boss_negotiation_timer
            jump ch3_boss_negotiate_mc_opt2

        "I think this might be a great addition to your red collection! (Give red seaweed)" if has_red_seaweed:
            hide screen ch3_boss_negotiation_timer
            jump ch3_boss_negotiate_mc_opt3

label ch3_boss_negotiate_mc_timeout:
    hide screen ch3_boss_negotiation_timer
    show goby annoy:
        full
        center
    show mc shock_hu:
        full
        right
    gob "Time's up! You hesitated, dirtwater!"
    mc "W-wait! I have an answer! Don't poke me with the spear!"
    hide mc
    hide goby
    jump ch3_boss_negotiate_mc_opt1

label ch3_boss_negotiate_mc_opt1:
    show mc default:
        unpose
        full
        right
    with moveinleft
    show goby default:
        unpose
        full
        center
    with moveinright
    gob "..."
    gob "Unlike a defect breed like you.."
    gob "We have no hands you speak of"
    gob "All we have are chelipeds"

    show mc o:
        full
        right
        surprise
    mc "But you're not even a crustacean! What you have are fins!"

    show goby surprise:
        full
        center
    gob "...!"

    show mc o:
        full
        unpose
        right
    mc "If you can command an army of crustaceans"
    mc "If you can hold the empress' great chelipeds.."

    show mc pout:
        full
        right
    mc "What makes you stop at holding other fishes' fins..?"

    show mc default:
        full
        right
    mc "Besides.. Goby fishes have relatives in freshwater!"

    show goby default:
        full
        center
    gob "I'm not a part of that filthy kind."
    gob "You think you're so smart because you've read a few books?"
    gob "Save those futile fun facts for afterlife"
    hide goby
    hide mc
    jump ch3_boss_negotiate_mc_after

label ch3_boss_negotiate_mc_opt2:
    show mc o:
        unpose
        full
        right
    with moveinleft
    show goby default:
        unpose
        full
        center
    with moveinright
    mc "Everyone we met seemed really sad because of what the crustaceans did.."
    mc "Some lost their families. Some are scared to even leave their homes."

    show mc happy:
        full
        right
    mc "Therefore, saying sorry would be a good start?"
    mc "Maybe then they all would be kind and respect you too"

    show goby surprise:
        full
        center
        surprise
    gob "The audacity!"
    gob "You demand an apology from the rulers of the sea?"

    show mc pout:
        full
        right
        surprise
    mc "But order isn't supposed to make everyone scared!"

    show goby annoy:
        full
        center
    gob "What the sea thinks is never worth our concern!"
    hide goby
    hide mc
    jump ch3_boss_negotiate_mc_after

label ch3_boss_negotiate_mc_opt3:
    show mc happy:
        full
        unpose
        offscreenleft
    show mc default:
        right
    with moveinleft
    show goby surprise:
        unpose
        full
        center
    with moveinright
    gob "...!"
    gob "That's.. The great empress' favorite!"

    show teto laugh:
        unpose
        full
        centerleft
        surprise
    with moveinright
    show goby surprise:
        full
        centerright
    with move
    emp "DID SOMEONE SAY RED SEAWEED?!"

    show mc default:
        full
        right
        surprise
    mc "Mhm! I picked it up on the way here! As a peace offering!"

    show teto laugh:
        full
        unpose
        centerleft
    emp "How thoughtful! Gimme it!"

    play sound "audio/sfx/attack_1.mp3"
    "At the blink of an eye with a discreet bang! The seaweed vanished.. Now already a crushed victim under the shrimp's eager munch teeth"

    show goby annoy:
        full
        centerright
    gob "Your Majesty, please remember that they are here to negotiate."
    emp "I know! I can eat and listen at the same time."
    emp "munch munch munch…"

    show mc shock:
        full
        unpose
        right
    "Did she use her pistol to steal the seaweed from my hand without injuring me?"

    show mc o:
        full
        right
    "Whatever it was, I need to see it again! Maybe I should provoke her more?"

    show goby default:
        full
        centerright
    gob "Ah your majesty- there's a seaweed on your cheek"
    emp "Really?! Help me get rid of it my Gobby!"
    gob "Affirmative.."

    show mc happy:
        full
        right
    mc "Yaaay true love wins!"

    show mc excited:
        full
        right
        surprise
    mc "Which means Freshwater and Saltwater can live together in peace now!!"

    show goby surprise:
        full
        centerright
        surprise
    gob "T-true love-?!"
    hide goby
    hide teto
    hide mc
    
    jump ch3_boss_negotiate_mc_after

label ch3_boss_negotiate_mc_after:
    show goby surprise:
        unpose
        full
        centerright
    with moveinright
    gob "We have to obliterate these scums at once, Your Majesty"

    show teto gun_smirk:
        unpose
        full
        centerleft
    with moveinright
    emp "Hah! Count me in on the fun! I've got to test my new found!"

    show goby default:
        full
        centerright
    gob "My empress, I'm afraid these filth isn't worth your power…"

    show teto pout:
        full
        centerleft
        surprise
    emp "Hmph! But I wanna use my brand new golden toy!"

    "Ms Empress Shrimp pulls out what it seems a golden scale from under her robe. Its shimmer glistens in rainbows under the light."

    show mc shock:
        unpose
        full
        right
    with moveinleft
    mc "The golden scale.. she really has it"

    show teto gun_smirk:
        full
        centerleft
    show goby struck:
        full
        centerright
    gob "Then unleash nightmares that follows them to hell, Your Majestic Majesty"

    show cory side_close:
        unpose
        full
        leftish
    with moveinleft
    show teto gun_smirk:
        full
        centerright
    with move
    show goby default:
        full
        rightish
    with move
    cory "Looks like we have no choice but to fight fins and gills, ay?"
    jump ch3_boss_battle

label ch3_boss_battle:
    show cory talk:
        full
        leftish
    cory "Hah that means nothing, we got one ourself too! Show em guppy!"
    emp "Oh-ho! Well that makes it the more interesting…!"
    emp "May the best gold bearer wins! Spoiler: it is I, most obviously!"

    hide mc
    hide cory
    hide teto
    hide goby

    call empress_duel

    if _return != "win" and duel_result != "win":
        jump ch3_boss_battle_lose
    
    $ ch3_empress_defeated = True
    play music "audio/bgm/chap_3_night.ogg"
    jump ch3_ending

label ch3_boss_negotiate_as_cory:
    show cory talk:
        unpose
        full
        leftish
    with moveinleft
    show goby default:
        unpose
        full
        centerright
    with moveinright
    gob "You got exactly 1.8 seconds."

    show cory surprise:
        full
        leftish
    cory "...!"
    cory "Might as well say fugu off with your bullcarp shrimp regime-!"

    show goby surprise:
        full
        centerright
    gob "Enough! That was more than 3 seconds!"

    play sound "audio/sfx/attack_3.mp3"
    "My eyes widen into saucers as it registers a flash of red." 
    "The goby's spear grazes past Mr.Cory, tearing through flesh but missing anything vital. A warning, and nothing more."

    show cory hurt:
        full
        leftish 
    cory "Guh-!"

    show mc shock_hu:
        unpose
        full
        right
    with moveinleft
    mc "Mr. Cory…!!"

    show mc shock_hu:
        full
        right
        surprise
    mc "WHY WOULD YOU SAY THAAAT MR CORYYY!!"

    show teto default:
        unpose
        full
        center
    with moveinright
    emp "Oooh a rebel I sense?!"
    emp "Kekeke! That bravery of yours, I quite like it!"
    emp "It'll make your screams echo all the sweeter."

    show goby annoy:
        full
        centerright
    gob "Now face agonizing torture, worth three lifetimes over, dirtwater."
    hide goby with moveoutright

    show scy sepet:
        unpose
        full
        rightish
    with moveinleft
    scyllarus "Frankly! I don't think I can defend you on this one, my questionable friend!"

    jump ch3_boss_battle

label ch3_boss_negotiate_as_scyllarus:
    show goby surprise:
        unpose
        full
        centerright
    with moveinright
    show scy default:
        unpose
        full
        leftish
    with moveinleft
    gob "Make it count, Scyllarus."
    gob "I'm only hearing you out because you're our precious strongest personnel"

    show goby default:
        full
        centerright
    gob "Having you against us will be disadvantageous for both of us."

    show scy default_om:
        full
        leftish
    scyllarus "I'll make it justifiable!"
    hide scy
    hide goby
    menu:
        "We propose a future where freshwater creatures are no longer detained simply for existing in the sea":
            jump ch3_boss_scy_opt1

        "We propose that the crustaceans rule with honor again, not fear!":
            jump ch3_boss_scy_opt2

        "Calm yourself down first your highness!(Give red seaweed)" if has_red_seaweed:
            jump ch3_boss_scy_opt3

label ch3_boss_scy_opt1:
    show goby default:
        unpose
        full
        centerright
    with moveinright
    gob "Oh? You'd bring numbers to a fight, Scyllarus?"

    show scy default_om:
        unpose
        full
        leftish
    with moveinleft
    scyllarus "By statistics! Seafolks' crime rates are still higher than the freshwater immigrants!"
    scyllarus "With that data in mind.. we shouldn't have detained freshwaters for simply setting fins into sea!"
    scyllarus "And to keep punishing an entire species for the sins of a few is neither just, nor even strategic!"

    show goby annoy:
        full
        centerright
    gob "Even when those are facts.."
    gob "You can't dismiss that incident.."
    gob "In which disaster were caused by those filthy freshwaters?"
    gob "Fishes, mollusks, our own kind — all of them paid for what happened at the Old Canal Junction."
    gob "What we're doing are simply precautions"
    gob "So tragedy doesn't repeat itself…"

    show scy default:
        full
        leftish
    scyllarus "But that was 10 years ago, general!"
    scyllarus "Longer than both you and the empress' ages combined!"
    scyllarus "I was there when it happened…"
    scyllarus "And it was also a freshwater that helped me through that time…"
    
    show scy default_om:
        full
        leftish
    scyllarus "So don't tell me they're all the villains in this story!"
    scyllarus "I refuse to believe that anymore!"
    hide scy
    hide goby
    jump ch3_boss_negotiate_scy_after

label ch3_boss_scy_opt2:
    show goby default:
        unpose
        full
        centerright
    with moveinright
    show scy shy:
        unpose
        full
        leftish
    with moveinleft
    scyllarus "It truly pains me to say this but…!"
    scyllarus "We were once honored, loved. Well mannered."

    show scy default_om:
        full
        leftish
    scyllarus "Crustaceans are of the supportive, enthusiastically kind!"

    show scy shy:
        full
        leftish
    scyllarus "Our way of showing it might come off as rough but..!"

    show scy default_om:
        full
        leftish
    scyllarus "It is necessary to fight for the things we care for!"

    show scy default:
        full
        leftish
    scyllarus "Now all I've seen from seafolks are that of disdain and fear of us.."
    scyllarus "Is that really what our kind wants to be known as..?"
    scyllarus "A ruthless, impudent dictatorship that easily tramples the life of others..!"
    gob "You talk all high and mighty.."

    show goby disgust:
        full
        centerright
    gob "Yet how many died pleading at your own claws, Scyllarus?"

    show scy surprise:
        full
        leftish
    scyllarus "....!"
    scyllarus "That's why I…!!"

    show goby annoy:
        full
        centerright
    gob "Your fierce claws.. are not made for compassion is it?"
    gob "You're a killing machine."
    gob "One that would swipe through anything in its path, crustacean or not, if ordered to.."
    gob "You're not one to propose for harmony."

    show scy sepet:
        full
        leftish
    scyllarus "..."

    show mc pout:
        unpose
        full
        right
    with moveinleft
    mc "YOU'RE WRONG!!"

    show goby default:
        full
        centerright
    gob "oh..?"

    show mc holdcry:
        full
        right
        vibrate
    mc "Mr. shrimp- Mr.. Mr Sc... Cy.. Clarus has never once hurt me!"

    show cory talk:
        unpose
        full
        leftish
    with moveinleft
    show scy sepet:
        full
        center
    with move
    show goby default:
        full
        rightish
    with move
    cory "It's Scyllarus, guppy…"

    show scy default:
        full
        center
    show mc sad_hu at mc_left
    mc "He always touches me super carefully! I've never got any scratches, see!"

    "I extended both arms outwards, showing off every unscratched, unbruised inch of them."

    show mc sad:
        full
        right
    mc "He's.. he's … always trying his best to not hurt anyone…"
    scyllarus "....guppy"

    show cory smile:
        full
        leftish
    cory "What they said!"
    cory "Our big ol friend here is not what you claim a killin machine!"
    cory "He's just stuck under a regime he can't escape from.."

    show cory talk_hu:
        full
        leftish
    cory "He's not killin for fun, it was yous who put the weapon in his claws in the first place!"

    show scy shy:
        full
        center
    scyllarus "Cory…!"

    show goby disgust:
        full
        rightish
    gob "Foolish dirtwaters! You just haven't witnessed his true side yet!"

    show mc happy:
        full
        right
    mc "Maybe so! But.. I trust the side of him I have seen!"
    hide goby
    hide scy
    hide mc
    hide cory
    jump ch3_boss_negotiate_scy_after

label ch3_boss_scy_opt3:
    show scy smile:
        unpose
        full
        leftish
    with moveinleft
    scyllarus "My friend here picked out the brightest, freshest red seaweed for you to feast!"

    show teto laugh:
        unpose
        full
        centerright
    with moveinright
    emp "Oh ho ho don't mind if I do~!!"
    emp "Mmmn.. this is why you're the best Scyllarus..!"

    show goby surprise:
        unpose
        full
        rightish
    with moveinright
    gob "He's the best…? But your highness you told me that I'm-"

    show goby disgust:
        full
        rightish
    gob "sigh.. please don't play favorites in front of the enemy, your majesty."

    show teto default:
        full
        centerright
    emp "shh what does he have to say! Speak my esteemed soldier Scyllarus!"

    show scy default:
        full
        leftish
    scyllarus "Right now.. we are at a compromised position, your majesty.."
    scyllarus "The seafolks hates and fear us, the freshwaters no longer trust us either.."

    show scy default_om:
        full
        leftish
    scyllarus "This isn't a war we can win by claws and fear alone!"

    show scy default:
        full
        leftish
    scyllarus "So with that in mind.. I propose that.."
    scyllarus "We go back to Her Majesty the VII's system.."

    show scy default_om:
        full
        leftish
    scyllarus "We earn the sea's trust instead of demanding its fear!"

    show teto upset:
        full
        centerright
    emp "My.. mother?!"

    show teto upset:
        full
        centerright
        vibrate
    emp "YOU FOOLISH SAND-FILLED BRAIN LUDICROUS IMBECILE!!"

    show teto gun_upset:
        full
        centerright
    emp "I'm sick of it! My mother's softness cost us everything, and you want me to make that same mistake?!"

    show teto gun_upset:
        full
        centerright
        vibrate
    emp "CRUSTACEANS!! Detain them at once!"
    hide teto
    hide scy
    hide goby
    jump ch3_boss_negotiate_scy_after

label ch3_boss_negotiate_scy_after:
    hide teto
    show goby default:
        unpose
        full
        centerright
    with moveinright
    gob "This is exactly why you were never fit to be a general."
    gob "Sand for brains, One sob story from a guppy and you fold like a cheap net."
    gob "That's not honor, Scyllarus. That's just being easy to manipulate."

    show scy default_om:
        unpose
        full
        leftish
    with moveinleft
    scyllarus "I'd rather be wrong for believing in people than right for fearing them!"

    hide goby with moveoutright
    show teto default:
        unpose
        full
        centerright
    with moveinright
    emp "Heh! Time to answer the most asked question then!"
    emp "The ultimate showdown…!!"

    show mc excited:
        unpose
        full
        right
    with moveinleft
    mc "Oh my oh my!"

    emp_mc "PISTOL SHRIMP VS MANTIS SHRIMP!! YOU WON'T BELIEVE WHO WINS?? (GONE WRONG)"

    show teto gun_smirk:
        full
        centerright
    emp "KEKEKEKE!! Oh how I adore you! Too bad I gotta kill you now!"

    show cory upset:
        unpose
        full
        right
    with moveinleft
    cory "Aye! This is no play guppy! Get your ass ready for a fight!"
    hide mc
    hide scy
    hide cory
    hide teto

    call empress_duel

    if _return != "win" and duel_result != "win":
        jump ch3_boss_battle_lose
    
    $ ch3_empress_defeated = True
    play music "audio/bgm/chap_3_night.ogg"
    jump ch3_ending
    jump ch3_ending

label ch3_boss_battle_lose:
    hide scy
    show teto gun_smirk:
        unpose
        full
        centerleft
    with moveinright
    emp "KEKEKE!! I thought you would've last longer!"
    emp "I'm too overpowered for insignificant freshies!"

    show goby default:
        unpose
        full
        centerright
    with moveinright
    gob "None other shall dare defy the great crustacean empress regime, anymore"

    menu:
        "Try again?":
            jump ch3_boss_battle
        "Return to reef":
            jump ch3_night_explore.loop