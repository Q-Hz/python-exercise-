# 提示用户输入名字 ，并且将其名字写入到文件guest.txt中
file_name = 'guest.txt'
message = input("Enter your name ")
with open(file_name,'a') as file_object:
    file_object.write(message + '\n')