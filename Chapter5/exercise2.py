# define a function which will take list as a argument and this function
# will return a reversed list

# examples

# [1,2,3,4]-----------> [4,3,2,1]

# ['word1', ‘word2'] ---> [‘word2', ‘word1']

# Note you simply do this with reverse method 

# but try to do this with the help of append and pop method

# don't use regular string slicing or reverse metod.

def reverse_list(l):
    l.reverse()
    return l

numbers=[1,2,3,4]
print (reverse_list(numbers))

def reverse_list2(l):
    return l [::-1]

numbers=[1,2,3,4]
print (reverse_list2(numbers))


def reverse_list3(l):
    r_list=[]
    for i in range(len(l)):
        popped_item=l.pop()
        r_list.append(popped_item)
    return r_list

numbers=[5,6,7,8]
print (reverse_list3(numbers))