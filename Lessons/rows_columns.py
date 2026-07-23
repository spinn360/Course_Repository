num_rows = int(input())
num_columns = int(input())
number1= 1
letter2 = 'A'

for i in range(num_rows):
    for j in range(num_columns):
        print(str(number1)+letter2, end=" ")
        letter2 = chr(ord(letter2) + 1)
    number1 += 1
    letter2 = 'A'   
    print()