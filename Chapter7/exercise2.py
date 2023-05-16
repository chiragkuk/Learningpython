users={}
name = input("What is your Name : ")
age = input("What is your age : ")
fav_movies=input("Enter your fav movies seprated by , ").split(',')
fav_songs=input("Enter your fav songs seprated by , ").split(',')

users['name']=name
users['age']=age
users['fav_movies']=fav_movies
users['fav_songs']=fav_songs

print(users)

#To print in different lines

for key, value in users.items():
    print(f'{key} : {value}')
    