start_range = int(input('Enter a start range: '))
end_range = int(input('Enter an end range: '))

count = 0
for i in range(start_range):
    for j in range(end_range):
        count += 1

print(f'Inner loop ran {count} times')

in_num = int(input('Enter a number: '))

for i in range(1, in_num + 1):
    print(str(i) + ('=' * i))