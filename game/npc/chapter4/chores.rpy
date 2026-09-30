label ch4_chore1_seaweed:

    $ current_area = "gathering_grounds"

    hide mc
    scene ch4_festival_day
    with dissolve
    $ focus()
    $ focus()

    show rin talk
    rin "May you be of aid with gathering seaweeds and corals young one?"

    show mc excited at mc_left
    mc "Sure! Are the colors up to us to pick?"

    show rin smile
    rin "Yes, yes whatever pigment caught your eyes most.."
    rin "We need them to decorate the sacred statue"

    mc "Yaaay okay! I'll bring lots for you!"

    show rin o
    rin "Keep it balanced yes? We don't want to anger the ocean more than we already have.."

    $ focus()
    hide rin
    hide mc
    call screen ch4_companion_select(
        "Choose who to gather seaweeds with!",
        "Each companion offers a unique bonding moment"
    )
    $ ch4_chore1_companion = _return

    if ch4_chore1_companion == "scy":
        $ ch4_add_affection("scy")
        jump ch4_chore1_scy
    elif ch4_chore1_companion == "cory":
        $ ch4_add_affection("cory")
        jump ch4_chore1_cory
    else:
        $ ch4_add_affection("leo")
        jump ch4_chore1_leo

label ch4_chore1_scy:

    show screen ch4_affection_hud("scy")
    $ focus()
    $ focus()
    show scy proud at npc_right
    scy "Lay it on me!! My eyes are good at picking the freshest of seaweeds!"

    show mc o at mc_left
    mc "I've always been curious.. How do you see the with your super revolutionary 12 colored vision?"

    show scy smile at npc_right
    scy "It's Scyllarus! And.. hmm!"
    scy "Perhaps we can play a little game, my comrade"

    show mc excited at mc_left, jumpmc(windup=0.2, power=0.7, airtime=0.6)
    pause 0.6
    mc "A game?! What game? I wanna play! :D"

    scy "I spy with my little eyes!"
    scy "I believe it would be easier for you to understand!"

    show scy smile at npc_right, walkto(rightish, steps=2, walktime=0.7, bounce=0.2, sway=0.15)
    pause 0.7
    show scy smile at npc_right

    mc "ooo okay! I go first"
    mc "I spyyyy with my little eyeeees..!"
    $ focus()
  

    menu:
        "A bunch of swaaaying red branch-y guys":
            $ focus()
            show scy surprise at npc_right, jumpmc(windup=0.15, power=0.5, airtime=0.5)
            pause 0.5
            scy "Hm! A plumose coraline!"
            show mc happy at mc_left
            mc "ding ding ding you're spot on! So cool o.o"
            show scy proud at npc_right
            scy "Through these eyes of mine, red is a very prominent contrast color!"
            scy "It's all lustrous and shiny for me!"
            show scy proud at npc_right
            mc "Like… in a kaleidoscope?"
            scy "I'm not sure of this kaleidoscope you speak of!"
            scy "But if it reminds you of said thing perhaps you're right KAKAKA!"
            mc "Hehe maybe I can try and find you one mr Syllarus! I'm sure you'll love it!"
            "I wonder if he'll get dizzy and faint if he were to see a kaleidoscope from the overwhelming colors he would see.. Can shrimps faint from eyestrain I wonder… :o"
            scy "Even so.. I can't distinguish between what others call.. yellow orange and orange.."
            scy "Most of my vision goes to UV sightings!"
            show scy default at npc_right, walkto(rightish, steps=2, walktime=0.8, bounce=0.15, sway=0.1)
            pause 0.8
            show scy default at npc_right
            "Mr Scyllarus then looks over to the queued dancing corals. Grazing them with a careful gentle sway of his claw."
            show scy default at npc_right
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
            $ focus()
            $ ch4_add_affection("scy")
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

    show mc pout at mc_left, jumpmc(windup=0.2, power=0.35, airtime=0.5)
    pause 0.5
    mc "glowing..? But I can't see the glooow Mr Larus! :("
    show mc pout at mc_left

    scy "Oh right! Fine, I shall guide you through it then!"
    $ focus()

    $ ch4_chore1_done = True
    hide screen ch4_affection_hud
    hide mc
    hide scy
    with dissolve
    jump ch4_chore_explore_hub

