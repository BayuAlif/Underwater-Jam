# ============================================================
# CHAPTER 4: THE GOLDEN VILLAGE & THE ABYSSAL RITE
# ============================================================

default ch4_scy_affection = 0
default ch4_cory_affection = 0
default ch4_leo_affection = 0

default ch4_chore1_companion = None
default ch4_chore2_companion = None
default ch4_game1_companion = None
default ch4_game2_companion = None
default ch4_ritual_companion = None

default ch4_chapter_complete = False

# ------------------------------------------------------------
# START OF CHAPTER 4
# ------------------------------------------------------------

label chapter4_start:

    $ current_chapter = 4
    $ current_cycle = "day"
    $ current_area = "golden_village_outskirts"

    hide mc
    scene ch4_day
    with fade

    "The vast saltwater current stretches endlessly in every direction. With Empress Crustacean VIII dethroned, the heavy, suffocating aura that once choked the open waters has vanished."

    show mc default at mc_left
    show cory side at cory_left

    cory "The water sure feels easier to breathe now that she's gone, huh?"

    show scy default at npc_right
    scy "Really?! *sniff sniff* I feel the quality of water remains the same!"

    "Suddenly, a pair of energetic seafolks swim right past us, stopping abruptly in absolute excitement."

    fish1 "SCYLLARUS!!! I'M A BIG FAN, HI!!"

    fish2 "THANK YOU FOR BRINGING HER DOWN, SCYLLARUS!!"

    show scy surprise at npc_right
    scy "HUH-! Oh! Yes, why of course the pleasure is mine, dear seafolks!"

    fish1 "Good luck on whatever you're doing, Scyllarus!!"

    fish2 "Yeah!! We love you!"

    "The two fishes swim away, giggling to themselves after greeting Mr. Larus."

    show cory smile at cory_left
    cory "Hah, someone's getting famous, ay?"

    show mc happy at mc_left
    mc "Hehe, people love you now, Mr. Slarus!"

    show scy proud at npc_right
    scy "It's Scyllarus! And... I'm still trying to get used to it...!"

    show scy shy at npc_right
    scy "It's odd having strangers wave at you..."

    show mc default at mc_left
    mc "Mmn yaa, it kinda feels different..."

    show cory side at cory_left
    cory "Nay, I meant there's no... dread or pressure no more."
    cory "Yeah, the seafolks have been all the more peaceful..."

    show cory talk at cory_left
    cory "We still oughta keep our eyes peeled for the golden fish though."
    cory "Could be anywhere in this vast ocean."

    show scy smile at npc_right
    scy "Yea! There's no way it could be right behind us--"

    show cory surprise at cory_left
    cory "Speaking of... isn't that the golden fish?!"

    show mc shock at mc_left
    mc "Whauh?! Where?!"

    show cory talk at cory_left
    cory "Right behind you, guppy!"

    play sound "audio/splash.mp3"
    "A radiant, shimmering flash of gold streaks past our fins! In a blink of an eye, the golden fish whooshes straight toward a pair of luminous gates ahead."

    show mc excited at mc_left
    mc "Ah! C'mon sir fishes! After it!!"

    jump chapter4_village_arrival


# ------------------------------------------------------------
# ARRIVAL AT THE GOLDEN VILLAGE
# ------------------------------------------------------------

label chapter4_village_arrival:

    $ current_area = "golden_village_plaza"

    hide mc
    scene ch4_dialogue
    with dissolve

    "We dash through the grand gateway, our fins stirring up trails of golden dust. But as soon as we cross the threshold, the golden fish blurs into a blinding sea of ornaments, lanterns, and statues made entirely of pure gold."

    show mc o at mc_left
    show cory upset at cory_left
    show scy default at npc_right

    cory "Aw shrimp! Damn fish must be Usailfish Bolt or something."

    show mc happy at mc_left
    mc "It's okay Mr. Cory :DDD, we'll get it next time!!"

    show scy sepet at npc_right
    scy "How are we supposed to find the damn fish among all this gold... wait... hold on... Where are we??"

    show cory side at cory_left
    cory "I don't know, but this place gives me the heebie-jeebies. Stay close guppy, we don't know what's ahead of us."

    show mc excited at mc_left
    mc "Look! Maybe those mr fishes over there would know where we are, let's ask them! :DD"

    jump chapter4_meet_rin


# ------------------------------------------------------------
# NPC: CHIEF RIN (WHALE SHARK)
# ------------------------------------------------------------

label chapter4_meet_rin:

    "An enormous whale shark towers over the three of us. Piles of gilded coral and ornate gold effigies surround him like miniature mountain ranges."

    show mc happy at mc_left
    mc "Helloooo!! Good morning sir :D Wao you're so biiiiig!!"

    rin "Ah--! Goodness gracious!"
    rin "Oh, just a guppy, aren't you... Scared the teeth out of old me..."

    show mc o at mc_left
    mc "Oops hehe, my bad...!"

    rin "No matter. Youth need not apologize for simply... being young."

    menu:
        "Have you seen a golden fish around?":
            show mc o at mc_left
            mc "We saw it but we lost it amongst these... golds you have piled up!"
            rin "A golden fish, you say...?"
            "Mr. Whale Shark's great eye drifts slowly toward the mountain of gold ornaments piled around him, as though sifting through decades of memory rather than metal."
            rin "Mm. I believe... I may have seen such a thing."
            show mc excited at mc_left
            mc "Really?! Can you tell us?"
            rin "Now, now. Need not to hurry, young one."
            show mc pout at mc_left
            mc "Mnn, but I need to know now... before it goes further :("
            rin "Patience will reward you grandly..."
            rin "We're currently having trouble with a festival that's going to occur tonight..."

        "Why's there so many gold here? Are you a gold thief :o":
            show mc o at mc_left
            mc "Why's there so many gold here? Are you a gold thief :o"
            rin "Thief? Oh no, no, you have it wrong..."
            rin "I'm too old to be fretting about wealth..."
            rin "These golds will be used for an upcoming festival."
            rin "Golds are believed to stray away evil and bad omens, young one."

    show mc o at mc_left
    mc "A festival...?"

    show mc excited at mc_left
    mc "Will there be lots of food? I haven't eaten in a while!"

    rin "Oh, why of course a big feast will occur!"
    rin "It's only fitting for a festival this important."

    show cory talk at cory_left
    cory "What's the festival about if we may know, sir?"

    rin "Yes, a dire one."
    rin "It's a festival that we hold once a year to ward off evil and bad luck."
    rin "It's the least we can do to repay the ocean..."
    rin "However, the sea has been quite turbulent lately, so we were forced to change plans and decided to host it twice a year instead."
    rin "But we completely underestimated how long gathering materials would take..."
    rin "...Now we're worried we won't finish in time if the festival is held tonight."
    rin "That's why, as much as I'd love to help with your search, I can't assist you."

    show mc happy at mc_left
    mc "Alright, then we'll help you!"

    rin "Oh, how wonderful! The people thank you for your benevolence."
    rin "Rest assured travelers, we will be preparing the best of meals for your help."

    show cory smile at cory_left
    cory "About time we fill our stomachs..."

    show scy proud at npc_right
    scy "Don't fret my friend, we shall be of assistance! As much as we can!"

    jump chapter4_meet_leo


# ------------------------------------------------------------
# NPC: LEO DRURGA (LEOPARD SEAL)
# ------------------------------------------------------------

label chapter4_meet_leo:

    play sound "audio/bush_rustling.mp3"
    leo "Greetings~!"

    show mc shock at mc_left
    mc "Waouh--!"

    "I stumble backward into Mr. Larus's steady claw as a towering, sleek figure casts a long, graceful shadow over us."

    show scy surprise at npc_right
    scy "Careful now!"

    leo "Mmhehe, my apologies for the spook, friend..."
    leo "You're searching for the golden fish, yes?"
    leo "Sparkling rainbow, lush tail..."

    show mc excited at mc_left
    mc "Yes yes you're right!! Super spot on!"

    leo "I can be of your aid I assure you~!"
    leo "You just have to follow me!"

    show cory side at cory_left
    cory "Hold your seahorses!"

    menu:
        "How did ya know we're lookin' for it? (Cory)":
            cory "How did ya know we're lookin' for it?"
            leo "Mmm... it's no science. I've seen you go around asking about it..."
            leo "Like a little ballerina in a broken music box~"
            leo "Round and round you go, same question, same steps, same tune..."
            leo "Doesn't it make you dizzy?"
            show mc default at mc_left
            mc "Mmn... no! Because if I get dizzy..."
            mc "Mr. Cory and Mr. Larus will help make it go away!"
            mc "So I have nothing to worry about!"
            leo "I like your answer~!! Always so refreshing!"

        "How do we know ya really know of the fish's whereabouts? (Cory)":
            cory "How do we know ya really know of the fish's whereabouts?"
            leo "Mm, but until now... you've been blindly following clues from strangers too, right?"
            leo "What makes it different from what I said?"
            show scy smile at npc_right
            scy "He's right my friend, Cory! We have each other, it'll all be fine!"
            show mc happy at mc_left
            mc "Mhm yaa, Mr. Cory you worry too much."
            mc "More than both of my parents combined..."
            show cory upset at cory_left
            cory "Ugh... maybe you're right, my bad..."
            cory "Dunno what got into me."
            "Mr. Cory looks like he's got a lot on his mind."

    leo "Besides, the ocean's my playground~!"
    leo "I know it like the back of my hand..."
    leo "Which means I get to join your fun little party, yes?"

    show mc happy at mc_left
    mc "Yaa! Welcome aboard miss...?"

    leo "Leo is fine~! Leo Drurga."

    show mc o at mc_left
    mc "Drurga... :o"
    "The surname tickles something familiar in the back of my brain. Yet I can't really pinpoint what."

    show scy proud at npc_right
    scy "We welcome you to our thrilling little search party, comrade!"

    leo "My oh my, this will be spiiine-tingling~!"
    leo "Ah, but I doubt we can go into searching right away..."
    leo "Not when the chief's having trouble..."
    leo "He'll go whiny about how much help they require for the festival..."

    jump chapter4_day_chores


