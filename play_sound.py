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

import pygame
import time
import threading

pygame.mixer.init()

def play_file(File: str):
    print(File)
    try:
        
        pygame.mixer.music.load(filename=File)
        pygame.mixer.music.play()

        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()
    except Exception as e:
        print(f"Error: {e}")

def play(file, isQuarantine=True):
	if not isQuarantine:
		play_file(f"audios/{file}")
		return
	play_quarantine = threading.Thread(target=play_file, args=(f"audios/{file}",), daemon=True)
	play_quarantine.start()
	return

