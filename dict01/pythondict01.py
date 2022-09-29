#!/usr/bin/env python3

""" Alta3 Research |
    Work with dictionary """

switch = {"hostname": "sw1",
          "ip": "10.0.1.1",
          "version": "1.2",
          "vendor": "cisco"}

print( switch["hostname"] )
print( switch["ip"] )

#print( switch["lynx"] )

#requesting fake keys using the .get() method

print( "First test - .get()" )
print( switch.get("lynx") )

print( "Second test - .get()" )
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get("version") )


#getting all the keys and values

print( "Fourth test - .keys()" )
print( switch.keys() )

print( "Fifth test - .values()" )
print( switch.values() )

#removing and adding new items

print( "Sixth test - .pop()" )
switch.pop("version")
print( switch.keys() )
print( switch.values() )


print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "Eighth test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )



