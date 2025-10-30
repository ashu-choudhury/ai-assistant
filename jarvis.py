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

import threading
from play_sound import play
import sys
import gui
from user_call import  user_call, user_keyboard, load_json
import keyboard
import exit

def exitAi():
	user_input = exit.show_exit_dialog()
	if user_input == 0:
		gui.app.ExitMainLoop()
	elif user_input == 1:
		play("shutdown.mp3", isQuarantine=False)
		exit.restart_program()
	elif user_input == 2:
		# Do nothing
		pass
	else:
		pass

call_thread=threading.Thread(target=user_call, daemon=True)
keyboard_thread=threading.Thread(target=user_keyboard, daemon=True)

keyboard.add_hotkey(load_json()["quit"], exitAi)

call_thread.start()
keyboard_thread.start()

play("startup.mp3")
gui.app.MainLoop()
print("!!")
play("shutdown.mp3", isQuarantine=False)
