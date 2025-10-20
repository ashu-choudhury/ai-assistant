import yt_dlp
import vlc

yt_c = {
    "format": "bestaudio/best",
    'outtmpl': '-',
    'quiet': True,
    'force_generic_extractor': True,
    'noplaylist': False,
    'extract_flat': False,
    'max_downloads': 5
}

def search(text):
    with yt_dlp.YoutubeDL(yt_c) as ydl:
        info = ydl.extract_info(text, download=False)

        # If it's a search result or playlist
        if 'entries' in info:
            video = info['entries'][0]
        else:
            video = info

        return {
            "title": video.get('title'),
            "url": video.get('url'),
            "provider": video.get('uploader')
        }

class Music:
    name = ""
    player = None
    musicProvider = None
    streamLink = ""

    def __init__(self, Name, Volume):
        self.name = Name
        self.volume = Volume
        self.streamLink = search(Name)
        self.name = self.streamLink['title']
        self.musicProvider = self.streamLink["provider"]
        self.player = vlc.MediaPlayer(self.streamLink["url"])
        self.player.audio_set_volume(Volume)

    def play(self):
        """Start or restart the music playback."""
        self.player.play()

    def pause(self):
        """Pause the music playback."""
        self.player.pause()

    def stop(self):
        """Stop the music playback."""
        self.player.stop()

    def resume(self):
        """Resume the music playback."""
        self.player.resume()

    def setVolume(self, volume):
        """Set the volume of the music player."""
        self.player.audio_set_volume(volume)

    def changeMusic(self, name):
        """Change the current music to a new one by name."""
        self.stop()
        self.streamLink = search(name)
        self.name = self.streamLink['title']
        self.musicProvider = self.streamLink['provider']
        self.player = vlc.MediaPlayer(self.streamLink['url'])
        self.player.audio_set_volume(self.volume)


