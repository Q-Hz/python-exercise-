
class User():
    """
    创建一个User类
    两个属性：first_name 和last_name
    两个方法：describe_user() 和 greet_use()
    """
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def describe_user(self):
        """打印用户信息摘要"""
        full_name = self.first_name + ' ' + self.last_name
        print("The user's name is "+full_name)


    def greet_user(self):
        """问候用户"""
        full_name = self.first_name + ' ' + self.last_name
        print("Hello "+full_name)