import csv

# Type your code here. 
file = input()
words = {}
with open(file, 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        for word in row:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

for word, count in words.items():
    print(f'{word} - {count}')
