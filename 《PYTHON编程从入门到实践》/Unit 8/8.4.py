# 向函数传递列表，向列表中的每个元素进行问候
def greet_user(user_list):
    """向列表中的每个元素问候"""
    for user in user_list:
        print("Hello "+user.title()+"!")


users = ['amy','andy','Q.Hz']
print(greet_user(users))


# 8.4.1 创建两个函数，一个用于打印已有的模型列表。另一个用于展示已经打印的模型
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计之后，都将其移动到completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟打印
        print("print model: "+current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的模型"""
    print("The following models have been printed:")
    for completed_model in  completed_models:
        print(completed_model)


unprinted_designs = ['ipone case','robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
'''
如果用“unprinted_designs[:]” 代替“unprinted_designs” 
可以创建副本，不修改原来的列表
'''
show_completed_models(completed_models)