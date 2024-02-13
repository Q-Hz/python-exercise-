# 创建一个Privileges类 该类储存了一个属性和一个方法
# 创建一个Admin类（是User的子类），该类以Privileges类的实例为属性
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


class Privileges():
    """该类的属性存储管理员特权（来自类Admin)，方法可以打印管理员特权的信息"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privilege(self):
        """打印管理员特权的信息"""
        print("The admin's privileges include: ",end='')
        for privilege in self.privileges:
            print(privilege,end=',')

# 建立Admin类，作为User的子类,将Privilege类作为其属性
class Admin(User):
    def __init__(self, first_name, last_name):
        """
        初始化父类属性
        初始化子类属性privileges 用于存储字符串
        """
        super().__init__(first_name,last_name)
        self.privileges = Privileges()



admin_1 = Admin('Q.', 'Hz')
admin_1.privileges.show_privilege()



