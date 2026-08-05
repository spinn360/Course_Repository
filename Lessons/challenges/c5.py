'''
Challenge 5: 
String Slicing & FormattingBased on: Taking a raw 9-digit 
integer and formatting it into a string with hyphens using 
string slicing.  Your Task:Write a script that accepts a 
10-digit integer representing a vehicle part number 
(e.g., 5551234567). Convert it into a string and use 
slicing to format and print it with hyphens like this: 
555-123-4567.
'''
userinput = int(input())
strinput = str(userinput)
print(f'{strinput[:3]}-{strinput[3:6]}-{strinput[-4:]}')