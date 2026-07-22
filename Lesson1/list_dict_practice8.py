# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
    if ascending:
        mylist.sort()
        return mylist
    else:
        mylist.sort(reverse=True)
        return mylist

# Student code goes here
    #alternative one liner to replace if statement
    #mylist.sort(reverse=not ascending)
    #return my list
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))
 
# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))