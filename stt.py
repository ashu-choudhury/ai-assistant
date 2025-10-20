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

