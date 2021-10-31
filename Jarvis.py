import pyttsx3 #pip install di terminal
import speech_recognition as sr #install ini speechReconition
import datetime
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia.exceptions import HTTPTimeoutError

print ("initializing JARVIS")

MASTER = "Daniel"

engine = pyttsx3.init("sapi5")
Voices = engine.getProperty("voices")
engine.setProperty("voice", Voices[0].id)

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >- 12 and hour < 18:
        speak("Good afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")

    except Exception as e:
        print("Sorry can you say that again?")
        query - None

    return query    


 #main start here
speak ("Hello Daniel, im Jarvis, can i help you?")
wishMe()
query = takeCommand()

#logic for tasks as per query
if "wikipedia" in query.lower90:
    speak("searching wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)