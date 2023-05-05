name = "                     Kuk reja                           "
dots = "........................................................"
#lstrip method basically trims all the spaces on the left
print (name.lstrip() + dots)
#rstrip method basically trims all the spaces on the right
print (name.rstrip() + dots)
#strip method trims all the left and right spaces in the string
print (name.strip()  + dots)
#replace method replaces the string condition is we have to give 2 arguments to replace (" ","")  
print (name.replace(" ","") + dots)