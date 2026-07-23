import math
z = 4.5
z = math.pow(math.floor(z), 2.0) # math.floor(z) returns 4. Then, math.pow(4, 2.0) returns 16.0.
print(z)
z = 15.75
z = math.sqrt(math.ceil(z)) # math.ceil(z) returns 16. Then, math.sqrt(16) returns 4.0
print(z)
z = 4
z = math.factorial(z) # 4 * 3 * 2 * 1 = 24
print(z)

x = math.sqrt(36.0)
print(x)
x = math.fabs(-6.7)
print(x)
x = math.pow(5.0, 3.0)
print(x)
x = math.fabs(-12.0 + 6.0)
print(x)
x = math.pow(4.0, math.sqrt(9.0))
print(x)



x1 = float(input('Enter x1 location: '))
y1 = float(input('Enter y1 location: '))
x2 = float(input('Enter x2 location: '))
y2 = float(input('Enter y2 location: '))

point_dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print(f'Points distance: {point_dist:.1f}')

v = float(input())
w = float(input())

val = v + math.sqrt(w)

print(f'{val:.1f}')  # Outputs val with 1 decimal place

w = float(input())
x = float(input())

val = math.sqrt(math.fabs(w+x)) # square root of absolute value (positive value)

print(f'{val:.2f}')  # Outputs val with 2 decimal places

b = float(input())
c = float(input())

val = math.pow((math.sqrt(b)),math.sqrt(c)) # square root of number to the power of square root of other number

print(f'val = {val:.1f}')  # Outputs val with 1 decimal place

h = float(input())
i = float(input())

answer = math.floor(h - (math.sqrt(i))) # square root of i subtracted from h and the rounded down to nearest whole


print(answer)


user_num = int(input())
div_num = int(input())
user_num1 = math.floor((user_num / div_num))
user_num2 = math.floor((user_num1 / div_num))
user_num3 = math.floor((user_num2 / div_num))
print(user_num1,user_num2,user_num3)