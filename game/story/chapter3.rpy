default ch3_rainbow_algae = 1
default ch3_red_seaweed = 0
default ch3_bunny_family_lead = False
default ch3_bunny_trusts_mc = False
default ch3_bunny_trusts_cory = False
default ch3_bunny_received_algae = False
default ch3_bunny_shrimp_apologized = False
default ch3_empress_battle_result = None
default ch3_dunge_result = None
default ch3_empress_defeated = False
default ch3_scyl_proposal = None
default ch3_golden_scale_found = False
default ch3_bunny_path_opened = False
default ch3_chapter_complete = False

label chapter3_start:

    $ current_chapter = 3
    $ current_cycle = "day"

    hide mc
    scene ch3_day
    with fade

    "The sea fills my line of sight with overwhelmingly bright pretty colors. My gaze erratically jumps from one color to another as we continue to swim further. From parrot fishes, sparkly elvis worms to rainbow open brain corals. There's way too many stuff to focus on!"

    show mc excited at mc_left
    show cory side at cory_left

    cory "heh.. Yer eyes been flying everywhere since we got here"
    cory "Don't ya get dizzy?"

    mc "ohmigosh!! Is that coral dancing?! Did you see that, Mr Cory?! I think that's the Spanish dancer!"

    show cory fond at cory_left
    cory "So excited, can't even hear me huh.."

    show cory side at cory_left
    cory "Though I must admit that this is some otherworldly beaut going on"

    show shrimp proud at npc_right
    shrimp "Right?! Feast your eyes upon the neverending beauty that is sea!"

    show cory side at cory_left
    cory "To think your empress’ been gatekeepin all this.. kinda messed up to think about"

    show shrimp sepet at npc_right
    shrimp "But she's not entirely wrong either! Most fish criminals are freshwater types!"

    show cory side at cory_left
    cory "Ay.. Sure, being careful is one thing.."
    cory "But pushing that stereotype into every freshwater is a whole different thing"

    show shrimp default 
    shrimp "Mm.. well! It's the daughter that just got promoted into empress!"
    shrimp "The former queen that saved my life had dethroned herself not long ago"
    shrimp "So she's still trying out new rules that feel fitting!"

    show cory side at cory_left
    cory "New ruler's a kid? That checks out.."

    cory "About time somefish teaches em a lesson then"
        
    show shrimp surprise
    shrimp "....!"
    shrimp "Wait! Why are you crying comrade?!"

    show cory side at cory_left
    cory "Huh? I ain't crying! Are you guppy?"

    show mc o at mc_left
    mc "Me? Why would I be?"

    show shrimp surprise
    shrimp "But I feel the vibration of someone crying!"

    "nngueeeh.."

    show cory side at cory_left
    cory "Wait, I hear it too..!"

    show shrimp default 
    shrimp "What if it's another one of golden fish's unfortunate victims?!"

    show mc o at mc_left
    mc "oh no! We have to find them!"

    show cory side at cory_left
    cory "Everybody's been gloomy lately huh"

    jump chapter3_reef_exploration

label chapter3_reef_exploration:

    hide mc
    scene ch3_dialogue
    with dissolve

    show dunge default at npc_right
    dunge "Well, well. Ain't seen a river guppy 'round these parts before."

    show mc excited at mc_left
    mc "Whoa, a crab that talks!"

    show dunge smile at npc_right
    dunge "Heh. Everything talks down here, kid. You'll get used to that too."

    show hawk default at npc_right
    hawk "Oi, quit hoggin' the current, Dunge."

    show dunge yeesh at npc_right
    dunge "Yeesh, alright, alright."

    show cory fond at cory_left
    cory "...Seems like this place has its fair share of characters."

    show bunny default at npc_right

    bunny "Oh! New faces! Welcome, welcome!"

    show mc happy at mc_left

    mc "Hello! I'm glad to meet you!"

    show bunny sad at npc_right

    bunny "I'm happy to see new faces too..."

    mc "Hm? Is something wrong?"

    # --- SEA BUNNY INTERACTION ---
    show bunny sad 
    bunny "nghuuuu.. ueeeh… ueeh!!!!"

    show mc shock 
    mc "huh..? What's wrong?"

    show bunny sad 
    bunny "uuu.. shiku shiku.. My family.. They took them!!"

    show shrimp default_om 
    shrimp "And who exactly is this 'they'?!"

    show bunny scared 
    bunny "GYAAA IT'S THEM IT'S THEM!!"

    "The bunny-shaped slug lets out a high-pitched scream."
    "Mr. Shrimp's presence sends her scurrying away to curl and hide behind a coral."

    show shrimp surprise 
    shrimp "Huh…?!"

    show mc o
    mc "Can you specify who or what took your family?"

    show bunny scared 
    "The sea bunny seems to refuse to answer anything with Mr. Shrimp nearby."

    menu:
        "Who should ask the sea bunny?"

        "Ask her as MC":
            jump ch3_bunny_as_mc

        "Ask her as Cory":
            jump ch3_bunny_as_cory

        "Ask her as Scyllarus":
            jump ch3_bunny_as_shrimp



label ch3_bunny_as_mc:

    show mc happy
    mc "Don't be scared, sea bunny!"

    mc "Mr. Shrimp is far away now!"

    show bunny scared
    bunny "He's.. still around though.."

    show mc happy
    mc "It's okay! I won't let him get near you!"

    show bunny sad
    bunny "nguu.. okay I trust you…"
    $ ch3_bunny_trusts_mc = True

    menu:
        "What do you want to ask her?"

        "What happened to your family?":
            jump ch3_bunny_family

        "Why are you scared of Mr. Shrimp?":
            jump ch3_bunny_shrimp

        "Do you need a hug? (Give rainbow algae)" if ch3_rainbow_algae > 0:
            jump ch3_bunny_hug

label ch3_bunny_as_cory:

    show bunny scared
    bunny "He's.. still around though.."

    show cory side at cory_left
    cory "Aw, don't worry. I'll keep my distance."

    show bunny sad
    bunny "nguu.. okay..."
    $ ch3_bunny_trusts_cory = True

    menu:
        "What do you want to ask her?"

        "What happened to your family?":
            jump ch3_bunny_cory_family

        "I'm sorry to hear about your family.. must be tough on ya..":
            jump ch3_bunny_cory_comfort


