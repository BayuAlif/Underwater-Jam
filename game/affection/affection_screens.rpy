screen relationship_indicator(char_aff):
    """
    A reusable screen to show a character's affection.
    
    :param char_aff: A CharacterAffection object to display.
    Example usage: `show screen relationship_indicator(eileen_affection)`
    To hide: `hide screen relationship_indicator`
    """
    zorder 100

    frame:
        xalign 0.95
        yalign 0.1
        xpadding 10
        ypadding 10
        background "#555" 

        vbox:
            spacing 5

            # Display the character's name
            text "[char_aff.name] Affection:" style "heart_label_text"

            # Display the dynamic affection bar
            bar range char_aff.max_points value char_aff.points:
                style "gui_bar"
                xysize (200, 20)

            # Display the textual representation
            text "[char_aff.points]/[char_aff.max_points]" style "heart_value_text"

style heart_label_text:
    size 14
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    xalign 0.5

style heart_value_text:
    size 12
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    xalign 0.5
