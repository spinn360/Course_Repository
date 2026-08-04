#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum

print("Enter 1st number:")
num1 = int(input())
print("Enter 2nd number:")
num2 = int(input())
print("Enter 3rd number:")
num3 = int(input())
print("Enter 4th number:")
num4 = int(input())
print("Enter 5th number:")
num5 = int(input())

solution1 = (num1 + num2 + num3 + num4 + num5)
solution2 = float(solution1)
solution3 = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f"Integer: {solution1}")
print(f"Float: {solution2}")
print(f"String: {solution3}")


