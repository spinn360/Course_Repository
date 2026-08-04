print("--- Time Converter ---")
total_seconds = int(input("Enter the total number of seconds: "))

# 1. Find the whole hours (3600 seconds in an hour)
hours = total_seconds // 3600

# 2. Find the leftover seconds that didn't fit into a whole hour
leftover_seconds = total_seconds % 3600

# 3. Find the whole minutes from those leftovers (60 seconds in a minute)
minutes = leftover_seconds // 60

# 4. Find the final leftover seconds that didn't fit into a whole minute
final_seconds = leftover_seconds % 60

# Print the final result!
print("\nThat converts exactly to:")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {final_seconds}")