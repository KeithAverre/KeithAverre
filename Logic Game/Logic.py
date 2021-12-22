# -*- coding: utf-8 -*-

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
        self.expressions = []
        for i in range(int(2 ** self.numVars)):
            self.expressions.append([self.board[j][i] for j in range(self.numVars)])
            
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
    
    #These functions compute the unreduced Sum of Minterms of self.function
    #####################################################################################
    def UnreducedSUM(self):
        unreduced = ""
        for i in range(int(2 ** self.numVars)):
            if(self.function[i] == "1"):
                unreduced = unreduced + self.unreducedHelperSUM(self.expressions[i])
        unreduced = unreduced.rsplit(" + ", 1)[0]
        
        return unreduced
    
    def unreducedHelperSUM(self,expr):
        temp = ""
        for i in range(len(expr)):
            if(expr[i] == "0"):
                temp = temp  + self.variables[i] +"'"
            else:
                temp = temp + self.variables[i]
                
        return temp + " + "
    #####################################################################################
    
    #These functions compute the unreduced Product of Maxterms of self.function
    #####################################################################################
    def unreducedMAX(self):
        unreduced = ""
        for i in range(int(2 ** self.numVars)):
            if(self.function[i] == "0"):
                unreduced = unreduced + self.unreducedHelperMAX(self.expressions[i])
        return unreduced
    
    def unreducedHelperMAX(self,expr):
        temp = "("
        for i in range(len(expr)):
            if(expr[i] == "0"):
                temp = temp  + self.variables[i] +"'"
            else:
                temp = temp + self.variables[i]
            if(i + 1 == len(expr)):
                continue
            else:
                temp = temp + " + "
        return temp + ")"
    #####################################################################################

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
    
    
    
    