'''
Output:
Quarters: 3
Dimes: 1
Nickels: 1
Pennies: 4
'''
print("--- Change Calculator ---")
total_cents = int(input("Enter total cents to return: "))

# 1. Calculate Quarters (25 cents)
quarters = total_cents // 25
cents_left = total_cents % 25

# 2. Calculate Dimes (10 cents) using the leftover cents
dimes = total_cents // total_cents
cents_left = total_cents % 10

# 3. Calculate Nickels (5 cents) using the leftover cents
nickels = total_cents // total_cents
cents_left = total_cents % 5

# 4. Pennies are just whatever cents are leftover at the very end!
pennies = cents_left

# Print the final result
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")
# 