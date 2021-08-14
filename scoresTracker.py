# ----- Design Tool - PseudoCode ---------
# Create Menu system
# Create Functions for each exam
# Create function to get exam score
# create Function to Display all Exam Scores
# Create Function to Display
# Create exam statistics
# Create a function to adjust all exam scores
# Create a function to remove all f grades from the list


# ------ Comment Header -----------


def main():
    # main()
    def getChoice():
        userMenuChoice = (input ('the choice of your preference :  ') )
        print('1. Menu function please make a choice:')
        print('[A] Input a score')
        print('[B] Input multiple scores or -999')
        print('[C] sort from high to low')
        print('[D] sort from low to high')
        print('[E] Display exam statistics')
        # print('[P] Adjust all exam scores')
        print('[F] Quit     - game over')
        choice = input("Enter your selection: ")
        return choice.upper()  # this converts the value of choice to uppercase

    getChoice()

    def examOne(prompt):
        while True:
            try:
                type = int(input(prompt))
            except ValueError:
                print("Value must be between 0 and 100. Please re-enter.")
                continue
            else:
                while type < 0 or type > 100:
                    print("Value must be between 0 and 100. Please re-enter.")
                    type = examOne(" Please enter your exam one score between 0 - 100: "
                                   )
                return type
                break

    credits1 = examOne(" Please enter your exam one score between 0 - 100: ")
    print("Your first exam score is :", credits1)

    def moreExamScoreUntil999():
        while True:
            try:
                type = int(input())
            except ValueError:
                print("Value must be between 0 and 100. Please re-enter.")
                continue
            else:
                while type < 0 or type > 1000:
                    print("Value must be between 0 and 100. Please re-enter.")
                    type = examOne(" Please enter your exam one score between 0 - 100: "
                                   )
                return type
                break

    severalScores = moreExamScoreUntil999(" Please enter your exam one score between 0 - 1000: ")
    print("Your first exam score is TEST :", severalScores)

    examOne()
    moreExamScoreUntil999()


main()