# ------------------------------------------------------------
# DATING ROUTE: FESTIVAL PREPARATION CHORES (DAY)
# ------------------------------------------------------------

label chapter4_day_chores:

    $ current_area = "festival_prep_grounds"

    "Chief Rin gathers us at the edge of the village pavilion."

    rin "Young ones, our preparations are split between gathering natural decorations from the reefs and constructing the merchant stalls."
    rin "Please, divide the tasks and see them through before nightfall."

    jump ch4_chore_seaweeds


# ------------------------------------------------------------
# CHORE 1: FETCHING SEAWEEDS AND CORALS
# ------------------------------------------------------------

label ch4_chore_seaweeds:

    rin "May you be of aid with gathering seaweeds and corals, young one?"

    show mc excited at mc_left
    mc "Sure! Are the colors up to us to pick?"

    rin "Yes, yes, whatever pigment caught your eyes most..."
    rin "We need them to decorate the sacred statue."

    mc "Yaaay okay! I'll bring lots for you!"

    rin "Keep it balanced, yes? We don't want to anger the ocean more than we already have..."

    "Who should I go gathering seaweeds with?"

    menu:
        "Gather seaweeds with Scyllarus":
            $ ch4_chore1_companion = "scy"
            jump ch4_seaweeds_scy

        "Gather seaweeds with Cory":
            $ ch4_chore1_companion = "cory"
            jump ch4_seaweeds_cory

        "Gather seaweeds with Leo":
            $ ch4_chore1_companion = "leo"
            jump ch4_seaweeds_leo


# --- Scyllarus Seaweed Branch ---
label ch4_seaweeds_scy:

    show scy proud at npc_right
    scy "Lay it on me!! My eyes are good at picking the freshest of seaweeds!"

    show mc o at mc_left
    mc "I've always been curious... How do you see the sea with your super revolutionary 12-colored vision?"

    show scy smile at npc_right
    scy "It's Scyllarus! And... hmm!"
    scy "Perhaps we can play a little game, my comrade!"

    show mc excited at mc_left
    mc "A game?! What game? I wanna play! :D"

    scy "I spy with my little eyes!"
    scy "I believe it would be easier for you to understand!"

    mc "Ooo okay! I go first!"
    mc "I spyyyy with my little eyeeees...!"

    menu:
        "A fuzzy looking white tree... with dancing toothpicks as its hair!":
            scy "Hm...! A plumose anemone?"
            show mc happy at mc_left
            mc "Ding ding ding! Woah you're right!"
            show scy proud at npc_right
            scy "In my eyes, white is a very bright, shiny color!"
            scy "Sometimes... white comes to me in shades of yellow!"
            mc "Ooowao so cool! How I see it is just... pearlescent-ish white."
            mc "Mmm but can you... wait, can you tell the color of my slingbag?"
            scy "It's... red, isn't it?!"
            show mc pout at mc_left
            mc "Mmn nono, it's orange!"
            scy "It's all lustrous and shiny for me! I can see three in one color you would usually perceive!"
            mc "Like... in a kaleidoscope?"
            scy "I'm not sure of this kaleidoscope you speak of!"
            scy "But if it reminds you of said thing, perhaps you're right KAKAKA!"
            mc "Hehe maybe I can try and find you one, Mr. Scyllarus! I'm sure you'll love it!"
            "I wonder if he'll get dizzy and faint if he were to see a kaleidoscope from all the overwhelming colors... Can shrimps faint? :o"

        "A bunch of swaaaying red branch-y guys":
            scy "Hm! A plumose coralline!"
            show mc happy at mc_left
            mc "Ding ding ding, you're spot on! So cool o.o"
            show scy proud at npc_right
            scy "Through these eyes of mine, red is a very prominent contrast color!"
            scy "It's all lustrous and shiny for me!"
            mc "Like... in a kaleidoscope?"
            scy "I'm not sure of this kaleidoscope you speak of!"
            scy "But if it reminds you of said thing, perhaps you're right KAKAKA!"
            mc "Hehe maybe I can try and find you one, Mr. Scyllarus! I'm sure you'll love it!"
            "I wonder if he'll get dizzy and faint from eyestrain if he were to see a kaleidoscope... :o"

        "A big... strooong colorful hard shelled creature with a super strong punch! (+1 Affection)":
            $ ch4_scy_affection += 1
            show scy surprise at npc_right
            scy "Big... colorful hard shelled... Super strong..."
            scy "It can't be...!"
            scy "Is mother sea so concerned about my superior kind that they invented a new special creature worthy of becoming our true rival?!"
            scy "Where is it?! I must see this for myself!"
            show mc happy at mc_left
            mc "Pfft hehe nonono! It is you, Mr. Scyllarus!"
            show scy proud at npc_right
            scy "Oh...!"
            scy "Hah! Well I must say I'm quite the charming and strong mantis shrimp myself!"

    show scy default at npc_right
    scy "Even so... I can't distinguish between what others call yellow-orange and orange..."
    scy "Most of my vision goes to UV sightings!"

    "Mr. Scyllarus looks over to the swaying corals, grazing them with a careful, gentle sweep of his claw."

    scy "And! This coral in particular is my mom's favorite..."

    show mc o at mc_left
    mc "Really? :o"

    show scy smile at npc_right
    scy "When I was little, I kept bringing her home tens of them everyday!"
    scy "And she always put them up on the walls like medals... each and every one of them."

    show mc pout at mc_left
    mc "Mnn... but when I do it, you scold me! >:T"

    show scy proud at npc_right
    scy "Now, now! Back then corals were overgrown! And I didn't know any better either!"
    scy "We're in a time of scarcity, little guppy! Everyone's greedy!"

    show scy sepet at npc_right
    scy "Before the kingdom tore me away from her..."

    show mc shock at mc_left
    mc "Whah! Why?? :o"

    scy "Because I was the only mantis shrimp in the area!"
    scy "And they wanted a strong, esteemed soldier, so they took me in ever since I was little!"
    scy "I went through countless rigorous training regimes!"

    show mc o at mc_left
    mc "Like Sparta? o.o All day all night training until your body gives out?"

    show scy smile at npc_right
    scy "No! Nonono! They treated me well, I guarantee you!"
    scy "They fed me, sparred with me in training, gave me quarters..."
    show scy sepet at npc_right
    scy "But... they just didn't let me see her often..."

    show scy proud at npc_right
    scy "We're getting a little sidetracked here! Come on guppy, fetch the glowing red ones!"

    show mc pout at mc_left
    mc "Glowing...? But I can't see the glooow, Mr. Larus! :("

    scy "Oh right! Fine, I shall guide you through it then!"

    jump ch4_chore_stands


# --- Cory Seaweed Branch ---
label ch4_seaweeds_cory:

    show cory talk at cory_left
    cory "Plucking seaweeds? I got ya, guppy!"
    cory "Which colors are we pickin'?"

    show mc excited at mc_left
    mc "Mmm I like orange..! And blue.. Oh oh pink coral too! And a little bit of pastel purple..."

    show cory smile at cory_left
    cory "Woah, you got a whole palette over there...!"
    cory "But hey, I dig orange too."

    show mc happy at mc_left
    mc "Yay! Let's pick the orange ones first then :D"

    "Mr. Cory and I take our time in picking the best fluorescent seaweeds."

    show cory side at cory_left
    cory "You know... pickin' corals and seaweeds like this..."
    cory "It's quite comforting, yeah?"

    menu:
        "Mm! It's like... plucking fleas from a wild cat.":
            show cory unimpressed2 at cory_left
            cory "Flea plucking? Mane, you're into bizarre hobbies aren't ya?"
            cory "What the eel is even a flea?"
            show mc pout at mc_left
            mc "But the satisfaction that you freed a little creature from its parasitic agony is nice!"
            mc "And and you also get to torture the little mean fleas! So they don't do more harm."
            show mc o at mc_left
            mc "Is it really odd...?"
            show cory side at cory_left
            cory "Ay, don't make that face... I meant good!"
            show cory smile at cory_left
            cory "The weird in people is what makes the world challenging and fun."
            show cory smile_hu at cory_left
            cory "And as long as you're doin' it for good... I ain't got a problem with it."
            show mc happy at mc_left
            mc "Mm... I get called weird lots..."
            mc "You're the first to tell me that weird is good, Mr. Cory!"
            show cory proud at cory_left
            cory "Those jerks are just envyin' ya. They don't have as much 'personality' as you do."
            cory "Being the norm is boring anyway, livin' the same way everyone does..."
            cory "Talk about a dead monochrome world..."
            show cory fond at cory_left
            cory "Stay weird little guppy, I mean it."

        "Mm! It's like drawing! (+1 Affection)":
            $ ch4_cory_affection += 1
            show cory talk at cory_left
            cory "Drawing, huh...? You an artist?"
            show mc happy at mc_left
            mc "Mhmm! I draw in my free time! I draw the fishes I see and document them! Their behavior and details like that!"
            show cory smile at cory_left
            cory "*whistle* You never cease to amaze me."
            show mc excited at mc_left
            mc "Yaa, other than to be a fish, I also want to be a book author! And and a marine biologist!"
            mc "I wanna document all my finds and draw them myself."
            mc "So people can appreciate water creatures more!"
            show cory fond at cory_left
            cory "The more I realize just how well you'd get along with her..."
            show mc o at mc_left
            mc "Her? :o Mm, Ms. Gator?"
            show cory side at cory_left
            cory "Nah, ain't her... I knew a sunshine little fishie just like you."
            cory "She loved makin' stuff with seaweeds like these."
            show mc happy at mc_left
            mc "Ooo I'd love to meet her! Where is she now? We should let her join in our adventure too!"
            show cory upset at cory_left
            cory "....She's not with me anymore, guppy."
            cory "She's somewhere... in this vast ocean."
            show mc sad at mc_left
            mc "Oh... will... you be able to meet her again?"
            show cory side_close at cory_left
            cory "Doubt it. Even then, I'm not too sure if she'd be happy to see me after what happened..."
            show mc default at mc_left
            mc "If she means that much to you, then I think she'll appreciate seeing you again."
            show cory fond at cory_left
            cory "Hah... what do ya know, guppy... Appreciate it though."

    show cory talk at cory_left
    cory "Alright, I think this much is plenty!"

    show mc excited at mc_left
    mc "Mhm! We got orange and pink and yellow and--"
    mc "Can we get thirty of the purple ones too, Mr. Cory?"

    show cory unimpressed at cory_left
    cory "No can do, guppy. That's enough."

    jump ch4_chore_stands


