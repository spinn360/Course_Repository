jnum = int(input('Enter jersey number 1-99:'))
# lineback 40-59 or 90-99
# tight end 30-39 or 80-89
# defensive lineback 20-29 of 60-79 
# quarterback 1-19

if (jnum >= 90 and jnum < 100) or (jnum >= 40 and jnum <60):
    print('Looks like a linebacker')
elif (jnum >= 30 and jnum < 40) or (jnum >= 80 and jnum < 90):
    print('Looks like a tight end')
elif (jnum >= 20 and jnum < 30) or (jnum >= 60 and jnum < 80):
    print('Looks like a defensive back')
elif jnum > 0 and jnum <20:
    print('We got a quarterback')
else:
    print('That number is incorrect, try again')