# 将remember_me.py 的功能重构为几个函数
import json
import os  # 需要导入 os 模块

def get_stored_username(file_name):
    """如果存储了用户名，就获取它"""
    if os.path.exists(file_name):  # 检查文件是否存在
        with open(file_name) as f_obj:
            try:
                username = json.load(f_obj)  # 尝试读取 JSON 数据(文件为空或者不包含有效的 JSON 数据时引发异常）
            except json.JSONDecodeError:  # 捕获 JSONDecodeError 异常
                return None  # 如果文件中没有无数据，返回None
            else:
                return username
    else:
        return None  # 如果文件不存在，返回 None
'''
    # 当文件不为空且不包含有效json数据时会崩溃
    if os.path.exists(file_name) and os.path.getsize(file_name) >0:
        with open(file_name) as f_obj:
        username = json.load(f_obj)
        return username
    else:
        return None
'''
def get_new_username(file_name):
    """提示用户输入用户名"""
    username = input("What is your name? ")
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user(file_name):
    """问候用户，并指出其名字"""
    username = get_stored_username(file_name)
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(file_name)
        print("We'll remember you when you come back, " + username + "!")  # 使用新用户名

# 调用上述函数
file_name = 'username.json'
greet_user(file_name)