label ch4_chore1_cory:

    show screen ch4_affection_hud("cory")
    $ focus()
    $ focus()

    show cory talk at cory_left
    cory "Plucking seaweeds? I got ya guppy!"
    cory "Which colors are we pickin?"

    show mc excited at mc_left
    mc "Mmm I like orange..! And blue.. Oh oh pink coral too! And a little bit of pastel purple.."

    show cory smile at cory_left
    cory "Woah you got a whole palette over there…!"
    cory "But hey I dig orange too"

    show mc happy at mc_left, walkto(centerleft, steps=2, walktime=0.7, bounce=0.2, sway=0.15)
    pause 0.7
    show mc happy at mc_left
    mc "yay! Let's pick on the oranges one first then :D"

    "Me and Mr. Cory took our time in picking the best fluorescent color of the seaweeds"

    show mc happy at mc_left
    show cory smile at cory_left
    show cory side at cory_left, walkto(centerleft, steps=2, walktime=0.8, bounce=0.1, sway=0.1)
    pause 0.8
    show cory side at cory_left
    cory "You know.. pickin corals and seaweeds like this"
    cory "Is it quite comforting yeah?"
    $ focus()

    menu:
        "Mm! It's like… plucking fleas from a wild cat.":
            $ focus()
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
            show cory fond at cory_left, walkto(centerleft, steps=1, walktime=0.5, bounce=0.1, sway=0.1)
            pause 0.5
            show cory fond at cory_left
            cory "Stay weird little guppy, I mean it."

        "Mm! It's like drawing!":
            $ focus()
            $ ch4_add_affection("cory")
            show cory talk at cory_left
            cory "Drawing huh..? You an artist?"
            show mc happy at mc_left
            mc "Mhmm! I draw in my free time! I draw the fishes I see and document them! Their behavior and details like that"
            show cory proud at cory_left
            cory "*whistle* You never cease to amaze me"
            show mc excited at mc_left, jumpmc(windup=0.2, power=0.6, airtime=0.6)
            pause 0.6
            mc "Yaa other than to be a fish, I also want to be a book author! And and a marine biologist!"
            show mc excited at mc_left
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

    $ focus()
    $ ch4_chore1_done = True
    hide screen ch4_affection_hud
    hide mc
    hide cory
    with dissolve
    jump ch4_chore_explore_hub

label ch4_chore1_leo:

    show screen ch4_affection_hud("leo")

    show leo default at npc_right, walkto(rightish, steps=2, walktime=0.8, bounce=0.15, sway=0.2)
    pause 0.8
    show leo default at npc_right
    $ focus()
    leo "Ooo hehe how fun~! I like picking flowers"
    leo "Tell me what's your favorite flower, little guppy?"

    show mc o at mc_left
    mc "Mmm.. I often see and pick lots of wildflowers on my walks.. So it's probably it!"
    show leo niko
    leo "Wildflowers huh..? How very fitting of you~!"
    $ focus()

    menu:
        "What about you? What's your favorite flower?":
            $ focus()
            $ ch4_add_affection("leo")
            show leo default
            leo "Hmm.. I think it would be.. the Night shade.. Familiar?"
            show mc o at mc_left
            mc "No I don't think I've heard of it.. What's it like?"
            show leo niko
            leo "Ah it's a flower of gorgeous purple shade.. My favorite part? The little flecks of yellow in the center"
            show mc happy at mc_left
            mc "Yellow and purple… it's complementary colors right? I can see why you find them pretty :D"
            show leo smile #dengan animasi jumpmc(windup=0.1, power=0.45, airtime=0.45)
            leo "ding ding ding~! You're right! Very perceptive aren't you?"

        "Are you going to eat me? :o":
            $ focus()
            show leo sad
            leo "Eat you…? Oh no~ humans were never on the menu"
            leo "What rumors have you been hearing, hm?"
            show mc o at mc_left
            mc "I heard that sea leopards can eat humans if they want!"
            show leo niko
            leo "While it might be paaaartially true.. Doesn't mean I'm eating every human I see.."
            show leo smile
            leo "My appetite lies in quenching curiosity, guppy"
            show mc happy at mc_left
            mc "Mm! I totally get it, the satisfaction of knowledge is incomparible!"

    show mc o at mc_left
    mc "Ah! we're getting a little sidetracked here.."

    show leo ehe
    leo "Mhehe it's fine we're allowed to have fun every now and then no?"
    leo "Just sit back and relax little guppy.. I know you've been through a lot.."

    show mc pout at mc_left
    mc "Mnn.. but we can't slack off can we?"
    mc "The festival is just.. tonight! um.. How many hours til then?"

    show leo sad
    leo "Hmm counting time would do us no fun.."

    show mc sad_hu
    mc "But but the golden fish! It'll stray super far too if we take long :("

    show leo default at npc_right, walkto(rightish, steps=2, walktime=0.8, bounce=0.1, sway=0.1)
    pause 0.8
    show leo default at npc_right
    leo "Would you believe me If I were to say that.."
    show leo smile
    leo "The goldenfish.. It moves only when you move."

    show mc shock at mc_left
    mc "Huh? So when I'm in one place it'll always be nearby?"

    show leo ehe
    leo "Mhm, just a theory though.. a sea theory"
    $ focus()

    $ ch4_chore1_done = True
    hide screen ch4_affection_hud
    hide mc
    hide leo
    with dissolve
    jump ch4_chore_explore_hub

