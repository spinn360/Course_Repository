letter1 = 'a'
letter2 = '?'
letter3 = '?'
letter4 = '?'
search = input('Enter a 4-letter word to search for: ')
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        letter3 = 'a'
        while letter3 <= 'z':  # Inner loop
            letter4 = 'a'
            while letter4 <= 'z':  # Inner loop
                
                # Create the list and join it immediately
                lista = [letter1, letter2, letter3, letter4]
                word = ''.join(lista)
                
                if word == search:
                    print(f'Found {word}')
                #else:
                 #   print(f'Not found {word}')
                letter4 = chr(ord(letter4) + 1)
            letter3 = chr(ord(letter3) + 1)
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)
    
    # brute force search for the word
    