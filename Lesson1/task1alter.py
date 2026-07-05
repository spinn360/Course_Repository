num1 = int(input('Enter times John travels to a job this in a month: '))
num2 = int(input('Enter times Fred travels to a job this in a month: '))
num3 = int(input('Enter times Wilma travels to a job site this month: '))



employeeA = float(input('Enter miles driven this month: '))
employeeB = float(input('Enter miles driven this month: '))
employeeC = float(input('Enter miles driven this month: '))

total_miles_traveled = (employeeA * num1) + (employeeB * num2) + (employeeC *num3)

print(f'Distance: {total_miles_traveled} miles')