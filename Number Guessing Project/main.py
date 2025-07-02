from art import logo
import random




def numberguess():
    number = random.randint(1, 100)
    print(logo)

    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    diff_lev = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if diff_lev == "easy":
        lev = 10
    else:
        lev = 5
    gameover=False

    while (lev>0) and not gameover:
            print(f"you have {lev} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))

            if guess==number:
                print(f"You got it! The answer was {number}")
                gameover=True
            elif guess>number:
                print("Too high.\n Guess again.")
                lev-=1
            elif guess<number:
                print("Too low.\n Guess again.")

                lev -= 1
    play_again=""
    if lev==0 :
        play_again = input("You've run out of guesses. Type 'yes' to play again or 'no' if want to exit ").lower()
    elif gameover:
        play_again= input("Type 'yes' to play again or 'no' if want to exit ").lower()

    if play_again=="yes":
        numberguess()
    else:
        return

numberguess()




