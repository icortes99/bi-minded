import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import playsound
import os
import config

def listen_to_user():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Te escucho...")
    try:
      audio = recognizer.listen(source, timeout = 5)
      text = recognizer.recognize_google(audio, language="en-US") # en-US - es-ES
      return text
    except sr.UnknownValueError:
      return "Lo siento, no entendí eso."
    except sr.RequestError:
      return "Error en la conexión al servicio de reconocimiento de voz."

def speak_to_user(text, language = config.DEFAULT_TARGET_LANGUAGE):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id) # 0 hombre, 1 mujer. Ambos en ingles
  engine.say(text)
  engine.runAndWait()
