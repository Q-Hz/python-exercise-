# 用附加模式写入
file_name = 'programming.txt'
with open(file_name,'a') as file_object:
    file_object.write("I also love C.\n ")