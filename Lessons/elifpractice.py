num_years = int(input('Enter years married: '))
if num_years >=1 and num_years < 25:
    print('Newlyweds')
elif num_years >= 25 and num_years < 50:
    print("Silver")
elif num_years >= 50:
    print('Gold')
else:
    print('Congrats!')