label ch3_bunny_cory_family:
    $ ch3_bunny_family_lead = True

    show bunny sad
    bunny "He ate.. My baby sibling..!!"

    show cory surprise at cory_left
    cory "Oh shrimp.. That's real messed up…"

    show cory side at cory_left
    cory "I'm so very sorry…"

    show bunny default
    bunny "But we sea bunnies.. have toxins in our bodies.."

    bunny "When the crab took a bite.. The toxins start eating him out from inside"

    bunny "Angered.. He then took the rest of my family away claiming us as a danger to the sea.."

    show bunny sad
    bunny "At least.. my sibling fought until the very end.."

    bunny "I still couldn't forgive myself for letting that crab get away…"

    bunny "And for letting it all.. happen… It's my fault.."

    show bunny cry
    bunny "UEEEEHH SHIKU SHIKU"

    show cory upset at cory_left
    cory "Hey, hey don't blame yourself now!"

    show cory talk at cory_left
    cory "What could ya possibly do anyway? If you jump out you'll get kidnapped too!"

    show cory talk at cory_left
    cory "What you did was the best choice, so now you can save your family"

    show bunny cry
    bunny "uuu…"

    show cory talk at cory_left
    cory "Don't worry we'll get him"

    cory "We're planning to overthrow this whole crustacean dictator bullshrimp"
    jump ch3_bunny_done


label ch3_bunny_cory_comfort:

    show cory side at cory_left
    show bunny sad
    bunny "Mm.."

    show cory talk at cory_left
    cory "I had a little sister too.."

    show cory smile at cory_left
    cory "Real ball of sunshine.."

    show cory talk at cory_left
    cory "But she got some kind of weird sickness going on.. that eventually separates us…"

    show cory side at cory_left
    cory "guh sorry for the sudden vent.. I'll stop now"

    show bunny default
    bunny "No! It's fine.. She must've been really dear to you.. I'm sorry.."

    show cory side at cory_left
    cory "She's still alive though.. Somewhere in this vast sea.."

    if ch3_rainbow_algae > 0:
        $ ch3_rainbow_algae -= 1
        $ ch3_bunny_received_algae = True

    show cory smile at cory_left
    cory "Ah, Have you eaten anything? I've got some algae for ya.."

    cory "And it's rainbow algae!"

    show bunny happy
    bunny "Rainbow algae..? so pretty! kirakira"

    bunny "Thank you!"

    show bunny sad
    bunny "But I.. I don't think I can.. eat after what I had to witness…"

    show cory talk at cory_left
    cory "You can't be like that… your family wouldn't want ya to skip meals would they?"

    bunny "..."

    show cory smile at cory_left
    cory "Eat up sea bunny.."

    show cory smile at cory_left
    cory "So you've got the strength to look at them in the eyes when ya meet them again"

    show bunny default
    bunny "You're right.. Thank you.."

    jump ch3_bunny_done

label ch3_bunny_as_shrimp:

    "The sea bunny stands at a reasonably far distance."

    show bunny scared 
    bunny "Your red shelled kind! the one who does all of this evil baka stuff!"

    show bunny sad 
    bunny "My family.. Is detained for simply living…"

    show shrimp default_om 
    shrimp "Oh! It's probably one of the crustaceans doing!"

    menu:
        "How should Mr. Shrimp apologize?"

        "Apologize in advance":
            jump ch3_bunny_shrimp_apologize

        "Please accept this algae as a token of apology!":
            jump ch3_bunny_shrimp_algae


label ch3_bunny_shrimp_apologize:
    $ ch3_bunny_shrimp_apologized = True
    "Mr Shrimp took a few steps forward to properly bow down in an apologetical manner"

    show shrimp default_om 
    shrimp "I apologize for the inconvenience that my kind has inflicted upon your family!"

    show bunny scared 
    bunny "EEEK-!"

    "The sea bunny curls up in fear"

    bunny "I.. kindly.. ask you to stay away.. Please…!"

    show shrimp default 
    shrimp "...! Understood!"

    shrimp "Then I shall stand at a safe, reasonable distance!"

    "Mr Shrimp took exactly one step away from the sea bunny"

    show bunny scared 
    bunny "T-that’s not enough distance!"

    jump ch3_bunny_done


label ch3_bunny_shrimp_algae:
    if ch3_rainbow_algae <= 0:
        "Mr. Shrimp has no algae left to offer."
        jump ch3_bunny_done

    $ ch3_rainbow_algae -= 1

    show shrimp shy
    shrimp "I was informed that algae counts as one of your diet!"

    show bunny scared
    bunny "...?!"

    bunny "I.. I read this in mangas before!"

    bunny "It's probably poisoned right?! Or.."

    bunny "Or you make it super delicious.."

    bunny "And when I'm busy eating your gift.. piri piri..."

    bunny "BAAN!! You kidnap me!"

    show shrimp surprise at npc_right
    shrimp "WHAT! Preposterous! I wouldn't do such dirty tactics!"

    show bunny sad 
    bunny "Guuu..!You'll never know! Must keep guard up! kuyo kuyo…"

    show shrimp sepet at npc_right
    shrimp "And manga.. Is that some kind of.. new type of algaes?!"

    show shrimp default_om at npc_right
    shrimp "I'll search for one if it makes you forgive us!"

    "The sea bunny refuses to take the sea algae"

    jump ch3_bunny_done

label ch3_bunny_family:
    $ ch3_bunny_family_lead = True

    show bunny sad 
    bunny "They were taken away.. by a big brute crab.."

    bunny "He claimed to be.. doing that under the crustacean empress' command.."

    bunny "Said that my.. kind is a threat to the sea…"

    show mc pout
    mc "What!! That's awful!"

    mc "Everyone gets a chance to live at the sea no matter how dangerous!"

    mc "Without what they claim as threats.. the sea would be in a bigger danger!"

    show bunny default
    bunny "Eh..? Is that so..?"

    show mc default
    mc "Mhm! Even the scary stuff has a job!"

    show mc actually
    mc "If you take it away, whatever it used to hunt just grows and grows until that's the problem instead!"

    mc "It's like a big circle: predator, prey, little guys, big guys."

    mc "Snap one part off and the whole thing tips over!"

    mc "So whoever's calling your kind a 'threat'? They just don't get it!"

    show bunny happy
    bunny "Ahh I see! Mmn! That makes perfect sense!"

    show bunny sad
    bunny "If only they would understand…"

    show mc happy
    mc "Don't worry, we'll make them understand!!"

    show bunny sad
    bunny "I just want my family back…"

    show mc happy
    mc "We'll do what we can to help."

    jump ch3_bunny_done


label ch3_bunny_shrimp:

    show mc o at mc_left
    show bunny scared

    bunny "He's a crustacean!!"

    bunny "They're the kind who took my family away!"

    show bunny sad
    bunny "And crustaceans they.. they all work under the crustacean empress, right?"

    show mc pout
    mc "Mm, he does, but.. he's different!"

    mc "He realized that what the empress is pushing is wrong!"

    mc "And now we're here to talk to the empress about it!"

    show bunny default
    bunny "But will the empress hear you out…?"

    bunny "She's very ruthless and stubborn…"

    show bunny sad
    bunny "She's not afraid to kill those who defy her…"

    show mc happy
    mc "Mmm.. then we'll just fight her!"

    show bunny scared
    bunny "Dowawa?! Fight her..?!"

    show mc excited at mc_left
    mc "Yeah! Mr. Cory will tank all her attacks!"

    show bunny happy
    bunny "That's so very cool!! You need your own shounen series!"

    show mc shock
    mc "Shounen? Ah!! Like Chainsaw Man?"

    show bunny happy
    bunny "Yes!! Ah finally someone that gets it!!"

    show mc happy
    mc "Hehe! We'll get your family back, sea bunny!"

    jump ch3_bunny_done


