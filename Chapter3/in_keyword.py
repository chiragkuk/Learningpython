name=input("Enter the name : ")
charToFind=input("Enter the char to find : ")
# in keyword
# if with in

if charToFind in name:
    print(f"Your inputted character {charToFind} is present in {name} ")
else:
    print(f"Your inputted character {charToFind} is not present in {name}")