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
        $ ch4_add_affection("scy")
        jump ch4_plankton_scy
    elif ch4_game1_companion == "cory":
        $ ch4_add_affection("cory")
        jump ch4_plankton_cory
    else:
        $ ch4_add_affection("leo")
        jump ch4_plankton_leo

label ch4_plankton_scy:

    show screen ch4_affection_hud("scy")

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
            $ ch4_add_affection("scy")
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
    hide screen ch4_affection_hud
    jump ch4_festival_hub

label ch4_plankton_cory:

    show screen ch4_affection_hud("cory")

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
            $ ch4_add_affection("cory")
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
    hide screen ch4_affection_hud
    jump ch4_festival_hub

label ch4_plankton_leo:

    show screen ch4_affection_hud("leo")

    leo "Catching helpless little beings huh? I'm skilled at that~!"
    leo "We'll catch as many as we can, little guppy"

    planktons "We'll tear your fins flappers to shreds!"

    leo "Wow, feisty are we?"

    menu:
        "Do you eat planktons, Leo?":
            $ ch4_add_affection("leo")
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
    hide screen ch4_affection_hud
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
        $ ch4_add_affection("cory")
        jump ch4_shoot_cory
    elif ch4_game2_companion == "scy":
        $ ch4_add_affection("scy")
        jump ch4_shoot_scy
    else:
        $ ch4_add_affection("leo")
        jump ch4_shoot_leo

label ch4_shoot_cory:

    show screen ch4_affection_hud("cory")

    show cory talk at cory_left
    cory "Here's the trick to winnin' this, guppy."
    cory "Imagine those clams are the ones who called ya weird."

    "Mr Cory tilted the pistol toward the nearest clam, taking a brief aim before squeezing the trigger."
    play sound "audio/sfx/shoot_tin.mp3"
    "KLANG!"
    "The shot ricocheted off the sea rock, missing the target entirely."
    "Mr. Cory's grin instantly vanished into a frown."

    show cory upset at cory_left
    cory "Tch…"

    "I raised my pistol, lining up the sights of the exact same clam."
    "I held my breath, squeezed."
    play sound "audio/sfx/tin_metal.mp3"
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
            $ ch4_add_affection("cory")
            show mc happy at mc_left
            mc "Mmm.. perhaps it's simply an issue with your pistol, Mr. Cory?"
            mc "Or maybe aiming is just harder over there."
            mc "Try taking a shot with mine, Mr. Cory!"
            "I stepped aside, clearing space so Mr.Cory can commandeer my pistol shooter."
            show cory talk at cory_left
            cory "Aight… imma try."
            "Mr Cory squared his shoulders, locking his sight onto the target."
            play sound "audio/sfx/shoot_tin.mp3"
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
            play sound "audio/sfx/shoot_tin.mp3"
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
    hide screen ch4_affection_hud
    jump ch4_festival_hub

label ch4_shoot_scy:

    show screen ch4_affection_hud("scy")

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
            $ ch4_add_affection("scy")
            show mc o at mc_left
            mc "Um. So accounting for the cross-current drag, the salinity density…"
            mc "... and the angle of refraction through the water column and and,"
            leo "Also consider the margin percent for shell thickness, relative to the kinetic torque~!"
            show scy default at npc_right
            scy "I don't think you need to overthink it, guppy!"
            show mc excited at mc_left
            mc "Aough yessir!"
            "I pressed the trigger."
            play sound "audio/sfx/shoot_tin.mp3"
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
            play sound "audio/sfx/shoot_tin.mp3"
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
    hide screen ch4_affection_hud
    jump ch4_festival_hub

label ch4_shoot_leo:

    show screen ch4_affection_hud("leo")

    leo "Eight shiny little bullets total. Four for each of us, then~"

    show mc happy at mc_left
    mc "Okay! Here Leo, pinnipedia first!"

    "Leo takes the pistol with lazy elegance, tilting the grip sideways at a completely nonchalant angle."
    "Without even closing an eye to aim, she booped the trigger with her head."
    play sound "audio/sfx/shoot_tin.mp3"
    "KLANG!"
    "The clam shell target shuddered violently, but refused to drop."

    show mc shock at mc_left
    mc "Dead center!! It counts, rightright? :D"

    stall2 "Nein, nein! You must knock ze clam completely off ze shelf, ja!"
    stall2 "Merely rattling its hinges gets you zero pointz!"

    show mc pout at mc_left
    mc "Awh… no way.."

    leo "Your turn, guppy~"
    play sound "audio/sfx/shoot_tin.mp3"
    "KLANG! The pearl bullet hit the same clam. But it won't fall."

    show mc pout at mc_left
    mc "Huuh… :/"

    leo "My, my… are you quite certain this mechanism isn't rigged~?"

    menu:
        "It is totally is!":
            $ ch4_add_affection("leo")
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
            play sound "audio/sfx/thump.mp3"
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
            play sound "audio/sfx/shoot_tin.mp3"
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
    hide screen ch4_affection_hud
    jump ch4_festival_hub
