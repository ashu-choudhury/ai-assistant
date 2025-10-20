import play_sound
from gemini import AI
from stt import stt
import keyboard
import time
import threading
import gui
import json



keyboard_is_pressed_function=threading.Event()
def load_json():
	with open("keys.json") as f:
		return json.load(f)

def user_keyboard():
	while True:
		try:
			if keyboard.is_pressed(load_json()["gui"]):
				print("ctrl+shift+alt+i!")
				gui.chat_app.show_ui()
			if keyboard.is_pressed(load_json()["voice"]):
				print("ctrl+alt+v!")
				keyboard_is_pressed_function.set()
				AI()
				keyboard_is_pressed_function.clear()
			if keyboard.is_pressed(load_json()["screenshot"]):
				print("ctrl+shift+alt+x!")
				keyboard_is_pressed_function.set()
				AI(isScreenshot=True)
				keyboard_is_pressed_function.clear()
		except Exception as e:
			print(f"An error occurred: {e}")
			keyboard_is_pressed_function.clear()
		time.sleep(0.01)

def user_call():
	while True:
		if keyboard_is_pressed_function.is_set():
			continue
		if gui.chat_app.is_muted():
			break
		try:
			t=stt()
			if gui.chat_app.get_ai_name() in t.lower():
				AI()
		except Exception as e:
			print(f"An error occurred: {e}")

