# logical if statements for assigning table size to group size at a restaraunt

party_size = int(input('How many? '))
if party_size > 1 and party_size < 3 :
    print('you get a small table')
elif party_size >=3 and party_size < 10:
    print('You get a large table')
elif party_size >= 10 and party_size < 25:
    print('We will move two large tables together for you')
elif party_size >= 25:
    print('Looks like we will be booking you an entire room')
else:
    print('Counter seating for you')

    ''' correct statement requires correct formatting
if condition:
    result
elif condition:
    result
else:
    result

    do not have elif with same spacing as result and be sure to include : after
    condition
    '''