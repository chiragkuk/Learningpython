num1= int(input("Enter the first number : "))
num2= int(input("Enter the second number : "))


def greater_num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

bigger=greater_num(num1,num2)

print(f"{bigger} is greater")