#Here I will be moving on from p1 where I ended with user input so the beginning will continue with input
print('hello, and welcome back are you ready to continue?', end= ' ')
cont = input()
print('You said', cont, 'that is either great or not I have no idea LOL')

# ok
# salary calculator
hours = 40
weeks = 52
hourly_wage = int(input('Enter Hourly wage: '))

print('Salary is', hourly_wage * hours * weeks)

# dog year calculator
human_years = int(input('Enter age of dog (in human years): '))
print()

dog_years = 7 * human_years

print(human_years, 'human years is about', end=' ')
print(dog_years, 'dog years.')
