#concatination
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# do not use + with string and integer or error
# you can however convert to a string first

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

#+= add to a string while assigning new value to string variable

name_and_age = 'John Doe'
name_and_age += str(age)

print(name_and_age)


# Using fStrings

name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
# when using Fstring you don't have to assign variables to string it is automatic
