# if-else 结构
alien_color = 'green'
if alien_color == 'green':
    print("You have gotten 5 points")
else:
    print("You have gotten 10 points")

# if-elif-else 结构
alien_color = 'green'
if alien_color == 'green':
    print("You have gotten 5 points")
elif alien_color == 'yellow':
    print("You have gotten 10 points")
elif alien_color == 'red':
    print("You have gotten 15 points")

# if-elif-else 结构
age = 20
if age < 2:
    print("He is a infant.")
elif age<4:
     print("He is toddling.")
elif age < 13:
    print("He is a child.")
elif age < 20:
    print("He is a teenager.")
elif age< 65:
    print("He is a adult.")
else:
    print("He is an elder.")

# 列表中执行if语句
fruit = ['apple', 'pineapple', 'watermelon']
for fruit_1 in fruit:
    if fruit_1 == 'watermelon':
        print("You really like watermelon!")
    if fruit_1 == 'pineapple':
        print("You really like pineapple!")
        