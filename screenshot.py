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



