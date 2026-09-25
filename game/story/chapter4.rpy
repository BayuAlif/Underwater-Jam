default ch4_scy_affection = 0
default ch4_cory_affection = 0
default ch4_leo_affection = 0

default ch4_chore1_done = False
default ch4_chore2_done = False
default ch4_chore1_companion = None
default ch4_chore2_companion = None

default ch4_game1_done = False
default ch4_game2_done = False
default ch4_game1_companion = None
default ch4_game2_companion = None

default ch4_ritual_companion = None
default ch4_chapter_complete = False

label chapter4_start:

    $ current_chapter = 4
    $ current_cycle = "day"
    $ current_area = "ocean_festival_day"

    hide mc
    scene ch4_day
    with fade

    show cory talk at cory_left
    cory "The water sure feels easier to breathe now that she's gone huh?"

    show scy default at npc_right
    scy "Really?! *sniff sniff* I feel the quality of water remains the same!"

    fish1 "SCYLLARUS!!! IM A BIG FAN HI"

    fish2 "THANK YOU FOR BRINGING HER DOWN SCYLLARUS!!"

    show scy surprise at npc_right
    scy "HUH-! Oh! Yes, why of course the pleasure is mine, dear seafolks!"

    fish1 "Good luck on whatever you're doing scyllaruus!!"

    fish2 "Yeah!! We love you!"

    scy "R-right..! Good luck to all of you too!"

    "The two fishes swims away, giggling to themselves after greeting Mr Larus."

    show cory smile at cory_left
    cory "hah someone's getting famous ay?"

    show mc happy at mc_left
    mc "hehe people love you now Mr. Slarus!"

    show scy proud at npc_right
    scy "It's Mr.Slarus! And.. I'm still trying to get used to it..!"
    scy "It's odd having strangers wave at you.."

    show cory side at cory_left
    cory "Yeah the seafolks' have been all the more peaceful.."
    cory "We still oughta keep our eyes for the golden fish though"
    cory "Could be anywhere in this vast ocean"

    show scy smile at npc_right
    scy "Yea! There's no way it could be right behind us.."

    show cory surprise at cory_left
    cory "Speaking of… isn't that the golden fish? "

    show mc shock at mc_left
    mc "whauh?! Where?"

    show cory talk at cory_left
    cory "right behind you guppy"

    play sound "audio/splash.mp3"
    "A brilliant rainbow-golden glimmer flashes right behind us, darting through the water at impossible speed towards a massive golden gate ahead!"

    show mc excited at mc_left
    mc "ah! c'mon sir fishes! after it!!"

    jump ch4_day_explore

label ch4_day_explore:

    $ current_area = "golden_village_gate"

    hide mc
    scene ch4_dialogue
    with dissolve

    show cory upset at cory_left
    cory "aw shrimp! Damn fish must be Usailfish Bolt or something"

    show mc happy at mc_left
    mc "it's okayy mr Cory :DDD, We'll get it next time!!"

    show scy sepet at npc_right
    scy "How are we supposed to find the damn fish among all these gold… wait.. hold on.. Where are we??"

    show cory side at cory_left
    cory "I don't know but this place gives me the heebie-jeebies, stay close guppy we don't know what's ahead of us"

    show mc excited at mc_left
    mc "Look! Maybe those mr fishes would know where we are, let's ask them! :DD"

    "An enormous whale shark towers the three of us."

    show mc happy at mc_left
    mc "Helloooo!! Good morning sir :D wao you're so biiiiig!!"

    rin "Ah-! Goodness Gracious!"
    rin "Oh just a guppy aren't you.. Scared the teeth out of old me.."

    show mc o at mc_left
    mc "oops hehe my bad..!"

    rin "No matter, Youth need not apologize for simply... being young"

    menu:
        "Have you seen a golden fish around?":
            show mc o at mc_left
            mc "We saw it but we lost it amongst these.. Golds you have piled up!"
            rin "A Golden fish, you say..?"
            "Mr Whale Shark's great eye drifts slowly toward the mountain of gold ornaments piled around him, as though sifting through decades of memory rather than metal."
            rin "Mm. I believe... I may have seen such a thing"
            show mc excited at mc_left
            mc "Really?! Can you tell us?"
            rin "Now, now. Need not to hurry young one."
            show mc pout at mc_left
            mc "Mnn but I need to know now.. Before it goes further :("
            rin "Patience will reward you grand.."
            rin "We're currently having trouble with a festival that's going to occur tonight.."

        "Why's there so many gold here? Are you a gold thief :o":
            show mc o at mc_left
            mc "Why's there so many gold here? Are you a gold thief :o"
            rin "Thief? Oh no, no you have it wrong.."
            rin "I'm too old to be fretting about wealth.."
            rin "These golds will be used for an upcoming festival."
            rin "Golds are believed to stray away evil and bad omens, young one"

    show mc o at mc_left
    mc "A festival..?"

    show mc excited at mc_left
    mc "Will there be lots of food? I haven't eaten in a while"

    rin "Oh why of course a big feast will occur!"
    rin "It's only fitting for a festival this important."

    show cory talk at cory_left
    cory "What's the festival about if we may know, sir?"

    rin "Yes, a dire one."
    rin "It's a festival that we held up once a year to ward off evil and bad luck"
    rin "It's the least we can do to repay the ocean.."
    rin "However, the sea has been quite turbulent lately, so we were forced to change plans and decided to host it twice a year instead."
    rin "But we completely underestimated how long gathering materials would take…"
    rin "... now we're worried we won't finish in time if the festival is held tonight."
    rin "That's why, as much as I'd love to help with you search, I can't assist you."

    show mc happy at mc_left
    mc "Alright then we'll help you!"

    rin "Oh how wonderful! The people thank you for your benevolence."
    rin "Rest assured travelers, we will be preparing the best of meals for your help."

    show cory smile at cory_left
    cory "About time we fill our stomachs.."

    show scy proud at npc_right
    scy "Don't fret my friend we shall be of assistance! As much as we can!"

    play sound "audio/bush_rustling.mp3"
    leo "Greetings~!"

    show mc shock at mc_left
    mc "waouh-!"

    "I stumbled backwards for Mr Larus to catch me, a super tall figure cast shadows over us."

    show scy surprise at npc_right
    scy "Careful now!"

    leo "Mmhehe my apologies for the spook, friend.."
    leo "You're searching for the golden fish, yes?"
    leo "Sparkling rainbow, lush tail.."

    show mc excited at mc_left
    mc "Yes yes you're right!! Super spot on!"

    leo "I can be of your aid I assure you~!"
    leo "You just have to follow me!"

    show cory side at cory_left
    cory "Hold your seahorses!"

    menu:
        "How did ya know we're lookin for it?":
            cory "How did ya know we're lookin for it?"
            leo "Mmm.. it's no science, I've seen you go around asking about it.."
            leo "Like a little ballerina in a broken music box~"
            leo "Round and round you go, same question, same steps, same tune.."
            leo "Doesn't it make you dizzy?"
            show mc default at mc_left
            mc "mmn.. No! Because if I get dizzy.."
            mc "Mr. Cory and Mr. Larus will help make it go away!"
            mc "So I have nothing to worry about!"
            leo "I like your answer~!! Always so refreshing!"

        "How do we know ya really know of the fish's whereabouts?":
            cory "How do we know ya really know of the fish's whereabouts?"
            leo "Mm but until now.. you've been blindly following clues from strangers too right?"
            leo "What makes it different from what I said?"
            show scy smile at npc_right
            scy "He's right my friend, Cory! We have each other, it'll all be fine!"
            show mc happy at mc_left
            mc "Mhm yaa mr Cory you worry too much"
            mc "More than both of my parents combined.."
            show cory upset at cory_left
            cory "Ugh.. maybe you're right my bad…"
            cory "Dunno what got to me"
            "Mr Cory looks like he's got a lot in mind"

    leo "Besides, the ocean's my playground~!"
    leo "I know it like the back of my hand..."
    leo "Which means i get to join your fun little party yes?"

    show mc happy at mc_left
    mc "Yaa! Welcome aboard miss…?"

    leo "Leo is fine~! Leo Drurga"

    show mc o at mc_left
    mc "Drurga.. :o"
    "The surname tickles something familiar in the back of my brain. Yet I can't really pinpoint what"

    show scy proud at npc_right
    scy "We welcome you to our thrilling little search party, comrade!"

    leo "My oh my this would be spiiine tingling~!"
    leo "Ah but I doubt we can go into searching right away.."
    leo "Not when the chief's having trouble.."
    leo "He'll go whiny about how much help they require for the festival…"

    jump ch4_chore1_seaweed

label ch4_chore1_seaweed:

    $ current_area = "gathering_grounds"

    hide mc
    scene ch4_dialogue
    with dissolve

    rin "May you be of aid with gathering seaweeds and corals young one?"

    show mc excited at mc_left
    mc "Sure! Are the colors up to us to pick?"

    rin "Yes, yes whatever pigment caught your eyes most.."
    rin "We need them to decorate the sacred statue"

    mc "Yaaay okay! I'll bring lots for you!"

    hide mc
    call screen ch4_companion_select(
        "Choose who to gather seaweeds with!",
        "Each companion offers a unique bonding moment"
    )
    $ ch4_chore1_companion = _return

    if ch4_chore1_companion == "scy":
        jump ch4_chore1_scy
    elif ch4_chore1_companion == "cory":
        jump ch4_chore1_cory
    else:
        jump ch4_chore1_leo

