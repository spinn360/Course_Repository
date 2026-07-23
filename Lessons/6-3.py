import random

# Generates a random floating point number 
print(random.random())
print(random.random())

# Generates random integers with 3 possible values
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))

# 0, 1, or 2
# powerball numbers
print('Here are the winning Powerball numbers:')
print(random.randint(1,69))
print(random.randint(1,69))
print(random.randint(1,69))
print(random.randint(1,69))
print(random.randint(1,69))
print(random.randint(1,26))


"""
Switch a student from a random seat on the left  (cols 1 to 15)
to a random seat on the right (cols 16 to 30)
Seat rows are 1 to 20
"""
rowNumL = random.randint(1, 20)  # 1 to 20 rows left 
colNumL = random.randint(1, 15)  # 1 to 15  columns left
rowNumR = random.randint(1, 20)  # 1 to 20 rows right
colNumR = random.randint(16, 30) # 16 to 30 columns right

print(f'Move from row {rowNumL} col {colNumL} to row {rowNumR} col {colNumR}')

# Generate same sequence of numbers using same seed
random.seed(15)

# Generate same sequence of random integers between 1 and 10
print (random.randint(1, 10))
print (random.randint(1, 10))
print (random.randint(1, 10))