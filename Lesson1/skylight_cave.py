cave_size = 4
# Creates a 4x4 grid of darkness
cave_wall = [
    ['#', '#', '#', '#'],
    ['#', '#', '#', '#'],
    ['#', '#', '#', '#'],
    ['#', '#', '#', '#']
]

# Write your nested for loops using range() here!
for r in range(cave_size):
    for c in range(cave_size):
        if r < c:
            cave_wall[r][c] = '*'


# This prints your cave wall nicely when you are done
for row in cave_wall:
    for rock in row:
        print(rock, end=' ')
    print()