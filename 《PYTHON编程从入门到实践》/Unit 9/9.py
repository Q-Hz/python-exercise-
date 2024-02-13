# 更新电池容量

#建立一个Car类
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

# 建立一个Battery类
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size = 70):
        """初始化点电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car  has a "+str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full range"
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

# 建立一个子类ELectricCar 并且将上述的类Battery用于该类的属性
class ElectircCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化子类的属性(将类Battery用于该子类的属性）"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectircCar('Tesla', 'model s', 2016)
# 检查电池容量
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# 升级电池容量
my_tesla.battery.upgrade_battery()
# 再次检查电池容量
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()