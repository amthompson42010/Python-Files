#################################
#                                                                                       
# Project 3                                                                             
# Alexander M. Thompson                                                                 
# CS 260                                                                                
#                                                                                       
#                                                                                       
# Game of Sticks!                                                                       
# filename = project3.py                                                                
#                                                                                       
#                                                                                       
#                                                                                       
#################################



import random

class HumanVsHuman():      #This class is the for the human versus human game
    def __init__(self, NumOfSticks):
        self._NumOfSticks = NumOfSticks #NumOfSticks is the amount of sticks in the game

    def player1(self):
        player1_choice = input("Player1: Please choose a number of sticks (1-3):")
        if int(player1_choice) < 1 or int(player1_choice) > 3:
            print("Please choose a number between 1 and 3!")
        else:
            self._NumOfSticks = self._NumOfSticks - int(player1_choice) #Takes the original amount of sticks and decreases by what player chose
            if self._NumOfSticks == 0:
                print("You lose player1!")
                return False
            else:
                print("There are", self._NumOfSticks, " sticks left")
                return True
                return self._NumOfSticks #Returns the remaining sticks

    def player2(self):
        player2_choice = input("Player2: Please choose a number of sticks (1-3):")
        if int(player2_choice) < 1 or int(player2_choice) > 3:
            print("Please choose a number between 1 and 3!")
        else:
            self._NumOfSticks = self._NumOfSticks - int(player2_choice) #Takes the amount of sticks after player's turn and decreases it by what player 2 chose
            if self._NumOfSticks == 0:
                print("You Lose player2!")
                return False
            else:
                return True
                return self._NumOfSticks #returns the amount of sticks after player2's turn

class HumanVsComputer():
    def __init__(self, NumOfSticks):
        self._NumOfSticks = NumOfSticks
                
    def player1(self):
        player1_choice = int(input("Player1: Please choose a number of sticks (1-3):"))
        if player1_choice < 1 or player1_choice > 3:
            print("Please choose a number between 1 and 3!")
        else:
            self._NumOfSticks = self._NumOfSticks - player1_choice
            if self._NumOfSticks <= 0:
                print("You Lose Player 1!")
                return False
            else:
                print("There are", self._NumOfSticks," sticks left")
                return True
                return self._NumOfSticks

    def computer(self, C, TC):
        computer_choice = random.choice(C[self._NumOfSticks])
        beside = [] #Makes a list to put the balls in once selected
        beside.append(computer_choice) #Appends computer's choice to the beside list
        new = beside.pop() #Pops off the what is in the beside list
        C[self._NumOfSticks].append(new) #puts what was popped off in the beside list back in the original list
        print("The Computer chooses", computer_choice, "sticks.")
        self._NumOfSticks = self._NumOfSticks - computer_choice
        if self._NumOfSticks <= 0:
            C = TC
            print("You Lose Computer!")
            return False
        else:
            return True
            return self._NumOfSticks
        
class HumanVsTrainedComputer():
    def __init__(self, NumOfSticks):
        self._NumOfSticks = NumOfSticks

    def Player1(self):
        player1_choice = int(input("Player1: Please choose a number of sticks (1-3):"))
        if player1_choice < 1 or player1_choice > 3:
            print("Please choose a number between 1 and 3!")
        else:
            self._NumOfSticks = self._NumOfSticks - player1_choice
            if self._NumOfSticks <= 0:
                print("You Lose Player 1!")
                return False
            else:
                print("There are", self._NumOfSticks," sticks left")
                return True                         
                return self._NumOfSticks

        

    def computer1(self, C, TC):
        computer_choice = random.choice(C[self._NumOfSticks])
        beside = []
        beside.append(computer_choice)
        new = beside.pop()
        C[self._NumOfSticks].append(new)
        print("The Computer chooses", computer_choice, "sticks.")
        self._NumOfSticks = self._NumOfSticks - computer_choice
        if self._NumOfSticks <= 0:
            C = TC
            print("You Lose Computer!")
            return False
        else:
            return True
            return self._NumOfSticks


    def SmartComputer(self, computer1):
        i = 0
        while i != 100000: #trains the AI
            i += 1
            computer1
        return computer1



def main():
    board = int(input("Please enter how many sticks you want to start out with (10-100): "))
    if board < 10 or board > 100:
        print("Please enter a number of sticks between 10 and 100.")
    choice = int(input("Please enter a choice:\n 1: Human Vs Human\n 2: Human Vs Computer\n 3: Computer Vs Computer\n Choice is yours: "))
    if choice == 1:
        game1 = HumanVsHuman(board)
        while board > 0 and game1.player1() == True and game1.player2() == True:
            game1.player1()
            game1.player2()
        play_again = int(input("Would you like to play again? (1 = yes, 2 = no)"))
        while play_again == 1:
            game1 = HumanVsHuman(board)
            while board > 0 and game1.player1() == True and game1.player2() == True:
                game1.player1()
                game1.player2()
            play_again = int(input("Would you like to play again? (1 = yes, 2 = no)"))
    elif choice == 2:
        game2 = HumanVsComputer(board)
        a = Content(board, Hats(board))
        while board > 0 and game2.player1() == True and game2.computer(a, TrueContent(board, Hats(board))) == True:
            game2.player1()
            game2.computer(a, TrueContent(board, Hats(board)))
        play_again = int(input("would you like to play again? (1 = yes, 2 = no)"))
        while play_again == 1:
            game2 = HumanVsComputer(board)
            a = Content(board, Hats(board))
            while board > 0 and game2.player1() == True and game2.computer(a, TrueContent(board, Hats(board))) == True:
                game2.player1()
                game2.computer(a, TrueContent(board, Hats(board)))
            play_again = int(input("would you like to play again? (1 = yes, 2 = no)"))
    elif choice == 3:
        game3 = HumanVsTrainedComputer(board)
        print("Training AI please wait...")
        while (board > 0 and game3.Player1() == True): 
            game3.SmartComputer(game3.computer1(Content(board, Hats(board)), TrueContent(board, Hats(board))))
        play_again = int(input("would you like to play again? (1 = yes, 2 = no)"))
        while play_again == 1:
            game2 = HumanVsTrainedComputer(board)
            print("Training AI please wait...")
            while(board > 0 and game3.Player1() == True):
                game3.SmartComputer(game3.computer1(Content(board, Hats(board)), TrueContent(board, Hats(board))))
            play_again = int(input("would you like to play again? (1 = yes, 2 = no)"))

#Makes the Hats list filled with values 1,2, and 3
def Hats(NumOfSticks):
    hats = []
    for i in range(0, NumOfSticks):
        hats = [1,2,3]
    return hats

#Copies Hat for the the range of the amount of sticks in the game
def Content(NumOfSticks, m):
    content = []
    for i in range(NumOfSticks):
        new_content = []
        for row in m:
            new_content.append(row)
        content.append(new_content)
    return content

#Used when the Computer makes the new list
def TrueContent(NumOfSticks, w):
    content1 = []
    for i in range(NumOfSticks):
        new_content1 = []
        for row in w:
            new_content1.append(row)
        content1.append(new_content1)
    return content1

main()
