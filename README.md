# KikOriki Slot Machine Game

This is a simple slot machine game implemented in Python 3. It's inspired by the "A Big Share" episode of the Russian animated series *KikOriki* (also known as *Smeshariki*).

## How to Play

1.  Make sure you have Python 3 installed on your system.
2.  Save the provided code as a Python file (e.g., `kikoriki_slot.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the game by executing the command: `python kikoriki_slot.py`
6.  The game will prompt you to "Enter any word you want, then press Enter to activate the slot machine...". Type anything and press Enter.
7.  A combination of four symbols will be displayed: `🍎`, `🍌`, `🍒`, `🍇`, `🍖`, or `X`.
8.  **Winning:** If the combination does not contain the symbol `X`, you win!
9.  **Losing:** If the combination contains one or more `X` symbols, you lose.
10. After each round, you'll be asked if you want to play again. Type `yes` or `Yes` to continue, or anything else to quit.

## Game Logic

The game works as follows:

* The `combination_generator()` function randomly selects four symbols from the list: `["🍎", "🍌", "🍒", "🍇", "🍖", "X"]`.
* The `play_game()` function handles the game loop:
    * It prompts the user to spin the slot machine.
    * It generates a new combination of symbols.
    * It displays the generated combination.
    * It checks if the symbol `X` is present in the combination.
    * If `X` is present, the player loses.
    * If `X` is not present, the player wins.
    * It asks the player if they want to play another round.
    * If the player chooses not to play again, a copyright notice and a message about the game's inspiration are displayed before the game ends.

## Copyright
(c)2025 Alexander E. All rights reserved. <br/>

This game is based on the KikOriki episode 'A Big Share'.
TM and © ООО «Смешарики», 2003. All Rights Reserved.

This game is a fan-made project inspired by the *KikOriki* episode "A Big Share". *KikOriki* (Смешарики) and its characters are intellectual property of ООО «Смешарики». All rights related to the original animated series belong to them.
