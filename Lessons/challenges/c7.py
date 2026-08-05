gear = {"carabiner": 5.50, "rope": 45.00, "headlamp": 25.99, "trail_mix": 3.25}
item = input('Enter item: ')
quantity = int(input('Enter quantity: '))
sale = 1
if 10 <= quantity <= 20:
    sale = 0.95
elif  quantity >= 21:
    sale = 0.9
if item in gear:
    print(f'Total cost for {item} is ${(gear[item] * quantity )* sale:.2f}')
else:
    print(f"Sorry we don't sell that here")