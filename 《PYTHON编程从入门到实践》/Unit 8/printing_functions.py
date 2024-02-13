# 作为15-17的导入函数
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