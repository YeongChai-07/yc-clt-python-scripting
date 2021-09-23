import os
path_to_check = '/data/myUser/myFiles/nthFile'
#path_to_check = os.getcwd() + '/stupidTest.py'
# Let's begin by first check whether the path exists or not
if os.path.exists(path_to_check):
    print("The path " + path_to_check + " exists.")
    # Now we know this path exists, let's assert whether we have permission to write to the file or
    # not
    try:
        # Opening the file stream to the file and setting it to write mode.
        with open(path_to_check, 'r+') as write_file_stream:
            # Append some empty content to test whether the file is writable by the current user.
            write_file_stream.write("")
            print("Oh...Yeah... You are allowed to change this file.")
    except PermissionError:
        print("Nah.... Nope, you ain't permitted to change this file.")

