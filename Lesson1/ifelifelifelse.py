'''If input_year is in the inclusive range:

1940 - 1949, output 'The 40s'.
1950 - 1959, output 'The 50s'.
1960 - 1969, output 'The 60s'.
Otherwise, output 'Outside the range of study'.'''

input_year = int(input('Enter year between 1940 and 1969: '))

if input_year >= 1940 and input_year < 1950:
    print('The 40s')
elif input_year >= 1950 and input_year < 1960:
    print('The 50s')
elif input_year >= 1960 and input_year < 1970:
    print('The 60s')
else:
    print('Outside the range of study')