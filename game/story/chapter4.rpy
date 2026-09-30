label chapter4_start:

    $ current_chapter = 4
    $ current_cycle = "day"
    $ current_area = "ocean_festival_day"

    hide mc
    scene ch4_day
    with fade
    
    play music "audio/bgm/chap_2_day.ogg" volume 0.4
    play ambience "audio/ambience/crowd_01.mp3" loop fadein 1.0 volume 0.3

    $ focus()
    $ focus()
    show cory smile:
        full
        unpose
    show cory smile:
        unpose
        rightish
        toleft
        walkloop(0.5, 0.5, 1)
    with moveinleft
    show shrimp default:
        unpose
        full
        leftish
        walkloop(1, 1, 1)
    with moveinleft
    cory "The water sure feels easier to breathe now that she's gone huh?"
    hide shrimp default

    show shrimp sepet:
        unpose
        full
        leftish
        walkloop(1, 1, 1)
    scy "Really?! *sniff sniff* I feel the quality of water remains the same!"
    fish1 "SCYLLARUS!!! IM A BIG FAN HI"
    fish2 "THANK YOU FOR BRINGING HER DOWN SCYLLARUS!!"

    show cory smile2:
        full
        rightish
    show scy surprise:
        unpose
        full
    show scy surprise:
        leftish
        jump(windup=0.15, power=0.45, airtime=0.35)
    scy "HUH-! Oh! Yes, why of course the pleasure is mine, dear seafolks!"

    fish1 "Good luck on whatever you're doing scyllaruus!!"
    fish2 "Yeah!! We love you!"

    show scy shy:
        unpose
        full
    show scy shy:
        leftish
    scy "R-right..! Good luck to all of you too!"

    "The two fishes swims away, giggling to themselves after greeting Mr Larus."

    show cory smile_hu:
        full
        unpose
        rightish
    cory "hah someone's getting famous ay?"

    show mc happy at mc_left, jumpmc(windup=0.1, power=0.55, airtime=0.4)
    mc "hehe people love you now Mr. Slarus!"

    show scy default_om:
        unpose
        full
        leftish
    scy "It's Mr.Scyllarus! And.. I'm still trying to get used to it..!"
    show scy sepet:
        unpose
        full
        leftish
    scy "It's odd having strangers wave at you.."

    show cory smile:
        full
        unpose
        rightish
    cory "Yeah the seafolks' have been all the more peaceful.."
    show cory talk_hu:
        full
        unpose
        rightish
    cory "We still oughta keep our eyes for the golden fish though"
    cory "Could be anywhere in this vast ocean"

    show scy smile at npc_right
    scy "Yea! There's no way it could be right behind us.."

    show cory surprise at cory_left, jump(windup=0.1, power=0.6, airtime=0.4)
    cory "Speaking of… isn't that the golden fish?"

    show mc shock at mc_left, jumpmc(windup=0.1, power=0.5, airtime=0.35)
    mc "whauh?! Where?"

    show cory talk at cory_left
    cory "right behind you guppy"

    play sound "audio/sfx/splash.mp3"
    "A brilliant rainbow-golden glimmer flashes right behind us, darting through the water at impossible speed towards a massive golden gate ahead!"

    show mc excited at mc_left
    mc "ah! c'mon sir fishes! after it!!"

    $ focus()
    show mc excited at mc_left, walkto(offscreenright, steps=5, walktime=1.5)
    pause 1.5

    jump ch4_day_explore

label ch4_day_explore:

    $ current_area = "golden_village_gate"

    hide mc
    scene ch4_festival_day
    with dissolve
    $ focus()
    show cory upset at cory_left, shake
    cory "aw shrimp! Damn fish must be Usailfish Bolt or something"

    show mc happy at mc_left, jumpmc(windup=0.1, power=0.45, airtime=0.35)
    mc "it's okayy mr Cory :DDD, We'll get it next time!!"

    show scy sepet at npc_right, bowleft(depth=1)
    scy "How are we supposed to find the damn fish among all these gold… wait.. hold on.. Where are we??"
    show scy sepet at npc_right, unpose

    show cory side at cory_left
    cory "I don't know but this place gives me the heebie-jeebies, stay close guppy we don't know what's ahead of us"

    show mc excited at mc_left, vibrate(intensity=2)
    mc "Look! Maybe those mr fishes would know where we are, let's ask them! :DD"
    $ focus()

    hide cory
    hide scy
    hide mc
    with dissolve

