# problem
# ask user to input a number containing more than one digit
# example 1256
# algorithm - (method to solve problem in human language)
# calculate 1+2+5+6 and print
# ask input in string, i.e don't change string to int
# example - "1256"
# pick string character one by one and change to int
# int(example[0]) + int(example [1]) go upto len(example) - 1

inputString=input("Enter the Number : ")
total=0
i=0
while i<len(inputString):
    total += int(inputString[i])
    i += 1
print(f"Total of Inputted String {inputString} is {total}")