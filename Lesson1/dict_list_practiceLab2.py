''' Type your code here. '''
inp = input('Enter a list of integers separated by spaces: ')
intlist = [int(num) for num in inp.split()]

intlist= [x for x in intlist if x<0]
'''
for pos, val in enumerate(intlist[:]):
    if val >= 0:
        intlist.remove(pos)
'''
intlist.sort(reverse=True)
for i in intlist:
    print(f'{i}', end=' ')