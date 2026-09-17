label salmon_interaction:
    hide mc
    scene ch2_day
    $ focus()
    show salmon pien:
        full
        center
        toright
        pacing
        vibrate
    show mc shock:
        full
        right

    "A Salmon paces back and forth restlessly."

    salmon "{bt=5}Hic hic...{/bt}"
    salmon "{cps=20}{bt=5}Sniff.......oouuugh....{/bt}{/cps}"

    show mc sad_hu:
        full
        right
        surprise
    mc "... Ma'am? Why are you crying :("

    show salmon default:
        ease 0.5
        full
        center
    salmon "....? huh??"

    show salmon pien:
        ease 0.5
        full
        center
        vibrate
    salmon "........."
    salmon "I want to go get down to the sea..."
    salmon "but i bloody well can't..."

    show salmon pout:
        full
        center
    salmon "It's all... because... of that God awful selfish wank-....."

    show salmon pien:
        ease 0.5
        full
        center
        vibrate
    salmon "{cps=20}{size=65}{bt=5}UEEEEHHH………{/bt}{/size}{/cps}"

    show mc sad_hu:
        full
        right
        surprise
    mc "!! waouh-? Don't cry, Mrs Salmon!"
    "I wrapped my arms around mrs salmon in an attempt to calm her down."

    show salmon pien:
        ease 0.5
        full
        center
        jumpmc
    salmon "......!!!"

    show mc happy:
        full
        right
    mc "There, there."
    mc "If the mama is sad, the baby gets sad, too."

    show salmon default:
        ease 0.5
        full
        center
    salmon "...... how on ocean does a tiny you know that, love?"

    show mc default:
        full
        right
        surprise
    mc "I watched salmon migration on YouTube!!"
    mc "Mama salmon swims really far to lay their eggs, right?"

    show salmon happy:
        full
        center
        surprise
    salmon "Oh my.... Hahaha."
    salmon "You're a very lovely little thing, aren't you?"

    show salmon default:
        ease 0.5
        full
        center
    salmon "Though i haven't a clue what this \"YouTube\" is...."
    salmon "Must be a helpful source of information.."

    show salmon happy:
        ease 0.5
        full
        center
    salmon "Tell me love, are there any sort of.. Pregnancy tips in there?"
    salmon "Or what a salmon parent must prepare to leave their young..."

    show mc happy:
        full
        right
        surprise
    mc "I think so! YouTube's got everything you'd want to see!"

    show salmon happy:
        ease 0.5
        full
        center
        surprise
    salmon "Oh that sounds about perfect!"

    show cory side:
        full
        leftish
    with moveinleft

    show salmon default:
        full
        centerright
    with move
    "Mrs. Salmon stares at Cory."
    show salmon default:
        full
        centerright
        surprise
    salmon "Go back to your father now. He must be worried for you"

    show mc shock:
        full
        right
        surprise
    mc "Ah, he's not my father!"
    mc "I only met him yesterday!"

    show salmon pout:
        full
        centerright
    salmon "..........???"
    "Salmon glares at Cory suspiciously."

    show cory side_close:
        full
        leftish
    cory "Ay.. no need to look at me like that ma'am.."
    cory "I'm a trusted adult!"

    "Salmon squints her eyes at him in suspicion, not believing a thing."

    salmon "...."

    show cory side_close:
        full
        leftish
        sink
    cory "glup...."
    
    $ focus()
    hide mc
    hide cory
    call screen choose_interactor(
        "Choose who should ask Mrs. Salmon!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump salmon_as_mc

    jump salmon_as_cory


label salmon_as_mc:
    hide cory side
    hide cory side_close
    menu:
        "What's stopping you from going down there, ma'am??":
            $ focus()
            show mc o:
                full
                right
            show salmon default:
                full
                center
            salmon "There's only one path down to the sea from here, innit,"

            show salmon pout:
                full
                center
                vibrate
            salmon "But a bloody mantis shrimp's blocking the way,"
            salmon "So I can't get past, love."

            show mc o:
                full
                right
                surprise
            mc "But... why does the mantis shrimp block the way???"

            show salmon default:
                full
                center
            salmon "I haven't the foggiest idea, love."


        "Can't you just push past the river, ma'am?":
            $ focus()
            show mc o:
                full
                right
            show salmon default:
                full
                center
            salmon "Push past it??"
            salmon "Oh, perish that thought, love.."
            salmon "... that path is guarded... by a mantis shrimp."
            salmon "Whacking great claws and all."

            show salmon pout:
                full
                center
                vibrate
            salmon "I reckon he's a bloody MMA (Marine Martial Arts) fighter."
            salmon "Tried to ask nicely, but he shooed me right off..."

            show mc sad_hu:
                full
                right
                surprise
            mc "Oh no that's terrible.."
            mc "but why would mr mantis do that?"

            show salmon default:
                full
                center
            salmon "I haven't a clue dear, he looks like he lost his mind"
            salmon "Only way to walk pass him is to win in a duel"


        "I found a tiny krill!" if has_item("tiny_krill"):
            show mc happy:
                full
                right
            show salmon happy:
                full
                center
                surprise
            salmon "Oh how lovely! For me, sweet guppy?"
            
            show mc happy:
                full
                right
                surprise
            mc "Mhm! It can be your tiny companion to keep you safe or-"
            show mc shock:
                full
                right
                surprise
            "Mrs. Salmon starts eating the krill with a delighted face."
            salmon "Mm! Scrumptious krill"

            mc "Ah.. Salmon does eat krills huh.."
            "Mrs. Salmon pulls me into a sudden hug. I can faintly hear the tiny eggs shuffling under her scales."
            
            show salmon happy:
                full
                center
                surprise

            show salmon hug:
                full
                center
                #with shake ntar
        
            salmon "Thank you, thank you.. I can't remember the last time I had a meal.."
            show mc shock:
                full
                right
                surprise
            "Her voice trembles in sincere gratitude, so soft it's enough to lull me to sleep. It was akin to mama's voice when she sings. But it's not the same.."
            show mc holdcry:
                full
                right
                sink
            "It's not her..."

            show mc cry:
                full
                right
                vibrate
            mc "{bt=5}mn..*sniff*{/bt}"
            mc "{bt=5}Mama...{/bt}"

            show salmon default:
                full
                center
                surprise
            salmon "...!"

            show salmon happy:
                full
                center
                surprise
            salmon "mhm, I'm here for you.."
            salmon "It's alright my sweet little guppy... you're okay.."
            $ remove_item("tiny_krill")

    show salmon pien:
        ease 0.5
        full
        centerright
    with move
    salmon "I think I will have to take a detour-"
    salmon "-even it'll take me aeons."

    show cory talk_hu:
        full
        leftish
    with moveinleft
    cory "A detour.... whaddya think, guppy?"

    show mc pout:
        full
        right
        surprise
    mc "NOOO I dont wanna take a detour...!!"
    mc "The golden fish will be gone farther by then :("

    show salmon default:
                full
                centerright
    salmon "Haven't a clue about any other way, unfortunately."

    show salmon happy:
                full
                centerright
                surprise
    salmon "I can only wish you the best of luck."
    salmon "I bid you farewell guppy"

    $ add_clue("The only way to go to the sea is blocked by a mantis shrimp.")
    $ focus()

    return


label salmon_as_cory:
    $ focus()
    show cory talk_hu:
        full
        leftish
    show salmon pout:
                full
                centerright
    salmon "What on ocean are you doing with that guppy?"

    cory "Ay, easy, ma'am..."
    cory "I'm just protecting the little guppy, alright?"
    $ focus()

    menu:

        "D'you mind us asking why you can't get down to the sea?":
            $ focus()
            salmon "......."
            salmon "I won't be answering your queries young man!"
            salmon "not until you tell the truth about the little one."

            show cory side:
                full
                leftish
            "Mr. Cory approached Mrs. Salmon with a sigh, lowering his voice to a whisper. Though I can still make out the words quite clear."
            cory "I haven't got a full picture of the guppy's story but..."
            show cory side_close:
                full
                leftish
                sink
            cory "To me, it looks like their parents somewhat abandoned 'em."

            show salmon default:
                full
                centerright
                surprise
            salmon "......!"

            show salmon pout:
                full
                centerright
                vibrate
            salmon "Then just turn around and go back."
            salmon "You'd know how bloody dangerous the sea can be for a fry..."

            show cory talk:
                full
                leftish
            cory "I'm well aware ma'am.."
            cory "they almost fell a deep river hole where I first found em.."

            show cory talk_hu:
                full
                leftish
            cory "But withholding a guppy's dream from coming true?"
            show cory side_close:
                full
                leftish
            cory "I'd be too evil for that"
            $ focus()


        "Maam, why can't you go down to the sea?":
            $ focus()
            show salmon pout:
                full
                centerright
                vibrate
            salmon "... are you sure he's not up to anything dodgy, dear?"

            show mc happy:
                full
                right
                surprise
            mc "Mm-hmm! Mr Cory is super nice!"
            mc "He's been helping me lots!"

            show salmon default:
                full
                centerright
            salmon "Hm, if you say so then..."

            show salmon pout:
                full
                centerright
                vibrate
            salmon "But! you watch your back around him anyway, love."

            show cory side_close:
                full
                leftish
                surprise
            cory "I'm trustworthy, swear on my gills!"
            $ focus()


        "May I offer you some food, ma'am?" if has_item("tiny_krill"):
            $ focus()
            show cory smile_hu at cory_npc
            "Cory offers a krill to Mrs. Salmon."

            salmon "...!"

            show salmon pout:
                full
                centerright
                vibrate
            salmon "... Hmph"

            show cory side_close:
                full
                leftish
            cory "I'll just... leave it here for you ma'am."

            show salmon default:
                full
                centerright
                surprise
            salmon "Wait!"

            show cory talk_hu:
                full
                leftish
            cory "... hm? What is it ma'am?"

            show salmon default:
                full
                centerright
                surprise
            salmon "Wait!"
            salmon "I should be thanking you bloke properly.."
            salmon "That was rude of me, My deepest apologies.."

            show cory smile:
                full
                leftish
            cory "Nay ma'am it's chill I'm used to it.."
            show cory smile_hu:
                full
                leftish
            cory "Besides, a carrying mother needs to have their guard up yeah?"

            show salmon pout:
                full
                centerright
                sink
            salmon "Fair enough.. I can't help it"
            salmon "You better take a dainty great care of the little fry, okay?"
            show salmon default:
                full
                centerright
                sink
            salmon "I'm bloody worried for them.."

            show cory proud:
                full
                leftish
            cory "Don't worry ma'am I had a little sibling just their age"
            show cory proud_hu:
                full
                leftish
            cory "I know what I'm doing alright!"
            $ focus()
            $ remove_item("tiny_krill")

    $ salmon_trusts_cory = True

    return
