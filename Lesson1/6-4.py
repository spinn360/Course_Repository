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
endswithg = greet.endswith('greeting!!')
print('it is also', endswithg, 'that it ends wtih greeting!!')
print('it is', greet.endswith('goodbye'),'that it ends in goodbye')

# unicode

val = input('enter a single letter to get unicode number: ')
print(ord(val))
print('Beth\\\nRudy\\nPaul\nJen')
print("here is a quote 'to be or not to be'")
print('new line \n new line \n new line \n ignore escape sequence \\\\')
print('jimmy\tjohnny\tbob\tgeorge')

vegetable_input = input('Enter vegetable: ')

# Modify the string literal below
my_list = "Amy's vegetables:\nOkra\tCorn\t"

print(my_list, end="")
print(vegetable_input)