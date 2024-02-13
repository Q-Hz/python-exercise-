# 打开文件，读取内容
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    print(contents)
# 绝对文档路径 (某些地方要使用双反斜杠//）
file = 'D:\Program Files\python exercise\\Unit 10\\10.1\pi_digits.txt'
with open(file) as file_object:
    contents  = file_object.read()
    print(contents)


# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    file_object.seek(0)
    for line in file_object:
        print(line,end='')


# 创建一个包含文件各行内容的列表
file_name ='pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
# 按照文档形式输出
for line in lines:
    print(line,end='')
# 都在一行输出
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


# 打开包含一百万位的大文件
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:50] + '...')
print(len(pi_string))


# 检查生日是否包含在圆周率里面
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")