# =========================================================
# NPC - SEA BUNNY (Joruna Parva)
# Chapter 3 - Sea Day Cycle
# =========================================================

label seabunny:

    scene expression get_dialogue_background()

    # Bersihkan sprite sebelumnya
    hide mc
    hide cory
    hide shrimp
    hide scy
    hide bunny
    hide hawk

    "A sea bunny is found crying behind luscious corals. I wonder what made it cry that loud?"

    show bunny cry at bunny_pos

    bunny "nghuuuu.. ueeeh… ueeh!!!!"

    show mc shock at mc_pos

    mc "Huh..? What’s wrong?"

    show bunny cry at bunny_pos

    bunny "uuu.. shiku shiku.. My family.. They took them!!"

    show scy defaultom at shrimp_right_pos

    scy "And who exactly is this \"they\"?!"

    show bunny scared at bunny_pos

    bunny "GYAAA IT'S THEM IT'S THEM!!"

    "The bunny shaped slug lets out a high pitched scream. Mr. Shrimp's presence sending her scurrying away to curl and hide behind a coral as it cowers in fear."

    show scy surprise at shrimp_right_pos

    scy "Huh...?!"

    show mc o at mc_pos

    mc "Can you specify who or what took your family?"

    show bunny scared at bunny_pos

    "The sea bunny seems to refuse to answer anything with Mr Shrimp nearby."

    "Choose who should ask the sea bunny! The answers it gives may vary based on its relationship with the character."

    hide mc
    hide scy

    call select_interactor_ch3

    $ seabunny_talked = True

    if _return == "mc":
        jump seabunny_ask_as_mc
    elif _return == "cory":
        jump seabunny_ask_as_cory
    else:
        jump seabunny_ask_as_scy


# =========================================================
# AS MC
# =========================================================

label seabunny_ask_as_mc:

    hide cory
    hide scy
    hide shrimp

    show mc happy at mc_pos
    show bunny scared at bunny_pos

    mc "Don’t be scared, sea bunny!"
    mc "Mr shrimp is far away now!"

    show bunny scared at bunny_pos

    bunny "He’s.. still around though.."

    show mc happy at mc_pos

    mc "It’s okay I won’t let him get near you!"

    show bunny sad at bunny_pos

    bunny "nguu.. okay I trust you…"

    menu:

        "What happened to your family?":

            show bunny sad at bunny_pos

            bunny "They were taken away.. by a big brute crab…"
            bunny "He claimed to be.. doing that under the crustacean empress' command…"
            bunny "Said that my.. kind is a threat to the sea…"

            show mc pout at mc_pos

            mc "What!! That’s awful!"
            mc "Everyone gets a chance to live at the sea no matter how dangerous!"
            mc "Without what they claim as threats.. The sea would be in a bigger danger!"

            show bunny default at bunny_pos

            bunny "Eh..? Is that so..?"

            show mc actual at mc_pos

            mc "Mhm! Even the scary stuff has a job!"
            mc "If you take it away, whatever it used to hunt just grows and grows until that's the problem instead!"
            mc "It's like a big circle predator, prey, little guys, big guys—snap one part off and the whole thing tips over!"
            mc "So whoever's calling your kind a 'threat'? They just don't get it!"

            show bunny happy at bunny_pos

            bunny "Ahh I see! Mmn! That makes perfect sense!"

            show bunny sad at bunny_pos

            bunny "If only they would understand…"

            show mc happy at mc_pos

            mc "Don’t worry we'll make them understand!!"

        "Why are you scared of Mr Shrimp?":

            show mc o at mc_pos
            show bunny scared at bunny_pos

            bunny "He’s a crustacean!!"
            bunny "They’re the kind who took my family away!"

            show bunny sad at bunny_pos

            bunny "And crustaceans they.. they all work under the crustacean empress right?"

            show mc pout at mc_pos

            mc "Mm he does but.. He’s different!"
            mc "He realized that what the empress’ pushing is wrong!"
            mc "And now we’re here to talk to the empress about it!"

            show bunny default at bunny_pos

            bunny "But will the empress hear you out…?"
            bunny "She’s very ruthless and stubborn…"

            show bunny sad at bunny_pos

            bunny "She’s not afraid to kill those who defy her…"

            show mc happy at mc_pos

            mc "mmm.. Then we’ll just fight her!"

            show bunny scared at bunny_pos

            bunny "dowawa?! Fight her..?!"

            show mc excited at mc_pos

            mc "Yeah! Mr Cory will tank all her attacks!"

            show bunny happy at bunny_pos

            bunny "That’s so very cool!! You need your own shounen series!"

            show mc shock at mc_pos

            mc "shounen? Ah!! Like Chainsaw Man?"

            show bunny happy at bunny_pos

            bunny "Yes!! Ah finally someone that gets it!!"

        "Do you need a hug?":

            show bunny scared at bunny_pos

            bunny "i..!"

            show bunny sad at bunny_pos

            bunny "As much as I’d very much like one… right now"

            show bunny cry at bunny_pos

            bunny "nnghh shiku shiku *sniffle* you can’t hug me..!!"

            if has_item("rainbow_algae"):
                show mc happy at mc_pos
                mc "It’s fine! I know sea bunnies contain this weird toxin in their bodies but.."

                show mc actual at mc_pos
                mc "Try eating this.. I read that what makes seabunny toxic is what they eat!"

                show bunny default at bunny_pos
                bunny "mn.. huh? Rainbow algae.."
                bunny "Even when it’s true.. The sponges that we eat are still crucial for our survival…"
                $ bunny_fed = True

            show mc happy at mc_pos

            mc "mm then I’ll still hug you!"

            show bunny scared at bunny_pos

            bunny "huh?"

            show mc excited at mc_pos

            mc "I don’t mind a little itch! You look very fluffy to touch!"

            show bunny scared at bunny_pos

            bunny "B-but..!"

            "Without letting those words finish, I pulled it into a tight hug. Burying my face into its fluffy looking appendages."

            show bunny cry at bunny_pos

            bunny "uu.. UEHHHH"

            show mc happy at mc_pos

            mc "it’s okay.. Let it all out"

            show bunny cry at bunny_pos

            bunny "UHNNG I MISS MY FAAAMILY.. I MISS THEM!!"
            bunny "ITS ALL MY FAAAULT UEEEEH…!!!!"

            show mc pout at mc_pos

            mc "no no it's not!!"

            show mc default at mc_pos

            mc "it's a good thing that you're still here with us…"

            show mc happy at mc_pos

            mc "don't worry sea bunny we’ll get your family back!!"

            show bunny sad at bunny_pos

            bunny "promise…?"

            mc "mhm! Pinky promise!!"
            $ bunny_hugged = True

    hide mc
    hide bunny

    return


