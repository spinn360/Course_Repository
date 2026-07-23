hourly_wage = 20

print('Annual salary is: ')
print(hourly_wage * 40 * 50)
print()

print('Monthly salary is: ')
print(((hourly_wage * 40 * 50) / 12)) #previously /1
print()

# FIXME: The above is wrong. Change 
#        the 1 so that the statement
#        outputs monthly salary.


print('Enter your program here')
program = input()
print("Wow you entered", program)

print("Enter hello.txt:")
# Get the name of the input file
input_file_name = input()

# Open the input file
f = open(input_file_name)

# Print contents of input file
for line in f:
    print(line)

# Close the input file
f.close()