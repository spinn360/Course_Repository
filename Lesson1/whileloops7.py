spondias_count = 0

next_item = input('Enter an item (or "Finished" to stop): ')

while next_item != 'Finished':
    if next_item == 'Spondias':
        spondias_count += 1
    next_item = input('Enter an item (or "Finished" to stop): ')

print(f'Spondias occurs {spondias_count} time(s).')