label ch4_npc_explore_hub:

    call screen ch4_npc_exploration
    $ ch4_npc_choice = _return

    if ch4_npc_choice == "rin":
        jump ch4_talk_rin
    elif ch4_npc_choice == "leo":
        jump ch4_talk_leo
    elif ch4_npc_choice == "proceed":
        jump ch4_start_chores
    else:
        jump ch4_npc_explore_hub

label ch4_start_chores:

    $ current_area = "festival_preparation_grounds"

    hide mc
    scene ch4_festival_day
    with dissolve

    $ focus()
    show mc happy at mc_left
    mc "Okay! Let's help out with the festival chores so we can find the golden fish tonight!"

    show cory talk at cory_left
    cory "Sounds like a plan. Let's see what needs fixin' or gatherin' around here."

    $ focus()
    hide cory
    hide mc
    with dissolve

label ch4_chore_explore_hub:

    call screen ch4_chore_exploration
    $ ch4_chore_choice = _return

    if ch4_chore_choice == "chore1":
        if ch4_chore1_done:
            show mc happy at mc_left
            mc "We already fetched plenty of radiant seaweeds and corals for the sacred statue!"
            hide mc
            with dissolve
            jump ch4_chore_explore_hub
        else:
            jump ch4_chore1_seaweed

    elif ch4_chore_choice == "chore2":
        if ch4_chore2_done:
            show mc happy at mc_left
            mc "The festival stalls and timber frames are already all built and sturdy!"
            hide mc
            with dissolve
            jump ch4_chore_explore_hub
        else:
            jump ch4_chore2_stand

    elif ch4_chore_choice == "feast":
        jump ch4_dinner_incident

    else:
        jump ch4_chore_explore_hub

label ch4_dinner_incident:

    $ current_cycle = "afternoon"
    $ current_area = "golden_village_pavilion"

    hide mc
    scene ch4_festival_day
    with dissolve

    $ focus()
    show mc happy at mc_left, surprise
    mc "Mr whaaale, we're done! :D"

    rin "Oh praise the mother of sea.. Aren't you as swift as an arrow?"
    rin "We are truly grateful for your assistance!"

    mc "Yaaa no problem!"

    show mc excited at mc_left
    mc "Soo when will the festival start? Is the food ready :o"

    rin "Fufu"
    "Mr whale slips out a tiny chuckle at my impatience. Is starvation something that amuses him? >:T"

    rin "Rest assured my child, we have prepared a forethoughtful spread for all of you, come."

    "I nodded gleefully, drooling at the mouth while skipping behind mr whale's enormous tail"
    "We then arrive at a super big table, it looks like it could serve two whale sharks!"
    "Yet as my gaze fell down to the contents, I scrunched up in disappointment."
    show mc pout at mc_left

    show cory proud at cory_left
    cory "bloodworms?! Didn't know you were fancy like that mr chief sir."

    show scy proud at npc_right
    scy "Hah! Talk about a banquet!"

    rin "Yes of course, we prepare this with every species' likings in mind"

    show mc o at mc_left
    mc "Are there.. any.. fried fishes?"

    show cory surprise at cory_left, jumpmc(windup=0.1, power=0.45, airtime=0.45)
    pause 0.45
    show cory surprise at cory_left
    cory "...???"
    show cory surprise at cory_left

    leo "Oh dear the cat's out of the bag~"

    cory "Guppy… you wouldn't eat me would ya?! I'm made of bones and pigments!"

    show mc shock at mc_left
    mc "mn nonono! I mean! Like.. tuna or.. Salmon or.. fried catfish maybe?"
    mc "Don't fishes eat other fishes too..? Mr whale shark your diet is small fishes right? Mackerel.. and.."

    leo "Mhm that's right, whale sharks eat baby fishes too.. As well shrimps"

    show scy surprise at npc_right, jumpmc(windup=0.1, power=0.7, airtime=0.5)
    pause 0.5
    scy "Did someone say shrimp?!"
    show scy surprise at npc_right

    show mc pout at mc_left
    mc "and mr.. mr scyllarus too you.. you eat crabs.. Supposedly!"

    scy "A-are you suggesting I would eat my own comrades..?!"

    mc "But it's how nature is…!"
    
    show rin surprise
    rin "…"
    "My confused stare bore back into my own at tenfolds. Meanwhile Leo just sits there in the corner unbothered."
    "Her unreadable smile felt like a wash of relief and support amongst the overwhelmingly rigid tension."

    show rin o
    rin "My apologies young one.. Our village had long forbid such extreme practice…"
    rin "While there are fishes that are still… what I would describe as crassly primitive"
    show rin o #with sink animation??? idk whichever fits this best
    rin "We do not condone of such unvirtuous behavior around here"
    
    show rin smile
    rin "The best we can provide for your appetites are.. Jellies made algaes"

    show mc pout at mc_left
    mc "....okay."

    show rin talk
    rin "Do… rest yourselves until tonight. Before the parade begins."
    show rin o
    rin "Please excuse me."

    ".............................."

    leo "You know guppy, I can indulge you in some.. fishes that suits your taste"

    show cory upset at cory_left
    cory "In front of my bloodworms?!"

    leo "Oh I might be talking about you, Corydoras.."

    show mc shock at mc_left
    mc "I wouldn't-! No, I wouldn't eat my friends!"

    leo "Would you now?"
    leo "Let's ask the consensus~!"
    leo "Starting from you, Doras~! Are you just now imagining our beloved protagonist's tiny sharp teeth chewing away on you?"

    show cory side at cory_left
    cory "Nah of course not! You're just trying to rile things up! I ain't falling for that"

    leo "Hmm~ But your fins.. I saw them tremble just now.."

    cory "They're just a kid! If they want anything from me I could still defend myself from-"

    show scy proud at npc_right
    scy "That's right! If the situation came to that.. my claws are ready to stop your nibbles!"

    show mc holdcry at mc_left
    mc "I.. *sniff* I'm not hungry anymore…"

    play sound "audio/sfx/splash.mp3"
    show mc holdcry at mc_left, walkto(offscreenleft, steps=6, walktime=1.2, bounce=0.25, sway=0.2)
    pause 1.2
    hide mc
    "Stands up and runs away."

    leo "Hmm, folded too fast."

    $ focus()
    jump ch4_night_explore

