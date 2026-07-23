my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing values
print(my_dict['name'])  # Output: John
# Adding a new key-value pair
my_dict.clear()
print(my_dict)  # Output: {}
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'country': 'USA'}
my_dict.update({'age': 31, 'city': 'Los Angeles'})
print(my_dict)  # Output: {'country': 'USA', 'age': 31, 'city': 'Los Angeles'}
# Removing a key-value pair
del my_dict['age']
print(my_dict)  # Output: {'country': 'USA', 'city': 'Los Angeles'}
# Iterating through keys and values
for key, value in my_dict.items():
    print(f'{key}: {value}')    
my_dict.get('name', 'Not Found')  # Output: Not Found
print(my_dict.keys())  # Output: dict_keys(['country', 'city'])
print(my_dict.values())  # Output: dict_values(['USA', 'Los Angeles'])
my_dict.pop('city')
print(my_dict)  # Output: {'country': 'USA', 'age': 31}
my_dict.popitem()  # Removes the last inserted key-value pair
print(my_dict)  # Output: {'country': 'USA'}
my_dict.setdefault('age', 25)  # Adds 'age' key with value 25 if it doesn't exist
print(my_dict)  # Output: {'country': 'USA', 'age': 25}
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
my_dict.pop('age')  # Removes the 'age' key-value pair
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}
my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)
my_dict.update(dict(soda=1.49, burger=3.69))
burger_price = my_dict.get('burger', 0)
print(burger_price)
print(my_dict.get('salad', 'Not Found'))  # Output: Not Found because default value is provided
print(my_dict.pop('bananas', 'Not Found'))  # Output: 1.59
my_dict.pop()

'''
room_temperatures1 = {'323': '8.3'}
room_temperatures2 = {'601': '7.1'}
room_temperatures3 = {'272': '7.2'}
ref_record1 = room_temperatures1  # For testing purposes, ref_record1 references room_temperatures1
ref_record2 = room_temperatures2  # For testing purposes, ref_record2 references room_temperatures2
ref_record3 = room_temperatures3  # For testing purposes, ref_record3 references room_temperatures3


input_line = input()
while input_line != 'done':
	room, temperature = input_line.split()
	room_temperatures1[room] = temperature
	input_line = input()

room_temperatures2.update(room_temperatures1)
room_temperatures3.update(room_temperatures2)
room_temperatures1.clear()

print('Room temperatures 1:')
print(room_temperatures1)
print('Room temperatures 2:')
print(room_temperatures2)
print('Room temperatures 3:')
print(str(room_temperatures3))
'''


vegetables_record = {'peas': 'great', 'leek': 'fair', 'beet': 'good', 'kale': 'poor'}
price_chart = {'great': 50.0, 'good': 40.0, 'fair': 20.0, 'poor': 5.0}

vegetables_name = input()

''' Your code goes here '''
#Use pop() to remove vegetables_name from vegetables_record and assign vegetables_grade with the value returned. Any string that is not a key in vegetables_record has the default value 'no info'.
vegetables_grade = vegetables_record.pop(vegetables_name, 'no info')

#Assign patient_price with the value associated with key vegetables_grade in price_chart. Any number that is not a key in price_chart has default value -99.
patient_price = price_chart.get(vegetables_grade, -99)

print(f'{vegetables_name} ({vegetables_grade}) scores {patient_price}')
print('Remaining vegetables:')
print(vegetables_record)
'''
Method	Description
clear()	Removes all items from the dictionary.
copy()	Returns a shallow copy of the dictionary.
fromkeys(keys, value)	Returns a new dictionary with specified keys and a default value.
get(key)	Returns the value for the specified key, or None if the key does not exist.
items()	Returns a view object of the dictionary’s key-value pairs.
keys()	Returns a view object of the dictionary's keys.
pop(key)	Removes and returns the value for the specified key.
popitem()	Removes and returns an arbitrary((random)) (key, value) pair from the dictionary.
setdefault(key, value)	Returns the value of the specified key if it exists, otherwise 
        sets it to the default value.
update(other)	Updates the dictionary with key-value pairs from another dictionary 
        or iterable.
values()	Returns a view object of the dictionary's values.

While these methods can be useful in certain situations, remember that dictionary 
indexing ([ ]) is the most common way to access and modify dictionary values. 
For example, instead of using get(), you can simply use dict[key] to retrieve a value, 
and dict[key] = value to set or update a value. This direct referencing makes 
dictionary methods less essential compared to other types like lists and strings.
'''