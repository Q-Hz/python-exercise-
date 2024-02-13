# 传递任意数量的实参
def make_pizza (*toppings):
    print("Making a Pizza with the following toppings: ")
    for topping in toppings:
        print("- "+topping)


make_pizza('mushrooms')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def bulid_profile(first,last,**user_information):
    """输入姓名，信息，并且放入一个字典"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_information.items():
        profile[key] = value
    return profile


user_profile = bulid_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)