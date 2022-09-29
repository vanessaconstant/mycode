#!/usr/bin/env python3
"""Alta3 Research || Author: VC"""

def main():

    """ Run-time code"""
    # make a list using a string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ")
    print(newlist)

    # create a string using a list
    myiplist = ["192", "168", "0", "12"]
    singleip = ".".join(myiplist)
    print(singleip)

main()
