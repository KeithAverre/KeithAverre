# -*- coding: utf-8 -*-

"""
This file is to hold all expression handling to avoid clutter within other files where it would be out of place.

-Format checking; complete parenthesis, no unusual characters, 
-logic checking and reducing
-Keep track of all unique alphabet characters
-Give to logic.py to compute a Logic object.

"""

def startComputing(startString):
    raise Exception("Function is not functional yet. From expression")
    adjustString = startString.lower() #convert to lowercase
    symCheck = ["+","'","(",")"] #allowed symbols
    adjustToList = []
    for i in adjustString:
        if(not inList(i,symCheck)):
            raise Exception("Invalid Symbol within input {}".format(i))
        
def formatCheck(startString):
    raise Exception("Function is not functional yet. From format Checking")
        
def inList(item, arr):
    for i in arr:
        if i == item:
            return True
    return False