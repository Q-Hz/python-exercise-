'''
设置一个 Restaurant类，
两个属性：restaurant_name 和 restaurant_type
两个方法: describe_restaurant() 和 open_restaurant()
'''
class Restaurant():
    def __init__(self,restaurant_name, restaurant_type_):
        '''两个属性'''
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type_

    # 两个方法
    def describe_restaurant(self):
        """打印餐馆名字和类型的信息"""
        print("The restaurant's name is "+self.restaurant_name)
        print("The restaurant's type is "+self.restaurant_type)

    def open_restaurant(self):
        print("This restaurant is opening.")


# 访问 Restaurant类的两个属性
my_restaurant=Restaurant("Q.Hz's Restaurant", "chinoiserie")
print("The restaurant's name is "+my_restaurant.restaurant_name)
print("The restaurant's type is "+my_restaurant.restaurant_type)

# 访问 Restaurant类的两个方法
your_restaurant = Restaurant('delicious', 'European type')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
