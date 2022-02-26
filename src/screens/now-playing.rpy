init python:
    def get_playing_title(text, time):
        music_is_playing = renpy.music.is_playing(channel="music")
        if music_is_playing:
            what_music_is_playing = renpy.music.get_playing(channel="music")
            if (what_music_is_playing not in pwl_playlist):
                return Text("Играет неизвестная словарю музыка"), 0.1
            else:
                what_music_is_playing = pwl_playlist[what_music_is_playing]
                return Text("Сейчас играет:\n%s" % what_music_is_playing), 0.1
        else:
            return Text(""), 0.1
    renpy.image("pwl_gui now_playing", DynamicDisplayable(get_playing_title))
