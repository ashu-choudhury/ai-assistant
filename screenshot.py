import pyautogui
from PIL import Image
from play_sound import play

def screenshot():
	try:
		s=pyautogui.screenshot()
		play("screenshot.mp3")
		s.save("screenshot.png")
		file = Image.open("screenshot.png")
		return file
	except:
		return False



