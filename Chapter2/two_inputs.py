# name= input ("enter your name : ")
# age= input ("enter your age : ")

####How to do it in one line with split() method#####

name,age = input("enter your name and age ").split(",")
print("Your name is " + name)
print("Your age is " + str(age))