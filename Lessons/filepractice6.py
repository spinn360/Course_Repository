import os

# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
    if os.path.isdir(somePath):
        return 'DIRECTORY'
    elif os.path.isfile(somePath):
        return 'FILE'

    else:
        return 'NEITHER'
    
        # Student code goes here
 
# expected output: DIRECTORY
print('first',whatIsIt(os.getcwd()))
 
# expected output: FILE
print('second',whatIsIt(os.listdir(os.getcwd())[0]))
 
# expected output: NEITHER
print('third',whatIsIt('apple.pie.123.txt'))