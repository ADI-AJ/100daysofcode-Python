import random  # Importing the random module to generate random numbers

# Welcome message for the player
print("Welcome to the Number Guessing Game!\n")

# Explaining the range of numbers to the player
print("I'm thinking of a number between 1 and 100 \n")

# Function to determine the number of chances based on difficulty level
def chances():
    # Prompting the user to select a difficulty level
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    chance = 0  # Initializing the number of chances
    
    # Assigning chances based on the difficulty level chosen
    if difficulty == 'easy':
        chance = 10  # Easy level gives 10 chances
    elif difficulty == 'hard':
        chance = 5  # Hard level gives 5 chances
    return chance  # Returning the number of chances

# Main game function
def game(chance):
    # Generating a random number between 1 and 100
    correct_number = random.randint(1, 100)
    
    # Loop to allow the player to guess until chances run out
    while chance != 0:
        # Displaying the remaining number of attempts
        print(f"\nYou have {chance} attempts remaining to guess the number.\n")
        
        # Taking the player's guess as input
        guess = int(input("Make a guess: "))
        
        # Checking if the guess is correct
        if guess == correct_number:
            print(f"Congrats! Your guess is correct. The number is {correct_number}")
            break  # Exiting the loop if the guess is correct
        elif guess < correct_number:
            # Hint if the guess is less than the correct number
            print("Guessed number is less than the correct number")
        else:
            # Hint if the guess is greater than the correct number
            print("Guessed number is greater than the correct number")
        
        # Reducing the number of chances after each guess
        chance -= 1
        
        # Message when the player runs out of attempts
        if chance == 0:
            print(f"\nYou lost the game. The number was {correct_number}")

# Starting the game by calling the game function with chances
game(chances())
