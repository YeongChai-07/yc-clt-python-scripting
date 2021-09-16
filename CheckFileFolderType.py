from os import system, path
# Gets input from user
file_folder_name = input("Please enter a name of a file or folder:")
# Let's check what item type does the file/folder that the user input, belongs to
if path.isdir(file_folder_name):
    print("This is a directory.\n")
elif path.isfile(file_folder_name):
    print("This is a regular file.\n")
elif path.islink(file_folder_name):
    print("This is a symbolic link.\n")
elif path.ismount(file_folder_name):
    print("This is a mount point.\n")
# Finally displaying the information of the file/folder in long-listing format
os_list_dir_command = "ls -lart " # OS-Specific list directory command (Unix)
system(os_list_dir_command + file_folder_name) # Invoking the command
