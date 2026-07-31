''' Type your code here. '''
word = input()
stripword = word.strip(' ') # removes any leading or trailing spaces from the string.

newword = stripword.replace(' ', '') # removes any extra spaces in between words.
# ADDITIONAL STEPS COULD INCLUDE MAKING THE WORD ALL UPPER OR ALL LOWER BEFORE COMPARING IT WITH ITS REVERSE.

if newword[::-1] == newword:
    print(f'palindrome: {word}')
else:
    print(f'not a palindrome: {word}')