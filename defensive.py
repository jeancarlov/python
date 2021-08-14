# ----- Design Tool - PseudoCode ---------
# create main function
#  create input statements for user to type answers
# Create if statements to match result
# create functions inside main functions for question b and c
# Print result
# all code must be inside the function main code block

# ------ Comment Header -----------
# Name: Jean Carlo Valderrama
# Date : July 3, 2021
# Purpose : Defensive programming homework


def main():
    questionA()


def questionA():
    # while True:
    userChoice = int(input("Please type your current age between the range of 21 and 99 : "))
    if 21 <= float(userChoice) <= 99:
        print(userChoice, "your age is between 21 and 99")
        questionB()
        questionC()
    else:
        print(userChoice, "is number NOT between 21 and 99. Please try again")
        main()


def questionB():
    repeat = input("Do you like programming? (Y/N) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()
        if repeat == 'n':
            break
    repeat1 = input("Do you think programming started in 1800s? (Y/N) ").lower()
    while repeat1 not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()
        if repeat == 'n':
            break
    yIsTrue = 'true'
    nIsFalse = 'false'
    if repeat1 == 'y':
        print(nIsFalse)
    else:
        print(yIsTrue)


def questionC():
    userSentence = str(input("Please type a sentence : "))
    print("Your sentence is: ", userSentence)
    sentenceConvertion = userSentence.lower()

    vowelCounts = {}

    for vowel in "aeiou":
        count = sentenceConvertion.count(vowel)
        vowelCounts[vowel] = count
    counts = vowelCounts.values()
    totalVowels = sum(counts)

    print(vowelCounts)
    print("The total number of vowels found is : ", totalVowels)


main()
