import os
import pathlib
import datetime
import re

# Default the prompt_user_ext_toggle to True as we want the script to prompt the user for the file
# extension during the start of the script
prompt_user_file_ext_toggle = True

while prompt_user_file_ext_toggle:
    # Prompts user on files for which file extension to perform the rename
    file_ext_for_file_rename = input("Which file extension would you prefer to rename filename prefix ?\n"
                                     + "(DO NOT simply press enter and left the input empty)")
    # Stripping (removes) away whitespaces on the start and end of the file extension input
    file_ext_for_file_rename = file_ext_for_file_rename.strip()

    # Validates the file extension that user entered is in correct format or not
    file_ext_is_not_valid = len(file_ext_for_file_rename) == 0 or re.fullmatch(r'\.[0-9a-zA-z]{2,}', file_ext_for_file_rename ) is None
    if file_ext_is_not_valid:
        # Uh..Oh...We are either receiving an empty input from the file extension prompt above or it is not in
        # the correct file extension format. Shows an error (with valid file extension examples) to user.
        print("You have entered an invalid file extension.\n"
              + "File extension usually start with a dot (.) followed by 2 or more alpha or numeric characters\n"
              + "Examples: .sh, .jpg, .j2, .3gp, .mp3, .m4v, mp4 and many more\n" + "Please try again.\n")

    # Updates prompt_user_file_ext_toggle with the value of file_ext_is_not_valid so that the user will be prompted
    # to enter the file extension again if the above validation failed
    prompt_user_file_ext_toggle = file_ext_is_not_valid

else:
    # The file extension user entered is in the correct file extension format, it's safe to proceed further.
    # Instantiates a pathlib.Path object with the current directory path
    curr_dir_path = pathlib.Path(os.getcwd())
    # Filter the list of files contained in the current directory, to only those with ".jpg" extension
    list_of_matching_files = curr_dir_path.glob("*" + file_ext_for_file_rename)

    # Prompts user on files for which file extension to perform the rename
    filename_prefix = input("Which prefix would you prefer to append to the filename ?")

    if len(filename_prefix) == 0:
        # Defaulting the value of the filename prefix to the current (today's) date as a string in
        # YYYY-MM-DD format (ISO-8601 format) using the datetime object.
        filename_prefix = datetime.date.today().isoformat() + "-"

    for file_to_rename in list_of_matching_files:
        # Assigning the renaming filename with the following format:
        # "[FilenamePrefix][OriginalFileName]"
        new_filename = f"{filename_prefix}{file_to_rename.name}"
        # Perform the actual file renaming with the new filename format.
        print(f"Renaming {file_to_rename.name} to {new_filename}....")
        file_to_rename.rename(file_to_rename.parent.joinpath(new_filename))
