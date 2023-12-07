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

@eel.expose
def app_start():   
    eel.init('web') #
    eel.start('login.html',size = (800,600))

if __name__ ==  '__main__':
    app_start()