label salmon:

    scene expression get_dialogue_background()

    show salmon pien at salmon_pos

    "A Salmon paces back and forth restlessly."

    salmon "Hic hic..."
    salmon "Sniff....."
    salmon "....oouuugh...."

    show mc shock at mc_pos

    mc "... Ma'am? Why are you crying :("

    show salmon default at salmon_pos

    salmon "....? huh??"

    show salmon pien at salmon_pos

    salmon "..."
    salmon "I want to go get down to the sea..."
    salmon "but I bloody well can't..."

    show salmon pout at salmon_pos

    salmon "It's all... because... of that God awful....."

    show salmon pien at salmon_pos

    salmon "UEEEEЕННН."

    show mc shockhu at mc_pos

    mc "!! waouh-? Don't cry, Mrs Salmon!"
    mc "(hugs the salmon)"

    show salmon pien at salmon_pos

    salmon "......!!!"

    show mc happy at mc_pos

    mc "There, there."
    mc "If the mama is sad, the baby gets sad, too."

    show salmon default at salmon_pos

    salmon "...... how on ocean does a tiny you know that, love?"

    show mc actual at mc_pos

    mc "I watched salmon migration on YouTube!!"
    mc "Mama salmon swims really far to lay their eggs, right?"

    show salmon happy at salmon_pos

    salmon "Oh my.... Hahaha."
    salmon "You're a very lovely little thing, aren't you?"

    show salmon default at salmon_pos

    salmon "Though I haven't a clue what this \"YouTube\" is...."
    salmon "Must be a helpful source of information.."

    show salmon happy at salmon_pos

    salmon "Tell me love, are there any sort of.. Pregnancy tips in there?"
    salmon "Or what a salmon parent must prepare to leave their young..."

    show mc happy at mc_pos

    mc "I think so! YouTube's got everything you'd want to see!"

    salmon "Oh that sounds about perfect!"

    show salmon default at salmon_pos

    "Mrs. Salmon looks at Cory."

    salmon "Go back to your father now. He must be worried for you"

    show mc shock at mc_pos

    mc "Ah, he's not my father!"

    show mc happy at mc_pos

    mc "I only met him yesterday!"

    show salmon pout at salmon_pos

    salmon "..........???"

    "Salmon glares at Cory suspiciously."

    # Cory belum muncul sampai dia mulai bicara
    show cory side at cory_right_pos
    hide mc

    cory "Ay.. no need to look at me like that ma'am.."
    cory "I'm a trusted adult!"

    "Salmon squints her eyes at him in suspicion, not believing a thing"

    salmon "...."

    show cory sideclose at cory_right_pos

    cory "glup...."

    call select_interactor

    if _return == "mc":

        jump salmon_ask_as_mc

    else:

        jump salmon_ask_as_cory


# =========================================================
# AS MC
# =========================================================

label salmon_ask_as_mc:

    hide cory
    show mc default at mc_pos

    menu:

        "What's stopping you from going down there, ma'am??":

            show mc o at mc_pos

            show salmon default at salmon_pos

            salmon "There's only one path down to the sea from here, innit,"

            show salmon pout at salmon_pos

            salmon "But a bloody mantis shrimp's blocking the way,"
            salmon "So I can't get past, love."

            mc "But... why does the mantis shrimp block the way???"

            show salmon default at salmon_pos

            salmon "I haven't the foggiest idea, love."

        "Can't you just push past the river, ma'am?":

            show mc o at mc_pos

            show salmon default at salmon_pos

            salmon "Push past it??"
            salmon "Oh, perish that thought, love.."
            salmon "... that path is guarded... by a mantis shrimp."
            salmon "Whacking great claws and all."

            show salmon pout at salmon_pos

            salmon "I reckon he's a bloody MMA (Marine Martial Arts) fighter."
            salmon "Tried to ask nicely, but he shooed me right off..."

            show mc shockhu at mc_pos

            mc "Oh no that's terrible.."
            mc "but why would Mr Mantis do that?"

            show salmon default at salmon_pos

            salmon "I haven't a clue dear, he looks like he lost his mind"
            salmon "Only way to walk pass him is to win in a duel"

        "I found a tiny krill!" if has_item("tiny_krill"):

            show mc happy at mc_pos
            show salmon happy at salmon_pos

            salmon "Oh how lovely! For me, sweet guppy?"

            mc "Mhm! It can be your tiny companion to keep you safe or-"

            "Mrs. Salmon starts eating the krill with a delighted face."

            show mc shock at mc_pos

            salmon "Mm! Scrumptious krill"

            mc "Ah.. Salmon does eat krills huh.."

            "Mrs. Salmon pulls me into a sudden hug. I can faintly hear the tiny eggs shuffling under her scales"

            salmon "Thank you, thank you.. I can't remember the last time I had a meal.."

            "Her voice trembles in sincere gratitude, so soft it's enough to lull me to sleep. It was akin to mama's voice when she sings. But it's not the same.."
            "It's not her..."

            show mc pout at mc_pos

            mc "mn..*sniff*"
            mc "Mama..."

            show salmon default at salmon_pos

            salmon "...!"

            show salmon happy at salmon_pos

            "I feel a faint tap on my glass head. Even when I couldn't directly feel it, I could picture how it would land on my head, a gentle caress that would wipe all my worries and sadness away"

            salmon "mhm, I'm here for you.."
            salmon "It's alright my sweet little guppy... you're okay.."

            $ remove_item("tiny_krill")

    show salmon pien at salmon_pos

    salmon "I think I will have to take a detour-"
    salmon "-even it'll take me aeons."

    show cory netral_hu at cory_right_pos
    hide mc

    cory "A detour.... whaddya think, guppy?"

    show mc pout at mc_pos
    hide cory

    mc "NOOO I dont wanna take a detour...!!"
    mc "The golden fish will be gone farther by then :("

    show salmon default at salmon_pos

    salmon "Haven't a clue about any other way, unfortunately."

    show salmon happy at salmon_pos

    salmon "I can only wish you the best of luck."
    salmon "I bid you farewell guppy"

    $ add_clue("The only way to go to the sea is blocked by a mantis shrimp.")

    hide mc
    hide cory
    hide salmon

    scene expression get_background()

    return


