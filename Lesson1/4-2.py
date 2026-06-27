
#single and double quotes are treated equal
my_str_1 = 'Hello'
my_str_2 = "World"

print(my_str_1,my_str_2)

#fstring to print out Hello World
print(f"{my_str_1} {my_str_2}")


#Triple quote to create multiline strings
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
print(my_str_3)
print("  ")
print(my_str_4)

#creating strings with quotes in them use opposing quotes to wrap
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
print(msg, "\n", quote) #produces a space from comma after new line
print(msg, "\n" + quote) #does not produce space from + after new line