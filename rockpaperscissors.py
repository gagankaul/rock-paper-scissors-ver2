#Welcome to a game of Rock, Paper, Scissors!

import random

#Get user input
rounds = int(input("How many rounds would you like to play: "))

#Initialize variables
moves = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

#The main game loop
for play in range (1, rounds+1):
    #Print the main game screen and get user input
    print("\nRound " + str(play))
    print("Player: " + str(player_score) + "\t Computer: "+ str(computer_score))

    #Get computer move
    c_index = random.randint(0,2)
    computer_pick = moves[c_index]

    #Get player move
    player_pick = input("Time to pick ... rock, paper, scissors: ").lower().strip()

    if player_pick not in moves:
        print("That is not a valid game option.") 
        print("Computer gets the point.")
        computer_score += 1
    else:
        print("\tComputer: " + computer_pick)
        print("\tPlayer: " + player_pick)

        if computer_pick == player_pick:
            print("\tIt's a tie. How boring!")
            print("\tThis round is a draw.")
        else:
            if computer_pick == "rock":
                if player_pick == "paper":
                    message = "Paper wins against rock."
                    winner = "player"
                elif player_pick == "scissors":
                    message = "Rock wins against scissors."
                    winner = "computer"
            elif computer_pick == "scissors":
                if player_pick == "rock":
                    message = "Rock wins against scissors."
                    winner = "player"
                elif player_pick == "paper":
                    message = "Scissors wins against paper."
                    winner = "computer"
            elif computer_pick == "paper":
                if player_pick == "scissors":
                    message = "Scissors wins against paper."
                    winner = "player"
                    player_score += 1
                elif player_pick == "rock":
                    message = "Paper wins against rock."
                    winner = "computer"
        
        #Display round results
        print("\t" + message)
        if winner == "player":
            print("\tYou win round " + str(play) + ".")
            player_score += 1
        elif winner == "computer":
            print("\tComputer wins round " + str(play) + ".")
            computer_score += 1
        else:
            print("\tThis round is a tie.")

#Display final game results and declare the winner
print("\nFinal Game Results:")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(player_score))
print("\tComputer Score: " + str(computer_score))
if player_score > computer_score:
    print("\nYou won the game. Congratulations!!!")
elif computer_score > player_score:
    print("\nOops. Computer won the game!!!")
else:
    print("\nThe match is a draw!")