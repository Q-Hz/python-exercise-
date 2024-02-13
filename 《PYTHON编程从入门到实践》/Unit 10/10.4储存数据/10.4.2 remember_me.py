# 写入一个用户名到一个json文件
import json
username = input("What is your name? ")
file_name = 'username.json'
with open(file_name,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, " + username + " !")