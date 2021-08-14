'''
==================================================
== Written by..: Dennis Hunchuck and students   ==
== Date Written: June 25, 2021                  ==
== Purpose.....: Simulate a R P S game          ==
==================================================
'''
import random

def main():
    choice = 'X'
    win = 0
    lose = 0
    tie = 0
    wStreak = 0
    lStreak = 0
    lwStreak = 0
    llStreak = 0

    while(choice != 'Q'):
        choice = getChoice()
        if(choice ==  'R'):
            win, lose, tie, wStreak, lStreak, lwSteak, llStreak = \
                play('R', win, lose, tie, wStreak, lStreak, lwStreak, llStreak)
        elif(choice == 'P'):
            win, lose, tie, wStreak, lStreak, lwSteak, llStreak = \
                play('P', win, lose, tie, wStreak, lStreak, lwStreak, llStreak)
        elif(choice == 'S'):
            win, lose, tie, wStreak, lStreak, lwSteak, llStreak = \
                play('S', win, lose, tie, wStreak, lStreak, lwStreak, llStreak)
        elif(choice == 'Q'):
            marquee("Thanks for playing, see you later!!!!!!!!!!!")
            pause()
        else:
            marquee("YOU must select from the menu...ONLY!")
            pause()
#===================================================
def displayResults(w, l, t, ws, ls, lws, lls):
    marquee("R P S   Results Menu")
    print("No. Wins..............:", w)
    print("No. Losses............:", l)
    print("No. Ties..............:", t)
    print("Current win Streak....:", ws)
    print("Current loss Streak...:", ls)
    print("Longest Winning Streak:", lws)
    print("Longest Losing Streak.:", lls)
    pause()

#===================================================
def getChoice():
    marquee("Rock-Paper-Scissors Game Main Menu")
    print('[R]ock     - player throws rock')
    print('[P]aper    - player throws paper')
    print('[S]cissors - player throws scissors')
    print('[Q]uit     - game over')
    choice = input("Enter your selection: ")
    return choice.upper() # this converts the value of choice to uppercase
#======================================================================
def getComputerThrow():
    choice = random.randint(1,3)
    if(choice == 1):
        choice = 'R'
    elif(choice == 2):
        choice = 'P'
    else:
        choice = 'S'
    return choice
#======================================================================
def marquee(message):
    print()
    size = len(message) + 6
    print('*' * size)
    print("**", message, "**")
    print('*' * size)
# ======================================================================
def play(pp, w, l, t, ws, ls, lws, lls):
    cp = getComputerThrow()
    if(pp == 'R' and cp == 'R'):
        marquee("Player and computer threw ROCK, they tied")
        t += 1
        ws = 0
        ls = 0
    elif(pp == 'R' and cp == 'S'):
        marquee("Player picked Rock & computer picked scissors, PLAYER WON")
        w += 1
        ws += 1
        ls = 0
        if(ws > lws):
            lws = ws
    elif(pp == 'R' and cp == 'P'):
        marquee("Player picked Rock & computer picked Paper, COMPUTER WON")
        l += 1
        ls += 1
        ws = 0
        if(ls > lls):
            lls =  ls
    #---------------------------------------------------------
    if(pp == 'P' and cp == 'P'):
        marquee("Player and computer threw Paper, they tied")
        t += 1
        ws = 0
        ls = 0
    elif(pp == 'P' and cp == 'R'):
        marquee("Player picked Paper & computer picked Rock, PLAYER WON")
        w += 1
        ws += 1
        ls = 0
        if(ws > lws):
            lws = ws
    elif(pp == 'P' and cp == 'S'):
        marquee("Player picked Paper & computer picked Scissors, COMPUTER WON")
        l += 1
        ls += 1
        ws = 0
        if(ls > lls):
            lls =  ls
    #---------------------------------------------------------
    if(pp == 'S' and cp == 'S'):
        marquee("Player and computer threw Scissors, they tied")
        t += 1
        ws = 0
        ls = 0
    elif(pp == 'S' and cp == 'P'):
        marquee("Player picked Scissors & computer picked PAPER, PLAYER WON")
        w += 1
        ws += 1
        ls = 0
        if(ws > lws):
            lws = ws
    elif(pp == 'S' and cp == 'R'):
        marquee("Player picked Scissors & computer picked Rock, COMPUTER WON")
        l += 1
        ls += 1
        ws = 0
        if(ls > lls):
            lls =  ls
    #---------------------------------------------------------
    displayResults(w, l, t, ws, ls, lws, lls)
    return w, l, t, ws, ls, lws, lls
# ======================================================================
def pause():
    input("press ENTER to continue....")
#======================================================================
main()
