# Copyright 2025 Ashu Choudhury
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import music
import random

mp = None

def playMusic(musicName: str = None, musicVolume: float = 50) -> dict:
    """
    Plays the given media on the user's speakers.

    This function expects a direct link to the media you want to play.
    You must use the media search tool (such as `searchYoutube`) to find and select the appropriate media first.
    Once you have the media link, pass it to this function to start playback.

    If another track is currently playing, it will be stopped automatically before starting the new one.

    Args:
        musicName (str): The direct media link to play (must be from a trusted source).
        musicVolume (float, optional): The playback volume level (0–100). Defaults to 50.

    Returns:
        dict: A dictionary containing information about the media being played, or an error if playback fails.
    """
    global mp
    try:
        # Ensure volume is an integer
        musicVolume = int(musicVolume)

        # Stop currently playing music, if any
        if mp:
            mp.stop()

        # Initialize and play new music
        if not musicName:
            # Randomly select a song if no name is provided
            musicName = random.choice(["song1", "song2", "song3", "famous90ssong"])

        mp = music.Music(musicName, musicVolume)
        mp.play()
        return {
            "status": "Music is playing",
            "musicName": mp.name,
            "musicProvider": mp.musicProvider,
            "currentVolume": mp.volume,
            "error": False
        }
    except Exception as e:
        return {
            "status": "Error occurred while trying to play music",
            "error": True,
            "errorMessage": str(e)
        }

def stopMusic() -> dict:
    """
    Stop the currently playing music.
    Returns:
        dict: Status indicating whether music has been stopped or an error occurred.
    """
    global mp
    try:
        if mp:
            mp.stop()
            return {
                "status": "Music has been stopped",
                "musicName": mp.name,
                "error": False
            }
        else:
            return {
                "status": "No music is currently playing",
                "error": True
            }
    except Exception as e:
        return {
            "status": "Error occurred while trying to stop music",
            "error": True,
            "errorMessage": str(e)
        }

def pauseMusic() -> dict:
    """
    Pause the currently playing music.
    Returns:
        dict: Status indicating whether music has been paused or an error occurred.
    """
    global mp
    try:
        if mp:
            mp.pause()
            return {
                "status": "Music has been paused",
                "musicName": mp.name,
                "error": False
            }
        else:
            return {
                "status": "No music is currently playing",
                "error": True
            }
    except Exception as e:
        return {
            "status": "Error occurred while trying to pause music",
            "error": True,
            "errorMessage": str(e)
        }

def setMusicVolume(volume: float) -> dict:
    """
    Adjust the volume of the currently playing music.
    Args:
        volume (float): The desired volume level (0-100).
    Returns:
        dict: Status and current volume level, or an error message if adjustment fails.
    """
    global mp
    try:
        if mp:
            volume = int(volume)  # Ensure volume is an integer
            mp.setVolume(volume)
            return {
                "status": "Volume has been set",
                "currentVolume": volume,
                "error": False
            }
        else:
            return {
                "status": "No music is currently playing",
                "error": True
            }
    except Exception as e:
        return {
            "status": "Error occurred while trying to set volume",
            "error": True,
            "errorMessage": str(e)
        }

def changeMusic(musicName: str) -> dict:
    """
    Change the currently playing music to a new song.
    Args:
        musicName (str): The name of the new music to play.
    Returns:
        dict: Information about the new music being played or an error message if change fails.
    """
    global mp
    try:
        if mp:
            mp.changeMusic(musicName)
            mp.play()
            return {
                "status": "Music has been changed",
                "musicName": mp.name,
                "musicProvider": mp.musicProvider,
                "error": False
            }
        else:
            return {
                "status": "No music is currently playing to change",
                "error": True
            }
    except Exception as e:
        return {
            "status": "Error occurred while trying to change music",
            "error": True,
            "errorMessage": str(e)
        }

def resumeMusic() -> dict:
    """
    Resume the currently paused music.
    Returns:
        dict: Status indicating whether music has been resumed or an error occurred.
    """
    global mp
    try:
        if mp:
            mp.play()
            return {
                "status": "Music has been resumed",
                "musicName": mp.name,
                "error": False
            }
        else:
            return {
                "status": "No music is currently paused to resume",
                "error": True
            }
    except Exception as e:
        return {
            "status": "Error occurred while trying to resume music",
            "error": True,
            "errorMessage": str(e)
        }
