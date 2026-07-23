'''print(f'{2**2=}')
# 2**2=4
two_power_two = 2**2
print(f'{two_power_two=}')
# two_power_two=4
print(f'{2**2=},{2**4=}')
# 2**2=4,2**4=16
print(f'{{2**2}}')
# {2**2}
print(f'{{{2**2=}}}')
# {2**2=4}'''

'''A format specification inside a replacement field allows a value's formatting in the 
string to be customized. Ex: Using a format specification, a variable with the integer 
value 4 can be output as a floating-point number (4.0), with leading zeros (004), and 
aligned to the left or right, etc.

A format specification is introduced with a colon : in the replacement field. The colon 
separates the "what" on the left from the "how" on the right. The left "what" side is an 
expression to be evaluated, perhaps just a variable name or a value. The right "how" side 
is the format specification that determines how to show that value using special characters. 
Ex: {4:.2f} formats 4 as 4.00.

A presentation type is part of a format specification that determines how to represent a value 
in text form, such as an integer (4), a floating point (4.0), a fixed precision decimal (4.000), 
a percentage (4%), a binary (100), etc. A presentation type can be set in a replacement field by 
inserting a colon : and providing one of the presentation type characters described below.

More advanced format specifications, like fill and alignment, are provided in a later section.'''

num = 5009
letter = 'a'
print(f'{num:d}') # decimal presentation
print(f'{num:,d}') # adds commas to integers
print(f'{num:08d}') #precedes number with 0000 making full number 8 digits
print(f'{num:b}') # prints binary version 1001110010001
num = 3100
print(f'{num:x}') # hexadecimal in lowercase
print(f'{num:X}') # hex in upper
print(f'{num:e}') # exponent notation
print(f'{num:f}') # fixed point notation 6th place
print(f'{num:.2f}') # fixed point notation programmer defined
print(f'{num:,.2f}') # fixed point notation programmer defined with commas



