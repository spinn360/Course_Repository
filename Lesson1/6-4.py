#strings

greet = 'Hello this is \n a normal string \n greeting!!'
print(greet)
greetraw = r'Hello this is \n a raw string \n greeting!!' # ignores escape sequence
print(greetraw)


print(greet.upper(), 'capitalized')
print(greet.lower(), 'lowercased')
spacegreet = '    Hello this is \n a space before and after \n greeting!!    '
print(spacegreet)
print(spacegreet.strip(), 'spaces removed')
print(spacegreet.upper().strip(), 'spaces removed and uppercased')
print(spacegreet.replace('Hello', 'Hi'), 'hello replaced with hi')

print(greet.split(), 'SPLIT APART')
greetsplit = greet.split() # splits the string into a list of each word
print(greetsplit)
print(' '.join(greetsplit), 'joined back together from the split list') #joins a list with the ' ' as the seperator
startsWithHello = greet.startswith('Hello') #checks the string starts with 'Hello' 
print('it is',startsWithHello,'that the strings starts with Hello')