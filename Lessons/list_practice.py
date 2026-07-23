'''list_data = []
for elem in input().split():
	if elem.isdigit(): # If elem is a digit, then convert to int.
		list_data.append(int(elem))
	else:
		list_data.append(elem)

print(f'List items: {list_data[1]} {list_data[3]}')
'''
#########################################################
'''
city_populations = [
	1331254, 'Lusaka', 1197816, 'Dallas', 2099451, 'Houston', 
	1526006, 'Philadelphia', 934243, 'Ottawa', 1789635, 'Rabat', 
	1327407, 'San Antonio', 1307402, 'San Diego', 3792621, 'Los Angeles', 
	701063, 'Kingston', 945942, 'San Jose', 829718, 'Indianapolis', 
]
list_index = int(input())

print(f'The population of {city_populations[list_index]} is {city_populations[list_index - 1]}.')
'''
###########################################################

'''Integer n and string my_color are read from input. Then, four strings are 
read from input and stored in the list color_database. Delete the element 
at index n in color_database, then replace the last element 
of color_database with my_color.

'''
'''
n = int(input())
my_color = input()
color_database = input().split()

del color_database[n]
color_database[len(color_database) -1] = my_color

print(f'My favorite colors: {color_database}')

####################################################


course_list = input().split()
added_courses = input().split()

updated_courses = course_list[:] + added_courses[:]

###########################################################

'''
'''
List method	Description	Code example	                         >Final my_list value
list.append(x)	Add an item to the end of list.	my_list = [5, 8]
my_list.append(16)	                                             [5, 8, 16]
list.extend([x])	Add all items in [x] to list.	my_list = [5, 8]
list = list + otherlist is essentially the same as list.extend(otherlist).
my_list.extend([4, 12])	                                         [5, 8, 4, 12]
list.insert(i, x)	Insert x into list before position i.	my_list = [5, 8]
my_list.insert(1, 1.7)	                                         [5, 1.7, 8]
Removing elements
List method	Description	Code example	                         Final my_list value
list.remove(x)	Remove first item from list with value x.	my_list = [5, 8, 14]
my_list.remove(8)	                                             [5, 14]
list.pop()	Remove and return last item in list.	my_list = [5, 8, 14]
val = my_list.pop()	                                             [5, 8]
                                                                 val is 14
list.pop(i)	Remove and return item at position i in list.	my_list = [5, 8, 14]
val = my_list.pop(0)	                                         [8, 14]
                                                                 val is 5

Modifying elements
List method	Description	Code example	                        Final my_list value
list.sort()	Sort the items of list in-place.	my_list = [14, 5, 8]
my_list.sort()	                                                [5, 8, 14]
list.reverse()	Reverse the elements of list in-place.	my_list = [14, 5, 8]
my_list.reverse()	                                            [8, 5, 14]

Miscellaneous
List method	Description	Code example	                        Final my_list value
list.index(x)	Return index of first item in list with value x.	my_list = [5, 8, 14]
print(my_list.index(14))	                                    Prints "2"
list.count(x)	Count the number of times value x is in list.	my_list = [5, 8, 5, 5, 14]
print(my_list.count(5))	                                        Prints "3"
'''

mylist = ['dog', 'cat', 'frog', 1, 2, 3]

print(mylist)
mylist.append('antelope')
print(mylist)
otherlist = [9,8,7,6,5,4]
mylist.extend(otherlist)
print(mylist)
mylist.insert(1, 1.7)
print(mylist)
mylist.remove('cat')
print(mylist)
mylist.pop(8)
mylist.pop(5)
print(mylist)
mylist.pop()
print(mylist)
#mylist.sort()
#print(mylist)
mylist.reverse()
print(mylist)
#print(mylist.index(3))
print(mylist.count(3))

'''
not_on_board = input().split()
on_board_bus = input().split()

print(f'Passengers waiting at a bus stop: {not_on_board}')
print(f'Passengers on board: {on_board_bus}')
removed = on_board_bus[0]
on_board_bus.pop(0)
print(f'Passenger alighted: {removed}')
on_board_bus.extend(not_on_board)
print(f'Updated passengers on board: {on_board_bus}')
'''
'''tokens = input().split()
ticket_numbers = []
for token in tokens:
    ticket_numbers.append(int(token))

ticket_numbers.sort()
first_smallest = ticket_numbers[0]
second_smallest = ticket_numbers[1]
third_smallest = ticket_numbers[2]

print(f'Sorted ticket numbers: {ticket_numbers}')
print(f'Smallest: {first_smallest}')
print(f'Second smallest: {second_smallest}')
print(f'Third smallest: {third_smallest}')
'''
'''Method	Description
append(item)	Adds an item to the end of the list.
clear()	Removes all items from the list.
copy()	Returns a shallow copy of the list.
count(item)	Returns the number of occurrences of the specified item in the list.
extend(iterable)	Extends the list by appending all items from an iterable.
index(item)	Returns the index of the first occurrence of the specified item.
insert(index, item)	Inserts an item at the specified index in the list.
pop(index)	Removes and returns the item at the specified index.
remove(item)	Removes the first occurrence of the specified item from the list.
reverse()	Reverses the elements of the list in place.
sort()	Sorts the list in place.

Additional List Methods

Use help(list) and print(dir(list)) to see more about lists and their methods. These commands provide detailed information and a list of available list methods.

Function	Description
len(list)	Returns the number of items in the list.
min(list)	Returns the smallest item in the list.
max(list)	Returns the largest item in the list.
sum(list)	Returns the sum of all items in the list (requires numeric items).
sorted(list)	Returns a new sorted list from the items in the original list.
reversed(list)	Returns an iterator that accesses the elements of the list in reverse order.


'''
