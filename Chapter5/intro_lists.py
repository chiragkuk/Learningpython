# data structures
# List ---> this chapter
# ordered collection of items
# you can store anything in Lists int, float, string

numbers = [1,2,3,4]
print(numbers[1])

words=["Pehla","Dusra","Teesra"]
print(words[0:1])

mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed[1] ="two"
print(mixed)

mixed[1:] ="two"
print(mixed)

mixed[1:] =["three","four"]
print(mixed)