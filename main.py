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

r = sr.Recognizer()
mic = sr.Microphone()

@eel.expose
def process_user_input(user_input_name, user_lang_select):
    global userName
    global userLang
    userName = user_input_name
    userLang = user_lang_select
    print(f"User input name: {user_input_name}")
    print(f"User language selection: {user_lang_select}")
    
@eel.expose
def app_init():
    eel.init('web') #
    eel.start('login.html',size = (800,600)) 

if __name__ ==  '__main__':
    app_init()