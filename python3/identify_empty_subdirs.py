#!/usr/bin/python3
import os
import sys

# This script identifies the empty directories and subdirectories within a path using os.walk()

def checkForValidPath(input_path):
    return os.path.exists(input_path)

my_path = input("Enter path to scan (default: cwd): ") or os.getcwd()

if not checkForValidPath(my_path):
    print("That was not a valid path")
    sys.exit()
else:
    empty_dir_list = []
    directory_tree_list = os.walk(my_path) # Returns a python generated list of tuples of root path, list of files, list of subdir

    print (f"\nThis is list of empty directories within {my_path}:")
    for directory in directory_tree_list:
        root_dir, subdir_list, file_list  = directory
        # print(directory)
        if (len(file_list) == 0) and (len(subdir_list) == 0):
            empty_dir_list.append(root_dir)
            print(root_dir)
        