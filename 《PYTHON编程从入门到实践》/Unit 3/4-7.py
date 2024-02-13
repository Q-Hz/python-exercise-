# append insert del pop remove
name=['eric', 'heno', 'wande']
message=" I want to invite you to have a dinner."
print(name)
print("Hello "+name[0].title()+","+message)
print("Hello "+name[1].title()+","+message)
print("Hello "+name[2].title()+","+message)
popped_name = name.pop(0)
print(popped_name.title()+" can't accept my invitation for some reasons.")
name.insert(0,'Q.HZ')
'''或者如下
add_name= "Q.Hz"
name.insert(0,add_name)
'''
print(name[0].title()+" will replace "+popped_name.title()+" and come to our banquet.")
print("Hello "+name[0].title()+","+message)
print("Hello "+name[1].title()+","+message)
print("Hello "+name[2].title()+","+message)
name.append('lala')
name.append('haha')
name.append('alapha')
print("We have found a new dinner table with more seats, so I want to invite "+str(name))
name.insert(0,'kuku')
print("We have found a new dinner table with more seats, so I want to invite "+str(name))
# 测试 append insert del pop remove
del name[0]
print(name)
name.insert(0,'kuku')
print(name)
name.append('bta')
print(str(name).title())
popped_name1=name.pop(-1)
print(str(name).title())
name.remove('haha')
print(str(name).title())
