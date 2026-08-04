import csv

user_input = input()
offroad = {}

with open(user_input, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        time = line[0]
        trail = line[1]
        location = line[2]

        if trail not in offroad:
            offroad[trail] = {'location' : location, 'time':[time]}
        else:
            offroad[trail]['time'].append(time)

for trails, innerdict in offroad.items():
    display_trail = trails[:26]
    time_str = ' '.join(innerdict['time'])
    location = innerdict['location']
    print(f'{display_trail:<26} | {location:>15} | {time_str}')