# ----- Design Tool - PseudoCode ---------
# Create main function and inside the main function enter the variables codes for input and output
# Enter variables with input request to the use
# print user input result
# Create new variables to calculate the newWeight and height
# Print result from new variables
#  call main function main() for inside code to display

# ------ Comment Header -----------
# name: Jean Carlo Valderrama
# Date : June 5, 2021
# Purpose : Input and Output homework



def main():
    firstName = input('Hi please type your first name:')
    print("Your first name is",firstName)
    lastName = input('Hi please type your last name:')
    print("Your last name is", lastName)
    height = input('Hi please type your height:')

    weight = input('Hi please type your weight:')

    daysRunning = input('Hi please type the number of days has gone running:')

    newBodyWeight = float(weight) - (float(daysRunning) * .5)

    heightAssumption = 1.5 * 3 + 3.4 * 2
    # print(heightAssumption)
    newHeight = float(heightAssumption) + float(height)
    print("Hello", firstName, lastName)
    print("Your weight is", weight)
    print("Your are", height, " feet tall")
    print('Days ran is', daysRunning)
    print('Based on your exercise you now weight', newBodyWeight, "pounds")
    print('If you stood on 3 stools and 2 chairs you would be', newHeight, 'feet tall')

# main()
main()
