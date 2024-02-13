# 特定名字打印特定信息
names =['admin', 'eric', 'andy', 'ademy', 'pahama']
for name in names:
    if name == 'eric':
        print("Hello "+name.title()+", would you like to see a status report?")
    else:
        print("Hello "+name.title()+", thank you for logging in again.")

# 检查列表是否为空
list_1 =[]
if list_1:
    print("We have some users.")
else:print("We need to find some users!")

# 确保用户名的独一无二(不区分大小写）
current_users = ['admin', 'eric', 'andy', 'ademy', 'pahama']
new_users = ['Candy', 'eric', 'Handy', 'andy', 'pahama']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to input another user's name.")
    else:
        print("The name " + "'"+new_user+"'" + " isn't used.")

# 当current_users内也存在大写时
current_users = ['Admin', 'eric', 'Andy', 'ademy', 'pahama']
new_users = ['Candy', 'eric', 'andy', 'Andy', 'Pahama']
current_users_lower =[i.lower() for i in current_users]  # 先让current_users和new_users中元素变成小写
new_users_lower = [i.lower() for i in new_users]
for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print("You need to input another user's name.")
    else:
        print("This name isn't used.")

# 打印列表中的数字所对应的序数
num_list =  list(range(1,10))
print(num_list)
for num in num_list:
    if num == '1':
        print("1st")
    elif num == '2':
        print("2nd")
    else:
        print(str(num)+"th")