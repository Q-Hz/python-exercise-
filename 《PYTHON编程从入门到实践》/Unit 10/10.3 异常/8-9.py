# 打印文件中文档信息
def show_pets_name(file_name):
    """打印文件中动物的名字 """
    try:
        with open(file_name) as f_boj:
            contents = f_boj.read()
    except FileNotFoundError:
        print("Sorry, " + file_name + " can't be found.")
    else:
        print(contents)


pet_file_list = ['cats.txt', 'dogs.txt']
for file in pet_file_list:
    show_pets_name(file)


# 当发生FileNotFound错误时不报错
def show_pets_name(file_name):
    """打印文件中动物的名字 """
    try:
        with open(file_name) as f_boj:
            contents = f_boj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


pet_file_list = ['cats.txt', 'dogs.txt']
for file in pet_file_list:
    show_pets_name(file)