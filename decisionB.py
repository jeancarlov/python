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
# Date : June 13, 2021
# Purpose : Decision B homework
from datetime import date


def main():
    print('1. Get name then display name')
    print('2. Get Age then display statement')
    print("3. Today's date ")
    print('4. Quit')
    choice = input('Enter selection:')
    if choice == '1':
        displayName()
    if choice == '2':
        ageDisplay()
    if choice == '3':
        displayDate()
    if choice == '4':
        print('Thanks for trying program ended.')


def displayName():
    userName = input('What is your name: ')
    print('hello', userName, ", have a good day.")


def ageDisplay():
    userAge = input('What is your age: ')
    if float(userAge) <= 10:
        print(' You are only', userAge, 'go to bed')
    if 10 <= float(userAge) <= 20:
        print(' This age would display no output')
    if 21 <= float(userAge) <= 60:
        print("Since you are", userAge, "let's go have a drink.")
    elif float(userAge) >= 61:
        print( 'Wow,', userAge, ' is really old.')

def displayDate():
    today = date.today()
    today = today.strftime(" %m/%d/%y")
    print(" Today's date:", today)

# main()
main()

userNumberLines = input('Hi please type a number from 1 - 50: ')
print('hello', userNumberLines, ", have a good day.")
if int(userNumberLines) <= 50:
    print(' Thanks your number is with in 1 - 50')
else:
    print('please try again ')

userKeyword = input('Enter a character from the keyboard: ')
print('your keyboard character is :', userKeyword, )
# newResult = ''.join([char * userNumber for char in userKeyword])
# print(newResult)
for userNumberLine in userNumberLines:
    print(str(userKeyword) * userNumberLine)
# print(x.replace(userNumber, userKeyword, 50))


userNumberLines = input('Hi please type a number from 1 - 50: ')
    print('hello', userNumberLines, ", have a good day.")
    print("Twice the number you give: {number}".format(number=userNumberLines * 2))

    if int(userNumberLines) <= 50:
        print(' Thanks your number is with in 1 - 50')
    else:
        print('please try again ')

    userKeyword = input('Enter a character from the keyboard: ')
    print('your keyboard character is :', userKeyword, )
    # newResult = ''.join([char * userNumber for char in userKeyword])
    # print(newResult)
    for userNumberLine in userNumberLines:
        print(str(userKeyword) * userNumberLine)