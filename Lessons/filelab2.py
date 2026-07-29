#Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method
file_name = input("Enter the filename: ")
with open(file_name, 'r') as f:
    lines = f.readlines()
    #Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a Python list of TV shows are the values 
shows_dict = {}
for i in range(0, len(lines), 2):
    seasons = int(lines[i].strip())
    show = lines[i+1].strip()
    if seasons in shows_dict:
        shows_dict[seasons].append(show)
    else:
        shows_dict[seasons] = [show]

#sort by keys (greatest to least) and write to output_keys.txt
with open('output_keys.txt', 'w') as out_keys:
    for key in sorted(shows_dict.keys(), reverse=True):
        # join multiple shows with a semicolon and a space
        shows_str = '; '.join(shows_dict[key])
        out_keys.write(f'{key}: {shows_str}\n')
#sort by values (reverse alphabetical) and write to output_titles.txt
all_shows = []
# gather all the shows from dictionary values into a single list
for shows in shows_dict.values():
    all_shows.extend(shows)

# sort the entire list
all_shows.sort(reverse=True)
with open('output_titles.txt', 'w') as out_titles:
    for show in all_shows:
        out_titles.write(f'{show}\n')


    