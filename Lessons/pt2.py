#list of mixed data elements
data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None, {"name": "John", "age": 25}]

#input for index
print("Enter index:")
index = int(input())
try:
    my_element = data_mixture[index]
    data_type = type(my_element).__name__
    if hasattr(my_element, '__iter__'):
        message = 'This element is iterable.'
    elif type(my_element) in (int, float):
        message = 'This element is numeric.'
    else:
        message = 'This is a different data type.'

    print(f'Element: {my_element}, Type: {data_type}, Message: {message}')


except:
    print('Error')