# --- Leo Seaweed Branch ---
label ch4_seaweeds_leo:

    leo "Ooo hehe, how fun~! I like picking flowers."
    leo "Tell me, what's your favorite flower, little guppy?"

    show mc default at mc_left
    mc "Mmm... I often see and pick lots of wildflowers on my walks... so that's probably it!"

    leo "Wildflowers, huh...? How very fitting of you~!"

    menu:
        "What about you? What's your favorite flower? (+1 Affection)":
            $ ch4_leo_affection += 1
            leo "Hmm... I think it would be... the nightshade. Familiar?"
            show mc o at mc_left
            mc "No, I don't think I've heard of it... What's it like?"
            leo "Ah, it's a flower of gorgeous purple shade... My favorite part? The little flecks of yellow in the center."
            show mc happy at mc_left
            mc "Yellow and purple... they're complementary colors, right? I can see why you find them pretty :D"
            leo "Ding ding ding~! You're right! Very perceptive, aren't you?"

        "Are you going to eat me? :o":
            leo "Eat you...? Oh no, humans were never on the menu."
            leo "What rumors have you been hearing, hm?"
            show mc o at mc_left
            mc "I heard that leopard seals can eat humans if they want!"
            leo "While it might be paaaartially true... doesn't mean I'm eating every human I see..."
            leo "My appetite lies in quenching curiosity, guppy."
            show mc happy at mc_left
            mc "Mm! I totally get it! The satisfaction of knowledge is incomparable!"

    show mc o at mc_left
    mc "Ah! We're getting a little sidetracked here..."

    leo "Mhehe, it's fine. We're allowed to have fun every now and then, no?"
    leo "Just sit back and relax, little guppy... I know you've been through a lot..."

    show mc pout at mc_left
    mc "Mnn... but we can't slack off, can we?"
    mc "The festival is just... tonight! Um... how many hours 'til then?"

    leo "Hmm, counting time would do us no fun..."

    show mc sad at mc_left
    mc "But but the golden fish! It'll stray super far too if we take long :("

    leo "Would you believe me if I were to say that..."
    leo "The golden fish... it moves only when you move."

    show mc shock at mc_left
    mc "Huh? So when I'm in one place, it'll always be nearby?"

    leo "Mhm, just a theory though... a sea theory~"

    jump ch4_chore_stands


# ------------------------------------------------------------
# CHORE 2: BUILDING UP STANDS / STALLS
# ------------------------------------------------------------

label ch4_chore_stands:

    "We return to the festival grounds with our gathered materials. Chief Rin approaches with timber planks and rope cords."

    rin "Can I trust your hands with assembling these materials into stalls, young one?"

    show mc default at mc_left
    mc "Mm, I can try...! But I'm going to need a hand from my friends."

    rin "Do whatever shall make this easier for you."
    rin "If you need anything, I'll be around the corner. Do be careful."

    "Who should I build the stalls with?"

    menu:
        "Build stalls with Scyllarus":
            $ ch4_chore2_companion = "scy"
            jump ch4_stands_scy

        "Build stalls with Cory":
            $ ch4_chore2_companion = "cory"
            jump ch4_stands_cory

        "Build stalls with Leo":
            $ ch4_chore2_companion = "leo"
            jump ch4_stands_leo


# --- Scyllarus Stand Branch ---
label ch4_stands_scy:

    show scy proud at npc_right
    scy "Kakaka, deal then, guppy!"

    show mc excited at mc_left
    mc "Yayay let's work together, Mr. Cy--Clarus--"

    scy "I'll set up the stall frame, you handle the decorations, understood!!"

    mc "Ay ay captain!!"

    "Mr. Shrimp works with insane efficiency. Moving with clockwork precision, timbers snap into place in seconds."

    show mc shock at mc_left
    mc "WOAH that's zippy!!"

    show scy proud at npc_right
    scy "Ha! Of course, I've been drilling under Her Highness since I was a mere kid!"
    scy "This is nothing... but duck soup!"

    show scy default at npc_right
    scy "...."

    "Despite his boastful words, I catch him suddenly growing quiet, his posture slumping."

    show mc o at mc_left
    mc "...Um, you don't seem like yourself, Mr. Shrimp..."

    scy "...? Am I?"
    scy "I'm running on all cylinders!!"

    show mc sad at mc_left
    mc "No, no, that's not what I meant at all."

    "Mr. Shrimp pauses, his claws coming to a sudden halt on the timber."

    show scy sepet at npc_right
    scy "I don't know. Feels like... I'm losing my drift sometimes!"
    scy "Guess what I'm trying to say is... it feels strange when I'm no longer on duty."
    scy "Hard to even function like a normal seafolk."

    show mc o at mc_left
    mc "Oooo...."

    scy "Once this journey ends, I got no clue where the current's supposed to take me."

    menu:
        "Take your time, Mr. Shrimp! (+1 Affection)":
            $ ch4_scy_affection += 1
            show mc default at mc_left
            mc "I don't know how it feels... to lose your purpose."
            mc "I don't know how you're feeling right now..."
            mc "But the ocean is huge! And we're travelling around right now."
            show mc happy at mc_left
            mc "Maybe what you need to do is... find out what you actually like doing."
            mc "Or maybe you could just stick around with me forever! Problem solved :D"
            show scy surprise at npc_right
            scy "...! THAT'S A BRILLIANT OBSERVATION GUPPY!"
            show scy laugh at npc_right
            scy "Kakaka! I'll bear that in mind!"

        "You should be grateful, Mr. Shrimp!":
            show mc happy at mc_left
            mc "Not working means more time to play!"
            mc "Other grown-ups have to work every single day and they look suuuper tired."
            mc "So you should be grateful and happy :D"
            show scy proud at npc_right
            scy "..Yeah. Yeah, you're right!"
            scy "Guess I'm just out of the line of fire and complaining about the weather!"
            scy "Bad look on me, guppy!"

    "The stand is finally completed."

    show mc excited at mc_left
    mc "WOAHH this turned out way cooler than I thought!!"

    show scy proud at npc_right
    scy "Hmph!! I'll call this... a crustacean-ship!!"

    show mc happy at mc_left
    mc "With... guppy's assistance :D!"

    jump chapter4_feast_afternoon


# --- Cory Stand Branch ---
label ch4_stands_cory:

    show cory talk at cory_left
    cory "Ay, gimme a hand with this frame, guppy!!"

    show mc excited at mc_left
    mc "Waouh, on it!"

    cory "Aand here. Hold these ends steady when I tie the knots."

    mc "Moremoremore Mr. Cory!!"

    show cory smile at cory_left
    cory "Woah easy there, you're really excited, huh?"

    show mc happy at mc_left
    mc "Mhm! This is my first festival ever!"
    mc "Have you ever been to a festival, Mr. Cory?"

    show cory side at cory_left
    cory "Ay... used to spend days around the Samba festival..."

    show mc o at mc_left
    mc "Samba festival? What's that??"

    show cory talk at cory_left
    cory "Ah, it's an annual celebration back down in the Southern Reefs."
    cory "Wild stuff. You got fishfolks dancing around in these massive glowing anemone suits..."

    show mc excited at mc_left
    mc "MASSIVE ANEMONES?"

    cory "Yeah. Massive, vibrant, glowing anemones..."
    cory "And sea percussion pounding so hard you could feel the vibration through your fins."
    cory "Type of shrimp you don't forget easily."

    show mc happy at mc_left
    mc "Oooh I'd like to visit your house someday! :D"

    show cory upset at cory_left
    cory "Well... ain't sure about that, guppy."
    cory "Truth is, I haven't stepped back home in a long while."

    show mc o at mc_left
    mc "Why?? :o"

    cory "My siblings... they all made something big of themselves."
    cory "One's a freshwater guard commander, another runs a pearl merchant."
    cory "And there's me, just drifting around, taking whatever odd jobs I can find."
    cory "Feels like if I show my face back home like this... I'd just be a disappointment..."

    menu:
        "Well, isn't that just natural?":
            show mc sad at mc_left
            mc "If your siblings are doing great and you're just doing odd jobs..."
            mc "...It's natural that you feel a bit disappointed, right?"
            show cory side_close at cory_left
            cory ".....Yeah."
            cory "Hearing this straight from a little kid hits hard..."
            cory "But you ain't wrong, guppy."

        "I'm sure your family waits for you (+1 Affection)":
            $ ch4_cory_affection += 1
            show mc default at mc_left
            mc "I don't think your family cares about your job, Mr. Cory."
            mc "If it were me, I'd just be happy to see you come home safe and sound."
            show cory surprise at cory_left
            cory "....!"
            show mc happy at mc_left
            mc "AND! I want to go dance at that Samba festival with you someday..."
            mc "...So you have to go make up with your family first!"
            show cory fond at cory_left
            cory "............"
            cory "HIC, guppy... my little baby guppy..."
            cory "*Sniff* Thank you... I needed to hear that..."

    "The stand is finally completed."

    show mc happy at mc_left
    mc "Phew! My arms are completely dead... but we actually pulled it off!"

    show cory smile at cory_left
    cory "Ay, we are the dream team, guppy."

    jump chapter4_feast_afternoon


