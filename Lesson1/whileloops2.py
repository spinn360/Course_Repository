nose = 'o'

user_input = input('Enter a character ("q" for quit): ')
user_value = user_input[0]

while user_value != 'q':
    print(f' {user_value} {user_value} ')
    print(f'  {nose}  ')
    print(user_value * 5)
    print('\n')
    
    user_input = input('Enter a character ("q" for quit): ')
    user_value = user_input[0]

print('goodbye!')