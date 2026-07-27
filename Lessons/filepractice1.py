'''
# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    print(mystring[0:x])
    # Student code goes here
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)
'''

import os

# Complete the function to return the current working directory
def getCurrentDirectory():
    directory = os.getcwd()
    return directory
    # Student code goes here
 
# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())