# --- Leo Stand Branch ---
label ch4_stands_leo:

    leo "Hee hee! Let's construct this stand together~"

    show mc happy at mc_left
    mc "Mhm! Time to roll!"

    "We set to work side-by-side, joining the timber as the midday light filters through the festival grounds."

    show mc o at mc_left
    mc "Just a fleeting thought..."
    mc "...But isn't the name 'Leo' usually belonging to suuuper famous people!?"
    mc "Like Leonardo da Vinci! Leo Tolstoy! Leonel Messi!"

    leo "It's... Lionel~"

    show mc shock at mc_left
    mc "Hum yeah!! Wait, how do you even know about Mr. Lionel Messi :o"

    leo "Hee-hee~ never overlook my knowledge, twin~"

    "Leo glides into action with sleek grace, showing surprising, terrifying power in those long flippers."
    "Joint pegs are hammered and heavy timber snaps effortlessly into place."

    menu:
        "Have you participated in this festival before, Miss Leo?":
            leo "...Pretty much~"
            leo "All the seafolk... so many seafolk..."
            leo "Tail in tail through their little festival life~"
            leo "Pretending it's all about helping each other~"
            show mc o at mc_left
            mc "Pretending...? :o"
            leo "Ah, what I mean is... purely selfless virtue is merely an illusion~"
            leo "Strip away the smiles, and at the end of the day, every single creature..."
            leo "...is ultimately carving their path through their own current~"
            show mc default at mc_left
            mc "Mnn you mean that... everyone is living only for the things they like?"
            mc "That's not true at all! You can clearly see how genuine my friends are with me :D"
            leo "Hee hee. If you say so~"

        "You're so cool :0 (+1 Affection)":
            $ ch4_leo_affection += 1
            leo "Hee-hee~ you're fully capable of this too, twin~"
            leo "Or well... you could, if you weren't so accustomed..."
            leo "...to having your fin held through every tiny wave~"
            show mc o at mc_left
            mc "Um... but Mr. Cory and Mr. Shrimp are just helping me out."
            leo "Of course, of course~"
            leo "I'm suggesting it's not good to always rely on someone else~"
            leo "How will you ever survive when you're on your own~?"
            show mc shock at mc_left
            mc "Gulp......."

    "The stand is finally established."

    show mc happy at mc_left
    mc "That's actually pretty easy!"

    leo "See? I told you that you've got it in you~"

    jump chapter4_feast_afternoon


# ------------------------------------------------------------
# THE FEAST & DIETARY CONFLICT (AFTERNOON TENSION)
# ------------------------------------------------------------

label chapter4_feast_afternoon:

    hide mc
    scene ch4_day
    with dissolve

    show mc happy at mc_left
    mc "Mr. Whaaale, we're done! :D"

    rin "Oh, praise the Mother of Sea... Aren't you as swift as an arrow?"
    rin "We are truly grateful for your assistance!"

    mc "Yaaa no problem!"
    show mc excited at mc_left
    mc "Soo when will the festival start? Is the food ready :o"

    rin "Fufu."
    "Mr. Whale slips out a tiny chuckle at my impatience. Is starvation something that amuses him? >:T"

    rin "Rest assured my child, we have prepared a bountiful spread for all of you. Come."

    "I nod gleefully, drooling at the mouth while skipping behind Mr. Whale's enormous tail."
    "We arrive at a massive dining table—it looks like it could serve two whale sharks!"
    "Yet as my gaze falls down to the dishes, my face scrunches up in bewilderment."

    show cory talk at cory_left
    cory "Bloodworms?! Didn't know you were fancy like that, Mr. Chief sir."

    show scy laugh at npc_right
    scy "Hah! Talk about a banquet!"

    rin "Yes of course, we prepare this with every species' likings in mind."

    show mc o at mc_left
    mc "Are there... any... fried fishes?"

    show cory surprise at cory_left
    cory "...???"

    leo "Oh dear, the cat's out of the bag~"

    show cory upset at cory_left
    cory "Guppy... you wouldn't eat me, would ya?! I'm made of bones and pigments!"

    show mc shock at mc_left
    mc "Mn nonono! I mean! Like... tuna or... salmon or... fried catfish maybe?"
    show mc o at mc_left
    mc "Don't fishes eat other fishes too...? Mr. Whale Shark, your diet is small fishes right? Mackerel... and..."

    leo "Mhm, that's right. Whale sharks eat baby fishes too... as well as shrimps~"

    show scy surprise at npc_right
    scy "Did someone say shrimp?!"

    show mc actually at mc_left
    mc "And Mr... Mr. Scyllarus too, you... you eat crabs... supposedly!"

    show scy shock at npc_right
    scy "A-Are you suggesting I would eat my own comrades...?!"

    show mc sad at mc_left
    mc "But it's how nature is...! The ecosystem!"

    rin "..."
    "Mr. Whale's heavy stare bears down in silence. Meanwhile, Leo sits casually in the corner, thoroughly amused."

    rin "My apologies, young one... Our village has long forbidden such extreme practices..."
    rin "While there are creatures in the sea that are still... what I would describe as crassly primitive..."
    rin "We do not condone such unvirtuous behavior around here."
    rin "The best we can provide for your appetites are... jellies made of algae."

    show mc sad at mc_left
    mc "....Okay."

    rin "Do... rest yourselves until tonight. Before the parade begins."
    rin "Please excuse me."

    "Chief Rin slowly swims away, leaving an awkward, stiff silence across the table."
    ".............................."

    leo "You know guppy, I can indulge you in some... fishes that suit your taste~"

    show cory upset at cory_left
    cory "In front of my bloodworms?!"

    leo "Oh, I might be talking about you, Corydoras..."

    show mc pout at mc_left
    mc "I wouldn't--! No, I wouldn't eat my friends!"

    leo "Would you now? Let's ask the consensus~!"
    leo "Starting from you, Doras~! Are you just now imagining our beloved protagonist's tiny sharp teeth chewing away on you?"

    show cory side at cory_left
    cory "Nah, of course not! You're just trying to rile things up! I ain't falling for that!"

    leo "Hmm~ But your fins... I saw them tremble just now~"

    show cory upset at cory_left
    cory "They're just a kid! If they want anything from me, I could still defend myself from--"

    show scy proud at npc_right
    scy "That's right! If the situation came to that... my claws are ready to stop your nibbles!"

    show mc holdcry at mc_left
    mc "I... *sniff* I'm not hungry anymore...!"

    hide mc with easeoutleft
    "Tears stinging my eyes, I push away from the table and swim off into the shadows."

    leo "Hmm, folded too fast."

    jump chapter4_night_exploration


# ------------------------------------------------------------
# NIGHT EXPLORATION: ORIN (THE CHAINED CATSHARK)
# ------------------------------------------------------------

label chapter4_night_exploration:

    $ current_cycle = "night"
    $ current_area = "quiet_coral_cove"

    hide mc
    scene ch4_night
    with fade

    "I manage to find myself a quiet space to ponder over everything."
    "The gentle swaying of anemones and softly glowing night corals calms me down a little."

    show mc sad at mc_left
    mc "*sniffles* W-wauh...?"

    ori "Meow."

    show mc o at mc_left
    mc "M... Meow?"
    mc "Hello... Miss...ter cat shark...?"

    ori "Mhm."

    "The chained catshark, despite his intimidating, jailbreak appearance wrapped in rusted iron links, holds out a square-shaped jelly."
    "It looks like a crudely cut sponge character."

    ori "Sepombob."

    show mc o at mc_left
    mc "Spongebob...?"

    ori "Sepombob."

    show mc default at mc_left
    mc "Is it for me...? Thank you..."

    ori "Welcome."

    "I carefully nibble the wiggly jelly. It tastes vaguely like strawberry and sweet algae."

    ori "...I've been there."

    show mc o at mc_left
    mc "Mm? Been... where exactly?"

    ori "Been under."

    mc "Under where? :o"

    ori "I made you say underwear."

    show mc happy at mc_left
    mc "...??? Pfft-- Ahahahah! What was that!!"

    ori "Heh."

    show mc default at mc_left
    ori "Why are you alone? Saw you with friends. Big shrimp. And freshwater. And smiley seal."

    show mc sad at mc_left
    mc "I... mn... I said... something that might've offended them..."

    ori "...?"

    mc "Have you... eaten fishes in your life?"

    ori "Mm. Have..."

    show mc o at mc_left
    mc "Do you think it's wrong for predator fishes to eat other fishes?"

    ori "..."

    mc "Well... I don't think it's wrong... because that is the way nature intended us to be... the weak gets hunted."
    mc "But it also doesn't mean... we eat our friends because their species is in our diet! Like! If you had a pet chicken, you wouldn't eat it, right? Even if chickens are food to a lot of predators."

    ori "Mm... chickens...? Some kind of... new fish?"

    show mc actually at mc_left
    mc "Ah nono, they're a living creature that's... like a bird!"

    ori "Bird...?"

    show mc o at mc_left
    mc "Oh... right, you're a seabed shark..."

    ori "Mm, but..."
    ori "If a pet sees you eat the same kind as what they are..."
    ori "It would be scared of you too. Distrust."
    ori "Will think: What if I'm next?"

    show mc sad at mc_left
    mc "Mnnn... but I would never do thaaat! D:"

    ori "Mm, even so. Will still think that. In the back of mind."
    ori "If I tell: I eat human daily. Would you... think of me eating you in the back of mind?"

    show mc o at mc_left
    mc "....Mn, would, but... wouldn't make me scared of you."

    ori "Bizarre..."

    menu:
        "Is eating fishes the reason you're all chained up?":
            mc "Is eating fishes the reason you're all chained up?"
            ori "It's--"
            leo "Why helloooo there, friends~!"
            show mc shock at mc_left
            mc "Waugh?! Leo!"
            leo "Mhm yes yes, it is I~"
            leo "I've just been wondering where you've been..."
            "A tiny boop lands on my nose."
            leo "After the whole debacle there... I was worried my friend here might fall into a deeeeep hole of overthinking and sadness~"
            leo "So I came to check up!"
            show mc default at mc_left
            mc "Mmn... am fine, Leo. I made a friend!"
            leo "Oho? Another friend? How exciting~!"

        "Can I pet you, mister cat shark?":
            mc "Can I pet you, mister cat shark?"
            ori "You may."
            show mc happy at mc_left
            mc "Really?? You're okay with it? No hard feelings?"
            ori "Mean it."
            "The catshark gently lowers his head."
            mc "Hehehe, you can purrrrrr~!! Good... boy good girl good thing!"
            ori "Meow."
            leo "How fun~! May I join in on the pet fest?"
            show mc shock at mc_left
            mc "Waouh--! Leo!"
            leo "Mhm, yes it is I~"
            leo "I see you made a little friend. Are you feeling okay? No more hungry for fish?"
            show mc sad at mc_left
            mc "Mno... I should be more... considerate."
            leo "I don't think it's your fault, we all have our appetites."
            leo "I eat fishes and penguins on a daily basis too, you know~!"
            leo "Don't let anyone stop you from eating what you want, little guppy."
            ori "Bad advice..."

    "Leo closely inspects the catshark, circling in a slow 360 with an inquisitive hum."

    leo "Hmm, those chains... I've seen them before..."
    leo "Ah, I remember now~! You're that one fugitive that went on a cannibalistic rampage~!"
    leo "Guess we all have something in common, huh?"

    show mc shock at mc_left
    mc "???"

    ori "That's hyperbole... and I've changed."

    leo "You can't change what you've been born with, kitty~!"

    ori "I wasn't...! Conditions made me do--"

    leo "Now now, you hear that? The festival's about to start."
    leo "Bye kitty shark, we'll see you laaater~!"

    show mc o at mc_left
    mc "Wauh! Where are you taking me??"

    leo "To your friends, you silly eely billy. They've been worried sick."

    jump chapter4_festival_night


