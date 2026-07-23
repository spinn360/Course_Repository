'''Create a solution that accepts an integer input representing 
any number of ounces. Output the converted total number of tons, 
pounds, and remaining ounces based on the value of the input ounces. 
There are 16 ounces in a pound and 2,000 pounds in a ton.
The solution output should be in the format:
Tons: value_1 Pounds: value_2 Ounces: value_3
 
Sample Input and Output:
If the input is
32500
then the expected output is
Tons: 1 Pounds: 31 Ounces: 4
'''
ton = 2000
ouncePerPound = 16
ounce = 1
ouncePerTon = ton * ouncePerPound


weight = int(input('Enter weight in ounces: '))
tonscalc = weight // ouncePerTon
lbsCalc = (weight % ouncePerTon) // ouncePerPound
ounceCalc = weight % ouncePerPound
print(f'Tons: {tonscalc} Pounds: {lbsCalc} Ounces: {ounceCalc}')