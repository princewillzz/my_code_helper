#!/usr/bin/env python
import os, datetime
import sys
import speech_recognition as sr 
import pyttsx3 
import wikipedia, PyPDF2
import webbrowser


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

# This functions deals with the speaking functionality of the program 
def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
        return 0
    except:
        print("Sorry, for inconvenience")
    return 1

# Just a cute greeting code
def wish():
    time_in_hour = int(datetime.datetime.now().hour)
    if time_in_hour > 4 and time_in_hour < 12 :
        speak("Good, Morning my loven !!")
    elif time_in_hour < 17 and time_in_hour > 4:
        speak("Good, Afternoon! my love !!")
    else :
        speak("Good evening Love !!")

# Returns the name of the file that I want to create
def search_name(audio_message):
    speak("what should be the Name of the file")
    name = ""
    text = voice_input()
    while text == None:
        speak("Sorry, Can you please repeat")
        text = voice_input()
    name += text
    speak("What is the code of the quesion")
    text = voice_input()
    while text == None:
        speak("Sorry, Can you please repeat")
        text = voice_input()
    name += text
    speak("What Level is the question ?")
    level = voice_input()
    if level == None:
        level = 'A'
    else :
        level = level.split(" ")
        word = ""
        for ele in level:
            if len(ele) == 1:
                word = ele
                break
        name += word.upper()

    return name


# It is responsible for all the input using voice and return it in text format
def voice_input():
    # Using Microphone as the source
    with sr.Microphone() as source:
        # Adjusting the audio from the source to deal with the ambiance
        r.adjust_for_ambient_noise(source, duration=1)
        #print("Listening")
        audio = r.listen(source)

    try:
        # Using google to recognize the audio and convert it into text
        # Language set to india performs much better
        response = r.recognize_google(audio, language="en-in")
        response = response.replace("bulbul", "")
        response = response.replace("bullbull", "")
        return response
    except sr.UnknownValueError: # if it cannot be recognized
        speak("Sorry, I was not able to understand")
        print("Sorry, I was not able to understand")
    except sr.WaitTimeoutError: # IF the wait time before the you speak exceeds
        print("Time was over")
        speak("Time was over")
    except sr.RequestError: # If google does not reply due to over-use or internet connection problem
        print("Can't reach the recognizer")
        speak("Can't reach the recognizer")

    return None

def notes():
    print("Starting to Put down some notes!.... You can speak now")
    speak("Starting to Put down some notes!.... You can speak now")
    print("Listening")
    while True:
        note = voice_input()
        if note != None and "quit" in note:
            speak("Notes done!. Bye")
            return
        if note != None or note != "":
            print(note)


# The driver code
def main():
    while True:
        print("Listening")
        command = voice_input()
        if command == None: 
            continue
        speak(command)
        command = command.lower()

        if "note" in command or "record" in command:
            print("Starting to Put down some notes!.... You can speak now")
            speak("Starting to Put down some notes!.... You can speak now")
            print("Listening")
            notes()


        if "open" in command or "view" in command or "pdf" in command:
            command = command.replace("view", "")
            command = command.replace("open", "")
            command = command.replace("pdf", "")
            command = command.strip("")
            
            list_of_files = os.listdir()
            files = command.split()
            flag = 0
            for fil in files:
                pdf_name = fil + ".pdf"
                if pdf_name in list_of_files:
                    pdfFile = open(pdf_name, 'rb')
                    pdfReader = PyPDF2.PdfFileReader(pdfFile)
                    num_of_pages = pdfReader.numPages
                    for i in range(num_of_pages):
                        page = pdfReader.getPage(i).extractText()
                        page = page.replace("\n", "")
                        speak(page)
                        if i == num_of_pages-1:
                            flag = 1
                            break
                        speak("Do you want me to read another page, sir?")
                        com = voice_input()
                        if "yeah" in com or "yes" in com:
                            flag = 1
                            break
                if flag == 1:
                    break

        elif "clean" in command:
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
                speak("Sorry! I destroyed the file.")
                continue
            elif "yes" in decide:
                speak(f"Ok! {name_of_file} is created. ")
                if "." not in name_of_file:
                    name_of_file += ".java"
                writeContent(name_of_file)
            else:
                speak("Ok! The file is destroyed")
            speak("Do you want to open the file: ")
            cmnd = voice_input()
            if cmnd != None and ("yes" in cmnd or "yeah" in cmnd):
                os.system("code .")
            else:
                speak("Okay")


        elif "exit" in command:
            speak("Good Night my love!!!")
            return
        elif "wikipedia" in command or "pedia" in command or "wiki" in command:
            speak("Searching wikipedia")
            command = command.replace("wikipedia", "")
            res = wikipedia.summary(command)
            speak("According to wiki..")
            print(res)
            speak(res)
        elif "youtube" in command or "you" in command or "tube" in command:
            command = command.replace("youtube", "")
            command = command.replace("you", "")
            command = command.replace("tube", "")
            query = "http://www.youtube.com/results?search_query="
            command = command.split()
            for comm in command:
                query += comm
                query += '+'
            print(query)
            webbrowser.open(query)
        elif "search" in command or "google" in command:
            command = command.replace("google", "")
            command = command.replace("search", "")
            query = "https://www.google.com/search?q="
            command = command.split()
            for comm in command:
                query += comm
                query += '+'
            print(query)
            webbrowser.open(query)
        else:
            print("repeating")



# Properties of the python text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # Getting all the voices present in the system
engine.setProperty('voice', voices[1].id) # Setting it to zira
engine.setProperty('rate', 140) # setting the rate property

# Properties of my Recognizer
r = sr.Recognizer() 
r.pause_threshold = 0.8 # Setting the maximum pause allowed between the sentence
r.energy_threshold = 100 # Setting the threshold above which the recognizer listen
r.dynamic_energy_threshold = True

if __name__ == "__main__":
    wish()
    if sys.argv[1] != None:
        print(sys.argv[1])
        notes()
    else :
        main()