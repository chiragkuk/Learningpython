#Scope
x=5 #global variable
def func():
    global x
    x=7
    return x

#def func2():
    #print(x) ##### It will not be printed because x has scope upto func 
print(x)
print(func())
print(x)