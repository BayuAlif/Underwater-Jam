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
        "Face the peak of the festival and cast your burdens together",
        min_affection=2
    )
    $ ch4_ritual_companion = _return

    if ch4_ritual_companion == "scy":
        jump ch4_rite_scy
    elif ch4_ritual_companion == "leo":
        jump ch4_rite_leo
    else:
        jump ch4_rite_cory

label ch4_rite_scy:

    show screen ch4_affection_hud("scy")

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

    show screen ch4_affection_hud("leo")

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

    play sound "audio/ambience/unsettling_moment.ogg"
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

    show screen ch4_affection_hud("cory")

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
