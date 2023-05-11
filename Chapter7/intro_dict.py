# dictionaries intro
#Q-- why we use dictionaries?
# A - Because of limitations of lists , lists are not enough to represent
# real data .
# Example

#user = ['Harshit', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name , age , fav movies , fav tunes

# you can do this but this is not a good way to do this.

#Q-- what are dictionaries
#A- unordered collections of data in key : value pair.


user={'name':'Chirag','age':"30",}
print(user)
print (type(user))


#Secondary Method to create Dict.

user1=dict(name="Chirag",age="25")
print (user1)
print(user1['name'])
print(user1['age'])

# which type of data a dictionary can store ?
# anything
# numbers, strings, list , dictionary

user_info={
    'name':"chirag",
    'age':"30",
    'fav_movies':['coco', 'kimi no na wa'],
    'fav_tunes':['awakening', 'fairy tale']
}

print (user_info)
print (user_info['age'])

users={
    'user1':{'name':"chirag",
    'age':"30",
    'fav_movies':['coco', 'kimi no na wa'],
    'fav_tunes':['awakening', 'fairy tale']},
    
    'user2':{'name':"chirag2",
    'age':"32",
    'fav_movies':['coco2', 'kimi no na wa2'],
    'fav_tunes':['awakening2', 'fairy tale2']}
}

print (users['user2'])