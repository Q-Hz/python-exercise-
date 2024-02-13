#  读取文件learning_python.txt
file_name = 'learning_python.txt'
# 读取整个文件
with open(file_name) as file_object:
    contents = file_object.read()
print(contents)

# 遍历整个对象
with open(file_name) as file_object:
    for line in file_object:
        print(line,end='')

# 将各行存储在一个列表中
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line,end='')