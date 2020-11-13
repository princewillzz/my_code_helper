import os


def displayHelp():
    file_to_read = os.path.dirname(
        __file__) + "\\trackingfiles/display_help.txt"
    displayHelpFile = open(
        file_to_read)
    for line in displayHelpFile:
        print(line)


def sortHelpFile():
    try:
        # open the help file to read its content
        file_to_read = os.path.dirname(
            __file__) + "\\trackingfiles/display_help.txt"
        displayHelpFile = open(
            file_to_read)

        # create a list to store all the content
        allLinesList = list()
        for lines in displayHelpFile:
            allLinesList.append(lines)

        # Sort the list lexicograpphically
        allLinesList.sort()

        # Open the same help file to write in it and write the sorted list
        displayHelpFileNew = open(file_to_read, 'w')
        for ele in allLinesList:
            displayHelpFileNew.write(ele)
    except Exception as e:
        print("something wrong with the system... ")


if __name__ == "__main__":
    displayHelp()
    sortHelpFile()
