# =========================================================
# GAME SCRIPT - CHAPTER 1 (NIGHT CYCLE)
# =========================================================

# Deklarasi Karakter
define mc = Character("MC", color="#ffffff")
define cory = Character("Cory", color="#00a86b")
define F1 = cory
define lele = Character("Mr. Catfish", color="#90ee90")
define alligator = Character("Ms. Gator", color="#ff7f50")
define system = Character("System", color="#888888")

# Variabel Karakter Aktif
default current_character = "MC"

# Background dialog malam (Aset utuh 1920x1080 tanpa lubang)
image bg_dialog_night = "images/background/FIXbgnight1.png"

# =========================================================
# TRANSFORM POSISI KARAKTER (1080p)
# =========================================================
transform mc_left:
    xalign 0.12
    yalign 0.95

transform npc_right:
    xalign 0.85
    yalign 0.95

transform npc_center:
    xalign 0.5
    yalign 0.95

# =========================================================
# DEKLARASI SPRITE MC
# =========================================================
image mc default = Transform("images/Mc/McDefault.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc normal = "mc default"
image mc netral = "mc default"

image mc happy = Transform("images/Mc/McHappy.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc senang = "mc happy"
image mc senyum = "mc happy"

image mc actually = Transform("images/Mc/McActually.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc normal2 = "mc actually"
image mc smug = "mc actually"

image mc excited = Transform("images/Mc/McExcited.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc exited = "mc excited"
image mc semangat = "mc excited"

image mc dizzy = Transform("images/Mc/McDizzy.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc bingung = "mc dizzy"
image mc bingung1 = "mc dizzy"
image mc pusing = "mc dizzy"

image mc dizzy actually = Transform("images/Mc/McDizzyActually.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc bingungbanget = "mc dizzy actually"
image mc bingungbanget2 = "mc dizzy actually"

image mc o = Transform("images/Mc/Mc_o.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc _o = "mc o"
image mc bingung2 = "mc o"
image mc wow = "mc o"

image mc shock = Transform("images/Mc/McShock.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc kaget = "mc shock"
image mc dongok = "mc shock"
image mc surprised = "mc shock"

image mc shock hu = Transform("images/Mc/McShockHU.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc shockhu = "mc shock hu"
image mc kaget hu = "mc shock hu"
image mc dongok hu = "mc shock hu"

image mc pout = Transform("images/Mc/McPout.png", crop=(1200, 0, 1150, 1440), zoom=0.6875)
image mc gakpuas = "mc pout"
image mc cemberut = "mc pout"
image mc kecewa = "mc pout"

# =========================================================
# DEKLARASI SPRITE CORY (F1)
# =========================================================
image cory normal = Transform("images/cory/CoryTalkNetral.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory netral = "cory normal"
image cory talk netral = "cory normal"

image cory normal hu = Transform("images/cory/CoryTalkNetralHU_.png", crop=(400, 0, 1120, 1440), zoom=0.6875)
image cory netral hu = "cory normal hu"
image cory talk netral hu = "cory normal hu"

image cory smile = Transform("images/cory/CoryTalkSmile.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory senang = "cory smile"
image cory talk smile = "cory smile"

image cory smile hu = Transform("images/cory/CoryTalkSmileHU.png", crop=(400, 0, 1120, 1440), zoom=0.6875)
image cory senang hu = "cory smile hu"
image cory talk smile hu = "cory smile hu"

image cory fond = Transform("images/cory/CoryFondSmile.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory fond smile = "cory fond"

image cory proud = Transform("images/cory/CoryProud.png", crop=(400, 0, 900, 1440), zoom=0.6875)
image cory bangga = "cory proud"

image cory proud hu = Transform("images/cory/CoryProudHU.png", crop=(400, 0, 1120, 1440), zoom=0.6875)
image cory bangga hu = "cory proud hu"

image cory surprise = Transform("images/cory/CorySurprise.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory surprised = "cory surprise"
image cory kaget = "cory surprise"

image cory surprise hu = Transform("images/cory/CorySurpriseHU.png", crop=(400, 0, 1120, 1440), zoom=0.6875)
image cory surprised hu = "cory surprise hu"
image cory kaget hu = "cory surprise hu"

image cory upset = Transform("images/cory/CoryUpset.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory marah = "cory upset"
image cory kecewa = "cory upset"

image cory upset hu = Transform("images/cory/CoryUpsetHU.png", crop=(400, 0, 1120, 1440), zoom=0.6875)
image cory marah hu = "cory upset hu"

image cory disrespectful = Transform("images/cory/CoryDisrespectful_.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory remeh = "cory disrespectful"

image cory unimpressed1 = Transform("images/cory/CoryOhiounimpressed1_.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory ohio1 = "cory unimpressed1"

image cory unimpressed2 = Transform("images/cory/CoryOhiounimpressed2.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory ohio2 = "cory unimpressed2"

image cory side = Transform("images/cory/CorySide.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory samping = "cory side"

image cory side close = Transform("images/cory/CorySideClose.png", crop=(410, 0, 900, 1440), zoom=0.6875)
image cory samping tutup = "cory side close"

# Alias F1 untuk Cory
image F1 normal = "cory normal"
image F1 smile = "cory smile"
image F1 fond = "cory fond"
image F1 proud = "cory proud"
image F1 surprise = "cory surprise"
image F1 upset = "cory upset"
image F1 disrespectful = "cory disrespectful"
image F1 side = "cory side"

# =========================================================
# DEKLARASI SPRITE MS. GATOR (ALLIGATOR)
# =========================================================
image gator default = Transform("images/npc/GatorDefault.png", crop=(80, 0, 1260, 1440), zoom=0.6875)
image gator smile = Transform("images/npc/GatorSmile.png", crop=(80, 0, 1260, 1440), zoom=0.6875)
image gator annoyed = Transform("images/npc/GatorAnnoyed.png", crop=(80, 0, 1260, 1440), zoom=0.6875)
image gator surprised = Transform("images/npc/GatorSurprised.png", crop=(80, 0, 1260, 1440), zoom=0.6875)
image gator upset = Transform("images/npc/GatorUpset.png", crop=(80, 0, 1260, 1440), zoom=0.6875)

image alligator default = "gator default"
image alligator smile = "gator smile"
image alligator annoyed = "gator annoyed"
image alligator surprised = "gator surprised"
image alligator upset = "gator upset"

# =========================================================
# DEKLARASI SPRITE MR. CATFISH (LELE)
# =========================================================
image lele default = Transform("images/npc/LeleDefault.png", crop=(1260, 0, 1080, 1440), zoom=0.6875)
image lele curiga = Transform("images/npc/LeleCuriga.png", crop=(1260, 0, 1080, 1440), zoom=0.6875)
image lele depan = Transform("images/npc/LeleDepan.png", crop=(1260, 0, 1080, 1440), zoom=0.6875)
image lele purapuratidur = Transform("images/npc/LelePuraPuraTidur_.png", crop=(1260, 0, 1080, 1440), zoom=0.6875)
image lele tidur = "lele purapuratidur"


# =========================================================
# START LABEL
# =========================================================
label start:
    show screen day_night_hud

    # ---------------------------------------------------------
    # SCENE 1-5 (DAY CYCLE)
    # ---------------------------------------------------------
    $ load_area("beach")
    scene expression get_background() with fade
    
    system "--- SCENE 1-5: DAY CYCLE ---"
    mc "Semua objective siang beres! Waktunya masuk ke malam hari..."


    # ---------------------------------------------------------
    # SETUP MALAM (SCENE 1: DIALOG PEMBUKA - BG UTUH)
    # ---------------------------------------------------------
    $ change_cycle()
    
    # Background normal tanpa lubang untuk dialog pembuka
    scene bg_dialog_night with fade

    "After spending some time exploring the riverbed, the warm light above us slowly began to fade."
    "The golden rays that once danced across the water became dimmer and dimmer."
    
    show mc bingung at mc_left with dissolve
    mc "..."
    mc "Mr. Cory?"
    mc "Its getting dark.. is it night already?"
    show cory normal at npc_right with dissolve
    F1 "Time flies when yer busy picking up rocks."
    
    show mc senang with dissolve
    mc "Cool rocks!"
    show cory smile with dissolve
    F1 "they sure are."
    
    "The last traces of sunlight slowly disappeared behind the surface."
    "For a moment, the riverbed was bathed in a pretty faint blue glow."
    "Then… The world went dark."
    
    show mc bingungbanget with dissolve
    mc "..."
    "I looked around."
    "The river looked completely different."
    "The familiar rocks were now little more than silhouettes."
    "The plants swayed slowly in darkness, their shadows stretching across the riverbed."
    
    show mc bingungbanget with dissolve
    mc "Whoa…"
    show cory normal with dissolve
    F1 "Don’t wander too far."
    
    show cory normal hu with dissolve
    F1 "Night’s a little different around here."
    "Then suddenly the golden scale in my palm starts to emit a soft blue glow. Giving a small light to those around me"
    
    show cory smile with dissolve
    show mc bingung2 with dissolve
    F1 "well that's.. convenient!"
    show cory normal with dissolve
    F1 "Though still,"
    F1 "Keep your eyes open.. We dont know what might lurk in here"

    hide mc
    hide cory
    with dissolve


# =========================================================
# LOOPING EKSPLORASI MALAM (SCENE 2: MAP EKSPLORASI BERLUBANG)
# =========================================================
label night_exploration_loop:

    # 1. Pengecekan Syarat dari Progress Manager
    if night_objectives_complete():
        jump area_clear_transition

    # 2. Tampilkan background berlubang (night_bg)
    scene expression get_background() with fade

    # 3. Panggil Screen NPC & Item
    call screen screen_item_npc


    # ---------------------------------------------------------
    # INTERAKSI A: PICK UP ITEM (AMBALABU)
    # ---------------------------------------------------------
    if _return == "item_taken":
        scene bg_dialog_night with fade
        
        show mc senang at mc_left with dissolve
        "Item get: Ambalabu"
        show cory surprise at npc_right with dissolve
        F1 "...!"
        F1 "is that what i think it is??"
        
        show mc bingung2 with dissolve
        mc "what is it mr cory?"
        show cory disrespectful with dissolve
        F1 "eh, just a toy.. A very popular one"
        show cory smile with dissolve
        F1 "I might know who might like this… hah!"
        
        hide mc
        hide cory
        with dissolve
        jump night_exploration_loop


    # ---------------------------------------------------------
    # INTERAKSI B: NPC 3 - LELE (CATFISH)
    # ---------------------------------------------------------
    elif _return == "talk_fish03":
        
        scene bg_dialog_night with fade
        
        show lele purapuratidur at npc_right with dissolve
        "A small catfish quietly watches from behind some seaweed."
        
        show mc senang at mc_left with dissolve
        mc "I see you Mr catfish!"
        
        show lele curiga with dissolve
        lele "..."
        "The catfish eyes me for a long second before going back into hiding. It appears to be somewhat shy?"
        "But as soon as Mr Cory swam forward its head peek in interest, like seeing an old friend"
        
        show lele depan with dissolve
        hide mc
        show cory smile at mc_left with dissolve
        F1 "ay.. Good pal, catfish."
        show stiker admin_datang at stiker_lele
        lele "Here comes admin huh?"
        
        hide stiker with dissolve
        hide cory
        show mc bingung at mc_left with dissolve
        "mm maybe i should let mr cory asks instead?"

        # PILIHAN ROTASI INTEROGASI (MC / CORY)
        system "Choose who should ask mr catfish! The answers it gave may varied based on its relationship with the character"

        call screen rotasi_ikan_select(
            title="PILIH KARAKTER INTEROGASI",
            subtitle="Choose who should ask Mr. Catfish!"
        )

        if _return == "mc":
            jump lele_interrogation_mc
        elif _return == "cory":
            jump lele_interrogation_cory


    # ---------------------------------------------------------
    # INTERAKSI C: NPC 4 - ALLIGATOR
    # ---------------------------------------------------------
    elif _return == "talk_croc":
        
        scene bg_dialog_night with fade

        show gator default at npc_right with dissolve
        "An alligator lounging beside a large rock. It looked completely unbothered by anything that would be around it. One of its claws casually tapped against the rock."
        
        show mc senang at mc_left with dissolve
        mc "Hello! Good evening!"
        "The alligator slowly turned its head toward me."
        
        show gator surprised with dissolve
        alligator "Huh?"
        alligator "Oh."
        alligator "A guppy."
        
        show mc bingung2 with dissolve
        mc "Guppy! I’ve heard that a lot around… what's that mean? Do i look like a guppy?"
        
        show gator smile with dissolve
        alligator "A guppy means a guppy, guppy. FAHHH!"
        
        show mc dongok with dissolve
        mc "ohhh! I get it! (I don't get it..)"
        
        show mc exited with dissolve
        mc "anyway ms gator I’m looking for a golden fish!"
        
        show gator surprised with dissolve
        alligator "wait ya can tell I'm a gator?"
        alligator "Even down to the fact that I'm no male. impressive."
        
        show gator annoyed with dissolve
        alligator "Most thought that I'm a.. ugh, a croc."
        
        show mc normal with dissolve
        mc "mm it's pretty easy to tell an alligator and a crocodile apart.."
        mc "alligators have a U shaped snout while crocodiles have it V shaped!"
        mc "also alligators only have their upper teeth visible when the jaw is closed, while crocodiles have them both shown!"
        mc "as to how to tell the sex apart, it's the size and how slim you are"
        
        show gator smile with dissolve
        alligator "*whistle* I like this guppy."
        alligator "you were saying golden fish?"
        
        show mc exited with dissolve
        mc "Mhm! Suuuper shiny!"
        
        show gator default with dissolve
        alligator "Oh, THAT pretty thing."
        
        show mc senang with dissolve
        mc "You know it!??"
        alligator "Know it?"
        alligator "Kid, half the river’s been staring at the swimming gem."
        alligator "Thing practically lights up the whole river."
        alligator "I saw it zoom past me earlier."
        
        show mc normal with dissolve
        mc "Which direction did it go?"
        
        show gator default with dissolve
        alligator "mm.. pretty sure North…"
        
        show mc senang with dissolve
        mc "All leads roads to north!"
        hide mc
        show cory unimpressed1 at mc_left with dissolve
        F1 "ay.. i think ya got it mixed up there guppy"
        
        show gator annoyed with dissolve
        alligator "shut up. They can think on their own."
        
        show gator smile with dissolve
        alligator "Right, guppy?"
        show cory upset with dissolve
        F1 "what did ya get so defensive for!"
        
        show gator default with dissolve
        alligator "just teaching you on how to babysit."
        show cory unimpressed2 with dissolve
        F1 "who's saying what about babysitting?! I'm just accompanying the little thing!"
        
        show gator smile with dissolve
        alligator "you just defined babysitting."
        show cory disrespectful with dissolve
        F1 "since when did you care so much for a guppy anyway?"
        F1 "You always eat them for lunch, especially on Tuesdays."
        
        hide cory
        show mc bingung at mc_left with dissolve
        mc "mm, it is Tuesday today…"
        
        show gator annoyed with dissolve
        alligator "I could say the same to ya. Last time I seen you with a guppy it was when you were-"
        hide mc
        show cory upset hu at mc_left with dissolve
        F1 "LA LA LA CANT HEAR YA OVER THESE THIIICK FINS O’ MINE"
        
        show gator upset with dissolve
        alligator "OH YOU SHUT YOUR MOUTH BOY I CAN EAT YOU RIGHT ABOUT NOW."
        alligator "YOUR FOUL TASTE IS THE ONLY THING STOPPING ME."
        
        hide cory
        show mc bingungbanget2 at mc_left with dissolve
        "I stare at both of them from the sidelines. Feeling a stiff electric tension swells between them as it goes on. It was like watching mama and papa speak to each other. Maybe I should try stopping them.."

        menu:
            "Don't stop them":
                "I continue to stare as they exhaust themselves"
                
                show gator upset with dissolve
                alligator "you.. motherfucker"
                
                show mc bingungbanget with dissolve
                mc "...!"
                hide mc
                show cory upset at mc_left with dissolve
                F1 "nasty NASTY gator..!"
                
                hide cory
                show mc dongok at mc_left with dissolve
                mc "what does a motherfucker mean? :o my parents said that thing a lot too.."
                
                show gator surprised with dissolve
                hide mc
                show cory surprise at mc_left with dissolve
                F1 "....."
                alligator "......."
                show cory normal hu with dissolve
                F1 "it means uhh-!"
                show cory proud with dissolve
                F1 "Means that you love your mother a lot!"
                
                hide cory
                show mc senang at mc_left with dissolve
                mc "ohh I love my mama! so I'm a motherfucker too! :D"
                
                show gator annoyed with dissolve
                alligator ".... No! Motherfucker means you HATE your mother, guppy."
                alligator "don't listen to that fish"
                
                show mc gakpuas with dissolve
                mc "ohh.. okay I'm not a motherfucker then :("
                hide mc
                show cory side at mc_left with dissolve
                F1 "ya know what truce on that."
                
                show gator default with dissolve
                alligator "Anyway."
                alligator "You better run now"
                alligator "Everyone’s chasing it."
                
                hide cory
                show mc bingung2 at mc_left with dissolve
                mc "Everyone?"
                
                show gator default with dissolve
                alligator "Mhm, all creatures on water. Perhaps on land too like you are."
                alligator "Pretty thing like that doesn’t stay a secret for long"
                
                show gator annoyed with dissolve
                alligator "And once the whole water starts wanting the same thing…"
                alligator "Things get messy."
                
                show mc normal with dissolve
                mc "I’ll be careful!"
                
                show gator smile with dissolve
                alligator "Good, I’d hate to hear some little guppy got swept away."
                hide mc
                show cory proud at mc_left with dissolve
                F1 "Don’t worry gatha."
                F1 "I’ve got an eye on him."
                
                show gator annoyed with dissolve
                alligator "I don't trust you, you're bad at babysitting"
                show cory upset with dissolve
                F1 "no I'm not!"
                
                hide cory
                show mc senang at mc_left with dissolve
                mc "but Mr Cory is kind to me! I trust him!"
                
                show gator smile with dissolve
                alligator "Ha!"
                alligator "Go on then, little guppy."
                alligator "Chase your shiny thing."
                alligator "Just don’t let the river chase you back."
                alligator "and if you got lost in the way?"
                alligator "punch Cory in the face, I'll come running"
                hide mc
                show cory upset at mc_left with dissolve
                F1 "ay!"
                
                hide cory
                show mc senang at mc_left with dissolve
                mc "Okay! Thank you!"

            "Distract them":
                show mc dongok with dissolve
                mc "i uhm.. Ms.. gator why did you not follow the golden fish when it's so shiny?"
                "At the sound of my voice they both turn to me with a realizing look on their face. Distancing from one another with a firm ehem."
                
                show gator default with dissolve
                alligator "Because it was fast."
                alligator "Besides I had better things to do."
                
                show mc bingung2 with dissolve
                mc "Like what?"
                
                show gator default with dissolve
                alligator "..."
                "The alligator glanced at the rock next to it."
                alligator "Guarding this rock."
                
                show mc bingungbanget with dissolve
                mc "..."
                hide mc
                show cory unimpressed1 at mc_left with dissolve
                F1 "..."
                
                show gator annoyed with dissolve
                alligator "It’s important."
                
                hide cory
                show mc bingung2 at mc_left with dissolve
                mc "What’s so special about it."
                
                show gator default with dissolve
                alligator "It’s a rock."
                
                show mc dongok with dissolve
                mc "Oh!"
                show mc senang with dissolve
                mc "I like rocks!"
                
                show gator surprised with dissolve
                alligator "..."
                show gator smile with dissolve
                alligator "You’re alright, kid."
                
                show mc senang with dissolve
                mc "Hehe!"
                hide mc
                show cory smile at mc_left with dissolve
                F1 ".... Heh"
                
                show gator annoyed with dissolve
                alligator "..."
                alligator "Don’t give me that look."
                
                hide cory
                show mc bingung2 at mc_left with dissolve
                mc "What look?"
                
                show gator annoyed with dissolve
                alligator "The look."
                alligator "The ‘wow, the big scary alligator is lost to a fish’ look."
                
                show mc gakpuas with dissolve
                mc "I wasn’t at all thinking that!"
                hide mc
                show cory disrespectful at mc_left with dissolve
                F1 "I was sure as eel thinking that"
                
                show gator upset with dissolve
                alligator "I definitely could’ve caught it if I wanted."
                show cory unimpressed1 with dissolve
                F1 "Ya sure could."
                alligator "I COULD."
                show cory unimpressed2 with dissolve
                F1 "mhm"
                alligator "oh I CAN."
                show cory disrespectful with dissolve
                F1 "whatever you say guppy."
                "I heard a loud snap from miss Gator’s direction"
                
                show gator upset with dissolve
                alligator "Oh fine you wanna go, punk?"
                alligator "I'm getting to that fish first.."
                alligator "and eat im going to eat it right on your face"
                alligator "See how you'll like that"
                "With a face of determination and disdain Ms gator left in a hurry. The current swirling in her wake."
                
                hide gator with dissolve
                
                hide cory
                show mc bingungbanget2 at mc_left with dissolve
                mc "...."
                mc "Mr.. Cory.. alligators can actually swim up to thirty kilometers per hour"
                mc "which is.. faster than both of us combined.."
                show cory surprise hu at npc_right with dissolve
                F1 "they can WHAT."
                F1 "sweet mother of kraken.."
                show cory upset hu with dissolve
                F1 "WE SPRINTING GUPPY COME ON!"

        $ mark_fish_talked(1)
        hide mc
        hide gator
        hide cory
        with dissolve
        jump switch_character_prompt

    else:
        jump night_exploration_loop


# =========================================================
# SUB-ROUTINE: LELE INTERROGATION (MC VERSION)
# =========================================================
label lele_interrogation_mc:

    show mc normal at mc_left with dissolve
    show lele curiga at npc_right with dissolve
    mc "Do you know where the golden fish went?"
    
    show lele purapuratidur with dissolve
    lele "..."
    "It watches me with a very serious judging look."
    
    show lele depan with dissolve
    lele "😹"

    menu:
        "😹 (Gives item Ambalabu)" if shell_taken:
            "The catfish saw an opportunity and took the ambalabu from my hand."
            
            show mc dongok with dissolve
            mc "H-Hey!"
            
            show stiker gokil at stiker_lele
            show lele depan with dissolve
            lele "gokil"
            
            show mc bingung2 with dissolve
            mc "gokil…?"
            
            show stiker super_gokil at stiker_lele
            show lele default with dissolve
            lele "super mega gokil"
            
            show mc bingungbanget with dissolve
            mc "I don’t know what that means…"
            
            hide stiker with dissolve
            show lele default with dissolve
            lele "The sacred golden fish wields power enough to dry out all the water on this planet."
            lele "Yet not many would dare to pursue until the finish line"
            lele "I believe only those who remain by then are the people worthy of its blessing"
            lele "Whether they shall bring the world prosper or agony."
            lele "Repeating Fate only awaits by the hand of our God"
            lele "You should understand that better than anyone"
            
            show mc normal2 with dissolve
            mc "...Okay!"

        "What does that mean?":
            show stiker makanya_dibaca at stiker_lele
            show lele depan with dissolve
            lele "That’s why you should read more information 😂"
            
            show mc bingung with dissolve
            mc "...Ooh, okay…"
            
            show mc exited with dissolve
            mc "We were looking for the golden fish!"
            
            show stiker ya_ya_ya at stiker_lele
            show lele default with dissolve
            lele "Yes, yes, yes. I can see that. 😹"
            
            show stiker fih at stiker_lele
            lele "The fish headed north."
            
            show mc senang with dissolve
            mc "North!"
            
            show stiker waspadalah_sosok_hitam at stiker_lele
            show lele curiga with dissolve
            lele "But stay vigilant!"
            
            show stiker perlu_pencahayaan at stiker_lele
            lele "You might need to light your ways."

        "How can I even say that…":
            show lele purapuratidur with dissolve
            lele "..."
            lele "Suki…"
            
            show mc gakpuas with dissolve
            mc "...?"
            
            show lele curiga with dissolve
            lele "Suki’s Member… Member of Suki!!!"
            show stiker terdeteksi_suki at stiker_lele
            lele "Gotta be alert…"
            show stiker pergi_kau_suki at stiker_lele
            lele "Go away."
            "The catfish scares us away."

    $ mark_fish_talked(3)
    $ renpy.notify("Final Clue Added: All clues point toward the northern current.")
    hide mc
    hide lele
    hide stiker
    with dissolve
    jump switch_character_prompt


# =========================================================
# SUB-ROUTINE: LELE INTERROGATION (CORY VERSION)
# =========================================================
label lele_interrogation_cory:

    hide mc with dissolve
    show cory normal at mc_left with dissolve
    show lele default at npc_right with dissolve

    menu:
        "Which way is it pal?, i needa find out":
            show stiker mencari_tahu at stiker_lele
            show cory smile with dissolve
            F1 "which way is it pal?, i needa find out"
            
            show stiker main_sini_ke_kalimantan at stiker_lele
            show lele depan with dissolve
            lele "North Kalimantan"
            
            show stiker pembohonk_publik at stiker_lele
            show cory disrespectful with dissolve
            F1 "is what a public liar woulda say!"
            
            show stiker doksli at stiker_lele
            show cory normal with dissolve
            F1 "ay, spare me some real doksli would ya"
            
            show stiker besok_aja at stiker_lele
            show lele purapuratidur with dissolve
            lele "i’ll tell ya tomorrow"
            
            show stiker tempe_goreng at stiker_lele
            show cory smile with dissolve
            F1 "Even with tempe goreng on the line?"
            
            show stiker menggoda at stiker_lele
            show lele default with dissolve
            lele "tempting."
            
            show stiker malas at stiker_lele
            show lele purapuratidur with dissolve
            lele "but nah."
            
            show stiker awas_kamu_yah at stiker_lele
            show cory upset with dissolve
            F1 "oh you watch your back"
            
            show stiker es_teh at stiker_lele
            show cory smile with dissolve
            F1 "what about iced tea?"
            
            show stiker menggugah_selera at stiker_lele
            show lele default with dissolve
            lele "Appetizing.."
            
            show stiker pake_nasi at stiker_lele
            show cory proud with dissolve
            F1 "also with rice"
            
            show stiker pake_sambal at stiker_lele
            F1 "and spice"
            
            show stiker nah_ini at stiker_lele
            show lele depan with dissolve
            lele "that’s what i’m talking about!"
            
            show stiker cerdas at stiker_lele
            show cory smile with dissolve
            F1 "smart choice"
            
            show stiker aku_mau_sepuluh at stiker_lele
            show lele curiga with dissolve
            lele "but i want 10 of each of them"
            
            show stiker waduh at stiker_lele
            show cory surprise with dissolve
            F1 "oh shrimp"
            
            show stiker logikanya_dimana at stiker_lele
            show cory upset hu with dissolve
            F1 "where’s the logic behind that?!"
            
            show stiker apa_boleh_buat at stiker_lele
            show cory normal with dissolve
            F1 "oh well what can i do,, we have a deal"
            
            show stiker luar_biasa at stiker_lele
            show lele default with dissolve
            lele "awesome"
            
            show stiker fih at stiker_lele
            lele "The fish headed north"
            
            show stiker alhamdulillah at stiker_lele
            show cory proud with dissolve
            F1 "Alhamdulillah"

        "Gives Ambalabu" if shell_taken:
            show stiker gokil at stiker_lele
            show lele depan with dissolve
            lele "gokil"
            show stiker super_gokil at stiker_lele
            show cory smile with dissolve
            F1 "super gokil"
            lele "super mega gokil"
            show cory proud with dissolve
            F1 "super mega gokil pro max"
            
            hide stiker with dissolve
            show lele default with dissolve
            lele "The sacred golden fish wields power enough to dry out all the water on this planet."
            lele "Yet not many would dare to pursue until the finish line"
            lele "I believe only those who remain by then are the people worthy of its blessing"
            lele "Whether they shall bring the world prosper or agony."
            lele "Repeating Fate only awaits by the hand of our God"
            lele "You should understand that better than anyone"
            
            show stiker apa_makna_dari_hal_tersebut at stiker_lele
            show cory unimpressed1 with dissolve
            F1 "what does that even mean…"

        "What does that mean?":
            show stiker makanya_dibaca at stiker_lele
            show lele depan with dissolve
            lele "That’s why you should read more information 😂"
            show cory unimpressed2 with dissolve
            F1 "...Ooh, okay…"
            show cory normal with dissolve
            F1 "We were looking for the golden fish!"
            
            show stiker ya_ya_ya at stiker_lele
            show lele default with dissolve
            lele "Yes, yes, yes. I can see that. 😹"
            
            show stiker fih at stiker_lele
            lele "The fish headed north."
            show cory smile with dissolve
            F1 "North!"
            
            show stiker waspadalah_sosok_hitam at stiker_lele
            show lele curiga with dissolve
            lele "But stay vigilant!"
            
            show stiker perlu_pencahayaan at stiker_lele
            lele "You might need to light your ways."

        "How can I even say that…":
            show lele purapuratidur with dissolve
            lele "..."
            lele "Suki…"
            
            show cory unimpressed1 with dissolve
            F1 "...?"
            
            show lele curiga with dissolve
            lele "Suki’s Member… Member of Suki!!!"
            show stiker terdeteksi_suki at stiker_lele
            lele "Gotta be alert…"
            show stiker pergi_kau_suki at stiker_lele
            lele "Go away."
            "The catfish scares us away."

    $ mark_fish_talked(3)
    $ renpy.notify("Final Clue Added: All clues point toward the northern current.")
    hide cory
    hide lele
    hide stiker
    with dissolve
    jump switch_character_prompt


# =========================================================
# PROMPT GANTI KARAKTER (ROTASI EKSPLORASI)
# =========================================================
label switch_character_prompt:

    if getattr(store, "fish01_talked", False) and getattr(store, "fish03_talked", False):
        jump night_exploration_loop

    scene bg_dialog_night with fade

    show mc normal at mc_left with dissolve
    system "Pilih karakter yang akan memimpin eksplorasi berikutnya:"

    call screen rotasi_ikan_select(
        title="PILIH PEMIMPIN EKSPLORASI",
        subtitle="Pilih karakter yang akan berjalan di depan"
    )

    if _return == "mc":
        $ current_character = "MC"
        show mc senang with dissolve
        mc "Giliranku yang maju!"
        $ renpy.notify("Karakter Aktif: MC")
        hide mc with dissolve

    elif _return == "cory":
        $ current_character = "Cory"
        hide mc
        show cory proud at mc_left with dissolve
        F1 "Biar bang Cory yang urus sisanya!"
        $ renpy.notify("Karakter Aktif: Cory")
        hide cory with dissolve

    jump night_exploration_loop


# =========================================================
# TRANSISI AREA CLEAR (SELESAI MALAM) & AKHIR CHAPTER 1
# =========================================================
label area_clear_transition:

    scene bg_dialog_night with fade
    "A tiny peek of sunlight cuts through the riverwater. Tainting the murkish dark water in small dots of light that slowly stretches its reach. Soon enough the river is glowing in a calming blue"
    
    show mc exited at mc_left with dissolve
    mc "woah.. dawn in the river.."
    mc "so this is what a fish sees.."
    
    show cory smile at npc_right with dissolve
    F1 "Mhm, not so scary anymore is it?"
    
    show cory normal hu with dissolve
    F1 "And? What've we got?"
    
    show mc normal with dissolve
    mc "North!"
    
    show mc senang with dissolve
    mc "They all said north!"
    
    show cory side with dissolve
    F1 "north eh? The direction where the river ends.."
    
    show cory smile with dissolve
    F1 "...Guess we've got our answer."
    
    "I looked toward the distant current. The water there flowed faster. The sunlight barely reached it."
    
    show cory normal with dissolve
    F1 "but uhh guppy.. ain't your parents worried..?"
    F1 "it's been a full day since we got here.. ya don't wanna go back for a bit?"
    
    show mc bingung2 with dissolve
    mc "mm? No it's fine! My parents allow me to come back home whenever I want!"
    
    show mc normal with dissolve
    mc "I don't think I'm coming back before I see that fish again.."
    mc "aren't they just the kindest? To give freewill at my age!"
    
    show cory side with dissolve
    F1 "free will ay..? Sounds worrying to me."
    F1 "but you're right about one thing, guppy"
    F1 "we ain't going back until we catch that damn fish together!"
    
    show mc senang with dissolve
    mc "Let's go!"
    
    show cory fond with dissolve
    F1 "Just don’t make me save ya twice."
    
    "We begin swimming toward the northern stream. As we disappeared into the rushing water…"

    hide mc
    hide cory
    with dissolve
    
    scene black with fade
    system "--- END OF CHAPTER 1 ---"

    return