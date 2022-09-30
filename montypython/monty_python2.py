#!/usr/bin/env python3

""" Alta3 Research | VConstant
    Using while, if, elif, else """

def main():

    turn = 0
    answer = " "

    while turn < 3 and answer != "Brian":

        turn +=  1

        answer = input('Finish the movie title, "Monty Python\'s The Life of ______"')
    

        if answer.lower() == 'brian':
            print("Correct")
            break
        elif turn == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! Try again!")


main()

