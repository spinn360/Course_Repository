''' generate a random number guesser'''
import random
cont = True
while cont == True:


    num = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 10: "))
    print(f"The random number is {num}")
    # if guessed correctly, print   
    if num == int(guess):
        print('You win')
        cont = False

    else:
        print('You lose')
print("Try again")

