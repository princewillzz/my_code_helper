import pyttsx3 

class Speaker:
    # Properties of the python text to speech engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    def speak(self, audio):
        try:
            self.engine.say(audio)
            self.engine.runAndWait()
        except:
            print("Sorry, for inconvenience")

