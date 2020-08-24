#!/usr/bin/env python
import os, sys, time
import PyPDF2

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


def switch():
    if "." in sys.argv[1]:
        f = open(sys.argv[1], "w")
        f.close()
    elif "-cr" == sys.argv[1] or "-CR" == sys.argv[1]:
        try:
            run_c(f"{sys.argv[2]}.c")
        except:
            try:
                os.remove("a.exe")
            except:
                speaker.speak("no filename found")
                print("Nothing to do")
                print("syntax:- -cr 'filename'")
    elif "-r" == sys.argv[1] or "-R" == sys.argv[1]:
        try:
            os.remove(sys.argv[2])
        except IndexError:
            os.remove("a.exe")
        except:
            speaker.speak("No file found")
            print("Nothing to delete")
            print("syntax:- -r 'filename'")
    elif "-c" == sys.argv[1] or "-C" == sys.argv[1]:
        try:
            create_or_run_c_file(sys.argv[2])
        except:
            speaker.speak("No argument found")
            print("syntax:- -c 'filename'")
    elif "-convert" == sys.argv[1]:
        try:
            docx_name = input("Enter Docx file name: ")
            pdf_name = docx_name + ".pdf"
            docx_name += ".docx"
            final_pdf_name = input("Enter pdf name: ")
            final_pdf_name += ".pdf"
            print("converting...")
            convertDocxToPDF(docx_name=docx_name, pdf_name=pdf_name, final_pdf_name=final_pdf_name)
            print("converted...")
        except:
            print("Something went wrong")
            speaker.speak("Something strange")
    elif "-docx":
        pdf_name = input("Enter the pdf file name: ")
        
        print(pdf_name)
        PdfDocxcoverter(pdfName=pdf_name)


def helper(secret_command, pdf_name=None):
    try:
        if pdf_name == None:
            arguments = ""
            for ele in sys.argv[2:]:
                arguments += f"{ele} "
            os.system(f'start cmd /c "nishi.py {secret_command} {arguments}"')
        else:
            os.system(f'start cmd /c "nishi.py {secret_command} {pdf_name} {sys.argv[2]} "')
    except Exception as e:
        os.system(f'start cmd /c "nishi.py {secret_command} {pdf_name} "')




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
    elif "wikipedia" == sys.argv[1] or "pedia" == sys.argv[1] or "wiki" == sys.argv[1] or sys.argv[1] == "-w" or sys.argv[1] == "-W":
        try:
            t = Thread(target=helper, args=("speak_wiki002",))
            t.start()
        except:
            speaker.speak("Nothing to search!")
    elif "ytb" == sys.argv[1] or "youtube" in sys.argv[1] or "tube" == sys.argv[1]:
        if sys.argv[2:] == []:
            speaker.speak("The arguments are missing sir")
            print("syntax:- ytb \"arguments\"")
        else:
            t = Thread(target=search_youtube, args=(sys.argv[2:], ))
            t.start()
            speaker.speak("Searching youtube")
            #search_google(sys.argv[2:])
    elif "search" == sys.argv[1] or "google" == sys.argv[1]:
        if sys.argv[2:] == []:
            speaker.speak("The arguments are missing sir")
            print("syntax:- google \"arguments\"")
        else:
            t = Thread(target=search_google, args=(sys.argv[2:], ))
            t.start()
            speaker.speak("Searching google")
    elif "." not in sys.argv[1] and "-" not in sys.argv[1]:
        pdf_name = sys.argv[1] + ".pdf"
        
        if os.path.exists(pdf_name):
            print(f"Reading {pdf_name}")
            t2 = Thread(target=helper, args=("speak_pdf001", pdf_name))
            t2.start()
            
        else:
            sys.argv[1] += ".java"
            if Create_or_run_java_file(sys.argv[1]) == 404:
                remove_unwanted()
    else if "note" in sys.argv[1] or "record" in sys.argv[1]:
        pass
    else:
        switch()


if __name__ == "__main__":
    """docx_name = sys.argv[1]
    final_pdf_name = sys.argv[2]
    pdf_name = docx_name.split(".")[0] + ".pdf"
    convertDocxToPDF(docx_name=docx_name, pdf_name=pdf_name, final_pdf_name=final_pdf_name)"""
    
    

    if sys.argv[1] == "speak_pdf001":
        readPDF(sys.argv[2])
        
    elif sys.argv[1] == "speak_wiki002":       
        search_wiki(sys.argv[2:])
        
    else: 
        
        main()  
        
