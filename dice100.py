import random

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
        n=int(input("____________________________________\n1.Player 1 to roll dice (ENTER : 1)\n2. Player 2 to roll dice(ENTER : 2)\n"))
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
