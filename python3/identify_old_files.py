#!/usr/bin/python3
import sys
import os
import datetime

# Identifies files that are older than 'x' days

my_path = input ("Please enter the path where you would like to identify files (defaults to cwd): ") or os.getcwd()

# Returns only files from a list of files and directories
def filterFiles(dir_list):
    file_list = []
    for item in dir_list:
        if os.path.isfile(item):
            file_list.append(item)
    return file_list

def identify_old_files(file_list, time_parameter):
    current_time = datetime.datetime.now()
    old_files_list = []
    print(f'\n File Name \t Last Modified \t Days since last modified')
    print(f'\n ========= \t ============= \t ========================')
    for file in file_list:
        last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        time_diff_in_days = (current_time - last_modified_time).days
        if (time_diff_in_days > time_parameter) or (time_diff_in_days == time_parameter):
            old_files_list.append(file)
            print(f'\n {file} \t {last_modified_time} \t {time_diff_in_days}')
    return old_files_list

# Main function
if os.path.exists(my_path) is False:
    print("Please enter a valid path")
    sys.exit(1) # Exit with an error code of 1
if os.path.isfile(my_path) is True:
    print(f"Please enter a directory path. ({my_path}) is a file")
    sys.exit(2) # Exiting with a different error code
else:
    dir_list = os.listdir(my_path)  # Returns an array of files and folders in the mentioned path
    file_list = filterFiles(dir_list)
    required_age = int(input("How old should the files be in days? (default 1 day): ")) or 5

    identify_old_files(file_list, required_age)


