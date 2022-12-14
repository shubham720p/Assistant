
import datetime
import os
import smtplib
import webbrowser
from logging import exception

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

     
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir!")
    elif hour >=12 and hour <18:
        speak ("good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("i am you assistant , please tell me how may i help you?")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold  = 1 
        audio = r.listen(source)

    try:
        print("recognizing ...  ")
        query = r.recognize_google (audio, language= 'en-in' )
        print("user said: " + query)

    except exception as e :
        # print(e)

        print("say that again  please ...")
        return "none"
    return query
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak ("searching wikipedia ")
            query = query.replace('wikipedia',"")
            results =wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia ...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/")
        elif 'open mycamu' in query:
            webbrowser.open("https://www.mycamu.co.in/")
        elif 'open drive' in query:
            webbrowser.open("https://drive.google.com/drive/my-drive")
        elif 'open contact' in query:
            webbrowser.open("https://contacts.google.com/?hl=en&tab=oC")
        elif 'open code' in query:
            path = "C:\\Users\\Shubham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif'open git ' in query:
            path = "C:\\Users\\Shubham\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.openfile(path)
        
        
