import speech_recognition as sr 

r1 = sr.Recognizer()
r1.pause_threshold = 0.5
r1.energy_threshold = 100

with sr.Microphone() as source:
	print("listening: ")
	r1.adjust_for_ambient_noise(source, duration=1)
	print("speak")
	audio = r1.listen(source, timeout=6, phrase_time_limit=4)
	print("listended")

try:
    response = r1.recognize_google(audio)
    print(response)


except sr.UnknownValueError:
    print("Translator could not understand audio")
except sr.WaitTimeoutError:
    print("you did not speak")



