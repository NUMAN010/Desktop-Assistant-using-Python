import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia
import webbrowser 
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

engine.setProperty('voice', voices[0].id)  # Male voice
engine.setProperty('rate', rate - 10)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.now().hour
    if hour >= 0 and hour < 12:
        msg = 'Good Morning Sir. Jarvis here, how can I help you?'
    elif hour >= 12 and hour < 18:
        msg = 'Good Afternoon Sir. Jarvis here, how can I help you?'
    else:
        msg = 'Good Evening Sir. Jarvis here, how can I help you?'
    
    print(msg)
    speak(msg)

def takeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 2
            audio = r.listen(source)

        try:
            print('Recognizing...')
            q = r.recognize_google(audio, language='en-in')
            return q
        except Exception as e:
            print('Unable to recognize, say again please.')

if __name__ == "__main__":
    wish_me()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia,')
            print(result)
            speak(result)
            speak('Is there anything more that I can help you with, sir?')

        elif 'youtube' in query:
            speak('Opening YouTube.')
            webbrowser.open('https://www.youtube.com')
            speak('Is there anything more that I can help you with, sir?')

        elif 'google' in query:
            speak('Opening Google.')
            webbrowser.open('https://www.google.com')
            speak('Is there anything more that I can help you with, sir?')

        elif 'instagram' in query:
            speak('Opening Instagram.')
            webbrowser.open('https://www.instagram.com')
            speak('Is there anything more that I can help you with, sir?')

        elif 'facebook' in query:
            speak('Opening Facebook.')
            webbrowser.open('https://www.facebook.com')
            speak('Is there anything more that I can help you with, sir?')

        elif 'time' in query:
            cur_time = datetime.now().strftime('%I:%M %p, %d %B %Y, %A')
            print(f'The current time is: {cur_time}')
            speak(f'Sir, the current time is {cur_time}.')
            speak('Is there anything more that I can help you with, sir?')
            time.sleep(1)

        elif any(word in query for word in ['goodbye', 'no', 'nothing', 'bye']):
            speak('Okay sir. I am always here for you. Bye bye.')
            break

        else:
            speak('Sorry sir, I don’t have that information. What else can I help you with?')