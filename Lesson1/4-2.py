
#  single and double quotes are treated equal
my_str_1 = 'Hello'
my_str_2 = "World"

print(my_str_1,my_str_2)

# fstring to print out Hello World
print(f"{my_str_1} {my_str_2}")


# Triple quote to create multiline strings
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
print(my_str_3)
print("  ")
print(my_str_4)

# creating strings with quotes in them use opposing quotes to wrap or use \
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
print(msg, "\n", quote) # produces a space from comma after new line
print(msg, "\n" + quote) # does not produce space from + after new line
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(msg, "\n" + quote) 

# searching in a string
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

#getting length using len() fuction


print(len(my_str))  # returns 11

# get specific letters from index of string 

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1])  # d
print(my_str[-2]) # l

# mutable and immutable strings in python

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# greeting[0] = 'H' -- this will end in TypeError: 'str' object does not support item assignment
