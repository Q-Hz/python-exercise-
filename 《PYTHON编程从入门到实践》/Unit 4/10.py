# 切片
ifms = ['the', 'first', 'three', 'items', 'in', 'the', 'lines', 'are', ':']
for ifm in ifms:
    print(str(ifm),  end=' ')
print()

# 打印前三个元素
start_ifms = ifms[:3]
for start_ifm in start_ifms:
    print(start_ifm,end=' ')
print()
# 打印后三个元素
end_ifms = ifms[-3:]
for end_ifm in end_ifms:
    print(end_ifm,end=' ')


