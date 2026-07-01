print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# if condition:
    #pass - Code to execute if condition is true

# if condition:
    #pass 
# else:
    #pass

# if condition:
    #pass
# elif condition2:
    #pass
# else:
    #pass

age = int(input('Enter your age: '))
if age >= 18:
    print('You are an adult')
elif age>= 13:   # you can use as many of the elif statements as you want
    print('You are a teenager')
else:
    print('You are a minor, come back when you are an adult')


#more elif examples
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant

is_citizen = True
age = 25

#multiple if conditions

if is_citizen: #first if
    if age >= 18: #second if
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

# getting boolean values
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True non-zero numbers, and non-empty strings are truthy

is_citizen = True
age = 25
# and operator
print(is_citizen and age) # using and operator

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

age = 19
is_employed = False
# or operator returns first true ignores second if first is true if first is false it checks second
print(age or is_employed) # prints 19

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

# not operator 

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

    age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can watch the movie.")
else:
    print("You can't watch the movie.")