label ch4_chore2_stand:

    $ current_area = "stall_construction_site"

    hide mc
    scene ch4_festival_day
    with dissolve
    $ focus()

    show rin talk
    rin "Can I trust your hands on assembling these materials into stalls, young one?"

    show mc o at mc_left
    mc "mm I can try..! But I'm going to need a hand from my friends."

    show rin smile
    rin "Do whatever shall make this easier for you."
    rin "If you need anything, I'll be around the corner, do be careful."
    hide rin

    $ focus()

    hide mc
    call screen ch4_companion_select(
        "Choose who to build the stands with!",
        "Each companion offers a unique bonding moment"
    )
    $ ch4_chore2_companion = _return

    if ch4_chore2_companion == "scy":
        $ ch4_add_affection("scy")
        jump ch4_chore2_scy
    elif ch4_chore2_companion == "cory":
        $ ch4_add_affection("cory")
        jump ch4_chore2_cory
    else:
        $ ch4_add_affection("leo")
        jump ch4_chore2_leo

label ch4_chore2_scy:

    show screen ch4_affection_hud("scy")
    $ focus()

    show scy laugh at npc_right
    scy "Kakaka, deal then, guppy!"

    show mc happy at mc_left
    mc "Yayay let's work together mr Cy–Clarus-"
    
    show scy default om 
    scy "I'll set up the stall, you handle the decorations, understood!!"

    show scy proud at npc_right, walkloop
    show mc excited at mc_left, jumpmc(windup=0.15, power=0.5, airtime=0.5)
    pause 0.5
    show mc excited at mc_left
    mc "Ay ay captain!!"

    "Mr. Shrimp worked insanely efficient. Like machines, even."
    show scy proud at npc_right

    show mc shock at mc_left, jumpmc(windup=0.1, power=0.8, airtime=0.5)
    pause 0.5
    mc "WOAH that's zippy!!"
    show mc shock at mc_left

    show scy proud at npc_right
    scy "Ha! Of course, I've been drilling under her highness since I was a mere kid!"
    scy "This is nothing… but duck soup!"

    show scy sepet at npc_right
    scy "...."

    show scy sepet at npc_right, vibrate(intensity=1)
    pause 0.4
    show scy sepet at npc_right
    "Despite his boastful words, I could catch him… less energized?"

    show mc o at mc_left
    mc "... Um you don't seem like yourself, Mr. Shrimp.."

    show scy surprise at npc_right, jumpmc(windup=0.15, power=0.45, airtime=0.5)
    pause 0.5
    scy "...? Am I?"
    scy "I'm running on all cylinders!!"
    show scy surprise at npc_right

    show mc pout at mc_left
    mc "No, no, that's not what I meant at all."

    "Mr. Shrimp pauses, his movement coming into a sudden halt."

    show scy sepet at npc_right
    scy "I don't know. Feels like.. I'm losing my drift sometimes!"
    show scy shy 
    scy "Guess what im trying to say is…  it feels strange when im no longer in duty?"
    scy "Hard to even function like a normal seafolk."

    show mc o at mc_left
    mc "Oooo…."

    show scy shy #dengan animasi sink
    scy "Once this journey ends, I got no clue where the current's supposed to take me.."
    $ focus()

    menu:
        "Take your time, Mr. Shrimp!":
            $ focus()
            $ ch4_add_affection("scy")
            show mc o at mc_left
            mc "I don't know how it feels… to lose your purpose,"
            show mc sad 
            mc "I don't know how you're feeling right now…"
            show mc happy #with jumpmc
            mc "But the ocean is huge! And we're travelling around right now."
            show mc default
            mc "Maybe what you need to do is… finding out what you actually like doing."
            show mc exited #with jumpmc
            mc "Or maybe you could just stick around with me forever! Problem solved :D"
            show scy surprise at npc_right
            scy "...! THATS A BRILLIANT OBSERVATION GUPPY!"
            show scy laugh at npc_right
            scy "Kakaka! I'll bear that in mind."

        "You should be grateful, Mr.Shrimp!":
            $ focus()
            show mc happy at mc_left #dengan animasi jumpmc
            mc "Not working means more time to play!"
            show mc sad
            mc "Other grown ups have to work every single day and they look suuuper tired,"
            show mc happy
            mc "So you should be grateful and happy :D"
            show scy smile at npc_right
            scy ".. yeah. Yeah, you're right!"
            show scy laugh
            scy "Guess I'm just out of the line of fire and complaining about the weather!"
            scy "Bad look on me, guppy!"
            

    "The stand is finally completed."

    show mc excited at mc_left, walkto(centerleft, steps=2, walktime=0.7, bounce=0.2, sway=0.15)
    pause 0.7
    mc "WOAHH this turned out way cooler than i thought!"

    show scy proud at npc_right, jumpmc(windup=0.15, power=0.35, airtime=0.45)
    pause 0.45
    show scy proud at npc_right
    scy "Hmph!! I'll call this… a crustaseanship!!"

    show mc happy at mc_left
    mc "With.. guppy's assistance :D!"
    $ focus()

    $ ch4_chore2_done = True
    hide screen ch4_affection_hud
    hide mc
    hide scy
    with dissolve
    jump ch4_chore_explore_hub

