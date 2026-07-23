hours_bound = int(input())

print('Hours passed:', end=' ')

for i in range(hours_bound + 1):
    print(i, end=' ')
print()

catalog_low = int(input())
catalog_up = int(input())

print('Catalog numbers:', end=' ')

for i in range(catalog_low, catalog_up + 1):
    print(i, end=' ')
print()

catalog_start = int(input())
catalog_stop = int(input())

print('Catalog numbers:', end=' ')

for catalog_val in range(catalog_start, catalog_stop -1, -1):
    print(catalog_val, end=' ')
print()

begin_item = int(input())
end_item = int(input())
items_accepted = 0

for i in range(begin_item, end_item +1, 3):
    print(f'Checking item: {i}')
    items_accepted += 1

print(f'Total items accepted: {items_accepted}')