# ------------------------------------------------------------
# FESTIVAL NIGHT: RECONCILIATION
# ------------------------------------------------------------

label chapter4_festival_night:

    hide mc
    scene ch4_dialogue_night
    with dissolve

    "Leo ushers me back into the bustling, illuminated town square. Bioluminescent lanterns glow warmly across golden stalls."

    show cory upset at cory_left
    show scy default at npc_right

    cory "Guppy! Where the eel have ya been?!"

    show mc sad at mc_left
    mc "Nowhere... I was just... staring at the glow-in-the-dark anemones."

    show scy surprise at npc_right
    scy "Have you filled your stomach with anything?!"

    mc "I ate... some square jelly?"

    scy "A jelly is not a proper diet for a developing guppy like you!"

    show cory side at cory_left
    cory "We brought you smashed krill..."

    show scy proud at npc_right
    scy "Yes! I helped with the smashing, of course!"
    scy "I made sure it's digestible for your throat!"

    cory "It's the least we can do to fulfill your appetite..."

    show mc o at mc_left
    mc "...For me? You really didn't have to...! After what I... said..."

    show scy smile at npc_right
    scy "Cory also said that he's sorry!"
    scy "Though he didn't want to say it before preparing something grand for a proper apology!"
    scy "But I think you should know it, guppy! I apologize too..."

    show cory surprise at cory_left
    cory "I'm right here?!"

    show cory side_close at cory_left
    cory "But... *sigh* exactly what he said."
    cory "We're sorry for the way we reacted..."
    show cory fond at cory_left
    cory "We just wanna let you know that... we're not afraid of ya, guppy."
    cory "You're our friend."

    show scy laugh at npc_right
    scy "KAKAKA That's right Cory! And friends protect each other! Forever!"

    show mc shock at mc_left
    mc "Friends..."

    "A warm, relieved smile creeps across my face. I can't believe I've made friends as kind as this... This is a first for me."

    show mc happy at mc_left
    mc "Mm! Mr. Cory... Mr. Scyllarus... You're my friends... too!"
    mc "Thank you for... not being mad and yelling at me..."

    show mc o at mc_left
    mc "Ah, but where's Mr. Chief Whale Shark...?"

    show cory side at cory_left
    cory "Went somewhere, looks busy preparing the main event."

    leo "Then fun we shall have in the meantime~!"

    show cory surprise at cory_left
    cory "GYAH--!! Don't just sneak up on us!"

    leo "Aw, have some whimsy, would you?"
    leo "Also, look forward to the end of this festival~ They say a sacred ritual will be held."

    show mc excited at mc_left
    mc "Waouh, really?? Can't wait to see!"

    jump chapter4_festival_games


# ------------------------------------------------------------
# FESTIVAL GAMES
# ------------------------------------------------------------

label chapter4_festival_games:

    "The festival plaza is alive with bustling games and stalls."

    jump ch4_game_plankton


# --- Game 1: Plankton Catching ---
label ch4_game_plankton:

    "We arrive at a brightly lit shallow pool where hundreds of tiny, glowing planktons dart around."

    show mc excited at mc_left
    mc "Hello miss stall keeper! How do I--"

    stall1 "Just get as many as ye please."
    stall1 "Me oul self's knackered of having these feckin' loud eejits around."

    planktons "Yaya unana! Fugu you, we hate you too! Kew!"

    mc "Oh, okay then!"

    stall1 "Make sure to take bad care of 'em. Fellas keep effin' and blindin' at whoever passes."

    "Who should I play plankton catching with?"

    menu:
        "Play plankton catching with Scyllarus":
            $ ch4_game1_companion = "scy"
            jump ch4_plankton_scy

        "Play plankton catching with Cory":
            $ ch4_game1_companion = "cory"
            jump ch4_plankton_cory

        "Play plankton catching with Leo":
            $ ch4_game1_companion = "leo"
            jump ch4_plankton_leo


label ch4_plankton_scy:

    show scy proud at npc_right
    scy "Hah! Plankton catching is a discreet hobby of mine!"
    scy "We shall be victorious, guppy!"

    show mc o at mc_left
    mc "Mn, but can you catch them without crushing them with your big claws?"

    scy "...I uh... do you need them alive?"

    menu:
        "Ya I do! I want to show them off to everyone!":
            scy "Hmm! I don't think letting these pesky critters out is a wise choice...!"
            planktons "We will krill everyone! World conquest!"
            scy "My mantis radar senses something... sacrilegiously immoral within their tiny bodies!"
            show mc o at mc_left
            mc "Mm, you're right :o Why are you so full of hate, tiny planktons?"
            planktons "Kill kill kill! Hatred!! Corrupt world! Uana yaha!"
            show scy sepet at npc_right
            scy "They're too consumed by hate of how the world cruelly treats them..."
            scy "...Hah... to think I was serving someone of the same mindset..."
            scy "To think I was... at one point no different than these spiteful creatures..."
            show mc default at mc_left
            mc "Mm... but you're not who you were, Mr. Larus!"
            mc "I don't sense any more hate from you!"
            show scy smile at npc_right
            scy "I'm grateful to have your trust! But sometimes... I still--"
            planktons "Yaha naha murder! Kill kill everyone! Dismemberment!!"
            "Mr. Scyllarus's face scrunches up in mild trauma."
            scy "I'm fine...! Mother of Sea... Why must they have such foul mouths!"

        "Mmno, I want to feed it to you! (+1 Affection)":
            $ ch4_scy_affection += 1
            show scy surprise at npc_right
            scy "For me...?!"
            scy "Well... big shrimps like me don't eat critters like these anymore!"
            show mc o at mc_left
            mc "Ooo so you ate heaps of these when you were little...?"
            show scy proud at npc_right
            scy "Yes! My trainers told me they're full of nutrients to ensure a healthy, strong body!"
            scy "They made me eat thousands of them everyday!"
            show mc shock at mc_left
            mc "Thousands..?! Wouldn't that be overfeeding..?"
            scy "Uhh or was it hundreds! I don't remember too well!"
            scy "But it all got burned in the rigorous training I endured!"
            show mc o at mc_left
            mc "Does the taste of planktons... haunt you Mr. Scyllarus...?"
            scy "Hah! I won't let such measly organisms haunt me!"
            planktons "We're your worst nightmare!! Eat brains!"
            show scy sepet at npc_right
            scy "Maybe a tiny bit...!"
            show mc happy at mc_left
            mc "Oh okay... I won't feed it to you then. I'll get you something tastier later, Mr. Carus!"
            scy "It's Scyllarus!! Why does it get worse every time?!"

    "Mr. Scyllarus carefully scoops the vengeful tiny planktons into a glowing translucent jellyfish pouch."
    "The gentle gesture completely contrasts his giant razor claws."

    show mc happy at mc_left
    mc "Hehe, I never thought you could be this gentle!"

    show scy shy at npc_right
    scy "I... try my best to!"

    jump ch4_game_shooting


