import os


def run_c(file_name):
    executable_file = "a.exe"
    try:
        if os.system(f"gcc {file_name}") == 1:
            return

        os.system(executable_file)
    except:
        print("Something is wrong")


def create_or_run_c_file(file_name):
    file_name += ".c"

    if os.path.exists(file_name):
        run_c(file_name=file_name)
        return

    # Create the C file if it does not exists
    file_to_read = os.path.dirname(__file__) + "\\trackingfiles/forC.txt"
    read_c_file = open(file_to_read)
    # "D:\dev\projects\my_code_helper\\trackingfiles/forC.txt")

    write_c_file = open(file_name, "w+")
    # Write content into the .c type file
    for content in read_c_file:
        write_c_file.write(content)

    # close both the file streams
    read_c_file.close()
    write_c_file.close()
