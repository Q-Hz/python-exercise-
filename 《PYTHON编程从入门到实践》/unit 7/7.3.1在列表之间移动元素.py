# 在列表之间移动元素
# 创建一个未验证用户的列表和一个已验证用户的列表
unconfirmed_users =['alice','handy','lucy']
confirmed_users =[]
# 将未验证用户移动到已验证用户列表
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(current_user)
    confirmed_users.append(current_user)
print("confirm_users: ",end='')
# 打印已验证用户列表的名单
for confirmed_user in confirmed_users:
    print(confirmed_user,end=' ')
