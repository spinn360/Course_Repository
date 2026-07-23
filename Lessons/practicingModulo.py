total_time = 415
min_in_hour = 60
hourstotal = total_time // min_in_hour # returns the whole hours // instead of a fraction with /
mins = total_time % min_in_hour  # returns the remainder minutes dividing the time by 60 min per hour

print(f'Hours: {hourstotal} Min: {mins}')