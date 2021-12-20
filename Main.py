import pyttsx3
import speech_recognition as sr
import random
import wikipedia
import os
import time
import datetime
import webbrowser
import jokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")


def Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:

        query = r.recognize_google(audio, language='en-in')
        print(f"User said:" + query)
        loop = 1
        return loop
        return query


    except Exception as e:
        print(e)
        loop = 0
        print("X")
        return loop



while True:
        print("Say something")
        query = Takecommand()

        if 'search wikipedia for' in query:
            wiki = ["searching", "looking for it", "okay"]
            speak(random.choice(wiki))
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=4)
            result = ["according to my knowledge", "according to Wiki", "according to wikipedia"]
            speak(random.choice(result))
            print(results)
            speak(results)

        elif 'hello' in query:
            hi = ["hello there", "hey there", "How are you", "Greetings"]
            speak(random.choice(hi))

        elif 'hi' in query:
            hi = ["hello there", "hey there", "How are you", "Greetings"]
            speak(random.choice(hi))

        elif 'search youtube for' in query:
            youtube = ["searching", "looking for it", "okay"]
            speak(random.choice(youtube))
            query = query.replace("search in youtube", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'search google for' in query:
            wiki = ["searching", "looking for it", "okay"]
            speak(random.choice(wiki))
            query = query.replace("search google for", "")
            webbrowser.open("https://www.google.com/search?q=" + query)
            speak("Done")

        elif 'open drop box' in query:
            webbrowser.open("https://www.dropbox.com/home")
            speak("Done")
            os.startfile(query)

        elif 'tell me a joke' in query:
            speak("Ok let me find a good one")
            time.sleep(1)
            speak("ok here we go")
            speak(jokes.Joke)
            time.sleep(0.5)
            speak("Ok sorry")


        elif 'shut up' in query:
            engine.setProperty('rate', 100)
            reply = ["ok rude", "ok", "sorry", "understandable"]
            Reply = random.choice(reply)
            speak(Reply)

        else:
            error = ["sorry cant understand that", "sorry", "sorry cant do that right now"]
            speak(random.choice(error))







