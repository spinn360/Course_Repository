from collections import namedtuple

#normal tuple vs namedtuple vs dictionary
student = ('Bro', 21, 'male')

print(student.count('Bro'))
print(student.index('male'))

for x in student:
    print(x)

if "Bro" in student:
    print('Bro is here')
dict_color = {'red':55, 'green': 155, 'blue': 255}

color1 = (55, 155, 255)

print(f'{color1[0]}')

Color = namedtuple('Color', ['red', 'green', 'blue'])
blue = Color(0, 0, 255)
red = Color(255, 0, 0)
green = Color(0, 128, 0)
white = Color(255, 255, 255)
print(blue.red)
print(blue.green)
print(blue.blue)
print(f'{red} \n{white} \n{blue}')

