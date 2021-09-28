import os
import pathlib


def num_of_files_present_dir(param_directory_path=os.getcwd()):
    num_of_files = 0 # Variable to keep track of the files count
    # Instantiates a new pathlib.Path object, corresponds to the native OS platform.
    # Unix / Linux OS => pathlib.PosixPath object, Windows OS => pathlib.WindowsPath object
    directory_path = pathlib.Path(param_directory_path)
    # prints out the directory path being passed over to the function.
    print("Name of directory {0} : ".format(directory_path))

    try:
        # Invoking the pathlib.Path.iterdir() function to get all the files in present directory, iterable as
        # a Generator
        files_curr_dir_generator = directory_path.iterdir()
        while next(files_curr_dir_generator):
            # we will keep iterating each item in the collections within the iterator
            # until the StopIteration Exception is raised
            num_of_files+=1
    except StopIteration:
            # This means that we have reached the end / last item in the collection
            print("Number of files present working directory: {0} ".format(num_of_files))


# Call the num_of_files_present_dir function
num_of_files_present_dir('/tmp')
num_of_files_present_dir(os.getcwd() + "/.idea/")
num_of_files_present_dir('/users/User/Pictures')