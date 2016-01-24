"""
File: converter.py
Project 7.7

Add error recovery to the infix to postfix converter.

Defines a class that converts infix expressions to postfix form.
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack

class IFToPFConverter(object):

    def __init__(self, scanner):
        self._expressionSoFar = ""
        self._operatorStack = ArrayStack()
        self._scanner = scanner


    def convert(self):
        """Returns a list of tokens that represent the postfix
        form of sourceStr.  Assumes that the infix expression
        in sourceStr is syntactically correct"""
        postfix = []
        while self._scanner.hasNext():
            currentToken = self._scanner.next()
            self._expressionSoFar += str(currentToken) + " "
            if currentToken.getType() == Token.UNKNOWN:
                raise AttributeError("Unrecognized symbol")
            if currentToken.getType() == Token.INT:
                postfix.append(currentToken)
            elif currentToken.getType() == Token.LeftPar:
                self._operatorStack.push(currentToken)
            elif currentToken.getType() == Token.RightPar:
                if self._operatorStack.isEmpty():
                    raise AttributeError("Too few operators")
                topOperator = self._operatorStack.pop()
                while topOperator.getType() != Token.LeftPar:
                    postfix.append(topOperator)
                    if self._operatorStack.isEmpty():
                        raise AttributeError("Too few operators")
                    topOperator = self._operatorStack.pop()
            else:
                while not self._operatorStack.isEmpty() and \
                      self._operatorStack.peek().getPrecedence() >= currentToken.getPrecedence():
                    postfix.append(self._operatorStack.pop())
                self._operatorStack.push(currentToken)
        while not self._operatorStack.isEmpty():
            postfix.append(self._operatorStack.pop())
        return postfix
   
    def __str__(self):
        result = "\n"
        if self._expressionSoFar == "":
            result += "Portion of expression processed: none\n"
        else: 
            result += "Portion of expression processed: " + \
                   self._expressionSoFar + "\n"
        if self._operatorStack.isEmpty():
            result += "The stack is empty"
        else:
            result += "Operators on the stack          : " + \
                      str(self._operatorStack)
        return result

    def conversionStatus(self):
        return str(self)

    
def main():
    while True:
        sourceStr = input("Enter an infix expression: ")
        if sourceStr == "":
            break
        else:
            try:
                converter = IFToPFConverter(Scanner(sourceStr))
                postfix = converter.convert()
                print("Postfix:", end = " ")
                for token in postfix:
                    print(token, end = " ")
                print()
            except Exception as e:
                print(e, converter.conversionStatus())

if __name__ == "__main__":
    main()


