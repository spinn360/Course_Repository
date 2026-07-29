#create a prinout of a list of number and the average of the list of numbers
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
average = total / len(numbers) if numbers else 0
print(f"Numbers: {numbers}")
print(f"Average: {average}")
#find the maximum and minimum of the list of numbers
maximum = max(numbers) if numbers else None
minimum = min(numbers) if numbers else None
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
# output the message that everything was created with deepseek
print("Everything was created with deepseek")
# create a file called newfile.txt and write a message that it will all be okay inside then close the file, open the file read and print out the message
import os
file = open('newfile.txt', 'a')
file.write('\neverything is going to be alright\n')
file.close()
file = open('newfile.txt', 'r')
print(file.readlines())
file.close()
print('file closed')
            