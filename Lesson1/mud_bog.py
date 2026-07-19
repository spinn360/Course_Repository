bog_size = 3
# Creates a 3x3 grid of mud
mud_bog = [
    ['~', '~', '~'],
    ['~', '~', '~'],
    ['~', '~', '~']
]

# Write your nested for loops using range() here!
for m in range(bog_size):
    for b in range(bog_size):
        if b == 1:
            mud_bog[m][b] = '='


# This prints your mud bog nicely when you are done
for row in mud_bog:
    for mud in row:
        print(mud, end=' ')
    print()