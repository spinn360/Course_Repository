string = 'Music/artist/song.mp3'
my_tokens = string.split('/') #delimiter of / default is a space
print(my_tokens)

string = 'Music artist song.mp3'
my_tokens = string.split()  #default delimiter
print(my_tokens)
##########################################################
'''url = input('Enter URL:\n')

tokens = url.split('/')  # Uses '/' separator
print(tokens)
'''
##########################################################
mystr = 'I scream you scream we all scream for icecream!'
print(mystr)
print('mystr seperated by scream')
icecream = mystr.split('scream')
print(icecream)
separator = ' scream ' # variable to be used in the join newstr
newstr = separator.join(icecream)  # this concatenates the strings together using whatever value is in separator variable
print('newstr joined by separator scream')
print(newstr)

###########################################################
#Both of the following do the same but the latter is more effecient

phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''
for phrase in phrases:
    sentence += phrase 
print(sentence)

##################
#Easier Better way
##################

phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''.join(phrases)
print(sentence)
#do not need to actually create a variable# ''.join() instead of separator = ''
#'' empty string no spaces ' ' space string if needed between words, but can be anything
##################################################################


path = 'C:/worker/testing/words.document.doc'

new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(new_separator.join(tokens))