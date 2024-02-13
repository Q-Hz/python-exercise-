# 给pizza加配料，每添加一种配料都在后面显示
prompt = "Please int the Pizza ingredient."
prompt += "Enter 'quit' to end the program."
ingredient =[]
while True:
    message= input(prompt)
    ingredient.append(message)
    if message == 'quit':
        break
    else:
        print("Ok, I will put",end=' ')
        for ingre in ingredient:
            print(ingre,end=' ')
        print("into the Pizza.")

# 票价 不到3岁 free； 3-12岁 10dollars；超过12岁 15dollars
prompt = "How old are you?"
prompt +="Enter 'quit' to end the program."
while True:
    age = input(prompt)
    if str(age) == 'quit':
        break
    elif int(age) <3:
        print("Your age is less than 3 years old, thus you are free.")
    elif int(age) <=12:
        print("Age range from 3 to 12 is 10 dollars.")
    else:
        print("Age over 12 years old will take 15 dollars.")