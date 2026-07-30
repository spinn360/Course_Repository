'''
Write a program that reads integers user_num and div_num as input, 
and output the integer quotient (user_num divided by div_num). Use 
a try block to perform all the statements. Use an except block to 
catch any ZeroDivisionError as a variable and output "Zero Division
Exception: " followed by the exception message from the variable. 
Use another except block to catch any ValueError caused by invalid
input as a variable and output "Input Exception: " followed by 
the exception message from the variable.

Note: ZeroDivisionError is raised when a division by zero happens. 
ValueError is raised when a user enters a value of different data 
type than what is defined in the program. Do not include code to 
raise any exception in the program.
'''
try:
    user_num = int(input())
    div_num = int(input())
    # this should be an output of the program. For example, if user enters 15 and 0, it should output "Zero Division Exception: division by zero". If user enters '15' and 3, it should output "Input Exception: invalid literal for int() with base 10: '15.

    quotient = user_num // div_num
    print(f"{quotient}")
# except input exception here.
except ValueError as ve:
    print(f"Input Exception: {ve}")

except ZeroDivisionError as zde:
    print(f"Zero Division Exception: {zde}")