label ch3_bunny_hug:
    if ch3_rainbow_algae <= 0:
        "I don't have any rainbow algae left."
        jump ch3_bunny_done

    $ ch3_rainbow_algae -= 1
    $ ch3_bunny_received_algae = True

    show bunny scared
    bunny "I..!"

    show bunny sad
    bunny "As much as I'd very much like one… right now"

    show bunny cry
    bunny "Nnghh shiku shiku *sniffle* you can't hug me..!!"

    show mc happy
    mc "It's fine! I have some rainbow algae!"

    show bunny sad
    bunny "Rainbow algae..?"

    show mc happy
    mc "It might help you feel a little better."

    show bunny happy
    bunny "It's so pretty…"

    show bunny sad
    bunny "But I.. I don't think I can.. eat after what I had to witness…"

    show mc happy
    mc "You don't have to eat it right now."

    mc "Just keep it with you, okay?"

    show bunny default
    bunny "…Thank you."

    show mc happy
    mc "You're welcome! We'll help you find your family."

    jump ch3_bunny_done


label ch3_bunny_done:

    # Shared transition after the selected Sea Bunny route.
    # Route-specific emotional endings happen before arriving here.

    hide bunny cry
    hide bunny sad
    hide bunny scared
    hide bunny happy
    hide bunny default

    # GRAN HAWK
    show hawk default at npc_right
    hawk "You! You're a freshwater, aren't ya?"
    hawk "What on ocean are you doin' with that red shell?"

    show cory talk at cory_left
    cory "Ay, calm down, ma'am."
    cory "I ain't exactly a fan of the crustacean's idealism."

    show cory fond at cory_left
    cory "But my man, this shrimp ain't like the others."

    show hawk default at npc_right
    hawk "Hmph. And what makes ya so sure of that?"

    show cory side at cory_left
    cory "He's already lettin' the fishes pass now."
    cory "We're tryin' to talk it out with the empress!"

    show hawk sigh at npc_right
    hawk "Crikey. Good luck with that."

    menu:
        "What have the crustaceans done?":
            show mc o at mc_left
            mc "What happened here?"

            show hawk default at npc_right
            hawk "Whole sea's changed, guppy. Not for the better."

            show mc o at mc_left
            mc "Mm? How so?"

            show hawk sigh at npc_right
            hawk "The crustaceans used to mind their own business..."

            hawk "Until the former empress passed the crown to her young."

            hawk "It all became a mess from there on."

            hawk "Now there's checkpoints. Papers. 'Loyalty tests'."

            show hawk default at npc_right
            hawk "Ain't about danger. It's about control."

            show mc o at mc_left
            mc "Mmn... So the real problem lies with the empress!"

            show hawk sigh at npc_right
            hawk "Yeah. Most red shells are natural-born bullies."

            hawk "And her regime greenlit all their bad habits across the sea."

            show mc o at mc_left
            mc "Hmm... Why don't we all go and complain to the empress?"

            show hawk smile at npc_right
            hawk "Hah! We've tried."

            show hawk default at npc_right
            hawk "Most got killed for it. It's like a war goin' on."

            show hawk laugh at npc_right
            hawk "But I've eaten heaps of 'em for brekkie!"

            show mc happy at mc_left
            mc "Oh! Right, crustaceans are part of a sea turtle's diet!"

            show hawk laugh at npc_right
            hawk "Hah! Right! They don't call me Gran Hawk for nothin'!"

            show hawk default at npc_right
            hawk "Can't bring an empress down alone, though."

        "We're trying to talk it out with the empress!":
            show hawk sigh at npc_right
            hawk "Crikey, good luck with that."

            show cory side at cory_left
            cory "You don't sound too hopeful, ma'am."

            show hawk default at npc_right
            hawk "I've seen what happens to folks who try."

            hawk "Most don't get the chance to try again."


    # HAWK QUESTIONS CORY ABOUT shrimp LLARUS
    show hawk default at npc_right
    hawk "I remember faces. That shrimp's the one who guarded the gate!"

    show cory side at cory_left
    cory "I understand how ya feel, but..."

    cory "He's already lettin' all the fishes pass now."
    cory "Your grandturts should be safe."

    show cory smile at cory_left
    cory "I know he's got a good heart. Just a little lost cause."

    show hawk sigh at npc_right
    hawk "And how could ya be so sure of that?"

    show cory talk at cory_left
    cory "He's abandoned his post just to shout a protest at the empress."

    show hawk default at npc_right
    hawk "And have ya actually met the empress?"

    show cory side at cory_left
    cory "Not yet, but we're on our way, ma'am."

    show hawk smile at npc_right
    hawk "Have ya thought long enough to think that..."

    hawk "All of this might be a trap?"

    show cory side at cory_left
    cory "Huh?"

    show cory talk at cory_left
    cory "What do ya mean by that, ma'am?"

    show hawk default at npc_right
    hawk "That mantis shrimp's leadin' y'all to her lair..."

    hawk "What if it's just a facade?"

    show hawk sigh at npc_right
    hawk "You're divin' into the anglerfish's light, mate."

    show cory side at cory_left
    cory "Guh... I didn't think that far..."

    # TRANSITION TO THE NEXT TRAVEL BEAT
    "Gran Hawk's warning lingered in my mind as we continued our journey."

    hide hawk
    hide bunny
    hide dunge
    hide mc
    hide cory

    $ current_cycle = "night"

    scene ch3_night
    with fade

    show mc tired at mc_left
    show cory side at cory_left

    "The journey went on, and the light around us slowly faded."

    mc "Mr. Cory... How much longer do we have to swim?"

    show cory fond at cory_left
    cory "We've been at it for more than half a day, guppy."

    mc "My fins are getting tired..."

    show cory smile at cory_left
    cory "Aw, c'mere. I can hold ya for a bit."

    "I moved closer to Mr. Cory, letting him carry me as we swam onward."

    $ ch3_red_seaweed = 0
    # RED SEAWEED
    show mc excited at mc_left
    mc "Wao!! This seaweed is so red!"
    mc "Is it where the color red came from?"

    show shrimp default_om 
    shrimp "Mm! It is a firmly believed theory that it's where crustaceans get their color from!"

    shrimp "Crustacean mothers often told their young to feed on red seaweed to get a brighter red pigment!"

    show shrimp default 
    shrimp "The redder you are the fiercer you look!"

    show cory side at cory_left
    cory "Sounds like a plot to get your young to eat their veggies..."

    show mc o at mc_left
    mc "Ooo, I see..."

    show cory upset at cory_left
    cory "Ay, you're only allowed to take 2, guppy!"
    cory "Don't think I ain't noticing you counting how much you can take in your little arms!"

    show mc pout at mc_left
    mc "Aw... okay :("
    mc "One more for mama because she likes red..."
    $ ch3_red_seaweed = 2

    # DUNGE ENCOUNTER
    "We spotted another crustacean."

    "It's a grown-sized Dungeness crab. He seems like a laid-back crustacean."

    show dunge smile at npc_right
    show cory fond at cory_left

    "Mr. Shrimp advances towards him like he's seeing an old friend."

    cory "My comrade in arms, Dunge!"

    dunge "Well, butter my tail and call me a biscuit!"

    dunge "Larus! How's it hangin', you ol' bottom-feeder?"

    show mc o at mc_left
    mc "Larus...? Is that Mr. Shrimp's real name?"

    "The crab's expression subtly changes when he notices me and Mr. Cory."

    show dunge default at npc_right
    dunge "...Hold your seahorses. What the hell are you doin' here?"

    dunge "Your tail is supposed to be guardin' the salt-fresh border!"

    show cory talk at cory_left
    cory "Chill out, mane..."

    show dunge default at npc_right
    dunge "!!! And what's this junk you brought with ya?"

    show dunge yeesh at npc_right
    dunge "Don't tell me you're rollin' with these filthy freshies??"

    dunge "A guppy... and..."


    # MC'S CONVERSATION WITH DUNGE
    menu:
        "Mr. Crab, can you help us talk to the Empress?":

            show mc o at mc_left
            show dunge default at npc_right

            "Mr. Crab gives me a humbling look..."

            dunge "Help you? What are you even supposed to be?"

            dunge "Some kinda half-breed?"

            dunge "Do your parents even have the green corals?"

            show mc o at mc_left
            mc "Green corals? :0"

            show dunge yeesh at npc_right
            dunge "Yeah, green corals. The damn corals you need to legally live around here."

            dunge "You must've had some relative from the saltwater side hand 'em over to ya."

            show mc shock at mc_left
            mc "I uhhhhhh..."

            show dunge default at npc_right
            dunge "...You don't got 'em?"

            show mc shock at mc_left
            mc "Um, we don't have one..."

            mc "Is it alright, Mr. Shrimp?"

            show shrimp default 
            shrimp "They're my company, Dunge! From the freshwater."
            shrimp "They're just passing through the reefs, not taking up residence!"

            show shrimp default_om 
            shrimp "Also the green coral policy is still up for debate!"

            show dunge mad at npc_right
            dunge "The Empress firmly stated not to let any threats in."

            dunge "This is a clear violation of the rules, Larus!"

        "Do you hate freshwater creatures? :0":

            show mc o at mc_left
            show dunge default at npc_right

            dunge "Freshwater tadpoles are makin' our ocean colder just by breathin' up all the warm currents!"

            show mc default at mc_left
            mc "Uhm, actually, Mr. Crab, according to marine biology..."

            show mc actually at mc_left
            mc "...water temperature is regulated by thermohaline currents and depth, not fish respiration."

            mc "So freshwater species don't actually alter the ocean's temperature like that! :D"

            show dunge yeesh at npc_right
            dunge "...What a load of carp!"

            show dunge default at npc_right
            dunge "Haven't heard of such nonsense in all my years clawin' this reef!"

            dunge "That's prolly just fake propaganda, lil' guppy."

            dunge "Theories created by... by..."

            "Mr. Crab pauses, searching for words."

            show dunge yeesh at npc_right
            dunge "...Those fancy university intellectuals..."

            dunge "...Who don't know a damn thing about real ocean livin'!"
            # Both MC questions lead into the same confrontation.

    # CONFRONTATION
    "Neither of my questions seems to change Dunge's mind."

    show cory side at cory_left
    cory "..."

    show dunge default at npc_right
    dunge "..."

    "The atmosphere suddenly feels a lot less friendly."

    show mc o at mc_left
    mc "Mr. Cory...?"

    show cory talk at cory_left
    cory "Stay close, guppy."

    # SEA BUNNY FAMILY THREAD

    if ch3_bunny_family_lead:
        show cory upset at cory_left
        cory "Dunge... We heard what happened to the Sea Bunny's family."

        show dunge default at npc_right
        dunge "..."

        show cory talk at cory_left
        cory "You can't just take a whole family away."

        show dunge mad at npc_right
        dunge "They're a threat to the sea."

    # CORY ROUTE: CONFRONT DUNGE
    menu:
        "Ask Dunge to help us talk to the Empress":
            show mc o at mc_left

            mc "Mr. Dunge, can you help us talk to the Empress?"

            show dunge yeesh at npc_right

            dunge "Help ya? After you waltz in here without green corals?"

            show cory talk at cory_left

            cory "We're not here to cause trouble, mane."

            show dunge default at npc_right

            dunge "Then you picked a mighty strange way of showin' it."

        "Ask Dunge about the Sea Bunny's family":
            show mc pout at mc_left

            mc "Mr. Dunge... did you take a Sea Bunny's family?"

            show dunge default at npc_right

            dunge "..."

            show mc o at mc_left

            mc "They said a big crab took them away."

            show dunge yeesh at npc_right

            dunge "Those creatures are a threat to the sea!"

            show mc pout at mc_left

            mc "But they have a family too..."

    # CONFRONTATION
    show cory side at cory_left

    cory "That's enough, Dunge."

    show dunge default at npc_right

    dunge "Oh? And what are you gonna do about it, Larus?"

    show cory talk at cory_left

    cory "We're gettin' through to the Empress."

    cory "And you ain't gonna stop us."

    show dunge mad at npc_right

    dunge "Then I guess you'll have to get past me first."

    show mc shock at mc_left

    mc "Mr. Cory...!"

    show cory side at cory_left
    cory "Stay behind me, guppy."

    hide mc
    $ dunge_battle_encounter = "dunge"
    call dunge_battle_start

    if dunge_battle_result == "victory":
        jump ch3_dunge_aftermath
    else:
        jump ch3_battle_defeat

