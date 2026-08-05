'''
Challenge 2: 
Data Types & Exception Handling
Based on: Evaluating elements in a mixed data 
list by their index, determining their data 
type (iterable or numeric), and handling 
out-of-bounds errors with a try/except block.  
Your Task:Create the following list representing 
off-road trail data:
trail_data = ["Rubicon",
             22.5, 4,
             ["mud", "rocks"],
             None, {"difficulty": "hard"}
             ]
Accept an integer input for the index.
If the index exists, print the element and its data 
type.Add logic to print a specific message if the 
element is iterable, a different message if it is 
numeric, and a fallback message for anything else.
If the user enters an index that doesn't exist, use 
a try/except block to output "Error".

'''


trail_data = ["Rubicon",
             22.5, 4,
             ["mud", "rocks"],
             None, {"difficulty": "hard"}
             ]

try:
    user_input = int(input('Enter an index to access the trail data: '))
    trail_element = trail_data[user_input]      
    data_type = type(trail_element).__name__
    print(f"Element: {trail_element}")
    if hasattr(trail_element, '__iter__'):
        print(f"Data Type: {data_type} is iterable")
    elif type(trail_element) in [int, float]:
        print(f"Data Type: {data_type} is numeric")
    else:
        print(f"Data Type: {data_type} is neither iterable nor numeric")
    '''
    if data_type in ['list', 'tuple', 'set', 'dict', 'str']:
        print(f"Data Type: {data_type} is iterable")
    elif data_type in ['int', 'float']:
        print(f"Data Type: {data_type} is numeric")
    else:
        print(f"Data Type: {data_type} is neither iterable nor numeric")
'''

except:
    print("Error not found in the list")