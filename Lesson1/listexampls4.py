# Read input and split input into tokens
tokens = input().split()

data_list = []
for token in tokens:
    data_list.append(int(token))

print(f'Raw samples: {data_list}')

failed_samples = 0

for pos, data in enumerate(data_list):
    if data >= 35:
        print(f'{data} at index {pos} passed')
    else:
        print(f'{data} at index {pos} failed')
        failed_samples += 1

print(f'Total failed samples: {failed_samples}')