label ch4_chore1_scy:

    show scy proud at npc_right
    scy "Lay it on me!! My eyes are good at picking the freshest of seaweeds!"

    show mc o at mc_left
    mc "I've always been curious.. How do you see the with your super revolutionary 12 colored vision?"

    show scy smile at npc_right
    scy "It's Scyllarus! And.. hmm!"
    scy "Perhaps we can play a little game, my comrade"

    show mc excited at mc_left
    mc "A game?! What game? I wanna play! :D"

    scy "I spy with my little eyes!"
    scy "I believe it would be easier for you to understand!"

    mc "ooo okay! I go first"
    mc "I spyyyy with my little eyeeees..!"

    menu:
        "A bunch of swaaaying red branch-y guys":
            scy "Hm! A plumose coraline!"
            show mc happy at mc_left
            mc "ding ding ding you're spot on! So cool o.o"
            show scy proud at npc_right
            scy "Through these eyes of mine, red is a very prominent contrast color!"
            scy "It's all lustrous and shiny for me!"
            mc "Like… in a kaleidoscope?"
            scy "I'm not sure of this kaleidoscope you speak of!"
            scy "But if it reminds you of said thing perhaps you're right KAKAKA!"
            mc "Hehe maybe I can try and find you one mr Syllarus! I'm sure you'll love it!"
            "I wonder if he'll get dizzy and faint if he were to see a kaleidoscope from the overwhelming colors he would see.. Can shrimps faint from eyestrain I wonder… :o"
            scy "Even so.. I can't distinguish between what others call.. yellow orange and orange.."
            scy "Most of my vision goes to UV sightings!"
            "Mr Scyllarus then looks over to the queued dancing corals. Grazing them with a careful gentle sway of his claw."
            scy "And! this coral in particular is my mom's favorite.."
            show mc o at mc_left
            mc "really? :o"
            scy "When I was little I kept bringing her home tens of them everyday!"
            scy "And she always put them up on the walls like medals.. each and everyone of them"
            show mc pout at mc_left
            mc "Mnn.. but when I do it you scold me! >:T"
            show scy default at npc_right
            scy "Now, now! Back then corals were overgrown! And I didn't know any better either!"
            scy "We're at the time of scarcity little guppy! Everyone's greedy!"

        "A big… strooong colorful hard shelled creature with a super strong punch!":
            $ ch4_scy_affection += 1
            show scy surprise at npc_right
            scy "Big.. colorful hard shelled.. Super strong…"
            scy "It can't be…!"
            scy "Is mother sea so concerned about my superior kind they invent a new special worth of becoming our true rival?!"
            scy "Where is it?! I must see this for myself!"
            show mc happy at mc_left
            mc "pfft hehe nonono! It is you Mr Scyllarus!"
            show scy proud at npc_right
            scy "Oh…!"
            scy "Hah! Well I must say I'm quite the charming and strong mantis shrimp myself!"

    show scy default at npc_right
    scy "We're getting a little sidetracked here! Come on guppy fetch the glowing red ones!"

    show mc pout at mc_left
    mc "glowing..? But I can't see the glooow Mr Larus! :("

    scy "Oh right! Fine, I shall guide you through it then!"

    $ ch4_chore1_done = True
    jump ch4_chore2_stand

label ch4_chore1_cory:

    show cory talk at cory_left
    cory "Plucking seaweeds? I got ya guppy!"
    cory "Which colors are we pickin?"

    show mc excited at mc_left
    mc "Mmm I like orange..! And blue.. Oh oh pink coral too! And a little bit of pastel purple.."

    show cory smile at cory_left
    cory "Woah you got a whole palette over there…!"
    cory "But hey I dig orange too"

    show mc happy at mc_left
    mc "yay! Let's pick on the oranges one first then :D"

    "Me and Mr. Cory took our time in picking the best fluorescent color of the seaweeds"

    show cory side at cory_left
    cory "You know.. pickin corals and seaweeds like this"
    cory "Is it quite comforting yeah?"

    menu:
        "Mm! It's like… plucking fleas from a wild cat.":
            show cory unimpressed2 at cory_left
            cory "Flea plucking? Mane you're into bizarre hobbies aren't ya?"
            cory "what the eel is even a flea?"
            show mc pout at mc_left
            mc "But the satisfaction that you freed a little creature from its parasitic agony is nice!"
            mc "And and you also get to torture the little mean fleas! So they don't do more harm"
            show mc o at mc_left
            mc "Is it really odd..?"
            show cory side at cory_left
            cory "Ay don't with that face.. I meant good!"
            show cory smile at cory_left
            cory "The weird in people is what makes the world challengin and fun"
            show cory smile_hu at cory_left
            cory "And as long as you're doin it for good.. I ain't got a problem with"
            mc "Mm.. I get called weird lots.."
            mc "You're the first to tell me that weird is good, Mr Cory!"
            cory "Those jerks are just envyin ya, they dont have as much \"personality\" as you do"
            cory "Being the norm is boring anyway, livin the same way everyone does.."
            cory "Way about a dead monochrome world.."
            show cory fond at cory_left
            cory "Stay weird little guppy, I mean it."

        "Mm! It's like drawing!":
            $ ch4_cory_affection += 1
            show cory talk at cory_left
            cory "Drawing huh..? You an artist?"
            show mc happy at mc_left
            mc "Mhmm! I draw in my free time! I draw the fishes I see and document them! Their behavior and details like that"
            show cory proud at cory_left
            cory "*whistle* You never cease to amaze me"
            show mc excited at mc_left
            mc "Yaa other than to be a fish, I also want to be a book author! And and a marine biologist!"
            mc "I wanna document all my finds and draw them myself"
            mc "So people can appreciate water creatures more!"
            show cory side at cory_left
            cory "The more I realize just how well you'd get along with her"
            show mc o at mc_left
            mc "her? :o mm ms gator?"
            show cory side_close at cory_left
            cory "Nah ain't her.. I know a sunshine little fishie just like you"
            cory "She loves makin stuff with seaweeds like these"
            show mc excited at mc_left
            mc "ooo I'd love to meet her! Where is she now? We should let her join in our adventure too!"
            cory ".... she's not with me anymore guppy"
            cory "she's somewhere.. In this vast ocean"
            show mc o at mc_left
            mc "oh.. will.. you be able to meet her again?"
            cory "Doubt it. Even then I'm not too sure if she'd be happy to see me after what happened.."
            mc "If she means that much to you then I think she'll appreciate seeing you again?"
            cory "hah.. what do ya know guppy.. appreciate it though"

    show cory talk at cory_left
    cory "Alright I think this much's plenty!"

    show mc happy at mc_left
    mc "Mhm! We got oraaange and pink and yellow and"
    mc "Can we get the 30 of the purple ones oo Mr.Cory?"

    show cory unimpressed at cory_left
    cory "No can't do, guppy that's enough"

    $ ch4_chore1_done = True
    jump ch4_chore2_stand

label ch4_chore1_leo:

    leo "Ooo hehe how fun~! I like picking flowers"
    leo "Tell me what's your favorite flower, little guppy?"

    show mc o at mc_left
    mc "Mmm.. I often see and pick lots of wildflowers on my walks.. So it's probably it!"

    leo "Wildflowers huh..? How very fitting of you~!"

    menu:
        "What about you? What's your favorite flower?":
            $ ch4_leo_affection += 1
            leo "Hmm.. I think it would be.. the Night shade.. Familiar?"
            show mc o at mc_left
            mc "No I don't think I've heard of it.. What's it like?"
            leo "Ah it's a flower of gorgeous purple shade.. My favorite part? The little flecks of yellow in the center"
            show mc happy at mc_left
            mc "Yellow and purple… it's complementary colors right? I can see why you find them pretty :D"
            leo "ding ding ding~! You're right! Very perceptive aren't you?"

        "Are you going to eat me? :o":
            leo "Eat you…? Oh no, humans were never on the menu"
            leo "What rumors have you been hearing, hm?"
            show mc o at mc_left
            mc "I heard that sea leopards can eat humans if they want!"
            leo "While it might be paaaartially true.. Doesn't mean I'm eating every human I see.."
            leo "My appetite lies in quenching curiosity, guppy"
            show mc happy at mc_left
            mc "Mm! I totally get it, the satisfaction of knowledge is incomparible!"

    show mc o at mc_left
    mc "Ah! we're getting a little sidetracked here.."

    leo "Mhehe it's fine we're allowed to have fun every now and then no?"
    leo "Just sit back and relax little guppy.. I know you've been through a lot.."

    show mc pout at mc_left
    mc "Mnn.. but we can't slack off can we?"
    mc "The festival is just.. tonight! um.. How many hours til then?"

    leo "Hmm counting time would do us no fun.."

    mc "But but the golden fish! It'll stray super far too if we take long :("

    leo "Would you believe me If I were to say that.."
    leo "The goldenfish.. It moves only when you move."

    show mc shock at mc_left
    mc "Huh? So when I'm in one place it'll always be nearby?"

    leo "Mhm, just a theory though.. a sea theory"

    $ ch4_chore1_done = True
    jump ch4_chore2_stand

label ch4_chore2_stand:

    $ current_area = "stall_construction_site"

    hide mc
    scene ch4_dialogue
    with dissolve

    rin "Can I trust your hands on assembling these materials into stalls, young one?"

    show mc o at mc_left
    mc "mm I can try..! But I'm going to need a hand from my friends."

    rin "Do whatever shall make this easier for you."
    hide mc
    call screen ch4_companion_select(
        "Choose who to build the stands with!",
        "Each companion offers a unique bonding moment"
    )
    $ ch4_chore2_companion = _return

    if ch4_chore2_companion == "scy":
        jump ch4_chore2_scy
    elif ch4_chore2_companion == "cory":
        jump ch4_chore2_cory
    else:
        jump ch4_chore2_leo

