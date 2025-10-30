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

import ctypes
import subprocess
import gui
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)  # This restarts the program by executing the script again
    
    
def show_exit_dialog():
    # Define constants for the message box
    MB_YESNOCANCEL = 0x03  # Yes, No, and Cancel buttons
    MB_ICONQUESTION = 0x20  # Question icon

    # Message Box text
    message = "Do you want to exit the program? (Yes to Exit, No to Restart, Cancel to Abort)"

    # Title of the message box
    title = "Exit Program"

    # Inform the user about each button's purpose
    print("Button Instructions:")
    print("  - Yes: Exit the program")
    print("  - No: Restart the program")
    print("  - Cancel: Do nothing and continue running")

    # Call MessageBoxW from user32.dll
    result = ctypes.windll.user32.MessageBoxW(None, message, title, MB_YESNOCANCEL | MB_ICONQUESTION)

    # Return result based on the button clicked
    if result == 6:  # Yes button (Exit)
        return 0  # Exit
    elif result == 7:  # No button (Restart)
        return 1  # Restart
    elif result == 2:  # Cancel button
        return 2  # Cancel

