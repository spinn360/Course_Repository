'''When analyzing data sets, such as data for human heights or for 
human weights, a common step is to adjust the data. This adjustment 
can be done by normalizing to values between 0 and 1, or throwing 
away outliers.

For this program, adjust the values by dividing all values by the 
largest value. The input begins with an integer indicating the number 
of floating-point values that follow. Assume that the list will always 
contain positive floating-point values.

Output each floating-point value with two digits after the decimal 
point, which can be achieved as follows:
print(f'{your_value:.2f}')'''

num_values = int(input())
values = []

for i in range(num_values):
    val = float(input())
    values.append(val)

max_value = max(values)

for val in values:
    adjusted_val = val / max_value
    print(f'{adjusted_val:.2f}')