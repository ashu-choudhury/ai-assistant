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

