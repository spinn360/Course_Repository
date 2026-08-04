import csv

user_input = input()
moviedatabase = {}
with open(user_input, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        time = line[0]
        title = line[1]
        theater = line[2]

        if title not in moviedatabase:
            moviedatabase[title] = {'time': [time], 'theater': theater}
        else:
            moviedatabase[title]['time'].append(time)

for title, innerdict in moviedatabase.items():
    display_movie = title[:25]
    movie_time_str = ' '.join(innerdict['time'])
    theaterloc = innerdict['theater']
    print(f'{display_movie:<25} | {theaterloc:>18} | {movie_time_str}')
