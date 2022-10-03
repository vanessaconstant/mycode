#!/usr/bin/env python3

"""VConstant | Alta3 Research
   learning about for logic"""


def main():

    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

    approved_vendors = ["cisco", "juniper", "big_ip"]
    for x in vendors:
        print("\nThe vendor is: " + x )
        if x not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")

    print("\nOur loop has ended.")



    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        print(farm['name'])
        print(farm['agriculture'])

main()
