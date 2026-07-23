# Read input and split input into tokens
tokens = input().split()

measurements_list = []
for token in tokens:
    measurements_list.append(int(token))

print(f'All data: {measurements_list}')

sum_passed = 0
for pos, element in enumerate(measurements_list):
    if pos % 2 == 0 and element >= 40:
        print(f'Index {pos}: value is {element}')
        sum_passed += element

print(f'Sum of selected elements is: {sum_passed}')