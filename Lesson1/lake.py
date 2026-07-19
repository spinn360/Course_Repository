lake_size = 3
# Creates a 3x3 grid of water
lake = [
    ['~', '~', '~'],
    ['~', '~', '~'],
    ['~', '~', '~']
]

# Write your nested for loops here!
for m in range(lake_size):
    for n in range(lake_size):
        if m == n:
            lake[m][n] = 'f'

# This prints your lake nicely when you are done
for row in lake:
    for water in row:
        print(water, end=' ')
    print()