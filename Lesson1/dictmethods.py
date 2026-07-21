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