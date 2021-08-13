"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""


import random
import sys

print("---------------------------------------------")
print("Hello and welcome to the Number Guessing Game")
print("---------------------------------------------\n")
HIGHSCORE = 10


def start_game():
    randomNumber = random.randint(1,10)
    while True:
      try:
        yourGuess = int (input("Enter your guess number between 1 - 10: "))
        if type(yourGuess) is int:
          break
      except  ValueError:
        print("Please enter intger number.")   

    count  = 1
    while yourGuess != randomNumber:
      if 0 < yourGuess < 11:
        if yourGuess >  randomNumber:
          print("\n It's lower")
        elif yourGuess <  randomNumber:
          print("\n It's higher")
      else:
        print("plase make sure your guess must be between 1 - 10")    

      while True:
        try:
          yourGuess = int (input("Enter your guess number between 1 - 10: "))
          if type(yourGuess) is int:
            break
        except  ValueError:
          print("Please enter intger number.")   
      count += 1


    print("\n You got it, It took you {} tries.\n".format(count))
    WYLTPA = input("Would you like to play again? [y]es/[n]o: ") # WYLTPA == Would You Like To Play Again
    global HIGHSCORE
    if HIGHSCORE > count:
      HIGHSCORE = count
    
    
    if WYLTPA.lower() == "y":
      print("The HIGHSCORE is {}".format(HIGHSCORE))
      start_game()
      
    sys.exit("\n Closing game,your HIGHSCORE for this round is {}, see you next time!".format(HIGHSCORE))  
        

start_game()
  
