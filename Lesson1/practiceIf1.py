user_num = int(input('Enter whole number: '))

div_remainder = user_num %2
if div_remainder == 0:
    print(f'{user_num} is even.')
elif div_remainder == 1000:
    print('this is impossible') # 4 spaces
else:
    print(f'{user_num} is odd.')