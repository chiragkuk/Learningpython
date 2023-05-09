# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed =(1,2,3,4.0)

for i in mixed:
    print(i)
    
#tuple with one element
nums=(1,)
words=("words",)
print(type(words))

#tuples without paranthesis
guitars="yamaha","Jimms","taylor"
print(type(guitars))

#tuple unpacking
guitarists="raman negi","paras thankur","ramit mehra"

guitarist1,guitarist2,guitarist3=(guitarists)

print(guitarist1)

#list inside tuple

favs=("bulleshah","galib mirza","fareed",['Saasi-pannu','Heer-Ranjha','Romeo-Juliet'])
output=favs[3].pop()
print(output)
favs[3].append("Faiz Ahmed Faiz")
print(favs[3])

#Some Functions with tuples
print(min(mixed))
print(max(mixed))
print(sum(mixed))