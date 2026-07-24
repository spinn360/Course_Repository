userinput = input('Enter a number or q to quit: ')
while userinput != 'q':
    try:
        calc = int(userinput) * 11
        print(calc)

        userinput=('Enter a number or q to quit: ')
    except:
        print('could not calc non number\n')
    userinput =input('Enter a number or q to quit: ')