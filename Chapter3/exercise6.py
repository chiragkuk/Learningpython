from random import *
gussedNumber=int(input("Enter a number between 1 to 100 : "))
winningNumber=randint(1,100)
guess=1
game_over=False

while not game_over:
    if gussedNumber==winningNumber:
        print(f"you win and you guessed this number in {guess} times")
        game_over=True
        
    else:
        if gussedNumber< winningNumber:
            print("too low ")
            guess += 1
            gussedNumber = int(input("guess again : "))
        else:
            print("too high ")
            guess +=1
            gussedNumber = int(input("guess again : "))