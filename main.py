import speech_recognition as sr
import pyttsx3
import signal
import sys
import psutil
import time
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

class ram_info:
    def __init__(self):
        pass

    def get_size(self, bytes, suffix='B'):
        factor = 1024
        for unit in ['','K','M','G','T','P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor

    def ram_info(self):
        # Get the swap memory details (if exists)
        system = psutil.virtual_memory()
        print(f'Total :{self.get_size(system.total)} ')
        print(f'Available :{self.get_size(system.available)}')
        print(f'Used :{self.get_size(system.used)}')
        print(f'Percentage :{system.percent}%')
        swap = psutil.swap_memory()
        print('\nSwap partition:')
        print(f'Total: {self.get_size(swap.total)}')
        print(f'Free: {self.get_size(swap.free)}')
        print(f'Used: {self.get_size(swap.used)}')
        print(f'Percentage: {swap.percent}%')

# CPU class for checking CPU information
class Cpu:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_count = psutil.cpu_count()
        self.cpu_time = psutil.cpu_times()

    def print_detail(self):
        print('cpu_percent: ', self.cpu_percent)
        time.sleep(0.9)
        print('cpu_freq: ', self.cpu_freq)
        time.sleep(0.9)
        print('cpu_count: ', self.cpu_count)
        time.sleep(0.9)
        print('cpu_times: ', self.cpu_time)
        time.sleep(0.9)

signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    stt = SpeechToText()
    while True:
        text = stt.listen()
        stt.speak(text)
        if "exit" in text:
            exit(0)