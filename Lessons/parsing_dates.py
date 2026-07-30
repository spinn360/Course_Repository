def get_month_as_int(monthString):
    
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()
while user_string != '-1':
    # TODO: Read dates from input, parse the dates to find the one
    #       in the correct format, and output in m/d/yyyy format
    #user_string = user_string.replace(',', '')
    string_list = user_string.split(' ')
    if len(string_list) == 3 and ',' in string_list[1] :
        day = string_list[1]
        day = day[:-1]
        print(f'{get_month_as_int(string_list[0])}/{day}/{string_list[2]}')
    user_string = input()
