#DRY- Don't repeat Yourself
import random

winningNumber=random.randint(1,100)
guessedNumber=int(input("Enter a number between 1 to 100 : "))
guess=1

while True:
    if guessedNumber==winningNumber:
        print(f"you win and you guessed this number in {guess} times")
        break
        
    else:
        if guessedNumber < winningNumber:
            print("too low ")
        else:
            print("too high ")
            
        guess += 1
        guessedNumber = int(input("guess again : "))