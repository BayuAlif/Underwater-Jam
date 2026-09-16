# ============================================================
# CHAPTER 3 — SCAFFOLD
# NOTE: only the NPC art for chapter 3 (dunge/crab, hawk/turtle, teto/gobypis,
# seabunny) existed in the project files — there was no chapter 3 story script
# or npc interaction logic yet (unlike chapter 1 & 2, which each have their
# own game/npc/chapterX/*.rpy files). This file is a minimal, working
# placeholder so "prologue -> chapter1 -> chapter2 -> chapter3" runs end to
# end without crashing. Replace/expand the dialogue below with the real
# Chapter 3 story; the label name (chapter3_start) is what chapter2.rpy jumps
# to, so keep that if you rename anything else.
# ============================================================

label chapter3_start:

    $ current_chapter = 3
    $ current_cycle = "day"

    scene ch3_day
    with fade

    "The current grew colder, and the light from above thinned into a pale blue haze."

    show mc default at mc_left
    show cory side at cory_left

    mc "...We made it to the deep current?"

    show cory talk at cory_left
    cory "Yeah. Past this point, it ain't freshwater rules no more, guppy."

    show mc o at mc_left
    mc "Feels different down here.."

    show cory smile at cory_left
    cory "Get used to it. Reef folks out here got their own way of doing things."

    jump chapter3_reef_exploration


label chapter3_reef_exploration:

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
    mc "Everyone's so nice here!"

    "For now, the reef kept its secrets close — but something told me our search for the north current was far from over."

    # TODO: continue Chapter 3 from here (Teto/gobypis, the main quest hook,
    # any duel/exploration segments, and the chapter's ending).

    return
