# ----- Design Tool - PseudoCode ---------
# create a count variable for the wins losses and ties
#  S < R <P < S
# Create while loop to run the game until the user wants to stop with a break
# Create if statement to compared the user and the computer choices and to determined the results
# Print result
# all code must be inside the function main code block

# ------ Comment Header -----------
# Name: Jean Carlo Valderrama
# Date : July 11, 2021
# Purpose : Menu function homework
from datetime import date

import random


def main():
    def getChoice():
        print('1. Menu function please make a choice:')
        print('[G] Get a number')
        print('[S] Display current sum')
        print('[A] Display current average')
        print('[H] Display current highest number')
        print('[L] Display the current lowest number')
        print('[Q] Quit     - game over')
        choice = input("Enter your selection: ")
        return choice.upper()  # this converts the value of choice to uppercase

    getChoice()

    #   function getNumber
    #
    def getNum():
        computerRandom = random.randrange(1, 20)
        print(computerRandom)

    getNum()

    #   function for current sum
    def currentSum():
        firstNum = random.randrange(1, 20)
        secondNum = random.randrange(1, 20)
        thirdNum = random.randrange(1, 20)

        sumAll = firstNum + secondNum + thirdNum
        print(sumAll)

    currentSum()


#   function for current average

#   function for current highest number

#   function for current lowest number


# def examOne():
    #     # ExamOneScore = ()
    #     userInputExamOne = (input('input a single exam score: '))
    #     print(userInputExamOne)
    #     if 0 <= int(userInputExamOne) <= 100:
    #         print(' your exam score is in the range of 0 to 100 : ', userInputExamOne)
    #     elif int(userInputExamOne) > 100:
    #         print('do it again', examOne())
    #
    # examOne()
main()
