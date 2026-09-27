label seabunny_encounter:
    hide mc
    scene ch3_day
    "A seabunny is found crying behind luscious corals. I wonder what made it cry that loud?"
    $ focus()

    show mc o:
        full
        right 
        toleft
    with moveinright
    show bunny cry:
        full
        unpose
    show bunny cry:
        center
        vibrate
    with moveinright
    bunny "nghuuuu.. ueeeh… ueeh!!!!"

    show mc shock:
        full
        right
        toleft
        surprise
    mc "huh..? What's wrong?"
    bunny "uuu.. shiku shiku.. My family.. They took them!!"

    show bunny cry:
        full
        leftish
    with move
    show shrimp default_om:
        full
        unpose
        offscreenleft
    show shrimp default_om:
        centerright
        walkloop
    with moveinright
    scy "And who exactly is this \"they\"?!"

    show bunny scared:
        full 
        leftish
        surprise
    bunny "GYAAA IT'S THEM IT'S THEM!!"
    "The bunny shaped slug lets out a high pitched scream." 
    
    show bunny scared:
        full 
        leftish
        vibrate
    "Mr. Shrimp's presence sending her scurrying away to curl and hide behind a coral as it cowers in fear."

    show shrimp surprise:
        full 
        centerright
        surprise
    scy "Huh…?!"

    show mc o:
        offscreenright
        full
        right
        toleft
    mc "Can you specify who or what took your family?"

    show bunny scared:
        full
        leftish
    "The sea bunny seems to refuse to answer anything with Mr Shrimp nearby"
    $ focus()

    hide mc
    hide cory
    hide shrimp
    hide bunny

    call screen choose_interactor(
        "Choose who should ask Sea Bunny!",
        "The answers may vary based on the character asking"
    )

    $ selected_questioner = _return

    if selected_questioner == "mc":
        jump ch3_seabunny_as_mc
    elif selected_questioner == "cory":
        jump ch3_seabunny_as_cory
    else:
        jump ch3_seabunny_as_scyllarus

