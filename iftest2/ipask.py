#!/usr/bin/env python3

""" Alta3 Research | VC
    Conditionals - testing if strings test true """


def main():

    ipchk = input("Apply an IP address: ")

    if ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else:   # if data is NOT provided
        print("You did not provide input.")


main()
