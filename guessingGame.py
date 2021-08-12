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
HIGHSCORE = 0
def start_game():
    print("\N{TACO}")
    words = "hi rafat ahmad"
    listi = words.split()
    print(listi)
    print("+".join(listi))
    randomNumber = random.randint(1,10)
    try:
        yourGuess = int (input("Enter your guess number between 1 - 10: "))
    except  ValueError:
        print("Please enter intger number.")   
        yourGuess = int (input("Enter your guess number between 1 - 10: "))

    count  = 1
    while yourGuess != randomNumber:
      if yourGuess >  randomNumber:
        print("\n It's lower")
      elif yourGuess <  randomNumber:
        print("\n It's higher")
      yourGuess = int (input("Enter your guess number between 1 - 10: "))
      count += 1
    print("\n You got it, It took you {} tries.\n".format(count))
    
    WYLTPA = input("Would you like to play again? [y]es/[n]o: ")
    HIGHSCORE = count
    if WYLTPA.lower() == "y":
      print("The HIGHSCORE is {}".format(HIGHSCORE))
      start_game()
      
    sys.exit("\n Closing game, see you next time!")  
        

#clear && python guessing_game.py
# Kick off the program by calling the start_game function.
start_game()
  
