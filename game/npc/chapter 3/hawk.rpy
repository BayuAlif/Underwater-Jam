label hawk_encounter:
    hide mc
    scene ch3_day with dissolve

    show hawk default:
        unpose
        full
        center
        walkloop
    with moveinright
    show mc o:
        unpose
        full
        right
    with moveinright
    "A seaturtle sways haphazardly above us. It suddenly throws a rock at mr.shrimp"

    show scy surprise:
        unpose
        full
        centerright
        walkloop
    with moveinright
    show hawk default:
        full
        leftish
        walkloop
    with move
    scy "Whuh?! What's that about!"
    hawk "Get lost ya red shell!"
    hawk "We've got enough of ya bullshrimp"

    show cory smile_hu:
        unpose
        full
        right
        walkloop
    with moveinright
    show scy surprise:
        full
        center
    with move
    show hawk default:
        full
        left
        walkloop
    with move
    cory "everyone's got a problem with your kind huh?"

    show cory smile_hu:
        full
        right
    show mc o:
        unpose
        full
        right
    with moveinright
    mc "mmm it seems like the problem delve deeper than a simple hate…"
    mc "let's try asking her out!"

    hide mc
    hide cory
    hide scy
    hide hawk
    
    call screen choose_interactor(
        "Choose who should ask Gran Hawk!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_turtle_as_mc
    elif selected_questioner == "cory":
        jump ch3_turtle_as_cory
    else:
        jump ch3_turtle_as_scyllarus

label ch3_turtle_as_mc:
label ch3_hawk_as_mc:
    show hawk default:
        unpose
        full
        center
        walkloop
    with moveinright
    show mc o:
        unpose
        full
        right
    with moveinright
    hawk "Get away from that red freak guppy.."
    hawk "they can't be trusted with"
    hide mc
    hide hawk
    hide scy
    hide cory
    menu:
        "Why do you hate mr. shrimp so much?":
            show hawk default:
                unpose
                full
                center
            with moveinright
            show mc o:
                unpose
                full
                right
            with moveinright
            hawk "I remember faces, that shrimp's gate guarding one!"
            hawk "He didn't get my grandturts a passing!"

            show mc pout:
                full
                right
                surprise
            mc "But he's not like that anymore!"

            show mc default:
                full
                unpose
                right
            mc "He's let everyone pass now you should be able to meet your grand turtles!"

            show hawk sigh:
                full
                center
            hawk "I know, don't worry I met them, they're safe now"
            hawk "But eh, my blood gets boiling at the sight of them now"

            show mc pout:
                full
                right
            mc "well! Fair point but targeting your anger at every crustaceans is bad too.."
            mc "Maybe some of them didn't want to do it.."

            show mc o:
                full
                right
            mc "won't it make you just like them..?"

            show hawk laugh:
                full
                center
            hawk "Hah, s'pose you got a point there."

            show hawk smile:
                full
                center
            hawk "My neighbor's a shrimp. Marchin protests with us too."

            show hawk default:
                full
                center
            hawk "Not all are bad, but some that stay silent is as bad, which means they agree with whatever going on"

            show mc happy:
                full
                right
                surprise
            mc "Mr shrimp is good I know! We're trying to talk it out with the empress!"

            show hawk sigh:
                full
                center
            hawk "Crikey, good luck with that"
            $ ch3_visited_turtle = True
            jump ch3_day_explore_continue

        "What have the crustaceans done?":
            show mc o:
                full
                right
            show hawk default:
                full
                center
            hawk "Whole sea's changed, guppy. Not for the better."
            mc "mm? how so?"
            hawk "The crustaceans they used to mind their own business.."

            show hawk sigh:
                full
                center
            hawk "Until the former empress pass the crown to her young"
            hawk "It all became a mess from there on"
            hawk "Now there's checkpoints. Papers. 'Loyalty tests'."

            show hawk default:
                full
                center
            hawk "Ain't about danger. It's about control."

            show mc default:
                full
                right
            mc "Mmn.. So the real problem lies on the empress!"

            show hawk sigh:
                full
                center
            hawk "Yeah, most red shells are natural born bullies"
            hawk "And her regime greenlit all their bad habits to all of sea"

            show mc o:
                full
                right
            mc "hmmm.. Why don't we all go and complain to the empress?"

            show hawk smile:
                full 
                center
            hawk "hah! We've tried"
            hawk "Most got killed for it. It's like a war going on"
            hawk "But I've eaten heaps of em for brekkie!"

            show mc happy:
                full
                right
            mc "oh! Right crustaceans are a part of a sea turtle's diet"

            show hawk laugh:
                full
                center
            hawk "Hah right! They don't call me gran hawk for none!"
            hawk "Can't bring an empress down alone though"
            $ ch3_visited_turtle = True
            jump ch3_day_explore_continue
    
label ch3_turtle_as_cory:
label ch3_hawk_as_cory:

    show cory side:
        unpose
        full
        leftish
    with moveinright
    show hawk default:
        unpose
        full
        centerright
    with moveinright
    hawk "You! You're a freshwater aren't ya?"
    hawk "What on ocean are you doing with that red shell?"
    cory "Ay, calm down ma'am.."
    cory "I ain't exactly a fan of the crustacean's idealism"

    show cory talk_hu:
        full
        leftish
    cory "But my man, tis shrimp is ain't like others"
    hide cory
    hide hawk
    menu:
        "What ya got going with the shrimp?":
            show cory talk_hu:
                unpose
                full
                leftish
            with moveinright
            show hawk default:
                full
                offscreenright
            show cory talk_hu:
                centerright
            with moveinright
            hawk "He didn't get my grandturts a passing!"
            cory "I understand your feeling but.."
            cory "He's already lettin all the fishes pass now, your grandturts should be safe"

            show cory smile:
                full
                leftish
            cory "I know he's got a good heart. Just a little lost cause"

            show hawk sigh:
                full
                centerright
            hawk "and how could you be so sure of that?"

            show cory smile_hu:
                full
                leftish
            cory "He's abandoned his post just to shout a protest to the empress"

            show hawk default:
                full
                centerright
            hawk "and have you actually met the empress?"

            show cory talk:
                full
                leftish
            cory "Not yet, but we're on our way ma'am"

            show hawk smile:
                full
                centerright
            hawk "Have you thought long enough to think that…"
            hawk "All of this might be a trap?"

            show cory talk:
                full
                leftish
            cory "huh?"

            show cory talk_hu:
                full
                leftish
            cory "What do ya mean by that, ma'am?"

            show hawk default:
                full
                centerright
            hawk "That mantis shrimp's leading yall to her lair.."
            hawk "what if it's just a facade?"

            show hawk sigh:
                full
                centerright
            hawk "You're diving into the anglerfish's light, mate"

            show cory side_close:
                full
                leftish
            cory "guh, I didn't think that far…."

            show cory side:
                full
                leftish
            cory "A huge part of my heart believes in him though"

            show hawk laugh:
                full
                centerright
            hawk "hah you a better fish than I am then"
            hawk "Just stay vigilant alright?"
            $ ch3_visited_turtle = True
            jump ch3_day_explore_continue

        "Is it because of the crustacean empress?":
            show cory talk_hu:
                unpose
                full
                leftish
            with moveinright
            show hawk default:
                unpose
                full
                centerright
            with moveinright
            hawk "Be real careful of that empress alright"
            hawk "It's two peas in a pod situation"
            cory "Two peas in a pod? She got backup?"
            hawk "nay she's got a fatal weakness"
            hawk "a goby fish while she a pistol shrimp"
            hawk "Ever heard of that tale?"

            show cory side:
                full
                leftish
            cory "I'm a freshwater folk don't think I'm familiar with that"
            hawk "Pistol shrimp's near blind, see. Digs the burrow, keeps it tidy."
            hawk "So the goby does the watching. Sits right by the entrance, eyes peeled."
            hawk "Shrimp keeps a feeler on 'em at all times."

            show hawk sigh:
                full
                centerright
            hawk "Big threat? Goby'll block the whole entrance with its own body."
            hawk "They move as one. Can't have one without the other, really."

            show hawk default:
                full
                centerright
            hawk "You gotta aim for the goby first"
            hawk "or, take them both down at the same time"

            show cory surprise:
                full
                leftish
            cory "*whistle* Interesting mechanism they got going on"

            show cory talk_hu:
                full
                leftish
            cory "We plan on taking this the diplomatic route though ma'am."
            cory "But if it does get to that point.."

            show cory smile_hu:
                full
                leftish
            cory "I owe you for that one, ma'am thank you!"

            show hawk laugh:
                full
                centerright
            hawk "Anything to bring her down"
            $ clue_empress_weakness = True
            $ ch3_visited_turtle = True
            jump ch3_day_explore_continue

label ch3_turtle_as_scyllarus:
label ch3_hawk_as_scyllarus:

    show hawk default:
        unpose
        full
        leftish
    with moveinright
    hawk "Get ya stank dirty claws outta here red shell!"

    show scy default:
        unpose
        full
        centerright
    with moveinright
    scyllarus "I wipe my claws hourly! I can assure you that I'm not dirty!"
    hide scy
    hide hawk

    menu:
        "I apologize in advance":
            show hawk default:
                unpose
                full
                leftish
            with moveinright
            show scy default:
                unpose
                full
                centerright
            with moveinright
            hawk "hawk tuah! fugu off with that apology of yours!"
            hawk "I'm not the only one that needs your pointless apologies!"

            show hawk sigh:
                full
                leftish
            hawk "ya have wronged the whole sea, red shell"

            show scy default:
                full
                centerright
            scyllarus "...!"

            show scy default_om:
                full
                centerright
            scyllarus "Then please allow me…"

            "Mr Shrimp takes a firm step back and swivel around facing the vast sea, before he took a long deep breath."

            show scy laugh:
                full
                centerright
                vibrate
            scyllarus "I APOLOGIIIIIZEE FOR THEE INCONVEEENIIEEEEENNNCEEAAAHHH!!!!"

            show hawk smile:
                full
                leftish
                vibrate
            hawk "pfft-!"

            show hawk laugh:
                full
                leftish
                surprise
            hawk "hahahah!"
            hawk "Hate to admit it! But you pass the vibe check"
            hawk "Still ain't forgiving you though"
            $ ch3_visited_turtle = True
            jump ch3_day_explore_continue