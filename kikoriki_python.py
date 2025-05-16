#!/user/bin/env python3

# Alexander Egerev
# February 26, 2025

import random

# This is the combination for the game
def combination_generator():
    symbols = ["🍎", "🍌", "🍒", "🍇", "🍖", "X"]
    combination = [random.choice(symbols) for _ in range(4)]
    return combination;

# The function that contains everything needed for the game
def play_game():
    print("Welcome to the KikOriki Slot Machine game!")

    while True:
        input("Enter any word you want, then press Enter to activate the slot machine... ")
        combo = combination_generator()
        print(combo)

        if "X" in combo:
            print("There is an X in the combination - you lost.")
            
            one_more_round = input("Play again? (yes/no)")
            if one_more_round == "yes" or one_more_round == "Yes":
                continue
            else:
                print("(c)2025 Alexander E. All rights reserved.")
                print("\n")
                print("This game is based on the KikOriki episode 'A Big Share'.")
                print("TM and © ООО «Смешарики», 2003. All Rights Reserved.")
                break
        else:
            print("You Win!")
            
            one_more_round = input("Play again? (yes/no)")
            if one_more_round == "yes" or one_more_round == "Yes":
                continue
            else:
                print("(c)2025 Alexander E. All rights reserved.")
                print("\n")
                print("This game is based on the KikOriki episode 'A Big Share'.")
                print("TM and © ООО «Смешарики», 2003. All Rights Reserved.")
                break

# Calling the function to play the game
play_game()