label ch4_chore2_cory:

    show screen ch4_affection_hud("cory")
    $ focus()
    show cory talk at cory_left
    cory "Ay, gimme a hand with this frame, guppy!!"

    show mc excited at mc_left
    pause 0.7
    show mc excited at mc_left
    mc "Waouh on it!"

    show cory smile at cory_left
    cory "Aand here. Hold this ends steady when i tie the knots."

    show mc excited #dengan jumpmc
    mc "Moremoremore mr. Cory!!"

    show cory smile_hu #dengan surprise
    cory "Woah easy there, you're really excited, huh?"

    show mc happy at mc_left, jumpmc(windup=0.15, power=0.45, airtime=0.5)
    pause 0.5
    mc "Mhm! this is my first festival ever,"
    show mc happy at mc_left
    mc "Have you ever been to a festival, Mr Cory?"

    show cory side at cory_left
    cory "Ay… used to spend days around the Samba festival…"

    show mc o at mc_left
    mc "Samba festival? What's that??"

    show cory talk at cory_left
    cory "Ah, it's an annual celebration back Down in the Southern Reefs."
    cory "Wild stuff. You got fishfolks dancing around in these massive glowing anemone suits.."

    show mc shock at mc_left, jumpmc(windup=0.1, power=0.9, airtime=0.55)
    pause 0.55
    mc "MASSIVE ANEMONES?"
    show mc shock at mc_left

    show cory proud
    cory "Yeah. Massive, vibrant, glowing anemones.."
    cory "And sea percussion pounding so hard you could feel the vibration through your fins."
    show cory smile_hu
    cory "Type shrimp you don't forget easily,"

    show mc happy at mc_left
    mc "Oooh I'd like to visit your house someday! :D"

    show cory side_close at cory_left
    cory "Well… aint sure about that, guppy."
    cory "Truth is, I haven't stepped back home in a long while."

    show mc o at mc_left
    mc "Why?? :0"
    
    show cory talk 
    cory "It's because my sis-"
    show cory side 
    cory "ay nevermind."
    cory "My siblings… they all made something big of themselves."
    show cory talk_hu
    cory "One's a freshwater guard commander, another runs a pearl merchant."
    show cory side_close #dengan animasi sink
    cory "And there's me, just drifting around, taking whatever odd jobs I can find."
    cory "Feels like if i show my face back home like this… I'd be just a disappointment… "
    $ focus()

    menu:
        "Well, isn't that just natural?":
            $ focus()
            show mc o at mc_left
            mc "If you siblings are doing great and you're just doing odd jobs.."
            mc ".. it's natural that you feel a bit disappointed, right?"
            show cory side at cory_left
            cory ".....yeah."
            show cory side_close #dengan animasi vibrate
            cory "Hearing this straight from a little kid hits hard…"
            cory "But you aint wrong, guppy."

        "Im sure your family waits for you":
            $ focus()
            $ ch4_add_affection("cory")
            show mc happy at mc_left
            mc "I don't think your family cares about your job, Mr. Cory."
            mc "If it were me, I'd just be happy to see you come home safe and sound."
            show cory surprise at cory_left
            cory "....!"
            show mc excited at mc_left
            mc "AND! I want to go dance at that Samba festival with you someday…"
            mc "..so you have to go make up with your family first!"
            show cory side_close #dengan animasi vibrate
            cory "............"
            cory "HIC, guppy my little baby guppy…"
            show cory fond at cory_left
            cory "*Sniff* Thank you.. I needed to hear that.."

    "The stand is finally completed."

    show mc happy at mc_left, vibrate(intensity=0.7)
    pause 0.5
    show mc happy at mc_left
    mc "Phew! My arms are completely dead… but we actually pulled it off!"

    show cory smile at cory_left
    cory "Ay, we are the dream team, guppy."
    $ focus()

    $ ch4_chore2_done = True
    hide screen ch4_affection_hud
    hide mc
    hide cory
    with dissolve
    jump ch4_chore_explore_hub

