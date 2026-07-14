'''
def print_region_capital(capital_name, region_name):
    print(f"{capital_name} is {region_name}'s capital.")

cap1 = input()
cap2 = input()
reg1 = input()
reg2 = input()


print_region_capital(cap1, reg1)
print_region_capital(cap2, reg2)

'''
'''
def mph_and_minutes_to_miles(mph, mt):
    return (mt / 60.0) * mph
    

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')
'''
'''
CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12

def height_US_to_cm(feet, inches):
   """Converts height in feet/inches to centimeters"""
   total_inches = feet * INCHES_PER_FOOT + inches
   cm = total_inches * CM_PER_INCH
   return cm
feet = 6
inches = 1

centimeters = height_US_to_cm(feet, inches)
print(f'Centimeters: {centimeters}')
'''
'''
def c_to_f(c):
    f= c * 9 / 5 +32
    return  f

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

# FIXME: Call conversion function
temp_f = c_to_f(temp_c)
# temp_f = ??

# FIXME: Print result
print(f'Fahrenheit: {temp_f}')
# print(f'Fahrenheit: {temp_f}')
'''

'''
def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

print(f'max_sum is: {max_sum}')
'''
'''
import math

def calc_circular_base_area(radius):
   return math.pi * radius * radius

def calc_cylinder_volume(baseRadius, height):
   return calc_circular_base_area(baseRadius) * height

def calc_cylinder_surface_area(baseRadius, height):
   return (2 * math.pi * baseRadius * height) + (2 * calc_circular_base_area(baseRadius))

radius = float(input('Enter base radius: '))
height = float(input('Enter height: '))

print(f'Cylinder volume: {calc_cylinder_volume(radius, height):.3f}')
print(f'Cylinder surface area: {calc_cylinder_surface_area(radius, height):.3f}')
'''
'''
LITERS_TO_CUPS = 4.22675

def convert_to_cups(liters):
    
    return liters * LITERS_TO_CUPS

user_liters = int(input())
  
# Print with value rounded to 3 decimal places  
print(f'The number of cups is {convert_to_cups(user_liters):.3f}')
'''

'''
MILLILITERS_PER_TABLESPOON = 14.7868
TABLESPOONS_PER_FLUID_OUNCE = 2

def convert_to_milliliters(ounces,tablespoons):
    return ((ounces * TABLESPOONS_PER_FLUID_OUNCE) + tablespoons) * MILLILITERS_PER_TABLESPOON
   
num_fluid_ounces = int(input())
num_tablespoons = int(input())

# Print with value rounded to 3 decimal places  
print(f'{convert_to_milliliters(num_fluid_ounces, num_tablespoons):.3f} milliliters')

'''

'''
def compute_base_area(length, width):
    return length * width
def compute_vol(length, width, height):
    v = compute_base_area(length, width) * height
    return v
prism_base_length = float(input())
prism_base_width = float(input())
prism_height = float(input())

print(f'Prism base length: {prism_base_length}')
print(f'Prism base width: {prism_base_width}')
print(f'Prism height: {prism_height}')
print(f'Base area: {compute_base_area(prism_base_length, prism_base_width):.1f}')
print(f'Volume: {compute_vol(prism_base_length, prism_base_width, prism_height):.1f}')
'''

'''
def get_user_num():
    print('FIXME: Finish get_user_num()')
    return -1
def compute_avg(a,b):
    print('FIXME: Finish compute_avg()')
    return -1

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print(f'Avg: {avg_result}')

'''

'''
def calc_ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and 
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print(f'eBay fee: ${calc_ebay_fee(selling_price)}')

'''

'''
size = 5

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers


def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:')

def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:')

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

def print_all_numbers(numbers):
    print('Numbers:', end=' ')
    for num in numbers:
        print(num, end=' ')
    print() # Adds a newline at the end

def print_odd_numbers(numbers):
    print('Odd numbers:', end=' ')
    for num in numbers:
        if num % 2 != 0: # Checks if the number is not perfectly divisible by 2
            print(num, end=' ')
    print()

def print_negative_numbers(numbers):
    print('Negative numbers:', end=' ')
    for num in numbers:
        if num < 0: # Checks if the number is less than zero
            print(num, end=' ')
    print()
nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)

'''

