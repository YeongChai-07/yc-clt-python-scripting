import os
# Gets input from user
file_folder_name = input("Please enter a name of a file or folder:")
# Let's check what item type does the file/folder that the user input, belongs to
if os.path.isdir(file_folder_name):
    print("This is a directory.\n")
elif os.path.isfile(file_folder_name):
    print("This is a regular file.\n")
elif os.path.islink(file_folder_name):
    print("This is a symbolic link.\n")
elif os.path.ismount(file_folder_name):
    print("This is a mount point.\n")
# Finally displaying the information of the file/folder in long-listing format
# Using dictionary data structure to store the directory command for individual platform.
# E.g. posix => Unix OS, nt => Windows OS, java => Java-based OS
os_list_dir_command_dict = {"posix": "ls -lart ", "nt" : "dir "}
os.system(os_list_dir_command_dict[os.name] + file_folder_name) # Invoking the command
