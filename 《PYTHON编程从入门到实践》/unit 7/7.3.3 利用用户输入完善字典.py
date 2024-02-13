# 利用输入完善字典
# 创建一个字典
information = {}
# 提示输入并存储到字典中
while True:
    name = input("What is your name? ")
    response = input("Where do you want to go? ")
    information[name] = response
    repeat=input("Would yo like to let another respond? (yes/no) ")
    if repeat == "no":
        break
# 打印存储在字典里面的信息
for name,response in information.items():
    print(name+" want to go "+ response)
