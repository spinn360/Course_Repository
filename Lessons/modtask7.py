import calendar

# Complete the function to print the full name of the month using the calendar library 
def printMonthName(monthNum):
    # Student code goes here
    print(calendar.month_name[monthNum])
 
# expected output: March
printMonthName(3)
 
# expected output: November
printMonthName(11)