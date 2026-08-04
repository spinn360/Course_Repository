#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence
#accept input identifying filename
print("Enter the name of the input file:")
filename = input()

#open, read, and write text file (e.g., "WordTextFile.txt") using open(), read(), write()
with open(filename, 'r') as f:
    words = f.readlines()

newsentence = words[0].strip() + ' ' + words[1].strip() + ' ' + words[2].strip()    
#open and write sentence to end of file
with open(filename, 'a') as f:
    f.write('\n' + newsentence)
 
#open, read, and output the updated file contents 
with open(filename, 'r') as f:
    newwords = f.readlines()
for words in newwords:
    print(words, end='')
print()
