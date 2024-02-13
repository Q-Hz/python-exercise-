# 位置实参（基于实参位置关联形参）
def descripted_pets(animal_type,animal_name):
    """形参为：宠物类型，宠物名字"""
    print("The type of the animal is "+animal_type.title())
    print("Its name is "+animal_name.title())
    print()
descripted_pets('hamster','harry')
descripted_pets('dog','andy')

# 关键字实参
def descriped_pets(animal_type,animal_name):
    """实参：宠物类型，宠物名字"""
    print("The animal's type is "+animal_type)
    print("The animal's name is "+animal_name)
descriped_pets(animal_name='lucy',animal_type='haamster')

# 默认值
def descriped_pets(animal_name,animal_type='dog'):
    """实参；宠物名字，宠物类型"""
    print("The animal's name is "+animal_name.title())
    print("The animal's type is "+animal_type.title())
descriped_pets('lucy')
descriped_pets('kuku','duck')