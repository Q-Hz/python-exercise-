# 写入文件
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")

with open(file_name, 'a') as file_object:
    file_object.write("I really love programming.\n")