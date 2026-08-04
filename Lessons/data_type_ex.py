sensor_data = ["Temperature", 72.5, 101, ["Zone A", "Zone B"], {"active": True, "error": 0}, False]

# Get the integer index from the user
index = int(input("Enter index: "))

# 1. Retrieve the element
try:
    my_element = sensor_data[index]

# 2. Get the string name of the data type
    data_type = type(my_element).__name__


   
# 3. Determine the category message
    if data_type == 'bool':
        message = "This is a boolean flag."
    elif data_type in ['list', 'str', 'dict']:
        message = "This is an iterable object."
    elif data_type == 'int' or data_type == 'float':
        message = "This is a numerical reading."
    else:
        message = "This is an unknown reading."

# 4. Print the exact formatted string
    print(f"Data: {my_element}, Type: {data_type}, Status: {message}")
#Data: False, Type: bool, Status: This is a boolean flag.
except IndexError:
    print('There was an error: Index out of range.')
except ValueError:
    print('There was an error: Please enter a valid integer.')