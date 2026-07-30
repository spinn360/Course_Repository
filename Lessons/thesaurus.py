synonyms = {}

# input a filename
word_input = input()
# input a letter 
letter_input = input()
with open(word_input + '.txt', 'r') as f:
    for line in f:
        syn_list = line.split()
        
        if syn_list:
            first_letter = syn_list[0][0]
            synonyms[first_letter] = syn_list
if letter_input in synonyms:
    for synonym in synonyms[letter_input]:
        print(synonym)
else:
    print(f'No synonyms for {word_input} begin with {letter_input}.')

