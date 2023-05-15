# #From Keys

# d={
#     'name':'unknown',
#     'age':'unknwon'
# }

d=dict.fromkeys(['name','age','height'],'unknown')
print(d)
d1=dict.fromkeys(('name','age','height'),'unknown')
print(d1)
d2=dict.fromkeys('abc','unknown')
print(d2)
d3=dict.fromkeys(range(1,11),'unknown')
print(d3)
d4=dict.fromkeys(['name','age'],['unknown','unknown'])
print(d4)


#Get Method

d={
    'name':'unknown',
     'age':'unknwon'
}

print(d.get('name'))
print(d.get('names'))

if d.get('name'):
    print('True')
else:
    print('False')


#Clear Method
print(d.clear())

#Copy 
d1=d.copy() #It will create a different copy but d1=d is same 
print (d1)
