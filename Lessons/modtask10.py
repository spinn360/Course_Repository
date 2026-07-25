import datetime

# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
    return someDate + datetime.timedelta(days=38)
# Student code goes here
 
 
date = datetime.date.today()
print(f"The current date is {date}.") #Expected outcome will vary, but should follow
# expected output: 2018-12-30
print(add90Days(datetime.date.today()))
print(add90Days(datetime.date(2026, 7, 25)))
 
# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))