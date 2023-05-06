# exercise one of three
#sum of n natural numbers
# ask a user for natural number
# print total from 1 to n

total=0
input=int(input("Enter upto the numbers you want to sum : "))
i=1
while i<=input:
    total += i
    i += 1
print (f"Sum of the numbers from 1 to {input} : {total}")
