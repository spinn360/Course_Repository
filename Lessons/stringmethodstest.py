original_substring = input()
sentence = input()

if original_substring in sentence:
    print('Located at index:',sentence.find(original_substring))
    #replace the first 2 occurences
    sentence = sentence.replace(original_substring, '#', 2) #, 2 denotes only first 2
    print(sentence)
else:
    print('None found')


#################################################################


name_entry1 = input()
name_entry2 = input()

if name_entry1 == name_entry2:
    print('Same inputs')
elif name_entry1 > name_entry2:
    print(name_entry1)
else:
    print(name_entry2)


########################################################


string_input = input()

if string_input[0].isdigit() and string_input[0:].isupper():
    print('Valid')
else:
    print('Invalid')


########################################################

user_string = input()

user_string = user_string.strip()
if user_string.find('Color:') != -1:
    user_string = user_string.lower()
else:
    user_string = user_string.upper()
    
print(user_string)

############
#alternative
############

user_string = input()
user_string = user_string.strip()

# Use the 'in' operator to check if the substring exists
if 'Color:' in user_string:
    user_string = user_string.lower()
else:
    user_string = user_string.upper()
    
print(user_string)

'''String Methods Reference 
The following table provides a reference for the 47 non-dunder 
string methods in Python. These methods can be used to manipulate 
and perform operations on string objects.



Method	Description
capitalize()	Converts the first character of the string to uppercase.
casefold()	Converts the string to lowercase, more aggressive than lower().
center(width)	Centers the string within a given width, padding with spaces.
count(sub)	Counts the occurrences of a substring in the string.
encode(encoding)	Encodes the string into bytes using the specified 
encoding.
expandtabs(tabsize)	Expands tabs in the string into spaces.
find(sub)	Returns the lowest index where the substring is found, or -1 
if not found.
format(*args, **kwargs)	Performs string formatting by replacing 
placeholders in the string.
format_map(mapping)	Similar to format(), but takes a dictionary as input.
index(sub)	Returns the lowest index of the substring, raises ValueError 
if not found.
isalnum()	Returns True if all characters are alphanumeric.
isalpha()	Returns True if all characters are alphabetic.
isascii()	Returns True if all characters are ASCII.
isdecimal()	Returns True if all characters are decimal digits.
isdigit()	Returns True if all characters are digits.
isidentifier()	Returns True if the string is a valid Python identifier.
islower()	Returns True if all characters are lowercase.
isnumeric()	Returns True if all characters are numeric.
isprintable()	Returns True if all characters are printable.
isspace()	Returns True if all characters are whitespace.
istitle()	Returns True if the string is in title case.
isupper()	Returns True if all characters are uppercase.
join(iterable)	Concatenates elements of an iterable with the string 
as a separator.
ljust(width)	Left-justifies the string within a given width, 
padding with spaces.
lower()	Converts the string to lowercase.
lstrip()	Removes leading whitespace from the string.
partition(sep)	Splits the string into a 3-tuple at the first 
occurrence of the separator.
replace(old, new)	Replaces occurrences of a substring with a new 
substring.
removeprefix(prefix)	Removes the specified prefix if it exists.
removesuffix(suffix)	Removes the specified suffix if it exists.
rfind(sub)	Returns the highest index where the substring is found, 
or -1 if not found.
rindex(sub)	Returns the highest index of the substring, raises 
ValueError if not found.
rjust(width)	Right-justifies the string within a given width, 
padding with spaces.
rpartition(sep)	Splits the string into a 3-tuple at the last 
occurrence of the separator.
rsplit(sep)	Splits the string at each occurrence of the 
separator from the right.
rstrip()	Removes trailing whitespace from the string.
split(sep)	Splits the string at each occurrence of the separator.
splitlines()	Splits the string into a list of lines.
swapcase()	Swaps case, converting uppercase to lowercase and vice versa.
translate(table)	Translates characters using the given translation table.
upper()	Converts the string to uppercase.
zfill(width)	Pads the string with zeroes to the left to fill a given width.

Additional String Methods:
Use help(str) and print(dir(str)) to see more about strings and 
their methods. These commands provide detailed information and 
a list of available string methods.'''