label ch3_seabunny_as_mc:
    $ focus ()
    show mc happy:
        full
        unpose
        offscreenright
    show mc happy:
        right
        walkto(right)
        toleft
        walkloop
    with moveinright
    show bunny scared:
        full
        unpose
        offscreenright
    show bunny scared:
        center
        vibrate
    with moveinright
    mc "Don't be scared, sea bunny!"
    mc "Mr shrimp is far away now!"
    bunny "He's.. still around though.."
    mc "It's okay I won't let him get near you!"

    show mc happy:
        full
        right
    show bunny sad:
        full
        center
    bunny "Nguu.. okay I trust you…"
    $ focus ()
    hide mc
    hide bunny
    menu:
        "What happened to your family?":
            $ focus ()
            show mc happy:
                full
                offscreenright
            show mc happy:
                right
            with moveinright
            show bunny sad:
                full
                unpose
                offscreenright
            show bunny sad:
                center
            with moveinright
            bunny "They were taken away.. by a big brute crab.."
            bunny "He claimed to be.. doing that under the crustacean empress 'command.."
            bunny "Said that my.. kind is a threat to the sea…"

            show mc pout:
                full
                right
                vibrate
            mc "What!! That's awful!"
            mc "Everyone gets a chance to live at the sea no matter how dangerous!"
            mc "Without what they claim as threats.. The sea would be in a bigger danger!"

            show bunny default:
                full
                center
            bunny "Eh..? Is that so..?"

            show mc default:
                full
                right
            mc "Mhm!"
            mc "Mhm! Even the scary stuff has a job!"

            show mc actually:
                full
                right
            mc "If you take it away, whatever it used to hunt just grows and grows until that's the problem instead!"
            mc "It's like a big circle predator, prey, little guys, big guys"
            mc "snap one part off and the whole thing tips over!"
            mc "So whoever's calling your kind a 'threat'? They just don't get it!"

            show bunny happy:
                full
                center
            bunny "Ahh I see! Mmn! That makes perfect sense!"

            show bunny sad:
                full
                center
            bunny "If only they would understand…"

            show mc happy:
                full
                right
                surprise
            mc "Don't worry we'll make them understand!!"
            $ focus ()
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue

        "Why are you scared of Mr Shrimp?":
            $ focus ()
            show mc o:
                full
                offscreenright
            show mc o:
                right 
            with moveinright
            show bunny scared:
                full
                offscreenright
            show bunny scared:
                center
                vibrate
            with moveinright
            bunny "He's a crustacean!!"
            bunny "They're the kind who took my family away!"

            show bunny sad:
                full
                center
            show mc o:
                full
                right
            bunny "And crustaceans they.. they all work under the crustacean empress right?"

            show mc pout:
                full
                right
                vibrate
            mc "Mm he does but.. He's different!"
            mc "He realized that what the empress' pushing is wrong!"
            mc "And now we're here to talk to the empress about it!"

            show bunny default:
                full
                center
            bunny "But will the empress hear you out…?"
            bunny "She's very ruthless and stubborn…"

            show bunny sad:
                full
                center
                vibrate
            bunny "She's not afraid to kill those who defy her…"

            show mc happy:
                full
                right
            mc "Mmm.. Then we'll just fight her!"

            show bunny scared:
                full
                center
                surprise
            bunny "dowawa?! Fight her..?!"

            show mc excited:
                full
                right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "Yeah! Mr Cory will tank all her attacks!"

            show bunny happy:
                full
                center
            bunny "That's so very cool!! You need your own shounen series!"

            show mc shock:
                full
                right
                surprise
            mc "shounen? Ah!! Like Chainsaw Man?"

            show bunny happy:
                full
                center
                surprise
            bunny "Yes!! Ah finally someone that gets it!!"
            $ focus ()
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue
        "Do you need a hug? (Give rainbow algae)" if has_rainbow_algae:
            $ focus ()
            show mc o:
                full
                offscreenright
            show mc o:
                right
            with moveinright
            show bunny scared:
                full
                offscreenright
            show bunny scared:
                center
                surprise
            with moveinright
            bunny "i..!"

            show bunny sad:
                full
                center
            bunny "As much as I'd very much like one…right now"

            show bunny cry:
                full
                center
                vibrate
            bunny "nnghh shiku shiku *sniffle* you can't hug me..!!"

            show mc happy:
                full
                right
            mc "It's fine! I know sea bunnies contain this weird toxin in their bodies but.."

            show mc actually:
                full
                right
            mc "Try eating this.. I read that what makes seabunny toxic is what they eat!"

            show bunny default:
                full
                center
            bunny "Mnn.. huh? Rainbow algae.."
            bunny "Even when it's true.. The sponges that we eat are still crucial for our survival.."

            show mc happy:
                full
                right
            mc "Mm then, I'll still hug you!"

            show bunny scared:
                full
                center
            seabunny "Huh?"

            show mc excited:
                full
                right
                block:
                    jumpmc
                    pause 1
                    repeat
            mc "I don't mind a little itch! You look very fluffy to touch!"

            show bunny scared:
                full 
                center
            bunny "B-but..!"

            "Without letting those words finish, I pulled it into a tight hug. Burying my face into its fluffy looking appendages."

            show bunny cry:
                full
                center
            bunny "uu.. UEHHHH"

            show mc happy:
                full
                right
            mc "It's okay.. Let it all out"

            show bunny cry:
                full
                center
                vibrate
            bunny "UHNNG I MISS MY FAAAMILY.. I MISS THEM!!"
            bunny "ITS ALL MY FAAAULT UEEEEH…!!!!"

            show mc pout:
                full
                right
                vibrate
            mc "No, no, it's not!!"

            show mc default:
                full
                right
            mc "It's a good thing that you're still here with us…"

            show mc happy:
                full
                right
            mc "Don't worry sea bunny we'll get your family back!!"

            show bunny sad:
                full
                center
            bunny "Promise…?"
            mc "Mhm! Pinky promise!!"
            $ focus ()
            $ gave_algae_to_seabunny = True
            $ has_rainbow_algae = False
            $ ch3_seabunny_helped = True
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue

