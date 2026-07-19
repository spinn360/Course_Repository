# Read input and split input into tokens
tokens = input().split()

temperature_samples = []
for token in tokens:
    temperature_samples.append(int(token))

print(f'All data: {temperature_samples}')

''' Your code goes here '''
all_good = True
for pos, temp in enumerate(temperature_samples):
    if pos % 2 != 0:
        print(f'Sample at index {pos} is {temp}')
        if temp >= 55:
            all_good = False
        
if all_good:
    print('All integers at odd indices are less than 55.')
else:
    print('At least one integer at an odd index is greater than or equal to 55.')