label ch4_chore2_scy:

    show scy laugh at npc_right
    scy "Kakaka, deal then, guppy!"

    show mc happy at mc_left
    mc "Yayay let's work together mr Cy–Clarus-"

    scy "I'll set up the stall, you handle the decorations, understood!!"

    show mc excited at mc_left
    mc "Ay ay captain!!"

    "Mr. Shrimp worked insanely efficient. Like machines, even."

    show mc shock at mc_left
    mc "WOAH that's zippy!!"

    show scy proud at npc_right
    scy "Ha! Of course, I've been drilling under her highness since I was a mere kid!"
    scy "This is nothing… but duck soup!"

    show scy sepet at npc_right
    scy "...."

    "Despite his boastful words, I could catch him… less energized?"

    show mc o at mc_left
    mc "... Um you don't seem like yourself, Mr. Shrimp.."

    show scy surprise at npc_right
    scy "...? Am I?"
    scy "I'm running on all cylinders!!"

    show mc pout at mc_left
    mc "No, no, that's not what I meant at all."

    "Mr. Shrimp pauses, his movement coming into a sudden halt."

    show scy default at npc_right
    scy "I don't know. Feels like.. I'm losing my drift sometimes!"
    scy "Guess what im trying to say is…  it feels strange when im no longer in duty?"
    scy "Hard to even function like a normal seafolk."

    show mc o at mc_left
    mc "Oooo…."

    scy "Once this journey ends, I got no clue where the current's supposed to take me."

    menu:
        "Take your time, Mr. Shrimp!":
            $ ch4_scy_affection += 1
            show mc happy at mc_left
            mc "I don't know how it feels… to lose your purpose,"
            mc "I don't know how you're feeling right now…"
            mc "But the ocean is huge! And we're travelling around right now."
            mc "Maybe what you need to do is… finding out what you actually like doing."
            mc "Or maybe you could just stick around with me forever! Problem solved :D"
            show scy surprise at npc_right
            scy "...! THATS A BRILLIANT OBSERVATION GUPPY!"
            show scy laugh at npc_right
            scy "Kakaka! I'll bear that in mind."

        "You should be grateful, Mr.Shrimp!":
            show mc happy at mc_left
            mc "Not working means more time to play!"
            mc "Other grown ups have to work every single day and they look suuuper tired,"
            mc "So you should be grateful and happy :D"
            show scy smile at npc_right
            scy ".. yeah. Yeah, you're right!"
            scy "Guess I'm just out of the line of fire and complaining about the weather!"
            scy "Bad look on me, guppy!"

    "The stand is finally completed."

    show mc excited at mc_left
    mc "WOAHH this turned out way cooler than i thought!"

    show scy proud at npc_right
    scy "Hmph!! I'll call this… a crustaseanship!!"

    show mc happy at mc_left
    mc "With.. guppy's assistance :D!"

    $ ch4_chore2_done = True
    jump ch4_dinner_incident

label ch4_chore2_cory:

    show cory talk at cory_left
    cory "Ay, gimme a hand with this frame, guppy!!"

    show mc excited at mc_left
    mc "Waouh on it!"

    show cory smile at cory_left
    cory "Aand here. Hold this ends steady when i tie the knots."

    mc "Moremoremore mr. Cory!!"

    cory "Woah easy there, you're really excited, huh?"

    show mc happy at mc_left
    mc "Mhm! this is my first festival ever,"
    mc "Have you ever been to a festival, Mr Cory?"

    show cory side at cory_left
    cory "Ay… used to spend days around the Samba festival…"

    show mc o at mc_left
    mc "Samba festival? What's that??"

    show cory talk at cory_left
    cory "Ah, it's an annual celebration back Down in the Southern Reefs."
    cory "Wild stuff. You got fishfolks dancing around in these massive glowing anemone suits.."

    show mc shock at mc_left
    mc "MASSIVE ANEMONES?"

    cory "Yeah. Massive, vibrant, glowing anemones.."
    cory "And sea percussion pounding so hard you could feel the vibration through your fins."
    cory "Type shrimp you don't forget easily,"

    show mc happy at mc_left
    mc "Oooh I'd like to visit your house someday! :D"

    show cory side_close at cory_left
    cory "Well… aint sure about that, guppy."
    cory "Truth is, I haven't stepped back home in a long while."

    show mc o at mc_left
    mc "Why?? :0"

    cory "It's because my sis-ay nevermind."
    cory "My siblings… they all made something big of themselves."
    cory "One's a freshwater guard commander, another runs a pearl merchant."
    cory "And there's me, just drifting around, taking whatever odd jobs I can find."
    cory "Feels like if i show my face back home like this… I'd be just a disappointment… "

    menu:
        "Well, isn't that just natural?":
            show mc o at mc_left
            mc "If you siblings are doing great and you're just doing odd jobs.."
            mc ".. it's natural that you feel a bit disappointed, right?"
            show cory side at cory_left
            cory ".....yeah."
            cory "Hearing this straight from a little kid hits hard…"
            cory "But you aint wrong, guppy."

        "Im sure your family waits for you":
            $ ch4_cory_affection += 1
            show mc happy at mc_left
            mc "I don't think your family cares about your job, Mr. Cory."
            mc "If it were me, I'd just be happy to see you come home safe and sound."
            show cory surprise at cory_left
            cory "....!"
            show mc excited at mc_left
            mc "AND! I want to go dance at that Samba festival with you someday…"
            mc "..so you have to go make up with your family first!"
            show cory side_close at cory_left
            cory "............"
            cory "HIC, guppy my little baby guppy…"
            cory "*Sniff* Thank you.. I needed to hear that.."

    "The stand is finally completed."

    show mc happy at mc_left
    mc "Phew! My arms are completely dead… but we actually pulled it off!"

    show cory smile at cory_left
    cory "Ay, we are the dream team, guppy."

    $ ch4_chore2_done = True
    jump ch4_dinner_incident

label ch4_chore2_leo:

    leo "Hee hee! Lets construct this stand together~"

    show mc excited at mc_left
    mc "Mhm. Time to roll!"

    "We set to work side-by-side, joining the timber as the midday light filtered through the festival grounds."

    show mc o at mc_left
    mc "Just a fleeting thought…"
    mc "... but isn't the name 'Leo' usually belonging to suuper famous people!?"
    mc "Like Leonardo da Vinci! Leo Tolstoy! Leonel Messi! "

    leo "It's.. Lionel~"

    show mc shock at mc_left
    mc "Hum yeah!! Wait, how do you even know about Mr. Lionel Messi :0"

    leo "Hee-hee~ never overlook my knowledge, twin~"

    "Leo glides into action with sleek grace.. With surprising power in those long flippers."
    "Joint pegs are hammered and heavy timber snaps into place."
    "I guess this isn't the first time for Leo building the stand?"

    menu:
        "Have you participated in this festival before Miss Leo?":
            leo "... pretty much~"
            leo "All the seafolk… so many seafolk…"
            leo "Tail in tail through their little festival life~"
            leo "Pretending its all about helping each other~"
            show mc o at mc_left
            mc "Pretending..? :0"
            leo "Ah, what i mean is… purely selfless virtue is merely an illusion~"
            leo "Strip away the smiles, and at the end of the day, every single creature.."
            leo "... is ultimately carving their path through their own current~."
            show mc pout at mc_left
            mc "mnn you mean that… everyone is living only for the things they like?"
            mc "That's not true, at all! You can clearly see how genuine my friends are with me :D"
            leo "Hee hee. If you say so~"

        "You're so cool :0":
            $ ch4_leo_affection += 1
            leo "Hee-hee~ you're fully capable of this, too, twin~"
            leo "Or well.. You could, if you weren't so accustomed… "
            leo "... to having your fin held through every tiny wave~"
            show mc o at mc_left
            mc "Um… but mr cory and mr shrimp are just helping me out."
            leo "Of course, of course~"
            leo "I'm suggesting it's not good to always rely on someone else,~"
            leo "How will you ever survive when you're on your own~"
            show mc shock at mc_left
            mc "Gulp……."

    "The stand is finally established."

    show mc happy at mc_left
    mc "That's actually pretty easy!"

    leo "See? I told you that you've got it in you~"

    $ ch4_chore2_done = True
    jump ch4_dinner_incident

