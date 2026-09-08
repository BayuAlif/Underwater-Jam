# =========================================================
# NPC - SEA TURTLE (Gran Hawk)
# Chapter 3 - Sea Day Cycle
# =========================================================

label seaturtle:

    scene expression get_dialogue_background()

    # Bersihkan sprite sebelumnya
    hide mc
    hide cory
    hide shrimp
    hide scy
    hide bunny
    hide hawk

    "A sea turtle sways haphazardly above us. It suddenly throws a rock at Mr. Shrimp."

    show scy surprise at shrimp_right_pos

    scy "whuh?! What’s that about!"

    show hawk default at hawk_pos

    hawk "Get lost ya red shell!"
    hawk "We’ve got enough of ya bullshrimp!"

    show cory smile_hu at cory_pos

    cory "Everyone’s got a problem with your kind huh?"

    show mc o at mc_pos

    mc "mmm it seems like the problem delve deeper than a simple hate…"
    mc "Let’s try asking her!"

    hide mc
    hide cory
    hide scy

    call select_interactor_ch3

    $ seaturtle_talked = True

    if _return == "mc":
        jump seaturtle_ask_as_mc
    elif _return == "cory":
        jump seaturtle_ask_as_cory
    else:
        jump seaturtle_ask_as_scy


# =========================================================
# AS MC
# =========================================================

label seaturtle_ask_as_mc:

    hide cory
    hide scy
    hide shrimp

    show hawk default at hawk_pos
    show mc default at mc_pos

    hawk "Get away from that red freak guppy.."
    hawk "They can’t be trusted with."

    menu:

        "Why do you hate mr. shrimp so much?":

            show hawk default at hawk_pos

            hawk "I remember faces, that shrimp’s gate guarding one!"
            hawk "He didn't get my grandturts a passing!"

            show mc pout at mc_pos

            mc "But he’s not like that anymore!"

            show mc default at mc_pos

            mc "He’s let everyone pass now you should be able to meet your grand turtles!"

            show hawk sigh at hawk_pos

            hawk "I know, don’t worry I met them, they’re safe now."
            hawk "But eh, my blood gets boiling at the sight of them now."

            show mc pout at mc_pos

            mc "Well! Fair point but targeting your anger at every crustacean is bad too.."
            mc "Maybe some of them didn’t want to do it.."

            show mc o at mc_pos

            mc "Won’t it make you just like them..?"

            show hawk laugh at hawk_pos

            hawk "Hah, s'pose you got a point there."

            show hawk smile at hawk_pos

            hawk "My neighbor's a shrimp. Marchin protests with us too."

            show hawk default at hawk_pos

            hawk "Not all are bad, but some that stay silent is as bad, which means they agree with whatever going on."

            show mc happy at mc_pos

            mc "Mr shrimp is good I know! We’re trying to talk it out with the empress!"

            show hawk sigh at hawk_pos

            hawk "Crikey, good luck with that."

        "What have the crustaceans done?":

            show mc o at mc_pos
            show hawk default at hawk_pos

            hawk "Whole sea's changed, guppy. Not for the better."

            mc "mm? How so?"

            hawk "The crustaceans they used to mind their own business.."

            show hawk sigh at hawk_pos

            hawk "Until the former empress pass the crown to her young."
            hawk "It all became a mess from there on."
            hawk "Now there's checkpoints. Papers. 'Loyalty tests'."

            show hawk default at hawk_pos

            hawk "Ain't about danger. It's about control."

            show mc default at mc_pos

            mc "Mmn.. So the real problem lies on the empress!"

            show hawk sigh at hawk_pos

            hawk "Yeah, most red shells are natural born bullies."
            hawk "And her regime greenlit all their bad habits to all of sea."

            show mc o at mc_pos

            mc "hmmm.. Why don’t we all go and complain to the empress?"

            show hawk smile at hawk_pos

            hawk "Hah! We’ve tried."
            hawk "Most got killed for it. It’s like a war going on."
            hawk "But I’ve eaten heaps of em for brekkie!"

            show mc happy at mc_pos

            mc "Oh! Right, crustaceans are a part of a sea turtle’s diet!"

            show hawk laugh at hawk_pos

            hawk "Hah right! They don’t call me gran hawk for none!"
            hawk "Can’t bring an empress down alone though."

    hide mc
    hide hawk

    return


# =========================================================
# AS CORY
# =========================================================

