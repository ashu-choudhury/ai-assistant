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

from gettts import gettts
import pygame
import os
import time
import keyboard
import json

tts_volume=70

def load_json():
	with open("keys.json") as f:
		return json.load(f)

def speak(Text):
    """
    Converts text to speech using gTTS and plays it using pygame mixer.
    
    Args:
        Text (str): The text to convert and speak.
    """
    global tts_volume
    tts = gettts(Text)
    pygame.mixer.music.load("tts.mp3")
    pygame.mixer.music.set_volume(tts_volume / 100)  
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        if keyboard.is_pressed(load_json()["interruption"]):
            pygame.mixer.music.stop()
            break
        time.sleep(0.01)
    
    try:
        pygame.mixer.music.unload()
        os.remove("tts.mp3")
        print("File removed")
    except Exception as e:
        print(f"Error removing file: {e}")

def changeVolume(volume: int) -> dict:
    """
    Change the volume of the text-to-speech (TTS) system for your own voice.

    This function adjusts the volume level of the voice used in the TTS system, which is your own voice. 
    The volume can be set between 0 (mute) and 100 (maximum volume).

    Args:
        volume (int): The desired volume level (0-100).

    Returns:
        dict: Status message indicating whether the volume was changed successfully or an error occurred.
              Includes the current volume level.
    
    Raises:
        ValueError: If the volume is not between 0 and 100.
    """
    global tts_volume
    try:
        # Ensure volume is within valid range (0-100)
        if volume < 0 or volume > 100:
            raise ValueError("Volume must be between 0 and 100.")
        
        
        tts_volume = volume

        return {
            "status": "Volume changed successfully",
            "currentVolume": tts_volume,
            "error": False
        }
    except ValueError as ve:
        return {
            "status": "Error: Invalid volume level",
            "error": True,
            "errorMessage": str(ve)
        }
    except Exception as e:
        return {
            "status": "Error occurred while changing volume",
            "error": True,
            "errorMessage": str(e)
        }
