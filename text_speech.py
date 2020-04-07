import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices[1].age = 5
print(voices[1].age, voices[1].gender)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)


engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()