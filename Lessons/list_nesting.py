my_list = [
    ['a','b'],
    ['c','d'],
    ['e','f']
    ]
print(f'My first nested list contains {my_list[0][0]} and {my_list[0][1]}')
print(f'My 2nd nested list contains {my_list[1][0]} and {my_list[1][1]}')
print(f'My 3rd nested list contains {my_list[2][0]} and {my_list[2][1]}')
#nested for loop for nested lists
for row in my_list:
    for cell in row:
        print(cell, end=' ')
    print()

nums = [
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1],
    [
        [12,13,14],
        [16,17,18]
    ]
]

for row in nums:
    for cell in row:
        print(cell, end=' ')
        if cell is list:
            for cells in cell:
                print(cells, end=' ')
            print()
print()        
# Your list structure based on the description
mixed_list = [
    [1, 2, 3],                 # 1st nested list (contains numbers)
    [4, 5, 6],                 # 2nd nested list (contains numbers)
    [[7, 8, 9], [10, 11, 12]]  # 3rd nested list (contains 2 MORE lists)
]

# Iterate through the main outer list
for row in mixed_list:
    
    # Check if the first item inside this row is ANOTHER list
    if isinstance(row[0], list):
        # If it is, we need to loop one level deeper
        for inner_row in row:
            for num in inner_row:
                # Print each number with spacing, but stay on the same line
                print(f'{num:<4}', end='') 
            print() # Move to the next line after finishing the inner row
            
    else:
        # If it's not a list, it's just regular numbers, so print them normally
        for num in row:
            print(f'{num:<4}', end='')
        print() # Move to the next line after finishing the row