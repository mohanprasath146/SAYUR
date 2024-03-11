import random
"""Problem #3
Write an app for the follwoing two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game. """

def roll_dice():
    return random.randint(1, 6)

def calculate_points(roll):
    points_dict = {1: 1, 2: 5, 3: 15, 4: -15, 5: -5, 6: -1}
    return points_dict.get(roll, 0)

def play_game():
    player1_points = 0
    player2_points = 0
    rolls = 0

    while player1_points < 100 and player2_points < 100:
        rolls += 1
        n=int(input("____________________________________\n1.Player 1 to roll dice (ENTER : 1)\n2. Player 2 to roll dice(ENTER : 2)\n_________________________________\n"))
        if n==1:
            roll = roll_dice()
            player1_points += calculate_points(roll)
            print("Player 1 Point:", player1_points)
        elif n==2:
            roll = roll_dice()
            player2_points += calculate_points(roll)
            print("Player 2 Point:", player2_points)
        else:
            print("ENTER VALID NUMBER !!!!!!")
    return "Player 1 wins in {} rolls" if player1_points >= 100 else "Player 2 wins in {} rolls".format(rolls)

print(play_game())
