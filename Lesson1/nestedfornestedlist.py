tictactoe = [
    ['o','x','-'],
    ['o','o','o'],
    ['o','x','o']
]
o = 0
x = 0
for r in tictactoe:
    for c in r:
        if c == 'o':
            o += 1
        elif c == 'x':
            x += 1
if o == 3:
    print('o wins')
if x == 3:
    print('x wins')


        

# The board is 3x3, so we use range(3) to generate indices 0, 1, and 2
for col_index in range(3):
    o_count = 0
    
    # Inner loop moves down the rows while staying in the same column
    for row_index in range(3):
        # We check the specific coordinate [row][column]
        if tictactoe[row_index][col_index] == 'o':
            o_count += 1
            
    # After checking the whole column, see if we found 3
    if o_count == 3:
        print('Winner! (Vertical)')

# Check each row
for row in tictactoe:
    o_count = 0 
    for cell in row:
        if cell == 'o':
            o_count += 1
            
    # After checking the whole row, see if we found 3
    if o_count == 3:
        print('Winner! (Horizontal)')

if tictactoe[0][0] == 'o' and tictactoe[1][1] == 'o' and tictactoe[2][2] == 'o':
    print('Winner! (Diagonal)')