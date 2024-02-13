#  三明治制作名单——>完成列表
# 创建两个列表
sandwich_orders =['tuna sandwich', 'salmon sandwich', 'meat floss sandwich']
finished_sandwiches =[]
# 利用循环转移列表元素
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your "+current_sandwich)
    finished_sandwiches.append(current_sandwich)
# 检查finishided_sandwiches 列表中的元素
print("Here are the finished sandwich list: ",end='')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich,end='、')


# 删除列表中的某种元素
sandwich_orders =['tuna sandwich', 'salmon sandwich','pastrami', 'meat floss sandwich','pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich_order in sandwich_orders:
    print(sandwich_order)