label ch4_dinner_incident:

    $ current_cycle = "afternoon"
    $ current_area = "golden_village_pavilion"

    hide mc
    scene ch4_dialogue
    with dissolve

    show mc happy at mc_left
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

    show cory proud at cory_left
    cory "bloodworms?! Didn't know you were fancy like that mr chief sir."

    show scy proud at npc_right
    scy "Hah! Talk about a banquet!"

    rin "Yes of course, we prepare this with every species' likings in mind"

    show mc o at mc_left
    mc "Are there.. any.. fried fishes?"

    show cory surprise at cory_left
    cory "...???"

    leo "Oh dear the cat's out of the bag~"

    cory "Guppy… you wouldn't eat me would ya?! I'm made of bones and pigments!"

    show mc shock at mc_left
    mc "mn nonono! I mean! Like.. tuna or.. Salmon or.. fried catfish maybe?"
    mc "Don't fishes eat other fishes too..? Mr whale shark your diet is small fishes right? Mackerel.. and.."

    leo "Mhm that's right, whale sharks eat baby fishes too.. As well shrimps"

    show scy surprise at npc_right
    scy "Did someone say shrimp?!"

    show mc pout at mc_left
    mc "and mr.. mr scyllarus too you.. you eat crabs.. Supposedly!"

    scy "A-are you suggesting I would eat my own comrades..?!"

    mc "But it's how nature is…!"

    rin "…"
    "My confused stare bore back into my own at tenfolds. Meanwhile Leo just sits there in the corner unbothered."
    "Her unreadable smile felt like a wash of relief and support amongst the overwhelmingly rigid tension."

    rin "My apologies young one.. Our village had long forbid such extreme practice…"
    rin "While there are fishes that are still… what I would describe as crassly primitive"
    rin "We do not condone of such unvirtuous behavior around here"
    rin "The best we can provide for your appetites are.. Jellies made algaes"

    show mc pout at mc_left
    mc "....okay."

    rin "Do… rest yourselves until tonight. Before the parade begins."
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

    play sound "audio/splash.mp3"
    "Stands up and runs away."

    leo "Hmm, folded too fast."

    jump ch4_night_explore

label ch4_night_explore:

    $ current_cycle = "night"
    $ current_area = "isolated_coral_corner"

    hide mc
    scene ch4_dialogue_night
    with fade

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

    menu:
        "Is eating fishes the reason you're all chained up?":
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

    jump ch4_festival_night

label ch4_festival_night:

    $ current_area = "night_festival_grounds"

    hide mc
    scene ch4_night
    with dissolve

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

    jump ch4_festival_hub

label ch4_festival_hub:

    $ current_area = "night_festival_plaza"

    hide mc
    scene ch4_night
    with dissolve

    "The night festival is in full swing! Colorful lanterns and glowing corals illuminate stalls across the seafloor."

    menu:
        "Catch planktons at the Plankton Stall" if not ch4_game1_done:
            jump ch4_minigame_plankton

        "Play the Shooting Game at the Clam Booth" if not ch4_game2_done:
            jump ch4_minigame_shooting

        "Attend the Sacred Abyssal Effigy Ritual (Peak of Festival)" if (ch4_game1_done and ch4_game2_done):
            jump ch4_night_ritual

        "Look around the festival" if not (ch4_game1_done and ch4_game2_done):
            "The celebratory music echoes through the water. We need to participate in both festival games before the main ritual begins!"
            jump ch4_festival_hub

label ch4_minigame_plankton:

    $ current_area = "plankton_stall"

    show mc happy at mc_left
    mc "Hello miss stall keeper! How do i-"

    stall1 "Just get as many as ye please"
    stall1 "Me oul self's knackered of having these feckin' loud eejits around"

    planktons "Yaya unana! Fugu you, we hate you too! kew!"

    show mc o at mc_left
    mc "oh okay then!"

    hide mc
    call screen ch4_companion_select(
        "Who should I catch planktons with?",
        "Choose a companion to help manage the hostile critters"
    )
    $ ch4_game1_companion = _return

    if ch4_game1_companion == "scy":
        jump ch4_plankton_scy
    elif ch4_game1_companion == "cory":
        jump ch4_plankton_cory
    else:
        jump ch4_plankton_leo

label ch4_plankton_scy:

    show scy proud at npc_right
    scy "Hah! Plankton catching is a discreet hobby of mine!"
    scy "We shall be victorious guppy!"

    show mc o at mc_left
    mc "Mn but can you catch them without crushing them with your big claws?"

    show scy default at npc_right
    scy "... I uh do you need them alive?"

    menu:
        "Ya I do! I want to show them off to everyone!":
            show scy sepet at npc_right
            scy "Hmm! I don't think letting these pesky critters out is a wise choice..!"
            planktons "we will krill everyone! World conquer!"
            scy "My mantis radar senses something.. Sacrilegiously immoral within their tiny bodies!"
            show mc o at mc_left
            mc "Mm you're right :o why are you so full of hate, tiny planktons?"
            planktons "Kill kill kill! hatred!! Corrupt world! uana yaha!"
            scy "They're too consumed by hate of how the world cruelly treats them!"
            scy ".... Hah.. to think I was serving someone of the same mindset.."
            scy "To think I was.. At one point no different than these spiteful creatures.."
            show mc happy at mc_left
            mc "Mm.. But you're not who you were Mr larus!"
            mc "I don't sense anymore hate from you!"
            show scy proud at npc_right
            scy "I'm grateful to have your trust!"
            scy "But sometimes.. I still-"
            planktons "Yaha naha murder! kill kill everyone! Dismemberment!!"
            "Mr Clarus's face scrunched up into an uncontent expression. It looks like he's reminiscing a nightmare.."
            show scy sepet at npc_right
            scy "..."
            show mc o at mc_left
            mc "Mr.. Scyllarus?"
            scy "I'm fine..! Mother of sea.. Why must they have such foul mouths!"

        "Mmno, I want to feed it to you!":
            $ ch4_scy_affection += 1
            show scy surprise at npc_right
            scy "For me…?!"
            scy "Well.. big shrimps like me don't eat critters like these anymore!"
            show mc o at mc_left
            mc "Ooo so you ate heaps of these when you were little..?"
            show scy proud at npc_right
            scy "Yes! My trainers told me that they're full of nutrients to ensure a healthy strong body!"
            scy "They made me eat thousands of them everyday!"
            show mc shock at mc_left
            mc "Thousands..?! Wouldn't that be overfeeding..?"
            show scy default at npc_right
            scy "Uhh or was it hundreds! I don't remember too well"
            scy "But it all gets burned in the rigorous training I have to endure!"
            scy "So all the planktons will eventually build me muscles! Inside out!"
            show mc o at mc_left
            mc "Do the taste of planktons.. Haunt you Mr. Scyllarus..?"
            scy "Hah! I won't let such measly little organisms haunt me!"
            planktons "We're your worst nightmare!! Eat brains!"
            show scy sepet at npc_right
            scy "Maybe a tiny bit..!"
            show mc happy at mc_left
            mc "Oh okay.. I won't feed it to you then"
            mc "I'll get you something tastier later me Carus!"
            show scy surprise at npc_right
            scy "It's Scyllarus!! Why does it gets worse everytime?!"

    "Mr Scyllarus carefully scoops the vengeful tiny planktons, before tilting them into a plastic bag looking like jellyfish."
    "The gentle gesture fully contradicts his sharp giant claws"

    show mc happy at mc_left
    mc "Hehe I never thought you could be this gentle!"

    show scy proud at npc_right
    scy "I.. try my best to!"

    $ ch4_game1_done = True
    jump ch4_festival_hub

label ch4_plankton_cory:

    show cory side at cory_left
    cory "There sure is a lot of stuff huh.. buncha nautical nonsense."

    show mc pout at mc_left
    mc "They're not nonsense Mr. Cory!"
    mc "The one that looks like an isopod is an amphipod it's a type of macroplankton!"
    mc "And that over there are copepods, they filter out tiny algae and feed the larger krill!"
    mc "Plus, over in that corner, there's-"

    show cory talk at cory_left
    cory "Yea yea yeah, just tell me which one's your favorite.."

    menu:
        "Get the jellyfish lookalike!":
            $ ch4_cory_affection += 1
            show cory smile at cory_left
            cory "Fan of Jellyfishes I see."
            show mc happy at mc_left
            mc "Mhm! They're all so.. floaty and pretty"
            cory "Yeah I totally get it, I used to try and catch em too when I was little."
            cory "Until one day karma bit me in the fins.."
            show mc shock at mc_left
            mc "Oh no did you get stung??"
            cory "Damn right I did.. it left me a permanent imprint."
            planktons "serve you right freshie!! Get stung more!"
            show cory unimpressed at cory_left
            "Mr. Cory scoops up most of the planktons into his fin, topping it with his other fin."
            "The gesture reduced their complaints into tiny screams.. they sound like chipmunks trapped in a bottle."
            show cory side_close at cory_left
            cory "At that time I was cryin so loud it put a smile to my.. little sister who's been sick all week.. "
            cory "It was her first smile in a while.."
            cory "Hah.. and I couldn't help but think it's all worth it in the end."
            show mc happy at mc_left
            mc "You're a great kind older brother, Mr.Cory!"
            mc "I wish you were my papa…"
            show cory surprise at cory_left
            cory "Hah.. if I'd known you sooner I probably would.."
            cory "Wait.. that sounded wrong"
            show mc excited at mc_left
            mc "yaa! Be my papa Mr. Cory! :D"
            "The tiny screeches from Mr. Cory's hands grew louder. It faintly sounded like \"Be their papa!\" chanted repeatedly"
            show cory side_close at cory_left
            cory "I'd.. have to think about it, guppy."

        "The cockroach looking plankton reminds me of you":
            show cory surprise at cory_left
            cory "Me??"
            show mc happy at mc_left
            mc "Ya! if you were a plankton you'd be an amphipod!"
            show cory side at cory_left
            cory "Aye, I ain't that chopped!"
            cory "Well if you were a plankton.. you'd be that one guppy"
            "Mr Cory points at the floating blue button. Its tentacle-like branches swaying peacefully"
            show mc o at mc_left
            mc "The porpita porpita? :o"
            show cory talk at cory_left
            cory "Yep all bright and about.. A little odd looking, the name suits ya too in a way"
            planktons "if the word hate was engraved on every each nanoangstrom of those hundreds of millions of mi-"
            "Mr. Cory scoops up most of the planktons into his fin, topping it with his other fin."
            "The gesture reduced their complaints into tiny screams.. they sound like chipmunks trapped in a bottle."
            show cory smile at cory_left
            cory "These tiny things sure have big mouths, ay?"

    $ ch4_game1_done = True
    jump ch4_festival_hub

