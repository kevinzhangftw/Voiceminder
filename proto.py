import speech_recognition
from gtts import gTTS
import os

def speak(incomingtext):
	tts = gTTS(text=incomingtext, lang='en')
	tts.save("incomingtext.mp3")
	os.system("mpg321 incomingtext.mp3")


recognizer = speech_recognition.Recognizer()
def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		return recognizer.recognize_sphinx(audio)
		# or: return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

speak("Say something!")
speak("I heard you say " + listen())