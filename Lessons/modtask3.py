import datetime

def currentDate(x):
    # Student code goes here
    seconds = x * 24 * 60 * 60
    print(f"The total number of seconds is {seconds:.1f}.")
# Student code goes here
 
currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.