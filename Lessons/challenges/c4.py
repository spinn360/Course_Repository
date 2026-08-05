'''
Challenge 4: 
Multi-Input Type CastingBased on: Accepting five integer 
inputs and outputting their combined value as an integer 
sum, a float sum, and a concatenated string.  Your Task:
Write a program that asks for the weights of five fish 
caught during a catch-and-release trip.Calculate the sum 
of all five weights as an integer.Cast that total sum 
into a float.Concatenate all five original inputs into a 
single, continuous string.Print all three results.
'''
fish1 = int(input('Enter weight of fish 1: '))
fish2 = int(input('Enter weight of fish 2: '))
fish3 = int(input('Enter weight of fish 3: '))
fish4 = int(input('Enter weight of fish 4: '))
fish5 = int(input('Enter weight of fish 5: '))

total_weight = fish1 + fish2 + fish3 + fish4 + fish5
float_weight = float(total_weight)
str_weight = str(fish1) + str(fish2) + str(fish3) + str(fish4) + str(fish5)
print(f'Total weight as integer: {total_weight}')
print(f'Total weight as float: {float_weight}')
print(f'Total weight as a string: {str_weight}')