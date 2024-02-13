# 编写一个程序，询问用户为什么喜欢Python，原因存到一个文档reason_love_programme.txt
file_name = 'reason_love_programme'
while True:
    reason = input("Why you love programming?\nEnter 'q' to quit the programming. ")
    if reason == 'q':
        break
    else:
        print("Ok, I know  that one of the reasons is " + reason + " Please continue.")
        with open(file_name,'a') as file_object:
            file_object.write(reason + '\n')