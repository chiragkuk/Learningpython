# ask a user for name
# Example Harshit Vashisth
# print count of each words
# output :
#H: 1
#a: 2
#r: 1
#s: 3
#h: 3
#i: 2
#t: 2
# : 1
# V: 1

inputString=input("Enter the name: ")
tempVar=" "
i=0
while i<len(inputString):
    if inputString[i] not in tempVar:
        tempVar += inputString[i]        
    print(f"{inputString[i]} : {inputString.count(inputString[i])}")
    i += 1
