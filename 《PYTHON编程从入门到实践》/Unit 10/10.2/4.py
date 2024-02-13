# 提示用户输入名字 ，打印问候语，并且将其名字写入到文件guest_book.txt中
file_name = 'guest_book.txt'
while True:
    guest = input("Enter your name \nEnter 'q' to quit the programme. ")
    if guest == 'q':
        break
    else:
        print("Hello, " + guest.title())
        with open(file_name,'a') as file_object:
            file_object.write(guest+"\n")