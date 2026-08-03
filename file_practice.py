filename = input('Enter the name of a file: ')


with open(filename, 'r') as f:
    words = f.readlines()
word1 = words[0].strip()
word2 = words[1].strip()
word3 = words[2].strip()
new_sentence = f'I need to watch {word1}, which is an {word2} anime. Priority: {word3}.'
#print(new_sentence)

with open(filename, 'a') as f:
    f.write('\n' + new_sentence + '\n')

with open(filename, 'r') as f:
    newwords = f.readlines()

for words in newwords:
    print(words, end='')