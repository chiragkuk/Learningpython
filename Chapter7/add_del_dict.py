# add and delete data
user_info = {
    'name' : 'harshit',
    'age': 24,
    'fav_movies' : ["coco", 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# how to add data
user_info['fav_songs'] = ['tu jaane na','Bandey']
print(user_info)

# pop method
popped_item=user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")
print(user_info)

#Popitem method
popped_items=user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))