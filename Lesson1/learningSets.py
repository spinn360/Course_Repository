nums1 = set([1 , 2, 3])
nums2 = {7, 8, 9}
print(nums1, type(nums1))
print(nums2, type(nums2))

#Set is often used to reduce duplicates from a list

mylist = ('John', 'brady', 'sally', 'sally', 'sally', 'John', 'George')
mySet = set(mylist) # note you cannot simply say mySet = mylist because it doesn't change the type
# much as ensuring and input is an int by int(input()) use set(n) to change n
print(mySet)

mySet.add('Jeff')
print(mySet)
mySet.remove('sally')
print(mySet)
mySet.pop()

print(mySet)

#Adding multpile sets together

set1 = set([8, 6, 7, 5])
set2 = set([3, 0, 9])
print(type(set1))
print(type(set2))
set1.update(set2)
print(set1)
set1.add(1)
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set3 = {1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 10, 11, 11, 12}
print(type(set3))
print(set3)
mySet.update(set3)
print('set1')
print(set1)
print('set1 intersection set1, set2, set3, mySet')
print(set1.intersection(set1, set2, set3, mySet))
print('set1 union set1, set2, set3, mySet')
print(set1.union(set1, set2, set3, mySet))
print('set1 difference set1, set2, set3, mySet')
print(set1.difference(set1, set2, set3, mySet))
print('set1 symmetric difference mySet')
print(set1.symmetric_difference(mySet))
set3.clear()
print(set3)
monsters = {'Gorgon', 'Medusa'}
trolls = {'William', 'Bert', 'Tom'}
horde = {'Gorgon', 'Bert', 'Tom'}
print(monsters.union(trolls)) # joins elements of the sets together
print(monsters.symmetric_difference(horde)) # results in that are not found in both

names_set1 = {'Ava'}
names_set2 = set()
names_set2.add(input('enter value: '))
names_set2.add(input('enter value: '))

names_set1.add(input('enter value: '))
names_set1.update(names_set2)
names_set2.pop()

print(f'names_set1: {sorted(names_set1)}')
print(f'names_set2 size: {len(names_set2)}')


