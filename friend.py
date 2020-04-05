import os
import sys

def remove_unwanted(name_of_file):
    


def writeContent(name_of_file):
    f2 = open(name_of_file, "w+")
    f1 = open("forjava.txt")


    for content in f1:
        if "forjava" in content:
            name_of_file = name_of_file.split(".")
            cont = content.replace("forjava", name_of_file[0])
            f2.write(cont)
        else:
            f2.write(content)


if __name__ == "__main__":
    name_of_file = sys.argv[1]
    if name_of_file == "clean":
        remove_unwanted(name_of_file)
    else:
        writeContent(name_of_file)

