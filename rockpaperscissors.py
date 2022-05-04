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
        print("That is not a valid game option.") 
        print("Computer gets the point.")
        computer_score += 1
    else:
        random_pick = random.randint(0,2)
        computer_pick = moves[random_pick]
        print("\tComputer: " + computer_pick)
        print("\tPlayer: " + player_pick)

        if computer_pick == player_pick:
            print("\tIt's a tie. How boring!")
            print("\tThis round is a draw.")
        else:
            if computer_pick == "rock":
                if player_pick == "paper":
                    print("\tPaper wins against rock.")
                    print("\tYou win round "+ str(play) + ".")
                    player_score += 1
                elif player_pick == "scissors":
                    print("\tRock wins against scissors")
                    print("\tComputer wins round "+ str(play) + ".")
                    computer_score += 1
            elif computer_pick == "scissors":
                if player_pick == "rock":
                    print("\tRock wins against scissors.")
                    print("\tYou win round "+ str(play) + ".")
                    player_score += 1
                elif player_pick == "paper":
                    print("\tScissors wins against paper")
                    print("\tComputer wins round "+ str(play) + ".")
                    computer_score += 1
            elif computer_pick == "paper":
                if player_pick == "scissors":
                    print("\tScissors wins against paper.")
                    print("\tYou win round "+ str(play) + ".")
                    player_score += 1
                elif player_pick == "rock":
                    print("\tPaper wins against rock")
                    print("\tComputer wins round "+ str(play) + ".")
                    computer_score += 1

print("\nFinal Score:")
print("Player: " + str(player_score) + "\t Computer: "+ str(computer_score))
if player_score > computer_score:
    print("\nYou won the game. Congratulations!!!")
elif computer_score > player_score:
    print("\nOops. Computer won the game!!!")
else:
    print("\nThe match is a draw!")




