patients_record = {}

''' Your code goes here '''
key_string = input()
while key_string != 'done':
    key, value = key_string.split()
    patients_record[key] = int(value)
    key_string = input()

print('Patients record:')
print(patients_record)