#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file ("input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements
import csv

#accept string input identifying filename
print("Enter the name of the file along with its extension:")
file_name = input()

#open, read, and output the new file contents in the reverse order
with open(file_name, 'r') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')
           #open csv file
    for row in file_reader:
        reversed_row = row[::-1]
        print(reversed_row)
