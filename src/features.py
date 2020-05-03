
from .speaker import Speaker
import webbrowser
import wikipedia, sys, os

def search_youtube(query_list):
    url = "http://www.youtube.com/results?search_query="

    for word in query_list:
        url += word
        url += '+'
    #print(url)
    # url = http://www.youtube.com/results?search_query=beauty+tips
    webbrowser.open(url)

def search_google(query_list):
    url = "https://www.google.com/search?q="
    
    for word in query_list:
        url += word
        url += '+'
    #print(url)
    webbrowser.open(url)


def search_wiki(query_list):
    query = ""
    for ele in query_list:
        query += ele+ " "
    print(query)
    speaker = Speaker()
    
    try:
        speaker.speak("Searching wikipedia")
        
        sentences = int(input("Enter number of lines to read: "))
        speaker.speak("How many sentences do you want me to read")        
    except:
        sentences = 5
        speaker.speak("I can't get it. I am reading out 5 sentences for you!")
    
    res = wikipedia.summary(query, sentences=sentences)
    speaker.speak("According to wiki..")
    print(res)
    speaker.speak(res)



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


# Remove the ".class" type file created after the execution of the program 
def remove_unwanted(instruction=None):
    if not instruction == None:
        os.remove(instruction)
    else:
        list_of_files_in_current_directory = os.listdir()
        for file in list_of_files_in_current_directory:
            if ".class" in file:
                os.remove(file)
        