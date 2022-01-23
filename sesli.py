import speech_recognition as sr 
import webbrowser
import time
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import random
import os

time.sleep(2)
os.system("cls")
r = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            print("Anlamadım")
        except sr.RequestError:
            print("Sistem Çalışmıyor")
        return voice

def response(voice):
    if 'merhaba' in voice:
         speak("merhaba")
def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.system("del "+file)

speak("Nasıl Yardımcı Olabilirim")

while True:
 voice = record()
 v = v.lower()
 print(v)
 response(v)
 
