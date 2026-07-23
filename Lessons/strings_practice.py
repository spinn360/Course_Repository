# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    print(mystring[0:x])
# Student code goes here
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)

###################################################

# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    return mystring[-x:]
# Student code goes here
 
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))

##############################################

# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    return mystring[-x:]
# Student code goes here
 
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))

######################################################

# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
    if 'WGU' in mystring:
        return True
    else:
        return False
# Student code goes here
    
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))

############################################################


# Complete the function to print all of the words in the given string
def printWords(mystring):
    print(''.join(mystring))
# Student code goes here
    
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')

##################################################################

# Complete the function to combine the words into a sentence and return a string 
def combineWords(words):
    return ' '.join(words)
# Student code goes here
    
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))

#################################################
#Task 6

# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
    mystring = mystring.replace('WGU','Western Governors University')
    print(mystring)
# Student code goes here
    
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

##############################################################
#Task 7

# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
    if mystring.startswith('WGU'):
        return mystring
    else:
        return mystring.replace('WGU','')
# Student code goes here
    
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))

###############################################################
#Task 8

# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()
    return string1 + string2

# Student code goes here
    
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))

###############################################################
#Task 9 

# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    print(f'${rate:.2f}')
# Student code goes here
 
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)

##########################################################
#Task 10


# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    count_upper = 0

    for char in mystring:
        if char.isupper():
            count_upper += 1
    return count_upper
# Student code goes here
 
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))

###################################################

user_string = input('Enter a number: ')

if user_string.isdigit():
    print('Yes')
else:
    print('No')

####################################################

full_name = input('Enter full name: ')
name_list = full_name.split()
if len(name_list) == 3:
    print(name_list[2]+',', name_list[0][0]+'.'+ name_list[1][0]+'.')
elif len(name_list) == 2:
    print(name_list[1]+',', name_list[0][0]+'.')

##########################################################

str = input('Enter a letter to search for then a phrase to search then hit enter: ')
target_char = str[0]
phrase = str[2:]
countstr = 0
for char in phrase:
    if char == target_char:
        countstr += 1
if countstr == 1:
    print(countstr, target_char)
elif countstr >1:
    print(countstr, target_char+"'s")
else:
    print(countstr, target_char+"'s")


###############################################################

while True:
    answer = input('Enter food type and a number(ex: apples 2) or quit to exit: ')
    libslist = answer.split()
    
    if libslist[0] == 'quit':
        break
    word = libslist[0]
    number = libslist[1]

    print(f'Eating {number} {word} a day keeps you happy and healthy.')

    ###############################################################

my_string = input('Enter a string to return only alphanumeric: ')
newstring = ''
for char in my_string:
    if char.isalnum():
        newstring = newstring + char
print(newstring)