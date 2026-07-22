# Complete the function to return a dictionary using 
# list1 as the keys and list2 as the values
def createDict(list1, list2):
    list_dict = {}
    for i in range(len((list1))):
        key = list1[i]
        value = list2[i]
        list_dict[key] = value

    return list_dict
# Student code goes here
        
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))