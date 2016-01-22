######################################
#
#    Alexander M. Thompson
#    CS 150, Project 1
#    Due September 28, 2013
#
#    Time to play darts!!
#
######################################
import random

def main():
   #use the random function to get x and y coordinates
   x1,x2,x3,x4,x5,y1,y2,y3,y4,y5 = getDartCoord()
   #compute the distance from the center of the circle
   a1 = pow(x1,2) + pow(y1,2)
   a2 = pow(x2,2) + pow(y2,2)
   a3 = pow(x3,2) + pow(y3,2)
   a4 = pow(x4,2) + pow(y4,2)
   a5 = pow(x5,2) + pow(y5,2)
   d1 = float(pow(a1,.5))
   d2 = float(pow(a2,.5))
   d3 = float(pow(a3,.5))
   d4 = float(pow(a4,.5))
   d5 = float(pow(a5,.5))
   
   #display the results
   displayResults(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, d1, d2, d3, d4, d5)

def getDartCoord():   
   
   x1 = float(random.uniform(-1.4,1.4))
   x2 = float(random.uniform(-1.4,1.4))
   x3 = float(random.uniform(-1.4,1.4))
   x4 = float(random.uniform(-1.4,1.4))
   x5 = float(random.uniform(-1.4,1.4))
   y1 = float(random.uniform(-1.4,1.4))
   y2 = float(random.uniform(-1.4,1.4))
   y3 = float(random.uniform(-1.4,1.4))
   y4 = float(random.uniform(-1.4,1.4))
   y5 = float(random.uniform(-1.4,1.4))
   
   return x1, x2, x3, x4 , x5, y1, y2, y3, y4, y5


   
def displayResults(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, d1, d2, d3, d4, d5):
   
   hit = 0
   stillon = 0
   missed = 0

   if(d1 <= 1 and d1 >= -1):
     hit += 1
     print("\nDart 1 is in the circle! (x:", x1," y: ", y1,")")
   
   elif(d1 <= 1.4142135623709515 and d1 >= -1.4142135623709515 and x1 < 1 and y1 < 1 and x1 > -1 and y1 > -1):
     stillon += 1
     print("\nDart 1 is outside the circle but still on the board! (x:", x1," y: ", y1, ")")

   else:
     missed += 1
     print("\nDart 1 is outside the whole board! (x:", x1," y: ", y1,")")
   
   if(d2 <= 1 and d2 >= -1):
     hit += 1
     print("\nDart 2 is in the circle! (x:", x2," y: ", y2,")")
   
   elif(d2 <= 1.4142135623709515 and d2 >= -1.4142135623709515 and x1 < 1 and y1 < 1 and x1 > -1 and y1 > -1):
     stillon += 1
     print("\nDart 2 is outide the circle but still on the board! (x:", x2, " y: ", y2, ")")

   else:
     missed += 1
     print("\nDart 2 is outside the circle! (x:", x2," y: ", y2,")")
   
   if(d3 <= 1 and d3 >= -1):
     hit += 1
     print("\nDart 3 is in the circle! (x:", x3," y: ", y3,")")
   
   elif(d3 <= 1.4142135623709515 and d3 >= -1.4142135623709515 and x1 < 1 and y1 < 1 and x1 > -1 and y1 > -1):
     stillon += 1
     print("\nDart 3 is outside the circle, but still on the board!  (x:", x3, " y: ", y3, ")")

   else:
     missed += 1
     print("\nDart 3 is outside the whole board! (x:", x3," y: ", y3,")")
   
   if(d4 <= 1 and d4 >= -1):
     hit += 1
     print("\nDart 4 is in the circle! (x:", x4," y: ", y4,")")
   
   elif(d4 <= 1.4142135623709515 and d4 >= -1.4142135623709515 and x1 < 1 and y1 < 1 and x1 > -1 and y1 > -1):
     stillon += 1
     print("\nDart 4 is outside the circle, but still on the board!  (x:", x4, " y: ", y4, ")")

   else:
     missed += 1
     print("\nDart 4 is outside the whole board! (x:", x4," y: ", y4,")")
   
   if(d5 <= 1 and d5 >= -1):
     hit += 1
     print("\nDart 5 is in the circle! (x:", x5," y: ", y5,")")
   
   elif(d5 <= 1.4142135623709515 and d5 >= -1.4142135623709515 and x1 < 1 and y1 < 1 and x1 > -1 and y1 > -1):
     stillon += 1
     print("\nDart 5 is outside the circle, but still on the board!  (x:", x5, " y: ", y5, ")")

   else:
     missed += 1
     print("\nDart 5 is outside the whole board! (x:", x5," y: ", y5,")")
   
   print("\nThe amount of darts that hit the circle is: ", hit)
   print("\nThe amount of darts that did not hit the target is: ", missed)
   print("\nThe amount of darts that did not hit the circle, but still on the board is: ", stillon, "\n")


main()
