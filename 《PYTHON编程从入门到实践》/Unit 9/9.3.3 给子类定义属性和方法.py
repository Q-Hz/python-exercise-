# 创建一个Car类 定义子类Electric_car的属性和方法
class Car():
    """一次模拟汽车的描述的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
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

    def update_odometer(self, mileage):
        """修改里程"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """递增里程"""
        self.odometer_reading += miles


# 建立子类EletricCar, 给子类Electric_Car 定义属性和方法
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化子类的特有属性
        """
        super().__init__(make, model,year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")


my_tesla = ElectricCar('Tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
