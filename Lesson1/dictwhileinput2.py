patients_data = {'Eve': 9, 'Dan': 23, 'Fay': 14}

''' Your code goes here '''
key = input()
while key != 'stop':
    if key in patients_data:
        del patients_data[key]
    else:
        print(f'{key} not a key')
    key = input()

print('Updated patients data:')
print(patients_data)