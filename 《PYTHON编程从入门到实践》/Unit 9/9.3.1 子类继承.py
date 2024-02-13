# 对Car类的继承
class Car():
    '''一次模拟汽车的描述的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print("This car has "+ str(self.odometer_reading)+ " miles on it.")

class EletricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
my_tesla =EletricCar('Tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())