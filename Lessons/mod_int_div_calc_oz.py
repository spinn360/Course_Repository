'''
Gallon: 128 fluid ounces

Quart: 32 fluid ounces

Pint: 16 fluid ounces

Cup: 8 fluid ounces
If you input 345 fluid ounces, the breakdown should be:

345 fits 2 Gallons (256 oz used, 89 oz left)

89 fits 2 Quarts (64 oz used, 25 oz left)

25 fits 1 Pint (16 oz used, 9 oz left)

9 fits 1 Cup (8 oz used, 1 oz left)

Leaving 1 Ounce leftover.
345 expected output:
Gallons: 2
Quarts: 2
Pints: 1
Cups: 1
Leftover Ounces: 1
'''
print("--- Catering Calculator ---")
total_oz = int(input("Enter total fluid ounces: "))

# 1. Calculate Gallons (128 oz)
gallons = total_oz // 128
oz_left = total_oz % 128

# 2. Calculate Quarts (32 oz) using the leftover ounces
quarts = oz_left // 32
oz_left = oz_left % 32

# 3. Calculate Pints (16 oz) using the leftover ounces
pints = oz_left // 16
oz_left = oz_left % 16

# 4. Calculate Cups (8 oz) using the leftover ounces
cups = oz_left // 8
oz_left = oz_left % 8

# 5. Final leftover ounces
final_oz = oz_left

# Print the results
print(f"Gallons: {gallons}")
print(f"Quarts: {quarts}")
print(f"Pints: {pints}")
print(f"Cups: {cups}")
print(f"Ounces: {final_oz}")
...