label ch4_plankton_cory:

    show cory side at cory_left
    cory "There sure is a lot of stuff, huh... buncha nautical nonsense."

    show mc actually at mc_left
    mc "They're not nonsense Mr. Cory!"
    mc "The one that looks like an isopod is an amphipod, it's a type of macroplankton!"
    mc "And that over there are copepods, they filter out tiny algae and feed the larger krill!"
    mc "Plus, over in that corner, there's--"

    show cory talk at cory_left
    cory "Yea yea yeah, just tell me which one's your favorite..."

    menu:
        "Get the jellyfish lookalike! (+1 Affection)":
            $ ch4_cory_affection += 1
            show cory smile at cory_left
            cory "Fan of jellyfishes, I see."
            show mc happy at mc_left
            mc "Mhm! They're all so... floaty and pretty."
            show cory side at cory_left
            cory "Yeah, I totally get it. I used to try and catch 'em too when I was little."
            cory "Until one day karma bit me in the fins..."
            show mc shock at mc_left
            mc "Oh no, did you get stung??"
            cory "Damn right I did... left me a permanent imprint."
            planktons "Serves you right freshie!! Get stung more!"
            "Mr. Cory scoops up a cluster of planktons into his fin, capping it with his other fin."
            "The gesture muffles their angry screams into tiny chipmunk squeaks."
            show cory fond at cory_left
            cory "At that time I was cryin' so loud, it put a smile on my little sister who'd been sick all week..."
            cory "It was her first smile in a while."
            cory "Hah... and I couldn't help but think it was all worth it in the end."
            show mc happy at mc_left
            mc "You're a great, kind older brother, Mr. Cory!"
            mc "I wish you were my papa..."
            show cory surprise at cory_left
            cory "Hah... if I'd known you sooner I probably would..."
            cory "Wait... that sounded wrong."
            show mc happy at mc_left
            mc "Yaa! Be my papa Mr. Cory! :D"
            "The tiny screeches from Mr. Cory's fin faintly sound like 'Be their papa!' chanted repeatedly."
            show cory side_close at cory_left
            cory "I'd... have to think about it, guppy."

        "The cockroach looking plankton reminds me of you":
            show cory unimpressed at cory_left
            cory "Me??"
            show mc happy at mc_left
            mc "Ya! If you were a plankton, you'd be an amphipod!"
            cory "Aye, I ain't that chopped!"
            show cory smile at cory_left
            cory "Well, if you were a plankton... you'd be that one, guppy."
            "Mr. Cory points at a floating blue button (Porpita porpita), its tentacles swaying peacefully."
            show mc o at mc_left
            mc "The Porpita porpita? :o"
            cory "Yep, all bright and about... A little odd looking, the name suits ya too in a way."
            planktons "If the word hate was engraved on every nanoangstrom of--"
            "Mr. Cory claps his fins together, silencing them instantly."
            cory "These tiny things sure have big mouths, ay?"

    jump ch4_game_shooting


label ch4_plankton_leo:

    leo "Catching helpless little beings, huh? I'm skilled at that~!"
    leo "We'll catch as many as we can, little guppy."

    planktons "We'll tear your flippers to shreds!"

    leo "Wow, feisty are we?"

    menu:
        "Do you eat planktons, Leo?":
            leo "Hmm, if I'm bored, yes."
            leo "I like the feeling of them crawling their futile way down my innards..."
            leo "It sure is a tickling feeling~! Like drinking carbonated water."
            show mc o at mc_left
            mc "Ooo like drinking soda? Now I'm curious..."
            leo "Why don't you try some?"
            show mc pout at mc_left
            mc "Me...? Would I get a tummy ache from it? :("
            leo "You won't find out unless you try~"
            leo "I'm sure your golden treasure would protect you from harm."
            "Leo scoops up a large puddle of planktons in her wide flipper."
            planktons "We'll eat your guts!! We'll kill you slowly from inside!!"
            show mc shock at mc_left
            mc "*gulps*..."
            leo "Now say ah~"
            show mc holdcry at mc_left
            mc "Nnguh..!! Fine!"
            "Taking a deep breath, I gulp down the water from Leo's flipper."
            mc "Mnhah--! I... I drank it!"
            leo "Yaay~! Congratulations to you!"
            mc "Mnnngh... they taste weeeeeird D:"
            leo "Humans actually benefit from eating these... they're nutrient rich~!"
            show mc shock at mc_left
            mc "Whauht..?! Really??"
            leo "The tiny critters... they were just bluffing. Like chihuahuas... all bark and no bite."
            show mc pout at mc_left
            mc "Why didn't you start with that..!"
            leo "I want to see you make faces I haven't seen~ Is that so wrong?"

        "Why are the planktons so angry?":
            leo "Hmm... when a creature is weak, they bark to scare predators away."
            leo "Spewing pointless threats... yet harboring zero impact."
            leo "Much like a chihuahua, all bark no bite."
            planktons "Don't listen to the lunatic!! We can kill and tear your body inside out!!"
            show mc o at mc_left
            mc "Nnn... I don't know who to trust..."
            leo "Still don't believe me? Watch this~!"
            "Leo tips the entire bowl of planktons and swallows them in one massive gulp."
            show mc shock at mc_left
            mc "WAOUH..! Is... that really okay?? o.o"
            stall1 "Oh thank Jesus, Mary and Joseph! Now we're suckin' diesel! I owe ye a piece of me life!"
            leo "Hah~ see? Nothing's happening to me."
            leo "Planktons are nutrient-rich superfood."
            mc "Ah, but now we don't have any planktons to catch..."
            leo "Hehe oopsies~ We can find more in the wild later on~"

    jump ch4_game_shooting


# --- Game 2: Clam Shooting Gallery ---
label ch4_game_shooting:

    "Next, we come across a shooting gallery booth."
    "Colorful clam shells line four shelves—five clams on each, twenty targets in total."
    "Three squid-shaped wooden shooters rest firmly on mounts."

    show mc o at mc_left
    mc "How does this game work? :o"

    stall2 "Velkommen, young guppy! Zhe rules are super simple."
    stall2 "You see zhe shells up there? I give you 8 pearl bullets. You shoot down as many clams as you can."
    stall2 "But it only counts if zhe clam actually drops off zhe shelf!"
    stall2 "We tally your score, and you pick your prize based on your tier!"

    "A large sign displays the prizes:"
    "TIER 1 - SEAWEED SNACK (20 points)"
    "TIER 2 - BIOLUMINESCENT BUBBLE BLOWER (40 points)"
    "TIER 3 - BLOBFISH PLUSHIE (80 points)"

    show mc excited at mc_left
    mc "Oooou wunderbar!"

    "Who should I play the shooting game with?"

    menu:
        "Play shooting game with Cory":
            $ ch4_game2_companion = "cory"
            jump ch4_shoot_cory

        "Play shooting game with Scyllarus":
            $ ch4_game2_companion = "scy"
            jump ch4_shoot_scy

        "Play shooting game with Leo":
            $ ch4_game2_companion = "leo"
            jump ch4_shoot_leo


label ch4_shoot_cory:

    show cory proud at cory_left
    cory "Here's the trick to winnin' this, guppy."
    cory "Imagine those clams are the ones who called ya weird."

    "Mr. Cory tilts his pistol toward the nearest clam, takes aim, and squeezes the trigger."
    play sound "audio/thump.mp3"
    "KLANG!"
    "The shot ricochets harmlessly off the sea rock, missing entirely."

    show cory upset at cory_left
    cory "Tch..."

    "I raise my pistol, line up the sights, and pull the trigger."
    play sound "audio/thump.mp3"
    "CLANG!"
    "The clam shell shatters and tumbles off the perch onto the sand."

    show mc happy at mc_left
    mc "Don't look back in anger, Mr. Cory :D"

    show cory smile at cory_left
    cory "Ay... alright :D"

    "Mr. Cory fires another shot... only for it to clip the edge and skip off."

    show cory upset at cory_left
    cory "GRRRR mane, these sights must be off!"

    menu:
        "Maybe you can try using my shooter (+1 Affection)":
            $ ch4_cory_affection += 1
            show mc happy at mc_left
            mc "Mmm... perhaps it's simply an issue with your pistol, Mr. Cory?"
            mc "Try taking a shot with mine!"
            "I step aside, letting Mr. Cory take over my shooter."
            show cory side at cory_left
            cory "Aight... imma try."
            "Mr. Cory squares his shoulders, locking his sight onto the target."
            play sound "audio/thump.mp3"
            "CLANG!!!"
            "The clam fractures on impact, falling clean off the shelf."
            show mc excited at mc_left
            mc "YEEHAW, there we are, Mr. Cory!! :D"
            show cory fond at cory_left
            cory "Heh. Heheh."

        "It's a pure skill issue on your part, Mr. Cory :p":
            show mc actually at mc_left
            mc "It's a pure skill issue on your part, Mr. Cory :p"
            "I lean in to adjust his grip, but Leo suddenly looms from behind."
            leo "Fufufu~ here old man, let me help you too~"
            "Leo forcibly twists Mr. Cory's elbows with mock precision."
            show cory upset at cory_left
            cory "Aight AIGHT KIDS, back off, I caught yer drift!"
            play sound "audio/thump.mp3"
            "BANG-KLANG!"
            "The round flies wild. Another miss."
            leo "Ooof... well, my work here is done. Toodles~"
            show cory side at cory_left
            cory "Can't all be sharpshooters out here in the deep, yeah?"

    stall2 "Three clams down! Not bad, young vones."
    "The vendor hands over a decorated box of dark seaweed sticks, baked crisp like Pocky."

    show cory smile at cory_left
    cory "Eat up, guppy. You earned the lion's share of 'em anyway."

    show mc happy at mc_left
    mc "Mmm okay :D"

    jump chapter4_abyssal_rite


label ch4_shoot_scy:

    show scy proud at npc_right
    scy "I was trained directly under the Empress herself, KAKAKAKA!"

    show mc o at mc_left
    mc "Pistol-trained under a pistol shrimp to use a pistol. Incredible :o"
    mc "Crustacean first, Mr. Clarus!"

    show scy smile at npc_right
    scy "You truly possess a magnificent heart, guppy!"

    "Despite his skill, his claws tremble slightly around the grip."
    "A subtle recoil washes over him with every shot, his face scrunching at the sharp crack of pressure."
    "He neatly knocks down two clams in rapid succession."

    show scy default at npc_right
    scy "Hah! It's a little unfair if a pro like me partakes in child's play! Can you do the rest, guppy?"

    leo "Quitting halfway after only two shots~?"
    leo "There's really no shame in conceding if it exceeds your capabilities, though~"

    menu:
        "It's alright! If Mr. Larus can do it, I can do it too (+1 Affection)":
            $ ch4_scy_affection += 1
            show mc actually at mc_left
            mc "Um. So accounting for the cross-current drag, salinity density..."
            mc "...and the angle of refraction through the water column..."
            leo "Also consider the margin percent for shell thickness relative to kinetic torque~!"
            show scy surprise at npc_right
            scy "I don't think you need to overthink it, guppy!"
            show mc excited at mc_left
            mc "Aough yessir!"
            play sound "audio/thump.mp3"
            "KLANG!"
            "The clam shell shatters off the stall!"
            mc "I... I nailed it!"
            show scy laugh at npc_right
            scy "Kakakaka! Splendid trajectory!"

        "Please Mr. Larus, I want that plushie :'(":
            show mc holdcry at mc_left
            mc "Nu-uh, I want that plushie! You'll get it for me, won't you Mr. Larus?"
            show scy sepet at npc_right
            "Mr. Larus grimaces, his brow furrowing as he glances back at the pistol."
            show scy proud at npc_right
            scy "Of course! Who do you think I am, guppy?"
            play sound "audio/attack_1.mp3"
            "BANG-KLANG. BANG-KLANG. BANG-KLANG!"
            "Five clams shatter off their perches in instant mechanical succession."
            scy "KAKAKAKA! This game poses no threat to a distinguished shrimp like me!"

    stall2 "Wunderbar! Wunderbar! That is a new record! Zhe plush is yours, young guppy!"
    "He hands over a giant, squishy blobfish plushie."

    show mc happy at mc_left
    mc "Yayyy this is the best day ever!"

    jump chapter4_abyssal_rite


