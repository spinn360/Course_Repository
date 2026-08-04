
#solution accepts three integer inputs representing the number of times a given employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

#accept three integer inputs
print("Enter Employee A's total trips to the job site:")
trips_a = int(input())
print("Enter Employee B's total trips to the job site:")
trips_b = int(input())
print("Enter Employee C's total trips to the job site:")
trips_c = int(input())

#calculate total distance
total_distance = (trips_a * 15.62) + (trips_b * 41.85) + (trips_c * 32.67)
#output combined mileage
print(f"Distance: {total_distance:.2f} miles")
