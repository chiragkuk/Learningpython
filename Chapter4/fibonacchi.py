# fibonacci series
#1 1 2 3 5 8 13 21 34
# 1 --> 0
# 2 --> 0 1
# 3 ---> 0 1 1

fibo_series= int(input("Enter the number upto where you need Fibbo series : "))

def fibonacchi_seq(fibo_series):
    num1 = 0
    num2 = 1
    if fibo_series == 1:
        print(num1)
    elif fibo_series == 2:
        print(num1 , num2 , end=" ")
    else:
        print(num1 , num2, end=" ")
        for i in range(fibo_series-2):
            num3 = num1+num2
            num1 = num2
            num2 = num3
            print (num2, end= " ")

fibonacchi_seq(fibo_series)