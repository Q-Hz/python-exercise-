# 替换文件内容
file_name = 'learning_python.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line,end='')
print()

# 用C 替换 Python
for line in lines:
    line = line.replace('python', 'C')  # 大写
    line = line.replace('Python', 'C')  # 小写
    print(line,end='')