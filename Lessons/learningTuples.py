from collections import namedtuple
# Tuples differ from lists [] with () comma separated lists and are immutable and cannot be changed after creation

white_house_coordinates = (38.8977, 77.0366)
print(f'Coordinates: {white_house_coordinates}')
print(f'Tuple length: {len(white_house_coordinates)}')

# Access tuples via index
print(f'\nLatitude: {white_house_coordinates[0]} north')
print(f'Longitude: {white_house_coordinates[1]} west\n')

print(len(white_house_coordinates))

car = namedtuple('car', ['make', 'model', 'year', 'price', 'horsepower', 'seat'])

olds_intrigue = car('Oldsmobile', 'Intrigue', 1998, 1500, 220, 5)
buick_terraza = car('Buick', 'Terraza', 2005, 8900, 225, 7)

print(olds_intrigue)
print(buick_terraza)

print(buick_terraza.price)
print(olds_intrigue.horsepower)

from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name', 'birthday', 'age'])

first_name = input('Enter first Name: ')
last_name = input('Enter last Name: ')
birthday = input('Enter Birthday: ')
age = int(input('Enter Age: '))

person_data = Person(first_name, last_name, birthday, age)

print(f'First name: {person_data.first_name}, Last name: {person_data.last_name}, Birthday: {person_data.birthday}, Age: {person_data.age}')