'''
def print_popcorn_time(ounces):
    if ounces < 3:
        print('Too small')
    elif ounces > 10:
        print('Too large')
    else:
        print(f'{6 * ounces} seconds')

bag_ounces = int(input())
print_popcorn_time(bag_ounces)

'''
'''
def find_lottery_prize(num):
    if num == 221 or num == 527:
        prize = 12500
    elif num == 776 or num == 916:
        prize = 6000
    else:
        prize = 0
    return prize

input_lottery_number = int(input())

print(f'Testing 221: {find_lottery_prize(221)}')
print(f'Testing user input: {find_lottery_prize(input_lottery_number)}')
'''
'''
def output_vals(num1, num2):
    for i in range(num2, num1 -1, -1):
        print(i, end=' ')

num1 = int(input())
num2 = int(input())

print('Testing static input: ')
output_vals(2, 5) #sends to defined function returns the range of 5 to 2 counting down
print(f'\nTesting user input: ')
output_vals(num1, num2) # sends to defined function which return the range of 2nd int to 1st int counting down
'''
'''
def print_human_head():
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return

def print_monkey_head():
    print('   .-"-.')
    print(' _/.-.-.\\_')
    print('( ( o o ) )')
    print(' |/  "  \\|')
    print('  \\ .-. /')
    print('  /`"""`\\')
    return

def print_figure(face):
    face()  # Print the face
    print('     |')
    print('   --|--')
    print('  /  |  \\')
    print('@    |    @')
    print('     |')
    print('    /|\\')
    print('   @   @')
    return

choice = int(input('Enter "1" to draw monkey, "2" for human: '))

if choice == 1:
    print_figure(print_monkey_head)
elif choice == 2:
    print_figure(print_human_head)'''




'''def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0
    
    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 10.0
print(f'{value_c} C is {celsius_to_kelvin(value_c)} K')

value_k = float(input())
print(f'{value_k} K is {kelvin_to_celsius(value_k)} C')

'''


'''def add_grade(student_grades):
    print('Entering grade. \n')
    name, grade = input(grade_prompt).split()
    student_grades[name] = grade

def delete_name():
    print('Deleting grade.\n')
    name = input(delete_prompt)
    del student_grades[name]

# FIXME: Create print_grades function
def print_grades():
    print('Printing grades.\n')
    for name, grade in student_grades.items():
            print(f'{name} has a {grade}.')

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
delete_prompt = "Enter name to delete:\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

command = input(menu_prompt).lower().strip()

while command != '4':  # Exit when user enters '4'
    if command == '1':
        add_grade(student_grades)
    elif command == '2':
        # FIXME: Only call delete_name() here
        delete_name()
    elif command == '3':
        # FIXME: Only call print_grades() here
        print_grades()
    else:
        print('Unrecognized command.\n')

    command = input().lower().strip()
'''

'''def calculate_future_age(age, future_years):
    print(f'Age in {future_years} years: {age + future_years}')

my_age = int(input())
num_years = int(input())

calculate_future_age(my_age,num_years)

print(f'Age now: {my_age}')
'''



'''def swap(list):
    newlist =list[:]
    #or new_var = list[0]
    list[0] = list[2]
    list[2] = newlist[0]
    #or list[2] = new_var

val_list = input().split()

swap(val_list)
print(val_list)
'''





'''def number_of_pennies(dollars=0,pennies=0):
    return (dollars * 100) + pennies

print(number_of_pennies(int(input('enter dollars: ')), int(input('enter pennies: '))),'pennies') # Both dollars and pennies
print(number_of_pennies(int(input('enter dollars: '))),"pennies")               # Dollars only
'''


'''
def split_check(bill = 1.0, people = 1, tax_percentage = 0.09, tip_percentage = 0.15):
    total = ((bill* tip_percentage) + bill)+ (bill * tax_percentage)
    return total / people'''


'''
def print_sandwich(bread, meat, *args): 
    print(f'{meat} on {bread}', end=' ') 
    if len(args) > 0: 
        print('with', end=' ') 
    for extra in args: 
        print(extra, end=' ') 
    print('')

print_sandwich('sourdough', 'turkey', 'mayo')
print_sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')
'''

'''

def print_sandwich(meat, bread, **kwargs):
    print(f'{meat} on {bread}')
    for category, extra in kwargs.items():
        print(f'   {category}: {extra}')
    print()

print_sandwich('turkey', 'sourdough', sauce='mayo')
print_sandwich('ham', 'wheat', sauce1='mustard', veggie1='tomato', veggie2='lettuce')'''

student_scores = [75, 84, 66, 99, 51, 65]

def get_grade_stats(scores):
    # Calculate the arithmetic mean
    mean = sum(scores)/len(scores)
    
    # Calculate the standard deviation
    tmp = 0
    for score in scores:
        tmp += (score - mean )**2
    std_dev = (tmp/len(scores))**0.5

    # Package and return average, standard deviation in a tuple
    return [mean, std_dev]

# Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)

print(f'Average score: {average}')
print(f'Standard deviation: {standard_deviation}')