#dictionaries
players = {
    'Lionel Messi': 10,
    'Christiano Ronaldo': 7
}

print(players)

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

print('a Mr goodbar candy has',  caffeine_content_mg['Mr. Goodbar chocolate'], 'mg of caffiene')
prices = {}
prices['bananas'] = 1.49
print(prices)
prices['bananas'] = 1.99
print(prices)
del prices['bananas']
print(prices)


#I suppose this could be used to remove a guest that is staying at checkout
hotel_guests = {104: 'Mai', 534: 'Huy'}
print(hotel_guests)
key_name = int(input('Enter Room Number upon checkout: '))

print(hotel_guests[key_name])
del hotel_guests[key_name]

print('Remaining pairs:')
print(hotel_guests)



code_to_name = {
	'VT': 'Vermont', 'MS': 'Mississippi', 'OK': 'Oklahoma', 'ID': 'Idaho',
	'HI': 'Hawaii', 'ME': 'Maine', 'ND': 'North Dakota', 'NJ': 'New Jersey'
}

stateA= str(input('Enter 2 letters for state start point: '))
stateB= str(input('Enter 2 letters for state start point: '))

print(code_to_name[stateA] +' to ' + code_to_name[stateB])