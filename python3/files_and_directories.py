#!/usr/bin/python3
# Use the shebang when you wanna run the script directly on a unix system with the system python (or the path shown by which python3)
# Also, you would need to give it execute permissions using $ chmod +x script.py

# Write a python script that reads a directory and identifies all the files and subdirectories within it
import os
import sys

my_path = input("Enter your path here (default: pwd): ") or os.getcwd() # cwd() gives the current workig directory
print(my_path)
# In a windows machine, while providing path always use two / to escape the /.
# For example: C://My_Files//script.py

if os.path.exists(my_path) is False:
    sys.exit()

list_directories = os.listdir(my_path) # Lists the immediate directory contents within the mentioned path
print(list_directories)

# Sorting the files and directories:
my_files = []
my_dir = []

def fileAndDirectorySorter(listDir):
    for item in listDir:
        if(os.path.isfile(item)):
            my_files.append(item)
        else:
            my_dir.append(item)

fileAndDirectorySorter(list_directories)
print(f"These are the files: {my_files}")
print(f"These are the directories: {my_dir}")

# To create a complete path for a file, one can use os.path.join as so:
# full_path_to_file = os.path.join(os.cwd() + filename.py)