label ch4_plankton_leo:

    leo "Catching helpless little beings huh? I'm skilled at that~!"
    leo "We'll catch as many as we can, little guppy"

    planktons "We'll tear your fins flappers to shreds!"

    leo "Wow, feisty are we?"

    menu:
        "Do you eat planktons, Leo?":
            leo "Hmm if I'm bored, yes."
            leo "I like the feeling of them crawling their futile way about my innards.."
            leo "It sure is a tickling feeling~! Like drinking carbonated water"
            show mc o at mc_left
            mc "Ooo like drinking soda? Now I'm curious.."
            leo "Why don't you try some?"
            show mc pout at mc_left
            mc "Me..? Would I get a tummy ache from it? :("
            leo "You won't find out unless you try~"
            leo "I'm sure your golden treasure there would protect you from harm"
            mc "Are you sure…?"
            leo "Mhm~! here, let me help you get a herd of it."
            "Leo gathers a huge sum of planktons into his wide flippers. The single celled organisms flitter flutters in disarray, they look like they're panicking."
            planktons "we'll eat your guts!! We'll kill you slowly from inside!"
            show mc shock at mc_left
            mc "gulps…"
            leo "now say ah~"
            mc "mnn…! wait!!"
            leo "Hmm, are you backing out now?"
            mc "I'm not scared..!!"
            leo "Then, where's that unbridled enthusiasm of yours, hm?"
            mc "Can I at least try one or two first..?"
            leo "Mmn no, you won't be able to feel them if it's just one or two"
            leo "Trust me will you~? Or trust in your scale.."
            show mc pout at mc_left
            mc "Nnguh..!! Fine!"
            "Taking a deeeep breath I pushed myself and started drinking from Leo's flippers."
            "I emptied my head, hearing nothing but my forced gulps as the plankton infiltrated water goes down my throat"
            show mc shock at mc_left
            mc "Mnhah-! I.. I drank it!"
            leo "Yaay~! Congratulations to you!"
            mc "Mnnngh.. they taste weeeeeird D:"
            leo "Humans actually benefit from eating these.. they're nutrient rich~!"
            mc "Whauht..?! Really??"
            leo "The tiny critters.. They were just bluffing"
            leo "Like chihuahuas.. All barks and no bite"
            show mc pout at mc_left
            mc "Why didn't you start with that..!"
            leo "I want to see you make faces I haven't seen~"
            leo "Is that so wrong?"
            mc "hmph..!"

        "Why are the planktons so angry?":
            leo "Hmm.. when a creature is weak.. they bark their way into scaring predators away"
            leo "Spewing pointless threats.. yet harboring zero impact."
            leo "Much like a chihuahua, all barks no bite."
            planktons "Don't listen to the lunatic!! We can kill and tear your body inside out!!"
            show mc pout at mc_left
            mc "nnn.. I don't know who to trust.."
            leo "Still don't believe me? Watch this~!"
            "Leo then takes the whole bowl of pond and sucks all the plankton out"
            show mc shock at mc_left
            mc "WAOUH..! Is.. that really okay?? o.o"
            stall1 "Oh thank Jesus, Mary and Joseph! Now we're suckin diesel'!"
            stall1 "I owe ye a peace of my life!"
            leo "hah~ see? Nothing's happening to me"
            leo "Planktons are among the nutrient richest sea food, this applies to humans too."
            show mc happy at mc_left
            mc "You know so much, Leo!"
            leo "Mm why of course I do~"
            show mc o at mc_left
            mc "Ah but now we don't have any planktons to catch.."
            leo "hehe oopsies~ we can find more in the wild later on"

    $ ch4_game1_done = True
    jump ch4_festival_hub

label ch4_minigame_shooting:

    $ current_area = "shooting_booth"

    "Colorful clam shells lined up across four shelves, with five clams on each. Making twenty targets in total."
    "Three squid-shaped, wooden shooters sit firmly on its stand. Apparently it can be fired with a single tap of its coral button."
    "So… I assume winning this is all about adjusting your angle and getting the aim just right."

    show mc o at mc_left
    mc "How does this game work? :0 "

    stall2 "Velkommen, young guppy! Zhe rules are super simple,"
    stall2 "You see zhe shells up there?"
    stall2 "I give you 8 pearl bullets. You shoot down as many clams as you can."
    stall2 "But it only counts if zhe clam actually drops off zhe shelf"
    stall2 "We will tally up your total score at zhe end, and you pick your prize based on your tier!"

    "The stall vendor gestured toward the sign, which was flanked by a sprawling display of prizes."
    "REWARDS."
    "TIER 1 - SEAWEED SNACK (20 points)"
    "TIER 2 - BIOLUMINESCENT BUBBLE BLOWER (40 points) "
    "TIER 3 - BLOBFISH PLUSHIE (80 points)."

    hide mc
    call screen ch4_companion_select(
        "Who should I play the shooting game with?",
        "Choose a companion to take on the target gallery"
    )
    $ ch4_game2_companion = _return

    if ch4_game2_companion == "cory":
        jump ch4_shoot_cory
    elif ch4_game2_companion == "scy":
        jump ch4_shoot_scy
    else:
        jump ch4_shoot_leo

label ch4_shoot_cory:

    show cory talk at cory_left
    cory "Here's the trick to winnin' this, guppy."
    cory "Imagine those clams are the ones who called ya weird."

    "Mr Cory tilted the pistol toward the nearest clam, taking a brief aim before squeezing the trigger."
    play sound "audio/attack_3.mp3"
    "KLANG!"
    "The shot ricocheted off the sea rock, missing the target entirely."
    "Mr. Cory's grin instantly vanished into a frown."

    show cory upset at cory_left
    cory "Tch…"

    "I raised my pistol, lining up the sights of the exact same clam."
    "I held my breath, squeezed."
    play sound "audio/attack_1.mp3"
    "CLANG!"
    "The shell shattered from its perch, tumbling onto the seabed below."

    show mc happy at mc_left
    mc "Don't look back in anger, Mr. Cory :D"

    show cory smile at cory_left
    cory "Ay… alright :D"

    show mc happy at mc_left
    mc "That's it, try again, mr. cory :D"

    "Mr. Cory took aim once more, firing another shot... only for it to clip the edge and glance off into the sand."

    show cory side at cory_left
    cory "..... :D"
    show cory upset at cory_left
    cory "GRRRR mane these sights must be off!"

    menu:
        "Maybe you can try using my shooter.":
            $ ch4_cory_affection += 1
            show mc happy at mc_left
            mc "Mmm.. perhaps it's simply an issue with your pistol, Mr. Cory?"
            mc "Or maybe aiming is just harder over there."
            mc "Try taking a shot with mine, Mr. Cory!"
            "I stepped aside, clearing space so Mr.Cory can commandeer my pistol shooter."
            show cory talk at cory_left
            cory "Aight… imma try."
            "Mr Cory squared his shoulders, locking his sight onto the target."
            play sound "audio/attack_1.mp3"
            "CLANG!!!"
            "The clam fractures on impact, falling from its perch."
            show mc excited at mc_left
            mc "YEEHAW there we are, Mr. Cory!! :D"
            show cory smile at cory_left
            cory "Heh. Heheh."

        "It's a pure skill issue in your part, Mr. Cory :p":
            "I lean in close, taking his hands in mine to physically adjust his grip.."
            leo "Oh, look at you two~ "
            "Leo suddenly appeared from behind, leaning right between us like a shadow."
            show mc shock at mc_left
            mc "Eeek- leo! "
            leo "Fufufu~ here old man, let me help you too~"
            "Leo maneuvered his posture and re-aligned Mr. Cory's elbows with meticulous care."
            show cory upset at cory_left
            cory "Aight AIGHT KIDS, back off, I caught yer drift."
            "Mr Corry pushed the trigger again."
            play sound "audio/attack_2.mp3"
            "BANG-KLANG!"
            "The round strays wild, skipping harmlessly across the rockface. Another miss."
            show mc pout at mc_left
            mc "Augh… so close…"
            leo "Ooof… well, my work here is done. Toodles~"
            "Leo disappeared."
            show cory side at cory_left
            cory ".. well, mane win some, lose some."
            cory "Can't all be sharpshooters out here in the deep, yeah?"

    "With our final shots spent, our little game finally came to an end ."

    stall2 "Three clams down! Not bad, young vones."
    "He hands over a decorated box of dark seaweed sticks."
    "Baked crisp and shaped remarkably like Pocky."

    show cory smile at cory_left
    cory "Eat up, guppy. You earned the lion's share of 'em, anyway."

    show mc happy at mc_left
    mc "Mmm okay :D."

    $ ch4_game2_done = True
    jump ch4_festival_hub

