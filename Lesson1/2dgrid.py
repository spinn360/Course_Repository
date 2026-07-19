grid_size = int(input())

grid_2d = []
for m in range(grid_size):
    row = []
    for n in range(grid_size):
        row.append(':')
    grid_2d.append(row)

# Loop through every row index (m)
for m in range(grid_size):
    print(f"\n--- Starting Row m = {m} ---")
    
    # Loop through every column index (n) inside that row
    for n in range(grid_size):
        print(f"  Checking Column n = {n}: Is {m} <= {n}?")
        
        if m <= n:
            print(f"    Yes! Changing grid_2d[{m}][{n}] to '$'")
            grid_2d[m][n] = '$'
        else:
            print(f"    No. Leaving grid_2d[{m}][{n}] alone.")

for row in grid_2d:
    for cell in row:
        print(cell, end='')
    print()


