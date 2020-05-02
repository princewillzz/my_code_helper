import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices[1].age = 5
print(voices[1].age, voices[1].gender)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)


engine.say('The pdf has been fully read')
engine.runAndWait()