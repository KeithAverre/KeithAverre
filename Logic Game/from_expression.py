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
    #raise Exception("Function is not functional yet. From format Checking")
    err = "Interpreted as: {}\n".format("".join(i for i in workStr))
    originalStr = workStr
    uniqueChars = []
    try:
        symCheck = ["+","'","(",")"," ","{","}"] #allowed symbols
        adjustToList = []
        for idx,i in enumerate(workStr):
            if(i < "a" or i > "z"): #checks if is letter
                if(not inList(i,symCheck)[0]): #checks if is accepted symbol 
                    err += "Invalid Symbol within input \"{}\" at index {}.".format(i,str(idx))
                    raise Exception(err)
                if(i == "("): # Makes sure there is a pair of parenthesis
                    tempCheck = inList(")",workStr[idx:len(workStr)])
                    if(not tempCheck[0]):
                        err += "Invalid Symbol position within input \"{}\" at index {}.".format(i,str(idx))
                        raise Exception(err)
                    else:
                        workStr[tempCheck[1]+idx] = "}" # this represents a pair of parenthesis
                if(i == ")"):
                    err += "Invalid Symbol position within input \"{}\" at index {}.".format(i,str(idx))
                    raise Exception(err)
            else: # is a letter
                if(not inList(i, uniqueChars)[0]): #Checks if letter is unique
                    uniqueChars.append(i)
    except Exception as e:
        print(e)
        return False
    uniqueChars.sort()
    print(uniqueChars)
    return True


def inList(item, arr):
    for idx,i in enumerate(arr):
        if i == item:
            return True,idx
    return False,-1