label ch4_night_explore:

    $ current_cycle = "night"
    $ current_area = "isolated_coral_corner"

    hide mc
    scene ch4_deeptalk
    with fade
    play music "audio/bgm/chap_4_night.ogg" volume 0.4
    play ambience "audio/ambience/ambience_windy_night.mp3" loop fadein 1.0 volume 0.3

    $ focus()
    $ focus()
    play sound "audio/sfx/sigh_01.mp3" volume 0.4
    "I managed to find myself a quiet space to pond over everything."
    "The swaying of anemones and glowing corals calms me down a little."
    "I sat somewhere far from where my friends are to calm myself down"
    "Until suddenly a fish sat down beside me. It's a catshark"

    show mc holdcry at mc_left
    mc "*sniffles* w-wauh?"

    ori "meow"

    show mc o at mc_left
    mc "m.. meow?"
    mc "hello.. Miss..ter cat shark..?"

    ori "mhm."

    "The chained cat shark despite its scary jailbreak appearance offers me a square shaped jelly that looks like a failed assasination attempt of a character?"

    ori "sepombop"

    mc "spongebob..?"

    ori "sepombop"

    show mc happy at mc_left
    mc "is it for me…? Thank you…"

    ori "welcome."

    "I carefully took the wiggly jelly into my mouth. It tasted a little like strawberry and weird algae chemical"

    ori "... I've been there.."

    show mc o at mc_left
    mc "mm? Been.. where exactly?"

    ori "been under."

    mc "under where? :o"

    ori "I made you said underwear."

    mc "...??? Pfft- ahahahah! What was that!!"

    ori "heh."
    ori "Why are you alone? Saw you with friends. Big shrimp. and freshwater and smiley Seal."

    show mc pout at mc_left
    mc "I.. mn.. I said.. something that might've offended them.."

    ori "...?"

    show mc o at mc_left
    mc "have you.. eaten fishes in your life?"

    ori "mm. have…"

    mc "Do you think it's wrong for predator fishes to eat other fishes?"

    ori "..."

    mc "well.. I don't think it's wrong.. because that is the way nature intended us to be.. the weak gets hunted."
    mc "but it also doesn't mean.. we eat our friends because their species is in our diet.. like! If you had a pet chicken, you wouldn't eat it right? Even if.. chickens are considered food to a lot of predators.. even if we eat chickens often."

    ori "mm.. chickens..? Some kind.. new fish?"

    show mc happy at mc_left
    mc "ah nono they're a living creature that's.. like a bird!"

    ori "bird..?"

    show mc o at mc_left
    mc "oh.. right you're a seabed shark.."

    ori "mm but.."

    mc "...?"

    ori "but if a pet sees you eat the same kind as what they are.."
    ori "It would be scared of you too. Distrust."
    ori "will think. What if I'm next?"

    show mc pout at mc_left
    mc "mnnn… but I would never do thaaat! D:"

    ori "mm even so. Will still think that. In the back of mind."
    ori "If I tell. I eat human daily. Would you.. think of me eating you in the back of mind?"

    show mc o at mc_left
    mc "....mn would but.. wouldn't make me scared of you"

    ori "bizarre.."

    $ focus()

    menu:
        "Is eating fishes the reason you're all chained up?":

            $ focus()
            ori "it's-"
            leo "why helloooo there friends~!"
            show mc shock at mc_left
            mc "waugh?! Leo!"
            leo "mhm yes yes it is i~"
            leo "I've just been wooondering where you've been.."
            "A tiny boop to my nose"
            leo "After the whole debacle there.. I'm worried my friend here might fall into a deeeeep hole of overthinking and sadness.."
            leo "so I came to check up~!"
            show mc default at mc_left
            mc "mmn.. am fine, leo."
            mc "I made a friend!"
            leo "Oho? Another friend? How exciting~!"

        "can I pet you misster cat shark":
            $ focus()
            ori "you may"
            show mc happy at mc_left
            mc "really?? You're okay with it? No hard feelings?"
            ori "mean it."
            "as the cat shark lowers its head for me,"
            mc "hehehe you can purrrrrr~!! Good.. boy good girl good thing!"
            ori "meow"
            leo "How fun~! May I join in on the pet fest?"
            show mc shock at mc_left
            mc "waouh-! Leo!"
            leo "mhm, yes it is i~"
            leo "I see you made a little friend"
            leo "Are you feeling okay? No more hungry for fish?"
            show mc pout at mc_left
            mc "Mno.. I should be more.. Considerate"
            leo "I don't think it's your fault, we all have our appetites"
            leo "I eat fishes, penguins on a daily basis too, you know~!"
            leo "don't let anyone stop you from eating what you want, little guppy."
            ori "bad advice…"
            

    "Leo closely inspects the cat shark, twirling a 360 around it with an inquisitive hum"

    leo "Hmm, those chains I've seen it before.."
    leo "Ah I remember now~! You're that one fugitive that went on a cannibalistic rampage~!"
    leo "Guess we all have something in common huh?"

    show mc shock at mc_left
    mc "???"

    ori "that's hyperbole.. and I've changed."
    leo "You can't change what you've been born with kitty~!"

    ori "I wasn't…! Condition made me do-"

    leo "now now, you hear that? Festival's about to start"

    "In a sudden moment I was ushered by the seal"

    leo "bye kitty shark we'll see you laaater~!"

    show mc shock at mc_left
    mc "wauh! Where are you taking me??"

    leo "To your friends, you silly eely billy. They've been worried"

    $ focus()
    jump ch4_festival_night

