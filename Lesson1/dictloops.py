my_dict = {'tamagachi': 'game', 'gogo': 'adventure'}
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
num_caloris = dict(coke=90, coke_zero =0, pepsi= 94)
for soda, calories in num_caloris.items():
    print(f'{soda}: {calories}')

#converting a dictionary view into a list to sort it

solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list
# note values only
list_of_planets = list(solar_distances.keys())
print(list_of_planets)
print(list_of_distances)
sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]


for keys, values in solar_distances.items():
    if values == closest:
        print(f'Closest planet is {keys} at {closest:.4e}')
    if values == next_closest:
        print(f'Second closest planet is {keys} at {next_closest:.4e}')


room_temperatures = {}

input_line = input()
while input_line != 'exit':
    room_number, temp = input_line.split()
    room_temperatures[int(room_number)] = float(temp)
    input_line = input()

''' Your code goes here '''
list_temps = list(room_temperatures.values())
sorted_temps = sorted(list_temps)

for vals in sorted_temps:
    print(vals)
