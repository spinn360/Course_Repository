import csv

user_input = input()
classes = {}

with open(user_input, 'r') as csvfile:
    myreader = csv.reader(csvfile, delimiter = ',')
    for row in myreader:
        classtime = row[0]
        classname = row[1]
        classroom = row[2]

        if classname not in classes:
            classes[classname] = {'classroom': classroom, 'time':[classtime]}
        else:
            classes[classname]['time'].append(classtime)
for classname, data in classes.items():
    display_class = classname[:30]
    class_time_str = " ".join(data['time'])
    classroom = data['classroom']
    print(f'{display_class:<30} | {class_time_str:>6} | {classroom}')
import csv
from collections import defaultdict

