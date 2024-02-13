# 9 创建一个名单列表，传递到函数里面，并且打印
def magician_name_list(magician_list):
    for magician in magician_list:
        print(magician)


magician_list = ['A', 'B', 'C']
magician_name_list(magician_list)



# 10 在原来列表的每个元素后面都加上‘the great’
def make_great(magician_list):
    great_magician_list = []
    for magician in magician_list:
        great_magician = magician+' the great'
        great_magician_list.append(great_magician)
    print("great magician list: ",end=' ')
    for great_magician in great_magician_list:
        print(great_magician,end=' ')

magician_list = ['A', 'B', 'C']
make_great(magician_list)

# 10 用完第二个函数之后，再重新调用第一个名单的函数

def magician_name_list(magician_list):
    '''展示名单'''
    for magician in magician_list:
        print(magician)
def make_great(magician_list):
    '''在每个元素后面加上 the great'''
    for magician in magician_list:
        great_magician = magician+' the great'
        great_magician_list.append(great_magician)
    print("great magician list: ",end=' ')
    for great_magician in great_magician_list:
        print(great_magician,end=' ')

magician_list = ['A', 'B', 'C']
great_magician_list = []
make_great(magician_list)
magician_name_list(magician_list)
magician_name_list(great_magician_list)