import random

rock = '''
    _______
---'   ____)
      (_____ )
      (_____ )
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")

# Get user move
player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Validate input
if player_move < 0 or player_move > 2:
    print("Invalid input! Please choose 0, 1, or 2.")
else:
    comp_move = random.randint(0, 2)

    print("\nYou chose:")
    print(moves[player_move])
    print("Computer chose:")
    print(moves[comp_move])

    if player_move == comp_move:
        print("It's a tie!")
    elif (player_move == 0 and comp_move == 2) or \
         (player_move == 1 and comp_move == 0) or \
         (player_move == 2 and comp_move == 1):
        print("You Win!")
    else:
        print("Computer Wins!")
