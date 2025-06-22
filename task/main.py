import random
from hangman_art import stages, logo
word_list = ["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder_string = ["_"] * len(chosen_word)
print(placeholder_string)
life=6
while "_" in placeholder_string and life>0:
    character=input("Enter the character")
    if character in chosen_word:
        positions = [i for i, c in enumerate(chosen_word) if c == character]
        for i in range(0,len(positions)):

            placeholder_string[positions[i]]=character
        print(placeholder_string)
    else:
        life-=1
        print("The Character in not in the Word")
        print(f"life left: {life}")
    print(stages[life])

print('Game Over! Hang man died!')






# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word



# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.



