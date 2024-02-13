# 提示用户输入喜欢的数字，存储到一个json文件
# 读取上述json文件并且进行打印

# 存储一个数字
import json

favourite_number = input("What is your favourite number? ")
file_name = 'favourite_number.json'
with open(file_name, 'w') as f_obj:
    json.dump(favourite_number, f_obj)

# 打印该数字
with open(file_name) as f_obj:
    f_num = json.load(f_obj)
print(f_num)