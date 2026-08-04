import csv

user_input = input()
caves = {}
with open(user_input, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        time = line[0]
        name = line[1]
        location = line[2]

        if name not in caves:
            caves[name] = {'location': location, 'time' : [time]}
        else:
            caves[name]['time'].append(time)
for name, innerdict in caves.items():
    display_cave = name[:28]
    cave_time_str = ' '.join(innerdict['time'])
    caveloc = innerdict['location']

    print(f'{display_cave:<28} | {caveloc:>12} | {cave_time_str}')
