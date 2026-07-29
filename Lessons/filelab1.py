'''Write a program that first reads in the name of an input file, followed 
by two strings representing the lower and upper bounds of a search range. 
The file should be 
read using the file.readlines() method. The input file contains a 
list of alphabetical, ten-letter strings, each on a separate line. 
Your program should determine if the strings from the list are 
within that range (inclusive of the bounds) and output the results.
Ex: If the input is:

input1.txt
ammoniated
millennium
and the contents of input1.txt are:

aspiration
classified
federation
graduation
millennium
philosophy
quadratics
transcript
wilderness
zoologists
the output is:

aspiration - in range
classified - in range
federation - in range
graduation - in range
millennium - in range
philosophy - not in range
quadratics - not in range
transcript - not in range
wilderness - not in range
zoologists - not in range
Notes:

End the output with a newline.
'''



name = input('Enter file name: ')
'''
newfile = open(name, 'a+')
# write to file
#aspiration
#classified
#federation
#graduation
#millennium
#philosophy
#quadratics
#transcript
#wilderness
#zoologists
newfile.write('aspiration\n')
newfile.write('classified\n')
newfile.write('federation\n')
newfile.write('graduation\n')
newfile.write('millennium\n')
newfile.write('philosophy\n')
newfile.write('quadratics\n')
newfile.write('transcript\n')
newfile.write('wilderness\n')
newfile.write('zoologists\n')
newfile.close()
'''

lower_bound = input('Enter lower range: ')
upper_bound = input('Enter upper range: ')

with open(name, 'r') as file:
    words = file.readlines()

for word in words:
    clean_word = word.strip()

    if lower_bound <= clean_word <= upper_bound:
        print(f'{clean_word} - in range\n')
    else:
        print(f'{clean_word} - not in range\n')
