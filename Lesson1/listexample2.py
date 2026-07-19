mylist = [1, 2, 3, 4, 5]
for i in range(len(mylist)):
    mylist[i] = mylist[i] * 2
print(mylist)   
for i in mylist:
    print(i * 2)
    
div = 10

for i in mylist:
    print(i * 8)
    
print(all(mylist   ))
print(max(mylist))
print(min(mylist))
print(sum(mylist))
'''
Function 	Description 	        Example code 	        Example output
all(list) 	True if every element in list is True (!= 0), or if the list is empty. 	
                                print(all([1, 2, 3]))       True

                                print(all([0, 1, 2])) 	    False


any(list) 	True if any element in the list is True. 	
                                print(any([0, 2]))          True
                                print(any([0, 0]))          False
                   

max(list) 	Get the maximum element in the list. 	
                                print(max([-3, 5, 25])) 	25

min(list) 	Get the minimum element in the list. 	
                                print(min([-3, 5, 25])) 	-3

sum(list) 	Get the sum of all elements in the list. 	
                                print(sum([-3, 5, 25])) 	27
'''
    