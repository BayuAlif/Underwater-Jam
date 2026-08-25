# =========================================================
# UI MAP EKSPLORASI MALAM (ITEM & NPC)
# =========================================================

screen screen_item_npc():

    zorder 10

    # 1. BUAYA (TENGAH ATAS)
    if not fish01_talked:
        imagebutton:
            idle "images/npc/aligator_idle.png"      
            hover "images/npc/aligator_hover.png"   
            xpos 810 ypos 260                 
            focus_mask True  
            at Transform(zoom=0.75)
            action Return("talk_croc")

    # 2. LELE (KIRI BAWAH)
    if not fish03_talked:
        imagebutton:
            idle "images/npc/catfish_idle.png"      
            hover "images/npc/catfish_hover.png"    
            xpos 225 ypos 300           
            focus_mask True 
            at Transform(zoom=0.75)
            action Return("talk_fish03")

    # 3. AMBALABU (ITEM DI KANAN BAWAH)
    if not shell_taken:
        imagebutton:
            idle "images/npc/ambalabu_idle.png"     
            hover "images/npc/ambalabu_hover.png"    
            xpos 810 ypos 675          
            focus_mask True
            at Transform(zoom=0.75)
            action [
                SetVariable("shell_taken", True),
                Function(add_item, "Ambalabu"),
                Notify("Kamu mendapatkan Ambalabu!"),
                Return("item_taken")
            ]