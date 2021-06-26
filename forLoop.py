# ----- Design Tool - PseudoCode ---------
# Create main function and inside the main function enter the variables codes for input and output
# Display Menu options and request user to make a selection
# Enter variables with input request to the use
# print user input result
# Create if statements to check if variable number match choice selection
# Create def functions and add to each if statement
# Print result from new variables
#  call main function main() for inside code to display

# ------ Comment Header -----------
# Name: Jean Carlo Valderrama
# Date : June 20, 2021
# Purpose : Decision B homework
from datetime import date


def main():

    userChoice = int(input("Please enter how many lines you want: "))
    charChoice = str(input('Please type the keyboard character:'))
    for x in range(1, userChoice+1):
        print({charChoice}* x)
# main()
main()