label ch3_dunge_aftermath:

    $ ch3_dunge_result = dunge_battle_result

    if ch3_dunge_result == "victory":

        show dunge yeesh at npc_right

        dunge "Gah...! Alright, alright!"

        show cory side at cory_left

        cory "That's enough, Dunge."

        show dunge default at npc_right

        dunge "..."

        dunge "Guess I can't stop ya now, Larus."

        show cory talk at cory_left

        cory "Then let us through."

        show dunge yeesh at npc_right

        dunge "Don't go thinkin' this means I agree with ya."

        dunge "I'm just... lettin' ya pass."

        show cory side at cory_left

        cory "That's a start."

        show mc o at mc_left

        mc "Mr. Dunge..."

        mc "What about the Sea Bunny's family?"

        show dunge default at npc_right

        dunge "..."

        dunge "I ain't got 'em here."

        dunge "The ones I took were sent off under the Empress' orders."

        show mc shock at mc_left

        mc "They're still alive?!"

        show dunge yeesh at npc_right

        dunge "Didn't say that, kid."

        dunge "I don't know what happened to 'em after."

        show cory upset at cory_left

        cory "Dunge..."

        dunge "I did what I was ordered to do."

        dunge "That's all I'm sayin'."

        show mc pout at mc_left

        mc "Then we'll find them."

        show cory talk at cory_left

        cory "We'll ask the Empress what she did with them."

        show dunge default at npc_right

        dunge "You're really gonna keep pushin' this, huh?"

        show cory side at cory_left

        cory "You know me."

        dunge "Heh..."

        dunge "Yeah. I do."

        "Dunge moves aside, leaving the way forward open."

        # TODO:
        # Confirm whether Dunge directly knows where the Sea Bunny
        # family was taken, or whether this information should remain
        # unknown until a later scene.

        $ ch3_bunny_path_opened = True

        jump ch3_empress_arrival

    else:

        jump ch3_battle_defeat


