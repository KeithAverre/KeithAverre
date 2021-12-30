# -*- coding: utf-8 -*-
from Logic import Logic
from from_expression import *
import math
def main():
    
    # USER INPUT SECTION
    #######################################
    endState = False
    while(not endState):
        UserInput = input("Input some Function wanted to be implemented (must be a power of 2): (ex: 0 0 0 1)\n")
        #startComputing(UserInput)
        #return
        UserInput = UserInput.split()
        
        #Check if out of bounds call
        try:
            LogCheck = math.log(len(UserInput),2)
        except:
            print("Too few arguments")
            continue
        
        #checks if power of 2
        if((not LogCheck.is_integer())):
            print("The input function must be a power of 2, try again")
            continue
        
        #checks for more than 1 argument
        if(LogCheck < 1):
            print("Too Few arguments")
            continue
        
        #check if only each split is either "1" or "0" and length of 1
        temp = False
        for i in range(len(UserInput)):
            if(UserInput[i] == "0"):
                continue
            elif(UserInput[i] == "1"):
                continue
            else:
                temp = True
                break
        if(temp):
            print("User Input must contain only 1s and 0s, try again")
            continue
        endState = True
    #######################################
    
    alphabet = "a b c d e f g h i j k l m n o p q r s t u p w x y z aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az"
    alphabet_split = alphabet.split()
    
    y = Logic(alphabet_split[0:int(LogCheck)],UserInput)
    #y.MakeKarnaugh()
    y.printTruthTable()
    
def ExpressionInput():
    raise Exception("Function is not Functional Yet. expression input")
    #endState = False
    #while(not endState):
        #UserInput = input("Input some Function wanted to be implemented (in terms of single character variables): (ex: xy + z')\n")
        
    #used for testing purposes, to be deleted
    UserInput = "x + y'z"
    UserInput.lower()
    UserInput = UserInput.split()
    
if(__name__ == "__main__"):
    main()



"""
TO DO LIST:
    
    -ABILITY TO TRANSLATE IN AND OUT OF UNREDUCED F AND TO ARRAY F
        AKA TRANSLATE A DECODED STRING BACK INTO AN F ARRAY
    
    -DECIDE WHETHER KARNAUGH MAP OR OTHER LOGIC
    -POSSIBLY INCORPORATE CHIPS INTO PROGRAM
    -MAYBE BOOLEAN LOGIC 
    -MAYBE MAYBE BOOLEAN LOGIC REDUCTION

"""