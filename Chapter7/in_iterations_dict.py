# how to access data from dictionary
# NOTE - There is no indexing because of unordered collections of data.
# print(user['name'])
# print(user[ ‘age’])
# which type of data a dictionary can store ?
# anything
# numbers, strings, list , dictionary

users={
    'name':"chirag",
    'age':"30",
    'fav_movies':['coco', 'kimi no na wa'],
    'fav_tunes':['awakening', 'fairy tale']
    }

#check if key exists
if 'name' in users:
    print('present')
else:
    print('not present')
#Check if value exists

if ['coco', 'kimi no na wa'] in users.values():
    print('present')
else:
    print('Not present')


#loops in dictionaries
for i in users:
    print(i)

for k in users.values():
    print(k)


#values Method
user_values=users.values()
print(user_values)
print(type(user_values))

#Keys Method
user_keys=users.keys()
print(user_keys)
print(type(user_keys))


#Loops in dict.
for i in users:
    print(users[i])
    


#Items method it converts the whole string into tuples as in Key Value Pairs
users_item=users.items()
print(users_item)
print(type(users_item))

for key,value in users.items():
    print (f"The Key is {key} and value is {value}")