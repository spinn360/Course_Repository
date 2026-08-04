#solution accepts integer input and integer comparison value
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is greater than identified comparison value

#import math module and call factorial()
import math

#accepts integer input
print("Enter a number to calculate its factorial:")
factorial_num = int(input())
print("Enter a number to compare with the factorial:")
comparison_num = int(input())
#greater = False
#factorial method
result = math.factorial(factorial_num)
print(f'The factorial value of {factorial_num} is {result}')
#greater than user_input_comparison?
print(f'{result > comparison_num}')
'''if result > comparison_num:
    greater = True
else:
    greater = False
print(f'{greater}')'''

#output factorial


#output boolean