label ch4_chore2_leo:

    show screen ch4_affection_hud("leo")
    $ focus()

    show leo niko
    leo "Hee hee! Lets construct this stand together~"

    show mc excited at mc_left, jumpmc(windup=0.15, power=0.45, airtime=0.5)
    pause 0.5
    show mc excited at mc_left
    mc "Mhm. Time to roll!"

    "We set to work side-by-side, joining the timber as the midday light filtered through the festival grounds."

    show leo default at npc_right
    show mc o at mc_left
    mc "Just a fleeting thought…"
    show mc serious_hu
    mc "... but isn't the name 'Leo' usually belonging to suuper famous people!?"
    mc "Like Leonardo da Vinci! Leo Tolstoy! Leonel Messi! "

    show leo niko
    leo "It's.. Lionel~"

    show mc shock at mc_left
    mc "Hum yeah!! Wait, how do you even know about Mr. Lionel Messi :0"

    show leo ehe
    leo "Hee-hee~ never overlook my knowledge, twin~"

    show leo default at npc_right, walkloop
    pause 1.0
    show leo default at npc_right
    "Leo glides into action with sleek grace.. With surprising power in those long flippers."
    "Joint pegs are hammered and heavy timber snaps into place."
    show leo default at npc_right, jumpmc(windup=0.1, power=0.3, airtime=0.4)
    pause 0.4
    show leo default at npc_right
    "I guess this isn't the first time for Leo building the stand?"
    $ focus()

    menu:
        "Have you participated in this festival before Miss Leo?":
            $ focus()
            show leo niko
            leo "... pretty much~"
            show leo default
            leo "All the seafolk… so many seafolk…"
            show leo smile
            leo "Tail in tail through their little festival life~"
            leo "Pretending its all about helping each other~"
            show mc o at mc_left
            mc "Pretending..? :0"
            show leo niko
            leo "Ah, what i mean is… purely selfless virtue is merely an illusion~"
            leo "Strip away the smiles, and at the end of the day, every single creature.."
            show leo smile
            leo "... is ultimately carving their path through their own current~."
            show mc sad at mc_left
            mc "mnn you mean that… everyone is living only for the things they like?"
            show mc happy #dengan animasi jump
            mc "That's not true, at all! You can clearly see how genuine my friends are with me :D"
            show leo niko
            leo "Hee hee. If you say so~"

        "You're so cool :0":
            $ focus()
            $ ch4_add_affection("leo")
            show leo ehe
            leo "Hee-hee~ you're fully capable of this, too, twin~"
            show leo sad
            leo "Or well.. You could, if you weren't so accustomed… "
            leo "... to having your fin held through every tiny wave~"
            show mc o at mc_left
            mc "Um… but mr cory and mr shrimp are just helping me out."
            show leo default
            leo "Of course, of course~"
            show leo smile
            leo "I'm suggesting it's not good to always rely on someone else,~"
            leo "How will you ever survive when you're on your own~"
            show mc shock at mc_left
            mc "Gulp……."

    "The stand is finally established."

    show mc happy at mc_left, jumpmc(windup=0.15, power=0.45, airtime=0.5)
    pause 0.5
    show mc happy at mc_left
    mc "That's actually pretty easy!"

    show leo niko
    leo "See? I told you that you've got it in you~"
    $ focus()

    $ ch4_chore2_done = True
    hide screen ch4_affection_hud
    hide mc
    hide leo
    with dissolve
    jump ch4_chore_explore_hub