label ch3_battle_defeat:

    hide mc
    hide cory
    hide dunge

    "The fight has become too much for us."

    "We have no choice but to retreat."

    # TODO:
    # Decide whether defeat should:
    # - return the player to the encounter,
    # - trigger a unique story scene,
    # - or end the chapter.
    #
    # For now, the battle system's own retry menu handles retries.
    # This label only handles the story flow if the player does not
    # return to the fight.

    return

label ch3_empress_battle_start:
    $ ch3_empress_battle_result = None

    # TEMPORARY: Reuses the Dunge battle system.
    # Encounter-specific HP and party setup are not implemented yet.
    hide mc
    $ dunge_battle_encounter = "empress"
    call dunge_battle_start(cory_start_hp=2)

    $ ch3_empress_battle_result = dunge_battle_result

    return

label ch3_empress_arrival:

    # Temporary visual until the Empress sprite is ready.

    show empress placeholder at npc_right
    show teto default 

    "Abruptly..."

    teto "Fall to your knees and tremble before Her Majestic Majesty, the one and only!"

    teto "Her Majesty Empress Crustacean the VIII!"

    emp "Ah, a visitor?"

    emp "Kekeke! That's me, that's me! I'm Crustacean Empress VIII!"

    teto "Mhm, the best empress on the crustacean line~!"

    emp "Oh, you humble me so, my right hand!"

    teto "Ah, but your greatness must be known across the seven seas~!"

    emp "Across seven seas, you say?!"

    teto "I am merely speaking truth, your Majesty!"

    show cory unimpressed at cory_left

    cory "Are all crustaceans like this...?"

    emp "WHAT?! You dare question the might of an empress?!"

    teto "They seem to have a death wish, your majesty..."

    emp "Then fulfill your wish I shall! Wouldn't the majestic I be the fairest?!"

    show cory surprise at cory_left

    cory "WOAH WOAH-! CHILL OUT YOUR CRUSTACEAN MAJESTY! PUT THE GUN DOWN!"

    show shrimp default_om 

    shrimp "Wait, don't!! I beg for mercy on every one of my ten legs, your majesty!"

    emp "Ah, if it's not my strongest soldier Scyllarus..."

    emp "What petty excuse do you have in defense?"

    teto "I don't think there was ever an excuse to bring in dirtwater..."

    show shrimp default_om 

    shrimp "I beg of Your Majesty and your highly regarded right hand!"

    emp "Oh oh! Are you here to spread marvelous news?! Have you found and fetched me the great golden fish?!"

    shrimp "I-! No... not yet, your majesty... I still have yet to acquire the golden fish... but!"

    shrimp "My dear comrades here have a proposition that'll make it worthwhile!"

    emp "Proposition...? Bleehh, my ears are made to hear only the best of things, not the boring ones..."

    teto "Their filthy words are not for your ears, your majesty."

    teto "Let me decide if it is worthwhile... As you say it."

    emp "Hah! You be my filter, my highly regarded right hand."

    emp "I shall busy myself with my new golden toy!"
    jump ch3_empress_negotiation

label ch3_empress_negotiation:

    menu:

        "Speak to General Goby as MC":
            jump ch3_empress_as_mc

        "Let Cory speak":
            jump ch3_empress_as_cory

        "Let Scyllarus make the proposal":
            jump ch3_empress_as_scyllarus

label ch3_empress_as_mc:

    # Keep your existing MC timed negotiation here.
    # Start with:
    show mc happy at mc_left

    mc "Hi!! Your highness goby fish!"

    show teto gun_upset

    teto "You have 10 seconds to speak your lies."
    teto "Before my spear goes through you."

    show mc shock_hu at mc_left

    mc "Ah, only t-ten seconds?! Oh no! Oh no!"

    teto "There goes your two seconds."

    $ negotiation_choice = renpy.call_screen("negotiation_timer")

    if negotiation_choice == "timeout":

        show mc shock at mc_left
        mc "I-I...!"

        teto "Time's up."

    elif negotiation_choice == "hands":

        show mc default at mc_left
        show teto default

        teto "..."
        teto "Unlike a defect breed like you..."
        teto "We have no hands you speak of."
        teto "All we have are chelipeds."

        show mc o at mc_left
        mc "But you're not even a crustacean! What you have are fins!"

        teto "..."

        show mc o at mc_left
        mc "If you can command an army of crustaceans..."
        mc "If you can hold the empress' great chelipeds..."

        show mc pout at mc_left
        mc "What makes you stop at holding other fishes' fins...?"

        show mc default at mc_left
        mc "Besides... Goby fishes have relatives in freshwater!"

        teto "I'm not a part of that filthy kind."
        teto "You think you're so smart because you've read a few books?"
        teto "Save those futile fun facts for afterlife."

    elif negotiation_choice == "apology":

        show mc o at mc_left
        mc "Everyone we met seemed really sad because of what the crustaceans did..."
        mc "Some lost their families. Some are scared to even leave their homes."

        show mc happy at mc_left
        mc "Therefore, saying sorry would be a good start?"
        mc "Maybe then they all would be kind and respect you too."

        teto "The audacity!"
        teto "You demand an apology from the rulers of the sea?"

        show mc pout at mc_left
        mc "But order isn't supposed to make everyone scared!"

        teto "What the sea thinks is never worth our concern!"

    elif negotiation_choice == "seaweed":

        if ch3_red_seaweed > 0:
            $ ch3_red_seaweed -= 1

        show mc happy at mc_left
        teto "..."

        emp "DID SOMEONE SAY RED SEAWEED?!"

        show mc default at mc_left
        mc "Mhm! I picked it up on the way here! As a peace offering!"

        emp "How thoughtful! Gimme it!"

        "At the blink of an eye, with a discreet bang, the seaweed vanished... now already a crushed victim under the shrimp's eager munch teeth."

        teto "Your Majesty, please remember that they are here to negotiate."

        emp "I know! I can eat and listen at the same time."
        emp "Munch munch munch..."

        show mc shock at mc_left
        "Did she use her pistol to steal the seaweed from my hand without injuring me?"

        show mc o at mc_left
        "Whatever it was, I need to see it again! Maybe I should provoke her more?"

        teto "Ah, your majesty... there's seaweed on your cheek."
        emp "Really?! Help me get rid of it, my Gobby!"

        teto "Affirmative.."

        show mc happy at mc_left
        mc "Yaaay true love wins!"

        show mc excited at mc_left
        mc "Which means Freshwater and Saltwater can live together in peace now!!"

        teto "T-true love-?!"

    jump ch3_empress_shared_hostility

