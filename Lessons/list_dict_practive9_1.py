# Complete the function to return a dictionary using the items in 
# the list as the keys and the length of each item as the values.
def createLengthDict(mylist):
    new_dict = {}
    for i in range(len((mylist))):
        key = mylist[i]
        value = len(mylist[i])
        new_dict[key] = value
    return(new_dict)
    
    # Student code goes here
    

# expected output: {'apple': 5, 'banana': 6, 'kiwi': 4}
print(createLengthDict(['apple', 'banana', 'kiwi']))

# expected output: {'Python': 6, 'Data': 4, 'Analytics': 9}
print(createLengthDict(['Python', 'Data', 'Analytics']))