label seaturtle_ask_as_cory:

    hide mc
    hide scy
    hide shrimp

    show hawk default at hawk_pos
    show cory side at cory_right_pos

    hawk "You! You’re a freshwater aren’t ya?"
    hawk "What on ocean are you doing with that red shell?"

    show cory side at cory_right_pos

    cory "Ay, calm down ma’am.."
    cory "I ain’t exactly a fan of the crustacean’s idealism."

    show cory netral_hu at cory_right_pos

    cory "But my man, tis shrimp is ain’t like others."

    menu:

        "What ya got going with the shrimp?":

            show hawk default at hawk_pos

            hawk "I remember faces, that shrimp’s gate guarding one!"
            hawk "He didn't get my grandturts a passing!"

            show cory netral_hu at cory_right_pos

            cory "I understand your feeling but.."
            cory "He’s already lettin all the fishes pass now, your grandturts should be safe."

            show cory smile at cory_right_pos

            cory "I know he’s got a good heart. Just a little lost cause."

            show hawk sigh at hawk_pos

            hawk "And how could you be so sure of that?"

            show cory smile_hu at cory_right_pos

            cory "He’s abandoned his post just to shout a protest to the empress."

            show hawk default at hawk_pos

            hawk "And have you actually met the empress?"

            show cory netral at cory_right_pos

            cory "Not yet, but we’re on our way ma’am."

            show hawk smile at hawk_pos

            hawk "Have you thought long enough to think that…"
            hawk "All of this might be a trap?"

            show cory netral at cory_right_pos

            cory "Huh?"

            show cory netral_hu at cory_right_pos

            cory "What do ya mean by that, ma’am?"

            show hawk default at hawk_pos

            hawk "That mantis shrimp’s leading yall to her lair.."
            hawk "What if it’s just a facade?"

            show hawk sigh at hawk_pos

            hawk "You’re diving into the anglerfish's light, mate."

            show cory sideclose at cory_right_pos

            cory "guh, I didn’t think that far…."

            show cory side at cory_right_pos

            cory "A huge part of my heart believes in him though."

            show hawk laugh at hawk_pos

            hawk "Hah you a better fish than I am then."
            hawk "Just stay vigilant alright?"

        "Is it because of the crustacean empress?":

            show hawk default at hawk_pos

            hawk "Be real careful of that empress alright."
            hawk "It’s two peas in a pod situation."

            show cory netral_hu at cory_right_pos

            cory "Two peas in a pod? She got backup?"

            show hawk default at hawk_pos

            hawk "Nay she’s got a fatal weakness."
            hawk "A goby fish while she a pistol shrimp."
            hawk "Ever heard of that tale?"

            show cory side at cory_right_pos

            cory "I’m a freshwater folk don’t think I’m familiar with that."

            show hawk default at hawk_pos

            hawk "Pistol shrimp's near blind, see. Digs the burrow, keeps it tidy."
            hawk "So the goby does the watching. Sits right by the entrance, eyes peeled."
            hawk "Shrimp keeps a feeler on 'em at all times."

            show hawk sigh at hawk_pos

            hawk "Big threat? Goby'll block the whole entrance with its own body."
            hawk "They move as one. Can't have one without the other, really."

            show hawk default at hawk_pos

            hawk "You gotta aim for the goby first."
            hawk "Or, take them both down at the same time."

            show cory surprise at cory_right_pos

            cory "*whistle* Interesting mechanism they got going on."

            show cory netral_hu at cory_right_pos

            cory "We plan on taking this the diplomatic route though ma’am."
            cory "But if it does get to that point.."

            show cory smile_hu at cory_right_pos

            cory "I owe you for that one, ma’am thank you!"

            show hawk laugh at hawk_pos

            hawk "Anything to bring her down."

    hide cory
    hide hawk

    return


# =========================================================
# AS SCYLLARUS
# =========================================================

label seaturtle_ask_as_scy:

    hide mc
    hide cory

    show hawk default at hawk_pos
    show scy default at shrimp_right_pos

    hawk "Get ya stank dirty claws outta here red shell!"

    show scy defaultom at shrimp_right_pos

    scy "I wipe my claws hourly! I can assure you that I'm not dirty!"

    menu:

        "I apologize in advance":

            show hawk default at hawk_pos

            hawk "hawk tuah! fugu off with that apology of yours!"
            hawk "I’m not the only one that needs your pointless apologies!"

            show hawk sigh at hawk_pos

            hawk "Ya have wronged the whole sea, red shell."

            show scy default at shrimp_right_pos

            scy "...!"

            show scy defaultom at shrimp_right_pos

            scy "Then please allow me…"

            "Mr Shrimp takes a firm step back and swivels around facing the vast sea, before he takes a long deep breath."

            show scy laugh at shrimp_right_pos

            scy "I APOLOGIIIIIZEE FOR THEE INCONVEEENIIEEEEENNNCEEAAAHHH!!!!"

            show hawk smile at hawk_pos

            hawk "pfft-!"

            show hawk laugh at hawk_pos

            hawk "hahahah!"
            hawk "Hate to admit it! But you pass the vibe check."
            hawk "Still not forgiving you though."

    hide scy
    hide hawk

    return