label ch3_empress_as_cory:

    teto "You got exactly 1.8 seconds."

    show cory surprise at cory_left
    cory "...!"
    cory "Might as well say fugu off with your bullcarp shrimp regime, ya redshell-!"

    teto "Enough! That was 3 seconds!"

    "My eyes widen into saucers as it registers a flash of red. The goby's spear grazes past Mr. Cory, tearing through flesh but missing anything vital. A warning, and nothing more."

    show cory hurt at cory_left
    cory "Guh-!"

    show mc shock_hu at mc_left
    mc "Mr. Cory…!!"
    mc "WHY WOULD YOU SAY THAAAT MR CORYYY!!"

    emp "Oooh a rebel I sense?!"
    emp "Kekeke! That bravery of yours, I quite like it!"
    emp "It'll make your screams echo all the sweeter."

    teto "Now face agonizing torture, worth three lifetimes over, dirtwater."

    show shrimp sepet
    shrimp "Frankly! I don't think I can defend you on this one, my questionable friend!"

    # PLACEHOLDER: Cory's battle reuses the Dunge battle.
    # Cory should begin this battle at 2 HP.
    # TODO: Set Cory's HP to 2 using the actual combat-system variable.
    jump ch3_empress_shared_hostility

label ch3_empress_as_scyllarus:

    teto "Make it count, Scyllarus."
    teto "I'm only hearing you out because you're our precious strongest personnel."
    teto "Having you against us will be disadvantageous for both of us."

    show shrimp default_om
    shrimp "I'll make it justifiable!"

    menu:
        "What should Scyllarus propose?"

        "A future where freshwater creatures are no longer detained simply for existing in the sea":
            jump ch3_scyllarus_freshwater_rights

        "The crustaceans should rule with honor again, not fear":
            jump ch3_scyllarus_honor

        "Calm the Empress with red seaweed":
            jump ch3_scyllarus_seaweed

label ch3_scyllarus_freshwater_rights:
    $ ch3_scyl_proposal = "freshwater_rights"

    teto "Oh? You'd bring numbers to a fight, Scyllarus?"

    shrimp "By statistics! Seafolks' crime rates are still higher than the freshwater immigrants!"
    shrimp "With that data in mind.. we shouldn't have detained freshwaters for simply setting fins into sea!"
    shrimp "And to keep punishing an entire species for the sins of a few is neither just, nor even strategic!"

    teto "Even when those are facts.."
    teto "You can't dismiss that incident.."
    teto "In which disaster were caused by those filthy freshwaters?"
    teto "Fishes, mollusks, our own kind — all of them paid for what happened at the Old Canal Junction."
    teto "What we're doing are simply precautions."
    teto "So tragedy doesn't repeat itself…"

    shrimp "But that was 10 years ago, general!"
    shrimp "Longer than both you and the empress' ages combined!"
    shrimp "I was there when it happened…"
    shrimp "And it was also a freshwater that helped me through that time…"
    shrimp "So don't tell me they're all the villains in this story!"
    shrimp "I refuse to believe that anymore!"

    jump ch3_scyllarus_shared_response

label ch3_scyllarus_honor:
    $ ch3_scyl_proposal = "honor"
    shrimp "It truly pains me to say this but…!"
    shrimp "We were once honored, loved. Well mannered."
    shrimp "Crustaceans are of the supportive, compassionate kind!"
    shrimp "Now all I've seen from seafolks are that of disdain and fear of us.."
    shrimp "Is that really what our kind wants to be known as..?"
    shrimp "A ruthless, impudent dictatorship that easily tramples the life of others..!"

    teto "You talk all high and mighty.."
    teto "Yet how many died pleading at your own claws, Scyllarus?"

    shrimp "....!"
    shrimp "That's why I…!!"

    teto "Your fierce claws.. are not made for compassion is it?"
    teto "You're a killing machine."
    teto "One that would swipe through anything in its path, crustacean or not, if ordered to.."
    teto "You're not one to propose for harmony."

    shrimp "..."

    mc "YOU'RE WRONG!!"

    teto "Oh..?"

    mc "Mr. shrimp- Mr.. Mr Sc... Cy.. Clarus has never once hurt me!"
    cory "It's Scyllarus guppy…"

    mc "He always touches me super carefully! I've never got any scratches see!"

    "I extended both arms outwards, showing off every unscratched, unbruised inch of them."

    mc "He's.. he's … always trying his best to not hurt anyone…"

    shrimp "....guppy"

    cory "What they said!"
    cory "Our big ol friend here is not what you claim a killin machine!"
    cory "He's just stuck under a regime he can't escape from.."
    cory "He's not killin for fun, it was yous who put the weapon in his claws in the first place!"

    shrimp "Cory…!"

    teto "Foolish dirtwaters! You just haven't witnessed his true side yet!"

    mc "Maybe so! But.. I trust the side of him I have seen!"

    jump ch3_scyllarus_shared_response

