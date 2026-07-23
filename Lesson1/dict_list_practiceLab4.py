''' Type your code here. 
namenumber = input()
firstlist = [word for word in namenumber.split()]
namenumlist = [word for word in namenumber.split(',')]
namenumberdict = {namenumlist[0]:namenumlist[1]}
getnumber = input()
print(f'{namenumberdict[getnumber]}')'''

inp = input()
pairs = inp.split() #split the input string into a list of name,number pairs
contacts = {} #create an empty dictionary to store the name,number pairs

for pair in pairs:
    name_and_number = pair.split(',') #split each name,number pair into a list of two elements
    name = name_and_number[0] #get the name from the list
    number = name_and_number[1] #get the number from the list
    contacts[name] = number #add the name and number to the dictionary

search_name = input() #get the name to search for
print(contacts[search_name]) #print the number for the searched name