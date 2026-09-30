label start:

    jump name_input_start

    return

init python:
    _last_playing_audio = None
    def check_audio():
        playing = renpy.music.get_playing("music") or renpy.music.get_playing("sound")
        if playing != store._last_playing_audio:
            store._last_playing_audio = playing
            if playing:
                import os
                full_path = os.path.join(renpy.config.basedir, "game", playing)
                if not os.path.isfile(full_path):
                    renpy.show_screen("audio_error", missing=playing)
                else:
                    renpy.notify("Audio Debug: Playing " + str(playing))

    config.overlay_screens.append("debug_audio_tracker")

screen debug_audio_tracker():
    timer 0.25 action Function(check_audio) repeat True

screen audio_error(missing):
    modal True
    zorder 100
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        text "Audio file not found:" color "#ff0000"
        text "[missing]" color "#ff0000"
        textbutton "Dismiss" action Hide("audio_error")
    timer 0.25 action Function(check_audio) repeat True