label ch3_scyllarus_seaweed:
    $ ch3_scyl_proposal = "red_seaweed"

    shrimp "My friend here picked out the brightest, freshest red seaweed for you to feast!"

    emp "Oh ho ho don't mind if I do~!!"
    emp "Mmmn.. this is why you're the best Scyllarus..!"

    teto "He's the best…? But your highness you told me that I'm-"
    teto "Sigh.. please don't play favorites in front of the enemy, your majesty."

    emp "Shh what does he have to say! Speak my esteemed soldier Scyllarus!"

    shrimp "Right now.. we are at a compromised position, your majesty.."
    shrimp "The seafolks hates and fear us, the freshwaters no longer trust us either.."
    shrimp "And the golden fish's power is stirring up more chaos than we can hope to contain.."
    shrimp "This isn't a war we can win by claws and fear alone!"
    shrimp "So with that in mind.. I propose that.."
    shrimp "We go back to Her Majesty the VII's system.."
    shrimp "We earn the sea's trust instead of demanding its fear!"

    emp "My.. mother?!"
    emp "YOU FOOLISH SAND-FILLED BRAIN LUDICROUS IMBECILE!!"
    emp "I'm sick of it! My mother's softness cost us everything, and you want me to make that same mistake?!"
    emp "CRUSTACEANS!! Detain them at once!"

    jump ch3_scyllarus_shared_response

label ch3_empress_shared_hostility:

    # MC and Cory's negotiation paths escalate into the same shared battle.
    jump ch3_scyllarus_shared_response


label ch3_scyllarus_shared_response:

    show teto default

    teto "This is exactly why you were never fit to be a general."

    teto "Sand for brains. One sob story from a guppy and you fold like a cheap net."

    show shrimp default

    shrimp "I'd rather be wrong for believing in people than right for fearing them!"

    show empress placeholder at npc_right

    emp "Heh! Time to answer the most asked question then!"

    emp "The ultimate showdown...!!"

    show mc excited at mc_left

    mc "Oh my oh my!"

    emp "PISTOL SHRIMP VS MANTIS SHRIMP!! YOU WON'T BELIEVE WHO WINS?? (GONE WRONG)"

    emp "KEKEKEKE!! Oh how I adore you! Too bad I gotta kill you now!"

    show cory upset at cory_left

    cory "Aye! This is no play, guppy! Get your ass ready for a fight!"

    # PLACEHOLDER: Reuse the Dunge battle for now.
    # Scyllarus should NOT join the party for this fight.
    # TODO: Configure the battle party to exclude Scyllarus.
    # TODO: Set Cory's HP to 2 for this encounter.
    # TODO: Confirm the correct party and HP variable names.
    hide mc
    $ ch3_empress_battle_result = None

    $ dunge_battle_encounter = "empress"
    call dunge_battle_start(cory_start_hp=2)

    $ ch3_empress_battle_result = dunge_battle_result

    if ch3_empress_battle_result == "victory":
        jump ch3_empress_battle_victory
    else:
        jump ch3_empress_battle_defeat

