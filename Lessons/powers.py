import math
from decimal import Decimal
"""Given three floating-point numbers x, y, and z, output x to the power of z,
 x to the power of (y to the power of z), the absolute value of (x minus y),
  and the square root of (x to the power of z)."""
''' Type your code here. '''
x = Decimal(input('input for x: '))
y = Decimal(input('input for y: '))
z = Decimal(input('input for z: '))


try:
    your_value1 = math.pow(x,z)
    your_value2 = math.pow(x, math.pow(y,z))
    your_value3 = math.fabs(x - y)
    your_value4 = math.sqrt(math.pow(x,z))
    print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')
except OverflowError:
    print("Overflow error occurred please input numbers under 4")



#unfortunately this will throw overflow errors if the numbers are too large hence the try block
