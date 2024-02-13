# 以Restaurant为父类 IceCreamStand为子类，并在子类补充一个属性和方法
class Restaurant():
    def __init__(self,restaurant_name, restaurant_type):
        '''两个属性'''
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    # 两个方法
    def describe_restaurant(self):
        """打印餐馆名字和类型的信息"""
        print("The restaurant's name is "+self.restaurant_name)
        print("The restaurant's type is "+self.restaurant_type)

    def open_restaurant(self):
        print("This restaurant is opening.")

class IceCreamStand(Restaurant):
    """作为 Restaurant的子类"""
    def __init__(self, restaurant_name, restaurant_type):
        """
        初始化父类属性
        添加一个子类属性，用于储存风味
        """
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = ['chocolate', 'strawberry', 'vanilla']

    def show_icecream_flavors(self):
        """展示冰淇淋风味"""
        print("Our Icecream have ", end='' )
        for flavor in self.flavors:
            print(flavor,end=' ')
        print("flavors")


# 实例
icecream = IceCreamStand('xiaozhi', 'chinoiserie')
icecream.show_icecream_flavors()
