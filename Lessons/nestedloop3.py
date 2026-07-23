c1 = 'a'
while c1 < 'b':
    c2 = 'a'
    while c2 <= 'c':
        print(f'{c1}{c2}', end = ' ')
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)


i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}', end=' ')
        i2 = i2 + 3
    i1 = i1 + 10

print()
    
i = 3
while i < 18:
    j = 5
    while j <= 12:
        print(f'{i}{j}')
        j = j + 4
    i = i + 14
    
print()

i = 1
while i < 23:
    j = 2
    while j <= 11:
        print(f'{i}{j}')
        j = j + 3
    i = i + 12
    
print()
num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    for j in range(num_cols):
        print('*', end=' ') 
    print()

num_rows = int(input())
num_cols = int(input())

# Outer loop controls the number of rows
for i in range(num_rows):
    # Inner loop controls the number of columns (stars per row)
    for j in range(num_cols):
        print('*', end=' ')
    # Move to the next line after printing all columns in the current row
    print()
    
num_rows = int(input())
num_columns = int(input())

# Step 1: Outer loop for rows, starting at 1
for current_row in range(1, num_rows + 1):
    
    # Step 2: Initialize the column letter to 'A'
    current_column_letter = 'A'
    
    # Step 3: Inner loop for columns, starting at 1
    for current_column in range(1, num_columns + 1):
        
        # Print the seat label (e.g., 1A) followed by a space
        print(f'{current_row}{current_column_letter}', end=' ')
        
        # Increment the letter to the next one in the alphabet (A -> B -> C)
        current_column_letter = chr(ord(current_column_letter) + 1)
        
    # Print a newline at the end of each row
    print()