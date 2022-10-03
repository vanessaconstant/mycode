#!/usr/bin/env python3
"""Alta3 Research | VConstant
   For - Using a file's lines as a source for the for-loop"""


def main():

    #open file in read mode

    with open("dnsservers.txt", "r") as dnsfile:
    
        #create list of lines read
        dnslist = dnsfile.readlines()

        #loop over the lines
        for svr in dnslist:

            print(svr, end="")

        # no need to close file if you use the new python3.3 with
        #close the file
        #dnsfile.close() #sometimes considered best practice

main()