label ch4_festival_night:

    $ current_area = "night_festival_grounds"

    hide mc
    scene ch4_night
    with dissolve
    play ambience "audio/ambience/crowd_01.mp3" loop fadein 1.0 volume 0.3

    $ focus()
    show cory upset at cory_left
    cory "Guppy! Where the eel have ya been??"

    show mc o at mc_left
    mc "Nowhere! I was just.. Staring at the glow in the dark anemones"

    show scy surprise at npc_right
    scy "Have you filled your stomach with anything?!"

    show mc default at mc_left
    mc "I ate.. some square jelly?"

    show scy default at npc_right
    scy "A jelly is not a proper diet for a developing guppy like you!"

    show cory side at cory_left
    cory "We brought you smashed krills…"

    show scy proud at npc_right
    scy "Yes! I helped with the smashing of course!"
    scy "I made sure it's digestible for your throat!"

    show cory talk at cory_left
    cory "It's the least we can do to fulfill your appetite.."

    show mc o at mc_left
    mc "... for me? You really didn't have to..! After what i.. said"

    show scy smile at npc_right
    scy "Cory also said that he's sorry!"
    scy "But he didn't want to tell it yet before Preparing something grand or something along the line for a proper apology."
    scy "But I think you should know it guppy! I apologize too.."

    show cory surprise at cory_left
    cory "I'm right here?!"

    show cory side at cory_left
    cory "but.. *siiigh* exactly what he said"

    show cory side_close at cory_left
    cory "We're sorry for the way we reacted.."
    cory "We just wanna let you know that.. we're not afraid of ya guppy"

    show cory fond at cory_left
    cory "You're our friend."

    show scy laugh at npc_right
    scy "KAKAKA That's right Cory! And Friends protect each other! Forever!"

    show mc shock at mc_left
    mc "friends.."

    "I nodded, a relieved smile creeping up my face. I can't believe I got to the point where I made such kind friends like this.. I don't know how to react, this was a first."

    show mc happy at mc_left
    mc "Mm! Mr Cory.. Mr Scyllarus You're my friends.. Too!"

    show mc default at mc_left
    mc "Thank you for.. Not being mad and yelling at me.."

    "Looking around I noticed that someone's absent presence"

    show mc o at mc_left
    mc "Ah but where's mr chief whale shark..?"

    "Mr Cory shrugged"

    show cory side at cory_left
    cory "Went somewhere, he looks busy"

    show mc pout at mc_left
    mc "But.. he promised he'll help with searching!"

    show scy smile at npc_right
    scy "Yes! But he told us to have fun and enjoy the festival!"
    scy "Maybe then he'll help us after the festival!"

    leo "then fun we shall have~!"

    show cory surprise at cory_left
    cory "GYAH-!! Don't just sneak up on us!"

    leo "Aw, have some whimsy would you?"
    leo "Ah, also look forward to the end of this festival~!"
    leo "They say a sacred ritual will be held"

    show mc excited at mc_left
    mc "Waouh, really?? Can't wait to see!"

    $ focus()
    jump ch4_festival_hub

