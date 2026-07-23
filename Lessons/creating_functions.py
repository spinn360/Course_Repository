def calc_pizza_area():
    pi_val = 3.14159265

    pizza_diameter = 12.0
    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    return pizza_area

print(f'{12:.1f} inch pizza is {calc_pizza_area():.3f} square inches')

def get_face():
   face_char = 'o   o\n  o\nooooo'
   return face_char
	
print('Say cheese!')
	
print(get_face())
	
print('Did it turn out ok?')


def compute_square(num_to_square):
    return num_to_square * num_to_square


num_squared = compute_square(7)

print(f'7 squared is {num_squared}')

def get_minutes_as_hours(orig_minutes):

    return orig_minutes / 60

minutes = float(input())
print(get_minutes_as_hours(minutes))
def change_values(x,y):
    return x + y

print(change_values(4,3))

def change_value(x, y):
    result = x + y
    return result

print(change_value(2, 4))


def compute_val(x):
    return x * 6.6

input_value = float(input())

print(f'{compute_val(input_value):.2f}')

def calculate_num(x, y):
    return (x+y)*5

value_in1 = int(input())
value_in2 = int(input())

print(calculate_num(value_in1, value_in2))

def print_menu():
    print("Today's Menu:")
    print('   1) Gumbo')
    print('   2) Jambalaya')
    print('   3) Quit\n')

quit_program = False

'''while not quit_program :
    print_menu()
    choice = int(input('Enter choice: '))
    if choice == 3 :
        print('Goodbye')
        quit_program = True
    else :
        print('Order: ', end='')
        if choice == 1 :
            print('Gumbo')
        elif choice == 2 :
            print('Jambalaya')
        print()'''

def print_points(name, age, total_points):
    print(f'{name} is {age}')
    print(f'{name} made {total_points} points')

user_name = 'May'
user_age = 22
regular_time_points = 22
overtime_points = 7

print_points(user_name, user_age, regular_time_points + overtime_points)
