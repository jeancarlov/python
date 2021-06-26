# ----- Design Tool - PseudoCode ---------
# Create main function and inside the main function enter the variables codes for input and output
# Enter variables with input request to the use
# print user input result
# Create if statements to check if variable number is even or odd
# Create if statements to check if variable number is teen or not teen number
# Create if statements to check if variable number is in the red, blue, or white category
# Print result from new variables
#  call main function main() for inside code to display

# ------ Comment Header -----------
# Name: Jean Carlo Valderrama
# Date : June 6, 2021
# Purpose : Decision A homework


def main():
    firstUser = input('Hi please enter an integer value:')
    # print("Your value is", firstUser)
    if float(firstUser) % 2 == 0:
        print(firstUser, "is an even number")
    else:
        print(firstUser, "is an odd number")
    if float(firstUser) % 3 == 0:
        print(firstUser, "is a multiple of 3")
    else:
        print(firstUser, "is not a multiple of 3")
    if float(firstUser) <= 10:
        print(f"The color base on", firstUser, "is red")
    if 10 <= float(firstUser) <= 20:
        print(firstUser, "is in the teens ")
    else:
        print(firstUser, "is number NOT in the teens")
    if float(firstUser) >= 20:
        print("The color base on", firstUser, "is blue")
    if float(firstUser) == " ":
        print("The color base on", firstUser, "is white")


# main()
main()

# choice = 'x'
# while choice != '4':
#     # displayDate()
#     displayMenu()
#
#     if choice == '1':
#         # displayDate()
#         displayName()
#     # elif choice == '2':
#     # getAgeDisplay()
#     elif choice == '3':
#         displayDate()
#     # elif choice == '4':
#     #     print(' see you later ..')
#     #
#     else:
#         print('INVALID SELECTION')