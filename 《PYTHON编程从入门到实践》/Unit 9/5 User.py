# 登录次数的修改
class User():
    """
    创建一个User类
    两个属性：first_name 和last_name
    两个方法：describe_user() 和 greet_use()
    """
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_ser(self):
        """打印用户信息摘要"""
        full_name = self.first_name + ' ' + self.last_name
        print("The user's name is "+full_name)

    def greet_user(self):
        """问候用户"""
        full_name = self.first_name + ' ' + self.last_name
        print("Hello "+full_name)

    def increment_login_attempts(self):
        """将属性login_attempts的值加一"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将属性login_attempts的值归零"""
        self.login_attempts = 0


user_1 = User('Q.', 'Hz')
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)