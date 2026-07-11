'''Primary U.S. interstate highways are numbered 1-99. 
Odd numbers (like the 5 or 95) go north/south, and evens 
(like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, 
and service the primary highway indicated by the rightmost two digits. 
Thus, I-405 services I-5, and I-290 services I-90. Note: 
200 is not a valid auxiliary highway because 00 is not a valid primary 
highway number.

Given a highway number, indicate whether it is a primary or 
auxiliary highway. 
If auxiliary, indicate what primary highway it serves. 
Also indicate if the (primary) highway runs north/south or east/west.'''



highway_number = int(input('Enter Hwy Number: '))

# 1. Check for primary highways (1-99)
if 1 <= highway_number <= 99:
    # Determine direction
    if highway_number % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"
        
    print(f"I-{highway_number} is primary, going {direction}.")
    
# 2. Check for auxiliary highways (100-999)
elif 100 <= highway_number <= 999:
    # Extract the rightmost two digits
    served_primary = highway_number % 100
    
    # Catch invalid auxiliary highways ending in 00 (e.g., 200)
    if served_primary == 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    else:
        # Determine direction based on the primary highway it serves
        if served_primary % 2 == 0:
            direction = "east/west"
        else:
            direction = "north/south"
            
        print(f"I-{highway_number} is auxiliary, serving I-{served_primary}, going {direction}.")
        
# 3. Catch everything else (0, negatives, 1000+)
else:
    print(f"{highway_number} is not a valid interstate highway number.")