label ch4_shoot_leo:

    leo "Eight shiny little bullets total. Four for each of us, then~"

    show mc excited at mc_left
    mc "Okay! Here Leo, pinniped first!"

    "Leo takes the pistol with lazy elegance. Without even aiming, she boops the trigger with her snout."
    play sound "audio/thump.mp3"
    "KLANG!"
    "The target shudders violently, but refuses to fall."

    stall2 "Nein, nein! You must knock ze clam completely off ze shelf, ja!"

    leo "My, my... are you quite certain this mechanism isn't rigged~?"

    menu:
        "It totally is! (+1 Affection)":
            $ ch4_leo_affection += 1
            show mc pout at mc_left
            mc "It totally is!"
            mc "Awh, I really want the bioluminescent bubble blower :("
            leo "Worry not, my darling. I can still acquire that bubble blower for you~"
            leo "Though you might want to look away for a second~"
            mc "Why, Miss Leo? :o"
            leo "Because I wouldn't want you to see me doing something terribly improper~"
            "I press both palms tightly over my eyes."
            "A soft rustle of water follows, accompanied by a suspicious heavy thud."
            play sound "audio/attack_3.mp3"
            "CLATTER-BANG-KLANG!"
            show mc shock at mc_left
            "I open my eyes. Every single clam on the shelf is now lying facedown on the seabed."
            stall2 "Huh... That's weird. Must've been ze current..."

        "No, it probably isn't":
            show mc default at mc_left
            mc "Um, the pistol gear is solid. The pearls seem okay."
            mc "Here I go!"
            play sound "audio/attack_2.mp3"
            "BANG! BANG! BANG! BANG!"
            "Four rapid shots ring out in perfect sequence, shattering four clams clean off the shelf."
            leo "You're a natural~!"

    stall2 "Congratulationz! Tier 2, der biolumineszierende Seifenblasenbläser!"

    "I dip the wand into the glowing liquid and blow a gentle stream of air."
    play sound "audio/splash.mp3"
    "A cascade of shimmering bioluminescent bubbles bursts into the water, floating around us in neon blues and purples."
    "A high-pitched, satisfied squeak escapes Leo as she twirls happily through the bubbles."

    leo "Now isn't that just enchanting... Mmhehe~"

    jump chapter4_abyssal_rite


# ------------------------------------------------------------
# THE ABYSSAL EFFIGY RITUAL (PEAK OF FESTIVAL)
# ------------------------------------------------------------

label chapter4_abyssal_rite:

    hide mc
    scene ch4_night
    with fade

    "Drums echo through the waters as the crowd gathers before the central podium."
    "Behind Chief Rin stands a colossal, terrifying statue made of pure gold—the Abyssal Effigy. Its grotesque, uncanny shape looks like an unknown abyssal beast from the darkest depths."

    rin "Dear seafolks, Freshinians... scooters, swimmers, and those who've made it for this Devout Ritual. Welcome."

    leo "Ah, it has begun..."

    rin "For generations, we have upheld this sacred tradition. These little vessels shall carry what weighs upon us. Anger. Fear. Regret. Grief. Words left unsaid and thoughts we have carried for far too long."
    rin "Tonight, we give those burdens to the sea. Speak what you wish to leave behind. Let the Abyssal Effigy hear it. Then, when the time comes, we shall send them into the deep together."

    "The crowd murmurs with devout reverence."

    rin "Before we proceed, there is one tradition left to observe."
    rin "Tonight, no one should have to face this ritual alone. Each of you may choose one companion to accompany you to the edge of the deep."
    rin "Through your effigy replica, channel your deepest sorrows. Cast it into the abyssal ocean bed and let the ocean carry away what you no longer wish to bear."

    "Who should I choose to accompany me to the edge of the deep?"

    menu:
        "Go to the abyssal ledge with Scyllarus":
            $ ch4_ritual_companion = "scy"
            jump ch4_rite_scy

        "Go to the abyssal ledge with Cory":
            $ ch4_ritual_companion = "cory"
            jump ch4_rite_cory

        "Go to the abyssal ledge with Leo":
            $ ch4_ritual_companion = "leo"
            jump ch4_rite_leo


# --- Scyllarus Abyssal Rite ---
label ch4_rite_scy:

    show mc happy at mc_left
    mc "Mr. Larus! Let's go together! :D"

    show scy surprise at npc_right
    scy "Me?! Are you sure you want to spend the peak of this festival with me?!"

    mc "Of course!"

    show scy smile at npc_right
    scy "Well, if you insist! Come on, little guppy!"

    "We receive our small golden replica effigies and swim away from the crowd, settling at the edge of the dark abyssal drop-off."

    show scy default at npc_right
    scy "So... I guess we're supposed to put our burdens into this creepy statue now!"
    "Mr. Shrimp scratches the back of his head."

    show mc o at mc_left
    mc "Are we supposed to say it out loud? :o"

    scy "I believe so. You go first, guppy!"

    mc "No! You should go first."

    show scy proud at npc_right
    scy "Me? A great soldier such as myself wouldn't be troubled by something so trivial as feelings!"

    show mc o at mc_left
    mc "Ah yeah, I forgot you were a soldier sometimes..."

    show scy default at npc_right
    scy "I worked under the Empress, little guppy. I was taught to fight, to follow orders, and to eliminate those who threatened her kingdom!"

    show mc sad at mc_left
    mc "Mnn, does that mean you've killed lots?"

    scy "I simply did what I was ordered, and I was the best among all her soldiers!"

    menu:
        "But were you happy?":
            show mc default at mc_left
            mc "But were you happy? During your time... under the Empress?"
            show scy sepet at npc_right
            scy "Of course I was! Why wouldn't I be? I served the Empress. I had a purpose. I was strong, respected, and--"
            scy "...And I guess that's all gone now."
            show mc default at mc_left
            mc "But the seafolks love you now! Nobody's throwing rocks at you anymore."
            show scy default at npc_right
            scy "You're... not wrong! I'm just not used to all of this yet!"
            scy "I am aware that the people see me as some sort of hero now. And I suppose I should be pleased."
            scy "And yet... after all the sorrow I inflicted with my very own claws... the families I exiled..."
            scy "A tiny, noisy voice inside my head just doesn't think that I..."
            show mc sad at mc_left
            mc "That you deserve... the praises?"
            show scy sepet at npc_right
            scy "Perhaps so...! I keep telling myself I must be strong. If I am strong enough, useful enough, impressive enough... then maybe I can convince myself that I deserve to be here."
            show mc default at mc_left
            mc "Mr. Larus? You don't have to prove that you're a good person every second. You can just be you!"
            show scy smile at npc_right
            scy "Just me, huh? That sounds rather frightening."
            mc "Then you can be scared too."

        "How long did you serve the Empress for?":
            scy "Since I was a little larva. I suppose you could say I spent my whole life in her service!"
            show mc o at mc_left
            mc "Waouh... I can't imagine doing one thing for your whole life."
            show scy default at npc_right
            scy "Under her command, I did a variety of things! Guarding borders, and before that... annihilation."
            show mc shock at mc_left
            mc "Wait! Annihilation...?"
            scy "Eradicating those who did not bow to the rules of Her Highness! Those who broke laws and caused chaos!"
            show mc sad at mc_left
            mc "Mr. Scyllarus... how many exactly did you kill?"
            "I see him subtly flinch. A heavy silence follows."
            show scy sepet at npc_right
            scy "....I didn't bother to keep count! Annihilation isn't something you wear proudly like a medal..."
            mc "Do you regret them?"
            scy "For killing the wrong folks? Yes... yes I do."
            scy "I became so accustomed to taking orders that I never stopped to wonder what I actually wanted."
            show mc default at mc_left
            mc "So what do you want now?"
            show scy smile at npc_right
            scy "I want to keep adventuring with you, little guppy! Stay by your side, see new places, meet new people."
            mc "Me...? You want to stay with me?"
            scy "Meeting you was undoubtedly the greatest thing that has ever happened to a great shrimp like myself."
            show mc happy at mc_left
            mc "Then you can stay with me as long as you want! :D I could use a pickle opener, hehe."
            show scy laugh at npc_right
            scy "Is that all I am to you?! A pickle opener?! Well... I suppose I shall be your most dutiful pickle opener!"

    show scy smile at npc_right
    scy "Guppy... you really have a talent for making a great shrimp say things he would rather keep to himself."

    show mc happy at mc_left
    mc "Well, someone has to!"

    "A faint, warm glow begins to pulse from Mr. Larus's effigy, absorbing his long-buried regrets."

    scy "Thank you."

    "Together, we toss our glowing effigies over the ledge, watching them drift softly into the deep abyss."

    jump chapter4_climax


