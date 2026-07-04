distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
    
# 5. Distance is 1 mile or less
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
        
# 6. Distance is greater than 1 mile and up to 6 miles
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
        
# 7. Distance is greater than 6 miles
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)