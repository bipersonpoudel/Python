from gtts import gTTS

import os

text=input("Enter Your Text ")

language ="en"
obj =gTTS(text=text, lang="en", slow=True)
obj.save("audio.mp3")
#os.system("start audio.mp3")

