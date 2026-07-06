x = int(input('Enter 1st whole number: '))
y = int(input('Enter 2nd whole number: '))
max = 0
if x > y:
    max = x
elif x == y:
    max = str(x) + ' which was the same value'
else:
    max = y
print(f'The higher number is {max}')
