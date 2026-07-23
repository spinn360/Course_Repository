print(f'{"Player Name":16}{"Goals":8}')
print('-' * 24)
print(f'{"Sadio Mane":16}{"22":8}')
print(f'{"Gabriel Jesus":16}{"7":8}')
print(f'{"Left here right there":<40}{"7":>16}')
print(f'{"Left":<16}{"7":>16}')
print(f'{"Left":>16}{"7":<16}')
print(f'{"Left":*<16}{"7":0>16}')
print(f'{"Left":*^16}{"7":*^16}')

item_name = 'fart'

print(f'{item_name:=<16}')
print(f'{item_name:=>16}')

feet_length = 61
meters_length = feet_length * 0.3048

print(f'Before formatting: {meters_length} meters')

print(f'After formatting: {meters_length:.6f} meters')


'''
employees = input().split()
states = input().split()
separator_char = input()

print(f'{"Employees":^27}{"States":^27}')
print(f'{separator_char * 54}')
print(f'{employees[0]:^27}{states[0]:^27}')
print(f'{employees[1]:^27}{states[1]:^27}')
print(f'{employees[2]:^27}{states[2]:^27}')
'''

phrase = 'Someday I will have three goats, six horses, and nine llamas.'

# Replace English with Spanish.
phrase = phrase.replace('one', 'uno')
phrase = phrase.replace('two', 'dos')
phrase = phrase.replace('three', 'tres')
phrase = phrase.replace('four', 'cuatro')
phrase = phrase.replace('five', 'cinco')
phrase = phrase.replace('six', 'seis')
phrase = phrase.replace('seven', 'siete')
phrase = phrase.replace('eight', 'ocho')
phrase = phrase.replace('nine', 'nueve')

print('Translation:', phrase)
print('searching for "and": Found in string index', phrase.find('and'))
print('searching for "and": Found in string index', phrase.find('and',40)) #start searching at index 40
print('searching for "and": between 40 and 44', phrase.find('and',40,44)) #-1 means not found
print('searching in reverse for "and": Found in string index', phrase.rfind('and')) #searches in reverse
print('Count "i" in string:', phrase.count('i'))

if 'llama' in phrase:
    print('llama found in phrase string')
else:
    print('llama not found in string')

    '''Some methods are useful for finding the position of where a 
    character or substring is located in a string:

find(x) -- Returns the index of the first occurrence of item x in the string, 
        otherwise, find(x) returns -1. x may be a string variable or string 
        literal. Recall that in a string, the index of the first character 
        is 0, not 1. If my_str is 'Boo Hoo!':
my_str.find('!')  # Returns 7
my_str.find('Boo')  # Returns 0
my_str.find('oo')  # Returns 1 (first occurrence only)
find(x, start) - Same as find(x), but begins the search at index start:
my_str.find('oo', 2)  # Returns 5
find(x, start, end) -- Same as find(x, start), but stops the search at index 
                        end - 1:
my_str.find('oo', 2, 4)  # Returns -1 (not found)
rfind(x) -- Same as find(x) but searches the string in reverse, returning the 
            last occurrence in the string.
Another useful function is count, which counts the number of times a 
substring occurs in the string:


count(x) -- Returns the number of times x occurs in the string'''



'''
word = 'onomatopoeia'
num_guesses = 10

hidden_word = '-' * len(word)

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input(f'Enter a character (guess #{guess}): ')
    
    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)
    
        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position+1)  # Find the position of the next occurrence
            hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]  # Rebuild the hidden word string
    
        guess += 1
        
if not '-' in hidden_word:
    print('Winner!', end=' ')        
else:
    print('Loser!', end=' ')

print(f'The word was {word}.')
'''

if 'seph' in 'Joseph':
    print(True)
if 'jo' in 'Joseph':
    print(True)
else:
    print(False)

student_name = input('Enter student name Amy Adams: ')

if student_name is 'Amy Adams': # is returns false because python creates a new object on input and they dont point to same object
    print('Identity operator: True')
else:
    print('Identity operator: False')

if student_name == 'Amy Adams':
    print('Equality operator: True')
else:
    print('Equality operator: False')

    '''Methods to check a string value that returns 
    a True or False Boolean value:
isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
isdigit() -- Returns True if all characters are the numbers 0-9.
islower() -- Returns True if all cased characters are lowercase letters.
isupper() -- Returns True if all cased characters are uppercase letters.
isspace() -- Returns True if all characters are whitespace.
startswith(x) -- Returns True if the string starts with x.
endswith(x) -- Returns True if the string ends with x.
Note that the methods islower() and isupper() ignore non-cased characters. 
Ex: "abc?".islower() returns True, ignoring the question mark.'''

'''Methods to create new strings:
capitalize() -- Returns a copy of the string with the first character 
capitalized and the rest lowercased.
lower() -- Returns a copy of the string with all characters lowercased.
upper() -- Returns a copy of the string with all characters uppercased.
strip() -- Returns a copy of the string with leading and trailing whitespace 
removed.
title() -- Returns a copy of the string as a title, with first letters of 
words capitalized.'''

namebob = input('enter name with spaces and random capital and I will fix: ').strip().lower()
print(namebob)

menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS'] 

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination
            
    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print(f'{passenger.title()} --> {passengers[passenger]}')
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()

    