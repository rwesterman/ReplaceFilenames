<<<<<<< HEAD
#! python3

import os
import re   #regular expressions


def findAndList(find, replace):

    # Exits early if search term and replacement term are identical
    if find == replace:
        return "Search and replace are equal. Exiting without rename"


    #Make a dictionary with format Key:Value is OldFilename:NewFilename
    filelist = {}

    # Fixing edge case of find being substring of replace

    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for file in filenames:
            # returns index of first matching substring
            start = file.find(find)
            end = start + len(find)
            last_index = start + 1      #Keep track of previous start index + 1, begin search here

            #Set new_file to original file name. We will modify new_file and use it to replace original filename
            new_file = file

            # while the requested substring is still in the name, loop and replace it
            while start >= 0:
                new_file = new_file[0:start] + replace + new_file[end:]
                start = new_file.find(find, last_index)
                end = start + len(find)
                last_index = start

            # Add to dictionary if filename has changed
            if file != new_file:
                filelist[file] = new_file

        # Show user the results of the name change, and get approval
        # Only runs if filelist is populated and there will be some changes
        if filelist:
            print("\nThis will change names as shown below:")
            for key in filelist:
                print("Original Filename:\t" + key)
                print("New Filename:\t\t" + filelist[key] +"\n")

            if input("Do you want to proceed? (Y/n) ").lower() == 'y':
                rename(filelist)
                return "Rename complete"
            else:
                return "Exiting without renaming files"
        else:
            print("No match found in filenames")
            if input("Would you like to try another search? (Y/n)").lower() == 'y':
                main()
            else:
                return "Exiting..."


def rename(filelist):
    # Will replace requested substring in filenames
    for key in filelist:
        try:
            os.rename(key, filelist[key])
        except OSError as e:
            print("Could not rename file due to OS error")


def main():
    print("Run this script from the folder with files you want to edit")
    find = str(input("What do you want to find?: "))
    replace = str(input("What should it be replaced with?: "))
    print(findAndList(find, replace))

if __name__ == '__main__':
    main()
=======
#! python3

import os
import re   #regular expressions

# Issue: if find=replace, then program will continually find the replaced substring in the name. Can't allow this.
# Same for any time find is a substring of replace. Will perpetually add characters
# Need to program special cases for these.

def findAndList(find, replace):

    # Exits early if search term and replacement term are identical
    if find == replace:
        return "Search and replace are equal. Exiting without rename"


    #Make a dictionary with format Key:Value is OldFilename:NewFilename
    filelist = {}

    # Fixing edge case of find being substring of replace

    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for file in filenames:
            # returns index of first matching substring
            start = file.find(find)
            end = start + len(find)
            last_index = start + 1      #Keep track of previous start index + 1, begin search here

            #Set new_file to original file name. We will modify new_file and use it to replace original filename
            new_file = file

            # while the requested substring is still in the name, loop and replace it
            while start >= 0:
                new_file = new_file[0:start] + replace + new_file[end:]
                start = new_file.find(find, last_index)
                end = start + len(find)
                last_index = start

            # Add to dictionary if filename has changed
            if file != new_file:
                filelist[file] = new_file

        # Show user the results of the name change, and get approval
        # Only runs if filelist is populated and there will be some changes
        if filelist:
            print("\nThis will change names as shown below:")
            for key in filelist:
                print("Original Filename:\t" + key)
                print("New Filename:\t\t" + filelist[key] +"\n")

            if input("Do you want to proceed? (Y/n) ").lower() == 'y':
                rename(filelist)
                return "Rename complete"
            else:
                return "Exiting without renaming files"
        else:
            print("No match found in filenames")
            if input("Would you like to try another search? (Y/n)").lower() == 'y':
                main()
            else:
                return "Exiting..."


def rename(filelist):
    # Will replace requested substring in filenames
    for key in filelist:
        try:
            os.rename(key, filelist[key])
        except OSError as e:
            print("Could not rename file due to OS error")


def main():
    print("Run this script from the folder with files you want to edit")
    find = str(input("What do you want to find?: "))
    replace = str(input("What should it be replaced with?: "))
    print(findAndList(find, replace))

if __name__ == '__main__':
    main()
>>>>>>> 18214a59d86f9d78b8185717f39a32de3e1bbac1
