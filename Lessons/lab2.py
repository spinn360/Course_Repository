#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

print("Enter the number of ounces to convert:")
ounces = int(input())

#calculate total tons
tons = ounces // 16 //2000
remainder = ounces % (16 * 2000)
print(f"tons {tons}")
print(f"remainder {remainder}")
#calculate toatl pounds
pounds = remainder // 16
print(f"pounds {pounds}")
remainderoz = ounces % 16
print(f"remainderoz {remainderoz}")
#calculate total ounces
ounces_final = remainder % 16
print(f"ounces_final {ounces_final}")

#convert ounces to pounds and tons 
#output number of tons, remaining pounds, and remaining ounces
