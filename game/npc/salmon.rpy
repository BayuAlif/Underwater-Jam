# =========================================================
# CHAPTER 2 - NPC: MRS. SALMON
# =========================================================

label salmon:

    $ cory_at_right = False

    show mc default at mc_pos

    "Mrs. Salmon is crying."

    salmon "Hic... hic..."
    salmon "Sniff..."
    salmon "...oouuugh..."

    show mc o at mc_pos

    mc "...Ma'am?"
    mc "Why are you crying? :("

    salmon "...?"
    salmon "Huh?"

    salmon "I want to get down to the sea..."
    salmon "But I bloody well can't..."
    salmon "It's all because of that God-awful..."
    salmon "UEEEEHHH...!"

    show mc shock at mc_pos

    mc "WAOUH?!"
    mc "Don't cry, Mrs. Salmon!"

    "I throw my arms around Mrs. Salmon."

    show mc happy at mc_pos

    mc "There, there."
    mc "If the mama is sad, the baby gets sad too."

    salmon "...How on ocean does a tiny thing like you know that, love?"

    show mc excited at mc_pos

    mc "I watched salmon migration on YouTube!!"
    mc "Mama salmon swims really far to lay their eggs, right?"

    salmon "Oh my..."
    salmon "Hahaha."
    salmon "You're a very lovely little thing, aren't you?"
    salmon "Though I haven't a clue what this 'YouTube' is..."
    salmon "Must be a helpful source of information."

    salmon "Tell me, love."
    salmon "Are there any sort of pregnancy tips in there?"
    salmon "Or what a salmon parent must prepare to leave their young...?"

    show mc happy at mc_pos

    mc "I think so!"
    mc "YouTube's got everything you'd want to see!"

    salmon "Oh that sounds about perfect!"

    "Mrs. Salmon looks at Cory."

    salmon "Go back to your father now. He must be worried for you."

    show mc o at mc_pos

    mc "Ah, he's not my father!"
    mc "I only met him yesterday!"

    salmon "..........???"

    "Mrs. Salmon glares at Cory suspiciously."

    $ cory_at_right = True
    hide mc
    show cory side at cory_right_pos

    cory "Ay.. no need to look at me like that ma'am.."
    cory "I'm a trusted adult!"

    "Mrs. Salmon squints her eyes at him in suspicion, not believing a thing."

    salmon "...."

    cory "glup…."

    call screen who_should_ask(title="Choose who should ask Mrs. Salmon!", subtitle="The answers she gives may vary based on her relationship with the character")

    if _return == "mc":
        jump salmon_as_mc
    else:
        jump salmon_as_cory


# =========================================================
# SALMON - AS MC
# =========================================================

label salmon_as_mc:

    $ cory_at_right = False
    hide cory
    show mc default at mc_pos

    menu:

        "What's stopping you from going down there, ma'am?":

            salmon "There's only one path down to the sea from here, innit."
            salmon "But a bloody mantis shrimp's blocking the way."
            salmon "So I can't get past, love."

            show mc shock at mc_pos

            mc "But… why does the mantis shrimp block the way???"

            salmon "I haven't the foggiest idea, love."


        "Can't you just push past the river, ma'am?":

            salmon "Push past it??"
            salmon "Oh, perish that thought, love.."
            salmon "...that path is guarded… by a mantis shrimp."
            salmon "Whacking great claws and all."

            salmon "I reckon he's a bloody MMA fighter."
            salmon "Marine Martial Arts."

            salmon "Tried to ask nicely, but he shooed me right off…"

            show mc shock at mc_pos

            mc "Oh no that's terrible.."
            mc "But why would Mr. Mantis do that?"

            salmon "I haven't a clue dear, he looks like he lost his mind."
            salmon "Only way to walk past him is to win in a duel."


        "I found a tiny krill!" if has_item("tiny_krill"):

            salmon "Oh how lovely!"
            salmon "For me, sweet guppy?"

            show mc happy at mc_pos

            mc "Mhm!"
            mc "It can be your tiny companion to keep you safe or-"

            "Mrs. Salmon starts eating the krill with a delighted face."

            $ remove_item("tiny_krill")

            salmon "Mm! Scrumptious krill."

            show mc o at mc_pos

            mc "Ah.. Salmon does eat krills huh.."

            "Mrs. Salmon pulls me into a sudden hug."

            "I can faintly hear the tiny eggs shuffling under her scales."

            salmon "Thank you, thank you.."
            salmon "I can't remember the last time I had a meal.."

            "Her voice trembles in sincere gratitude."

            "So soft it's enough to lull me to sleep."

            "It was akin to Mama's voice when she sings."

            "But it's not the same.."

            "It's not her…"

            show mc shock at mc_pos

            mc "mn.. *sniff*"
            mc "Mama..."

            salmon "...!"

            "I feel a faint tap on my glass head."

            "Even when I couldn't directly feel it, I could picture how it would land on my head."

            "A gentle caress that would wipe all my worries and sadness away."

            salmon "Mhm, I'm here for you.."
            salmon "It's alright my sweet little guppy…"
            salmon "You're okay.."


    salmon "I think I will have to take a detour-"
    salmon "-even it'll take me aeons."

    $ cory_at_right = True
    hide mc
    show cory side at cory_right_pos

    cory "A detour…. whaddya think, guppy?"

    $ cory_at_right = False
    hide cory
    show mc shock at mc_pos

    mc "NOOO I don't wanna take a detour…!!"
    mc "The golden fish will be gone farther by then :("

    salmon "Haven't a clue about any other way, unfortunately."

    salmon "I can only wish you the best of luck."
    salmon "I bid you farewell, guppy."

    $ cory_at_right = False
    hide mc
    hide cory

    return


