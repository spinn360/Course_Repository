print('name\tbob\njob\tdeveloper')

cd = 'rap'
artist = '360'
albumn = 5

print('There is a new',artist,'cd called',cd, 'and it is number',albumn)
print(cd,type(cd))
print(artist,type(artist))
print(albumn,type(albumn))
cd:str = 'rap'
artist:str = '360'
albumn:int = 5

print('There is a new',artist,'cd called',cd, 'and it is number',albumn)
print(cd,type(cd))
print(artist,type(artist))
print(albumn,type(albumn))

print(int(artist) + albumn)
best_friend = 'Timmy'
print('Enter your best friend',end= ' ') 
best_friend = input()
print('Your best friend is named', best_friend)