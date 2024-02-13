# 条件测试
car = 'Tesla'
print("Is car == 'Tesla'? I predict Ture.")
print(car == 'Tesla')
print("Is car == 'Audi'? I predict False")
print(car == 'Audi')

# 更多的测试1
char_a = 'A'
char_b = 'B'
if char_a == char_b:
    print("char_a == char b")
else:
    print("char_a != char_b")

# 更多的测试2 lower()
char_a = "A"
char_b = "a"
if char_a.lower() == char_b.lower():
    print("char_a.lower() == char_b.lower()")
else:
    print("char_a.lower() != char_b.lower()")

# 更多的测试3
num_1 = 1
num_2 = 2
if num_1 == num_2:
    print("num_1 == num_2")
elif num_1 >= num_2:
    print("num_1 >= num_2")
elif num_1 <= num_2:
    print("num_1 <= num_2")
elif num_1 > num_2:
    print("num_1 > num_2")
elif num_1 < num_2:
    print("num_1 < num_2")

# 更多的测试3'
num_1 = 1
num_2 = 2
if num_1 == num_2:
    print("num_1 == num_2")
if num_1 >= num_2:
    print("num_1 >= num_2")
if num_1 <= num_2:
    print("num_1 <= num_2")
if num_1 > num_2:
    print("num_1 > num_2")
if num_1 < num_2:
    print("num_1 < num_2")
# 3'与3不同：多个if 都会执行 而使用elif时，当其中一个为Ture时，剩下的不再执行。

# 更多的测试4 and or
num_1 = 1
num_2 = 2
test_num = 3
if num_1 >= 1 and num_2 >= test_num:
    print("num_1 and num_2 >= " + str(test_num))
else:
    print("num_1 or num_2 < " + str(test_num))
if num_1 >= 1 and num_2 >= test_num:
    print("num_1 or num_2 >= " + str(test_num))
else:
    print("num_1 and num_2 < " + str(test_num))

# 更多的测试5 列表中是否含特定值
num = 0
list_1 = ['haha', 'kuku']
name = 'haha'
for test_list in list_1:
    if test_list == name:
        num = 1
if num :
    print("'haha' is in the list_1")
else:
    print("'haha' is not in the list_1")


