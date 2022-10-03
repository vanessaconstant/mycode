#!/usr/bin/env python3

""" Alta3 Rsearch | VC
    Custom script for conditionals"""


def main():

    score_input = input("Please enter your score: ")
    score = int(score_input)

    if score >= 90:
        print("Yu got an A  on the assignment.")
    elif score >= 80:
        print("Yu got an B on the assignment.")
    elif score >= 70: 
        print("Yu got an C on the assignment.")
    elif score >= 60:
        print("Yu got an D on the assignment.")
    else:
        print("Yu got an F on the assignment.")


main()

