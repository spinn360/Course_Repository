cont = True
while cont:
    input1 = int(input('\nEnter the first number: '))
    input2 = int(input('Enter the second number: '))
    while input1 == input2:
        print('Numbers must be different.')
        break
    
    if input1 < input2:
        for i in range(input1, input2 + 1):
            print(i, end=' ')
    else:
        for i in range(input1, input2 - 1, -1):
            print(i, end=' ')

    if input1 == 99 or input2 == 99:
        cont = False
