#calculate the GCD (greatest common divisor) of two positive integers using the Euclidean algorithm

num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
        print(f'num_a is now {num_a}')
    else:
        num_b = num_b - num_a
        print(f'num_b is now {num_b}')

print(f'GCD is {num_a}') 
