# Some more methods to add data in our list
# inset method
# how to join(concatenate 2 lists)
# extend method
# difference between append and extend method

fruits1=["Mango","Orange"]
fruits1.insert(1,"Grapes")
print(fruits1)

fruits2=["Apple","Strawberry"]
fruits=fruits1+fruits2
print (fruits)

fruits1.extend(fruits2)
print(fruits1)

###### List inside list########

fruits1.append(fruits2)
print (fruits1[5])
print (fruits1)