label ch3_empress_battle_victory:

    $ ch3_empress_defeated = True

    # EMPRESS DEFEATED

    hide mc
    hide cory

    show empress placeholder at npc_right
    show teto default

    emp "May the best gold bearer wins!"

    emp "Spoiler: it is I, most obviously!"

    "The clash between the two crustaceans shakes the surrounding water."

    "For a moment, it feels as though the entire sea has stopped to watch."

    # The battle system has already determined the result.
    # The following scene begins after the Empress has lost.

    show empress placeholder at npc_right

    emp "KEKEKE~! This golden..."

    "The Empress' laughter cuts short."

    show teto surprise

    teto "Your Majesty!!"

    emp "Gooobyyy..."

    teto "Your Majesty, we must retreat!"

    emp "Retreat?!"

    emp "How undignified!"

    teto "Your survival takes priority, Your Majesty!"

    teto "Scyllarus has won this battle fair and square."

    emp "I am not some undignified tyrant who runs away!"

    emp "Besides, I still have the golden scale!"

    show cory side_close at cory_left

    cory "Heh."

    cory "You mean this thing?"

    show mc shock at mc_left

    "Mr. Cory holds up the golden scale."

    emp "WHAT?!"

    emp "You filthy freshwater thief!"

    "The Empress lunges forward, but a fin gently shuts her mouth."

    teto "Your Majesty, please."

    teto "We must go."

    emp "Mmph!!"

    teto "My apologies."

    teto "If fate allows us to cross paths again..."

    teto "I hope we may settle this with a fitting revenge."

    "Goby hauls the Empress away, leaving the battlefield behind."

    hide empress
    hide teto

    # THE CROWD

    "For a moment, the sea remains silent."

    "Then, cheers begin to rise from every direction."

    "The surrounding sea folk celebrate the end of the battle."

    show mc excited at mc_left

    mc "We did it!!"

    show cory side at cory_left

    cory "Heh. We sure did, guppy."

    show shrimp surprise at npc_right

    mc "But Mr. Scyllarus was the one who fought her!"

    show shrimp default_om at npc_right

    shrimp "I..."

    "Scyllarus looks around at the cheering crowd."

    show cory talk at cory_left

    cory "You stood up to her, even when it meant defyin' your own kind."

    cory "You showed us the way here."

    cory "And you've been protectin' us this whole time."

    show shrimp default at npc_right

    shrimp "Cory..."

    cory "You ain't a weapon, mate."

    cory "You're our friend."

    "The crowd continues to cheer."

    "Some of the sea folk approach Scyllarus, thanking him for standing up to the Empress."

    "One of them even jokes about naming a guppy after him."

    show shrimp shy at npc_right

    shrimp "I..."

    shrimp "Thank you, everyone."

    shrimp "I have never felt so powerful..."

    # DUNGE AND THE CRUSTACEAN ARMY

    "A familiar red shell emerges from the crowd."

    show dunge default at npc_right

    dunge "Scyllarus!"

    "Dunge approaches, followed by a group of crustaceans."

    "He kneels before Scyllarus."

    show dunge default at npc_right

    dunge "The crown should belong to the strongest soldier."

    dunge "You've earned it."

    "The crustaceans behind him bow as well."

    "Their voices echo through the water."

    "Long live the new Emperor!"

    show shrimp surprise at npc_right

    shrimp "W-Wait!"

    shrimp "I refuse!"

    "The crowd falls silent."

    shrimp "I don't want to become an emperor."

    shrimp "I want the old rule to die."

    # SCYLLARUS REFUSES THE THRONE

    show shrimp default_om at npc_right

    shrimp "Her Majesty the VII once told me..."

    shrimp "The sea belongs to no one."

    shrimp "It belongs to everyone."

    shrimp "We were never given the right to rule over it."

    shrimp "Only the responsibility to help it thrive."

    shrimp "Her dethroning was her own choice."

    shrimp "And her daughter took that chance to rule."

    shrimp "But I won't accept a throne built upon someone else's exile."

    shrimp "Let the sea be a No Man's Land."

    show dunge default at npc_right

    dunge "..."

    dunge "Then I guess I ain't got any orders left to follow."

    "Dunge rises."

    dunge "I'm steppin' down too."

    dunge "No more green corals."

    dunge "No more borders."

    "The crustaceans exchange uncertain glances."

    "Then, one by one, they lower their claws."

    # A NEW RESPONSIBILITY

    show shrimp default_om at npc_right

    shrimp "All sea folk..."

    shrimp "Those with fins, chelipeds, claws, flippers, and spikes..."

    shrimp "We must help one another."

    shrimp "We must make this sea a place where everyone can feel comfortable and safe."

    "The crowd listens."

    "Some nod. Others look at one another, unsure of what comes next."

    "But for the first time, no one is ordering them to bow."

    # SCYLLARUS THANKS MC AND CORY

    show shrimp shy at npc_right

    shrimp "Cory..."

    shrimp "Thank you for calling me your mate."

    shrimp "And for seeing me as a friend, rather than a weapon."

    show cory fond at cory_left

    cory "Heh. That's what mates are for."

    show shrimp default_om at npc_right

    shrimp "And you, little guppy..."

    shrimp "You defended me before the general."

    shrimp "You helped me find the part of myself I lost beneath all that armor."

    show mc happy at mc_left

    mc "Hehe! Of course, Mr. Scyllarus!"

    shrimp "From now on..."

    shrimp "I vow to remain under your command."

    show mc shock at mc_left

    mc "Huh?!"

    mc "Under our command?"

    show cory side at cory_left

    cory "Hold on a second, mane."

    cory "I'm not gonna command ya around."

    cory "You're not ours to command."

    cory "You're our mate."

    show shrimp surprise at npc_right

    shrimp "MATE?!"

    shrimp "Mate! You say...!"

    shrimp "Hmm..."

    shrimp "And you say 'our'..."

    shrimp "Which includes the guppy..."

    # THE PARTY'S NEXT STEPS

    show mc excited at mc_left

    mc "Mhm!"

    mc "Then, as your mate..."

    mc "Could you help us get 30 rainbow algae, 40 red seaweeds, and 35 clams?"

    show cory surprise at cory_left

    cory "Guppy!"

    cory "That's not what I meant!"

    show shrimp shy at npc_right

    shrimp "Thirty rainbow algae..."

    shrimp "Forty red seaweeds..."

    shrimp "And thirty-five clams..."

    shrimp "I shall remember these requests!"

    show cory side at cory_left

    cory "Aw, don't take her seriously, mate."

    # MC'S TRANSFORMATION PROGRESS

    show cory side at cory_left

    cory "Feel anythin different?"

    show mc excited at mc_left

    mc "Woah..! I.. I can hear your voices clearer and and!"

    mc "And.. my skin feels.. less pruny now!"

    mc "It's as if I'm becoming more and more of a fish! :D"

    show shrimp smile at npc_right

    shrimp "KAKAKA! Good for you!"

    show mc o at mc_left

    mc "Mnn.. I wanna try something"

    "I took off the weighing glass on my head."

    mc "..."

    show cory side at cory_left

    cory "Don't push yourself too hard, alright?"

    show mc shock at mc_left

    mc "... nguhk..!"

    show mc excited at mc_left

    mc "It's.. the waterbreathing time!"

    mc "It was only 15 minutes-ish before!"

    mc "Now it's 30! yaay!"

    # GATHA REAPPEARS

    show gator default at npc_right

    gator "Ouuu shiiii.."

    gator "You all look nasty... need help?"

    show mc excited at mc_left

    mc "Ms. Gator!! We meet again!"

    show gator default at npc_right

    gator "Mm yep."

    gator "What I say about catching that golden fish before you do?"

    gator "But frankly? I just.. lost motivation midway..."

    gator "Waaay too much of a hassle..."

    show cory side at cory_left

    cory "Gatha..."

    show gator default at npc_right

    gator "But I did get this..."

    gator "As a proof that I did get to it, hmph!"

    gator "You can't be saying shrimp like I was too slow or anythin' now."

    show mc shock at mc_left

    mc "Wait! Where did you get this and when?"

    mc "We haven't seen the fish lately..."

    gator "It's just riiiight there."

    # TODO:
    # The source draft stops before explaining exactly what Gatha
    # is pointing at or showing.
    # Confirm what she obtained and how it relates to the golden fish.

    gator "I don't get why you're so adamant on getting it, guppy..."

    gator "But best of luck to ya, alright?"


    # THE GOLDEN SCALE

    "The cheering gradually settles."

    "Mr. Cory looks down at the golden scale in his possession."

    show mc o at mc_left

    mc "Mr. Cory..."

    mc "That golden scale..."

    mc "The Empress had one too."

    show cory side_close at cory_left

    cory "Yeah."

    cory "And she was usin' it to make herself even more powerful."

    show shrimp default at npc_right

    shrimp "The golden scale..."

    shrimp "So the Empress was also chosen?"

    mc "I don't know..."

    "I look at the golden scale."

    "If the Empress had been able to gather more power from it..."

    "What would have happened if she had found the golden fish?"

    "Would she have used that power to rule over the entire sea?"

    "The thought makes my fins feel a little colder."

    # SEA BUNNY FAMILY THREAD

    show mc pout at mc_left

    mc "But..."

    mc "What about the Sea Bunny's family?"

    "The celebration quiets around us."

    show cory upset at cory_left

    cory "We still don't know where they are."

    show shrimp default at npc_right

    shrimp "..."

    "Scyllarus looks toward the path the Empress and Goby took."

    shrimp "Then we must find out."

    shrimp "We cannot leave them behind."

    # THE GOLDEN FISH REMAINS THE OBJECTIVE

    "I look beyond the crowd, toward the vast sea stretching around us."

    "The golden fish is still out there."

    "And now, I know that the Empress was not the only one searching for it."

    "The golden scale in Mr. Cory's possession glimmers faintly."

    show mc default at mc_left

    mc "We still have to find the golden fish, don't we?"

    show cory side at cory_left

    cory "Yeah, guppy."

    cory "But we ain't leavin' anyone behind on the way."

    show shrimp default_om at npc_right

    shrimp "Then I shall accompany you."

    shrimp "Not as your weapon..."

    shrimp "But as your mate."

    show cory smile at cory_left

    cory "Heh. That's more like it."

    show mc happy at mc_left

    mc "Then let's go!"

    hide mc
    scene black with dissolve

    "END OF CHAPTER 3"

    menu:
        "Continue to Chapter 4":
            jump chapter4_start

        "End":
            return


label ch3_empress_battle_defeat:

    hide mc
    hide cory

    show shrimp upset at npc_right

    "The fight has become too much for us."

    "We retreat, leaving the Empress and her army behind."

    show cory hurt at cory_left
    cory "Guh...!"

    show mc shock at mc_left
    mc "Mr. Cory...!"

    shrimp "..."

    "We have no choice but to fall back."

    # The battle system should handle retries or game-over behavior.
    # This story label only handles a non-victory result.
    return
    # The existing source does not yet provide the next scene.
    return