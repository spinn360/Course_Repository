help(print)
# this will display some help with options for print
help(type)
# displays info on class type(object, name, base, or dict) 
#                             __call__(self, /, *args, **kwargs) and much much more

x = 42
print(type(x)) # returns type or class object of x <class 'int'>

def my_function():
    pass

print(my_function.__name__)  # Output: 'my_function'

