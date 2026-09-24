# The game starts here.
label start:

    jump prologue

    return

init python:
    _last_playing_audio = None
    def check_audio():
        playing = renpy.music.get_playing("music")
        if playing != store._last_playing_audio:
            store._last_playing_audio = playing
            if playing:
                renpy.notify("Audio Debug: Playing " + str(playing))

    config.overlay_screens.append("debug_audio_tracker")

screen debug_audio_tracker():
    timer 0.25 action Function(check_audio) repeat True
