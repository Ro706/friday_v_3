import speech_recognition as sr
import pyttsx3
import signal
import sys
class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)
        self.engine.setProperty('voice', 'english')
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio)
                print("You said: " + text)
                return text
            except:
                print("Sorry, I did not get that.")
                return ""
            
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
def signal_handler(sig, frame):
    print("Exiting Program")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    stt = SpeechToText()
    while True:
        text = stt.listen()
        stt.speak(text)