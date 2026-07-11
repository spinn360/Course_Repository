num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        count = num // 5
        for i in range(count):
            print('*', end=' ')
        print('\n')

print('Goodbye.')

#prints an asterisk for every 5 in the number entered by the user