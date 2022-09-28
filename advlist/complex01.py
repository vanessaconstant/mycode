#!/usr/bin/env python3
"""Alta3 Research | RZfeeser
   List - simpler list"""


def main():

    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    print(list1)

    #display lists1[1] which should display arista_eos
    print(list1[1])

    #create a second list

    list2 = ["juniper"]

    list1.extend(list2)

    print(list1)


    #create a third list
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    list1.append(list3)


    print(list1)

    print(list1[4])

    print(list1[4][0])


main()
