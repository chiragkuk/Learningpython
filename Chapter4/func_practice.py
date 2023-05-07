# function practice

def last_char(name):
    return name[-1]

print (last_char("Ahuja"))

def odd_even(num):
    if num%2 == 0:
        return("Even")
    else :
        return("Odd")
print (odd_even(10))

def is_even(num):
    if num%2 == 0:
        return True
    else :
        return False

print(is_even(35))

print("############################")

######Pythonic Way#########

def is_even2(num): ##### Here num is parameter
    return num%2 == 0 

print(is_even2(45)) ######## Here 45 is argument

