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
