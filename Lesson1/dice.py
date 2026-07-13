import random

# Initial input before the loop starts
num_rolls = int(input('Enter number of rolls (0 to quit):\n'))

# 2. Repeatedly ask until num_rolls is less than 1
while num_rolls >= 1:
    
    # 1. Calculate the number of times each sum is rolled.
    # Create a list of 13 zeros to hold the counts for sums 0-12 
    # (Indices 0 and 1 will simply remain 0 and be ignored)
    counts = [0] * 13 
    
    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2
        
        # Add 1 to the specific index matching the rolled sum
        counts[roll_total] += 1
        
    print('\nDice roll histogram:\n')
    
    # 3. Print the histogram for values 2 through 12
    for i in range(2, 13):
        
        # Multiply the asterisk string by the count at that index
        stars = '*' * counts[i]
        
        # This formatting ensures the asterisks align perfectly 
        # regardless of whether the number has 1 or 2 digits
        if i < 10:
            print(f'{i}s:  {stars}')
        else:
            print(f'{i}s: {stars}')
            
    # Ask again to continue or break the loop
    num_rolls = int(input('\nEnter number of rolls:\n'))