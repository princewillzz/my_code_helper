import sys, PyPDF2
from .speaker import Speaker

def readPDF(pdf_name):
    speaker = Speaker()
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
            print("Do you want to read more(y/n):- ")
            speaker.speak("Do you want to read more(yes/nes):- ")
            choice = input().strip()
            if "y" in choice or "Y" in choice:
                continue
            else:
                return
        speaker.speak("The pdf has been fully read")
    except:
        speaker.speak("The page number cannot be found by me sorry")

