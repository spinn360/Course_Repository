import random
# TODO: Import the random module

def number_guess(num):
    random_number = random.randint(1, 100) # Get a random number between 1-100
    # TODO: Get a random number between 1-100
    if num == random_number:
        print(f"Congratulations! You guessed the number {random_number}.")
    elif num < random_number:
        print(f"Your guess of {num} is too low. The number was {random_number}.")
    else:
        print(f"Your guess of {num} is too high. The number was {random_number}.")
    # TODO: Compare parameter num to the random number
    
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)