for value in range(1, 21):
    print(value)
for value in range(1, 1000001):
    print(value)

# 创建一个列表，打印最大值，最小值以及求和
num = list(range(1,1000001))
print((max(num)))
print((min(num)))
sum_num = sum(num)
print(sum_num)

#打印1-20内的奇数
num = list(range(1,21,2))
print(num)
#或者
for num in range(1,21,2):
    print(num)

# 打印3-30内能被3整除的数字
for num in range(3,31,3):
    print(num)

# 打印1-10这十个数的立方
for num in range(1,11):
    print(num)
    square_num = num**3
    print('square is '+str(square_num))
# 列表解析（缩减代码行数）
squares = [value**3 for value in range(1,11)]
print(squares)