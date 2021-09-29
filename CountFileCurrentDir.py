import os


def num_of_files_present_dir():
    num_of_files = 0 # Variable to keep track of the files count
    # Invoking the os.scandir() function to get all the files in present directory, iterable as
    # an iterator (ScandirIterator)
    with os.scandir(os.getcwd()) as files_curr_dir_iterator:
        try:
            while next(files_curr_dir_iterator):
                # we will keep iterating each item in the collections within the iterator
                # until the StopIteration Exception is raised
                num_of_files+=1
        except StopIteration:
            # This means that we have reached the end / last item in the collection
            print("Number of files present working directory: {0} ".format(num_of_files))


# Call the num_of_files_present_dir function
num_of_files_present_dir()