label ch3_seabunny_as_cory:
    $ focus ()
    show cory smile_hu:
        full
        unpose
        offscreenright
    show cory smile_hu:
        leftish
        walkto(leftish)
        toleft
        walkloop
    with moveinright
    show bunny scared:
        full
        unpose
        offscreenright
    show bunny scared:
        centerright
        vibrate
    with moveinright
    cory "Ay, easy now slug.."
    cory "I've driven the shrimp away for a bit, you're safe"

    show bunny default:
        full
        centerright
    bunny "Thank you.. You have my gratitude…"

    "Sea bunny bows down in expression of gratitude"

    show bunny sad:
        full
        centerright
    bunny "Also.. please don't refer to me with that.. S word.."

    show cory smile_hu:
        full
        leftish
    cory "S word…?"
    bunny "And ends with a g.."

    show cory side:
        full
        leftish
    cory "Oh right! My bad.."

    show cory smile:
        full
        leftish
    cory "What would you like to be called then?"

    show bunny default:
        full
        centerright
    bunny "Sea bunny or nudibranch is fine.."
    $ focus ()
    hide cory
    hide bunny
    menu:
        "Mind telling us what happened?":
            $ focus ()
            show cory talk_hu:
                full
                offscreenright
            show cory talk_hu:
                leftish
            with moveinright
            show bunny default:
                full
                offscreenright
            show bunny default:
                centerright
            with moveinright
            bunny "Me and my family were just having a nice sunny picnic.. under the pink acropora coral…"

            show bunny happy:
                full
                centerright
            bunny "Laughter all around.. As we feed each other sponges.."
            bunny "I was going out a little to pick more sponges for us.."

            show bunny scared:
                full 
                centerright
            bunny "Until.. A big brute crab suddenly came through"

            show bunny sad:
                full
                centerright
                vibrate
            bunny "So I hid behind a coral.."
            bunny "He said he was hungry.. So my mom tried to offer him a sponge but..!"
            bunny "He tried it.. He spat it out.. Then he moves over to.. My- and he-!"

            show bunny scared:
                full
                centerright
                vibrate
            bunny "He..! He ate.. My baby sibling..?!"

            show cory surprise:
                full
                leftish
                surprise
            cory "Oh shrimp.. That's real messed up…"

            show cory side:
                full
                leftish
            cory "I'm so very sorry…"

            show bunny default:
                full
                centerright
            bunny "But we sea bunnies.. have toxins in our bodies.."
            bunny "When the crab took a bite.. The toxins start eating him out from inside"
            bunny "Angered.. He then took the rest of my family away claiming us as a danger to the sea.."

            show bunny sad:
                full
                centerright
            bunny "At least.. my sibling fought until the very end.."
            bunny "I still couldn't forgive myself for letting that crab get away…"
            bunny "And for letting it all.. happen… It's my fault.."

            show bunny cry:
                full
                centerright
                vibrate
            bunny "UEEEEHH SHIKU SHIKU"

            show cory upset:
                full
                leftish
            cory "Hey, hey don't blame yourself now!"

            show cory talk:
                full
                leftish 
            cory "What could ya possibly do anyway? If you jump out you'll get kidnapped too!"

            show cory talk_hu:
                full
                leftish
            cory "What you did was the best choice, so now you can save your family"

            show bunny cry:
                full
                centerright
            bunny "uuu…"

            show cory talk_hu:
                full
                leftish
            cory "Don't worry we'll get him"
            cory "We're planning to overthrow this whole crustacean dictator bullshrimp"
            $ focus ()
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue

        "I'm sorry to hear about your family.. must be tough on ya.. (Give rainbow algae)" if has_rainbow_algae:
            $ focus ()
            show cory side:
                full
                offscreenright
            show cory side:
                leftish
            with moveinright
            show bunny sad:
                full
                offscreenright
            show bunny sad:
                centerright
            with moveinright
            bunny "Mm.."

            show cory talk:
                full
                leftish
            cory "I had a little sister too.."

            show cory smile_hu:
                full
                leftish
            cory "Real ball of sunshine.."

            show cory talk_hu:
                full
                leftish
            cory "But she got some kind of weird sickness going on.. that eventually separates us…"

            show cory side_close:
                full
                leftish
            cory "guh sorry for the sudden vent.. I'll stop now"

            show bunny default:
                full
                centerright
            bunny "No! It's fine.. She must've been really dear to you.. I'm sorry.."

            show cory side:
                full
                leftish
            cory "She's still alive though.. Somewhere in this vast sea.."

            show cory smile_hu:
                full
                leftish
            cory "Ah, Have you eaten anything? I've got some algae for ya.."
            cory "And it's rainbow algae!"

            show bunny happy:
                full
                centerright
                surprise
            bunny "Rainbow algae..? so pretty! kirakira"
            bunny "Thank you!"

            show bunny sad:
                full
                centerright
            bunny "But I.. I don't think I can.. eat after what I had to witness…"

            show cory talk_hu:
                full
                leftish
            cory "You can't be like that… your family wouldn't want ya to skip meals would they?"
            bunny "..."

            show cory smile_hu:
                full
                leftish
            cory "Eat up sea bunny.."

            show cory fond:
                full
                leftish
            cory "So you've got the strength to look at them in the eyes when ya meet them again"

            show bunny default:
                full
                centerright
            bunny "You're right.. Thank you.."
            $ focus ()
            $ gave_algae_to_seabunny = True
            $ has_rainbow_algae = False
            $ ch3_seabunny_helped = True
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue

