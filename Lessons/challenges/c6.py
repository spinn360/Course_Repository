temp = int(input('Enter engine temp: '))
state = ''
optional_comment = ''
if temp >= 240:
    state = 'Overheating'
    if temp == 240:
        optional_comment = 'Pull over immediately'
elif 210 <= temp <= 239:
    state = 'Running hot'
elif 195 <= temp <= 209:
    state = 'Optimal'
elif  temp >= 32:
    state = 'Warming Up' 
elif temp < 32:
    state = 'Freezing'
    optional_comment = 'Check antifreeze'

if state != '':
    print(f"{state}")
if optional_comment != '':
    print(f"{optional_comment}")


