import pyttsx3
import datetime
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib
import wolframalpha

engine = pyttsx3.init()

MASTER = "bilal"

client = wolframalpha.Client('Your api key here')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def retry():
    com = ['Any thing else sir','waiting for next command']
    retry = random.choice(com)
    speak(retry)

def hour():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<24:
        speak("good Evening sir")
    else:
        speak("good night sir")

def wishme():
    speak("Initializing jarvis")
    speak("starting assistivity")
    speak("preparing things ready")
    speak("I am back and Online")
    hour()
    speak("Welcome back!")
    point = ['How are you sir' , 'wish you a nice day sir']
    poi = random.choice(point)
    speak(poi)
    speak("How can i help you?")

wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)


    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        
        return None
    return query

if __name__ == '__main__':

    while True:
        query = takeCommand()
        query = query.lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
                webbrowser.open(www.youtube.com)

        elif 'open google' in query:
                webbrowser.open(www.google.com)

        elif 'open facebook' in query:
                webbrowser.open(www.facebook.com)

        elif 'open gmail' in query:
                webbrowser.open(mail.google.com)

        elif 'time' in query:
            speak('time is')
            time()

        elif 'date' in query:
            speak('today is')
            date()

        elif 'play music' in query:
            songs_dir = "C:\\Users\\Admin\\Music\\songs"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'hello' in query or 'hello jarvis' in query:
            rep = ['hello sir','hi sir','hi there']
            reply = random.choice(rep)
            speak(reply)

        elif 'how are you' in query or 'are you all right' in query:
            repy = ['i am fine','i am alright']
            replya = random.choice(repy)
            speak(replya)
            speak('thank you for asking')

        elif 'take a rest ' in query or 'shut down ' in query or 'see you later' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        elif 'open whatsapp' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codepath)
            
        elif 'jarvis status report' in query:
            speak('I am working well')
            speak('no error repot or crashes in my system , sir')

        elif 'open whatsapp' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codepath)

        elif 'open text box' in query:
                speak('here you go')
                query = str(input('Command: '))

        else:
            query = query
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('Got it.')
                speak('WOLFRAM-ALPHA says - ')
                speak(results)

            except:
                speak('Do you want to search it in google , sir')
                Answer = mycommand()
                if 'yes' in Answer:
                    try:
                         speak('here you go')
                         webbrowser.open('www.google.com')

                    except:
                        speak('OK,sir')

    retry()