label ch4_festival_hub:

    $ current_area = "night_festival_plaza"

    scene ch4_festival_night
    with dissolve

    call screen ch4_festival_night_exploration
    $ ch4_night_choice = _return

    if ch4_night_choice == "game1":
        if ch4_game1_done:
            show mc happy at mc_left
            mc "We already won plenty of prizes at the Krill Catch stall!"
            hide mc
            with dissolve
            jump ch4_festival_hub
        else:
            jump ch4_minigame_plankton

    elif ch4_night_choice == "game2":
        if ch4_game2_done:
            show mc happy at mc_left
            mc "We already hit all the clam targets at the Shell Shooter booth!"
            hide mc
            with dissolve
            jump ch4_festival_hub
        else:
            jump ch4_minigame_shooting

    elif ch4_night_choice == "ritual":
        jump ch4_night_ritual

    else:
        jump ch4_festival_hub

label ch4_climax:

    hide screen ch4_affection_hud
    hide mc
    scene ch4_night
    with dissolve
    stop ambience fadeout 1.0
    play ambience "audio/ambience/unsettling_01.mp3" loop fadein 1.0 volume 0.4
    $ focus()
    "At the ledge of the great abyss, multiple glowing effigies are cast into the dark void by the seafolks, tumbling downward into the deep sea."
    play ambience "audio/ambience/gemuruh_3.mp3" noloop volume 0.45

    "Then suddenly, amongst the multiple thrown effigies I noticed something glows a bright gold."
    play ambience "audio/ambience/riser_gemuruhketinggi.mp3" noloop volume 0.5
    "Not the kind of gold that Mr. Rin uses.."
    "Not the kind of gold that the effigy has"

    show expression Transform("ch4_dialogue_night", zoom=1.5, xalign=0.5, yalign=0.8) as zoomed_abyss
    with dissolve
    play ambience "audio/ambience/mysterious_golden_looking.mp3" loop fadein 0.5 volume 0.65

    "But that rainbow radiant.. shimmering glow"
    "In that moment, everything else were a blur."

    show mc serious at mc_left
    with dissolve

    mc "I must get it.. I must get it, I must have it, no matter.. what!"

    "Papa always told me to catch anything that looks interesting"
    "He always brings back home cool fishes"
    "So maybe if I bring it home, this time he'll-!"

    play sound "audio/sfx/splash.mp3"
    play sound "audio/sfx/wind_riser.mp3" volume 0.5
    hide mc
    with dissolve

    scene black with fade
    stop music fadeout 2.0

    "There were faint shouts ringing in the back of my head."
    "Amidst all of them, the loudest ones sounded familiar"
    "Before I knew it, I was already falling"

    $ focus()

    $ ch4_chapter_complete = True

    jump chapter5_start
