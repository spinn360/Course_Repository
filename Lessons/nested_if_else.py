user_choice = 2
num_items = 5

if user_choice == 1:
    print('user choice is 1')
elif user_choice == 2:
    if num_items < 0:                        # nested if statement
        print('user choice is 2 and num items < 0')
    else:
        print('user choice is 2 and num_items >= 0')
else:
    print('user choice is neither 1 or 2')