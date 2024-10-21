import random

ascii_art = {
    0: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    1: """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""",
    2: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
}

def game(player1,player2):
    print(f'You chose \n')
    print(ascii_art[player1], '\n')
    print(f'Your oponent chose \n')
    print(ascii_art[player2], '\n')
    if player1 == player2:
        print("Draw")
    elif player1 == 0 and player2 == 2:
        print('You won')
    elif player1 == 2 and player2 == 0:
        print('You lose')
    elif player1 > player2:
        print('You won')    
    else:
        print('You lose')

player1 = int(input('Type 0 for Rock, 1 for Paper and 2 for Scissors\n').lower())
player2 = random.randint(0,2)

game(player1,player2)