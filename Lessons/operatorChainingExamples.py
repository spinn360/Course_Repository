user_grade = int(input('Enter School year 1-12: '))

if 9 <= user_grade <= 12:
    print('In high school')
elif 6 <= user_grade <=8:
    print('In middle school')
elif 1<= user_grade <= 5:
    print('In elementary school')
else:
    print('not in 1st through 12 grade')

a = int(input('Enter a number: '))
if 5 <= a <= 15:
    print('the # is between 5 and 15')
else:
    print('The number is not between 5 and 15')
# just an if elif elif else

num_coats = int(input('Enter number of coats you own: '))

if num_coats <= 0:
    print('Invalid number')
elif num_coats < 9:
    print('Mid-sized coat closet')
elif num_coats <29:
    print('Walk-in coat closet')
else:
    print('Too many coats')


scammer = int(input('Enter amount stolen: '))

if scammer <= 0: 
    print('You didn\'t get scammed')
else: # scammer 
    print(f'You got scammed ${scammer}')
