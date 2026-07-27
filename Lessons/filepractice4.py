import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
    with open(filename, 'r'):
        
        if os.path.exists(filename):
            return (os.path.exists(filename))
        else:
            print('could not find')
    # Student code goes here
 
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))