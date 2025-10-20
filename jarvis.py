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
