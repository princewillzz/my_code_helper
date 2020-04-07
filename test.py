
import os, datetime
import sys
import speech_recognition as sr 
import pyttsx3 


# Properties of the python text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# Properties of my Recognizer
r = sr.Recognizer()
r.pause_threshold = 0.5
r.energy_threshold = 100


def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
        return 0
    except:
        print("Sorry, for inconvenience")
    return 1


def wish():
    time_in_hour =int(datetime.datetime.now().hour)
    if time_in_hour > 4 and time_in_hour < 12 :
        speak("Good, Morning my love!")
    elif time_in_hour < 17 and time_in_hour > 4:
        speak("Good, Afternoon my love!")
    else :
        speak("Good evening, Love!")

def search_name(audio_message):
    words = audio_message.split(" ")
    return words[len(words)-1]



def voice_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening")
        audio = r.listen(source, timeout=6, phrase_time_limit=4)

    try:
        response = r.recognize_google(audio)
        return response
    except sr.UnknownValueError:
        print("Sorry, I was not able to understand")
    except sr.WaitTimeoutError:
        print("Time was over")
    except sr.RequestError:
        print("Can't reach the recognizer")

    return "Sorry"

if __name__ == "__main__":
    wish()
    text = voice_input()
    speak(text)
