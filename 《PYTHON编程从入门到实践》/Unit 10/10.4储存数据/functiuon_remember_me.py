# 将remember_me.py 的功能重构成一个函数
import json
def greet_user():
    """问候用户，并指出其名字"""
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(file_name, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back," + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()