# =========================================================
# AS CORY
# =========================================================

label salmon_ask_as_cory:

    "Before Cory can speak, Mrs salmon interrupts-"

    show salmon pout at salmon_pos

    salmon "What on ocean are you doing with that guppy?"

    show cory netral_hu at cory_right_pos

    cory "Ay, easy, ma'am..."
    cory "I'm just protecting the little guppy, alright?"

    menu:

        "D'you mind us asking why you can't get down to the sea?":

            show cory netral_hu at cory_right_pos

            show salmon pout at salmon_pos

            salmon "......."
            salmon "I won't be answering your queries young man!"
            salmon "not until you tell the truth about the little one."

            show cory side at cory_right_pos

            "Mr. Cory approached Mrs. Salmon with a sigh, lowering his voice to a whisper. Though I can still make out the words quite clear."

            cory "I haven't got a full picture of the guppy's story but..."
            cory "To me, it looks like their parents somewhat abandoned 'em."

            show salmon default at salmon_pos

            salmon "......!"

            show salmon pout at salmon_pos

            salmon "Then just turn around and go back."
            salmon "You'd know how bloody dangerous the sea can be for a fry..."

            show cory netral at cory_right_pos

            cory "I'm well aware ma'am.."
            cory "they almost fell a deep river hole where I first found em.."

            show cory sideclose at cory_right_pos

            cory "But withholding a guppy's dream from coming true?"
            cory "I'd be too evil for that"

        "Maam, why can't you go down to the sea?":

            show salmon pout at salmon_pos
            show cory sideclose at cory_right_pos

            "Mrs.Salmon ignores Cory completely."

            salmon "... are you sure he's not up to anything dodgy, dear?"

            hide cory
            show mc default at mc_pos

            mc "Mm-hmm! Mr Cory is super nice!"

            show mc happy at mc_pos

            mc "He's been helping me lots!"

            show salmon default at salmon_pos

            salmon "Hm, if you say so then..."

            show salmon pout at salmon_pos

            salmon "But! you watch your back around him anyway, love."

            hide mc
            show cory upset at cory_right_pos

            cory "I'm trustworthy, swear on my gills!"

        "May I offer you some food, ma'am?" if has_item("tiny_krill"):

            show cory smile_hu at cory_right_pos
            show salmon default at salmon_pos

            "Cory offers a krill to Mrs. Salmon"

            salmon "...!"

            show salmon pout at salmon_pos

            salmon "... Hmph"

            show cory sideclose at cory_right_pos

            cory "I'll just... leave it here for you ma'am."

            show salmon default at salmon_pos

            salmon "Wait!"

            show cory netral_hu at cory_right_pos

            cory "... hm? What is it ma'am?"

            show salmon default at salmon_pos

            salmon "I should be thanking you bloke properly.."
            salmon "That was rude of me, My deepest apologies.."

            show cory smile_hu at cory_right_pos

            cory "Nay ma'am it's chill I'm used to it.."
            cory "Besides, a carrying mother needs to have their guard up yeah?"

            salmon "Fair enough.. I can't help it"
            salmon "You better take a dainty great care of the little fry, okay?"
            salmon "I'm bloody worried for them.."

            cory "Don't worry ma'am I had a little sibling just their age"
            cory "I know what I'm doing alright!"

            $ remove_item("tiny_krill")

    $ cory_at_right = False

    hide mc
    hide cory
    hide salmon

    scene expression get_background()

    return