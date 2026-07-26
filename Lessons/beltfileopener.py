'''A file's name is read from input. The file is opened and belt_file is assigned with the file object. Each line in belt_file contains a name and a color, representing a person's name and the color of the person's belt. Complete the assignment of belt_data by reading belt_file's contents as a list of strings, where each string is a line in belt_file.

Click here for example
Ex: If the input is data1.txt and:

Contents of file data1.txt
Del gray
Eve red
Mia tan
Zoe sienna

Contents of file data2.txt
Fay ochre
Pat maroon

Contents of file data3.txt
Pat indigo
Jan gold
Eli magenta

then the output is:

['Del gray\n', 'Eve red\n', 'Mia tan\n', 'Zoe sienna']

'''
belt_file = open(input())

belt_data = belt_file.readlines()

belt_file.close()

print(belt_data)