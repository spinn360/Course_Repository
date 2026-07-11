lugnuts = 5
wheels = 4
for wheel in range(wheels):
    print(f'Wheel {wheel + 1} has {lugnuts} lugnuts.')
    for lugnut in range(lugnuts):
        print(f'  Lugnut {lugnut + 1} is tight.')
        
        
trashcans = int(input(f'How many trashcans? '))

streets = int(input(f'How many streets? '))

for street in range(int(streets)):
    
    print(f'Street {street + 1} has {trashcans} trashcans.')
    for trashcan in range(int(trashcans)):
        print(f'  Trashcan {trashcan + 1} is now empty.')
        
apples = int(input(f'How many apples? '))
oreanges = int(input(f'How many oranges? '))
fruits = apples + oreanges
for fruit in range(fruits):
    if fruit < apples:
        print(f'Fruit {fruit + 1} is an apple.')
    else:
        print(f'Fruit {fruit + 1} is an orange.')
        
bras = int(input(f'How many bras? '))
underwear = int(input(f'How many underwear? '))
clothes = bras + underwear
for cloth in range(clothes):
    if cloth < bras:
        print(f'Cloth {cloth + 1} is a bra.')
    else:
        print(f'Cloth {cloth + 1} is underwear.')

