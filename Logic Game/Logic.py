# -*- coding: utf-8 -*-
from from_expression import *
class Logic:
    
    def __init__(self,args, function):
        if(len(args) <= 0):
            raise Exception("Too few arguements")
        self.variables = args
        self.numVars = len(self.variables)
        self.board = self.makeBoard()
        
        self.varList = [i for i in self.variables]
        self.varList.append("F")
        
        self.function = function
        self.minterms,self.maxterms = self.makeMinTermsMaxTerms()
        
        #expression for each row
        self.Allexpress = []
        for i in range(int(2 ** self.numVars)):
            self.Allexpress.append([self.board[j][i] for j in range(self.numVars)])
        print(self.Allexpress)
        self.expressions = self.computeExpressions() #a tuple of list of SOM terms and list of POM terms
    #self.board, it is a 2D list made of the columns of the truth table
    def makeBoard(self):
        k = self.numVars
        board = []
        for p in range(k):    
            board.append([])
        for i in board:
            p = 0 
            while(p != 2 ** self.numVars):
                for j in range(int(2 **(k - 1))):
                    i.append("0")
                    p += 1
                for j in range(int(2 **(k - 1))):
                    i.append("1")
                    p += 1
            k -= 1
        return board
    
    def makeMinTermsMaxTerms(self):
        Minterms = []
        Maxterms = []
        for i in range(0, len(self.function)):
            if(self.function[i] == "1"):
                Minterms.append(i)
            else:
                Maxterms.append(i) 
        return Minterms,Maxterms
    
    def makeTranslation(self):
        trans = []
        for i in self.variables:
            trans.append([])
        
        return trans
    
    #This function returns the unreduced Sum of Minterms of self.function in a nice format
    #####################################################################################
    def UnreducedSUM(self):
        unreduced = ""
        formatTrack =0
        for i in self.expressions[0]:
            for j in i: 
                unreduced = unreduced + j
            formatTrack +=1
            if formatTrack == len(self.expressions[0]):
                continue
            else:
                unreduced += "+"
            
        return unreduced
    
    #####################################################################################
    
    #This function returns the unreduced Product of Maxterms of self.function in a nice format
    #####################################################################################
    def unreducedMAX(self):
        unreduced = ""
        
        for i in self.expressions[1]:
            formatTrack =0
            unreduced += "("
            for j in i: 
                formatTrack +=1
                if(formatTrack == self.numVars):    
                    unreduced = unreduced + j 
                else:
                    unreduced = unreduced + j +"+"
            unreduced += ")"
        return unreduced
    
    #####################################################################################

    #Computes all the true expressions in the truth table based on self.function
    def computeExpressions(self):
        arrSOM = []
        arrPOM = []
        #holds both variable and notted variables
        hold = [[i] for i in self.variables]
        for i in range(len(hold)):
            hold[i].append(hold[i][0] + "'")
            hold[i].reverse()
        
        for i in range(len(self.function)):
            temp = []
            if self.function[i] == "1":
                for j in range(len(self.board)):
                    temp.append(hold[j][int(self.board[j][i])])
                arrSOM.append(temp)
            else:
                for j in range(len(self.board)):
                    temp.append(hold[j][int(self.board[j][i])])
                arrPOM.append(temp)
        return arrSOM,arrPOM

    def printTruthTable(self):
        for i in range(self.numVars + 1):
            print(self.varList[i], end = "  ")
        print()
        for j in range(int(2 **self.numVars)):
            for i in range(self.numVars):
                print(self.board[i][j] + " ", end = " ")   
            print(self.function[j])
            
        print("Sum of Minterms: ", self.minterms)
        print("Unreduced Boolean Expression SOM: ",self.UnreducedSUM())
        print("Product of Maxterms: ", self.maxterms)
        print("Unreduced Boolean Expression POM: ",self.unreducedMAX())
      
    
    
    def MakeKarnaugh(self):
        raise Exception("Function is not functional yet. MakeKarnaugh")
        count = 0
        temp = self.numVars
        while(temp > 2):
            count += 1
            temp = temp // 2
        print(count)   
        print("""
_____________________________________________
|                     |                     |
|                     |                     |
|_____________________|_____________________|
              
              
              """)
        return
        
    def EQUAL(self, a,b):
        return a == b
    
    def NOT(self, a):
        return not a
    
    def AND(self, a, b):
        return a and b

    def OR(self, a,b):
        return a or b
    
    def NAND(self, a,b):
        return self.NOT(self.AND(a,b))
    
    def NOR(self, a,b):
        return self.NOT(self.OR(a,b))
    
    def XOR(self, a, b):
        return self.OR(self.AND(self.NOT(a),b),self.AND(a,self.NOT(b))) 
    
    def XNOT(self, a,b):
        return self.NOT(self.XOR(a,b))
    
    
    
    