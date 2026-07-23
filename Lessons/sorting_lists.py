nums = [100, 8, -7, 35, 1000]
print(nums) # print unsorted nums list
print(nums.sort()) # nums.sort() sorts the list, but print produces None
#for i in nums: #print each value of nums that has already been sorted
#    print(i)
print(nums) # print sorted nums list
nums.sort(reverse=True)
print('reversed',nums)
# different then sorted() method which makes a copy and sorts the list but
# does not alter the original as list.sort() does
num1 = [1,3, 7, -8, -9, 10, -11]
print(sorted(num1))
print('reversed',sorted(num1, reverse=True))
print(num1)
num2 = [[18, 17, 13, 12],[11, 35, 20],[7, 6, 1]]
print(sorted(num2, key=max))
names = ['John Jacob', 'mary Duright', 'Ford Fallon', 'Angel Zod', 'angel Berut']
print(names)
sorted_names = sorted(names)
print(sorted_names)
sorted_names = sorted(names, key=str.lower)
print(sorted_names)
sorted_names.sort(key=str.upper)
print(sorted_names)

