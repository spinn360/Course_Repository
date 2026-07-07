x = int(input('Enter whole number: ')) 
y = 5 if (x == 2) else 9 * x      # conditional expression here
if x == 2:
    print(f'You entered {x} which makes the output {y} always')
else:
    print(f'you entered {x} which times 9 = {y}')


num_users = int(input('Enter num users: '))
update_direction = int(input('Enter num 1-4: '))

num_users = num_users + 1 if (update_direction == 3) else num_users - 1  # conditional expression

print(f'New value is: {num_users}')