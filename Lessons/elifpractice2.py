# alternate way to output same results as elifpractice.py

num_years = int(input('Enter years married: '))
if num_years < 1:
    print('Congrats')
elif num_years  < 2:
    print('newlyweds')
elif num_years  < 25:
    print('You keep going')
elif num_years <50:
    print("Silver")
elif num_years < 1000:
    print('Gold')
