# 用字典储存一个人的信息
information ={'first_name':'Q','last_name':'Hz','age':'18','city':'guangdong'}
print(information['first_name'])
print(information['last_name'])
print(information['age'])
print(information['city'])

# 用字典存储每个人对应的数字
information_num={'crazy':'1','candy':'2','landy':'3','hansy':'4','dery':'5'}
print("candy's number is "+information_num['candy'])
print("crazy's number is "+information_num['crazy'])

# 字典，存储某些词的意思
vocabulary={
    'file':'a collection of information stored together in a computer, under a particular name',
    'bit':'the smallest unit of information used by a computer',
    'array':'a way of organizing and storing related data in a computer memory',
    'compiler':'a person who compiles sth',
    'constant':'a number or quantity that does not vary',
    }
print("file means "+vocabulary['file'])
print("bit means "+vocabulary['bit'])
del vocabulary['file']
print("file means "+vocabulary['file']) # 删除后不能再显示

# 利用循环打印字典的键-值对
vocabulary={
    'file':'a collection of information stored together in a computer, under a particular name',
    'bit':'the smallest unit of information used by a computer',
    'array':'a way of organizing and storing related data in a computer memory',
    'compiler':'a person who compiles sth',
    'constant':'a number or quantity that does not vary',
    'byte':' unit of information stored in a computer, equal to 8 bits .',
    'bit':'he smallest unit of information used by a computer',
    'binary':'using only 0 and 1 as a system of numbers',
    'desktop':'the background of a computer screen that shows icons of the programs that are available',
    'chipset':'a group of microchips designed to perform one or more related functions as a unit,',
    }
for n,mean in vocabulary.items():
    print(n,end=': ')
    print(mean)
