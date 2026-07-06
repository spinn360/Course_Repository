'''Integers num_bananas and my_allowance are read from input. Each banana costs 3 dollars.

Write the following if-else statement. Within the else branch, write the following assignment and nested if-else statement:

If num_bananas is less than 3, output 'Not enough bananas purchased'.
Otherwise:
Assign variable total_cost with the product of num_bananas and 3.
If total_cost is less than or equal to my_allowance, then output 'Approved transaction'.
Otherwise, output 'Not enough money to buy all'.'''

num_bananas = int(input('Number of bananas: '))
my_allowance = int(input('Allowance amount: '))
total_cost = num_bananas * 3

if total_cost <= my_allowance:
    if num_bananas < 3:
        print('Not enough bananas purchased')
    else:
        print('Approved transaction')
else:
    print('Not enough money to buy all')