# --- Cory Abyssal Rite ---
label ch4_rite_cory:

    show mc happy at mc_left
    mc "Hi Mr. Cory! :D Seems like you got your statue too!"

    show cory talk at cory_left
    cory "Sup guppy goo. Let's head over to the ledge."

    "The two of us swim to the edge of the deep sea chasm."

    show cory side at cory_left
    cory "So... what are ya tellin' the statue?"

    show mc o at mc_left
    mc "Do we have to say it out loud? :o"

    cory "Nay, I don't think we're obliged to for it to work."

    "My gaze falls down to the Effigy. Thoughts run a mile a minute. What should I put into this statue...? How Papa hasn't come back...? Or maybe Mama..."

    show cory side_close at cory_left
    cory "You know guppy... my little sister... she's just about your age."

    show mc o at mc_left
    mc "Really?? :o"

    cory "Yeah... In my head, you'd be the bestest of friends. She didn't have many to begin with... most of her life was spent being sick."
    cory "She loved picking up anything that caught her eyes, just like ya do."

    show mc happy at mc_left
    mc "Ooo I would've shared my rock collections with her!"

    show cory fond at cory_left
    cory "Pfft, yeah, she'd be thrilled."

    show mc sad at mc_left
    mc "So... where is she now? Is she still alive?"

    show cory upset at cory_left
    cory "I... sure hope she is. I ain't know nothing, guppy. It's been years... years since I last saw her."

    show mc default at mc_left
    mc "Then why don't you just search for her?"

    cory "Guh... scrap that idea. She could be anywhere in the seven seas! It'd take ages, I'd long be a peepaw!"

    show mc pout at mc_left
    mc "But you're over here helping me find a golden fish that could be anywhere too! Nnn, sounds like you actually don't want to meet her..."

    show cory upset at cory_left
    cory "Look...! Because it ain't... ain't at all that simple!"
    cory "It ain't just a matter of finding Nemo!"
    cory "You don't understand guppy, ya think it's all sunshines and rainbows do ya?!"

    show mc shock at mc_left
    mc "...!"

    show mc holdcry at mc_left
    mc "Nn... I'm... *sniff*"

    show cory surprise at cory_left
    cory "No! Nononono, hey hey shh, I didn't mean to yell at ya... I'm sorry."
    "Mr. Cory pulls me in with a gentle fin."

    show mc sad at mc_left
    mc "Why won't you let me help...? I don't get it..."

    show cory side_close at cory_left
    cory "Because I... I abandoned her, guppy."
    cory "Left her to survive alone... in saltwater."

    show mc shock at mc_left
    mc "What...?"

    cory "I had to...! Her life was on the line! Her sickness... she was never meant to be in freshwater in the first place!"
    cory "I couldn't let her suffer anymore. But sometimes... a part of me still wants to see her... as selfish as it sounds."

    "A flickering glow emits from Mr. Cory's effigy."

    menu:
        "You could've just... come along!!":
            show mc sad at mc_left
            mc "That's a very bad thing to do Mr. Cory, she must've been so scared all alone!"
            show cory upset at cory_left
            cory "Oh for Kraken's sake-- I wouldn't be here at all with you if I could just--! I didn't have the golden scale's blessing before!"
            show mc shock at mc_left
            mc "...Is... that it...?"
            mc "Mr. Cory, do you only... see me as your little sister?"
            cory "What..?! No! I care about you as you are guppy, not because of--"
            show mc holdcry at mc_left
            mc "You said you wouldn't be here if it weren't because of the scale! Does that mean once this is all over... you're going to leave me too...?"
            mc "Just like... Papa did..."
            show cory surprise at cory_left
            cory "Guppy, you know I wouldn't--!"

        "How did she get to freshwater in the first place?":
            cory "When I was your age, I was out explorin'... then I found an abandoned little egg."
            cory "We didn't realize she was saltwater, so she was sick left and right."
            cory "Until one day, her body was at its limit. So my family told me to drop her off by the border."
            cory "Ironic, ain't it...? I was the one who found her, and the one who left her behind."
            show mc sad at mc_left
            mc "If I were her, I'd rather die with my closest ones around... than be left alone."
            "I step closer to the looming abyssal ledge."
            show cory upset at cory_left
            cory "Hey, hey, Guppy, listen, you're playing a dangerous game here..."
            show mc sad at mc_left
            mc "If I jump right now... are you going to leave me too? Just like Papa did...?"
            cory "Guppy, don't you dare...!"

    jump chapter4_climax


# --- Leo Abyssal Rite ---
label ch4_rite_leo:

    leo "Out of everyone you could have chosen to spend the peak festival with... You chose me~?"
    leo "My, you must put that much trust in me... I can't help but feel flattered~!"

    "We swim away from the crowd to the dark ledge."

    leo "Have you ever confessed, guppy?"

    show mc o at mc_left
    mc "Confess...? Like tell my parents if I did something bad?"

    leo "Mhm, that's it~! This whole thing feels like a confession booth, no?"

    mc "But I've been a good child! I have nothing to confess!"

    leo "You're the happy-go-lucky type, aren't you? Always cheerful... keeping others afloat~"
    leo "Which is why I brought you a little gift~"

    "Leo pulls out a piece of fresh fish meat from under her tail."

    show mc shock at mc_left
    mc "Fish meat..?! o.o Where did you get this?"

    leo "Shh now now, no need to wonder, just eat it will you?"

    "Hesitantly, I take a bite. It's surprisingly soft, with a peculiar metallic tang."

    show mc o at mc_left
    mc "Mmn, tasted like chains..."

    leo "Mhehe, how interesting. Wondered if you ever indulge in malicious thoughts~"

    show mc actually at mc_left
    mc "Mmmm actually I often thought of skipping naps."

    leo "Mhehe, 'course you do. You're as green as a green marble~"
    leo "Every creature in this world harbors latent malice. Is there really nothing that breeds resentment within you?"

    show mc sad at mc_left
    mc "Uh... if it had to be one thing... then it's... my Papa."
    mc "He went on a suuuper long sail at sea... so long that he hasn't come home for years."

    leo "Oh~! You're just a kid, yet life treats you harshly!"

    menu:
        "Take a sad song and make it better! :D":
            show mc happy at mc_left
            mc "There are still a lot of things we can decide for ourselves!"
            mc "Like... I picked you to go with me! That means we get to choose what we want."
            leo "Nu-uh! Your genes, the environment shaping your tiny brain... those things have made every choice for you~"

        "Being with friends makes me happy!":
            show mc happy at mc_left
            mc "Mr. Cory is my papa, Mr. Larus is my big brother, and you're my sister! We're like twins!"
            mc "And besides--"

    # Glitch dramatic shift
    play sound "audio/unsettling_moment.wav"
    leo "{cps=15}{size=36}SHUT UP, you really don't understand!!{/size}{/cps}"

    "The effigy in her grasp glows violently, flickering with unstable crimson light."

    show mc shock at mc_left
    mc "...! Uh... uh............. :'"

    leo "........."
    leo ".................."
    leo "Whoops, sorry~ got carried away."

    "Her voice drops into an icy, razor-sharp whisper."

    leo "You want to know what really matters now~?"
    leo "Just be vigilant around those playfellows of yours. When push comes to shove, every creature is fundamentally selfish."
    leo "The golden fish can grant you a wish, even the impossible... They haven't told you that, have they?"

    show mc shock at mc_left
    mc "Mn... no..."

    leo "Remember earlier? They were ready to pounce on you all because you wanted to eat a little fish."
    leo "I had best friends too, once. They used to say they'd never abandon me. But in the end... I was left to rot all alone."
    leo "You will be too. You will always... end up alone."

    show mc holdcry at mc_left
    mc "No..! Mr. Cory and Larus won't desert me!!"

    leo "...Then let's put that to the test, shall we~?"
    leo "Step off the edge. Cast yourself into the abyss down there~"
    leo "Let's see if they truly bother to come searching for you."

    jump chapter4_climax


# ------------------------------------------------------------
# CHAPTER CLIMAX: THE LEAP INTO THE ABYSS
# ------------------------------------------------------------

label chapter4_climax:

    hide mc
    scene ch4_night
    with dissolve

    "At the ledge of the great abyss, hundreds of glowing effigies are cast into the dark void by the seafolks."
    "They drift down like falling stars into an endless trench."

    show cory surprise at cory_left
    show scy surprise at npc_right

    "Then suddenly, amidst the sinking effigies..."
    play sound "audio/mysterious_golden_looking.wav"

    "A brilliant, blinding pulse of radiant rainbow-gold flashes from the dark ocean floor below!"

    show mc shock at mc_left
    mc "THE GOLDEN FISH!!"

    "Not the fake gold of the village. Not the dull gold of the effigies."
    "It is the real, shimmering, wish-granting golden fish!"

    "In that split second, everything else blurs into complete white noise."
    "Papa's words echo violently in my chest:"
    "{i}'Bring home the rarest fish in the sea...'{/i}"

    show mc serious at mc_left
    mc "I must get it... I must get it, no matter what!!"

    play sound "audio/splash.mp3"
    "With zero hesitation, I leap straight off the ledge, throwing myself into the bottomless abyss!"

    show cory upset at cory_left
    show scy shock at npc_right

    cory "GUPPY--!!!"

    scy "NO! GUPPY, WAIT!!"

    leo "What are we waiting for? We've got to go after them~!"

    "Without a second thought, Mr. Cory, Scyllarus, and Leo plunge straight into the dark void after me."

    scene black with fade
    stop music fadeout 2.0

    "{i}There were faint shouts ringing in the back of my head.{/i}"
    "{i}Amidst all of them, the loudest ones sounded familiar...{/i}"
    "{i}Before I knew it, I was already falling.{/i}"
    "{i}Down and down and down into the endless dark...{/i}"

    "{i}'It's dark...'{/i}"
    "{i}'It's so dark in here...'{/i}"
    "{i}'I can't be scared now...!!'{/i}"
    "{i}'I can't go back now...'{/i}"

    $ ch4_chapter_complete = True

    "To be continued in Chapter 5..."

    return
