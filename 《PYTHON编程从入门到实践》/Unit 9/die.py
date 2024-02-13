# 创建一个Die类
class Die():
    """
    属性sides，默认值为6
    方法roll_die，打印一个随机数
    """
    def __init__(self,x):
        self.side = 6
        self.x= x

    def roll_side(self):
        if 1 <= self.x <= self.side:
            print("The number is "+str(self.x))