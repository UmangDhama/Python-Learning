from game_data import data
from art import logo,vs
import random


def higher_lower():


    first_player = data[random.randint(0, 49)]
    used_players = [first_player]

    score = 0
    game_over = False
    while not game_over:
        second_player = data[random.randint(0, 49)]
        while second_player in used_players:
            second_player = data[random.randint(0, 49)]

        used_players.append(second_player)
        print(logo)
        print(f"Compare A: {first_player['name']}, {first_player['description']}, from {first_player['country']}")
        print(vs)
        print(f"Against B: {second_player['name']}, {second_player['description']}, from {second_player['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_followers = first_player["follower_count"]
        b_followers = second_player["follower_count"]

        if (guess == 'A' and a_followers > b_followers) or (guess == 'B' and b_followers > a_followers):
            score += 1
            print(f"You're right! Current score: {score}\n")
            first_player = first_player if guess == 'A' else second_player
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


higher_lower()