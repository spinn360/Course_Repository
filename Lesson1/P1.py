print('name\tbob\njob\tdeveloper') #testing out tab and new line make sure \ and not /

#creating some variables
cd = 'rap' 
artist = '360'
albumn = 5
#printing out using variables
print('There is a new',artist,'cd called',cd, 'and it is number',albumn)
print(cd,type(cd)) #getting type of variable using type() function
print(artist,type(artist))
print(albumn,type(albumn))
cd:str = 'rap'
artist:str = '360'
albumn:int = 5

print('There is a new',artist,'cd called',cd, 'and it is number',albumn)
print(cd,type(cd))
print(artist,type(artist))
print(albumn,type(albumn))
#passing a string to an integer using int(artist)
print(int(artist) + albumn)
best_friend = 'Timmy'
#testing getting inputs
print('Enter your best friend',end= ' ') 
best_friend = input()
print('Your best friend is named', best_friend)
print('enter random things until you dont have to anymore')
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()

print('thank you')
print('You entered', a,b,c,d,e,f)
#probably best to print out something for user to know what input they are on
print('enter random things until you dont have to anymore')
print('6:', end= ' ')
a=input()
print('5:', end= ' ')
b=input()
print('4:', end= ' ')
c=input()
print('3:', end= ' ')
d=input()
print('2:', end= ' ')
e=input()
print('1:', end= ' ')
f=input()
print('thank you')
print('You entered', a,b,c,d,e,f)