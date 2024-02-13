# 提示用户输入喜欢的数字，存储到一个json文件
# 读取上述json文件并且进行打印

import json
import os

file_name = 'favourite_number.json'
try:
    if os.path.getsize(file_name) > 0:  # 检查文件是否为空
        with open(file_name) as f_obj:
            f_num = json.load(f_obj)
    else:
        raise FileNotFoundError # 当文件为空时，用raise 引发异常
except FileNotFoundError:  # 文件没有建立时或者文件为空
    favourite_number = input("What is your favourite number? ")
    with open(file_name, 'w') as f_obj:
        json.dump(favourite_number, f_obj)
        print("We'll remember your favourite number.")
else:  # 文件建立时
            print("Your favourite number is " + f_num + " .")
