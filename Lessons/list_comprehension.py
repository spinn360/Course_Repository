import math
my_list = [10, 12, 15, 19, 25, 110]
new_list = [(i+75) for i in my_list]
print(f'Old list contains: {my_list}')
print(f'New list contains: {new_list}')

stringlist = [str(i) for i in my_list]
print(stringlist)
intlist = [int(i) for i in stringlist]
print(intlist)
floatlist = [float(i) for i in stringlist]
print(floatlist)

to_be_sum = [[5,10,15],[2,3,6],[100,100,100]]
sum_list = [sum(row) for row in to_be_sum]
print(sum_list) 

find_min_list = [[5,10,15],[2,3,6],[100,100,100]]
min_row = min([sum(row) for row in find_min_list])
print(min_row)
max_row = max([sum(row) for row in find_min_list])
print(max_row)

#user input into list

inp = input('Enter Numbers separated by spaces: ')
nums = [int(i) for i in inp.split()]
print(nums)

rooting = [10, 20, 17, 18, 22]
max_squared = [max(math.sqrt(i) for i in rooting)]

print(rooting)
print(max_squared)


#CONDITIONAL COMPREHENSION

numbers = [12, 123, 14, 15, 16, -16, 17, 18, 19, -20]

odd_nums = [i for i in numbers if (i % 2 == 1)]
print(odd_nums)
neg_nums = [i for i in numbers if (i < 0)]
print(neg_nums)

# Read input
num_rows = int(input())
input_list = []
for i in range(num_rows):
    input_list.append([int(x) for x in input().split()])

computed_value = sum([len(i) for i in input_list])

print(f'All numbers: {input_list}')
print(f'Total number of elements: {computed_value}')