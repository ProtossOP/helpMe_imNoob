#!/usr/bin/env python3

    """
    basic_directory_searcher.py: Search the system for names of files and
    directories containing your input string.
    
    Takes 2 arguments:
    search (string)       = 'your searchword'
    dig_counter (integer) = 'number' (amount of dir-layers to open)

    --- Please excuse me for the terminology like 'layers', I'm very new to
    --- programming. In this example the numbers are the layers:

        C:\1\2\3\4\5

    --- I hope it's not too messy...
    """

# Imports
import os
import sys
import string

### Arguments
##search = sys.argv[1]
##dig_counter = sys.argv[2]
# hardcoded Arguments
search = "Cubase"
dig_counter = 3

# Constants and Variables.
alfabet = string.ascii_uppercase

root_layer = [] #bottom layer; old layer
apex_layer = [] #top layer; new layer
layer_counter = 0

"""This should be __init__?"""" 
# Make a list of every possible path 'on the first layer' of the drive.
for letter in alfabet:    
    try:
        rawlist = os.listdir(letter+":\\")
        for item in rawlist:
            root_layer.append(letter+":\\"+item)
    except:
        pass

"""The main function"""
def dig():
    # Check dig_counter, if above 0, carry on and subtract 1.
    global dig_counter
    if dig_counter > 0:
        dig_counter -= 1

        # Check the root_layer for a match with the user input (search)
        for item in root_layer:
            if str(search) in item:
                print (item)

            # Check in the root_layer for items that are maps.
            if os.path.isdir(item)==True:
                
                # Make list of items inside verified map.
                # Append new paths to apex_layer.
                try:
                    temp = os.listdir(item)
                    for child_item in temp:
                        apex_layer.append(item+"\\"+child_item)
                        
                # Remove the item if it can't be opened. (Permission etc.)
                except:
                    root_layer.remove(item)

        
        # Flush root_layer, copy apex_layer to root_layer, flush apex_layer.
        del root_layer[:]
        for item in apex_layer:
            root_layer.append(item)
        del apex_layer[:]

        # Repeat.
        global layer_counter
        layer_counter += 1
        print ("Layer number %d done." % layer_counter)
        dig()

# __init__
dig()
        



            
              








        
    



        

    
