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

import speech_recognition as sr
from play_sound import play

r = sr.Recognizer()

def stt(ai=False, audioFile=None):
	audio = None
	try:
		if audioFile:
			with sr.AudioFile(audioFile) as src:
				print(f"Opening audio file: {audioFile}")
				audio = r.record(src)
		else:
			with sr.Microphone() as src:
				print("Calibrating microphone for ambient noise...")
				r.adjust_for_ambient_noise(src, duration=0.5)
				if ai:
					play("ok.mp3")
					print("Listening now. Speak clearly.")
				audio = r.listen(src, timeout=None)
		print("Recognizing speech...")
		text = r.recognize_google(audio, language='en-IN')
		return text
	except sr.UnknownValueError:
		print("Could not understand the audio. Speak clearly.")
		return None
	except sr.RequestError as e:
		print(f"Service error: {e}")
		return None

