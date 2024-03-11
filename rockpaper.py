import random
from colorama import Fore

"""Problem #1
Play the game Rock Papar Scissors with the computer.
Play it three times and best of three wins. 
If you win, print your name in color (look for a python package to do this)
Hint - Use random number generation"""

choices = ['rock', 'paper', 'scissors']
player_point = 0
computer_point = 0

def prnt(player_point, computer_point, player_choice, computer_choice):
    print(Fore.GREEN + f"| COMPUTER POINT: {computer_point}")
    print(f"| PLAYER POINT: {player_point}")
    print(f"| COMPUTER CHOICE: {computer_choice}")
    print(f"| PLAYER CHOICE: {player_choice}" )

while True:
    player_choice = input("---------------------------------\nChoose: rock, paper, or scissors: \n---------------------------------\n").lower()
    computer_choice = random.choice(choices)

    if player_choice not in choices:
        print("Invalid choice.")
        continue
    elif player_choice == computer_choice:
        player_point += 1
        computer_point += 1
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        player_point += 1
    else:
        computer_point += 1
    prnt(player_point, computer_point, player_choice, computer_choice)

    if player_point == 3:
        print("Best of three times. User Wins")
        break
    elif computer_point == 3:
        print("Best of three times. Computer Wins")
        break