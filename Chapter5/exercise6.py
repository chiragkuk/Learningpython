# last exercise
# function
# [1,2,3, [1,2], [3,4] ]- input
# 2
def sublist_list(l):
    count=0
    for i in l:
        if type(i) == list:
            count +=1
    return count

mixed=[1,2,3,["arun","vikas"],[5,6,7]]
print(sublist_list(mixed))
         