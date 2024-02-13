#切片复制
My_pizza = ['A', 'B', 'C']
firend_pizza = My_pizza[:]
print(My_pizza)
print(firend_pizza)
firend_pizza.append('D')
print(firend_pizza)
# 列表解析
print(firend_pizza[1:])

# 用循环打印
for pizza in My_pizza:
    print(pizza,end=' ')
print()
for pizza in firend_pizza:
    print(pizza,end=' ')
print('\n')
