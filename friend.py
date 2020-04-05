#!/usr/bin/env python
import os
import sys

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

def git_add(message):
    remove_unwanted()
    os.system("git add .")
    os.system("git commit -m " + "\"" + message + "\"")


def main():
    name_of_file = sys.argv[1]
    if name_of_file == "clean":
        remove_unwanted()
    elif name_of_file == "doit":
        doit()
    elif name_of_file == "commit":
        try:
            message = input("Message:- ")
            if message.strip() == "":
                print("cannot commit without message:)")
                return
            git_add(message)
        except:
            return
    else:
        name_of_file += ".java"
        writeContent(name_of_file)

if __name__ == "__main__":
    main()