import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
    # Student code goes here
    print(calendar.day_name[datetime.date(year, month, day).weekday()])

# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)