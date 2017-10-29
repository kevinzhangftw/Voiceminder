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
		audio = recognizer.listen(source, timeout=500, phrase_time_limit=3000)

	try:
		# print(recognizer.recognize_sphinx(audio))
		# return recognizer.recognize_sphinx(audio)
		print(recognizer.recognize_google(audio))
		return recognizer.recognize_google(audio)
		# for testing purposes, we're just using the default API key
    	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    	# instead of `r.recognize_google(audio)`
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

speak("Say something!")
print("Aigent said something")
# speak("I heard you say " + listen())
speak(listen())