# =========================================================
# AS CORY
# =========================================================

label seabunny_ask_as_cory:

    hide mc
    hide scy
    hide shrimp

    show cory smile_hu at cory_right_pos
    show bunny default at bunny_pos

    cory "Ay, easy now slug.."
    cory "I’ve driven the shrimp away for a bit, you’re safe"

    show bunny default at bunny_pos

    bunny "Thank you.. You have my gratitude…"

    "The sea bunny bows down in expression of gratitude."

    show bunny sad at bunny_pos

    bunny "Also.. please don’t refer to me with that.. S word…"

    show cory side at cory_right_pos

    cory "S word…?"

    bunny "And ends with a g…"

    show cory side at cory_right_pos

    cory "Oh right! My bad.."

    show cory smile at cory_right_pos

    cory "What would you like to be called then?"

    show bunny default at bunny_pos

    bunny "Sea bunny or nudibranch is fine.."

    menu:

        "Mind telling us what happened?":

            show cory netral_hu at cory_right_pos
            show bunny default at bunny_pos

            bunny "Me and my family were just having a nice sunny picnic.. under the pink acropora coral…"

            show bunny happy at bunny_pos

            bunny "Laughter all around.. As we feed each other sponges…"
            bunny "I was going out a little to pick more sponges for us…"

            show bunny scared at bunny_pos

            bunny "Until.. A big brute crab suddenly came through"

            show bunny sad at bunny_pos

            bunny "So I hid behind a coral…"
            bunny "He said he was hungry.. So my mom tried to offer him a sponge but..!"
            bunny "He tried it.. He spat it out.. Then he moves over to.. My- and he-!"

            show bunny scared at bunny_pos

            bunny "He..! He ate.. My baby sibling..!!"

            show cory surprise at cory_right_pos

            cory "Oh shrimp.. That’s real messed up…"

            show cory side at cory_right_pos

            cory "I’m so very sorry…"

            show bunny default at bunny_pos

            bunny "But we sea bunnies.. have toxins in our bodies…"
            bunny "When the crab took a bite.. The toxins start eating him out from inside"
            bunny "Angered.. He then took the rest of my family away claiming us as a danger to the sea…"

            show bunny sad at bunny_pos

            bunny "At least.. my sibling fought until the very end…"
            bunny "I still couldn’t forgive myself for letting that crab get away…"
            bunny "And for letting it all.. happen… It’s my fault.."

            show bunny cry at bunny_pos

            bunny "UEEEEHH SHIKU SHIKU"

            show cory upset at cory_right_pos

            cory "Hey, hey don’t blame yourself now!"

            show cory netral at cory_right_pos

            cory "What could ya possibly do anyway? If you jump out you’ll get kidnapped too!"

            show cory netral_hu at cory_right_pos

            cory "What you did was the best choice, so now you can save your family"

            show bunny cry at bunny_pos

            bunny "uuu…"

            show cory netral_hu at cory_right_pos

            cory "Don’t worry we’ll get him"
            cory "We’re planning to overthrow this whole crustacean dictator bullshrimp"

        "I’m sorry to hear about your family.. must be tough on ya..":

            show cory side at cory_right_pos
            show bunny sad at bunny_pos

            bunny "Mm…"

            show cory netral at cory_right_pos

            cory "I had a little sister too.."

            show cory smile_hu at cory_right_pos

            cory "Real ball of sunshine.."

            show cory netral_hu at cory_right_pos

            cory "But she got some kind of weird sickness going on.. that eventually separates us…"

            show cory sideclose at cory_right_pos

            cory "guh sorry for the sudden vent.. I'll stop now"

            show bunny default at bunny_pos

            bunny "No! It’s fine.. She must’ve been really dear to you.. I’m sorry…"

            show cory side at cory_right_pos

            cory "She’s still alive though.. Somewhere in this vast sea…"

            if has_item("rainbow_algae"):
                show cory smile_hu at cory_right_pos
                cory "Ah, Have you eaten anything? I’ve got some algae for ya.."
                cory "And it’s rainbow algae!"

                show bunny happy at bunny_pos
                bunny "Rainbow algae..? so pretty! kirakira"
                bunny "Thank you!"

                show bunny sad at bunny_pos
                bunny "But I.. I don’t think I can.. eat after what I had to witness…"

                show cory netral_hu at cory_right_pos
                cory "You can’t be like that… your family wouldn’t want ya to skip meals would they?"

                bunny "..."

                show cory smile_hu at cory_right_pos
                cory "Eat up sea bunny.."

                show cory fond at cory_right_pos
                cory "So you’ve got the strength to look at them in the eyes when ya meet them again"

                show bunny default at bunny_pos
                bunny "You’re right.. Thank you.."
                $ bunny_fed = True

    hide cory
    hide bunny

    return


