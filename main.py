import random

from click import option

while True:
    print("Select any of the two numbers:1. Roll the dice\n2.Quit the game.")
    userOption=int(input())
    
    if userOption ==1:
        number =random.randint(1, 7)
        print(f"The random number is {number}")  
        if number ==1:
            print("Move one position forward in the game.")
        elif number ==2:
            print("Move two positions forward in the game")    
        elif number ==3:
            print("Move three positions forward in the game")  
        elif number ==4:
            print("Move four positions forward in the game")
        elif number ==5:
            print("Move five positions forward in the game") 
        elif number ==6:
            print("Move six positions forward in the game")
        else:
            print("Roll the dice")                                 
    else:
        break    