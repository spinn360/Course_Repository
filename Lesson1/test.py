'''threshold = int(input())
for a in range(0, 2):
    print(a + 1, end=": ")

    for b in range(0, 3):
        if a > threshold:
            print("_,", end="")
            continue

        print(b, end=",")

    print()'''
color_popularities = [input(), input(), input()]

for k, color in enumerate(color_popularities):
    print(f'#{k + 1}: {color}')

numbers = [3, 6, -2, -7]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} {number}')
    else:
        print(f'{position} x')

#simon says comparing a string by its index using len() function
user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in range(len(simon_pattern)):
    if simon_pattern[i] == user_pattern[i]:
        user_score += 1
    else:
        break 

print(f'User score: {user_score}')

# .index() do not use this method as it searches only the first occurence in a string if
# repeat characters exist it will error (bug)

user_score = 0
simon_pattern = input()
user_pattern  = input()

for simon_char in simon_pattern:
    i = simon_pattern.index(simon_char) # Finds the index of the character
    
    if simon_char == user_pattern[i]:
        user_score += 1
    else:
        break 

print(f'User score: {user_score}')


#enumerate() function instead
user_score = 0
simon_pattern = input()
user_pattern  = input()

for i, simon_char in enumerate(simon_pattern):
    if simon_char == user_pattern[i]:
        user_score += 1
    else:
        break 

print(f'User score: {user_score}')


'''Integer num_colors is read from input, representing the number of color names 
to be read from input. List colors_list contains the color names read from the 
remaining input. For each element in colors_list, output:

'Color: '
the element
', Popularity ranking: '
the element's index in the list plus one'''

num_colors = int(input())

colors_list = []
for i in range(num_colors):
    colors_list.append(input())

for k, color in enumerate(colors_list):
    print(f'Color: {color}, Popularity ranking: {k + 1}')

'''Integer num_samples is read from input, representing the 
number of candidate names to be read from input. List 
candidates_list contains the candidate names read from the 
remaining input. For each element in candidates_list:

If the element's index is odd, output the element followed by ' to Hall 862'.
Otherwise, output the element followed by ' to Hall 939'.

Note: x % 2 != 0 returns True if x is odd.'''


num_samples = int(input())

candidates_list = []
for i in range(num_samples):
    candidates_list.append(input())

for j, candidate in enumerate(candidates_list):
    if j % 2 != 0:
        print(f'{candidate} to Hall 862')
    else:
        print(f'{candidate} to Hall 939')