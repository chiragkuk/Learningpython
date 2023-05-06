from random import *
gussedNumber=int(input("Enter a number between 1 to 100 : "))
winningNumber=randint(1,100)

if(gussedNumber==winningNumber):
    print("You won the Lottery")
else:
    if (gussedNumber<winningNumber):
        print(f"Winning number was {winningNumber} your Number was too low")
    else:
        print(f"Winning number was {winningNumber} your Number was too high")