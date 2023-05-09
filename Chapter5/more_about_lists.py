# generate lists with range functions
# something more about pop method
# index method
# pass list to a function

numbers = list(range(1,11))
print (numbers)
popped_item=numbers.pop()
print (popped_item)
print(numbers)
numbers1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
print(numbers1.index(1))
print(numbers1.index(1,3))
#print(numbers1.index(1,3,5))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))