# 创建一个Car类 练习修改类中属性的值
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

# 调用Car类的get_descriptive_name方法
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
# 显示汽车初始里程
my_new_car.read_odometer()

# 修改类的属性
# 一、直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 二、通过方法修改属性的值
class Car():
    '''一次模拟汽车的描述的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """返回整洁的信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print("This car has "+ str(self.odometer_reading)+ " miles on it.")

    def update_odometer(self,message):
        """将里程修改为特定的值"""
        if message >= self.odometer_reading:
            self.odometer_reading = message
        else:
            print("You can't roll backa an odometer!")
my_new_car = Car('audi', 'a4', '2016')
my_new_car.update_odometer(22)
my_new_car.read_odometer()

# 三、通过方法对属性的值进行递增
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

    def update_odometer(self,miles):
        """将里程增加为特定的值"""
        self.odometer_reading +=miles
my_new_car = Car('audi', 'a4', '2016')
my_new_car.update_odometer(10)
my_new_car.read_odometer()