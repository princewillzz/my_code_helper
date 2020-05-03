import os

# Compile and Run the program given as the input 
def run_java(java_file_to_be_run=None):
    if java_file_to_be_run == None:
        # Access the file name to be executed
        f = open("D:\projects\my_code_helper\code_helper/run.txt")
        java_file_to_be_run = f.readline()
        f.close()

    # Return if there exists no files stored in the "run.txt" file to be executed
    if java_file_to_be_run == "":
        return
    try:
        if os.system("javac " + java_file_to_be_run) == 1:
            return
        cont = java_file_to_be_run.split(".")
        os.system("java " + cont[0])
    except:
        print("except")



# Write the contents from "forjava.txt" to the "name_of_file" file
def Create_or_run_java_file(name_of_file):
    
    # Check if the file already exist then just compile and run the program
    if os.path.exists(name_of_file):
        run_java(java_file_to_be_run=name_of_file)
        return

    # Write the name of the file in run.txt to compile and run the program later
    f = open("D:\projects\my_code_helper\code_helper/run.txt", "w")
    f.write(name_of_file)
    f.close()

    # if the file is not present create a new file with the name given as input
    f2 = open(name_of_file, "w+") 
    f1 = open("D:\projects\my_code_helper\code_helper/forjava.txt")
    
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