label ch4_shoot_scy:

    show scy proud at npc_right
    scy "I was trained directly under the Empress herself, KAKAKAKA!"

    show mc happy at mc_left
    mc "Pistol-trained under a pistol shrimp to use a pistol. Incredible :0"
    mc "Crustacean first, mr. Clarus!"

    scy "You truly possess a magnificent heart, guppy!"

    "Despite his effortless skill, his claws tremble slightly around the grip."
    "A subtle recoil washes over him with every shot, his face scrunching in discomfort at the sharp crack of gunpowder."
    "As if… he associates that with something awful?"
    "Without missing a beat, he neatly takes down two clams in rapid succession."

    scy "Hah! It's a little unfair if a pro like me were to partake in this child play!"
    scy "Can you do the rest, guppy?"

    leo "Quitting halfway after only two shots~?"
    "Leo suddenly appeared from behind, leaning right between us like a shadow."

    show scy surprise at npc_right
    scy ".....!"

    show mc shock at mc_left
    mc "Leo!"

    scy "It's not like that, missy. Just giving guppy the chance!"

    leo "There's really no shame in conceding if it exceeds your capabilities, though~"

    scy "......!"
    "What should I say?"

    menu:
        "It's alright! If Mr. Laurs can do it, I can do it too":
            $ ch4_scy_affection += 1
            show mc o at mc_left
            mc "Um. So accounting for the cross-current drag, the salinity density…"
            mc "... and the angle of refraction through the water column and and,"
            leo "Also consider the margin percent for shell thickness, relative to the kinetic torque~!"
            show scy default at npc_right
            scy "I don't think you need to overthink it, guppy!"
            show mc excited at mc_left
            mc "Aough yessir!"
            "I pressed the trigger."
            play sound "audio/attack_1.mp3"
            "KLANG! The clam shell shatters off the stall, rumbling backward into the slit below."
            show mc happy at mc_left
            mc "I.. I nailed it!"
            leo "That's supersonic, twin~!"
            show scy laugh at npc_right
            scy "Kakakaka! Splendid trajectory!"

        "Please Mr. Laurs, I want that plushie :’0!":
            show mc pout at mc_left
            mc "Nu uh, I want that plushie, you'll get it for me wont you Mr Larus."
            "Mr. Laurs grimaces, his brow furrowing as he glances back at the pistol."
            show scy default at npc_right
            scy "Of course, who do you think I am, Guppy?"
            "With practiced, mechanical perfection, he fired off five consecutive shots."
            play sound "audio/attack_1.mp3"
            "BANG-KLANG. BANG-KLANG. BANG-KLANG"
            "Five clams shattered off their perches in instant succession "
            show scy sepet at npc_right
            "Mr. Shrimp looked away, breathing heavily."
            show mc shock at mc_left
            mc "Barnacle's eyes, mr. Clyarus!!"
            show scy laugh at npc_right
            scy "KAKAKAKA! This game poses no threat to a distinguished shrimp like me!"

    stall2 "Wunderbar! Wunderbar! Ach, that is a new record for ze booth!"
    stall2 "Zhe plush iz yours young Guppy!"

    show mc excited at mc_left
    mc "Yayyy this is the best day ever!"

    leo "That's actually remarkable~"

    show scy proud at npc_right
    scy "Kekeke! Today was gonna be the day that we brought it back to you, guppy!"

    $ ch4_game2_done = True
    jump ch4_festival_hub

label ch4_shoot_leo:

    leo "Eight shiny little bullets total. Four for each of us, then~"

    show mc happy at mc_left
    mc "Okay! Here Leo, pinnipedia first!"

    "Leo takes the pistol with lazy elegance, tilting the grip sideways at a completely nonchalant angle."
    "Without even closing an eye to aim, she booped the trigger with her head."
    play sound "audio/attack_3.mp3"
    "KLANG!"
    "The clam shell target shuddered violently, but refused to drop."

    show mc shock at mc_left
    mc "Dead center!! It counts, rightright? :D"

    stall2 "Nein, nein! You must knock ze clam completely off ze shelf, ja!"
    stall2 "Merely rattling its hinges gets you zero pointz!"

    show mc pout at mc_left
    mc "Awh… no way.."

    leo "Your turn, guppy~"
    play sound "audio/attack_3.mp3"
    "KLANG! The pearl bullet hit the same clam. But it won't fall."

    show mc pout at mc_left
    mc "Huuh… :/"

    leo "My, my… are you quite certain this mechanism isn't rigged~?"

    menu:
        "It is totally is!":
            $ ch4_leo_affection += 1
            show mc pout at mc_left
            mc "It totally is!"
            mc "Awh I really want the bioluminescent bubble blower :C"
            leo "Worry not my darling. I can still acquire that bioluminescent bubble blower for you~"
            show mc o at mc_left
            mc "Really? You can win me the bubble blower?"
            leo "Hmm-mm. Though you might want to look away for a second~"
            mc "Why, miss leo? :0"
            leo "Because I wouldn't want you to see me doing something terribly improper~"
            mc "Mmmm but you're not doing anything harmful right? :C"
            leo "Oh, no at all~ it's just my secret trick i won't share with anyone~"
            mc "Alright……"
            "I dutifully press both palms over my eyes, squeezing them tight shut."
            "A brief, soft rustle of water follows, accompanied by a suspicious, heavy thud."
            play sound "audio/thump.mp3"
            "CLATTER-BANG-KLANG!"
            show mc shock at mc_left
            mc "Waouh, are we winning?!"
            "I snap my eyes open. Every single clam target on the shelf is now lying facedown on the seabed."
            stall2 "Huh Zhats weird, Must've been za current."

        "Noo it probably it isn't,":
            show mc o at mc_left
            mc "Um the pistol gear is solid. The pearls seem okay."
            mc "Besides, I saw Manta Ray play this exact booth earlier and they knocked some…"
            leo "Is that so? Well then, let's see that aim in action ~"
            show mc excited at mc_left
            mc "Mmmhm. Here I go!"
            play sound "audio/attack_1.mp3"
            "BANG! BANG! BANG! BANG!"
            "Four rapid shots ring out in perfect sequence."
            "Every single remaining clam target shatters clean off the shelf."
            show mc shock at mc_left
            mc "Waough??"
            leo "You're a natural~!"

    stall2 "Congratulationz! You are zhe champions of za day!"
    stall2 "Tier 2, der biolumineszierende seifenblasenbläser!"

    show mc excited at mc_left
    mc "WOO-HOO! We got the uh bioluminezdende seifenblaser!"

    leo "Mhehehe. Bioluminescent bubble blower~"

    "I dipped the wand into the glowing liquid and blew a gentle stream of air through the ring."
    mc "FUUUH!"
    "A cascade of shimmering, bioluminescent bubbles bursts into the air, floating around us and casting neon hues across our faces."
    "Right next to me, a high-pitched, satisfied squeak escapes Leo."
    "She joyfully spins around me, twirling happily through the bubbles."
    leo "Now isn't that just enchanting... Mmhehe~"

    $ ch4_game2_done = True
    jump ch4_festival_hub

label ch4_night_ritual:

    $ current_area = "sacred_ritual_podium"

    hide mc
    scene ch4_night
    with dissolve

    "Mr whale shark chief stepped into a small podium, behind him stood a giant statue made of gold, its sculpture resembles a scary uncanny unknown deep sea monster perhaps?"
    "It looks like it came out straight from a horror book."
    "I wonder if it's based on a real life deep sea creature.. or perhaps just a representation of negativity."

    rin "Dear seafolks, Freshinians… scooters, swimmers, and those who've made it for this Devout Ritual. Welcome."

    leo "Ah it has begun.."

    rin "For years, we, as the goldensea Council, have upheld this tradition. These little vessels shall carry what weighs upon us. Anger. Fear. Regret. Grief. Words left unsaid and thoughts we have carried for far too long."
    rin "Tonight, we give those burdens to the sea. Speak what you wish to leave behind. Let the Abyssal Effigy hear it. Then, when the time comes, we shall send them into the deep together."

    "The crowd merrily cheers at Mr chief's opening speech"

    rin "Settle down. Before we proceed to the final rite, there is one tradition left to observe."
    rin "Tonight, we have come to lay our burdens before the sea, however, no one should have to face this ritual alone. Each of you may choose one person to accompany them through the peak of the festival."

    "Uninteligable murmur from the crowds"

    rin "Once you've chosen your companion, we may begin the first part of our rite. Each of our attendants have been given with a replica of the Abyssal Effigy. Through it, you may channel all the deepest sorrows you carry within. Be it regrets that weigh upon your heart, the fears that haunt you or the worries you hold for what lies ahead."
    hide mc
    call screen ch4_companion_select(
        "Choose your companion for the Abyssal Effigy!",
        "Face the peak of the festival and cast your burdens together"
    )
    $ ch4_ritual_companion = _return

    if ch4_ritual_companion == "scy":
        jump ch4_rite_scy
    elif ch4_ritual_companion == "leo":
        jump ch4_rite_leo
    else:
        jump ch4_rite_cory

