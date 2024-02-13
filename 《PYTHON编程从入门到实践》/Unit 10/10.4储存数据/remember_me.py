# 练习写入和读取json文件
import json
# 如果以前存了用户名，就加载
# 否则，就提示用户输入用户名并存储它
file_name = 'username.json'
try:
    with open(file_name) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(file_name) as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back " + username + "!")