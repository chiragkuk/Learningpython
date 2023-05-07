def greater_num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def new_greatest(a,b,c):
    #bigger= greater_num(a,b)
    return greater_num(greater_num(a,b),c) ### or return greater_num(bigger,c)

print (new_greatest(1000,200,300))