label ch4_rite_scy:

    show mc happy at mc_left
    mc "Mr Larus! Let's go together! :D"

    show scy surprise at npc_right
    scy "Me?! Are you sure you want to spend the peak of this festival with me?!"

    show mc happy at mc_left
    mc "Of course!"

    show scy proud at npc_right
    scy "Well, if you insist! Come on, little guppy!"

    "The two of us swam up to one of the attendants handing out the small replicas of the effigies and was given one each."
    "We swam away from the crowd of people and toward the ledge of the deep sea."

    show scy default at npc_right
    scy "So…I guess we're supposed to put our burdens into this creepy statue now!"
    "Mr. Shrimp scratched the back of his head."

    show mc o at mc_left
    mc "Are we supposed to say it out loud? :o"

    scy "I believe so, you go first guppy!"

    show mc pout at mc_left
    mc "No! You should go first"

    show scy surprise at npc_right
    scy "Me?"

    show mc happy at mc_left
    mc "uh-huh!"

    show scy proud at npc_right
    scy "A great soldier such as myself wouldn't be troubled by something so trivial as feelings."

    show mc o at mc_left
    mc "Ah yeah I forgot you were a soldier sometimes…"

    show scy default at npc_right
    scy "I worked under the empress, little guppy. I was taught to fight, to follow orders, and to eliminate those who threatened her kingdom!"

    menu:
        "But were you happy?":
            show mc o at mc_left
            mc "But were you happy?"
            show scy surprise at npc_right
            scy "Happy?"
            show mc o at mc_left
            mc "mhm, during your time! Under the empress.."
            show scy proud at npc_right
            scy "Of course I was! Why wouldn't I be? I served the empress. I had a purpose. I was strong, respected, and-"
            show scy sepet at npc_right
            scy "and I guess that's all gone now."
            show mc happy at mc_left
            mc "But the seafolks love you now! Nobody's throwing rocks at you anymore"
            show scy default at npc_right
            scy "You're.. Not wrong! I'm just not used to all of this yet!"
            scy "I am aware that the people see me as some sort of hero now."
            scy "And I suppose I should be pleased."
            show mc o at mc_left
            mc "Buuut..?"
            show scy sepet at npc_right
            scy "And yet.. after all the sorrow I inflicted with my very own claws.. the families I exiled"
            scy "A tiny noisy voice inside my head just doesn't think that I.."
            show mc o at mc_left
            mc "that you deserve.. the praises?"
            scy "Perhaps so..!"
            scy "It is absurd, really. I am the strongest warrior in the kingdom. I should be proud of what I have become."
            scy "Yet whenever they praise me, I find myself wondering whether they would still do so if they knew everything I had done.."

        "How long did you serve the empress for?":
            show mc o at mc_left
            mc "How long did you serve the empress for?"
            show scy default at npc_right
            scy "Since I was a little larva. I suppose you could say I spent my whole life in her service!"
            show mc o at mc_left
            mc "waouh.. I can't imagine doing one thing for your whole life"
            mc "Even I get bored at doing my mama's chores.."
            show scy proud at npc_right
            scy "Well! Under her command, I did a variety of things, not one!"
            scy "Guarding the salt water border was one of my prominent ones.."
            show mc happy at mc_left
            mc "mhm yaa Mr.Cory told me that you've been guarding for long"
            show scy default at npc_right
            scy "But before that I also did some annihilation! and-"
            show mc shock at mc_left
            mc "wait! annihilation…?"
            show scy default at npc_right
            scy "Precisely! Eradicating those who did not bow to the rules of Her Highness!"
            scy "Those who broke the laws and cause chaos in all of sea!"
            show mc o at mc_left
            mc "Mr. Scyllarus.. How many exactly did you kill?"
            "I can see him subtly flinching at the question. Followed by a long pause."
            "I don't think he likes remembering that part.."
            show scy sepet at npc_right
            scy ".... I didn't bother to keep count!"
            scy "Annihilation isn't something you should wear proudly like a medal.."
            show mc o at mc_left
            mc "Do you regret them?"
            scy "For killing the wrong folks? Yes.. yes I do.."

    show mc o at mc_left
    mc "mmn.. Then why don't you just do good things? To cleanse all the bad things you've done?"
    mc "That way you'd feel less guilty!"

    show scy surprise at npc_right
    scy "Repentance.. activities…"
    scy "Ah! I think I understand now!"
    show scy proud at npc_right
    scy "Alright then from now on I shall exterminate all the perps in sea!"

    show mc shock at mc_left
    mc "No no! Murder is still bad Mr. Scyllarus!"
    mc "Even the bad people have families…"

    show scy default at npc_right
    scy "But all they do is take up space in the sea and corrupt it with their presence."
    scy "We shall never reach the peak of peace if we allow such people to continue."
    scy "Especially under the sea's current pitiful circumstances!"

    show mc o at mc_left
    mc "But.. what if I did something really bad?"
    mc "Would you exterminate me too?"

    show scy sepet at npc_right
    scy "...."
    scy "It.. depends..!"
    scy "If sacrificing one means saving many others…then perhaps it is the right thing to do."

    jump ch4_climax

label ch4_rite_leo:

    leo "Out of everyone you could have chosen to spend the peak festival with."
    leo "You chose me~?"
    leo "My, you must've put that much trust in me.. I can't help but feel flattered~!"
    leo "Are we like.. Bestest of buddies now? Delightful~"

    "The two of us swam up to one of the attendants handing out the small replicas of the effigies and was given one each."
    "We swam away from the crowd of people and toward the ledge of the deep sea."

    leo "Have you ever confessed, guppy?"

    show mc o at mc_left
    mc "Confess..? Like tell my parents if I did something bad?"

    leo "Mhm, that's it~! This.. whole thing feels like a confession booth, no?"

    show mc happy at mc_left
    mc "But I've been a good child! I have nothing to confess!"

    leo "You're the happy-go-lucky type aren't you? always cheerful.. Keeping others afloat~"

    show mc happy at mc_left
    mc "I could say the same to you! You're always so smiley and giggly."

    leo "But it's tiring isn't it? To always be so optimistic"
    leo "Which is why, I brought you a little gift~!"

    "Miss Leo pulls out a fresh fish meat from under her tail"

    show mc shock at mc_left
    mc "fish meat..?! o.o where did you, when did you get this?"

    leo "shh now now, no need to wonder just eat it will you?"

    "Lifting my glass bowl head up, hesitantly I took a bite"

    leo "mm that's it, good.."

    "To my surprise, the meat tasted super yum! It's soft, it doesn't taste fishy at all!"

    show mc happy at mc_left
    mc "mmn this is yummy meat.. I don't think papa has ever caught a fish that tastes this good raw.."

    leo "Riiight~? The subtle metallic tang makes it all the better"

    show mc o at mc_left
    mc "Mhm yaa tasted like chains"

    leo "Oh my, Are you saying you've licked chains before?"

    show mc default at mc_left
    mc "mhm! The smell is strong so I wonder how it tasted.. And I licked it!"

    leo "Mhehe how interesting, Wondered if you ever indulge in malicious thoughts~"

    show mc actually at mc_left
    mc "Mmmm actually I often thought of skipping naps."

    leo "Mhehe, 'course you do. You're as green as a green marble~"
    leo "Perhaps I failed to make myself clear~"
    leo "Every creature in this world must harbor a latent malice~"
    leo "Is there really no one, or nothing, that ever breeds resentment within you?"

    show mc o at mc_left
    mc "Uh… if it had to be one thing… then it's.. my papa."

    leo "Oh? What did he do to you? Did he abuse you? Lock you up in the basement  for days? Starve you for weeks?"

    show mc shock at mc_left
    mc "Whah? Nono! Not that..!"
    mc "He went to a suuuper long sail at the sea.. So long that he hadn't come home for years"
    mc "So I've just been with my mama at home, mama said he's catching a super rare big fish that's why he's taking so long."

    leo "Oh~! you're just a kid, yet life treats you harshly!"

    menu:
        "But we can just take a sad song and make it better, right! :D":
            show mc happy at mc_left
            mc "There are still a lot of things we can decide for ourselves."
            mc "Like.. I picked you to go with me! That means we get to choose what we want."
            leo "Nu-uh! there is no such thing~"
            leo "Your genes, the nurture you've been subjected to…"
            leo "... the environment shaping your tiny brain…"
            leo "Those things you can't control have been making every single choice for you~"
            show mc pout at mc_left
            mc "But i don't think it's alright if we blame something else for our choice-"

        "It's alright, being with Mr. Cory, Clarus, and you make me happy! :D":
            show mc happy at mc_left
            mc "You feel just like a family to me."
            mc "Mr. Cory is my papa, Mr. Larus is my.. uncle? My big bro?"
            mc "And you're my sister! You know so much about the sea. We're like… twins!"
            mc "And besides-"

    play sound "audio/unsettling_moment.wav"
    with vpunch
    leo "{glitch=60.0}{sc}{size=+6}SHUT UP, you really dont understand!!{/size}{/sc}{/glitch}"

    "The effigy glows, flickering erratically."

    show mc shock at mc_left
    mc "...! uh.. Uh……………. :'"

    leo "........."
    leo ".................."

    "Silence hangs heavily. The effigy is now fully glowing."

    show mc holdcry at mc_left
    mc "Uh.. are you.. okay miss Leo…  "
    mc "You can tell me if there's something that makes you sad.. :'("

    leo "Whoops, sorry~ got carried away."

    "However, her tone shifted sharper."

    leo "You want to know what really matters now~?"

    "Leo leans down, her breath cold against my cheek as she points his tail toward the shadows outside."

    leo "Just be vigilant around those playfellows of yours~"
    leo "One day, when push come to shove,"
    leo "All memories you've shared with them, will thrown away like it never existed~"
    leo "We're all fundamentally selfish beings, afterall~"
    leo "The golden fish can grant you a wish, even the impossible.."
    leo "They haven't known of that have they?"

    show mc shock at mc_left
    mc "mn.. No…"

    leo "And are you truly certain they won't hoard that power all for themselves the moment they find out?"

    show mc holdcry at mc_left
    mc "..... but they wont do that…!"

    leo "Oh, wouldn't they? Mhhehe."
    leo "Remember when your Mr. Cory and Mr. Scylarus were ready to pounce on you…"
    leo "All just because you wanted to eat a little fish?"
    leo "They can end you any given moment~"

    mc ".........."

    leo "I had best friends too, once. We always looked out for each other…"
    leo "They used to say, 'Oh leo, we will never abandon you, no matter happens!'"
    leo "But in the end…! I was left to rot all alone."

    mc "I-i… I'm very sorry, miss Leo-"

    leo "THAT'S NOT THE POINT! you will be too!"
    leo "You will always…. end up alone."

    mc "No..! Mr. Cory and Larus won't desert me!!"

    leo "... then let's put that to the test, shall we~?"
    leo "Step off the edge. Cast yourself into the abyss down there~"

    show mc shock at mc_left
    mc "....!"

    leo "Let's see if they truly bother to come searching for you."
    leo "Unless.. You aren't actually sure? You don't really believe you matter to them, do you~?"

    mc "Uh… uh…"

    leo "It's not like you have anywhere else to return to~"
    leo "Even if you die alone down there, at least you'll die knowing I was right~ "
    leo "Isn't that a win-win~?"

    mc ".................."

    "My gaze drifted downward, staring into the darkness beneath."
    "I looked back for the last time. Miss Leo smiled, nodding gently."
    "I pulled the effigy tightly against my chest."
    "One step."
    "Two steps."
    "Then my foot meets nothing but empty air."
    "Gravity dissolved."
    "A sudden weightlessness took me over as wind rushed past my ears…"
    "… plunging me down and down and down into the void….."
    "............................"

    jump ch4_climax

