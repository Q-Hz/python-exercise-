# 网址中存储每一个用户的信息， 每一个用户包含姓、名和住址三个信息
users ={
    'einstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'mcuire',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print("username is "+username,end='')
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print(", "+full_name+" located in "+location)