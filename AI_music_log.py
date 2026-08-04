import csv
music_data = {}
user_input = input()

with open(user_input, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        gen_time = line[0]
        track_title = line[1]
        genre = line[2]

        if track_title not in music_data:
            music_data[track_title] = {'genre' : genre, 'gen_time' : [gen_time]}
        else:
            music_data[track_title]['gen_time'].append(gen_time)
#print(music_data)
for music, innerdict in music_data.items():
    display_title = music[:22]
    gen_time_str = ' '.join(innerdict['gen_time'])
    genre = innerdict['genre']
    print(f'{display_title:<22} | {genre:>14} | {gen_time_str}')