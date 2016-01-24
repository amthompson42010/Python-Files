"""
	Project 2
   	CS 260
   	Alexander M. Thompson
"""
from scanner import Scanner
from arraystack import ArrayStack
from tokens import Token

#The Object being brought in to this class is the infix expression the user puts enters.
class InfixToPostfixConverter(object):
    
    def __init__(self, infix):
        self._infix = infix
        self._operand = 0
        self._operator = 0
    
#The following funciton converts the infix equation to postfix, and then returns the postfix expression.

    def convert(self):
        postfix = [] #Creating an empty list to store the postfix expression
        storage = ArrayStack() #Creates a stack to store the operands when converting the expression.
        while self._infix.hasNext():
            current = self._infix.next()
            if current.getType() == Token.INT:
                postfix.append(current)
            elif current.getType() == Token.LeftPar:
                storage.push(current)
                self._operand += 1
            elif current.getType() == Token.RightPar:
                self._operator += 1
                topOpInSt = storage.pop()
                while topOpInSt.getType() != Token.LeftPar:
                    postfix.append(topOpInSt)
                    topOpInSt = storage.pop()
            elif current.getType() == Token.LeftBrac:
                storage.push(current)
                self._operand += 1
            elif current.getType() == Token.RightBrac:
                self._operator += 1
                a = storage.pop()
                while a.getType() != Token.LeftBrac:
                    postfix.append(a)
                    a = storage.pop()
            else:
		#The loop below tells the program to go through the array that is created so far, and as long as it is not empty and the precedence found in the Tokens.py file of the first item in the array is greater than or equal to the precedence of the current token the Scanner is on, the program continues.
                while not storage.isEmpty() and storage.peek().getPrecedence() >= current.getPrecedence():
                    postfix.append(storage.pop())
                storage.push(current)
        if self._operand > self._operator or self._operator > self._operator:
            return "Unbalanced Expression"
        while not storage.isEmpty():
            postfix.append(storage.pop())
        return postfix


def main():
    infix_expression = input("Enter an infix expression: ")
    ConverterClass = InfixToPostfixConverter(Scanner(infix_expression)) #Calling Scanner and the class above
    postfix = ConverterClass.convert() #Telling the program which method to use
    print("Postfix:", end = " ")
    for token in postfix:
        print(token, end = " ")
    print()

if __name__ == "__main__":
    main()
