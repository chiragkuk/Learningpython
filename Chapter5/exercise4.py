# Filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]
# ouput ----> (CO9335}71, [2,4,6]]

def filter_odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i%2:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output=[even_nums,odd_nums]
    return (output)

nums=[1,2,3,4,5,6,7,8,9]
print (filter_odd_even(nums))