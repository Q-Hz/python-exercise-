# 以User为父类 Admin为子类 并在子类补充属性和方法
class User():
    """
    创建一个User类
    两个属性：first_name 和last_name
    两个方法：describe_user() 和 greet_use()
    """
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def describe_ser(self):
        """打印用户信息摘要"""
        full_name = self.first_name + ' ' + self.last_name
        print("The user's name is "+full_name)


    def greet_user(self):
        """问候用户"""
        full_name = self.first_name + ' ' + self.last_name
        print("Hello "+full_name)

# 建立Admin类，作为User的子类
class Admin(User):
    def __init__(self, first_name, last_name):
        """
        初始化父类属性
        初始化子类属性privileges 用于存储字符串
        """
        super().__init__(first_name,last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示管理员权限"""
        print("Admin ",end='')
        for privilege in self.privileges:
            print(privilege,end=',')

# 创建一个实例
admin_1 = Admin('Q.', 'Hz')
admin_1.show_privileges()