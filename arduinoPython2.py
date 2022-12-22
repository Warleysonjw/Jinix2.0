import serial
import threading
import time 
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
contar = 0;
for vozes in voices: # Lista de vozes
    print(contar, vozes.name)
    contar+=1

voz = 0
engine.setProperty('voice', voices[voz].id)

r = sr.Recognizer()

mic = sr.Microphone()

