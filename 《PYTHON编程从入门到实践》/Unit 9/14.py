# 调用python库 random模块里的函数
from random import randint
# 调用Die 类，方法roll_die可以打印随机数1-6
from die import Die
i = 1
while i<=10 :
    x = randint(1,6)
    number = Die(x)
    number.roll_side()
    i += 1