''' Type your code here. '''
total_change = int(input('Enter change amount in pennies:\nExample $762.01 would be 76201\n '))
owed = False
if total_change == 0:
    print('No change')
if total_change < 0:
    print('Looks like you owe me change.')
    total_change = abs(total_change)
    owed = True
    print(total_change)
if total_change > 0:
    if owed:
        print('The change breakdown to pay me is:\n')
    else:
        print('Here is your change breakdown:\n')

    dollars = total_change // 100
    total_change = total_change % 100
    
    # Calculate Quarters
    quarters = total_change // 25
    total_change = total_change % 25
    
    # Calculate Dimes
    dimes = total_change // 10
    total_change = total_change % 10
    
    # Calculate Nickels
    nickels = total_change // 5
    total_change = total_change % 5
    
    # Calculate Pennies
    pennies = total_change
    
    # Print Dollars
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")
            
    # Print Quarters
    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")
            
    # Print Dimes
    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")
            
    # Print Nickels
    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")
            
    # Print Pennies
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")