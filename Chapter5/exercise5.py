# common elements finder Function
# define a functions which take 2 lists as input and return a list
# which contains common elements of both lists
# example
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

def common_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output

num1=[1,2,3,4]
num2=[1,2,5,8]
print (common_finder(num1,num2))