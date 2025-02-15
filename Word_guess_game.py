import random

# List of words for the game
word_list = ['bat', 'alien', 'ant']

# Choosing a random word from the list
word = random.choice(word_list)
visible_word = '_' * len(word)  # Replacing all characters with underscores
life = 3  # Number of lives for the player

# Main game loop
while True:
    # Prompting the user to guess a letter
    guess = input('Guess a letter: ').lower()

    # If the guessed letter is in the word
    if guess in word:
        # Replacing '_' with the guessed character
        for i,char in enumerate(word):
            if char==guess:
                visible_word = visible_word[:i]+guess+visible_word[i+1:]
    else:
        # Decrease life on a wrong guess
        print('Wrong guess!')
        life -= 1

    # Display the updated word and remaining lives
    print('Word:', visible_word)
    print('Lives left:', life)
    print('\n')

    # Check for game-ending conditions
    if life == 0:
        print('You lost the game, fellow human! The word was:', word)
        break
    elif '_' not in visible_word:
        print('Congratulations, human! You won!')
        break
