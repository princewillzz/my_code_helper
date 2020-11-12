import os


def displayHelp():
    displayHelpFile = open(
        "D:\dev\projects\my_code_helper\\trackingfiles/display_help.txt")
    for line in displayHelpFile:
        print(line)


def sortHelpFile():
    try:
        # open the help file to read its content
        displayHelpFile = open(
            "D:\dev\projects\my_code_helper\\trackingfiles/display_help.txt")

        # create a list to store all the content
        allLinesList = list()
        for lines in displayHelpFile:
            allLinesList.append(lines)

        # Sort the list lexicograpphically
        allLinesList.sort()

        # Open the same help file to write in it and write the sorted list
        displayHelpFileNew = open(
            "D:\dev\projects\my_code_helper\\trackingfiles/display_help.txt", 'w')
        for ele in allLinesList:
            displayHelpFileNew.write(ele)
    except Exception as e:
        print("something wrong with the system... ")


if __name__ == "__main__":
    displayHelp()
    sortHelpFile()
