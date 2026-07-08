i = 10
while i > 0:
    print(i)
    i -= 1
    
curr_power = 2
user_char = 'y'

while user_char == 'y':
    print(f'Current Power: {curr_power}')
    user_char = input('Do you want to continue? (y/n): ')
    curr_power *= 2
print('You have exited the loop.')