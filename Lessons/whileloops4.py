result = 0
num_input = int(input('enter any positive number or (enter -1 to quit)'))

while num_input >=0:
    if num_input  % 4 == 0:
        print('lose')
    else:
        print('win')
        result += 1
    num_input = int(input())

print(f'Result of wins is {result}')