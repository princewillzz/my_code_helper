#!/usr/bin/env python
import os
import sys
import PyPDF2, wikipedia, webbrowser
import time
import pyttsx3 


# Properties of the python text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)

def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except:
        print("Sorry, for inconvenience")


def read_pdf_help(pdf_name):
    try:
        startPage = int(sys.argv[3]) - 1
    except:
        startPage = 0

    pdfFile = open(pdf_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    try:
        for i in range(startPage, pdfReader.numPages):
            page = pdfReader.getPage(i).extractText()
            print(page)
            page = page.replace("\n", "")
            speak(page)
            speak("Do you want to read more(y/n):- ")
            choice = input("Do you want to read more(y/n):- ").strip()
            if "y" in choice or "Y" in choice:
                continue
            else:
                return
        speak("The pdf has been fully read")
    except:
        speak("The page number cannot be found by me sorry")

def read_pdf(pdf_name):
    try:
        os.system(f'start cmd /c "friend.py speak_pdf {pdf_name} {sys.argv[2]} "')
    except:
        os.system(f'start cmd /c "friend.py speak_pdf {pdf_name} "')



# list of all the files and folder in this directory
list_of_files_in_current_directory = os.listdir()

# Access the file name to be executed
f = open("D:\projects\my_code_helper/run.txt")
java_file_to_be_run = f.readline()
f.close()


# Compile and Run the program given as the input 
def run_java():
    # Return if there exists no files stored in the "run.txt" file to be executed
    if java_file_to_be_run == "":
        return
    try:
        if os.system("javac " + java_file_to_be_run) == 1:
            return
        cont = java_file_to_be_run.split(".")
        os.system("java " + cont[0])
    except:
        print("except")

def run_c(file_name):
    try:
        if os.system("gcc " + file_name) == 1:
            return
        cmmd = "a.exe"
        os.system(cmmd)
        remove_unwanted(cmmd)
    except:
        print("Something is wrong")


# Remove the ".class" type file created after the execution of the program 
def remove_unwanted(instruction=None):
    if not instruction == None:
        os.remove(instruction)
    else:
        for file in list_of_files_in_current_directory:
            if ".class" in file:
                os.remove(file)


# Write the contents from "forjava.txt" to the "name_of_file" file
def Create_or_run_java_file(name_of_file):
    
    # Check if the file already exist then just compile and run the program
    if os.path.exists(name_of_file):
        run_java()
        return

    # Write the name of the file in run.txt to compile and run the program later
    f = open("D:\projects\my_code_helper/run.txt", "w")
    f.write(name_of_file)
    f.close()

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


def create_or_run_c_file():
    sys.argv[2] += ".c"

    if sys.argv[2] in list_of_files_in_current_directory:
        run_c(file_name=sys.argv[2])
        return

    # Create the C file if it does not exists
    read_c_file = open("D:\projects\my_code_helper/forC.txt")

    write_c_file = open(sys.argv[2], "w+")
    # Write content into the .c type file
    for content in read_c_file:
        write_c_file.write(content)
    # close both the file streams
    read_c_file.close()
    write_c_file.close()
        

def switch():
    if "." in sys.argv[1]:
        f = open(sys.argv[1], "w")
        f.close()
    elif "-c" in sys.argv[1] or "-C" in sys.argv[1]:
        create_or_run_c_file()


def git_add():
    remove_unwanted()
    try:
        os.system("git add .")
        message = input("(Press 'enter' for commiting without message)\nEnter message:- ").strip()
        if message == "":
            message = 'init commit'
        os.system("git commit -m " + "\"" + message + "\"")
        os.system("git push")
    except:
        print("Something went wrong")


def search_wiki():
    try:
        searching_context = sys.argv[2:]
        if len(searching_context) == 0:
            speak("nothing to search")
            return
        speak("Searching wikipedia")
        speak("How many sentences do you want me to read")
        sent = int(input("Enter number of lines to read: "))
    except IndexError:
        speak("No context to search")
        return
    except:
        sent = 10
        speak("I can't get it. I am reading out 10 sentences for you!")
    
    res = wikipedia.summary(searching_context, sentences=sent)
    speak("According to wiki..")
    print(res)
    speak(res)

def search_youtube():
    try:
        searching_context = sys.argv[2:]
        speak("Searching youtube")
    except IndexError:
        speak("No context to search")
        return
    query = "http://www.youtube.com/results?search_query="

    for comm in searching_context:
        query += comm
        query += '+'
    print(query)
    webbrowser.open(query)

def search_google():
    try:
        searching_context = sys.argv[2:]
        speak("Searching google")
    except IndexError:
        speak("No context to search")
        return
    query = "https://www.google.com/search?q="
    
    for comm in searching_context:
        query += comm
        query += '+'
    print(query)
    webbrowser.open(query)



def main():
    if sys.argv[1] == "clean" or sys.argv[1] == "flush" or sys.argv[1] == "cleam":
        remove_unwanted()
    elif sys.argv[1] == "run":
        run_java()
    elif sys.argv[1] == "commit" or sys.argv[1] == "push":
        git_add()
    elif "wikipedia" in sys.argv[1] or "pedia" in sys.argv[1] or "wiki" in sys.argv[1]:
        search_wiki()    
    elif "youtube" in sys.argv[1] or "yout" in sys.argv[1] or "tube" in sys.argv[1]:
        search_youtube()
    elif "search" in sys.argv[1] or "google" in sys.argv[1]:
        search_google()
    elif "." not in sys.argv[1] and "-" not in sys.argv[1]:
        pdf_name = sys.argv[1] + ".pdf"
        print(f"found {pdf_name}")
        if pdf_name in list_of_files_in_current_directory:
            read_pdf(pdf_name)
            return

        sys.argv[1] += ".java"
        Create_or_run_java_file(sys.argv[1])
    else:
        switch()


if __name__ == "__main__":
    if sys.argv[1] == "speak_pdf":
        read_pdf_help(sys.argv[2])
    else: 
        main()   

