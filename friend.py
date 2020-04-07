
import os, datetime
import sys
import speech_recognition as sr 
import pyttsx3 



# Compile and Run the program given as the input 
def doit():
    # Access the file name to be executed
    f = open("D:\projects\my_code_helper/run.txt")
    content = f.readline()

    # Return if there exists no files stored in the "run.txt" file to be executed
    if content == "":
        return
    try:
        if os.system("javac " + content) == 1:
            return
        cont = content.split(".")
        os.system("java " + cont[0])

    except:
        print("except")
        f.close()
        return 

    f.close()


# Remove the ".class" type file created after the execution of the program 
def remove_unwanted():
    files = os.listdir()
    to_be_delete = list()
    # Store all the files to be deleted
    for file in files:
        splited_file = file.split(".")
        if splited_file[len(splited_file)-1] == "class":
            to_be_delete.append(file)
    # remove all the files that are stored 
    for file in to_be_delete:
        os.remove(file)


# Write the contents from "forjava.txt" to the "name_of_file" file
def writeContent(name_of_file):
    # Write the name of the file in run.txt to compile and run the program later
    f = open("D:\projects\my_code_helper/run.txt", "w")
    f.write(name_of_file)
    f.close()

    # Check if the file already exist then just compile and run the program
    if os.path.exists(name_of_file):
        doit()
        return
    # if the file is not present create a new file with the name given as input
    f2 = open(name_of_file, "w+") 
    f1 = open("D:\projects\my_code_helper/forjava.txt")
    
    # Do the actual stuff of wrting the pre-set code into the new file
    for content in f1:
        # To replace the class name from "forjava" --> name_of_file.java
        if "forjava" in content:
            name_of_file = name_of_file.split(".")
            cont = content.replace("forjava", name_of_file[0])
            f2.write(cont)
        else:
            f2.write(content)

    f1.close()
    f2.close()

# Integrating it with git VC
def git_add(message):
    remove_unwanted()
    os.system("git add .")
    os.system("git commit -m " + "\"" + message + "\"")
    os.system("git push")


def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
        return 0
    except:
        print("Sorry, for inconvenience")
    return 1


def wish():
    time_in_hour = int(datetime.datetime.now().hour)
    if time_in_hour > 4 and time_in_hour < 12 :
        speak("Good, Morning my loven !!")
    elif time_in_hour < 17 and time_in_hour > 4:
        speak("Good, Afternoon! my love !!")
    else :
        speak("Good evening Love !!")

def search_name(audio_message):
    words = audio_message.split(" ")
    return words[len(words)-1]



def voice_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening")
        audio = r.listen(source)

    try:
        response = r.recognize_google(audio)
        return response
    except sr.UnknownValueError:
        speak("Sorry, I was not able to understand")
        print("Sorry, I was not able to understand")
    except sr.WaitTimeoutError:
        print("Time was over")
        speak("Time was over")
    except sr.RequestError:
        print("Can't reach the recognizer")
        speak("Can't reach the recognizer")

    return None



def main():
    while True:
        command = voice_input()
        if command == None: 
            continue
        speak(command)
        command = command.lower()
        if "clean" in command:
            remove_unwanted()
        elif "run" in command:
            doit()
        elif "commit" in command:
            try:
                message = input("Message:- ")
                if message.strip() == "":
                    print("cannot commit without message:)")
                    return
                git_add(message)
            except:
                return
        elif "create" in command:
            name_of_file = search_name(command)
            speak("Are you sure to create the file with this name: " + name_of_file)
            decide = voice_input()
            if decide == None:
                continue
            elif "yes" in decide:
                name_of_file += ".java"
                writeContent(name_of_file)
            else:
                speak("Ok! The file is destroyed")

        elif "exit" in command:
            speak("Good Night my love!!!")
            return
        else:
            print("repeating")



# Properties of the python text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)

# Properties of my Recognizer
r = sr.Recognizer()
r.pause_threshold = 0.8
r.energy_threshold = 100



wish()
main()