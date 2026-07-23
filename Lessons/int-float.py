my_int_1 = 56
my_int_2 = -4

print(type(my_int_1), my_int_1)
print(type(my_int_2), my_int_2)

sum_ints = my_int_1 + my_int_2
print(f'Integer Addition: {my_int_1} + {my_int_2} = {sum_ints}')
diff_ints = my_int_1 - my_int_2
print(f'Integer Subtraction: {my_int_1} - {my_int_2} = {diff_ints}')

int1 = 12
int2 = 4

product_ints = int1 * int2
print(f'Integer MultiplicationL {int1} x {int2} = {product_ints}')

divint1 = 56
divint2 = 12
divintss = divint1 / divint2
print(f'Division: {divint1} / {divint2} = {divintss}')

print(f'the variable class is no longer an integer, it is a {type(divintss)}')

myFloat1 = 5.4
myFloat2 = 12.0

floatAdd = myFloat1 + myFloat2
print(f'{myFloat1} + {myFloat2} = {floatAdd}')

print(f'{myFloat1} - {myFloat2} = {myFloat1 - myFloat2}')
print(f'{myFloat2} / {myFloat1} = {myFloat2/myFloat1}')
print(f'Modulo floats 56.9 % 12.9 = {56.9 % 12.9}')
print(f'Modulo Ints 56 % 12 = {56 % 12}')
print(f'Floor division ints: 56 // 12 = {56 // 12}')
print(f'Floor division floats: 12 // 5.4 = {12 // 5.4}')
print(f'Int Exponentiation: 56 to the power of 12 {56 ** 12}')
print(f'Float Exponentiation: 5.4to the power of 12 {5.4 ** 12}')
print(f'float 5.6 converted to int becomes {int(5.6)} \nwhile an int 5 to a float becomes {float(5)}')
print(f'4.798 rounded becomes {round(4.798)} using just round')
print(f'4.798 rounded becomes {round(4.798, 1)} using round, 1')
print(f'-4.798 abs (absolute value) becomes {abs(-4.798)}')
print(f'2 to the power of 3 = {pow(2,3)} --w/ pow(2,3)')
print(f'2 to the power of 3 = {pow(2,3,5)} --w/ pow(2,3,5)') # (2 ** 3) % 5
