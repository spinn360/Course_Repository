'''
def print_region_capital(capital_name, region_name):
    print(f"{capital_name} is {region_name}'s capital.")

cap1 = input()
cap2 = input()
reg1 = input()
reg2 = input()


print_region_capital(cap1, reg1)
print_region_capital(cap2, reg2)



def mph_and_minutes_to_miles(mph, mt):
    return (mt / 60.0) * mph
    

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')


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


LITERS_TO_CUPS = 4.22675

def convert_to_cups(liters):
    
    return liters * LITERS_TO_CUPS

user_liters = int(input())
  
# Print with value rounded to 3 decimal places  
print(f'The number of cups is {convert_to_cups(user_liters):.3f}')



MILLILITERS_PER_TABLESPOON = 14.7868
TABLESPOONS_PER_FLUID_OUNCE = 2

def convert_to_milliliters(ounces,tablespoons):
    return ((ounces * TABLESPOONS_PER_FLUID_OUNCE) + tablespoons) * MILLILITERS_PER_TABLESPOON
   
num_fluid_ounces = int(input())
num_tablespoons = int(input())

# Print with value rounded to 3 decimal places  
print(f'{convert_to_milliliters(num_fluid_ounces, num_tablespoons):.3f} milliliters')




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