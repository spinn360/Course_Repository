my_dict = {'Terrible': 'Woman', 'Angry': 'Bitch', 'Scammer': 'Sally'}
print(my_dict['Terrible'])
print(my_dict['Angry'])
print(my_dict['Scammer'])

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

print(caffeine_content_mg)

people_dict = {'Shawn': 44, 'Jo': 42, 'Matthew': 18, 'Jacob' : '15'}

print(f'I am {people_dict["Shawn"]}') # be sure to use opposite type quotes

people_dict['Nancy'] = 65

print(f'Nancy is {people_dict["Nancy"]}')

people_dict['Nancy'] = 68

print(f'Actually Nancy is {people_dict["Nancy"]}')

people_dict['George'] = 101

print(f'George is {people_dict["George"]}')
print(people_dict)
print(f'George died at {people_dict["George"]}')

del people_dict['George']

print(f'Goodbye George \n{people_dict}')

meeting1 = int(input())
meeting2 = int(input())
meeting3 = int(input())

schedule= {'August': meeting1,'December':meeting2,'February':meeting3}

print(f"August: {schedule['August']}")
print(f"December: {schedule['December']}")
print(f"February: {schedule['February']}")

guestroom_number1 = int(input())
guest_name1 = input()
guestroom_number2 = int(input())
guest_name2 = input()

room_guests= {guestroom_number1: guest_name1,guestroom_number2:guest_name2}

print(f'{guestroom_number1}: {room_guests[guestroom_number1]}')
print(f'{guestroom_number2}: {room_guests[guestroom_number2]}')

