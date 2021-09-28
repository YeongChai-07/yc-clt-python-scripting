import os
import pathlib
import datetime

# Instantiates a pathlib.Path object with the current directory path
curr_dir_path = pathlib.Path(os.getcwd())
# Filter the list of files contained in the current directory, to only those with ".jpg" extension
list_of_matching_files = curr_dir_path.glob("*.jpg")
# Retrieves the current (today's) date as a string in YYYY-MM-DD format (ISO-8601 format)
# using the datetime object
today_date_str = datetime.date.today().strftime('%Y-%m-%d')
# Alternatively today's date string could be accessed via the .isoformat() method
#today_date_str = datetime.date.today().isoformat()

for file_to_rename in list_of_matching_files:
    # Assigning the renaming file format to be as follows
    # "YYYY-MM-DD(Today's date)-OriginalFileName"
    new_filename = "{0}-{1}".format(today_date_str, file_to_rename.name)
    # Perform the actual file renaming with the new filename format.
    file_to_rename.rename(file_to_rename.parent.joinpath(new_filename))