# =========================================================
# SALMON - AS CORY
# =========================================================

label salmon_as_cory:

    $ cory_at_right = True
    hide mc
    show cory side at cory_right_pos

    salmon "What on ocean are you doing with that guppy?"

    cory "Ay, easy, ma'am…"
    cory "I'm just protecting the little guppy, alright?"

    menu:

        "D'you mind us asking why you can't get down to the sea?":

            salmon "......."
            salmon "I won't be answering your queries, young man!"
            salmon "Not until you tell the truth about the little one."

            "Mr. Cory approaches Mrs. Salmon with a sigh, lowering his voice to a whisper."

            "Though I can still make out the words quite clearly."

            cory "I haven't got a full picture of the guppy's story but..."
            cory "To me, it looks like their parents somewhat abandoned 'em."

            salmon "......!"

            salmon "Then just turn around and go back."
            salmon "You'd know how bloody dangerous the sea can be for a fry…"

            cory "I'm well aware, ma'am.."
            cory "They almost fell a deep river hole where I first found 'em.."

            cory "But withholding a guppy's dream from coming true?"
            cory "I'd be too evil for that."


        "Ma'am, why can't you go down to the sea?":

            "Mrs. Salmon ignores Cory completely."

            $ cory_at_right = False
            hide cory
            show mc default at mc_pos

            salmon "...Are you sure he's not up to anything dodgy, dear?"

            show mc happy at mc_pos

            mc "Mm-hmm!"
            mc "Mr Cory is super nice!"
            mc "He's been helping me lots!"

            salmon "Hm, if you say so then…"

            salmon "But!"
            salmon "You watch your back around him anyway, love."

            $ cory_at_right = True
            hide mc
            show cory talk at cory_right_pos

            cory "I'm trustworthy, swear on my gills!"


        "May I offer you some food, ma'am?" if has_item("tiny_krill"):

            "Cory offers a krill to Mrs. Salmon."

            $ remove_item("tiny_krill")

            salmon "...!"
            salmon "...Hmph."

            cory "I'll just... leave it here for you, ma'am."

            salmon "Wait!"

            cory "...Hm?"
            cory "What is it, ma'am?"

            salmon "I should be thanking you bloke properly.."
            salmon "That was rude of me."
            salmon "My deepest apologies.."

            show cory smile_hu at cory_right_pos

            cory "Nay ma'am, it's chill."
            cory "I'm used to it.."

            cory "Besides, a carrying mother needs to have their guard up, yeah?"

            salmon "Fair enough.."
            salmon "I can't help it."

            salmon "You better take a dainty great care of the little fry, okay?"
            salmon "I'm bloody worried for them.."

            show cory talk at cory_right_pos

            cory "Don't worry ma'am."
            cory "I had a little sibling just their age."
            cory "I know what I'm doing alright!"

    $ cory_at_right = False
    hide mc
    hide cory

    return
