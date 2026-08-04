#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

print("Enter the number of ounces to convert:")
ounces = int(input())
tons = ounces // 16 // 2000
remainder = ounces % (16 * 2000)
pounds = remainder //16
poundsremainder = ounces % 16
ounces = poundsremainder % 16
#convert ounces to pounds and tons 
#output number of tons, remaining pounds, and remaining ounces
print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")
