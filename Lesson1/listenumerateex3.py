# Read input and split input into tokens
tokens = input().split()

data_values = []
for token in tokens:
    data_values.append(int(token))

print(f'Sequence: {data_values}')

min_diff = None

for i, val in enumerate(data_values):
    if i > 0:
        prev_val = data_values[i-1]
        neighbor_diff = prev_val - val
        print(f'{prev_val} - {val} = {neighbor_diff}')
        
        if min_diff == None or neighbor_diff < min_diff:
            min_diff = neighbor_diff

print(f'The smallest difference between two neighboring values is {min_diff}')