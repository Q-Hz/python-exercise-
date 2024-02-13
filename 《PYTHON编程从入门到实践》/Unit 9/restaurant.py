# 修改类的属性值
class Restaurant():
    def __init__(self, restaurant_name, restaurant_type_):
        """两个属性"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type_
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆名和餐馆的类型"""
        print("The restaurant's name is "+self.restaurant_name)
        print("The restaurant's type is "+self.restaurant_type)

    def open_restaurant(self):
        """打印一条信息 """
        print("This restaurant is opening.")

    def show_number_served(self):
        """打印显示目前餐馆人数的信息"""
        print("The number of people is " + str(self.number_served))

    def update_number_served(self,number):
        """修改目前餐馆的人数"""
        self.number_served = number

    def increment_number_served(self,number):
        """递增餐馆人数"""
        self.number_served += number


# 方法一,直接修改属性的值
my_restaurant = Restaurant('Xiao Zhi Restaurant', 'chinoiserie')
my_restaurant.show_number_served()
my_restaurant.number_served = 9
my_restaurant.show_number_served()

# 方法二，通过方法修改属性的值
my_restaurant.update_number_served(10)
my_restaurant.show_number_served()

# 方法三，用递增法修改属性的值
my_restaurant.increment_number_served(10)
my_restaurant.show_number_served()