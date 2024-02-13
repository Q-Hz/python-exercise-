#从 user模块 调用 User类并 建立priviles 和 admin 类
from user import User
class Privileges():
    """该类的属性存储管理员特权（来自类Admin)，方法可以打印管理员特权的信息"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privilege(self):
        """打印管理员特权的信息"""
        print("The admin's privileges include: ",end='')
        for privilege in self.privileges:
            print(privilege,end=',')
class Admin(User):
    def __init__(self, first_name, last_name):
        """
        初始化父类属性
        初始化子类属性privileges 用于存储字符串
        """
        super().__init__(first_name,last_name)
        self.privileges = Privileges()