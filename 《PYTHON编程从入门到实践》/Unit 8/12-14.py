# 12 任意数量的实参
def sandwich_toppings(*toppings):
    for topping in toppings:
        print(topping)


sandwich_toppings('A','B','C')
sandwich_toppings('A')
sandwich_toppings('B', 'A')

# 14 输入姓名和个人信息，利用函数整合
def build_profile(first_name,last_name,**information):
    '''整合个人信息'''
    person_profile = {}
    person_profile['first'] = first_name
    person_profile['last'] = last_name
    for key,value in information.items():
        person_profile[key] = value
    return  person_profile


profile = build_profile('Q.', 'Hz', city=' gd', hometown= 'sd', profession= 'student')
print(profile)
# 13
full_name = profile['first'] + ' ' + profile['last']
print(full_name)