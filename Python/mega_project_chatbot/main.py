import speechrecognition as sr

import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine=pyttsx3.init()
def speak(text):
    engine.say("I will speak this text")
if __name__=="__main__":
    speak("Hey sir how may i help you")

