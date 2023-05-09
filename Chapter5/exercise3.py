# define a function that take list of words as argument and
# return list with reverse of every element in that list
# example
# ['abc', ‘tuv', ‘xyz'] ---> ['cba', ‘vut', ‘zyx']

def reverse_element(l):
    elements=[]
    for i in l :
        elements.append(i[::-1])
    return elements

words = ['abc','def','ghi']
print (reverse_element(words))