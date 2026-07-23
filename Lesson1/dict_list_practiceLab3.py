''' Type your code here. '''
inp = input('Enter a list of integers separated by spaces: ')
inprange = input('Enter the range (min max): ')
intList = [int(num) for num in inp.split()]
intrangelist = [int(num) for num in inprange.split()]
rangedList = [num for num in intList if num >= intrangelist[0] and num <= intrangelist[1]]
'''print(intList)
print(intrangelist)
print(rangedList)'''
for i in rangedList:
    print(i, end=',')