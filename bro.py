#!/usr/bin/env python
import os
import sys
import time
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
        print("Total time running seconds", str(t1-t0))
        return result
    return function_timer


def switch(switchQuery, queryCommand=None):

    if "." in switchQuery:
        f = open(switchQuery, "w")
        f.close()
    elif "-corona" == switchQuery or switchQuery == "-coro":
        coronaTracker = CoronaTracker()
        if coronaTracker.isConnectionBroken():
            print("Check your internet connection and Try Again...")
            speaker.speak(
                "Check your internet connection and Try Again later...")
            return

        print("Current Update")

        speaker.speak("Today's Update is!: ")
        coronaTracker.getTodaysUpdate()

        while True:
            countries = list(
                map(str, input("Enter Country/ies name or abbreviation to check it's update: ").split(" ")))

            if countries == None or len(countries) < 1 or len(countries[0]) < 1:
                print("Wear mask be safe... GoodBye")
                speaker.speak("wear mask! and be safe!... GoodBye!")
                return

            coronaTracker.getUpdateOfCountry(countries=countries)

        return
    elif "-cr" == switchQuery or "-CR" == switchQuery:
        try:
            run_c(f"{queryCommand}.c")
        except:
            try:
                os.remove("a.exe")
            except:
                speaker.speak("no filename found")
                print("Nothing to do")
                print("syntax:- -cr 'filename'")
    elif "-r" == switchQuery or "-R" == switchQuery:
        try:
            os.remove(queryCommand)
        except IndexError:
            os.remove("a.exe")
        except:
            speaker.speak("No file found")
            print("Nothing to delete")
            print("syntax:- -r 'filename'")
    elif "-c" == switchQuery or "-C" == switchQuery:
        try:
            create_or_run_c_file(queryCommand)
        except:
            speaker.speak("No argument found")
            print("syntax:- -c 'filename'")
    elif "-convert" == switchQuery:
        try:
            thread = Thread(target=runImageToPDFConverterApp)
            thread.start()
            speaker.speak("Starting the App")
        except:
            print("Something went wrong")
            speaker.speak("Something strange")
    elif "-docx" == switchQuery:
        pdf_name = input("Enter the pdf file name: ")

        print(pdf_name)
        PdfDocxcoverter(pdfName=pdf_name)
    elif "-pdf" == switchQuery:
        try:
            pdf_name = queryCommand + ".pdf"
        except Exception as e:
            print("pdf file name missing")
            raise e

        if os.path.exists(pdf_name):
            print(f"Reading {pdf_name}")
            t2 = Thread(target=helper, args=("speak_pdf001", pdf_name))
            t2.start()


def helper(secret_command, pdf_name=None):
    try:
        if pdf_name == None:
            arguments = ""
            for ele in sys.argv[2:]:
                arguments += f"{ele} "
            os.system(f'start cmd /c "bro.py {secret_command} {arguments}"')
        else:
            os.system(
                f'start cmd /c "bro.py {secret_command} {pdf_name} {sys.argv[2]} "')
    except Exception as e:
        os.system(f'start cmd /c "bro.py {secret_command} {pdf_name} "')


@fn_timer
def main():
    if "sql" in sys.argv[1] or "query" in sys.argv[1]:
        generateSQLQueries()
        return

    if sys.argv[1] == "clean" or sys.argv[1] == "flush" or sys.argv[1] == "cleam":
        try:
            extension = sys.argv[2]
            remove_unwanted(extension=extension)
        except Exception as e:
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
            # search_google(sys.argv[2:])
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
            # Ask Confirmation
            file_name = sys.argv[1] + ".java"

            if Create_or_run_java_file(name_of_file=file_name) == 404:
                remove_unwanted()
    else:
        try:
            switchQuery = sys.argv[1]
            queryCommand = None
            if len(sys.argv) > 2:
                queryCommand = sys.argv[2]
            switch(switchQuery=switchQuery, queryCommand=queryCommand)
        except Exception as e:
            print("something wrong...", e)


if __name__ == "__main__":

    try:
        if sys.argv[1] == "speak_pdf001":
            readPDF(sys.argv[2])

        elif sys.argv[1] == "speak_wiki002":
            search_wiki(sys.argv[2:])

        else:
            main()
    except:
        displayHelp()