# =========================================================
# AS SCYLLARUS
# =========================================================

label seabunny_ask_as_scy:

    hide mc
    hide cory

    show scy default at shrimp_right_pos
    show bunny scared at bunny_pos

    "The sea bunny stands at a reasonably far distance."

    show bunny scared at bunny_pos

    bunny "Your red shelled kind! the one who does all of this evil baka stuff!"

    show bunny sad at bunny_pos

    bunny "My family.. Is detained for simply living…"

    show scy defaultom at shrimp_right_pos

    scy "Oh! It’s probably one of the crustaceans' doing!"

    menu:

        "Apologize in advance":

            "Mr Shrimp took a few steps forward to properly bow down in an apologetical manner."

            show scy defaultom at shrimp_right_pos

            scy "I apologize for the inconvenience that my kind has inflicted upon your family!"

            show bunny scared at bunny_pos

            bunny "EEEK-!"

            "The sea bunny curls up in fear."

            bunny "I.. kindly.. ask you to stay away.. Please…!"

            show scy default at shrimp_right_pos

            scy "...! Understood!"
            scy "Then I shall stand at a safe, reasonable distance!"

            "Mr Shrimp took exactly one step away from the sea bunny."

            show bunny scared at bunny_pos

            bunny "T-that’s not enough distance!"

        "Please accept this algae as a token of apology!":

            show scy shy at shrimp_right_pos

            scy "I was informed that algae counts as one of your diet!"

            show bunny scared at bunny_pos

            bunny "...?!"
            bunny "I.. I read this in mangas before!"
            bunny "It’s probably poisoned right?! Or.."
            bunny "Or you make it super delicious.."
            bunny "And when I’m busy eating your gift.. piri piri..."
            bunny "BAAN!! You kidnap me!"

            show scy surprise at shrimp_right_pos

            scy "WHAT! Preposterous! I wouldn’t do such dirty tactics!"

            show bunny sad at bunny_pos

            bunny "Guuu..! You’ll never know! Must keep guard up! kuyo kuyo…"

            show scy sepet at shrimp_right_pos

            scy "And manga.. Is that some kind of.. new type of algaes?!"

            show scy defaultom at shrimp_right_pos

            scy "I’ll search for one if it makes you forgive us!"

            "The sea bunny refuses to take the algae from Mr. Shrimp."

    hide scy
    hide bunny

    return
