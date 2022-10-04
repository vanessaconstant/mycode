#!/usr/bin/env python3
"""Alta3 Research | Author: VConstant

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/"""


import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform


def main():

    resp = requests.get(f"{API}sets")

    # display the methods available to our new object
    print( dir(resp) )


if __name__ == '__main__':
    main()



