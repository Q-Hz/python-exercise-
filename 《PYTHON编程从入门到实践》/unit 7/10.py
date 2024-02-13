# 调差用户的度假胜地
resorts = {}
# 利用循环输入完善字典
active = True
while active:
    name = input("What is your name? ")
    resort = input("Where is your favourite resort? ")
    resorts[name] = resort
    active = input("Would you like to let another resort? (yes/no) ")
    if active =='yes':
        active = True
    elif active == 'no':
        active = False
# 输出字典内容
for name,resort in resorts.items():
    print(name+"'s favourite resort is "+resort)