#Welcome to a game of Rock, Paper, Scissors!

import random
rounds = int(input("How many rounds would you like to play: "))

moves = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

for play in range (1, rounds+1):
    print("\nRound " + str(play))
    print("Player: " + str(player_score) + "\t Computer: "+ str(computer_score))
    player_pick = input("Time to pick ... rock, paper, scissors: ").lower().strip()

    if player_pick not in moves:
        print("This is an invalid choice.")
    else:
        random_pick = random.randint(1,3)
        computer_pick = moves[random_pick]
        print("\tComputer: " + computer_pick)
        print("\tPlayer: " + player_pick)

        



