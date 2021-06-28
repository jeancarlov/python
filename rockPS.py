# ----- Design Tool - PseudoCode ---------
# create a count variable for the wins losses and ties
#  S < R <P < S
# Create while loop to run the game until the user wants to stop with a break
# Create if statement to compared the user and the computer choices and to determined the results
# Print result
# all code must be inside the function main code block

# ------ Comment Header -----------
# Name: Jean Carlo Valderrama
# Date : June 26, 2021
# Purpose : RPS homework
from datetime import date
import random


def main():
    userWins = 0
    # print(userWins)
    computerWins = 0
    currentWinStreak = 0
    currentLoseStreak = 0
    longestWinStreak = 0
    longestLoseStreak = 0
    gameTies = 0
    while True:
        choices = ["rock", "paper", "scissors"]
        # print(computerWins)

        userChoice = (input("Please enter pick  either rock, paper,  scissors, quit:  "))
        if userChoice in ['Rock', "rock", "r", "R"]:
            userChoice = "rock"
        if userChoice in ['Paper', "paper", "p", "P"]:
            userChoice = "paper"
        if userChoice in ['Scissors', "scissors", "s", "S"]:
            userChoice = "scissors"
        if userChoice in ['Quit', "quit", "q", "Q"]:
            userChoice = "quit"
        while userChoice not in choices:
            userChoice = input('please try again press enter').lower()
            main()
        # while userChoice != userChoice:
        #     userChoice = input("Invalid input please try again press enter")
        #     main()
        # for i in userChoice:
        #     if userChoice != i:
        #         print(input("Invalid input please try again press enter"))
        #         main()

        print("You selected:", userChoice)
        computerChoice = ["rock", "paper", "scissors"]
        computerRandom = random.choice(computerChoice)
        print("Computer Selected", computerRandom)

        print(f"\nYou chose {userChoice}, computer chose {computerRandom}.\n")
        if userChoice == "quit":
            print("You selected", userChoice, "try the game later")

        # Rock
        if userChoice == computerRandom:
            print(f"\n both players selected {userChoice}, is a tie. Try again\n")
            gameTies += 1
        elif userChoice == "rock":
            if computerRandom == "scissors":
                print(" Rock beats Scissors! user win")
                userWins += 1
                currentWinStreak += 1
                longestWinStreak += 1

            else:
                computerWins += 1
                currentLoseStreak += 1
                longestLoseStreak += 1
                print('paper covers rock. user lose ')

        # Paper
        elif userChoice == "paper":
            if computerRandom == "rock":
                userWins += 1
                currentWinStreak += 1
                longestWinStreak += 1
                print("paper covers rock. user wins ")

            else:
                computerWins += 1
                currentLoseStreak += 1
                longestLoseStreak += 1
                print('Scissors cuts paper. user lose ')

        # Scissors
        elif userChoice == "scissors":
            if computerRandom == "paper":
                userWins += 1
                currentWinStreak += 1
                longestWinStreak += 1
                print("Scissors cuts paper. user wins ")

            else:
                computerWins += 1
                currentLoseStreak += 1
                longestLoseStreak += 1
                print('Scissors cuts paper. user lose ')

        print("")
        print("Total wins: " + str(userWins))
        print("Total loses: " + str(computerWins))
        print("Game Ties: " + str(gameTies))
        print("Current win streak: " + str(currentWinStreak))
        print("Current lose streak: " + str(currentLoseStreak))
        print("Longest win streak: " + str(longestWinStreak))
        print("Longest lose streak: " + str(longestLoseStreak))


        print("")

        repeat = input("Play again? (Y/N) ").lower()
        while repeat not in ['y', 'n']:
            repeat = input("That is not a valid choice. Please try again: ").lower()

            if repeat == 'n':
                break

        print("\n----------------------------\n")



    # main()
main()
