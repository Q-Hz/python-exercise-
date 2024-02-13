# 输入quit退出，其它继续
prompt = "Please tell me which car do you want to cent."
prompt += "Enter 'quit' and you will end the program."
while True:
    message = input(prompt)
    if message != 'quit':
        print("Let me see if I can find a "+message+" .")
    else:
        break

# 超过8人，打印指出没有空桌，少于则有，quit退出
prompt = "How many people do you have?"
prompt += "\nEnter 'quit' or the number of people much than 10, you will end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    elif  int(message) <= 8:
        print("OK, we have a spare table for "+str(message)+" people.")
    elif int(message) > 8:
        print("Sorry, we couldn't have a spare table for "+str(message)+" people.")

# 指出一个数字，观察是否为10的整数倍
prompt = "input a number and I will tell you if a multiple of 10."
prompt += "\nEnter 'quit' and you will end the program."
while True:
    message = input(prompt)
    if message == 'quit':
        break
    elif int(message) % 10 == 0:
        multiple = int(message) / 10
        print("This number is the multiple of 10, and it is " + str(multiple) + " times of 10.")
    else:
        print("The number isn't the multiple of 10.")