label ch3_seabunny_as_scyllarus:
    "The sea bunny stands at a reasonably far distance"
    $ focus ()
    show bunny scared:
        full
        unpose
        offscreenright
    show bunny scared:
        leftish
        walkto(leftish)
        toleft
        vibrate
    with moveinright
    show scy default_om:
        full
        unpose
        offscreenright
    show scy default_om:
        centerright
        walkloop
    with moveinright
    bunny "Your red shelled kind! the one who does all of this evil baka stuff!"

    show bunny sad:
        full
        leftish
    bunny "My family.. Is detained for simply living…"

    show scy default:
        full
        centerright
        surprise
    scy "Oh! It's probably one of the crustaceans doing!"
    $ focus ()
    hide scy
    hide bunny
    menu:
        "Apologize in advance":
            "Mr Shrimp took a few steps forward to properly bow down in an apologetical manner"
            $ focus ()
            show scy default_om:
                full
                unpose
                offscreenright
            show scy default_om:
                centerright
            with moveinright
            show bunny scared:
                full
                offscreenright
            show bunny scared:
                leftish
                vibrate
            with moveinright
            scy "I apologize for the inconvenience that my kind has inflicted upon your family!"
            bunny "EEEK-!"

            "The sea bunny curls up in fear"
            bunny "I.. kindly.. ask you to stay away.. Please…!"

            show scy default:
                full
                centerright
            scy "...! Understood!"
            scy "Then I shall stand at a safe, reasonable distance!"

            "Mr Shrimp took exactly one step away from the sea bunny"

            show scy default:
                full
                right
            with move
            show bunny scared:
                full
                leftish
                surprise
            bunny "T-that's not enough distance!"
            $ focus ()
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue

        "Please accept this algae as a token of apology!" if has_rainbow_algae:
            $ focus ()
            show scy shy:
                full
                unpose
                offscreenright
            show scy shy:
                centerright
            with moveinright
            show bunny scared:
                full
                offscreenright
            show bunny scared:
                leftish
                vibrate
            with moveinright
            scy "I was informed that algae counts as one of your diet!"

            show bunny scared:
                full
                leftish
                surprise
            bunny "...?!"
            show bunny scared:
                full
                leftish
                vibrate
            bunny "I.. I read this in mangas before!"
            bunny "It's probably poisoned right?! Or.."
            bunny "Or you make it super delicious.."
            bunny "And when I'm busy eating your gift.. piri piri..."
            bunny "BAAN!! You kidnap me!"

            show scy surprise:
                full
                centerright
                surprise
            scy "WHAT! Preposterous! I wouldn't do such dirty tactics!"

            show bunny sad:
                full
                leftish
                vibrate
            bunny "Guuu..! You'll never know! Must keep guard up! kuyo kuyo…"

            show scy sepet:
                full
                centerright
            scy "And manga.. Is that some kind of.. new type of algaes?!"

            show scy default_om:
                full
                centerright
            scy "I'll search for one if it makes you forgive us!"

            "The sea bunny refuses to take the sea algae"
            $ focus ()
            $ ch3_visited_seabunny = True
            jump ch3_day_explore_continue
