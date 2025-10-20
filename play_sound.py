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