label ch4_rite_cory:

    show cory smile at cory_left
    cory "Sup guppy goo, you got your statue I see."

    show mc happy at mc_left
    mc "Hi Mr.Cory! :D Seems like you got yours too!"

    "The two of us swam over to the ledge of the deep sea"

    show cory side at cory_left
    cory "So.. what are ya telling to the statue?"

    show mc o at mc_left
    mc "Do we have to say it outloud? :o"

    show cory talk at cory_left
    cory "Nay, I don't think we're obliged to.. for it to work"

    show mc o at mc_left
    mc "mm.."

    "My gaze fell down to the Effigy, studying the meticulous sculpture."
    "Thoughts running over miles an hour, what should I put into this statue..? How has Papa haven't come back..? Or maybe mama-"
    "Mr. Cory's voice cuts through my trance"

    show cory side at cory_left
    cory "You know guppy, my little sister… she's just about your age"

    show mc o at mc_left
    mc "Really?? :o"

    cory "yeah.."
    cory "She loves picking up anything that catches her eyes like ya do"

    show mc happy at mc_left
    mc "ooo I would've shared with her my rock collections!"

    show cory smile at cory_left
    cory "pfft yeah she'd be thrilled."

    "Another pause, this time Mr Cory's caressing the effigy's scary face like it's family's"

    show mc o at mc_left
    mc "So.. where is she now?"

    show cory side_close at cory_left
    cory "I ain't know nothing guppy it's been years…! Years I tell ya.. since I last seen her"

    show mc o at mc_left
    mc "Then why don't you just meet her?"

    cory "I don't know where to find her, guppy..."

    show mc happy at mc_left
    mc "Then we'll search for her!"

    show cory side at cory_left
    cory "guh.. scrap that idea. She could be anywhere in the seven seas.."

    show mc o at mc_left
    mc "but we'll never know unless we try?"

    show cory side_close at cory_left
    cory "It'd took aaaages! I'd long be peepaw"

    show mc pout at mc_left
    mc "But you're over here helping me find a golden fish that could be anywhere too!"
    mc "nnn I don't get it Mr Cory! sounds like you actually don't want to meet her...."

    show cory upset at cory_left
    cory "Look..! Because it ain't.. ain't at all that simple!"
    cory "It ain't just a matter of finding nemo!"
    cory "You don't understand guppy, ya think it's all sunshines and rainbows do ya?!"

    show mc shock at mc_left
    mc "...!"

    show mc holdcry at mc_left
    mc "nn.. I'm… *sniff*"

    show cory surprise at cory_left
    cory "No! Nononono, hey hey shh I didn't mean to yell at ya.. I'm sorry"
    "Mr. Cory pulled me in by a side hug"

    show mc holdcry at mc_left
    mc "Why won't you let me help..? I don't get it.."

    show cory side_close at cory_left
    cory "Because I.."

    show mc o at mc_left
    mc "....?"

    cory "I.. abandoned her.. Guppy"
    cory "left her to survive alone.. In saltwater"

    "The word fell deaf on my ears"

    show mc shock at mc_left
    mc "what…"

    show cory upset at cory_left
    cory "I had to..! Her life was on the line..!"
    cory "Her sickness.. she was.. never meant to be in freshwater in the first place.."
    cory "I couldn't let her suffer anymore guppy"
    show cory side_close at cory_left
    cory "But sometimes.. a part of me still wants to see her.."
    cory "As selfish as it may sounds.."

    "A spark of flickering glow emits from Mr.Cory's effigy. So it does react to negative energy.."

    menu:
        "You could've just.. come along!!":
            show mc pout at mc_left
            mc "That's a very bad thing to do Mr. Cory she must've been.. so scared all alone"
            show cory upset at cory_left
            cory "Oh for Kraken's sak- I wouldn't be here at all with you if I could just-!"
            cory "I didn't have the golden crap's blessing before!"
            show mc o at mc_left
            mc "... Is.. that it..?"
            mc "Mr. Cory do you only.. see me as your.. Little sister?"
            show cory surprise at cory_left
            cory "What..?! No! I..!"
            cory "I care about you as you are guppy, not because of my- the eel did that come from?"
            show mc pout at mc_left
            mc "You said you wouldn't be here with me if it weren't because of.. the golden scale!"
            show cory upset at cory_left
            cory "I meant  I wouldn't be here if she was still with me! To eel with that stupid scale!"
            show mc holdcry at mc_left
            mc "But still.. that still means I'm.. just your little sister to you..!"
            show cory side at cory_left
            cory "Is it so wrong if it is..?"
            "The effigy glows brighter with each word."
            mc "....."
            cory "Ain't it the same as how you.. in a way see me as your father?"
            show mc holdcry at mc_left
            mc "mn.. does that mean.."
            mc "You're going to leave me too Mr.Cory..?"
            mc "Once it's all over.. you're going to leave me too aren't you…"
            mc "Just like.. papa did"
            show cory surprise at cory_left
            cory "Guppy, you know I wouldn't..!"

        "but how does she get to freshwater in the first place?":
            show cory side at cory_left
            cory "When I was your age, I was out explorin.. then I found an abandoned little egg.."
            cory "Went everywhere to search for the mother but found nothin.."
            cory "So.. our family raised it as our own"
            cory "We didn't realize she was saltwater.. so she was sick left and right"
            cory "But despite that.. she was still smilin.. always so eager to explore the world.."
            cory "She's the only pure thing I have in life.."
            cory "Until one day, her body decided that it was at its limit."
            show mc shock at mc_left
            mc "Did she die??"
            show cory side_close at cory_left
            cory "No! Just.. super weak couldn't even swim upright.."
            show mc pout at mc_left
            mc "Oh no..that's a sign of a dying fish :("
            cory "So we had no other choice.. my family told me to drop her off by the salt fresh border"
            cory "Ironic ain't it..? I was the one that found her.. and I was also the one to leave her behind.."
            show mc pout at mc_left
            mc "You're kinda evil for that Mr. Cory!"
            show cory side at cory_left
            cory "Aye.. but wouldn't it be more evil for me if I just let her wither away like that?"
            show mc o at mc_left
            mc "If I were her I'd rather.. die with my closest one around.."
            mc "Rather than live and be alone…"
            mc "If she means that much to you then you should've.. come with her!"
            show cory upset at cory_left
            cory "And kill myself instead?!"
            "My vision drifts past the faintly glowing effigy in my hands, dropping into the looming hole that brings anyone to the ocean bed"
            show mc o at mc_left
            mc "If I jump right now.. into the deep.."
            mc "Are you letting me go alone Mr.Cory..?"
            show cory surprise at cory_left
            cory "Guppy, don't you dare…"
            "I took a step forward to the hole."
            show cory upset at cory_left
            cory "Hey, hey, Guppy, listen, you're playing a dangerous game here.."
            "Mr. Cory's face grew pale, but he didn't do anything to stop me either"
            "Mr. Cory is a coward.."
            "I took another step forward"
            show mc holdcry at mc_left
            mc "Once it's all over.. you're going to leave me too aren't you…"
            mc "just like papa did…"

    jump ch4_climax

label ch4_climax:

    hide mc
    scene ch4_night
    with dissolve

    "At the ledge of the great abyss, multiple glowing effigies are cast into the dark void by the seafolks, tumbling downward into the deep sea."

    "Then suddenly, amongst the multiple thrown effigies I noticed something glows a bright gold."
    "Not the kind of gold that Mr. Rin uses.."
    "Not the kind of gold that the effigy has"

    show expression Transform("ch4_dialogue_night", zoom=1.5, xalign=0.5, yalign=0.8) as zoomed_abyss
    with dissolve
    play sound "audio/mysterious_golden_looking.wav"

    "But that rainbow radiant.. shimmering glow"
    "In that moment, everything else were a blur."

    show mc serious at mc_left
    with dissolve

    mc "I must get it.. I must get it, I must have it, no matter.. what!"

    "Papa always told me to catch anything that looks interesting"
    "He always brings back home cool fishes"
    "So maybe if I bring it home, this time he'll-!"

    play sound "audio/splash.mp3"
    hide mc
    with dissolve

    scene black with fade
    stop music fadeout 2.0

    "There were faint shouts ringing in the back of my head."
    "Amidst all of them, the loudest ones sounded familiar"
    "Before I knew it, I was already falling"

    $ ch4_chapter_complete = True

    jump chapter5_start
