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
    adjustString = list(map(str,adjustString))
    print(adjustString)
    formatCheck(adjustString)
    
        
def formatCheck(workStr):
    raise Exception("Function is not functional yet. From format Checking")
    try:
        symCheck = ["+","'","(",")"," "] #allowed symbols
        adjustToList = []
        for idx,i in enumerate(workStr):
            if(i < "a" or i > "z"): #checks if is letter
                if(not inList(i,symCheck)): #checks if is accepted symbol   
                    raise Exception("Interpreted as: {}\nInvalid Symbol within input \"{}\" at index {}.".format("".join(i for i in workStr),i,str(idx)))
                if(i == ")"):
                    raise Exception("Interpreted as: {}\nInvalid Symbol position within input \"{}\" at index {}.".format("".join(i for i in workStr),i,str(idx)))
    except Exception as e:
        print(e)
        return False
    return True
def inList(item, arr):
    for i in arr:
        if i == item:
            return True
    return False