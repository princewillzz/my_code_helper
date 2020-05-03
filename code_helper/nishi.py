import os, sys, time
import PyPDF2, wikipedia, webbrowser

from src import *

from threading import Thread
from functools import wraps

speaker = Speaker()

list_of_files_in_current_directory = os.listdir()


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running seconds", str(t1-t0))
        return result
    return function_timer


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
            speaker.speak(page)
            speaker.speak("Do you want to read more(y/n):- ")
            choice = input("Do you want to read more(y/n):- ").strip()
            if "y" in choice or "Y" in choice:
                continue
            else:
                return
        speaker.speak("The pdf has been fully read")
    except:
        speaker.speak("The page number cannot be found by me sorry")

def read_pdf(pdf_name):
    try:
        os.system(f'start cmd /c "nishi.py speak_pdf {pdf_name} {sys.argv[2]} "')
    except:
        os.system(f'start cmd /c "nishi.py speak_pdf {pdf_name} "')



# Remove the ".class" type file created after the execution of the program 
def remove_unwanted(instruction=None):
    if not instruction == None:
        os.remove(instruction)
    else:
        for file in list_of_files_in_current_directory:
            if ".class" in file:
                os.remove(file)
        

def switch():
    if "." in sys.argv[1]:
        f = open(sys.argv[1], "w")
        f.close()
    elif "-CR" == sys.argv[1] or "-cr" == sys.argv[1]:
        exefile = run_c(f"{sys.argv[2]}.c")
        os.remove(exefile)
    elif "-R" == sys.argv[1] or "-r" == sys.argv[1]:
        os.remove("a.exe")
    elif "-c" in sys.argv[1] or "-C" in sys.argv[1]:
        create_or_run_c_file(sys.argv[2])



@fn_timer
def main():
    if sys.argv[1] == "clean" or sys.argv[1] == "flush" or sys.argv[1] == "cleam":
        remove_unwanted()
    elif sys.argv[1] == "run":
        print("enter")
        run_java()
        print("exit")
    elif sys.argv[1] == "commit" or sys.argv[1] == "push":
        git_add()
    elif "wikipedia" in sys.argv[1] or "pedia" in sys.argv[1] or "wiki" in sys.argv[1]:
        try:
            thread = Thread(target=search_wiki, args=(sys.argv[2:],))
            thread.start() 
        except:
            speaker.speak("Nothing to search!")
    elif "youtube" in sys.argv[1] or "ytb" in sys.argv[1] or "tube" in sys.argv[1]:
        search_youtube()
    elif "search" in sys.argv[1] or "google" in sys.argv[1]:
        search_google()
    elif "." not in sys.argv[1] and "-" not in sys.argv[1]:
        pdf_name = sys.argv[1] + ".pdf"
        
        if pdf_name in list_of_files_in_current_directory:
            print(f"Reading {pdf_name}")
            t = Thread(target=read_pdf, args=(pdf_name,))
            t.start()
        else:
            sys.argv[1] += ".java"
            Create_or_run_java_file(sys.argv[1])
    else:
        switch()


if __name__ == "__main__":
    if sys.argv[1] == "speak_pdf":
        read_pdf_help(sys.argv[2])
        
    else: 
        main()  

