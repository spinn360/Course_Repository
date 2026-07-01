# creating lists is pretty straight forward like creating a variable with [ 'and', 'commas','separating']
my_nums = [5, 10, 20, 40]
my_list = [-100, 'lists yipee!', False, 'cat', 100]
empty_list = []
costs = [1.50, 2.50, 5.99, 11.78]

dog = 'Sally'
cat = 'Jinx'
frog = 'Ribbit'

names_list = [dog, cat, frog]

print(f'Least favorite dog is {names_list[0]}')
print(f'Favorite cat is {names_list[1]}')
print(f'The frog goes {names_list[2]}')
print(f'The sum of my_nums is {my_nums[0] + my_nums[1] + my_nums[2] + my_nums[3]}')
print(sum(costs))
print(f'The first price is ${costs[0]}0')
costs[0] = 99.99
print(f'The updated first price is ${costs[0]}')
print(f'costs list: {costs}')
print(len(costs))
costs.append(700.00)
print(f'costs list: {costs}')
print(len(costs))
costs.pop(1)
print(f'costs list: {costs}')
print(len(costs))
costs.remove(11.78)
print(f'costs list: {costs}')
print(len(costs))
print(min(costs))
print(max(costs))
print('700.00 is indexed at:',costs.index(700.00))


# Concatenating lists
house_prices = [380000, 900000, 875000] + [225000]
print(f'There are {len(house_prices)} prices in the list.')

# Find lowest cost housing
cost = min(house_prices)
print(f'The most affordable is for sale at ${cost}.')
# Add in taxes and fees to purchase
closing_costs = [
  cost * 0.02,  # Inspection, escrow, title insurance, etc.
  250,          # HOA fees
  cost * 0.005  # Moving company
]

total_cost = cost + sum(closing_costs)
print(f'Total closing cost: ${int(total_cost)}.')