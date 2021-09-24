import os,sys
# Gets input from the Python Interpreter
# sys.args[0] values contains the path of the script
# sys.args[1] & subsequent indexes contains the subsequent arguments passed to the script.
file_folder_name = sys.argv[1]
#file_folder_name = input("Please enter a name of a file or folder:")
SCRIPT_EXIT_STATUS = 2 # Defaulting the exit status to 2.
# Let's check what item type does the file/folder that the user input, belongs to
if os.path.isdir(file_folder_name):
    print("This is a directory.\n")
    SCRIPT_EXIT_STATUS = 1 # Assigning exit status to 1.
elif os.path.isfile(file_folder_name):
    print("This is a regular file.\n")
elif os.path.islink(file_folder_name):
    print("This is a symbolic link.\n")
elif os.path.ismount(file_folder_name):
    print("This is a mount point.\n")
else:
    SCRIPT_EXIT_STATUS = 0 # Assigning exit status to 0

# Exits the script with exit code
sys.exit(SCRIPT_EXIT_STATUS)
