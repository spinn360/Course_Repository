import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
    with os.scandir('.') as entries:
        for entry in entries:
            # Check if the entry is a file
            if entry.is_file():
                print(entry.name)
    # Student code goes here
    
# expected output: main.py    
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())