# 打印1-10内的偶数
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        print(current_number)
    else:
        continue