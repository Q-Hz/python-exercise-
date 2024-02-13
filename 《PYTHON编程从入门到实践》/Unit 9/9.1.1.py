# 创建一个Dog类 两个属性：name 和 age 两个方法：分别打印不同的信息
class Dog():
    """模拟小狗行为"""
    def __init__(self,name,age):
        """初始化属性name 和 age"""
        self.name = name
        self.age = age


    def sit(self):
        """模拟小狗被命令时坐下"""
        print(self.name.title() + " is now sitting")


    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " is now rolled over!")


# 访问上述Dog类的属性
my_dog = Dog('KUKU',3)
print("My dog's name is "+ my_dog.name)
print("It's age is "+str(my_dog.age))

# 访问上述Dog类的方法
your_dog = Dog('hensy', 4)
your_dog.sit()
your_dog.roll_over()