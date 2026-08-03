import csv

user_input = input()
with open(user_input, 'r') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',')
    for row in my_reader:
        print(f"{row[0]:<12} | {row[1]:<20} | {row[2]:>5}")
# #printing the numbers from 1 to 5 using a while loop
# i = 1
# while