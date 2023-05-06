#Exercise -Watch COCO
#Ask user name and age
#If user's name start with ('a' or 'A' ) and Age is above 10 then
#Print 'You can watch Coco Movie
#Else Print "You can't watch Coco Movie"

enterName=input("Enter your Name : ").lower()
enterAge=int(input("Enter Your age: "))
if(enterName[0] == 'a' and enterAge >= 10):
    print("you can watch Movie Coco")
else:
    print("Alas! you can't watch Movie Coco")
