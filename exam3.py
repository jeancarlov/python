# ----- Design Tool - PseudoCode ---------
# Create Functions for each exam
# Create Function to get exam score
# create Function to Display all Exam Scores
# create function for the exam grades chart
# Create function for high to low and low to high scores (sort)
# Create Function to Display exam Statistics
# Create a function to adjust all exam scores
# Create a function to remove all f grades from the list
# use type to check that input is an integer and not a letter
# verify result of output by using print and adding comments if necessary
# check every function and result prior to completion
# all code inside main function

# ------ Comment Header -----------
# Name: Jean Carlo Valderrama
# Date : July 25, 2021
# Purpose : Grading score tracker exam 3

def examOne(prompt, scores):
    # While True loop keeps asking user for number until they enter
    # a number from 0 - 100
    while True:
        # If user does not enter an integer, program will go to except
        # statement
        try:
            type = int(input(prompt))
        except ValueError:
            print('Value must be between 0 and 100. Please re-enter.')
            continue
        else:
            # If they entered a number not in the range 0 - 100, makes them
            # enter another number
            if type < 0 or type > 100:
                print('Value must be between 0 and 100. Please re-enter.')
                continue
            scores.append(type)
            break


def moreExamScoreUntil999(prompt, scores):
    while True:
        # If user does not enter an integer, program will go to except
        # statement
        try:
            type = int(input(prompt))
            # Keeps asking for scores until they enter -999
            if type == -999:
                break
        except ValueError:
            print('Value must be between 0 and 100. Please re-enter.')
            continue
        else:
            # If they entered a number not in the range 0 - 100, makes them
            # enter another number
            if type < 0 or type > 100:
                print('Value must be between 0 and 100. Please re-enter.')
                continue
            scores.append(type)


def getGrade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    elif score < 100:
        return 'A'


def displayAscending(scores):
    # Sorts the list from small to big
    scores.sort()

    # Goes through every score and converts it to its letter grade
    # Prints both score and letter out
    for score in scores:
        print(str(score) + ' - ' + getGrade(score))


def displayDescending(scores):
    # Sorts the list from big to small
    scores.sort(reverse=True)

    # Goes through every score and converts it to its letter grade
    # Prints both score and letter out
    for score in scores:
        print(str(score) + ' - ' + getGrade(score))


def statistics(scores):
    # Get highest, lowest and average score and output them
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    print('Number of scores entered: ' + str(len(scores)))
    print('Highest score so far: ' + str(highest) + ' - ' + getGrade(highest))
    print('Lowest score so far: ' + str(lowest) + ' - ' + getGrade(lowest))
    print('Average score: ' + str(average) + ' - ' + getGrade(average))

    # Go through every score, get its letter grade and add 1 to the amount of that letter grade
    # in this grade_count dictionary
    grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for score in scores:
        grade_count[getGrade(score)] += 1

    print('\nGRADE COUNT:')
    for grade in grade_count:
        print(grade + ' - ' + str(grade_count[grade]))


def adjustScores(scores):
    # Go through every score and take away 5
    for x in range(len(scores)):
        scores[x] -= 5

        # If the score would go below 0, set it to 0
        if scores[x] < 0:
            scores[x] = 0

    print('Successfully deducted 5% from every score')


def removeFGrades(scores):
    # Create copy of scores and clear the old list of scores
    old_scores = scores.copy()
    scores.clear()

    # Iterate through every score, if it is not an F grade, add it back to the scores list
    for score in old_scores:
        if score >= 60:
            scores.append(score)

    print('Successfully removed all F grades')


def main():
    # Create empty scores list to start
    scores = []

    # Keeps displaying menu until user picks option 7 (quit the program)
    while True:
        # Displays menu options
        print('MAIN      MENU')
        print('1) Get one exam score')
        print('2) Get exam scores until user enters -999')
        print('3) Display all exam scores entered')
        print('4) Display exam statistics')
        print('5) Adjust all exam scores')
        print('6) Remove all F grades from the list')
        print('7) Quit the program')
        option = input('Select an option: ')
        print()
        if option == '1':
            # Prompts user to enter their exam score
            examOne('Please enter your exam one score between 0 - 100: ', scores)
        elif option == '2':
            # Prompts user to enter their exam scores
            moreExamScoreUntil999('Please enter your exam one score between 0 - 100: ', scores)
        elif option == '3':
            print('1) From highest to lowest')
            print('2) From lowest to highest')
            option = input('Select an option: ')
            print()
            if option == '1':
                displayDescending(scores)
            elif option == '2':
                displayAscending(scores)
            else:
                print('Invalid option')
        elif option == '4':
            statistics(scores)
        elif option == '5':
            adjustScores(scores)
        elif option == '6':
            removeFGrades(scores)
        elif option == '7':
            print('Thank you for using this program')
            exit()
        else:
            print('Invalid option')
        print()


main()
