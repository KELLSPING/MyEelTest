from tkinter import *
from datetime import *
import threading
import tkinter
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
import os
import speech_recognition as sr
import time
from googletrans import Translator
from tkinter import ttk
from gtts import gTTS
from pygame import mixer
import tempfile
# generate WAV
import pyaudio
import wave
#image
import base64
import eel
import json
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

userName = ""
userLang = ""

port = random.randint(5000,65535)

r = sr.Recognizer()
mic = sr.Microphone()

j_str = {"type": "service_account",
  "project_id": "pythonfirebase-6b43c",
  "private_key_id": "d0eedb26e201720f1f24fd9487fb369265da6ca8",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCz1IqYXM4TGam8\n/NPsUbatzupN2UId//4u9pb9Cm5ljCUFCf1IlHA3e4hHFwpuCOn3iqlVnbJhw0q+\nornJuW8eOvE+bpaXS6Rplym3en84N4E/Phwb8vcda/H3naaoHTM0S/BkusX0SuMe\ngVzCcuXIqz6Oa6t67t97bck/pwkPYMofX6Oo8yNCUszCkDwVewoG86iJqIrlwbfh\n2qL7kbHfa2C87mt9/PorB9RprBsrXqNVGp9n07Csy0E6Hlu6dnm/F9JWSTYWB3xF\nmJmOKcXpYWCf5Tfel/H/VkGoL4znloDixgNoko00WV3i83ubq8qOa/JGdiTycYGX\nQgOfn7cNAgMBAAECgf8Z45b1bJzSiCzChQ9OQ8YnONv1AZjXYTyRtW5sVwoAL4EX\nZGmchfgbEjEdM1kGTy4BaxoJ+VyCbHYPiVcGxGt0ITddQjbr2zf1THLnjtKtraDP\nfWGVU6U5Gn0IwH26URuKq91YUjpqD13tRlrUUsp32TzhjiweaEwOTShQ94HnPrlU\nCglPtvmhbOdyx1ZsfAl+1q3mc9e6S29lGehCXrcm/hzO3ZMW2/5zD/UWH1DksWCV\n2dyXGbZOi04//OMMwj56M25v8p1FYT8kCLmjYiZnB4V9wYJ7yCMU9GIgZKPeHMDk\nRrRv17Vhbqnpvw2C6W9wmpvdV2tNUanO0DDGBQECgYEA2mEs2hWvXPhEpWCYhoOu\nP0oYrO0vcgv8B0SP7LIBEAbHx17IC3Tyzemgfw6QWIwa/zFlBlv1/MaMD+eiOHXW\nJCfsmfNLypEvtkUJdi22jLJ1QEynOKHfNgSQquvY0n9GjRdH/vsHw/SSxquER/GP\nvoHiblSanJGYgDT/9M4vNg0CgYEA0s9KHpsd9Q/Lvg63TLQHjqWXJC1s5j65f/RS\nkz8jrmU5HHFncRMYZp1SmAwLtnL3jEWVy1tHLOl+TBGoPspsZAk/abHKViqs4KNN\n/Ye6Py4ujSA8b9Gu2UJt6G2lZVWmk7W3eX0GKn9qJ9+t9C6yToS5byRhAqyyfomh\nNlabRQECgYEAiq8z4LvsxkoUrkIOGz79JcxUp11pyC+8OpFcJaFV82ua7A5RVJVM\nrWA1QPtqyBESBAbGdadpLMKaqG8eImUTPZrtM0fDVj2l40csnxSg3fFnbRJBEEIc\nkx2LEkD9TZDuqSOj4VZitBtaKzk5pMbP1th9iDvKhKwiASmnczyN1vECgYAJ7gew\nv1++3lqbfjf2HfjJKFWhN56MjeHQ/CIzm2LD4TK6e0EDG4InuztbvB2FH483hUOU\nC52jqO/xB1fkdUZ7w8+/28cLHgF8p1SSH6WPOk6pCR6vqbHRvAZPT3Ld/hXVmVam\nG1SCBfRrImcgPF7bwfa2HIGRTa8utK7qT1QLAQKBgQC3dDf6lwDAXquXT/1PLm8r\nhy4urSMuPVN74vpntiTUvy0OOVOW2bMyP38l00hqwkjE7ifGoV2g17HbmsNj44Xc\nrVL5gxj8E3BHcO272ExxgcdmaiJ3l7TqmyekIrSFEIEKIIivAHc92dDxs0o2fjvb\n5+u18iN+tiMt/5qLAaVTBA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-k2nly@pythonfirebase-6b43c.iam.gserviceaccount.com",
  "client_id": "101784948027192725809",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-k2nly%40pythonfirebase-6b43c.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com" 
}
with open("./key.json","w") as f:
    json.dump(j_str,f)
 
cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


class Recorder:
    def __init__(self, chunk=1024, channels=1, rate=16000):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []

    def start(self):
        threading._start_new_thread(self.__recording, ())

    def __recording(self):
        self._running = True
        self._frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        while self._running:
            data = stream.read(self.CHUNK)
            self._frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def stop(self):
        self._running = False

    def save(self):

        p = pyaudio.PyAudio()

        wf = wave.open("tmp.wav", 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()


@eel.expose
def process_user_input(user_input_name, user_lang_select):
    global userName
    global userLang
    userName = user_input_name
    userLang = user_lang_select
    print(f"User input name: {user_input_name}")
    print(f"User language selection: {user_lang_select}")
    
    
@eel.expose
def get_message(message):
    global userName, userLang
    tempMsg = message

    if (tempMsg == 'sudo_clean_all_users'):
        print("sudo_clean_all_users")
        lst_id=[i.id for i in db.collection('chatroom').get()]
        for i in lst_id:
            if i!=userName:
                db.collection('chatroom').document(i).delete()
        
    else:
        loc_dt = datetime.today()
        f_loc_dt = loc_dt.strftime("%Y:%m:%d %H:%M:%S")
        print("[" + f_loc_dt + "] " + userName + " : " + message)
        student1 = db.collection('chatroom').document(userName)
        student1.set({
            'message': tempMsg,
            'time':loc_dt.strftime("%Y:%m:%d:%H:%M:%S")
        })
        eel.update('[' + f_loc_dt + ']' + ' ' + userName + ' : ' + message)
        
def recordtext():
    global r,mic
    with sr.WavFile("tmp.wav") as source:    #read WAV files
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        try:
            text = r.recognize_google(audio,language = userLang)
            print(text)
            return text
        except :
            print ("Could not understand audio")

re = Recorder()

@eel.expose
def on_press():
    global re
    print("Record button pressed")
    re.start()

@eel.expose
def on_release():
    global re
    print("Record button released")
    re.stop()
    re.save()
    t=recordtext()
    eel.showText(t)



@eel.expose
def app_init():
    global port
    eel.init('web')
    eel.start('login.html', size=(800,600), port=port, mode='chrome-app')

if __name__ ==  '__main__':
    app_init()