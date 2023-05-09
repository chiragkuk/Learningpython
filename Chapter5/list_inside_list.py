# list inside list

matrix=[[1,2,3],[4,5,6],[7,8,9]] #2-D List 
print (matrix[0])

for i in matrix:
    print(i)

for sublist in matrix:
    for i in sublist:
        print(i)

print (matrix[1][1])

s= "string"
print(type(s))
print(type(matrix))