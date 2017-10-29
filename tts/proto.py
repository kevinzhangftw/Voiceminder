from gtts import gTTS
import os
tts = gTTS(text='June is gay ass, Camvy films wifi password is homophobia. ha', lang='en')
tts.save("bad.mp3")
os.system("mpg321 bad.mp3")