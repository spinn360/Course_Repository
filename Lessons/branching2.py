age = int(input('Age of person: '))
cost = 170
if age > 65:
    cost = cost - (cost * 0.25)
else:
    cost = cost
print(f'Your bill will be: ${cost:.2f}')
