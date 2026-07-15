print(f'{"Player Name":16}{"Goals":8}')
print('-' * 24)
print(f'{"Sadio Mane":16}{"22":8}')
print(f'{"Gabriel Jesus":16}{"7":8}')
print(f'{"Left here right there":<40}{"7":>16}')
print(f'{"Left":<16}{"7":>16}')
print(f'{"Left":>16}{"7":<16}')
print(f'{"Left":*<16}{"7":0>16}')
print(f'{"Left":*^16}{"7":*^16}')

item_name = 'fart'

print(f'{item_name:=<16}')
print(f'{item_name:=>16}')

feet_length = 61
meters_length = feet_length * 0.3048

print(f'Before formatting: {meters_length} meters')

print(f'After formatting: {meters_length:.6f} meters')



employees = input().split()
states = input().split()
separator_char = input()

print(f'{"Employees":^27}{"States":^27}')
print(f'{separator_char * 54}')
print(f'{employees[0]:^27}{states[0]:^27}')
print(f'{employees[1]:^27}{states[1]:^27}')
print(f'{employees[2]:^27}{states[2]:^27}')


phrase = 'Someday I will have three goats, six horses, and nine llamas.'

# Replace English with Spanish.
phrase = phrase.replace('one', 'uno')
phrase = phrase.replace('two', 'dos')
phrase = phrase.replace('three', 'tres')
phrase = phrase.replace('four', 'cuatro')
phrase = phrase.replace('five', 'cinco')
phrase = phrase.replace('six', 'seis')
phrase = phrase.replace('seven', 'siete')
phrase = phrase.replace('eight', 'ocho')
phrase = phrase.replace('nine', 'nueve')

print('Translation:', phrase)