from .speaker import Speaker
import webbrowser
import wikipedia, sys

def search_youtube(query):
    speaker = Speaker()
    try:
        searching_context = query
        speaker.speak("Searching youtube")
    except IndexError:
        speaker.speak("No context to search")
        return
    url = "http://www.youtube.com/results?search_query="

    for word in searching_context:
        url += word
        url += '+'
    print(url)
    # url = http://www.youtube.com/results?search_query=beauty+tips
    webbrowser.open(url)

def search_google(query):
    speaker = Speaker()
    try:
        searching_context = query
        speaker.speak("Searching google")
    except IndexError:
        speaker.speak("No context to search")
        return
    url = "https://www.google.com/search?q="
    
    for word in searching_context:
        url += word
        url += '+'
    print(url)
    webbrowser.open(url)


def search_wiki(query):
    speaker = Speaker()
    try:
        print(type(query))
        speaker.speak("Searching wikipedia")
        speaker.speak("How many sentences do you want me to read")
        sent = int(input("Enter number of lines to read: "))
    except:
        sent = 1
        speaker.speak("I can't get it. I am reading out 1 sentences for you!")
    
    res = wikipedia.summary(query, sentences=sent)
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


if __name__ == "__main__":
    argument = sys.argv[1]
    query = sys.argv[2:]
    if argument == "-w" or argument == "-W":
        search_wiki(query=query)


