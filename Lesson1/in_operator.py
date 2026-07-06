prices = ['$20', 15, 5]
print(15 in prices)
# prints output: True
print(14 in prices)
# prints False

# Use the "in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print(f'Found {name} on the roster.')
else:
    print(f'Could not find {name} on the roster.')
# checks if found and prints found or not found using in operator
if name not in barcelona_fc_roster:
    print(f'Could not find {name} on the roster.')
else:
    print(f'Found {name} on the roster.')
# same check using not in operator


# check substrings
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')

#Checking keys in a string NOTE does not check values
my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
   print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')